#!/bin/sh
# Push this checkout to the Ciel VM, where the door serves it.
#
#     scripts/push.sh            # rsync the tree; the door restarts to pick up code changes
#     scripts/push.sh --sync     # ...and re-sync the door's venv (after a dependency change)
#
# Static sites (math/) are read from disk per request, so they are live the
# moment the files land. The door's own code needs the restart.
set -e
HOST="${YUNHAN_HOST:-ciel@172.184.253.239}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
rsync -az --delete \
  --exclude .git --exclude node_modules --exclude .venv --exclude __pycache__ \
  --exclude .claude --exclude .DS_Store \
  "$ROOT/" "$HOST:~/yunhan.me/"
echo "pushed to $HOST"
if [ "$1" = "--sync" ]; then
  ssh "$HOST" 'cd ~/yunhan.me/door && ~/.local/bin/uv sync 2>&1 | tail -2'
fi
ssh "$HOST" 'sudo systemctl restart door && sleep 1 && systemctl is-active door'
