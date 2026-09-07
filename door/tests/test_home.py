"""The public landing and private Toolbox share Door without sharing access.

These checks use temporary accounts and an in-process server. Direct static
aliases cannot reveal Toolbox, and the same session that signs into Door must
pass the gate before any private page bytes or conditional response are sent.
"""

from __future__ import annotations

import asyncio
import tempfile
import time
import unittest
from pathlib import Path

from aiohttp import CookieJar
from aiohttp.test_utils import TestClient, TestServer
from yarl import URL

from door.accounts import sign_cookie
from door.app import Door, UTILITY_PAGES, UTILITY_PATHS
from door.config import Config, load

HOME = Path(__file__).resolve().parents[2] / "home"
PASSWORD = "only-a-test-password"


class HomeAccess(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.cfg = Config(dir=Path(self.temp.name), site="127.0.0.1", home=HOME,
                          sites={"math.localhost": HOME / "public"})
        self.door = Door(self.cfg)
        self.client = TestClient(TestServer(self.door.make_app()), cookie_jar=CookieJar(unsafe=True))
        await self.client.start_server()
        self.addAsyncCleanup(self.client.close)
        self.door.accounts.create("reader", password=PASSWORD)

    async def login(self, **kwargs: object) -> None:
        response = await self.client.post("/api/login", json={"username": "reader", "password": PASSWORD}, **kwargs)
        self.assertEqual(response.status, 200)

    async def test_landing_assets_and_login_are_public(self) -> None:
        for path in ("/", "/home.css?v=6", "/instrument.css", "/login?next=/toolbox"):
            with self.subTest(path=path):
                response = await self.client.get(path)
                self.assertEqual(response.status, 200)
        self.assertIn("Yunhan", await (await self.client.get("/")).text())

    async def test_anonymous_toolbox_redirects_without_private_content(self) -> None:
        for path in ("/toolbox", "/toolbox/", "/toolbox?anything=1"):
            for method in ("GET", "HEAD"):
                with self.subTest(path=path, method=method):
                    response = await self.client.request(method, path, allow_redirects=False)
                    self.assertEqual(response.status, 302)
                    self.assertEqual(response.headers["Location"], "/login?next=/toolbox")
                    self.assertIn("no-store", response.headers["Cache-Control"])
                    self.assertNotIn("<title>Toolbox", await response.text())

    async def test_static_aliases_never_expose_toolbox(self) -> None:
        paths = ("/toolbox/index.html", "/toolbox.html", "/private/toolbox.html",
                 "/%70rivate/toolbox.html", "/%2e%2e/private/toolbox.html", "//toolbox/index.html")
        for path in paths:
            with self.subTest(path=path):
                url = URL(str(self.client.make_url("/"))[:-1] + path, encoded=True)
                response = await self.client.session.get(url, allow_redirects=False)
                self.assertEqual(response.status, 404)
                self.assertNotIn("<title>Toolbox", await response.text())

    async def test_door_login_unlocks_toolbox_without_cacheable_content(self) -> None:
        await self.login()
        response = await self.client.get("/toolbox", headers={"Origin": str(self.client.make_url("/"))[:-1]})
        self.assertEqual(response.status, 200)
        self.assertIn("<title>Toolbox", await response.text())
        self.assertEqual(response.headers["Cache-Control"], "private, no-store")
        self.assertIn("Cookie", response.headers["Vary"])
        self.assertIn("Origin", response.headers["Vary"])
        response = await self.client.head("/toolbox")
        self.assertEqual(response.status, 200)
        self.assertEqual(await response.read(), b"")

    async def test_existing_auth_host_session_works_at_home(self) -> None:
        self.cfg.site = "yunhan.me"
        self.cfg.cookie_domain = ".yunhan.me"
        response = await self.client.post("/api/login", json={"username": "reader", "password": PASSWORD},
                                          headers={"Host": "auth.yunhan.me", "X-Forwarded-Proto": "https"})
        self.assertEqual(response.status, 200)
        cookie = response.cookies[self.cfg.cookie_name]
        self.assertEqual(cookie["domain"], ".yunhan.me")
        self.assertTrue(cookie["secure"])
        self.assertTrue(cookie["httponly"])
        # Emulate the browser forwarding the shared-domain cookie to the apex.
        response = await self.client.get("/toolbox", headers={"Host": "yunhan.me", "Cookie": f"yh_session={cookie.value}"})
        self.assertEqual(response.status, 200)
        self.assertEqual((await self.client.get("/", headers={"Host": "auth.yunhan.me"})).status, 200)

    async def test_logout_revokes_browser_access(self) -> None:
        await self.login()
        self.assertEqual((await self.client.post("/api/logout", json={})).status, 200)
        self.assertEqual((await self.client.get("/toolbox", allow_redirects=False)).status, 302)

    async def test_invalid_expired_disabled_and_deleted_sessions_are_rejected(self) -> None:
        for cookie in ("forged", sign_cookie(self.door.secret, "reader", time.time() - 60)):
            response = await self.client.get("/toolbox", headers={"Cookie": f"yh_session={cookie}"}, allow_redirects=False)
            self.assertEqual(response.status, 302)
        await self.login()
        self.door.accounts.set_disabled("reader", True)
        self.assertEqual((await self.client.get("/toolbox", allow_redirects=False)).status, 302)
        self.door.accounts.delete("reader")
        self.assertEqual((await self.client.get("/toolbox", allow_redirects=False)).status, 302)

    async def test_conditionals_cannot_skip_authentication(self) -> None:
        response = await self.client.get("/toolbox", headers={"If-None-Match": "*", "If-Modified-Since": "Wed, 01 Jan 2099 00:00:00 GMT", "Range": "bytes=0-100"}, allow_redirects=False)
        self.assertEqual(response.status, 302)

    async def test_cross_origin_login_remains_forbidden(self) -> None:
        response = await self.client.post("/api/login", json={"username": "reader", "password": PASSWORD}, headers={"Origin": "https://untrusted.example"})
        self.assertEqual(response.status, 403)
        self.assertEqual((await self.client.get("/toolbox", allow_redirects=False)).status, 302)

    async def test_math_stays_static_and_admin_stays_on_auth_host(self) -> None:
        self.assertEqual((await self.client.get("/", headers={"Host": "math.localhost"})).status, 200)
        self.assertEqual((await self.client.get("/toolbox", headers={"Host": "math.localhost"})).status, 404)
        self.assertEqual((await self.client.get("/api/admin/accounts")).status, 404)
        response = await self.client.get("/admin", allow_redirects=False)
        self.assertEqual(response.status, 302)
        self.assertEqual(response.headers["Location"], "https://auth.127.0.0.1/admin")

    async def test_utilities_require_auth_and_preserve_the_return_path(self) -> None:
        for slug in UTILITY_PAGES:
            response = await self.client.get(f"/tools/{slug}", allow_redirects=False)
            self.assertEqual(response.status, 302)
            self.assertEqual(response.headers["Location"], f"/login?next=/tools/{slug}")
            self.assertIn("no-store", response.headers["Cache-Control"])
        await self.login()
        for slug in UTILITY_PAGES:
            response = await self.client.get(f"/tools/{slug}")
            self.assertEqual(response.status, 200)
            self.assertEqual(response.headers["Cache-Control"], "private, no-store")
            self.assertIn('main class="utility"', await response.text())
        await self.client.post("/api/logout", json={})
        self.assertEqual((await self.client.get("/tools/qr-code", allow_redirects=False)).status, 302)

    async def test_utility_files_have_no_public_aliases(self) -> None:
        for slug in UTILITY_PAGES:
            for path in (f"/private/utilities/{slug}.html", f"/utilities/{slug}.html", f"/tools/{slug}.html"):
                self.assertEqual((await self.client.get(path, allow_redirects=False)).status, 404)
        self.assertEqual((await self.client.get("/tools/unknown")).status, 404)
        self.assertEqual((await self.client.get("/tools/qr-code", headers={"Host": "math.localhost"})).status, 404)

    async def test_favorites_require_active_account_and_are_never_cached(self) -> None:
        for method, path in (("GET", "/api/store/toolbox-favorites"),
                             ("GET", "/api/store/toolbox-favorites/ciel"),
                             ("PUT", "/api/store/toolbox-favorites/ciel"),
                             ("DELETE", "/api/store/toolbox-favorites/ciel")):
            response = await self.client.request(method, path, json={})
            self.assertEqual(response.status, 401)
            self.assertEqual(response.headers["Cache-Control"], "private, no-store")
        await self.login()
        self.door.accounts.set_disabled("reader", True)
        self.assertEqual((await self.client.get("/api/store/toolbox-favorites")).status, 401)
        self.assertFalse((self.cfg.users_dir / "reader" / "toolbox-favorites").exists())

    async def test_favorites_are_isolated_by_account_and_survive_server_restart(self) -> None:
        await self.login()
        base = "/api/store/toolbox-favorites"
        responses = await asyncio.gather(*(self.client.put(f"{base}/{key}", json={}) for key in ("ciel", "qr-code")))
        self.assertTrue(all(response.status == 200 for response in responses))
        await self.client.post("/api/logout", json={})
        self.door.accounts.create("second", password=PASSWORD)
        await self.client.post("/api/login", json={"username": "second", "password": PASSWORD})
        self.assertEqual((await (await self.client.get(base)).json())["keys"], [])
        self.assertEqual((await self.client.get(f"{base}/ciel")).status, 404)
        self.assertEqual((await self.client.delete(f"{base}/ciel")).status, 404)
        self.assertEqual((await self.client.put(f"{base}/math", json={})).status, 200)
        # A new server and browser session read the same saved account data.
        other = TestClient(TestServer(Door(self.cfg).make_app()), cookie_jar=CookieJar(unsafe=True))
        await other.start_server()
        self.addAsyncCleanup(other.close)
        await other.post("/api/login", json={"username": "reader", "password": PASSWORD})
        response = await other.get(base)
        self.assertEqual(response.headers["Cache-Control"], "private, no-store")
        self.assertEqual([item["key"] for item in (await response.json())["keys"]], ["ciel", "qr-code"])
        self.assertEqual((await other.delete(f"{base}/ciel")).status, 200)
        self.assertEqual([item["key"] for item in (await (await other.get(base)).json())["keys"]], ["qr-code"])
        self.assertEqual([item["key"] for item in (await (await self.client.get(base)).json())["keys"]], ["math"])

    async def test_favorites_preserve_origin_and_path_checks(self) -> None:
        await self.login()
        base = "/api/store/toolbox-favorites"
        for method in ("PUT", "DELETE"):
            response = await self.client.request(method, f"{base}/ciel", json={}, headers={"Origin": "https://untrusted.example"})
            self.assertEqual(response.status, 403)
            self.assertIn("no-store", response.headers["Cache-Control"])
        response = await self.client.put(f"{base}/ciel", json={}, headers={"Origin": str(self.client.make_url("/"))[:-1]})
        self.assertEqual(response.status, 200)
        self.assertIn("Origin", response.headers["Vary"])
        self.assertEqual((await self.client.put(f"{base}/INVALID", json={})).status, 400)
        self.assertEqual((await self.client.put(f"{base}/math", data="invalid")).status, 400)
        self.assertEqual((await self.client.get("/api/store/unrelated")).status, 404)
        self.assertEqual((await self.client.get("/api/store/toolbox-favorites-extra")).status, 404)

    async def test_tools_host_short_routes_share_login_and_protect_every_page(self) -> None:
        self.cfg.site = "yunhan.me"
        self.cfg.cookie_domain = ".yunhan.me"
        headers = {"Host": "tools.yunhan.me", "X-Forwarded-Proto": "https"}
        for short in UTILITY_PATHS:
            for suffix in ("", "/"):
                response = await self.client.get(f"/{short}{suffix}", headers=headers, allow_redirects=False)
                self.assertEqual(response.status, 302)
                self.assertEqual(response.headers["Location"], f"/login?next=/{short}")
                self.assertIn("no-store", response.headers["Cache-Control"])
        response = await self.client.post("/api/login", json={"username": "reader", "password": PASSWORD},
                                          headers={"Host": "auth.yunhan.me", "X-Forwarded-Proto": "https"})
        cookie = response.cookies[self.cfg.cookie_name]
        self.assertEqual(cookie["domain"], ".yunhan.me")
        self.assertTrue(cookie["secure"])
        signed = {**headers, "Cookie": f"yh_session={cookie.value}"}
        for short in UTILITY_PATHS:
            response = await self.client.get(f"/{short}", headers=signed)
            self.assertEqual(response.status, 200)
            html = await response.text()
            self.assertIn('href="https://yunhan.me/toolbox"', html)
            self.assertIn(f'https://tools.yunhan.me/{short}', html)
            self.assertNotIn("{{", html)
            self.assertEqual(response.headers["Cache-Control"], "private, no-store")
        response = await self.client.get("/toolbox", headers={**signed, "Host": "yunhan.me"})
        html = await response.text()
        for short in UTILITY_PATHS:
            self.assertIn(f'href="https://tools.yunhan.me/{short}"', html)
        self.assertIn('href="https://math.yunhan.me/zetamac"', html)
        for path in ("/admin", "/api/admin/accounts", "/qr.html", "/private/utilities/qr-code.html", "/utilities/qr-code.html"):
            self.assertEqual((await self.client.get(path, headers=signed, allow_redirects=False)).status, 404)
        self.door.accounts.set_disabled("reader", True)
        self.assertEqual((await self.client.get("/qr", headers=signed, allow_redirects=False)).status, 302)

    async def test_old_tool_urls_redirect_and_tools_assets_remain_available(self) -> None:
        self.cfg.site = "yunhan.me"
        for short, slug in UTILITY_PATHS.items():
            response = await self.client.get(f"/tools/{slug}", headers={"Host": "yunhan.me"}, allow_redirects=False)
            self.assertEqual(response.status, 302)
            self.assertEqual(response.headers["Location"], f"https://tools.yunhan.me/{short}")
        for path in ("/", "/toolbox"):
            response = await self.client.get(path, headers={"Host": "tools.yunhan.me"}, allow_redirects=False)
            self.assertEqual(response.headers["Location"], "https://yunhan.me/toolbox")
        for path in ("/instrument.css", "/home.css", "/utilities/common.js", "/vendor/qrcode.js"):
            self.assertEqual((await self.client.get(path, headers={"Host": "tools.yunhan.me"})).status, 200)

    async def test_tools_host_url_api_is_scoped_and_redirects_stay_on_apex(self) -> None:
        self.cfg.site = "yunhan.me"
        await self.login()
        headers = {"Host": "tools.yunhan.me", "Origin": "https://tools.yunhan.me", "X-Forwarded-Proto": "https"}
        response = await self.client.post("/api/links", json={"destination": "https://example.com", "expires_in": 60}, headers=headers)
        self.assertEqual(response.status, 201)
        self.assertEqual(response.headers["Cache-Control"], "private, no-store")
        link = await response.json()
        response = await self.client.get("/api/links", headers=headers)
        self.assertEqual(len((await response.json())["links"]), 1)
        self.assertEqual((await self.client.get(link["path"], headers={"Host": "tools.yunhan.me"}, allow_redirects=False)).status, 404)
        self.assertEqual((await self.client.get(link["path"], headers={"Host": "yunhan.me"}, allow_redirects=False)).status, 302)
        response = await self.client.post("/api/links", json={"destination": "https://example.com"}, headers={**headers, "Origin": "https://evil.example"})
        self.assertEqual(response.status, 403)

    async def test_home_directory_is_configurable(self) -> None:
        config = Path(self.temp.name) / "test.toml"
        config.write_text(f'home = "{HOME}"\n')
        self.assertEqual(load(config).home, HOME)


if __name__ == "__main__":
    unittest.main()
