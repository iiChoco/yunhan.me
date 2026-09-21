/* Ciel symbol engine v2 — the living mark. 2D canvas, additive light, no deps.
   Copied from the inlined block in Ciel's src/ciel/remote/chart.html
   (2026-09-20), which carries the design project's ciel-engine2.js without
   its unused aurora concept. Ciel's copy is the source: change it there,
   then re-copy here and bump the ?v= on the pages that load this file.
   new CielSymbol2(canvas, {concept, autoVoice, reducedMotion}) .setState() .wake() .setAmplitude() .tick(dt) .resize() */
(function (root) {
'use strict';
const TAU = Math.PI*2;
const COLORS = { idle:[143,168,179], listening:[122,222,168], thinking:[232,201,138], reasoning:[184,155,232], deep:[143,156,255], speaking:[160,240,255], error:[232,138,138] };
const HEX = { idle:'#8fa8b3', listening:'#7adea8', thinking:'#e8c98a', reasoning:'#b89be8', deep:'#8f9cff', speaking:'#a0f0ff', error:'#e88a8a' };
const ORDER = ['idle','listening','thinking','reasoning','speaking','error'];
const ORDER7 = ['idle','listening','thinking','reasoning','deep','speaking','error'];
const clamp = (v,a,b) => v<a?a:v>b?b:v, lerp = (a,b,t) => a+(b-a)*t, frac = x => x-Math.floor(x), sq = x => x*x;
const approach = (c,t,r,dt) => c+(t-c)*(1-Math.exp(-r*dt));
const smooth = x => x*x*(3-2*x);
const rgba = (c,a) => 'rgba('+(c[0]|0)+','+(c[1]|0)+','+(c[2]|0)+','+clamp(a,0,1).toFixed(3)+')';
const mix = (c,d,t) => [lerp(c[0],d[0],t), lerp(c[1],d[1],t), lerp(c[2],d[2],t)];
const WHITE = [255,255,255];

const TARGETS = {
  knot: {
    idle:      { r0:0.45, spin:0.25, tilt:0.9,  bSpeed:0.04, bAlpha:0.5, voiceR:0,   bright:0.75, fade:0.3,  rev:0 },
    listening: { r0:0.3,  spin:0,    tilt:0.35, bSpeed:0.12, bAlpha:0.9, voiceR:0.4, bright:1,    fade:0.3,  rev:0 },
    thinking:  { r0:0.5,  spin:1.2,  tilt:1.1,  bSpeed:0.3,  bAlpha:0.7, voiceR:0,   bright:0.7,  fade:0.34, rev:0 },
    reasoning: { r0:0.42, spin:0.12, tilt:0.18, bSpeed:0.1,  bAlpha:1,   voiceR:0,   bright:1.15, fade:0.2,  rev:1 },
    speaking:  { r0:0.4,  spin:0.15, tilt:0.5,  bSpeed:0.06, bAlpha:0.7, voiceR:1,   bright:1,    fade:0.3,  rev:0 },
    error:     { r0:0.15, spin:0,    tilt:1.5,  bSpeed:0,    bAlpha:0.2, voiceR:0,   bright:0.55, fade:0.5,  rev:0 }
  },
  eclipse: {
    idle:      { Rd:0.22, ring:0.35, corona:0.6, spin:0.05, prom:0, dbl:0, off:0,    bright:0.75, voiceL:0.1, beads:0, bias:0, fade:0.25, shim:1   },
    listening: { Rd:0.2,  ring:1,    corona:0.9, spin:0,    prom:0, dbl:0, off:0,    bright:1,    voiceL:0.5, beads:0, bias:1, fade:0.3,  shim:0.4 },
    thinking:  { Rd:0.22, ring:0.4,  corona:0.7, spin:0.9,  prom:1, dbl:0, off:0,    bright:0.7,  voiceL:0,   beads:0, bias:0, fade:0.35, shim:2   },
    reasoning: { Rd:0.21, ring:0.7,  corona:0.5, spin:0.15, prom:0, dbl:1, off:0,    bright:0.9,  voiceL:0,   beads:1, bias:0, fade:0.25, shim:0.6 },
    speaking:  { Rd:0.22, ring:0.8,  corona:0.7, spin:0.03, prom:0, dbl:0, off:0,    bright:1,    voiceL:1.2, beads:0, bias:0, fade:0.3,  shim:1   },
    error:     { Rd:0.22, ring:0.5,  corona:0.3, spin:0,    prom:0, dbl:0, off:0.16, bright:0.6,  voiceL:0,   beads:0, bias:0, fade:0.4,  shim:0.2 }
  }
};
const HUD = {
  idle:      { hudSpin:0.12, hudArcs:0.5,  hudSpec:0,   hudSplit:0, hudDash:0, hudBright:0.55 },
  listening: { hudSpin:0.02, hudArcs:0.9,  hudSpec:0.7, hudSplit:0, hudDash:0, hudBright:0.9 },
  thinking:  { hudSpin:1.6,  hudArcs:0.35, hudSpec:0,   hudSplit:0, hudDash:0, hudBright:0.7 },
  reasoning: { hudSpin:-0.3, hudArcs:0.6,  hudSpec:0,   hudSplit:1, hudDash:0, hudBright:0.8 },
  speaking:  { hudSpin:0.05, hudArcs:0.7,  hudSpec:1.3, hudSplit:0, hudDash:0, hudBright:0.9 },
  error:     { hudSpin:0,    hudArcs:0.3,  hudSpec:0,   hudSplit:0, hudDash:1, hudBright:0.45 }
};
TARGETS.armillary = {
  idle:      { align:0,   spread:1,   spin:0.2,  split:0, voiceR:0,   face:0.25, bright:0.75, fade:0.3 },
  listening: { align:1,   spread:1,   spin:0.05, split:0, voiceR:0.3, face:1.5,  bright:1,    fade:0.3 },
  thinking:  { align:0,   spread:1.4, spin:1.3,  split:0, voiceR:0,   face:0.25, bright:0.7,  fade:0.34 },
  reasoning: { align:0,   spread:0.8, spin:0.3,  split:1, voiceR:0,   face:0.25, bright:0.9,  fade:0.25 },
  speaking:  { align:0.6, spread:1,   spin:0.15, split:0, voiceR:1,   face:1.5,  bright:1,    fade:0.3 },
  error:     { align:1,   spread:1,   spin:0,    split:0, voiceR:0,   face:0.02, bright:0.55, fade:0.5 }
};
const IRIS = { idle:{ open:0.35 }, listening:{ open:1 }, thinking:{ open:0.6 }, reasoning:{ open:0.5 }, speaking:{ open:0.8 }, error:{ open:0.1 } };
const merge = (core, extra) => { const o = {}; for (const s in core) o[s] = Object.assign({}, core[s], HUD[s], extra ? extra[s] : null); return o; };
TARGETS.armillary = merge(TARGETS.armillary); TARGETS.iris = merge(TARGETS.eclipse, IRIS);
const IRIS4 = {
  idle:      { spike:0.5,  ringDash:0, corona:0.7 },
  listening: { spike:0.55, ringDash:0, corona:0.9 },
  thinking:  { spike:0.5,  ringDash:0, corona:0.8 },
  reasoning: { spike:0.45, ringDash:0, corona:0.6 },
  speaking:  { spike:0.6,  ringDash:0, corona:0.8 },
  error:     { spike:0.3,  ringDash:1, corona:0.35, off:0, open:0, ring:0.4, bright:0.5, shim:0.15, hudArcs:0.25 }
};
const merge2 = (base, extra) => { const o = {}; for (const s in base) o[s] = Object.assign({}, base[s], extra[s]); return o; };
TARGETS.irisKnot = merge2(TARGETS.iris, IRIS4);
for (const s in TARGETS.knot) { const k = TARGETS.knot[s]; Object.assign(TARGETS.irisKnot[s], { r0:k.r0, tilt:k.tilt, bSpeed:k.bSpeed, bAlpha:k.bAlpha, voiceR:k.voiceR, rev:k.rev, kspin:k.spin }); }
TARGETS.final = merge2(TARGETS.irisKnot, {});
{ const W = { idle:[1,0,0], listening:[0,1,0], thinking:[1,0,0], reasoning:[0,1,0], speaking:[1,0,0], error:[0,0,1] };
  for (const s in TARGETS.final) { const a = TARGETS.armillary[s], k = TARGETS.knot[s], f = TARGETS.final[s];
    Object.assign(f, { align:a.align, spread:a.spread, split:a.split, face:a.face, kspinA:a.spin, kspinK:k.spin, wArm:W[s][0], wKnot:W[s][1], wLens:W[s][2], voiceR: W[s][0] ? a.voiceR : k.voiceR }); }
  TARGETS.final.error.open = 0; TARGETS.final.reasoning.open = 1; TARGETS.final.reasoning.corona = 0.45; TARGETS.final.reasoning.Rd = 0.29; TARGETS.final.reasoning.ring = 0.55; }
TARGETS.final.deep = Object.assign({}, TARGETS.final.reasoning, { open:1, Rd:0.3, fade:0.25, kspinK:0.18, bSpeed:0.14 });
const KNOTS = { idle:[2,3], listening:[1,3], thinking:[3,7], reasoning:'inf', deep:'mob', speaking:[2,3], error:[1,0] };
const RATES = { wArm:3, wKnot:3, wLens:2, ringDash:2, spike:2, align:2, split:1, face:3, open:2.5, hudArcs:2, hudSplit:1.2, hudDash:2, tilt:3, off:2.5, dbl:1.2, prom:2, Rd:3, r0:2, corona:2.5 };

class CielSymbol2 {
  constructor(canvas, opts) {
    opts = opts || {};
    this.canvas = canvas; this.ctx = canvas.getContext('2d');
    this.concept = 'final';
    this.state = 'idle'; this.amp = 0; this.ampS = 0; this.t = 0; this.clock = 0; this.breathT = 0; this.wakeT = 9; this.dt = 0.016;
    this.reduced = opts.reducedMotion != null ? opts.reducedMotion : (typeof matchMedia !== 'undefined' && matchMedia('(prefers-reduced-motion: reduce)').matches);
    this.autoVoice = !!opts.autoVoice;
    this.col = COLORS.idle.slice(); this.p = {}; this.spr = {}; this.spin = 0;
    this.beads = []; for (let i = 0; i < 36; i++) this.beads.push({ u: Math.random(), s: 0.7+0.6*Math.random() });
    this.dpr = Math.min(2, (typeof devicePixelRatio !== 'undefined' ? devicePixelRatio : 1) || 1);
    this.resize();
  }
  resize() {
    const c = this.canvas, r = c.getBoundingClientRect();
    const w = Math.max(1, r.width || c.clientWidth || 300), h = Math.max(1, r.height || c.clientHeight || 300);
    this.w = w; this.h = h;
    const pw = Math.round(w*this.dpr), ph = Math.round(h*this.dpr);
    if (c.width !== pw || c.height !== ph) { c.width = pw; c.height = ph; }
  }
  setState(s) { if (COLORS[s] && s !== this.state) this.state = s; }
  wake() { this.wakeT = 0; this.setState('listening'); }
  setAmplitude(a) { this.amp = clamp(+a || 0, 0, 1); }
  voice(t) {
    const phrase = Math.sin(t*0.5)+0.6*Math.sin(t*0.23) > -0.2 ? 1 : 0;
    const syll = Math.max(0, 0.45*Math.sin(t*5.8)+0.35*Math.sin(t*9.3+1)+0.3*Math.sin(t*2.7)+0.25);
    return clamp(syll*phrase, 0, 1);
  }
  tick(dt) {
    dt = Math.min(dt || 0.016, 0.05); this.dt = dt;
    const mot = this.reduced ? 0 : 1;
    this.t += dt*mot; this.clock += dt; this.breathT += dt*(this.reduced ? 0.5 : 0.9); this.wakeT += dt;
    const raw = this.autoVoice ? this.voice(this.clock) : this.amp;
    this.ampS = approach(this.ampS, raw, raw > this.ampS ? 28 : 7, dt);
    const tg = TARGETS[this.concept][this.state];
    for (const k in tg) { const r = RATES[k] || 3; this.p[k] = this.p[k] === undefined ? tg[k] : approach(this.p[k], tg[k], r, dt); }
    const c = COLORS[this.state]; for (let i = 0; i < 3; i++) this.col[i] = approach(this.col[i], c[i], 4, dt);
    this.draw();
  }
  sprite(kind) {
    const col = this.col, key = (col[0]>>3)+','+(col[1]>>3)+','+(col[2]>>3);
    const s = this.spr[kind]; if (s && s.key === key) return s.c;
    const c = document.createElement('canvas'), g = c.getContext('2d');
    c.width = c.height = 64;
    const gr = g.createRadialGradient(32, 32, 0, 32, 32, 32);
    gr.addColorStop(0, rgba(mix(col, WHITE, 0.7), 1)); gr.addColorStop(0.18, rgba(col, 0.75)); gr.addColorStop(0.5, rgba(col, 0.18)); gr.addColorStop(1, rgba(col, 0));
    g.fillStyle = gr; g.fillRect(0, 0, 64, 64);
    this.spr[kind] = { key: key, c: c }; return c;
  }
  draw() {
    const ctx = this.ctx, S = Math.min(this.w, this.h);
    ctx.setTransform(this.dpr, 0, 0, this.dpr, 0, 0);
    ctx.globalAlpha = 1; ctx.setLineDash([]); ctx.lineCap = 'round'; ctx.lineJoin = 'round';
    if (S < 40 || this.reduced) { ctx.globalCompositeOperation = 'source-over'; ctx.clearRect(0, 0, this.w, this.h); }
    else { ctx.globalCompositeOperation = 'destination-out'; ctx.fillStyle = 'rgba(0,0,0,'+clamp(this.p.fade || 0.3, 0.1, 1).toFixed(2)+')'; ctx.fillRect(0, 0, this.w, this.h); }
    ctx.globalCompositeOperation = 'lighter';
    if (this.coreOnly) { this.drawCoreOnly(ctx); ctx.globalCompositeOperation = 'source-over'; ctx.globalAlpha = 1; return; }
    this.drawHUD(ctx);
    const p = this.p; this.coreScale = 0.68; this.drawEclipse(ctx);
    const ap = this.aperture(); ctx.save(); ctx.beginPath(); ctx.arc(ap.x, ap.y, Math.max(1, ap.r), 0, TAU); ctx.clip();
    const b = p.bright, sp = this.spin;
    if (p.wArm > 0.02) { p.bright = b*p.wArm; this.coreScale = 0.52; this.spin = this.aspin || 0; this.drawArmillary(ctx, p.kspinA); this.aspin = this.spin; }
    if (p.wKnot > 0.02) { p.bright = b*p.wKnot; const S = Math.min(this.w, this.h), ext = this.kn === 'inf' ? 1.45*1.08 : this.kn === 'mob' ? 1.53*1.18 : (1+p.r0)*1.15; this.coreScale = Math.min(0.4, ap.r*0.9/(ext*0.27*S)); this.spin = this.cspin || 0; this.drawKnot(ctx, p.kspinK); this.cspin = this.spin; }
    p.bright = b; this.spin = sp; this.coreScale = 0.68; ctx.restore();
    this.drawBlades(ctx);
    ctx.globalCompositeOperation = 'source-over'; ctx.globalAlpha = 1;
  }

  /* ---------- Core only: what lives inside the iris, filling the frame (chips, glyphs) ---------- */
  drawCoreOnly(ctx) {
    const p = this.p, b = p.bright, sp = this.spin, S = Math.min(this.w, this.h), cx = this.w/2, cy = this.h/2, col = this.col, wk = this.wakeT;
    if (p.wArm > 0.02) { p.bright = b*p.wArm; this.coreScale = 1.25; this.spin = this.aspin || 0; this.drawArmillary(ctx, p.kspinA); this.aspin = this.spin; }
    if (p.wKnot > 0.02) { p.bright = b*p.wKnot; const ext = this.kn === 'inf' ? 1.45*1.08 : this.kn === 'mob' ? 1.53*1.18 : (1+p.r0)*1.15; this.coreScale = Math.min(1.3, 1.7/ext); this.spin = this.cspin || 0; this.drawKnot(ctx, p.kspinK); this.cspin = this.spin; }
    if (p.wLens > 0.02) { ctx.setLineDash([S*0.06, S*0.1]); ctx.lineWidth = Math.max(1, S*0.03); ctx.strokeStyle = rgba(col, b*p.wLens*(0.7+0.3*Math.sin(this.t*2.2))); ctx.beginPath(); ctx.arc(cx, cy, S*0.36, this.t*0.2, this.t*0.2+TAU); ctx.stroke(); ctx.setLineDash([]); ctx.fillStyle = rgba(col, b*p.wLens*0.9); ctx.beginPath(); ctx.arc(cx, cy, Math.max(1, S*0.04), 0, TAU); ctx.fill(); }
    if (wk < 1) { ctx.strokeStyle = rgba(col, sq(1-wk)*0.7); ctx.lineWidth = Math.max(1, S*0.02); ctx.beginPath(); ctx.arc(cx, cy, S*(0.1+wk*0.4), 0, TAU); ctx.stroke(); }
    p.bright = b; this.spin = sp; this.coreScale = 0.68;
  }

  /* ---------- Knot: one strand of light, many crossings ---------- */
  drawKnot(ctx, spinRate) {
    const p = this.p, t = this.t, dt = this.dt, w = this.w, h = this.h, S = Math.min(w, h), cx = w/2, cy = h/2, small = S < 40, col = this.col, amp = this.ampS, wk = this.wakeT, mot = this.reduced ? 0 : 1;
    const bright = p.bright + (wk < 1.2 ? 0.35*Math.exp(-wk*4) : 0);
    const N = small ? 90 : 220, tgW = TARGETS[this.concept][this.state].wKnot, K0 = KNOTS[this.state], K = ((p.wKnot < 0.5 && !tgW) && this.kn) ? this.kn : K0;
    if (!this.pts || this.pts.length !== N*3) { this.pts = new Float32Array(N*3); this.prev = null; this.kn = K; this.morph = 1; this.proj = new Float32Array(N*4); }
    if (K !== this.kn) { this.prev = this.pts.slice(); this.kn = K; this.morph = 0; }
    this.morph = approach(this.morph, 1, 1.6, dt);
    const m = smooth(clamp(this.morph, 0, 1)), pts = this.pts, prev = this.prev, kn = this.kn;
    for (let i = 0; i < N; i++) {
      const u = i/N, a = TAU*u, r0 = p.r0*(1 + p.voiceR*amp*0.6*Math.sin(u*TAU*4+t*14) + p.voiceR*amp*0.25);
      let x, y, z;
      if (kn === 'inf') { const s = 1.45*(1+0.15*p.voiceR*amp); x = s*Math.cos(a); y = s*0.62*Math.sin(2*a); z = 0.3*Math.sin(a); }
      else if (kn === 'mob') { const A = 2*a, hw = 0.5, rr = 1.03 + hw*Math.cos(A/2) + 0.03*Math.sin(3*A+t*3); x = rr*Math.cos(A); y = rr*Math.sin(A); z = hw*Math.sin(A/2); }
      else { const r = 1 + r0*Math.cos(kn[1]*a); x = r*Math.cos(kn[0]*a); y = r*Math.sin(kn[0]*a); z = r0*Math.sin(kn[1]*a); }
      if (prev && m < 0.999) { x = lerp(prev[i*3], x, m); y = lerp(prev[i*3+1], y, m); z = lerp(prev[i*3+2], z, m); }
      pts[i*3] = x; pts[i*3+1] = y; pts[i*3+2] = z;
    }
    this.spin += (spinRate != null ? spinRate : p.spin)*dt*mot + 0.02*dt*mot;
    const tiltE = p.tilt + (kn === 'mob' ? 0.4*Math.sin(t*0.45) : 0);
    const cs = Math.cos(this.spin), sn = Math.sin(this.spin), ct = Math.cos(tiltE), st = Math.sin(tiltE), R = S*0.27*(this.coreScale || 1)*(1+0.012*Math.sin(this.breathT)), P = this.proj;
    for (let i = 0; i < N; i++) {
      const x = pts[i*3], y = pts[i*3+1], z = pts[i*3+2];
      const x1 = x*cs - z*sn, z1 = x*sn + z*cs, y1 = y*ct - z1*st, z2 = y*st + z1*ct, ps = 1/(1-0.18*z2);
      P[i*4] = cx + x1*R*ps; P[i*4+1] = cy + y1*R*ps; P[i*4+2] = z2; P[i*4+3] = ps;
    }
    const B = 6, segs = this.segs || (this.segs = Array.from({ length: B }, () => []));
    for (let b = 0; b < B; b++) segs[b].length = 0;
    for (let i = 0; i < N; i++) { const j = (i+1)%N, zb = (P[i*4+2]+P[j*4+2])*0.5; segs[clamp(Math.floor((zb+1.6)/3.2*B), 0, B-1)].push(i); }
    for (let pass = 0; pass < (small ? 1 : 2); pass++) for (let b = 0; b < B; b++) {
      const sg = segs[b]; if (!sg.length) continue;
      const df = (b+0.5)/B;
      ctx.beginPath();
      for (let k = 0; k < sg.length; k++) { const i = sg[k], j = (i+1)%N; ctx.moveTo(P[i*4], P[i*4+1]); ctx.lineTo(P[j*4], P[j*4+1]); }
      if (pass === 0 && !small) { ctx.lineWidth = 5+5*df; ctx.strokeStyle = rgba(col, bright*(0.04+0.1*df)); }
      else { const inf = kn === 'inf' ? 1.7 : kn === 'mob' ? 1.3 : 1; ctx.lineWidth = small ? 1 : (0.8+1.1*df)*inf; ctx.strokeStyle = rgba(mix(col, WHITE, (kn === 'inf' ? 0.35 : 0.2)*df), bright*(0.3+0.7*df)*(kn === 'inf' ? 1.3 : 1)); }
      ctx.stroke();
    }
    if (kn === 'mob' && !small) {
      const NA = 96, M = 4, hw = 0.5, NB = 6, M1 = M+1;
      const sp = this.msurf || (this.msurf = new Float32Array((NA+1)*M1*3));
      for (let i = 0; i <= NA; i++) {
        const A = i/NA*TAU*2, cA = Math.cos(A), sA = Math.sin(A), ch = Math.cos(A/2), sh = Math.sin(A/2), rip = 0.03*Math.sin(3*A+t*3);
        for (let j = 0; j <= M; j++) {
          const v = -1+2*j/M, rr = 1.03 + v*hw*ch + rip, x = rr*cA, y = rr*sA, z = v*hw*sh;
          const x1 = x*cs - z*sn, z1 = x*sn + z*cs, y1 = y*ct - z1*st, z2 = y*st + z1*ct, psq = 1/(1-0.18*z2), k = (i*M1+j)*3;
          sp[k] = cx + x1*R*psq; sp[k+1] = cy + y1*R*psq; sp[k+2] = z2;
        }
      }
      const bins = this.mbins || (this.mbins = Array.from({ length: NB }, () => []));
      for (let b = 0; b < NB; b++) bins[b].length = 0;
      for (let i = 0; i < NA; i++) for (let j = 0; j < M; j++) {
        const k00 = (i*M1+j)*3, k01 = k00+3, k10 = ((i+1)*M1+j)*3, k11 = k10+3;
        const ax = sp[k10]-sp[k00], ay = sp[k10+1]-sp[k00+1], bx = sp[k01]-sp[k00], by = sp[k01+1]-sp[k00+1];
        const area = Math.abs(ax*by - ay*bx), facing = clamp(area/((Math.hypot(ax, ay)*Math.hypot(bx, by))||1), 0, 1);
        const zav = (sp[k00+2]+sp[k11+2])*0.5, df = clamp((zav+1.5)/3, 0, 1);
        const al = (0.25+0.75*facing)*(0.35+0.65*df);
        bins[clamp(Math.floor(al*NB), 0, NB-1)].push(k00, k01, k11, k10);
      }
      for (let b = 0; b < NB; b++) {
        const q = bins[b]; if (!q.length) continue;
        ctx.beginPath();
        for (let k = 0; k < q.length; k += 4) { ctx.moveTo(sp[q[k]], sp[q[k]+1]); ctx.lineTo(sp[q[k+1]], sp[q[k+1]+1]); ctx.lineTo(sp[q[k+2]], sp[q[k+2]+1]); ctx.lineTo(sp[q[k+3]], sp[q[k+3]+1]); ctx.closePath(); }
        ctx.fillStyle = rgba(col, bright*0.16*((b+0.5)/NB)); ctx.fill();
      }
      // hologram grid: longitudinal lines and cross rungs
      ctx.lineWidth = 0.7; ctx.strokeStyle = rgba(mix(col, WHITE, 0.2), bright*0.28); ctx.beginPath();
      for (let j = 1; j < M; j++) for (let i = 0; i <= NA; i++) { const k = (i*M1+j)*3; i ? ctx.lineTo(sp[k], sp[k+1]) : ctx.moveTo(sp[k], sp[k+1]); }
      ctx.stroke();
      ctx.strokeStyle = rgba(col, bright*0.16); ctx.beginPath();
      for (let i = 0; i < NA; i += 4) { const k0 = (i*M1)*3, k1 = (i*M1+M)*3; ctx.moveTo(sp[k0], sp[k0+1]); ctx.lineTo(sp[k1], sp[k1+1]); }
      ctx.stroke();
    }
    if (!small) {
      const glow = this.sprite('glow'), core = rgba(mix(col, WHITE, 0.75), Math.min(1, bright));
      for (let k = 0; k < this.beads.length; k++) {
        const bd = this.beads[k], dir = p.rev > 0.5 && (k&1) ? -1 : 1;
        bd.u = frac(bd.u + p.bSpeed*bd.s*dt*mot*dir);
        const fi = bd.u*N, i = Math.floor(fi), j = (i+1)%N, f = fi-i;
        const x = lerp(P[i*4], P[j*4], f), y = lerp(P[i*4+1], P[j*4+1], f), ps = lerp(P[i*4+3], P[j*4+3], f), df = clamp((ps-0.79)/0.58, 0, 1);
        const gs = S*(this.coreScale || 1)*(0.045+0.06*df)*(1+p.voiceR*amp*0.5);
        ctx.globalAlpha = clamp(p.bAlpha*bright*(0.35+0.65*df), 0, 1); ctx.drawImage(glow, x-gs/2, y-gs/2, gs, gs);
        ctx.globalAlpha = 1; ctx.fillStyle = core; ctx.beginPath(); ctx.arc(x, y, 0.8+1.2*df, 0, TAU); ctx.fill();
      }
      if (wk < 1) { ctx.strokeStyle = rgba(col, sq(1-wk)*0.6); ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(cx, cy, S*(0.15+wk*0.45), 0, TAU); ctx.stroke(); }
    }
  }

  /* ---------- HUD: the instrument rings around the core ---------- */
  drawHUD(ctx) {
    const p = this.p, t = this.t, dt = this.dt, w = this.w, h = this.h, S = Math.min(w, h), cx = w/2, cy = h/2, small = S < 40, col = this.col, amp = this.ampS, wk = this.wakeT, mot = this.reduced ? 0 : 1;
    if (small) return;
    const flash = wk < 1.2 ? Math.exp(-wk*4) : 0, br = p.hudBright + flash*0.4, Ro = S*0.40;
    this.hspin = (this.hspin || 0) + p.hudSpin*dt*mot;
    ctx.lineCap = 'butt';
    // base rings
    ctx.lineWidth = 1; ctx.strokeStyle = rgba(col, 0.28*br);
    ctx.beginPath(); ctx.arc(cx, cy, Ro, 0, TAU); ctx.stroke();
    ctx.strokeStyle = rgba(col, 0.14*br); ctx.beginPath(); ctx.arc(cx, cy, Ro*(0.72-0.06*p.hudSplit), 0, TAU); ctx.stroke();
    // tick scale with voice spectrum
    const NT = 96; ctx.beginPath();
    for (let i = 0; i < NT; i++) {
      const a = i/NT*TAU - Math.PI/2, major = i % 8 === 0;
      let len = S*(major ? 0.04 : 0.016);
      const sp = p.hudSpec*amp*(0.5+0.5*Math.sin(i*0.7+t*20)*Math.sin(i*0.23-t*7));
      len *= 1 + sp*2.2;
      const r0 = Ro*1.02, r1 = r0+len;
      ctx.moveTo(cx+Math.cos(a)*r0, cy+Math.sin(a)*r0); ctx.lineTo(cx+Math.cos(a)*r1, cy+Math.sin(a)*r1);
    }
    ctx.lineWidth = 1; ctx.strokeStyle = rgba(col, 0.55*br); ctx.stroke();
    if (p.hudSpec*amp > 0.05) { ctx.lineWidth = 3; ctx.strokeStyle = rgba(col, 0.12*br*p.hudSpec*amp); ctx.stroke(); }
    // rotating segmented arcs
    const arcs = [[0.93, 1, 0.55, 2.4, 0.9], [0.86, -1.6, 0.32, 1.2, 0.7], [1.11, 0.6, 0.22, 1, 0.5], [0.79, 2.3, 0.14, 1.6, 0.6]];
    for (let k = 0; k < arcs.length; k++) {
      const A = arcs[k], rr = Ro*(A[0] + p.hudSplit*0.09*(k-1.5)), base = this.hspin*A[1] + k*1.9, cover = p.hudArcs*A[2]*TAU;
      const nseg = k === 0 ? 3 : 2;
      if (p.hudDash > 0.5) ctx.setLineDash([2, 7]);
      for (let sgi = 0; sgi < nseg; sgi++) {
        const a0 = base + sgi*TAU/nseg, a1 = a0 + cover/nseg*(0.6+0.4*Math.sin(t*0.7+k+sgi));
        ctx.beginPath(); ctx.arc(cx, cy, rr, a0, a1); ctx.lineWidth = A[3]; ctx.strokeStyle = rgba(mix(col, WHITE, 0.15), A[4]*br); ctx.stroke();
      }
      ctx.setLineDash([]);
      // end caps
      const ea = base + cover/nseg*0.5;
      ctx.fillStyle = rgba(mix(col, WHITE, 0.5), br*0.9); ctx.beginPath(); ctx.arc(cx+Math.cos(ea)*rr, cy+Math.sin(ea)*rr, 1.6, 0, TAU); ctx.fill();
    }
    // cardinal marks + readouts
    ctx.font = Math.max(8, Math.round(S*0.024))+'px ui-monospace, Menlo, Consolas, monospace'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillStyle = rgba(col, 0.6*br);
    const lab = ['000', '090', '180', '270'];
    for (let k = 0; k < 4; k++) { const a = k*Math.PI/2 - Math.PI/2, rr = Ro*1.16; ctx.fillText(lab[k], cx+Math.cos(a)*rr, cy+Math.sin(a)*rr); }
    ctx.fillStyle = rgba(col, 0.75*br);
    const lv = ((this.clock*7) % 1000) | 0;
    ctx.textAlign = 'right'; ctx.fillText(this.state.toUpperCase()+' · '+(amp*100|0).toString().padStart(3, '0'), cx+Ro*0.98, cy-Ro*0.86);
    ctx.textAlign = 'left'; ctx.fillText('LOCAL · '+String(lv).padStart(3, '0'), cx-Ro*0.98, cy+Ro*0.9);
    ctx.lineCap = 'round';
  }

  /* ---------- Armillary: rings on different axes that agree when she attends ---------- */
  drawArmillary(ctx, spinRate) {
    const p = this.p, t = this.t, dt = this.dt, w = this.w, h = this.h, S = Math.min(w, h), cx = w/2, cy = h/2, small = S < 40, col = this.col, amp = this.ampS, wk = this.wakeT, mot = this.reduced ? 0 : 1;
    const bright = p.bright + (wk < 1.2 ? 0.35*Math.exp(-wk*4) : 0);
    const K = 5, NP = small ? 24 : 64, R = S*0.27*(this.coreScale || 1)*(1+0.012*Math.sin(this.breathT));
    this.spin += (spinRate != null ? spinRate : p.spin)*dt*mot;
    if (!this.arm || this.arm.length !== K*NP*4) this.arm = new Float32Array(K*NP*4);
    const P = this.arm, B = 6, segs = this.segs || (this.segs = Array.from({ length: B }, () => []));
    for (let b = 0; b < B; b++) segs[b].length = 0;
    const splitV = p.split*(0.5-0.5*Math.cos(t*0.5));
    for (let k = 0; k < K; k++) {
      const own = p.spread*(0.35+0.32*k), az = k*TAU/K + this.spin*((k&1) ? -1 : 1)*(1+0.25*k);
      const tl = lerp(own, p.face, p.align), ph = lerp(az, this.spin*0.3, p.align);
      const rad = R*(1-0.11*k)*(1 + p.voiceR*amp*0.25*Math.sin(t*(9+k*2)+k));
      const dx = ((k&1) ? 1 : -1)*splitV*R*0.55;
      const ctl = Math.cos(tl), stl = Math.sin(tl), cph = Math.cos(ph), sph = Math.sin(ph);
      for (let i = 0; i < NP; i++) {
        const a = i/NP*TAU + t*0.3*(k+1)*mot, x0 = Math.cos(a), y0 = Math.sin(a);
        // ring in xz plane, tilted about x by tl, rotated about y by ph
        const y1 = -y0*stl, z1 = y0*ctl;
        const x2 = x0*cph + z1*sph, z2 = -x0*sph + z1*cph;
        const ps = 1/(1-0.2*z2), idx = (k*NP+i)*4;
        P[idx] = cx + dx + x2*rad*ps; P[idx+1] = cy + y1*rad*ps; P[idx+2] = z2; P[idx+3] = ps;
        const j = (i+1)%NP;
        segs[clamp(Math.floor((z2+1.2)/2.4*B), 0, B-1)].push(k*NP+i, k*NP+j);
      }
    }
    for (let pass = 0; pass < (small ? 1 : 2); pass++) for (let b = 0; b < B; b++) {
      const sg = segs[b]; if (!sg.length) continue;
      const df = (b+0.5)/B; ctx.beginPath();
      for (let q = 0; q < sg.length; q += 2) { const i = sg[q]*4, j = sg[q+1]*4; ctx.moveTo(P[i], P[i+1]); ctx.lineTo(P[j], P[j+1]); }
      if (pass === 0 && !small) { ctx.lineWidth = 4+4*df; ctx.strokeStyle = rgba(col, bright*(0.03+0.08*df)); }
      else { ctx.lineWidth = small ? 1 : 0.7+0.9*df; ctx.strokeStyle = rgba(mix(col, WHITE, 0.2*df), bright*(0.25+0.7*df)); }
      ctx.stroke();
    }
    if (!small) {
      const glow = this.sprite('glow'), core = rgba(mix(col, WHITE, 0.75), Math.min(1, bright));
      for (let k = 0; k < K; k++) for (let m = 0; m < 2; m++) {
        const i = ((Math.floor(frac(t*0.08*(k+1)+m*0.5)*NP)) % NP), idx = (k*NP+i)*4, ps = P[idx+3], df = clamp((ps-0.83)/0.4, 0, 1), gs = S*(this.coreScale || 1)*(0.04+0.05*df);
        ctx.globalAlpha = clamp(bright*(0.3+0.6*df), 0, 1); ctx.drawImage(glow, P[idx]-gs/2, P[idx+1]-gs/2, gs, gs);
        ctx.globalAlpha = 1; ctx.fillStyle = core; ctx.beginPath(); ctx.arc(P[idx], P[idx+1], 0.8+1.2*df, 0, TAU); ctx.fill();
      }
      // the pivot
      ctx.fillStyle = core; ctx.beginPath(); ctx.arc(cx, cy, 1.8, 0, TAU); ctx.fill();
      if (wk < 1) { ctx.strokeStyle = rgba(col, sq(1-wk)*0.6); ctx.lineWidth = 2; ctx.beginPath(); ctx.arc(cx, cy, S*(0.15+wk*0.4), 0, TAU); ctx.stroke(); }
    }
  }

  aperture() {
    const p = this.p, S = Math.min(this.w, this.h), Rd = S*p.Rd*(this.coreScale || 1), ox = p.off*S*(this.coreScale || 1), span = lerp(2.7, 0.8, clamp(p.open, 0, 1));
    return { x: this.w/2+ox, y: this.h/2, r: Rd*0.98*Math.abs(Math.cos(span/2)), Rd: Rd, span: span };
  }
  /* ---------- Iris blades over the eclipse disc ---------- */
  drawBlades(ctx) {
    const p = this.p, t = this.t, w = this.w, h = this.h, S = Math.min(w, h), cx = w/2, cy = h/2, col = this.col;
    if (S < 40) return;
    const A = this.aperture(), Rd = A.Rd, ox = A.x-cx, NB = 12, span = A.span, rot = t*0.15 + this.spin;
    ctx.globalCompositeOperation = 'source-over';
    ctx.lineWidth = 1; ctx.strokeStyle = rgba(col, 0.35*p.bright*(1-0.6*(p.wKnot || 0))); ctx.beginPath();
    for (let k = 0; k < NB; k++) {
      const a = k/NB*TAU + rot, x0 = cx+ox+Math.cos(a)*Rd*0.98, y0 = cy+Math.sin(a)*Rd*0.98, x1 = cx+ox+Math.cos(a+span)*Rd*0.98, y1 = cy+Math.sin(a+span)*Rd*0.98;
      ctx.moveTo(x0, y0); ctx.lineTo(x1, y1);
    }
    ctx.stroke();
    // aperture: the opening the blades leave
    const ap = A.r;
    if (p.wLens > 0.02) { ctx.strokeStyle = rgba(col, 0.25*p.bright*p.wLens); ctx.beginPath(); ctx.arc(cx+ox, cy, Math.max(1, ap*0.62), 0, TAU); ctx.stroke(); }
    ctx.strokeStyle = rgba(mix(col, WHITE, 0.3), 0.6*p.bright); ctx.beginPath(); ctx.arc(cx+ox, cy, Math.max(1, ap), 0, TAU); ctx.stroke();
    ctx.fillStyle = rgba(col, 0.08*p.bright); ctx.fill();
    ctx.globalCompositeOperation = 'lighter';
  }

  /* ---------- Eclipse: a dark body and a living corona ---------- */
  drawEclipse(ctx) {
    const p = this.p, t = this.t, dt = this.dt, w = this.w, h = this.h, S = Math.min(w, h), cx = w/2, cy = h/2, small = S < 40, col = this.col, amp = this.ampS, wk = this.wakeT, mot = this.reduced ? 0 : 1;
    const flash = wk < 1.2 ? Math.exp(-wk*4) : 0, bright = (p.bright + flash*0.5)*(p.ringDash > 0.5 ? 0.8+0.2*Math.sin(t*2.2) : 1);
    const Rd = S*p.Rd*(this.coreScale || 1)*(1+0.01*Math.sin(this.breathT)), ox = p.off*S*(this.coreScale || 1);
    this.spin += p.spin*dt*mot;
    const g = ctx.createRadialGradient(cx, cy, Rd*1.0, cx, cy, Rd*(1.5+p.corona*1.8));
    const hk = this.coreScale && this.coreScale < 1 ? 0.6 : 1;
    g.addColorStop(0, rgba(col, 0.5*bright*hk)); g.addColorStop(0.3, rgba(col, 0.1*bright*hk)); g.addColorStop(1, rgba(col, 0));
    ctx.fillStyle = g; ctx.fillRect(0, 0, w, h);
    const N = small ? 24 : 150, bins = this.bins || (this.bins = [[], [], [], []]);
    for (let b = 0; b < 4; b++) bins[b].length = 0;
    for (let i = 0; i < N; i++) {
      const a = i/N*TAU + this.spin + 0.02*Math.sin(i*7.1+t*0.3);
      const n = 0.5+0.5*Math.sin(i*3.7+t*1.3*p.shim)*Math.sin(i*1.3-t*0.7*p.shim);
      const L = Rd*p.corona*(p.spike != null ? p.spike : 1)*(0.35+1.1*n)*(1+p.bias*0.9*Math.max(0, Math.sin(a)))*(1+p.voiceL*amp*(0.6+0.5*Math.sin(i*0.9+t*15)))*(1+flash*0.8);
      bins[Math.min(3, Math.floor(n*4))].push(Math.cos(a), Math.sin(a), L);
    }
    for (let pass = 0; pass < (small ? 1 : 2); pass++) for (let b = 0; b < 4; b++) {
      const bn = bins[b]; if (!bn.length) continue;
      ctx.beginPath();
      for (let k = 0; k < bn.length; k += 3) { ctx.moveTo(cx+bn[k]*Rd*1.02, cy+bn[k+1]*Rd*1.02); ctx.lineTo(cx+bn[k]*(Rd+bn[k+2]), cy+bn[k+1]*(Rd+bn[k+2])); }
      const al = bright*(0.1+0.16*b)*(this.coreScale && this.coreScale < 1 ? 0.6 : 1);
      if (pass === 0 && !small) { ctx.lineWidth = 4; ctx.strokeStyle = rgba(col, al*0.3); } else { ctx.lineWidth = small ? 1 : 1.1; ctx.strokeStyle = rgba(mix(col, WHITE, 0.1*b), al); }
      ctx.stroke();
    }
    if (p.prom > 0.02 && !small) {
      for (let k = 0; k < 6; k++) {
        const a = k*TAU/6 + t*0.4 + this.spin, span = 0.3, ht = Rd*(0.35+0.5*(0.5+0.5*Math.sin(t*2.3+k*1.9)));
        const x0 = cx+Math.cos(a)*Rd, y0 = cy+Math.sin(a)*Rd, x3 = cx+Math.cos(a+span)*Rd, y3 = cy+Math.sin(a+span)*Rd;
        const x1 = cx+Math.cos(a+0.04)*(Rd+ht), y1 = cy+Math.sin(a+0.04)*(Rd+ht), x2 = cx+Math.cos(a+span-0.04)*(Rd+ht), y2 = cy+Math.sin(a+span-0.04)*(Rd+ht);
        ctx.beginPath(); ctx.moveTo(x0, y0); ctx.bezierCurveTo(x1, y1, x2, y2, x3, y3);
        ctx.lineWidth = 6; ctx.strokeStyle = rgba(col, p.prom*bright*0.18); ctx.stroke();
        ctx.lineWidth = 1.6; ctx.strokeStyle = rgba(mix(col, WHITE, 0.3), p.prom*bright*0.85); ctx.stroke();
      }
    }
    if (p.ringDash > 0.5) ctx.setLineDash([3, 6]);
    ctx.beginPath(); ctx.arc(cx, cy, Rd*1.01, 0, TAU);
    if (!small) { ctx.lineWidth = 8; ctx.strokeStyle = rgba(col, p.ring*bright*0.22); ctx.stroke(); }
    ctx.lineWidth = small ? 1.5 : 2.2; ctx.strokeStyle = rgba(mix(col, WHITE, 0.35), p.ring*bright); ctx.stroke(); ctx.setLineDash([]);
    if (p.dbl > 0.02) { ctx.beginPath(); ctx.arc(cx, cy, Rd*(1+0.42*p.dbl), 0, TAU); ctx.lineWidth = 1.3; ctx.strokeStyle = rgba(col, p.dbl*bright*0.7); ctx.stroke(); }
    if (!small) {
      const glow = this.sprite('glow');
      if (p.beads > 0.02) for (let j = 0; j < 14; j++) {
        const a = j*TAU/14 - t*0.5, rr = Rd*(1+0.42*p.dbl), gs = S*0.06*(0.6+0.4*Math.sin(t*5+j*2.1));
        ctx.globalAlpha = clamp(p.beads*bright*(0.4+0.6*Math.sin(t*3+j*1.3)), 0, 1); ctx.drawImage(glow, cx+Math.cos(a)*rr-gs/2, cy+Math.sin(a)*rr-gs/2, gs, gs);
      }
      if (wk < 1.1) { const a = -0.9, gs = Rd*(0.9+wk*2.4); ctx.globalAlpha = sq(1-wk/1.1); ctx.drawImage(glow, cx+Math.cos(a)*Rd-gs/2, cy+Math.sin(a)*Rd-gs/2, gs, gs); }
      ctx.globalAlpha = 1;
    }
    ctx.globalCompositeOperation = 'source-over';
    if (p.off > 0.005) { ctx.globalCompositeOperation = 'destination-out'; ctx.fillStyle = '#000'; ctx.beginPath(); ctx.arc(cx, cy, Rd*0.99, 0, TAU); ctx.fill(); ctx.globalCompositeOperation = 'source-over'; }
    ctx.fillStyle = '#030608'; ctx.beginPath(); ctx.arc(cx+ox, cy, Rd, 0, TAU); ctx.fill();
    ctx.globalCompositeOperation = 'lighter';
  }
}
CielSymbol2.COLORS = COLORS; CielSymbol2.HEX = HEX; CielSymbol2.ORDER = ORDER; CielSymbol2.ORDER7 = ORDER7;
root.CielSymbol2 = CielSymbol2;
})(typeof window !== 'undefined' ? window : this);
