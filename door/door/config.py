"""The door's configuration: one TOML file, a few keys.

    dir = "~/.door"                     # accounts.json, secret, users/<u>/<app>/<key>.json
    bind = "127.0.0.1"                  # the tailnet address in production
    port = 8770
    site = "yunhan.me"                  # the parent domain: ?next= may only point inside it
    cookie_name = "yh_session"
    cookie_domain = ".yunhan.me"        # empty = host-only (loopback dev)
    cookie_days = 30
    origins = ["https://math.yunhan.me"]   # cross-origin callers of the API
    instrument = "~/yunhan.me/instrument"  # where instrument.css is served from
    store_max_bytes = 262144
    [sites]
    "math.yunhan.me" = "~/yunhan.me/math/public"
"""

from __future__ import annotations

import os
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

DEFAULT_PATH = Path.home() / ".door" / "config.toml"


@dataclass
class Config:
    dir: Path = field(default_factory=lambda: Path.home() / ".door")
    bind: str = "127.0.0.1"
    port: int = 8770
    site: str = "yunhan.me"
    cookie_name: str = "yh_session"
    cookie_domain: str = ""
    cookie_days: int = 30
    origins: tuple[str, ...] = ()
    instrument: Path = field(default_factory=lambda: Path(__file__).resolve().parents[2] / "instrument")
    store_max_bytes: int = 262144
    sites: dict[str, Path] = field(default_factory=dict)

    @property
    def accounts_file(self) -> Path:
        return self.dir / "accounts.json"

    @property
    def secret_file(self) -> Path:
        return self.dir / "secret"

    @property
    def users_dir(self) -> Path:
        return self.dir / "users"


def _path(value: Any) -> Path:
    return Path(str(value)).expanduser()


def load(path: Path | None = None) -> Config:
    path = path or Path(os.environ.get("DOOR_CONFIG", DEFAULT_PATH)).expanduser()
    cfg = Config()
    try:
        raw = tomllib.loads(path.read_text())
    except FileNotFoundError:
        return cfg
    for key in ("bind", "site", "cookie_name", "cookie_domain"):
        if key in raw:
            setattr(cfg, key, str(raw[key]))
    for key in ("port", "cookie_days", "store_max_bytes"):
        if key in raw:
            setattr(cfg, key, int(raw[key]))
    if "dir" in raw:
        cfg.dir = _path(raw["dir"])
    if "instrument" in raw:
        cfg.instrument = _path(raw["instrument"])
    if "origins" in raw:
        cfg.origins = tuple(str(o).rstrip("/") for o in raw["origins"])
    sites = raw.get("sites") or {}
    cfg.sites = {str(h).lower(): _path(p) for h, p in sites.items()}
    return cfg
