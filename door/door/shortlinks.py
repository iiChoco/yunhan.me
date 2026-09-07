"""Temporary public redirects, created and managed by signed-in accounts.

SQLite makes name allocation atomic across workers. Expiration is checked on
every lookup, independent of cleanup or process restarts. Retired names stay
reserved forever: an old shared URL must never acquire a new destination.
"""

from __future__ import annotations

import json
import os
import re
import secrets
import sqlite3
import time
from contextlib import closing
from pathlib import Path
from typing import Any

from yarl import URL

MAX_LIFETIME = 86400
RESERVED = {'password', 'pdf', 'json', 'url', 'text', 'timer', 'image', 'convert', 'qr', 'color'} | {"api", "admin", "login", "logout", "toolbox", "tools", "healthz", "utilities", "vendor", "private", "public", "portfolio", "projects", "about", "contact", "assets", "instrument", "home"}


def destination(value: Any) -> str:
    if not isinstance(value, str) or not value or len(value) > 4096:
        raise ValueError("Enter a URL of at most 4,096 characters.")
    if any(ord(c) < 33 or ord(c) == 127 or c == "\\" for c in value):
        raise ValueError("The URL contains spaces or invalid characters.")
    try:
        url = URL(value)
        if url.scheme not in {"http", "https"} or not url.host or url.user is not None or url.password is not None:
            raise ValueError()
        _ = url.port
    except (ValueError, UnicodeError):
        raise ValueError("Use a full http:// or https:// URL without a username or password.") from None
    return str(url)


class ShortLinks:
    def __init__(self, path: Path, public: Path) -> None:
        self.path = path
        self.public = public

    def initialize(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        fd = os.open(self.path, os.O_CREAT | os.O_RDWR, 0o600)
        os.close(fd)
        os.chmod(self.path, 0o600)
        with closing(sqlite3.connect(self.path)) as db, db:
            db.execute("CREATE TABLE IF NOT EXISTS links (slug TEXT PRIMARY KEY, owner TEXT, destination TEXT, created_at INTEGER NOT NULL, expires_at INTEGER NOT NULL)")
            db.execute("CREATE INDEX IF NOT EXISTS links_owner ON links(owner)")
            db.execute("CREATE INDEX IF NOT EXISTS links_expiry ON links(expires_at)")

    @staticmethod
    def _retire(db: sqlite3.Connection, now: int) -> None:
        db.execute("UPDATE links SET destination = NULL, owner = NULL WHERE expires_at <= ? AND destination IS NOT NULL", (now,))

    def create(self, owner: str, target: str, lifetime: Any) -> dict[str, Any]:
        target = destination(target)
        if type(lifetime) is not int or not 1 <= lifetime <= MAX_LIFETIME:
            raise ValueError("Expiration must be between 1 second and 24 hours.")
        words = [word for word in json.loads((self.public / "vendor/words.json").read_text())
                 if re.fullmatch(r"[a-z]{3,12}", word) and word not in RESERVED
                 and not (self.public / word).exists() and not (self.public / f"{word}.html").exists()]
        if not words:
            raise RuntimeError("No link names are available.")
        with closing(sqlite3.connect(self.path, timeout=10)) as db, db:
            db.execute("BEGIN IMMEDIATE")
            now = int(time.time())
            self._retire(db, now)
            if db.execute("SELECT count(*) FROM links WHERE owner = ?", (owner,)).fetchone()[0] >= 50:
                raise ValueError("You have 50 active links. Expire one before creating another.")
            for attempt in range(256):
                # Prefer one word; expand the space as single words are used up.
                slug = "-".join(secrets.choice(words) for _ in range(1 + attempt // 64))
                try:
                    db.execute("INSERT INTO links VALUES (?, ?, ?, ?, ?)", (slug, owner, target, now, now + lifetime))
                except sqlite3.IntegrityError:
                    continue
                return {"slug": slug, "path": f"/{slug}", "destination": target, "created_at": now, "expires_at": now + lifetime}
        raise RuntimeError("Could not allocate a link name. Try again.")

    def list(self, owner: str) -> list[dict[str, Any]]:
        with closing(sqlite3.connect(self.path, timeout=10)) as db, db:
            self._retire(db, int(time.time()))
            db.row_factory = sqlite3.Row
            return [{**dict(row), "path": f"/{row['slug']}"} for row in db.execute(
                "SELECT slug, destination, created_at, expires_at FROM links WHERE owner = ? ORDER BY created_at DESC, slug", (owner,))]

    def revoke(self, owner: str, slug: str) -> bool:
        with closing(sqlite3.connect(self.path, timeout=10)) as db, db:
            return db.execute("UPDATE links SET destination = NULL, owner = NULL, expires_at = ? WHERE slug = ? AND owner = ?",
                              (int(time.time()), slug, owner)).rowcount > 0

    def resolve(self, slug: str) -> tuple[bool, str | None]:
        with closing(sqlite3.connect(self.path, timeout=10)) as db:
            row = db.execute("SELECT destination, expires_at FROM links WHERE slug = ?", (slug,)).fetchone()
        if row is None:
            return False, None
        return True, row[0] if row[1] > time.time() else None
