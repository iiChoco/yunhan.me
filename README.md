# yunhan.me

Personal website and independent web tools. This repository lives at
`~/Projects/yunhan.me`, alongside the separate Ciel and infrastructure repos.

- `door/`: shared login, per-user storage, and static hosting.
- `math/`: math tools served by Door.
- `instrument/`: shared visual design assets.
- `scripts/push.sh`: forwards deployment to `~/Projects/infrastructure`.

Infrastructure owns server service definitions and deployment configuration.
Run `scripts/push.sh` to preview, `scripts/push.sh --dry-run` to compare with the
server, or `scripts/push.sh --sync --apply` to deploy with locked dependency sync.
The server checkout remains `/home/ciel/yunhan.me`; runtime data stays in `~/.door`.

For local development, `cd door` and run `uv sync --locked`, then follow the
[Door README](door/README.md). Ciel's brain, hub, and Chart belong to the Ciel
repository even though its web interface is served at `ciel.yunhan.me`.
