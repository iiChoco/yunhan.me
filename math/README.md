# math.yunhan.me

Small math tools, hosted on Azure Static Web Apps (Free tier).

- `public/` is the whole site. `public/zetamac/index.html` is the Zetamac clone, `public/index.html` the index, `public/404.html` the not-found page.
- `public/staticwebapp.config.json` sets no-trailing-slash routing, the 404 page, and cache/security headers.
- Azure: subscription "Azure subscription 1", resource group `math`, Static Web App `math`, custom domain `math.yunhan.me` (CNAME at Cloudflare, DNS-only).

```bash
npm install
npm run dev      # local preview at http://localhost:4280
npm run deploy   # needs `az login` (uses your Azure CLI session)
```
