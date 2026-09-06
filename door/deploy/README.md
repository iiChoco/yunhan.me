# Deployment

The canonical Door unit is maintained in the independent infrastructure
repository at `~/Projects/infrastructure/services/systemd/door.service`.
See that repository's README and `docs/operations.md` for configuration,
routing, deployment, and recovery.

The website's `scripts/push.sh` forwards to infrastructure. It previews by
default; use `--apply` to deploy. The server source path remains
`/home/ciel/yunhan.me`, with runtime state under `/home/ciel/.door`.
