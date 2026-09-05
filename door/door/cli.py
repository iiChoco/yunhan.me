"""``door`` on the command line: serve, and the owner's account chores.

    door serve                       # the server, from ~/.door/config.toml (or DOOR_CONFIG)
    door list
    door add-user alice [--admin]    # prints the generated password once
    door reset alice
    door disable alice | enable alice | delete alice
    door import-ciel ~/.ciel/interview   # copy the interview room's accounts and secret in
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from door import config as _config
from door.accounts import Accounts


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="door", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--config", type=Path, default=None, help="config file (default ~/.door/config.toml or $DOOR_CONFIG)")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("serve")
    sub.add_parser("list")
    a = sub.add_parser("add-user"); a.add_argument("username"); a.add_argument("--admin", action="store_true")
    for name in ("reset", "disable", "enable", "delete"):
        s = sub.add_parser(name); s.add_argument("username")
    i = sub.add_parser("import-ciel"); i.add_argument("interview_dir", type=Path)
    args = p.parse_args(argv)

    cfg = _config.load(args.config)
    accounts = Accounts(cfg.accounts_file)

    if args.cmd == "serve":
        from door.app import serve
        serve(cfg)
        return 0
    if args.cmd == "list":
        rows = accounts.list()
        if not rows:
            print("no accounts")
        for acct in rows:
            flag = " (disabled)" if acct.disabled else ""
            print(f"{acct.username:20} {acct.role:6} created {acct.created}  last seen {acct.last_seen or '—'}{flag}")
        return 0
    if args.cmd == "add-user":
        try:
            pw = accounts.create(args.username, "admin" if args.admin else "user")
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr); return 1
        print(f"{args.username}: {pw}\n(shown once — the browser will remember it)")
        return 0
    if args.cmd == "reset":
        try:
            pw = accounts.reset(args.username)
        except KeyError:
            print("error: no such account", file=sys.stderr); return 1
        print(f"{args.username}: {pw}")
        return 0
    if args.cmd in ("disable", "enable"):
        try:
            accounts.set_disabled(args.username, args.cmd == "disable")
        except KeyError:
            print("error: no such account", file=sys.stderr); return 1
        print(f"{args.username} {args.cmd}d")
        return 0
    if args.cmd == "delete":
        try:
            accounts.delete(args.username)
        except KeyError:
            print("error: no such account", file=sys.stderr); return 1
        print(f"{args.username} deleted")
        return 0
    if args.cmd == "import-ciel":
        src_accounts = args.interview_dir.expanduser() / "interview-accounts.json"
        src_secret = args.interview_dir.expanduser() / "interview.secret"
        if not src_accounts.is_file():
            print(f"error: {src_accounts} not found", file=sys.stderr); return 1
        cfg.dir.mkdir(parents=True, exist_ok=True)
        if cfg.accounts_file.exists():
            print(f"error: {cfg.accounts_file} already exists; not overwriting", file=sys.stderr); return 1
        shutil.copy2(src_accounts, cfg.accounts_file); cfg.accounts_file.chmod(0o600)
        if src_secret.is_file() and not cfg.secret_file.exists():
            shutil.copy2(src_secret, cfg.secret_file); cfg.secret_file.chmod(0o600)
        print(f"imported {len(accounts.list())} accounts into {cfg.dir}")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
