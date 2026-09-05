# math.yunhan.me

Small math tools. Static files in `public/`, served by the door (`../door`) on the Ciel VM as the `math.yunhan.me` site, behind the Cloudflare Tunnel.

- `public/zetamac/index.html` is the Zetamac clone: presets, sprint mode, per-run stats, progress charts, and, when signed in through the door, history that follows you across devices.
- `public/index.html` is the index; `public/404.html` the not-found page.

Deploy is `scripts/push.sh` from the repo root: files are read from disk per request, so they are live when they land.

Local preview: run the door with a dev config that lists `"math.localhost" = "<repo>/math/public"` under `[sites]` and open http://math.localhost:8770/zetamac.
