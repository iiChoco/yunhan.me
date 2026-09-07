import { $, on, copy } from './common.js';
function hex(rgb) { return '#' + rgb.map(n => Math.round(n).toString(16).padStart(2, '0')).join(''); }
function fromHex(raw) { const s = raw.slice(1); return s.length === 3 ? [...s].map(c => parseInt(c + c, 16)) : s.match(/../g).map(c => parseInt(c, 16)); }
function parse(raw) {
  raw = raw.trim(); if (/^#(?:[0-9a-f]{3}|[0-9a-f]{6})$/i.test(raw)) return fromHex(raw);
  const rgb = raw.match(/^rgb\(\s*([\d.]+)\s*,\s*([\d.]+)\s*,\s*([\d.]+)\s*\)$/i);
  if (rgb) { const values = rgb.slice(1).map(Number); if (values.every(n => Number.isFinite(n) && n >= 0 && n <= 255)) return values.map(Math.round); }
  const hsl = raw.match(/^hsl\(\s*(-?[\d.]+)(?:deg)?\s*,\s*([\d.]+)%\s*,\s*([\d.]+)%\s*\)$/i);
  if (hsl) { let [h, s, l] = hsl.slice(1).map(Number); if ([h, s, l].every(Number.isFinite) && s >= 0 && s <= 100 && l >= 0 && l <= 100) {
    h = ((h % 360) + 360) % 360 / 60; s /= 100; l /= 100; const c = (1 - Math.abs(2 * l - 1)) * s, x = c * (1 - Math.abs(h % 2 - 1)), m = l - c / 2;
    const segments = [[c, x, 0], [x, c, 0], [0, c, x], [0, x, c], [x, 0, c], [c, 0, x]]; return segments[Math.floor(h)].map(n => Math.round((n + m) * 255));
  } }
  throw Error('Use #a0f0ff, rgb(160, 240, 255), or hsl(189, 100%, 81%). Alpha colors are not supported.');
}
function update(rgb) {
  const value = hex(rgb); $('color-picker').value = value; $('color-swatch').style.backgroundColor = value; $('color-hex').value = value;
  $('color-rgb').value = `rgb(${rgb.join(', ')})`;
  const [r, g, b] = rgb.map(n => n / 255), max = Math.max(r, g, b), min = Math.min(r, g, b), d = max - min, l = (max + min) / 2;
  let h = 0, s = 0; if (d) { s = d / (1 - Math.abs(2 * l - 1)); h = max === r ? ((g - b) / d) % 6 : max === g ? (b - r) / d + 2 : (r - g) / d + 4; h = (h * 60 + 360) % 360; }
  $('color-hsl').value = `hsl(${Math.round(h)}, ${Math.round(s * 100)}%, ${Math.round(l * 100)}%)`;
}
on('color-picker', 'input', () => { $('color-input').value = $('color-picker').value; update(fromHex($('color-picker').value)); });
on('color-convert', 'click', () => update(parse($('color-input').value)));
on('color-copy', 'click', () => copy($('color-hex').value));
function luminance(value) { return fromHex(value).map(n => { const c = n / 255; return c <= .04045 ? c / 12.92 : ((c + .055) / 1.055) ** 2.4; }).reduce((sum, n, i) => sum + n * [.2126, .7152, .0722][i], 0); }
function contrast() {
  const fg = $('contrast-fg').value, bg = $('contrast-bg').value, a = luminance(fg), b = luminance(bg), ratio = (Math.max(a, b) + .05) / (Math.min(a, b) + .05);
  $('contrast-preview').style.color = fg; $('contrast-preview').style.backgroundColor = bg; $('contrast-ratio').textContent = `${ratio.toFixed(2)}:1`;
  $('contrast-grade').textContent = `WCAG AA normal text: ${ratio >= 4.5 ? 'pass' : 'fail'} · AA large text: ${ratio >= 3 ? 'pass' : 'fail'} · AAA normal text: ${ratio >= 7 ? 'pass' : 'fail'}. Large means at least 24px regular or about 19px bold.`;
}
on('contrast-fg', 'input', contrast); on('contrast-bg', 'input', contrast); update(fromHex($('color-picker').value)); contrast();
