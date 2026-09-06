#!/bin/sh
# Push this checkout to the server. The deploy itself lives in the sibling
# infrastructure repository (scripts/deploy.py); this script only forwards.
#
#     scripts/push.sh              # rsync the source tree and restart door
#     scripts/push.sh --sync       # ...and re-sync door's locked dependencies
#     scripts/push.sh --dry-run    # rsync's remote dry run: what would change
#     scripts/push.sh --preview    # print the commands only; no network
#
# Set INFRASTRUCTURE_DIR if the infrastructure checkout is not under ~/Projects.
set -eu
SOURCE="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd -P)"
INFRA="${INFRASTRUCTURE_DIR:-$HOME/Projects/infrastructure}"
if [ ! -f "$INFRA/scripts/deploy.py" ]; then
  echo "Infrastructure checkout not found at $INFRA; set INFRASTRUCTURE_DIR." >&2
  exit 1
fi
# deploy.py previews unless told otherwise; here the default is to deploy.
mode="--apply"
n=$#
while [ "$n" -gt 0 ]; do
  arg=$1; shift; n=$((n - 1))
  case "$arg" in
    --preview) mode="" ;;
    --dry-run|--apply) mode="$arg" ;;
    *) set -- "$@" "$arg" ;;
  esac
done
# $mode is deliberately unquoted: empty means "pass nothing".
exec python3 "$INFRA/scripts/deploy.py" website --source "$SOURCE" $mode "$@"
