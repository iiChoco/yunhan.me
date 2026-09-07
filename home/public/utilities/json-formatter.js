import { $, on, status, copy, download } from './common.js';
function parse() {
  const raw = $('json-input').value; if (!raw.trim()) throw Error('Enter JSON first.');
  const value = JSON.parse(raw);
  // A formatter must not silently round large integer identifiers.
  const tokens = raw.replace(/"(?:\\.|[^"\\])*"/g, '""').match(/-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?/g) || [];
  if (tokens.some(token => !Number.isFinite(Number(token)) || (Number.isInteger(Number(token)) && !Number.isSafeInteger(Number(token))))) throw Error('A number exceeds JavaScript’s safe range. Store large identifiers as quoted strings before formatting.');
  return value;
}
let cursor = 0;
on('json-input', 'input', () => { $('json-output').value = ''; $('json-found').textContent = ''; cursor = 0; });
for (const mode of ['format', 'minify', 'validate']) on(`json-${mode}`, 'click', () => {
  const value = parse(); if (mode !== 'validate') $('json-output').value = JSON.stringify(value, null, mode === 'format' ? Number($('json-indent').value) : 0); cursor = 0; status('Valid JSON.');
});
on('json-copy', 'click', () => copy($('json-output').value));
on('json-download', 'click', () => { if (!$('json-output').value) throw Error('Format or minify the JSON first.'); download(new Blob([$ ('json-output').value], { type: 'application/json' }), 'formatted.json'); });
on('json-search', 'input', () => { cursor = 0; $('json-found').textContent = ''; });
on('json-find', 'click', () => {
  const query = $('json-search').value, output = $('json-output'); if (!query) throw Error('Enter something to find.');
  const lower = output.value.toLowerCase(), needle = query.toLowerCase(); let index = lower.indexOf(needle, cursor); if (index < 0) index = lower.indexOf(needle);
  if (index < 0) { $('json-found').textContent = 'No matches.'; return; }
  output.focus(); output.setSelectionRange(index, index + query.length); cursor = index + query.length;
  let count = 0, pos = 0; while ((pos = lower.indexOf(needle, pos)) >= 0) { count++; pos += needle.length; }
  $('json-found').textContent = `${count} match${count === 1 ? '' : 'es'} · selected at character ${index + 1}`;
});
