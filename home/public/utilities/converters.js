import { $, on, status, copy } from './common.js';
const units = {
  Length: { Meter: 1, Kilometer: 1000, Centimeter: .01, Millimeter: .001, Inch: .0254, Foot: .3048, Yard: .9144, Mile: 1609.344 },
  Mass: { Kilogram: 1, Gram: .001, Milligram: .000001, Pound: .45359237, Ounce: .028349523125 },
  Temperature: { Celsius: 1, Fahrenheit: 1, Kelvin: 1 },
  Area: { 'Square meter': 1, 'Square kilometer': 1000000, 'Square foot': .09290304, Acre: 4046.8564224, Hectare: 10000 },
  Volume: { Liter: 1, Milliliter: .001, 'Cubic meter': 1000, 'US gallon': 3.785411784, 'US fluid ounce': .0295735295625, 'US cup': .2365882365 },
  Speed: { 'Meters / second': 1, 'Kilometers / hour': 1 / 3.6, 'Miles / hour': .44704, Knot: .5144444444444445 },
  Data: { Byte: 1, Bit: .125, 'Kilobyte (1000)': 1000, 'Megabyte (1000²)': 1000000, 'Gigabyte (1000³)': 1e9, 'Kibibyte (1024)': 1024, 'Mebibyte (1024²)': 1048576, 'Gibibyte (1024³)': 1073741824 }
};
function options(select, values) { select.replaceChildren(...values.map(value => { const option = document.createElement('option'); option.value = option.textContent = value; return option; })); }
function category() { const keys = Object.keys(units[$('unit-category').value]); options($('unit-from'), keys); options($('unit-to'), keys); $('unit-to').selectedIndex = 1; convert(); }
function convert() {
  $('unit-output').textContent = ''; const n = Number($('unit-value').value); if (!$('unit-value').value.trim() || !Number.isFinite(n)) throw Error('Enter a finite number.');
  const from = $('unit-from').value, to = $('unit-to').value, group = $('unit-category').value; let result;
  if (group === 'Temperature') { const c = from === 'Fahrenheit' ? (n - 32) * 5 / 9 : from === 'Kelvin' ? n - 273.15 : n; result = to === 'Fahrenheit' ? c * 9 / 5 + 32 : to === 'Kelvin' ? c + 273.15 : c; }
  else result = n * units[group][from] / units[group][to];
  if (!Number.isFinite(result)) throw Error('This result is outside the supported numeric range.');
  $('unit-output').textContent = `${Number(result.toPrecision(12))} ${to}`;
}
on('unit-category', 'change', category); for (const id of ['unit-value', 'unit-from', 'unit-to']) on(id, id === 'unit-value' ? 'input' : 'change', convert); category();
for (const button of document.querySelectorAll('[data-converter]')) button.addEventListener('click', () => {
  for (const b of document.querySelectorAll('[data-converter]')) b.setAttribute('aria-pressed', String(b === button));
  for (const panel of document.querySelectorAll('[data-converter-panel]')) panel.hidden = panel.dataset.converterPanel !== button.dataset.converter; status();
});
function timestamp() {
  $('stamp-output').textContent = ''; const raw = $('stamp-input').value.trim(); if (!/^-?\d+(?:\.\d+)?$/.test(raw)) throw Error('Enter a numeric timestamp.');
  const date = new Date(Number(raw) * Number($('stamp-unit').value)); if (!Number.isFinite(date.getTime())) throw Error('This timestamp is outside the supported date range.');
  $('stamp-date').value = date.toISOString(); $('stamp-output').textContent = date.toISOString();
}
on('stamp-decode', 'click', timestamp); on('stamp-now', 'click', () => { $('stamp-input').value = String(Math.floor(Date.now() / Number($('stamp-unit').value))); timestamp(); });
on('stamp-encode', 'click', () => {
  $('stamp-output').textContent = ''; const raw = $('stamp-date').value.trim();
  if (!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:\d{2})$/i.test(raw)) throw Error('Use an ISO date with Z or an explicit offset, for example 2024-01-01T00:00:00Z.');
  const [year, month, day, hour, minute, second = 0] = raw.match(/^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})(?::(\d{2}))?/).slice(1).map(n => n === undefined ? 0 : Number(n));
  const days = [31, year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  if (month < 1 || month > 12 || day < 1 || day > days[month - 1] || hour > 23 || minute > 59 || second > 59) throw Error('This date is invalid.');
  const date = new Date(raw); if (!Number.isFinite(date.getTime())) throw Error('This date is invalid.');
  const value = date.getTime() / Number($('stamp-unit').value); $('stamp-input').value = value; $('stamp-output').textContent = String(value);
});
const zones = [...new Set(['UTC', Intl.DateTimeFormat().resolvedOptions().timeZone, ...(Intl.supportedValuesOf ? Intl.supportedValuesOf('timeZone') : ['America/Los_Angeles', 'America/New_York', 'Europe/London', 'Asia/Shanghai', 'Asia/Tokyo'])])].sort();
options($('zone-from'), zones); options($('zone-to'), zones); $('zone-from').value = Intl.DateTimeFormat().resolvedOptions().timeZone; $('zone-to').value = 'UTC';
const now = new Date(); $('zone-date').value = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}T${String(now.getHours()).padStart(2, '0')}:${String(now.getMinutes()).padStart(2, '0')}`;
function parts(date, zone) {
  return Object.fromEntries(new Intl.DateTimeFormat('en-CA', { timeZone: zone, year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', second: '2-digit', hourCycle: 'h23' }).formatToParts(date).filter(p => p.type !== 'literal').map(p => [p.type, Number(p.value)]));
}
function asUTC(p) { const d = new Date(0); d.setUTCFullYear(p.year, p.month - 1, p.day); d.setUTCHours(p.hour, p.minute, p.second, 0); return d.getTime(); }
on('zone-convert', 'click', () => {
  $('zone-output').textContent = ''; $('zone-note').textContent = '';
  const raw = $('zone-date').value; if (!raw) throw Error('Choose a date and time.');
  const nominal = new Date(raw.length === 16 ? raw + ':00Z' : raw + 'Z').getTime(); if (!Number.isFinite(nominal)) throw Error('Choose a valid date and time.');
  const from = $('zone-from').value, to = $('zone-to').value, offsets = new Set();
  // Find both neighboring UTC offsets so daylight-saving gaps and repeats are explicit.
  for (let hour = -36; hour <= 36; hour += 6) { const sample = nominal + hour * 3600000; offsets.add(asUTC(parts(new Date(sample), from)) - sample); }
  const candidates = [...offsets].map(offset => nominal - offset).filter(time => asUTC(parts(new Date(time), from)) === nominal).sort((a, b) => a - b);
  if (!candidates.length) throw Error('That local time does not exist because the clocks move forward. Choose a different time.');
  $('zone-output').textContent = new Intl.DateTimeFormat('en-US', { timeZone: to, dateStyle: 'full', timeStyle: 'long' }).format(new Date(candidates[0]));
  $('zone-note').textContent = candidates.length > 1 ? 'This time occurs twice when clocks move back. The earlier occurrence is shown.' : `${from} → ${to}`;
});
for (const mode of ['encode', 'decode']) on(`encoding-${mode}`, 'click', () => {
  $('encoding-output').value = ''; const input = $('encoding-input').value; let result;
  if ($('encoding-type').value === 'url') result = mode === 'encode' ? encodeURIComponent(input) : decodeURIComponent(input);
  else if (mode === 'encode') { const bytes = new TextEncoder().encode(input); let binary = ''; for (let i = 0; i < bytes.length; i += 8192) binary += String.fromCharCode(...bytes.subarray(i, i + 8192)); result = btoa(binary); }
  else { const binary = atob(input.replace(/\s/g, '')); result = new TextDecoder('utf-8', { fatal: true }).decode(Uint8Array.from(binary, c => c.charCodeAt(0))); }
  $('encoding-output').value = result;
});
on('encoding-copy', 'click', () => copy($('encoding-output').value));
