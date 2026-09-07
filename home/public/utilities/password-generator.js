import { $, on, status, copy, integer, busy } from './common.js';
let mode = 'password', words = null;
function randomInt(max) { const buffer = new Uint32Array(1), limit = 4294967296 - 4294967296 % max; do { crypto.getRandomValues(buffer); } while (buffer[0] >= limit); return buffer[0] % max; }
for (const type of ['password', 'phrase']) on(`${type}-mode`, 'click', () => {
  mode = type; $('password-mode').setAttribute('aria-pressed', String(type === 'password')); $('phrase-mode').setAttribute('aria-pressed', String(type === 'phrase'));
  $('password-options').hidden = type !== 'password'; $('phrase-options').hidden = type !== 'phrase'; $('password-output').value = '';
});
on('password-generate', 'click', () => busy([$('password-generate')], async () => {
  $('password-output').value = ''; let result;
  if (mode === 'phrase') {
    const count = integer($('phrase-count').value, 4, 12, 'Word count');
    if (!words) { const response = await fetch('/vendor/words.json'); if (!response.ok) throw Error('The wordlist could not load. Try again.'); words = await response.json(); }
    if (words.length !== 1296) throw Error('The wordlist is incomplete.');
    result = Array.from({ length: count }, () => words[randomInt(words.length)]).join($('phrase-separator').value);
  } else {
    const length = integer($('password-length').value, 8, 128, 'Length');
    const groups = [['upper', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'], ['lower', 'abcdefghijklmnopqrstuvwxyz'], ['digits', '0123456789'], ['symbols', '!@#$%^&*()-_=+[]{};:,.?']].filter(([id]) => $(`password-${id}`).checked).map(([, alphabet]) => alphabet);
    if (!groups.length) throw Error('Select at least one character group.'); const alphabet = groups.join('');
    const chars = groups.map(group => group[randomInt(group.length)]); while (chars.length < length) chars.push(alphabet[randomInt(alphabet.length)]);
    for (let i = chars.length - 1; i > 0; i--) { const j = randomInt(i + 1); [chars[i], chars[j]] = [chars[j], chars[i]]; } result = chars.join('');
  }
  $('password-output').value = result; status('Generated on this device.');
}));
on('password-copy', 'click', () => copy($('password-output').value)); on('password-clear', 'click', () => { $('password-output').value = ''; });
