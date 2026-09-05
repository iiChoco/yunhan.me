// math.yunhan.me — serves the static pages in public/, inlined at build time.
// scripts/build.mjs prepends `const ASSETS = {...}` (path -> {body, type})
// and writes the result to dist/worker.js. Deploy that file.
/* global ASSETS */

const HEADERS = {
  'cache-control': 'public, max-age=300',
  'x-content-type-options': 'nosniff',
  'referrer-policy': 'strict-origin-when-cross-origin',
};

function lookup(pathname) {
  let p = pathname;
  if (p.length > 1 && p.endsWith('/')) p = p.slice(0, -1);
  if (p === '/') p = '';
  for (const c of [p, p + '/index.html', p + '.html']) if (ASSETS[c]) return ASSETS[c];
  return null;
}

export default {
  async fetch(request) {
    const url = new URL(request.url);
    if (request.method !== 'GET' && request.method !== 'HEAD') {
      return new Response('Method not allowed', { status: 405, headers: { allow: 'GET, HEAD' } });
    }
    // Canonicalise trailing slashes: /zetamac/ -> /zetamac
    if (url.pathname.length > 1 && url.pathname.endsWith('/')) {
      url.pathname = url.pathname.replace(/\/+$/, '');
      return Response.redirect(url.toString(), 308);
    }
    const asset = lookup(url.pathname);
    if (!asset) {
      const nf = ASSETS['/404.html'];
      return new Response(nf ? nf.body : 'Not found', { status: 404, headers: { ...HEADERS, 'content-type': nf ? nf.type : 'text/plain; charset=utf-8', 'cache-control': 'no-store' } });
    }
    const headers = { ...HEADERS, 'content-type': asset.type, etag: `"${asset.hash}"` };
    if (request.headers.get('if-none-match') === headers.etag) return new Response(null, { status: 304, headers });
    return new Response(request.method === 'HEAD' ? null : asset.body, { headers });
  },
};
