# The Instrument

yunhan.me's design language, as one stylesheet: `instrument.css`. Cyan is structure, gold is voice, the cut-corner chip is the only shape, and it is dark only.

The token values are the same as Ciel's `chart.html` `:root` block, which remains the canonical statement. This file adds the shared components (chips, panels, captions, corners, scanlines, inputs, stat tiles) and the validated chart palette.

- The door serves it at `/instrument.css` for its own pages.
- Pages that must render offline (Ciel's Chart, the interview room, math) keep a vendored copy inline; bump the version comment at the top when the tokens change and re-copy.

Markup fragments that go with it:

```html
<div id="scan"></div>
<div class="corner tl"></div><div class="corner tr"></div><div class="corner bl"></div><div class="corner br"></div>
<span class="brand-mark">
  <svg class="mark-still" viewBox="0 0 128 128" fill="none" aria-hidden="true"><g stroke="#b6c6cd" stroke-opacity=".75" stroke-width="4"><ellipse cx="64" cy="64" rx="46" ry="17" transform="rotate(-38 64 64)"/><ellipse cx="64" cy="64" rx="40" ry="14" transform="rotate(38 64 64)"/><ellipse cx="64" cy="64" rx="33" ry="11" transform="rotate(90 64 64)"/></g><circle cx="64" cy="64" r="4" fill="#fff"/></svg>
  <canvas class="mark-live" aria-hidden="true"></canvas>
</span>
```

The brand mark is Ciel's living mark. Small marks show only what lives inside
the iris; a box with `data-mark="whole"` takes the whole instrument. Load
`/ciel-mark.js` then `/brand-mark.js` (both `defer`) and the canvas replaces the
still; without them the still stays. The engine's source is Ciel's `chart.html`;
`home/public/ciel-mark.js` is the copy every page here loads. v2 of the
stylesheet (2026-09-20) replaced the aperture glyph's rules with `.brand-mark`.
