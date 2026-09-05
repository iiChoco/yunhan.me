# The Instrument

yunhan.me's design language, as one stylesheet: `instrument.css`. Cyan is structure, gold is voice, the cut-corner chip is the only shape, and it is dark only.

The token values are the same as Ciel's `chart.html` `:root` block, which remains the canonical statement. This file adds the shared components (chips, panels, captions, corners, scanlines, inputs, stat tiles) and the validated chart palette.

- The door serves it at `/instrument.css` for its own pages.
- Pages that must render offline (Ciel's Chart, the interview room, math) keep a vendored copy inline; bump the version comment at the top when the tokens change and re-copy.

Markup fragments that go with it:

```html
<div id="scan"></div>
<div class="corner tl"></div><div class="corner tr"></div><div class="corner bl"></div><div class="corner br"></div>
<svg class="aperture" width="26" height="26" viewBox="0 0 128 128" aria-hidden="true">
  <circle class="c-outer" cx="64" cy="64" r="58" fill="none" stroke-width="5" stroke-dasharray="4 12"/>
  <circle class="c-mid" cx="64" cy="64" r="34" fill="none" stroke-width="5"/>
  <circle class="c-core" cx="64" cy="64" r="10"/>
</svg>
```
