"""The door as an aiohttp application.

Three jobs on one port, told apart by hostname and path:

* **auth** — ``/api/login``, ``/api/logout``, ``/api/me``, ``/api/password``,
  and the owner's ``/api/admin/accounts/…``; a login page at ``/`` and an
  admin page at ``/admin``.
* **store** — ``/api/store/<app>/<key>``: one small JSON document per user,
  app, and key, as a flat file. What a static page keeps across devices.
* **sites** — a hostname listed under ``[sites]`` is served straight from a
  directory: index files, no trailing slashes, a 404 page if the site has
  one. This is how math.yunhan.me lives on the same box.

Cross-origin callers are the listed origins only, with credentials; any
other Origin on an unsafe method is refused outright, which is the CSRF
rule. The cookie is HttpOnly, SameSite=Lax, Secure whenever the request
arrived over TLS (the tunnel says so in X-Forwarded-Proto).
"""

from __future__ import annotations

import asyncio
import json
import logging
import mimetypes
import os
import re
import time
from collections import deque
from pathlib import Path
from typing import Any

from aiohttp import web

from door.accounts import (
    USERNAME, Account, Accounts, atomic_write, check_password, mint_secret,
    read_cookie, sign_cookie,
)
from door.config import Config

log = logging.getLogger("door")

KEY = re.compile(r"^[a-z0-9][a-z0-9_.-]{0,63}$")
"""App and key names: boring, because they name files."""

STATIC_DENY = {".DS_Store", "staticwebapp.config.json"}
MAX_FAILURES = 8
FAILURE_WINDOW = 600.0


def fail(status: int, error: str, reason: str) -> web.Response:
    return web.json_response({"error": error, "reason": reason}, status=status)


class Door:
    def __init__(self, cfg: Config) -> None:
        self.cfg = cfg
        self.accounts = Accounts(cfg.accounts_file)
        self.secret = ""
        self.attempts: dict[str, deque[float]] = {}
        self.pages = Path(__file__).parent / "pages"

    # ── app ──────────────────────────────────────────────────────────────────

    def make_app(self) -> web.Application:
        app = web.Application(
            middlewares=[self._sites_mw, self._cors_mw],
            client_max_size=self.cfg.store_max_bytes + 4096,
        )
        r = app.router
        r.add_get("/", self._page_login)
        r.add_get("/admin", self._page_admin)
        r.add_get("/instrument.css", self._instrument_css)
        r.add_get("/healthz", self._healthz)
        r.add_post("/api/login", self._login)
        r.add_post("/api/logout", self._logout)
        r.add_get("/api/me", self._me)
        r.add_post("/api/password", self._password)
        r.add_get("/api/store/{app}", self._store_list)
        r.add_get("/api/store/{app}/{key}", self._store_get)
        r.add_put("/api/store/{app}/{key}", self._store_put)
        r.add_delete("/api/store/{app}/{key}", self._store_delete)
        r.add_get("/api/admin/accounts", self._admin_list)
        r.add_post("/api/admin/accounts", self._admin_create)
        r.add_post("/api/admin/accounts/{u}/reset", self._admin_reset)
        r.add_post("/api/admin/accounts/{u}/disable", self._admin_disable)
        r.add_post("/api/admin/accounts/{u}/enable", self._admin_enable)
        r.add_delete("/api/admin/accounts/{u}", self._admin_delete)
        app.on_startup.append(self._startup)
        return app

    async def _startup(self, app: web.Application) -> None:
        self.cfg.dir.mkdir(parents=True, exist_ok=True)
        try:
            os.chmod(self.cfg.dir, 0o700)
        except OSError:
            pass
        self.secret = mint_secret(self.cfg.secret_file)
        n = len(self.accounts.list())
        log.info(
            "door open on %s:%d — %d account%s, cookie %s on %r, %d site%s: %s",
            self.cfg.bind, self.cfg.port, n, "" if n == 1 else "s",
            self.cfg.cookie_name, self.cfg.cookie_domain or "(host)",
            len(self.cfg.sites), "" if len(self.cfg.sites) == 1 else "s",
            ", ".join(self.cfg.sites) or "none",
        )

    # ── middleware ───────────────────────────────────────────────────────────

    @staticmethod
    def _hostname(request: web.Request) -> str:
        return (request.headers.get("X-Forwarded-Host") or request.host or "").split(":")[0].lower()

    @staticmethod
    def _secure(request: web.Request) -> bool:
        forwarded = request.headers.get("X-Forwarded-Proto", "")
        return request.secure or forwarded.split(",")[0].strip() == "https"

    def _own_origin(self, request: web.Request) -> str:
        scheme = "https" if self._secure(request) else request.scheme
        host = request.headers.get("X-Forwarded-Host") or request.host
        return f"{scheme}://{host}"

    def _origin_allowed(self, request: web.Request, origin: str) -> bool:
        return origin in self.cfg.origins or origin == self._own_origin(request)

    @web.middleware
    async def _sites_mw(self, request: web.Request, handler: Any) -> web.StreamResponse:
        root = self.cfg.sites.get(self._hostname(request))
        if root is not None:
            return await self._static(request, root)
        return await handler(request)

    @web.middleware
    async def _cors_mw(self, request: web.Request, handler: Any) -> web.StreamResponse:
        origin = request.headers.get("Origin", "")
        allowed = bool(origin) and self._origin_allowed(request, origin)
        if request.method == "OPTIONS" and "Access-Control-Request-Method" in request.headers:
            if not allowed:
                return fail(403, "forbidden", "origin not allowed")
            return web.Response(status=204, headers=self._cors_headers(origin, preflight=True))
        if origin and not allowed and request.method not in ("GET", "HEAD", "OPTIONS"):
            return fail(403, "forbidden", "origin not allowed")
        response = await handler(request)
        if allowed:
            response.headers.update(self._cors_headers(origin))
        return response

    @staticmethod
    def _cors_headers(origin: str, preflight: bool = False) -> dict[str, str]:
        h = {
            "Access-Control-Allow-Origin": origin,
            "Access-Control-Allow-Credentials": "true",
            "Vary": "Origin",
        }
        if preflight:
            h["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
            h["Access-Control-Allow-Headers"] = "Content-Type"
            h["Access-Control-Max-Age"] = "600"
        return h

    # ── static sites ─────────────────────────────────────────────────────────

    async def _static(self, request: web.Request, root: Path) -> web.StreamResponse:
        if request.method not in ("GET", "HEAD"):
            return web.Response(status=405, text="Method not allowed", headers={"Allow": "GET, HEAD"})
        path = request.path
        if len(path) > 1 and path.endswith("/"):
            qs = f"?{request.query_string}" if request.query_string else ""
            raise web.HTTPMovedPermanently(location=path.rstrip("/") + qs)
        root = root.resolve()
        rel = path.lstrip("/")
        parts = [p for p in rel.split("/") if p]
        if any(p.startswith(".") or p in STATIC_DENY for p in parts):
            return await self._not_found(root)
        target = root.joinpath(*parts) if parts else root
        try:
            target = target.resolve()
        except OSError:
            return await self._not_found(root)
        if target != root and root not in target.parents:
            return await self._not_found(root)
        candidates = [target, target / "index.html"]
        if not target.suffix:
            candidates.append(target.with_name(target.name + ".html"))
        for c in candidates:
            if c.is_file():
                ctype, _ = mimetypes.guess_type(str(c))
                if ctype and ctype.startswith("text/") or ctype in ("application/json", "application/javascript", "image/svg+xml"):
                    ctype = f"{ctype}; charset=utf-8"
                headers = {
                    "Cache-Control": "public, max-age=300",
                    "X-Content-Type-Options": "nosniff",
                    "Referrer-Policy": "strict-origin-when-cross-origin",
                }
                if ctype:
                    headers["Content-Type"] = ctype
                return web.FileResponse(c, headers=headers)
        return await self._not_found(root)

    @staticmethod
    async def _not_found(root: Path) -> web.Response:
        page = root / "404.html"
        if page.is_file():
            return web.Response(status=404, body=page.read_bytes(), content_type="text/html", charset="utf-8",
                                headers={"Cache-Control": "no-store"})
        return web.Response(status=404, text="Not found", headers={"Cache-Control": "no-store"})

    # ── pages ────────────────────────────────────────────────────────────────

    def _page(self, name: str) -> web.Response:
        html = (self.pages / name).read_text(encoding="utf-8").replace("{{SITE}}", self.cfg.site)
        return web.Response(text=html, content_type="text/html", charset="utf-8",
                            headers={"Cache-Control": "no-store", "X-Content-Type-Options": "nosniff"})

    async def _page_login(self, request: web.Request) -> web.Response:
        return self._page("login.html")

    async def _page_admin(self, request: web.Request) -> web.Response:
        return self._page("admin.html")

    async def _instrument_css(self, request: web.Request) -> web.StreamResponse:
        path = self.cfg.instrument / "instrument.css"
        if not path.is_file():
            return web.Response(status=404, text="no instrument.css")
        return web.FileResponse(path, headers={"Content-Type": "text/css; charset=utf-8", "Cache-Control": "public, max-age=300"})

    async def _healthz(self, request: web.Request) -> web.Response:
        return web.json_response({"ok": True, "accounts": len(self.accounts.list())})

    # ── auth ─────────────────────────────────────────────────────────────────

    async def _body(self, request: web.Request) -> dict[str, Any]:
        if not request.content_type.startswith("application/json"):
            raise web.HTTPUnsupportedMediaType(text=json.dumps({"error": "bad_content_type", "reason": "send JSON"}), content_type="application/json")
        try:
            body = await request.json()
        except ValueError:
            raise web.HTTPBadRequest(text=json.dumps({"error": "bad_json", "reason": "body is not JSON"}), content_type="application/json")
        return body if isinstance(body, dict) else {}

    @staticmethod
    def _peer(request: web.Request) -> str:
        cf = request.headers.get("CF-Connecting-IP")
        if cf:
            return cf
        fwd = request.headers.get("X-Forwarded-For", "")
        if fwd:
            return fwd.split(",")[0].strip()
        return request.remote or "?"

    def _limited(self, key: str, now: float) -> bool:
        q = self.attempts.get(key)
        if not q:
            return False
        while q and now - q[0] > FAILURE_WINDOW:
            q.popleft()
        return len(q) >= MAX_FAILURES

    def _note_failure(self, key: str, now: float) -> None:
        self.attempts.setdefault(key, deque()).append(now)

    def _user(self, request: web.Request) -> Account | None:
        raw = request.cookies.get(self.cfg.cookie_name)
        if not raw or not self.secret:
            return None
        username = read_cookie(self.secret, raw)
        if username is None:
            return None
        account = self.accounts.get(username)
        if account is None or account.disabled:
            return None
        return account

    def _require(self, request: web.Request, *, admin: bool = False) -> Account:
        account = self._user(request)
        if account is None:
            raise web.HTTPUnauthorized(text=json.dumps({"error": "unauthorized", "reason": "sign in"}), content_type="application/json")
        if admin and not account.is_admin:
            raise web.HTTPForbidden(text=json.dumps({"error": "forbidden", "reason": "owner only"}), content_type="application/json")
        return account

    def _set_cookie(self, response: web.Response, request: web.Request, username: str) -> None:
        expires = time.time() + self.cfg.cookie_days * 86400
        kw: dict[str, Any] = dict(
            max_age=self.cfg.cookie_days * 86400, path="/", httponly=True,
            samesite="Lax", secure=self._secure(request),
        )
        if self.cfg.cookie_domain:
            kw["domain"] = self.cfg.cookie_domain
        response.set_cookie(self.cfg.cookie_name, sign_cookie(self.secret, username, expires), **kw)

    def _clear_cookie(self, response: web.Response) -> None:
        kw: dict[str, Any] = dict(path="/")
        if self.cfg.cookie_domain:
            kw["domain"] = self.cfg.cookie_domain
        response.del_cookie(self.cfg.cookie_name, **kw)

    @staticmethod
    def _me_payload(account: Account) -> dict[str, Any]:
        return {"username": account.username, "role": account.role, "admin": account.is_admin}

    async def _login(self, request: web.Request) -> web.Response:
        body = await self._body(request)
        username = str(body.get("username", "")).strip().lower()
        password = str(body.get("password", ""))
        now = time.time()
        peer = self._peer(request)
        if self._limited(f"ip:{peer}", now) or (username and self._limited(f"user:{username}", now)):
            return fail(429, "too_many_attempts", "try again in a few minutes")
        account = None
        if USERNAME.match(username) and password:
            account = await asyncio.to_thread(self.accounts.verify, username, password)
        if account is None:
            self._note_failure(f"ip:{peer}", now)
            if username:
                self._note_failure(f"user:{username}", now)
            log.info("login refused for %r from %s", username, peer)
            return fail(401, "bad_login", "wrong username or password")
        self.accounts.touch(account.username)
        response = web.json_response(self._me_payload(account))
        self._set_cookie(response, request, account.username)
        log.info("login: %s from %s", account.username, peer)
        return response

    async def _logout(self, request: web.Request) -> web.Response:
        response = web.json_response({"ok": True})
        self._clear_cookie(response)
        return response

    async def _me(self, request: web.Request) -> web.Response:
        account = self._user(request)
        if account is None:
            return fail(401, "unauthorized", "sign in")
        return web.json_response(self._me_payload(account), headers={"Cache-Control": "no-store"})

    async def _password(self, request: web.Request) -> web.Response:
        account = self._require(request)
        body = await self._body(request)
        current = str(body.get("current", ""))
        new = str(body.get("new", ""))
        if await asyncio.to_thread(self.accounts.verify, account.username, current) is None:
            return fail(401, "bad_login", "current password is wrong")
        try:
            check_password(new)
        except ValueError as exc:
            return fail(400, "bad_password", str(exc))
        self.accounts.reset(account.username, new)
        response = web.json_response({"ok": True})
        self._set_cookie(response, request, account.username)
        return response

    # ── store ────────────────────────────────────────────────────────────────

    def _store_dir(self, username: str, app: str) -> Path:
        return self.cfg.users_dir / username / app

    def _names(self, request: web.Request) -> tuple[str, str]:
        app = request.match_info.get("app", "")
        key = request.match_info.get("key", "")
        if not KEY.match(app) or (key and not KEY.match(key)):
            raise web.HTTPBadRequest(text=json.dumps({"error": "bad_name", "reason": "app and key: lowercase, digits, . _ -"}), content_type="application/json")
        return app, key

    async def _store_list(self, request: web.Request) -> web.Response:
        account = self._require(request)
        app, _ = self._names(request)
        d = self._store_dir(account.username, app)
        items = []
        if d.is_dir():
            for p in sorted(d.glob("*.json")):
                st = p.stat()
                items.append({"key": p.stem, "size": st.st_size, "updated": int(st.st_mtime)})
        return web.json_response({"app": app, "keys": items}, headers={"Cache-Control": "no-store"})

    async def _store_get(self, request: web.Request) -> web.Response:
        account = self._require(request)
        app, key = self._names(request)
        p = self._store_dir(account.username, app) / f"{key}.json"
        if not p.is_file():
            return fail(404, "not_found", "no such key")
        return web.Response(body=p.read_bytes(), content_type="application/json", charset="utf-8",
                            headers={"Cache-Control": "no-store", "X-Updated": str(int(p.stat().st_mtime))})

    async def _store_put(self, request: web.Request) -> web.Response:
        account = self._require(request)
        app, key = self._names(request)
        raw = await request.read()
        if len(raw) > self.cfg.store_max_bytes:
            return fail(413, "too_large", f"at most {self.cfg.store_max_bytes} bytes")
        try:
            text = raw.decode("utf-8")
            json.loads(text)
        except (UnicodeDecodeError, ValueError):
            return fail(400, "bad_json", "body is not JSON")
        p = self._store_dir(account.username, app) / f"{key}.json"
        await asyncio.to_thread(atomic_write, p, text)
        return web.json_response({"ok": True, "app": app, "key": key, "updated": int(time.time()), "size": len(raw)})

    async def _store_delete(self, request: web.Request) -> web.Response:
        account = self._require(request)
        app, key = self._names(request)
        p = self._store_dir(account.username, app) / f"{key}.json"
        try:
            p.unlink()
        except FileNotFoundError:
            return fail(404, "not_found", "no such key")
        return web.json_response({"ok": True})

    # ── admin ────────────────────────────────────────────────────────────────

    def _target(self, request: web.Request) -> str:
        u = request.match_info.get("u", "")
        if not USERNAME.match(u):
            raise web.HTTPBadRequest(text=json.dumps({"error": "bad_username", "reason": "no such account"}), content_type="application/json")
        return u

    async def _admin_list(self, request: web.Request) -> web.Response:
        self._require(request, admin=True)
        return web.json_response({"accounts": [a.public() for a in self.accounts.list()]}, headers={"Cache-Control": "no-store"})

    async def _admin_create(self, request: web.Request) -> web.Response:
        self._require(request, admin=True)
        body = await self._body(request)
        username = str(body.get("username", "")).strip().lower()
        role = str(body.get("role", "user"))
        try:
            password = self.accounts.create(username, role)
        except ValueError as exc:
            return fail(400, "bad_request", str(exc))
        log.info("account created: %s (%s)", username, role)
        acct = self.accounts.get(username)
        return web.json_response({"account": acct.public() if acct else None, "password": password})

    async def _admin_reset(self, request: web.Request) -> web.Response:
        self._require(request, admin=True)
        u = self._target(request)
        try:
            password = self.accounts.reset(u)
        except KeyError:
            return fail(404, "not_found", "no such account")
        log.info("password reset: %s", u)
        return web.json_response({"username": u, "password": password})

    async def _set_disabled(self, request: web.Request, disabled: bool) -> web.Response:
        me = self._require(request, admin=True)
        u = self._target(request)
        if disabled and u == me.username:
            return fail(400, "bad_request", "you can't disable yourself")
        try:
            acct = self.accounts.set_disabled(u, disabled)
        except KeyError:
            return fail(404, "not_found", "no such account")
        log.info("account %s: %s", "disabled" if disabled else "enabled", u)
        return web.json_response({"account": acct.public()})

    async def _admin_disable(self, request: web.Request) -> web.Response:
        return await self._set_disabled(request, True)

    async def _admin_enable(self, request: web.Request) -> web.Response:
        return await self._set_disabled(request, False)

    async def _admin_delete(self, request: web.Request) -> web.Response:
        me = self._require(request, admin=True)
        u = self._target(request)
        if u == me.username:
            return fail(400, "bad_request", "you can't delete yourself")
        try:
            self.accounts.delete(u)
        except KeyError:
            return fail(404, "not_found", "no such account")
        log.info("account deleted: %s", u)
        return web.json_response({"ok": True})


def serve(cfg: Config) -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")
    door = Door(cfg)
    web.run_app(door.make_app(), host=cfg.bind, port=cfg.port, access_log=None, print=None)
