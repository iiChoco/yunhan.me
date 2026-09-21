/* Mounts Ciel's living mark in every .brand-mark on the page, after
   ciel-mark.js. A small mark is only what lives inside the iris; a box
   marked data-mark="whole" takes the whole instrument. Each box already
   holds a still drawing, which stays in place when this file, the engine,
   or JavaScript is missing. The landing page wires its own marks, because
   its launcher wakes them; every other page loads this. */
(function () {
'use strict';
if (!window.CielSymbol2) return;
const marks = Array.from(document.querySelectorAll('.brand-mark canvas'), canvas => {
  const inst = new CielSymbol2(canvas, {concept: 'final'});
  inst.coreOnly = canvas.parentElement.dataset.mark !== 'whole';
  return inst;
});
if (!marks.length) return;
document.documentElement.classList.add('mark-on');
// A page that keeps its state on <body data-state> (Zetamac does) has its
// mark follow along; states the engine does not know leave it where it was.
const follow = () => { const st = document.body.dataset.state; if (CielSymbol2.COLORS[st]) for (const m of marks) m.setState(st); };
if (document.body.dataset.state) { follow(); new MutationObserver(follow).observe(document.body, {attributes: true, attributeFilter: ['data-state']}); }
new ResizeObserver(() => { for (const m of marks) m.resize(); }).observe(marks[0].canvas);
let last = performance.now();
const frame = now => {
  const dt = Math.min(.05, (now - last) / 1000); last = now;
  for (const m of marks) m.tick(dt);
  requestAnimationFrame(frame);
};
requestAnimationFrame(frame);
})();
