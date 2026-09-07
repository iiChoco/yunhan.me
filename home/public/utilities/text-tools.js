import { $, on, status, copy, download, loadScript } from './common.js';
const ready = loadScript('/vendor/diff.js'); ready.catch(err => status(err.message, true));
function count() { const s = $('text-input').value; $('text-count').textContent = `${(s.match(/[\p{L}\p{N}]+(?:['’-][\p{L}\p{N}]+)*/gu) || []).length} words · ${[...s].length} characters · ${s ? s.split(/\r?\n/).length : 0} lines`; $('text-diff').hidden = true; }
on('text-input', 'input', count); on('text-other', 'input', () => { $('text-diff').hidden = true; });
for (const button of document.querySelectorAll('[data-text]')) button.addEventListener('click', () => {
  let text = $('text-input').value;
  if (button.dataset.text === 'upper') text = text.toUpperCase();
  if (button.dataset.text === 'lower') text = text.toLowerCase();
  if (button.dataset.text === 'title') text = text.toLowerCase().replace(/(^|[^\p{L}\p{N}])(\p{L})/gu, (_, prefix, c) => prefix + c.toUpperCase());
  if (button.dataset.text === 'trim') text = text.split('\n').map(line => line.trim()).join('\n');
  if (button.dataset.text === 'dedupe') text = [...new Set(text.split(/\r?\n/))].join('\n');
  $('text-input').value = text; count(); status('Text updated.');
});
on('text-copy', 'click', () => copy($('text-input').value));
on('text-download', 'click', () => download(new Blob([$ ('text-input').value], { type: 'text/plain;charset=utf-8' }), 'text.txt'));
on('text-compare', 'click', async () => {
  const left = $('text-input').value, right = $('text-other').value;
  if (left.length > 100000 || right.length > 100000) throw Error('Compare up to 100,000 characters per side.');
  await ready; const changes = Diff.diffLines(left, right, { timeout: 1000, maxEditLength: 4000 }); if (!changes) throw Error('These texts are too different for a quick comparison. Try a smaller section.');
  const output = $('text-diff'); output.replaceChildren(); output.hidden = false;
  if (changes.every(c => !c.added && !c.removed)) { output.textContent = 'The texts are identical.'; return; }
  for (const part of changes) { const span = document.createElement('span'); span.className = part.added ? 'added' : part.removed ? 'removed' : ''; const prefix = part.added ? '+ ' : part.removed ? '− ' : '  '; span.textContent = prefix + part.value.replace(/\n(?=.)/g, '\n' + prefix); output.append(span); }
});
