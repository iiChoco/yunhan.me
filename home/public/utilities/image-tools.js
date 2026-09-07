import { $, on, status, download, integer, size, busy } from './common.js';
let source = null, file = null, result = null, previewURL = null, revision = 0;
function preview(blob) { if (previewURL) URL.revokeObjectURL(previewURL); previewURL = URL.createObjectURL(blob); $('image-preview').src = previewURL; $('image-preview').hidden = false; $('image-empty').hidden = true; }
function invalidate() { result = null; $('image-download').disabled = true; $('image-result').textContent = ''; }
on('image-file', 'change', async () => {
  const current = ++revision; invalidate(); $('image-export').disabled = true; $('image-width').disabled = $('image-height').disabled = true;
  source?.close(); source = null; file = $('image-file').files[0]; $('image-preview').hidden = true; $('image-empty').hidden = false;
  if (!file) return; if (file.size > 50 * 1024 * 1024) throw Error('Choose an image under 50 MB.');
  let decoded; try { decoded = await createImageBitmap(file); } catch { throw Error('This image could not be opened. Try PNG, JPEG, or WebP.'); }
  if (current !== revision) { decoded.close(); return; }
  if (decoded.width * decoded.height > 40000000) { decoded.close(); throw Error('Choose an image with fewer than 40 million pixels.'); }
  source = decoded; $('image-width').value = source.width; $('image-height').value = source.height;
  $('image-width').disabled = $('image-height').disabled = $('image-export').disabled = false;
  $('image-info').textContent = `${file.name} · ${source.width} × ${source.height} · ${size(file.size)}`; preview(file);
});
for (const axis of ['width', 'height']) on(`image-${axis}`, 'input', () => { invalidate(); if (!source || !$('image-lock').checked) return; const value = Number($(`image-${axis}`).value); if (value > 0) $(`image-${axis === 'width' ? 'height' : 'width'}`).value = Math.max(1, Math.round(value * (axis === 'width' ? source.height / source.width : source.width / source.height))); });
on('image-quality', 'input', () => { $('image-quality-label').textContent = `${$('image-quality').value}%`; invalidate(); });
on('image-format', 'change', () => { invalidate(); $('image-quality').disabled = $('image-format').value === 'image/png'; });
on('image-export', 'click', () => busy([$('image-export')], async () => {
  if (!source) throw Error('Choose an image first.'); const current = revision;
  const width = integer($('image-width').value, 1, 8192, 'Width'), height = integer($('image-height').value, 1, 8192, 'Height');
  if (width * height > 40000000) throw Error('Keep the output below 40 million pixels.');
  const format = $('image-format').value, canvas = document.createElement('canvas'); canvas.width = width; canvas.height = height; const ctx = canvas.getContext('2d');
  if (format === 'image/jpeg') { ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, width, height); }
  ctx.drawImage(source, 0, 0, width, height); const blob = await new Promise(resolve => canvas.toBlob(resolve, format, Number($('image-quality').value) / 100));
  if (current !== revision) return; if (!blob || blob.type !== format) throw Error('Your browser cannot export this format. Try PNG or JPEG.');
  result = { blob, name: `${file.name.replace(/\.[^.]+$/, '')}-${width}x${height}.${format.split('/')[1].replace('jpeg', 'jpg')}` };
  preview(blob); $('image-result').textContent = `${width} × ${height} · ${size(blob.size)} · ${blob.size <= file.size ? Math.round((1 - blob.size / file.size) * 100) + '% smaller' : 'larger than the original'} · original metadata removed`;
  $('image-download').disabled = false; status('Export ready.');
}));
on('image-download', 'click', () => { if (result) download(result.blob, result.name); });
