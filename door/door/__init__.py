"""The door: one login for every yunhan.me surface.

Accounts are the owner's to make (no signup), passwords are generated and
shown once, and a login is a stateless signed cookie set on the parent
domain so ciel.yunhan.me, math.yunhan.me, and whatever comes next all see
the same session. Beside it, a small per-user store so a static page can
keep something across devices, and static hosting by hostname so the
small sites live on the same box behind the same tunnel.
"""

__version__ = "0.1.0"
