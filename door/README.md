# The door

One login for every yunhan.me surface, plus the two things that make a login worth having for a static page: a small per-user store, and static hosting on the same box behind the same tunnel.

- `door/accounts.py` is Ciel's interview-room accounts module, unchanged in format: owner-created users, generated passwords shown once, scrypt hashes in `accounts.json`, and a stateless signed cookie. Ciel's room reads the same files and cookie, so a friend signed into `math.yunhan.me` is signed into `ciel.yunhan.me/interview` and back.
- `door/app.py` is the aiohttp server: `/api/login`, `/api/logout`, `/api/me`, `/api/password`, the owner's `/api/admin/accounts/…`, the store at `/api/store/<app>/<key>`, a login page at `/` on the auth host (also `/login`), an admin page at `/admin`, and any hostname listed under `[sites]` served from a directory.
- Config lives in `~/.door/config.toml`; see the docstring in `door/config.py`.

```bash
uv sync                                  # a venv with aiohttp
DOOR_CONFIG=dev.toml uv run door serve   # loopback dev
uv run door add-user alice               # prints the password once
uv run door import-ciel ~/.ciel/interview
```

Production: `~/Projects/infrastructure/services/systemd/door.service` on the Ciel VM, `auth.yunhan.me` and `math.yunhan.me` as tunnel ingress rules to its port, and a Cloudflare Access application (owner only) on `auth.yunhan.me/admin` and `/api/admin`.

On the parent domain configured as `site`, Door serves the public landing from
`home/public` and protects `/toolbox` with the same account/session validation as
its APIs. Signed-out requests redirect to `/login?next=/toolbox`. Toolbox comes
from `home/private/toolbox.html`, outside the static root; successful responses
and login redirects are private and uncached. Direct static aliases cannot serve
that file. The apex exposes login, logout, profile, password, and the
`/api/store/toolbox-favorites` namespace. Favorites use the existing authenticated
store: listing returns this account's saved tool keys, PUT adds a key, and DELETE
removes it. Responses, including errors, are private and uncached on the apex.
Separate keys avoid overwriting other tool choices when two devices save at once.
Admin stays on the auth hostname and its Access gate.

`home` defaults to the checkout's `home/` directory; set it in config if the
assets live elsewhere. Existing math `[sites]` mappings keep their static behavior.
Production's `.yunhan.me` cookie domain shares sessions between apex and auth.
The landing page link to Ciel does not change Ciel's own access requirements.

Authentication checks use temporary state and an in-process server:

```sh
uv run --no-sync python -m unittest discover -s tests -v
```

Utility pages on `tools.yunhan.me` use the same gate and return to their short
route after login. `tools_host` defaults to `tools.<site>`; loopback previews use
their existing origin unless explicitly configured. Old `/tools/<slug>` routes
on the apex redirect to the tool host. Tool navigation returns to the apex
Toolbox, and the production shared-domain cookie works on both hosts. Only the fixed utility allowlist can select a private page.
Their JavaScript and styles are public assets. The nine browser utilities keep
inputs local; the URL shortener sends destinations to Door for redirects.

Both apex and tool hosts serve the authenticated short-link API: GET `/api/links` lists
this account's active links, POST accepts `destination` and `expires_in` (integer
seconds, 1–86,400, default 86,400), and DELETE `/api/links/<slug>` expires an owned
link immediately. No account identifier is accepted from the client. Public
GET/HEAD `/<slug>` returns an uncached 302 while active or 410 after expiration.

`door/shortlinks.py` uses standard-library SQLite at `<dir>/shortlinks.sqlite3`,
created owner-only and independent of the shared accounts/store formats. Include
it in runtime backups. Transactions reserve unique names and enforce 50 active
links per account. Expiration is checked even without cleanup; listing or creating
links clears expired destinations and owners, retaining the slug so old links
cannot be reassigned. No scheduled job or extra dependency is needed.

The short paths are `/qr`, `/color`, `/url`, `/convert`, `/image`, `/json`, `/pdf`,
`/text`, `/password`, and `/timer`; their mapping to private HTML is fixed in
`UTILITY_PATHS`. Assets are served on the tool host so processing and API requests
remain same-origin. `/` on the tool host returns to the apex Toolbox. Only the
apex resolves generated short links. Admin endpoints stay on auth.yunhan.me.
