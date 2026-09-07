import { $, on, status, integer } from './common.js';
let running = false, started = 0, elapsed = 0, remaining = 300000, deadline = 0, sound = null, laps = 0;
const title = document.title;
function mode() { return $('timer-mode').value; }
function format(ms) { const tenths = Math.max(0, Math.floor(ms / 100)), seconds = Math.floor(tenths / 10), hours = Math.floor(seconds / 3600); return `${hours ? hours + ':' : ''}${String(Math.floor(seconds / 60) % 60).padStart(2, '0')}:${String(seconds % 60).padStart(2, '0')}.${tenths % 10}`; }
function duration() { return (integer($('timer-minutes').value, 0, 1440, 'Minutes') * 60 + integer($('timer-seconds').value, 0, 59, 'Seconds')) * 1000; }
function current() { return mode() === 'stopwatch' ? elapsed + (running ? performance.now() - started : 0) : running ? Math.max(0, deadline - Date.now()) : remaining; }
function lock() { $('timer-minutes').disabled = $('timer-seconds').disabled = running; $('timer-mode').disabled = running; document.querySelectorAll('[data-minutes]').forEach(b => { b.disabled = running; }); }
function paint() { const time = current(); $('timer-display').textContent = format(time); if (running) document.title = `${format(time).split('.')[0]} · Timer`; }
function beep() {
  if (!$('timer-sound').checked || !sound) return;
  try { const oscillator = sound.createOscillator(), gain = sound.createGain(); oscillator.frequency.value = 660; oscillator.connect(gain); gain.connect(sound.destination); gain.gain.setValueAtTime(.15, sound.currentTime); gain.gain.exponentialRampToValueAtTime(.001, sound.currentTime + .7); oscillator.start(); oscillator.stop(sound.currentTime + .7); } catch { /* Timing still works when audio is unavailable. */ }
}
function reset() { running = false; elapsed = 0; remaining = mode() === 'stopwatch' ? 0 : duration(); $('timer-start').textContent = 'Start'; $('timer-laps').replaceChildren(); laps = 0; lock(); paint(); document.title = title; }
on('timer-mode', 'change', () => { $('timer-duration').hidden = mode() === 'stopwatch'; $('timer-lap').hidden = mode() !== 'stopwatch'; $('timer-presets').hidden = mode() !== 'focus'; if (mode() === 'focus') { $('timer-minutes').value = 25; $('timer-seconds').value = 0; } reset(); });
for (const id of ['timer-minutes', 'timer-seconds']) on(id, 'change', () => { if (!running) { remaining = duration(); paint(); } });
for (const button of document.querySelectorAll('[data-minutes]')) button.addEventListener('click', () => { $('timer-minutes').value = button.dataset.minutes; $('timer-seconds').value = 0; reset(); status(); });
on('timer-start', 'click', async () => {
  if (running) { if (mode() === 'stopwatch') elapsed = current(); else remaining = current(); running = false; $('timer-start').textContent = 'Resume'; lock(); paint(); document.title = title; return; }
  if (mode() !== 'stopwatch') { if ($('timer-start').textContent === 'Start') remaining = duration(); if (remaining <= 0) throw Error('Set a duration greater than zero.'); deadline = Date.now() + remaining; }
  if ($('timer-sound').checked) { try { sound ||= new (window.AudioContext || window.webkitAudioContext)(); if (sound.state === 'suspended') await sound.resume(); } catch { status('Timer works, but this browser could not enable the finish sound.'); } }
  started = performance.now(); running = true; $('timer-start').textContent = 'Pause'; lock(); paint();
});
on('timer-reset', 'click', reset);
on('timer-lap', 'click', () => { if (!running && !elapsed) return; const item = document.createElement('li'); item.textContent = `Lap ${++laps} · ${format(current())}`; $('timer-laps').prepend(item); });
setInterval(() => { if (!running) return; if (mode() !== 'stopwatch' && current() <= 0) { running = false; remaining = 0; $('timer-start').textContent = 'Start'; lock(); beep(); status(mode() === 'focus' ? 'Session complete. Take a moment before your next one.' : 'Time is up.'); document.title = 'Time is up · Timer'; } paint(); }, 100);
paint();
