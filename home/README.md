# Home

The public landing page at `/` pairs a name with the animated orbital graphic.
Hover or keyboard focus adds a gentle lift and glow; activating it opens Ciel.
A small script randomizes the points' starting positions on each load. Without
JavaScript, their CSS animation uses fixed positions. Reduced-motion settings
keep them still and disable the lift. The orbital graphic is the website’s
only launcher for Ciel itself; Ciel Interview remains in Toolbox.

Toolbox at `/toolbox` is an alphabetical icon launcher for Ciel Interview,
Math, nine browser utilities, and a temporary URL shortener. It requires an active Door account. Signed-out visitors go to
`/login?next=/toolbox` and return after signing in. Its Account link opens Door's
existing password and sign-out controls. Math opens `math.yunhan.me/zetamac`
directly; the math hostname’s landing page is intentionally empty. The same `yh_session` cookie and account
files are used by the auth hostname; there is no second login system.

Star a tool to save it to your account and move it above the other tools. A line
separates favorites from the rest when both groups have tools; each group stays
alphabetical. Favorites persist across sign-ins and devices
through Door's existing per-user store, with one key per tool in
`toolbox-favorites`. The page refreshes favorites when reopened or returned to;
failed loads and saves offer a retry. Favorites need JavaScript; tool links do not.

`public/index.html`, `public/home.css`, and the vendored `public/instrument.css`
are public assets. `private/toolbox.html` is outside the static tree and is only
read after Door validates the session. Private responses and login redirects use
`Cache-Control: private, no-store`. Do not put a copy of Toolbox under `public/`.
The Instrument copy is v1, 2026-09-04; update it from
`../instrument/instrument.css` when that source changes.

## Local preview

Use Door for the complete login flow. Create a temporary state directory and a
local config outside the repository, with these values (replace the example
paths with that directory and your checkout):

```toml
site = "127.0.0.1"
bind = "127.0.0.1"
port = 8780
dir = "/tmp/your-preview-state"
home = "/absolute/path/to/yunhan.me/home"
cookie_domain = ""
```

From `door/`, run `uv run --no-sync door --config /path/to/dev.toml add-user preview`
to create a temporary account, then `uv run --no-sync door --config /path/to/dev.toml serve`.
Open http://127.0.0.1:8780. Use temporary credentials, never production account files.
Loopback previews keep tools on the same origin using the same short paths.
Set `tools_host` and a shared `cookie_domain` to preview separate hostnames.
A plain static server can preview the landing page but cannot serve Toolbox,
its utility pages, or login.

## Serving yunhan.me

Door serves `home/public` on the hostname configured as `site` (`yunhan.me` by
default), and handles its `/login`, account endpoints, and protected `/toolbox`.
`home` defaults to this checkout's `home/` directory and can be overridden in
Door's config. The apex does not need a `[sites]` entry. Keep the existing math
mapping and `cookie_domain = ".yunhan.me"` for shared production sessions.
Admin pages and APIs remain on the auth hostname, with its existing Access gate.

Both `yunhan.me` and `tools.yunhan.me` need tunnel ingress to Door and DNS
pointing to that tunnel. Deploying these files and restarting Door are separate from editing them.
Ciel's own Access policies and Math's existing access rules remain independent;
locking Toolbox only controls the directory of links.

Run the authentication checks from `door/`:

```sh
uv run --no-sync python -m unittest discover -s tests -v
```

## Browser utilities

Every tool page on `tools.yunhan.me` uses the same private, no-store Door gate
as Toolbox. Short routes are `/qr`, `/color`, `/url`, `/convert`, `/image`, `/json`,
`/pdf`, `/text`, `/password`, and `/timer`. Old `yunhan.me/tools/<slug>` URLs
redirect to the new addresses. Ciel, Interview, and Math keep their own hosts.
HTML lives in `private/utilities/`; public `/utilities/` holds the scripts and
styles, not the pages. The nine browser utilities below have no upload endpoints,
tracking requests, browser storage, or server-side processing of tool inputs. Utilities need JavaScript;
the landing page and launcher navigation work without it.

| Tool | Route | What it does |
|---|---|---|
| Color Picker | `tools.yunhan.me/color` | HEX/RGB/HSL conversion and WCAG text contrast |
| Converters | `tools.yunhan.me/convert` | Units, Unix dates, time zones with DST handling, URL/Base64 |
| Image Tools | `tools.yunhan.me/image` | Resize, quality control, PNG/JPEG/WebP export, remove source metadata |
| JSON Formatter | `tools.yunhan.me/json` | Validate, format, minify, search, copy, download |
| Password Generator | `tools.yunhan.me/password` | Secure random passwords and EFF-wordlist passphrases |
| PDF Tools | `tools.yunhan.me/pdf` | Select/reorder pages, merge/extract a PDF, split selected pages into ZIP |
| QR Code | `tools.yunhan.me/qr` | Unicode text/URL QR generation, PNG and SVG downloads |
| Text Tools | `tools.yunhan.me/text` | Counts, case changes, line cleanup/deduplication, line comparison |
| Timer | `tools.yunhan.me/timer` | Countdown, stopwatch/laps, focus/break presets and optional finish sound |

The QR, PDF, ZIP, and diff libraries are pinned and vendored; their versions,
source tarball integrity, licenses, and the EFF wordlist attribution are in
`public/vendor/`. Libraries load only on tools that use them. Shared input,
status, copy, and download helpers live in `public/utilities/common.js`.

Image input is limited to 50 MB and 40 million pixels; output dimensions are
limited to 8,192 per side and 40 million pixels. Animated images become one frame.
PDF input is limited to 50 MB and 300 pages. Encrypted PDFs are rejected; copied
pages may not retain document-level forms, bookmarks, or attachments. JSON uses
JavaScript numbers and rejects unsafe integer values rather than silently rounding
them; use strings for large identifiers. Text comparisons are bounded in size
and time. Timers use deadlines rather than counting callbacks, but a suspended
browser may delay the finish sound. None of the tools save your work after closing.

Browser verification covered all nine tools, including independent QR decoding,
PNG/JPEG/WebP dimensions, PDF order and ZIP contents, Unicode round trips, DST
gaps and repeated times, password character groups, countdown/stopwatch/focus
behavior, 320px and 390px layouts, and the absence of input-upload requests.

## Temporary URL shortener

`tools.yunhan.me/url` creates public links such as `yunhan.me/falcon`. Creating,
listing, and expiring links requires a Door account; opening a link does not.
Choose 1–1,440 minutes or 1–24 hours, with 24 hours as the default. The server
rejects lifetimes above 24 hours and checks the deadline on every redirect.
Copy a link, see its destination and expiration, or select **Expire now**. Active
links are saved to your account across devices, with a limit of 50 at once.

This tool sends destinations to Door so it can redirect visitors. It never fetches
the destination itself. Only full HTTP(S) URLs without embedded credentials are
accepted. Random names use the existing EFF wordlist, skip site routes, and are
never reused; additional words are joined with hyphens as single names run out.
Expired or revoked links return 410, and redirects are uncached. The local preview
uses its home origin; production short links always use yunhan.me, including
when created from tools.yunhan.me/url.
