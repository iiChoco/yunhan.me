# Working on yunhan.me

## Working together

- One writer per checkout. Parallel implementation needs separate worktrees
  and agreed file ownership.
- Read status and diffs before starting; re-read each file immediately before
  editing and reconcile any changes.
- Preserve other tasks' uncommitted work. Never discard, stash, stage, commit,
  or reformat it as cleanup.
- Reviews provide findings, evidence, and proposed fixes; the assigned writer
  makes the changes.
- Keep settled decisions unless changed requirements or new evidence justify
  revisiting them; record the reason.

Follow this repository's conventions and configured checks; otherwise match
neighbouring code. Google's style guides are optional references, not review
requirements. Permission covers the user's stated task and scope; it does not
carry over to unrelated work.

## Ownership and code

- This repository owns the personal website, math tools, Door, and Instrument
  components. Ciel's brain and interfaces belong to the separate Ciel repository.
  Deployment and service definitions belong to infrastructure.
- Read the README in the component you will change. `door/` is a Python 3.12
  aiohttp project managed with uv. Follow its type hints, dataclass config,
  async handlers, and explicit JSON error shapes.
- `math/public/` and Door's pages are plain HTML/CSS/JavaScript. Preserve the
  existing structure and formatting; do not introduce a bundler, framework,
  formatter, dependency, or broad file split as incidental cleanup.
- Explain decisions and failure cases in comments. Keep naming and public
  behavior stable. Add new configuration to Door's config dataclass and document it.
- Account identifiers, cookies, and per-user storage can affect Ciel Interview.
  Inspect both sides and define compatibility before changing those contracts;
  do not port only one side of an authentication fix and call the shared login done.
- Runtime accounts and secrets belong in `~/.door`, outside this repository.
  Checks use temporary users and data. Preserve origin checks, ownership checks,
  and private response handling.

## Visual and writing style

Read [Instrument](instrument/README.md) before UI changes; it describes token
ownership, shared components, and offline copies. Reuse those assets and follow
its versioning instructions when changing them.

Check small-screen layout, focus visibility, keyboard interactions, and relevant
empty/loading/error states. Keep UI copy brief and understandable; infrastructure
and implementation details should not leak into ordinary user flows.

Documentation explains behavior and why it exists. Match neighbouring prose and
existing sentence-style commit titles; do not invent Ciel subsystem codenames.

## Development and verification

From `door/`, use `uv run --no-sync ...` with an already prepared environment;
`uv sync --locked` prepares or updates that environment without changing the lock.
There is no repository-wide test runner currently documented. Inspect available
checks for the touched component and run a focused check with temporary fixtures
for backend behavior changes. Use local browser verification for UI changes and
state what was actually checked. Do not claim a test suite exists or passed if
it does not. Documentation-only work needs link/command checks and `git diff --check`.

Update the relevant README with changed behavior. Work on the assigned branch;
no new branch, commit, push, or deployment unless authorized. Stage only the
requested change when committing.

## Deployment flags

`scripts/push.sh` deploys by default. `--preview` prints without network access;
`--dry-run` compares against the server; `--sync` additionally synchronizes server
dependencies. Do not run the bare wrapper as a harmless validation command.
The underlying infrastructure `scripts/deploy.py` previews by default and uses
`--apply` for deployment. Keep the distinction explicit in docs and handoffs.
