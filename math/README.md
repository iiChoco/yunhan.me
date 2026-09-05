# math.yunhan.me

Small math tools, served by one Cloudflare Worker.

- `public/` — the pages. `public/zetamac/index.html` is the Zetamac clone; `public/index.html` is the index.
- `src/worker.js` — the Worker. `scripts/build.mjs` inlines `public/` into it and writes `dist/worker.js`.
- `wrangler.jsonc` — deploys `dist/worker.js` as the `math` Worker on the custom domain `math.yunhan.me`.

```bash
npm install
npm run dev      # local preview at http://localhost:8787
npm run deploy   # build + wrangler deploy (needs `npx wrangler login` once)
```
