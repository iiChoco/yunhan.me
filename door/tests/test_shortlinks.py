"""Public short links expire on the server; only their creator can manage them."""
from __future__ import annotations

import asyncio
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from aiohttp import CookieJar
from aiohttp.test_utils import TestClient, TestServer

from door.app import Door
from door.config import Config

HOME = Path(__file__).resolve().parents[2] / "home"
PASSWORD = "short-links-test-only"


class ShortLinkAccess(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.cfg = Config(dir=Path(self.temp.name), site="127.0.0.1", home=HOME)
        self.door = Door(self.cfg)
        self.client = TestClient(TestServer(self.door.make_app()), cookie_jar=CookieJar(unsafe=True))
        await self.client.start_server()
        self.addAsyncCleanup(self.client.close)
        for username in ("alice", "bob"):
            self.door.accounts.create(username, password=PASSWORD)

    async def login(self, username: str = "alice") -> None:
        response = await self.client.post("/api/login", json={"username": username, "password": PASSWORD})
        self.assertEqual(response.status, 200)

    async def create(self, **values: object) -> dict:
        response = await self.client.post("/api/links", json={"destination": "https://example.com/path?a=1&b=2#section", **values})
        self.assertEqual(response.status, 201)
        self.assertEqual(response.headers["Cache-Control"], "private, no-store")
        return await response.json()

    async def test_creation_management_require_auth_and_allowed_origin(self) -> None:
        for method, path in (("GET", "/api/links"), ("POST", "/api/links"), ("DELETE", "/api/links/word")):
            response = await self.client.request(method, path, json={})
            self.assertEqual(response.status, 401)
            self.assertIn("no-store", response.headers["Cache-Control"])
        await self.login()
        response = await self.client.post("/api/links", json={"destination": "https://example.com"}, headers={"Origin": "https://evil.example"})
        self.assertEqual(response.status, 403)
        self.assertEqual((await self.client.get("/api/links", headers={"Host": "auth.yunhan.me"})).status, 404)
        self.door.accounts.set_disabled("alice", True)
        self.assertEqual((await self.client.get("/api/links")).status, 401)

    async def test_default_is_24_hours_and_public_redirect_preserves_url(self) -> None:
        await self.login()
        link = await self.create()
        self.assertEqual(link["expires_at"] - link["created_at"], 86400)
        self.assertRegex(link["path"], r"^/[a-z]+$")
        await self.client.post("/api/logout", json={})
        for method in ("GET", "HEAD"):
            response = await self.client.request(method, link["path"], allow_redirects=False, headers={"If-None-Match": "*"})
            self.assertEqual(response.status, 302)
            self.assertEqual(response.headers["Location"], link["destination"])
            self.assertEqual(response.headers["Cache-Control"], "no-store")
        self.assertEqual((await self.client.post(link["path"], allow_redirects=False)).status, 405)
        self.assertEqual((await self.client.get(link["path"], headers={"Host": "auth.yunhan.me"}, allow_redirects=False)).status, 404)

    async def test_expiration_is_checked_at_boundary_without_cleanup(self) -> None:
        await self.login()
        link = await self.create(expires_in=60)
        self.assertEqual(link["expires_at"] - link["created_at"], 60)
        with patch("door.shortlinks.time.time", return_value=link["expires_at"]):
            for method in ("GET", "HEAD"):
                response = await self.client.request(method, link["path"], allow_redirects=False)
                self.assertEqual(response.status, 410)
                self.assertNotIn("Location", response.headers)
                self.assertIn("no-store", response.headers["Cache-Control"])
            self.assertEqual((await (await self.client.get("/api/links")).json())["links"], [])
        with sqlite3.connect(self.cfg.dir / "shortlinks.sqlite3") as db:
            self.assertEqual(db.execute("SELECT destination, owner FROM links WHERE slug = ?", (link["slug"],)).fetchone(), (None, None))
        with patch("door.shortlinks.secrets.choice", return_value=link["slug"]):
            replacement = await self.create()
        self.assertNotEqual(replacement["slug"], link["slug"])
        self.assertEqual((await self.client.get(link["path"], allow_redirects=False)).status, 410)

    async def test_list_and_revocation_are_owned_and_persist_across_restart(self) -> None:
        await self.login()
        link = await self.create()
        await self.login("bob")
        self.assertEqual((await (await self.client.get("/api/links")).json())["links"], [])
        self.assertEqual((await self.client.delete(f"/api/links/{link['slug']}")).status, 404)
        other = TestClient(TestServer(Door(self.cfg).make_app()), cookie_jar=CookieJar(unsafe=True))
        await other.start_server()
        self.addAsyncCleanup(other.close)
        self.assertEqual((await other.get(link["path"], allow_redirects=False)).status, 302)
        await other.post("/api/login", json={"username": "alice", "password": PASSWORD})
        self.assertEqual(len((await (await other.get("/api/links")).json())["links"]), 1)
        self.assertEqual((await other.delete(f"/api/links/{link['slug']}")).status, 200)
        self.assertEqual((await self.client.get(link["path"], allow_redirects=False)).status, 410)
        self.assertEqual((self.cfg.dir / "shortlinks.sqlite3").stat().st_mode & 0o777, 0o600)

    async def test_bad_urls_and_lifetimes_are_rejected_server_side(self) -> None:
        await self.login()
        for target in ("", "javascript:alert(1)", "data:text/html,test", "//example.com", "https://a:b@example.com", "https://example.com\\evil", "https://example.com/\r\nLocation:x", "https://example.com:abc", "https://", 123):
            response = await self.client.post("/api/links", json={"destination": target})
            self.assertEqual(response.status, 400, repr(target))
        for expiry in (0, -1, 86401, 1.5, True, "60", None):
            response = await self.client.post("/api/links", json={"destination": "https://example.com", "expires_in": expiry})
            self.assertEqual(response.status, 400, repr(expiry))
        self.assertEqual((await (await self.client.get("/api/links")).json())["links"], [])

    async def test_concurrent_creations_allocate_distinct_names_and_limit_active_links(self) -> None:
        await self.login()
        responses = await asyncio.gather(*(self.client.post("/api/links", json={"destination": f"https://example.com/{n}"}) for n in range(8)))
        self.assertTrue(all(response.status == 201 for response in responses))
        data = [await response.json() for response in responses]
        self.assertEqual(len({link["slug"] for link in data}), 8)
        now = data[0]["created_at"]
        with sqlite3.connect(self.cfg.dir / "shortlinks.sqlite3") as db:
            db.executemany("INSERT INTO links VALUES (?, 'alice', 'https://example.com', ?, ?)", [(f"fixture-{n}", now, now + 86400) for n in range(42)])
        self.assertEqual((await self.client.post("/api/links", json={"destination": "https://example.com"})).status, 400)
