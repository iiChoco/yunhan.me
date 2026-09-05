# The door

One login for every yunhan.me surface, plus the two things that make a login worth having for a static page: a small per-user store, and static hosting on the same box behind the same tunnel.

- `door/accounts.py` is Ciel's interview-room accounts module, unchanged in format: owner-created users, generated passwords shown once, scrypt hashes in `accounts.json`, and a stateless signed cookie. Ciel's room reads the same files and cookie, so a friend signed into `math.yunhan.me` is signed into `ciel.yunhan.me/interview` and back.
- `door/app.py` is the aiohttp server: `/api/login`, `/api/logout`, `/api/me`, `/api/password`, the owner's `/api/admin/accounts/…`, the store at `/api/store/<app>/<key>`, a login page at `/`, an admin page at `/admin`, and any hostname listed under `[sites]` served from a directory.
- Config lives in `~/.door/config.toml`; see the docstring in `door/config.py`.

```bash
uv sync                                  # a venv with aiohttp
DOOR_CONFIG=dev.toml uv run door serve   # loopback dev
uv run door add-user alice               # prints the password once
uv run door import-ciel ~/.ciel/interview
```

Production: `deploy/door.service` on the Ciel VM, `auth.yunhan.me` and `math.yunhan.me` as tunnel ingress rules to its port, and a Cloudflare Access application (owner only) on `auth.yunhan.me/admin` and `/api/admin`.
