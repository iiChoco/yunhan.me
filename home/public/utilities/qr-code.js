import { $, on, status, download, loadScript } from './common.js';
let qr = null;
const ready = loadScript('/vendor/qrcode.js').then(() => loadScript('/vendor/qrcode-utf8.js'));
ready.catch(err => status(err.message, true));
function invalidate() { qr = null; $('qr-png').disabled = $('qr-svg').disabled = true; $('qr-canvas').hidden = true; $('qr-empty').hidden = false; }
$('qr-text').addEventListener('input', invalidate); $('qr-level').addEventListener('change', invalidate);
on('qr-generate', 'click', async () => {
  invalidate(); const text = $('qr-text').value; if (!text.trim()) throw Error('Enter text or a URL first.');
  await ready;
  try { qr = window.qrcode(0, $('qr-level').value); qr.addData(text, 'Byte'); qr.make(); }
  catch { qr = null; throw Error('This text is too long for the selected correction level. Shorten it or choose a lower level.'); }
  render(); $('qr-png').disabled = $('qr-svg').disabled = false; $('qr-empty').hidden = true; $('qr-canvas').hidden = false;
  status('Ready. Download PNG for an image, or SVG for a scalable version.');
});
function render() {
  if (!qr) return; const canvas = $('qr-canvas'), pixels = Number($('qr-size').value), count = qr.getModuleCount(), cells = count + 8;
  canvas.width = canvas.height = pixels; const ctx = canvas.getContext('2d'); ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, pixels, pixels); ctx.fillStyle = '#000';
  for (let row = 0; row < count; row++) for (let col = 0; col < count; col++) if (qr.isDark(row, col)) {
    const x = Math.round((col + 4) * pixels / cells), y = Math.round((row + 4) * pixels / cells);
    ctx.fillRect(x, y, Math.round((col + 5) * pixels / cells) - x, Math.round((row + 5) * pixels / cells) - y);
  }
}
on('qr-size', 'change', render);
on('qr-png', 'click', async () => { const blob = await new Promise(resolve => $('qr-canvas').toBlob(resolve, 'image/png')); if (!blob) throw Error('PNG export failed.'); download(blob, 'qr-code.png'); });
on('qr-svg', 'click', () => {
  if (!qr) return; const n = qr.getModuleCount(); let path = '';
  for (let y = 0; y < n; y++) for (let x = 0; x < n; x++) if (qr.isDark(y, x)) path += `M${x + 4} ${y + 4}h1v1h-1z`;
  download(new Blob([`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${n + 8} ${n + 8}" shape-rendering="crispEdges"><rect width="100%" height="100%" fill="white"/><path d="${path}" fill="black"/></svg>`], { type: 'image/svg+xml' }), 'qr-code.svg');
});
