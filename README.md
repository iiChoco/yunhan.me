# yunhan.me

Personal website and independent web tools. This repository lives at
`~/Projects/yunhan.me`, alongside the separate Ciel and infrastructure repos.

- `home/`: a public landing page and an authenticated Toolbox with Ciel Interview,
  Math, nine local browser utilities, and a temporary URL shortener. Standalone
  tools use short paths on `tools.yunhan.me`; Toolbox lives on the apex.
- `door/`: shared login, per-user storage, and static hosting.
- `math/`: math tools served by Door.
- `instrument/`: shared visual design assets.
- `scripts/push.sh`: forwards deployment to `~/Projects/infrastructure`.

Infrastructure owns server service definitions and deployment configuration.
Run `scripts/push.sh --preview` to print commands, `scripts/push.sh --dry-run`
to compare with the server, or `scripts/push.sh --sync` to deploy with locked
dependency sync. The wrapper deploys by default.
The server checkout remains `/home/ciel/yunhan.me`; runtime data stays in `~/.door`.

For local development, `cd door` and run `uv sync --locked`, then follow the
[Door README](door/README.md). Ciel's brain, hub, and Chart belong to the Ciel
repository even though its web interface is served at `ciel.yunhan.me`.

The [homepage guide](home/README.md) covers local preview and serving the apex
through Door. The landing page is public; Toolbox requires the existing Door
session and is kept outside the public files. Neither page needs a build step.
Live DNS, tunnel routing, and service updates are configured separately.
