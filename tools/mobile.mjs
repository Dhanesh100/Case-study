// Phone layout for a case study, generated from its own desktop page.
//
//   node tools/mobile.mjs <slug> [<slug> ...]      (no args: every home/work/*)
//
// The desktop page is a 1440px Figma frame scaled to the window, unreadable on a phone. This
// opens it in headless Chrome, reads the layout, and writes a single-column version into the
// same index.html, shown below 768px:
//   - article text (18px and up in the design) becomes real HTML at a phone size;
//   - everything else is grouped and captured from the page itself at up to 2x, with the
//     article text hidden, so mockups and photos stay exactly as designed;
//   - links, and the screen recordings on Kotak, carry over.
// Idempotent: the block between the mobile markers is replaced. Needs Node 22+ and Chrome.
import { spawn } from 'node:child_process';
import { readFileSync, writeFileSync, mkdirSync, rmSync, readdirSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const A = '<!-- mobile:start -->', B = '<!-- mobile:end -->';
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function browser() {
  const port = 9400 + Math.floor(Math.random() * 400);
  const proc = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files',
    '--remote-debugging-port=' + port, '--window-size=1440,900', '--user-data-dir=' + (process.env.TMPDIR || '/tmp') + '/mob-' + port, 'about:blank'],
    { stdio: 'ignore' });
  let tabs;
  for (let i = 0; i < 100 && !tabs; i++) { try { tabs = await (await fetch(`http://127.0.0.1:${port}/json`)).json(); } catch { await sleep(150); } }
  const ws = new WebSocket(tabs.find(t => t.type === 'page').webSocketDebuggerUrl);
  await new Promise(r => (ws.onopen = r));
  let id = 0; const pend = {};
  ws.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pend[m.id]) { pend[m.id](m); delete pend[m.id]; } };
  const send = (method, params = {}) => new Promise(r => { const i = ++id; pend[i] = r; ws.send(JSON.stringify({ id: i, method, params })); });
  const ev = async x => {
    const m = await send('Runtime.evaluate', { expression: x, returnByValue: true, awaitPromise: true });
    if (m.error || m.result.exceptionDetails) throw new Error(JSON.stringify(m.error || m.result.exceptionDetails).slice(0, 600));
    return m.result.result.value;
  };
  await send('Page.enable');
  return { send, ev, close() { ws.close(); proc.kill(); } };
}

// ── runs inside the page: read the layout into a spec ───────────────────────────────────────
const ANALYSE = String.raw`(async function(){
  var MIN = 18, canvas = document.getElementById('canvas');
  ['ldr','rp','totop'].forEach(function(i){ var e=document.getElementById(i); if(e) e.remove(); });
  document.getElementById('hdr').style.display = 'none';
  /* every lazy background, now, and wait for all of them */
  await Promise.all([].map.call(document.querySelectorAll('[data-bg]'), function(el){
    var urls = el.getAttribute('data-bg').split('|');
    return Promise.all(urls.map(function(u){ return new Promise(function(r){ var i=new Image(); i.onload=i.onerror=r; i.src=u; }); }))
      .then(function(){ urls.forEach(function(u,i){ el.style.setProperty('--b'+i,'url("'+u+'")'); }); el.classList.add('ok'); });
  }));
  await document.fonts.ready;
  [].forEach.call(document.querySelectorAll('video.vid'), function(v){ v.removeAttribute('src'); v.load(); });
  var st = document.createElement('style'); st.textContent = '[data-bg]::before{display:none!important}'; document.head.appendChild(st);
  await new Promise(function(r){ setTimeout(r, 400); });

  var mid = 0;
  function tag(e){ if(!e.dataset.mid) e.dataset.mid = ++mid; return e.dataset.mid; }
  function isT(e){ return e.classList && e.classList.contains('t'); }
  function size(e){ return parseFloat(e.style.fontSize) || parseFloat(getComputedStyle(e).fontSize); }
  function words(e){ return (e.textContent || '').trim().split(/\s+/).filter(Boolean).length; }
  function R(e){ var r = e.getBoundingClientRect(); return {x:r.left+scrollX, y:r.top+scrollY, w:r.width, h:r.height}; }
  function inter(a,b){ var x=Math.max(a.x,b.x), y=Math.max(a.y,b.y), r=Math.min(a.x+a.w,b.x+b.w), d=Math.min(a.y+a.h,b.y+b.h);
    return r-x>1 && d-y>1 ? {x:x,y:y,w:r-x,h:d-y} : null; }
  function union(rs){ var x=1e9,y=1e9,r=-1e9,d=-1e9; rs.forEach(function(a){ x=Math.min(x,a.x); y=Math.min(y,a.y); r=Math.max(r,a.x+a.w); d=Math.max(d,a.y+a.h); });
    return {x:x,y:y,w:r-x,h:d-y}; }
  /* what is actually visible of an element: its box, clipped by every clipping ancestor */
  function clip(e){
    var r = R(e);
    for (var a = e.parentElement; a && a !== document.body && r; a = a.parentElement) {
      var cs = getComputedStyle(a);
      if (cs.overflowX !== 'visible' || cs.overflowY !== 'visible') r = inter(r, R(a));
    }
    return r && inter(r, R(canvas));
  }
  function shown(e){ var cs = getComputedStyle(e); return cs.display !== 'none' && cs.visibility !== 'hidden' && +cs.opacity > 0.02; }
  function stats(e){
    if (!shown(e) || !clip(e)) return e._s = {skip:1, cw:0, sw:0, img:0};
    if (isT(e)) {
      if (e._occ) return e._s = {skip:1, cw:0, sw:0, img:0};
      var w = words(e);                                           /* article text: big, or a real passage */
      return e._s = size(e) >= MIN || (size(e) >= 13 && w >= 12) ? {cw:w, sw:0, img:0} : {cw:0, sw:w, img:0};
    }
    var s = {cw:0, sw:0, img: /^(svg|VIDEO|IMG)$/.test(e.tagName) || e.hasAttribute('data-bg') ? 1 : 0};
    if (e.tagName !== 'svg') [].forEach.call(e.children, function(c){ var k = stats(c); s.cw += k.cw; s.sw += k.sw; s.img += k.img; });
    return e._s = s;
  }
  /* covered = something above the text at that point actually paints: an opaque fill, an image, text */
  function paints(h){
    var cs = getComputedStyle(h);
    if (+cs.opacity < 0.5 || cs.visibility === 'hidden') return false;
    if (/^(IMG|VIDEO|svg|path)$/.test(h.tagName) || h.classList.contains('t')) return true;
    if (cs.backgroundImage !== 'none') return true;
    var m = cs.backgroundColor.match(/rgba?\(([^)]*)\)/), a = m ? m[1].split(',') : [];
    return a.length === 4 ? +a[3] > 0.6 : a.length === 3;
  }
  function covered(e, x, y){
    var st = document.elementsFromPoint(x, y);
    for (var j = 0; j < st.length; j++) {
      var h = st[j];
      if (h === e || e.contains(h)) return false;
      if (h.contains(e)) continue;                                 /* an ancestor paints beneath its children */
      if (paints(h)) return true;
    }
    return false;
  }
  /* text that another layer covers is not part of what anyone sees: probe it where it sits */
  var all = [].slice.call(canvas.querySelectorAll('.t'));
  for (var i = 0; i < all.length; i++) {
    var e = all[i], r = e.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) continue;
    scrollTo(0, Math.max(0, r.top + scrollY - 300)); r = e.getBoundingClientRect();
    var hits = 0, pts = [[.5,.5],[.2,.3],[.8,.3],[.3,.7],[.7,.7]];
    pts.forEach(function(p){ var x = r.left + r.width * p[0], y = r.top + Math.min(r.height * p[1], 40);
      if (x < 0 || y < 0 || x >= innerWidth || y >= innerHeight) { hits++; return; }
      if (!covered(e, x, y)) hits++; });
    if (!hits) { e._occ = 1; e.dataset.mt = 1; }                  /* and keep it out of the captures too */
  }
  scrollTo(0, 0);
  stats(canvas);
  function kind(e){
    var s = e._s;
    if (s.skip) return 'skip';
    if (isT(e)) return s.cw ? 'text' : 'vis';
    if (!s.cw) return 'vis';
    if (s.img && s.cw <= 15 && s.sw >= s.cw) return 'vis';          /* a mockup: a few big words among UI text */
    return 'box';
  }
  function solid(e){
    var cs = getComputedStyle(e), bi = cs.backgroundImage;
    if (bi && bi !== 'none' && !/url\(/.test(bi)) {
      var m = bi.match(/^linear-gradient\(\s*(rgba?\([^)]*\))\s*,\s*(rgba?\([^)]*\))\s*\)$/);
      return m && m[1] === m[2] ? m[1] : bi;                       /* the converter writes solids as flat gradients */
    }
    var c = cs.backgroundColor; return c && !/rgba\(0, 0, 0, 0\)|transparent/.test(c) ? c : null;
  }
  function href(e){ var a = e.closest('a[href]'); return a && canvas.contains(a) ? a.getAttribute('href') : null; }
  function text(e){
    tag(e); e.dataset.mt = 1;
    var cs = getComputedStyle(e), fs = size(e), lh = parseFloat(cs.lineHeight);
    var html = e.innerHTML.replace(/font-size:[^;"]*;?/g, '');
    return {t:'text', html:html, fs:fs, ff:cs.fontFamily, fw:cs.fontWeight, color:cs.color, fst:cs.fontStyle,
            lh: lh && fs ? +(lh/fs).toFixed(3) : 1.3, ls: parseFloat(cs.letterSpacing) || 0, tt:cs.textTransform,
            align: cs.textAlign, td: cs.textDecorationLine, href: e.tagName === 'A' ? e.getAttribute('href') : href(e),
            y: R(e).y, x: R(e).x};
  }
  function box(e){
    var kids = [].filter.call(e.children, function(c){ return c._s && !c._s.skip; });
    var items = [], vis = [], plain = [], bg = solid(e), area = R(e).w * R(e).h;
    kids.forEach(function(c){
      var k = kind(c);
      if (k === 'text') items.push(text(c));
      else if (k === 'box') { var b = box(c); b.y = clip(c).y; b.x = clip(c).x; items.push(b); }
      else if (!c._s.img && !c._s.sw && !c.querySelector('a,svg')) plain.push(c);  /* a bare shape: background, not content */
      else vis.push(c);
    });
    plain.forEach(function(c){ var r = clip(c), cs = getComputedStyle(c);          /* a blurred or faded glow is not a ground */
      if (!bg && r && r.w * r.h > area * 0.6 && cs.filter === 'none' && +cs.opacity > 0.95) bg = solid(c); });
    /* visual children cluster by vertical overlap; each cluster becomes one capture */
    vis.sort(function(a,b){ return clip(a).y - clip(b).y; });
    var groups = [];
    vis.forEach(function(c){
      var r = clip(c), g = groups[groups.length-1];
      if (g && r.y < g.r.y + g.r.h + 24) { g.els.push(c); g.r = union([g.r, r]); } else groups.push({els:[c], r:r});
    });
    /* a phone reads a desktop composition best as a stack of full-width pieces: split a visual
       into its stacked rows, and a row into side-by-side columns, wherever the parts do not overlap */
    function vk(e){ return [].filter.call(e.children || [], function(c){ var r = c._s && !c._s.skip && clip(c); return r && r.w > 20 && r.h > 20; }); }
    function bands(els, axis){                                    /* group rects that overlap along one axis */
      var p = axis === 'y' ? 'y' : 'x', q = axis === 'y' ? 'h' : 'w';
      var it = els.map(function(c){ return {els:[c], r:clip(c)}; }).sort(function(a,b){ return a.r[p] - b.r[p]; }), out = [];
      it.forEach(function(o){ var l = out[out.length-1];
        if (l && o.r[p] < l.r[p] + l.r[q] - 8) { l.els.push(o.els[0]); l.r = union([l.r, o.r]); } else out.push(o); });
      return out;
    }
    function pieces(els, depth){
      if (depth > 6) return [union(els.map(clip))];
      if (els.length === 1) {
        var e = els[0];
        if (e.tagName === 'svg' || e.tagName === 'VIDEO' || (e.querySelector && e.querySelector('video'))) return [clip(e)];
        var k = vk(e);
        if (!k.length) return [clip(e)];
        return pieces(k, depth + 1).map(function(r){ return inter(r, clip(e)); }).filter(Boolean);
      }
      var rows = bands(els, 'y');
      if (rows.length > 1) return [].concat.apply([], rows.map(function(b){ return pieces(b.els, depth + 1); }));
      var cols = bands(els, 'x');
      if (cols.length > 1 && cols.every(function(b){ return b.r.w >= 300; }))
        return [].concat.apply([], cols.map(function(b){ return pieces(b.els, depth + 1); }));
      return [union(els.map(clip))];
    }
    var hide = kids.filter(function(c){ return kind(c) === 'box'; }).map(tag);
    groups = [].concat.apply([], groups.map(function(g){
      var ps = pieces(g.els, 0).filter(function(r){ return r && r.h >= 24; });
      if (ps.length < 2) return [g];
      /* never leave a piece smaller than a thumbnail on its own: merge it upward */
      var out = [];
      ps.forEach(function(r){ var l = out[out.length-1];
        if (l && (r.h < 120 || l.h < 120) && Math.abs(l.x - r.x) < 40 && Math.abs(l.w - r.w) < 80) out[out.length-1] = union([l, r]); else out.push(r); });
      return out.map(function(r, i){ return {els: g.els, r: r, col: i}; });
    }));
    groups.forEach(function(g){
      var r = inter(g.r, clip(e) || g.r); if (!r || (r.w < 40 && r.h < 40 && !g.els.some(href))) return;
      var hs = []; g.els.forEach(function(c){ var h = href(c) || (c.querySelector && c.querySelector('a[href]') && c.querySelector('a[href]').getAttribute('href')); if (h && hs.indexOf(h) < 0) hs.push(h); });
      var v = null;
      g.els.forEach(function(c){ var vd = c.tagName === 'VIDEO' ? c : c.querySelector && c.querySelector('video.vid');
        if (vd) { var vr = clip(vd); if (vr && vr.w * vr.h > r.w * r.h * 0.7) v = {poster: vd.getAttribute('poster'), src: vd.getAttribute('data-src'),
          start: vd.getAttribute('data-start'), label: vd.getAttribute('aria-label') || ''}; } });
      if (g.col !== undefined) { hs = hs.filter(function(h){ return g.els.some(function(c){ var a = c.closest('a[href]') || (c.querySelector && c.querySelector('a[href="' + h + '"]'));
        if (!a) return false; var ar = clip(a); return ar && inter(ar, r); }); }); }
      items.push({t:'vis', r:{x:Math.floor(r.x), y:Math.floor(r.y), w:Math.ceil(r.w), h:Math.ceil(r.h)}, hide:hide, href: hs.length === 1 ? hs[0] : null, video:v,
                  y: g.col !== undefined ? g.r.y + g.col * 0.01 : r.y, x: g.col !== undefined ? 0 : r.x});
    });
    /* reading order: rows top to bottom; within a row, left to right */
    items.sort(function(a,b){ return Math.abs(a.y - b.y) < 12 ? a.x - b.x : a.y - b.y; });
    return {t:'box', bg:bg, items:items};
  }
  var spec = box(canvas);
  spec.bg = solid(canvas) || getComputedStyle(document.body).backgroundColor;
  return JSON.stringify(spec);
})()`;

// ── turn the spec into HTML ─────────────────────────────────────────────────────────────────
const esc = s => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');
function rgb(c) {
  const m = (c || '').match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)/);
  return m ? [+m[1], +m[2], +m[3]] : null;
}
function lum(c) {
  const v = rgb(c); if (!v) return null;
  const f = x => { x /= 255; return x <= 0.03928 ? x / 12.92 : ((x + 0.055) / 1.055) ** 2.4; };
  return 0.2126 * f(v[0]) + 0.7152 * f(v[1]) + 0.0722 * f(v[2]);
}
const contrast = (a, b) => { const x = lum(a), y = lum(b); return x == null || y == null ? 21 : (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
// phone sizes for the design's text sizes
function phone(fs) {
  if (fs >= 80) return 42; if (fs >= 56) return 34; if (fs >= 48) return 30; if (fs >= 40) return 27;
  if (fs >= 32) return 23; if (fs >= 24) return 18; if (fs >= 20) return 17; return 16;
}

function render(spec, slug, pageBg) {
  const shots = [];
  let n = 0;
  function walk(node, bg, depth) {
    let out = '';
    for (const it of node.items) {
      if (it.t === 'text') {
        let color = it.color;
        // text whose ground was a photo can land on the page colour: keep it legible
        const fix = contrast(color, bg) < 2.2 ? ` style="background:${lum(color) > 0.5 ? '#151515' : '#fff'};padding:16px;border-radius:14px"` : '';
        const size = phone(it.fs), tagn = it.fs >= 32 ? 'h2' : 'p';
        const st = [`font-family:${it.ff.replace(/"/g, "'")}`, `font-weight:${it.fw}`, `font-size:${size}px`, `line-height:${Math.max(1.12, Math.min(it.lh, 1.6))}`,
          `color:${color}`];
        if (it.ls) st.push(`letter-spacing:${(it.ls * size / it.fs).toFixed(2)}px`);
        if (it.tt && it.tt !== 'none') st.push(`text-transform:${it.tt}`);
        if (it.fst === 'italic') st.push('font-style:italic');
        if (it.align === 'center') st.push('text-align:center');
        if (it.td && it.td !== 'none') st.push(`text-decoration:${it.td}`);
        let body = `<${tagn} class="m-t" style="${st.join(';')}">${it.html}</${tagn}>`;
        if (it.href && !/<a\b/.test(it.html)) body = `<a href="${esc(it.href)}"${/^https?:/.test(it.href) ? ' target="_blank" rel="noopener"' : ''}>${body}</a>`;
        out += fix ? `<div${fix}>${body}</div>` : body;
      } else if (it.t === 'box') {
        const own = it.bg && it.bg !== bg ? it.bg : null;
        const inner = walk(it, own || bg, depth + 1);
        if (!inner) continue;
        out += own ? `<div class="m-b${depth ? ' m-card' : ''}" style="background:${own}">${inner}</div>` : inner;
      } else {
        const name = `m${String(++n).padStart(2, '0')}.webp`;
        const scale = Math.min(2, 1080 / it.r.w);
        shots.push({ name, r: it.r, hide: it.hide, scale });
        const w = Math.round(it.r.w * scale), h = Math.round(it.r.h * scale);
        const wide = (it.r.w >= 1200 ? ' m-bleed' : '') + (it.r.h < 100 && it.r.w > it.r.h * 3 ? ' m-tx' : ''), small = it.r.w < 360 ? ` style="max-width:${Math.round(it.r.w * 0.8)}px"` : '';
        let body;
        if (it.video && it.video.src) {
          body = `<div class="m-vid${wide}" style="aspect-ratio:${it.r.w}/${it.r.h}"><video class="vid" muted playsinline poster="${esc(it.video.poster || 'm/' + name)}"` +
            ` data-src="${esc(it.video.src)}" data-start="${esc(it.video.start || '0')}" aria-label="${esc(it.video.label)}"></video></div>`;
        } else {
          body = `<img class="m-i${wide}" src="m/${name}" alt="" width="${w}" height="${h}" loading="lazy" decoding="async"${small}>`;
        }
        if (it.href) body = `<a class="m-a" href="${esc(it.href)}"${/^https?:/.test(it.href) ? ' target="_blank" rel="noopener"' : ''}>${body}</a>`;
        out += body;
      }
    }
    return out;
  }
  const html = walk(spec, pageBg, 0);
  return { html, shots };
}

async function build(b, slug) {
  const dir = join(ROOT, 'home', 'work', slug), file = join(dir, 'index.html');
  let page = readFileSync(file, 'utf8').replace(new RegExp(`\\s*${A}[\\s\\S]*?${B}`, 'g'), '');
  writeFileSync(file, page);                                   // analyse the page without an old phone layout
  await b.send('Page.navigate', { url: 'file://' + file }); await sleep(1500);
  const spec = JSON.parse(await b.ev(ANALYSE));
  const dark = lum(spec.bg) < 0.2;
  const { html, shots } = render(spec, slug, spec.bg);

  const mdir = join(dir, 'm'); if (existsSync(mdir)) rmSync(mdir, { recursive: true }); mkdirSync(mdir);
  await b.ev(`(function(){ var s=document.createElement('style'); s.id='mcap'; document.head.appendChild(s);
    var t=document.createElement('style'); t.textContent='[data-mt]{visibility:hidden!important}'; document.head.appendChild(t); })()`);
  for (const s of shots) {
    await b.ev(`document.getElementById('mcap').textContent=${JSON.stringify(s.hide.map(h => `[data-mid="${h}"]`).join(',') + (s.hide.length ? '{visibility:hidden!important}' : ''))}`);
    const m = await b.send('Page.captureScreenshot', { format: 'webp', quality: 80, captureBeyondViewport: true,
      clip: { x: s.r.x, y: s.r.y, width: s.r.w, height: s.r.h, scale: s.scale } });
    writeFileSync(join(mdir, s.name), Buffer.from(m.result.data, 'base64'));
  }

  const title = (page.match(/<title>(.*?)<\/title>/) || [])[1] || slug;
  const name = title.split(' — ')[0].split(' · ')[0];
  const fg = dark ? '#fff' : '#151515', pill = dark ? 'rgba(255,255,255,.12)' : 'rgba(0,0,0,.06)';
  const css = `<style>
.m{display:none}
@media (max-width:767.98px){
  .stage,.hdr-wrap{display:none!important}
  .m{display:block;background:${spec.bg};color:${fg};font-family:"PP Neue Montreal",-apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif;overflow-x:clip}
}
.m-h{position:sticky;top:0;z-index:50;display:flex;align-items:center;gap:10px;padding:10px 16px;
  background:${spec.bg.replace(/^rgb\((.*)\)$/, 'rgba($1,.82)')};-webkit-backdrop-filter:blur(20px);backdrop-filter:blur(20px)}
.m-h a{display:inline-flex;align-items:center;gap:6px;height:40px;padding:0 16px;border-radius:40px;font:500 15px/1 "PP Neue Montreal",-apple-system,"Helvetica Neue",Arial,sans-serif;color:${fg};background:${pill}}
.m-h .m-name{flex:1;min-width:0;font:700 13px/1.2 "PP Neue Montreal",-apple-system,"Helvetica Neue",Arial,sans-serif;opacity:.6;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.m-h .m-go{background:${fg};color:${spec.bg}}
.m-body{padding:8px 16px 48px}
.m-b{margin:16px 0;padding:28px 20px;border-radius:20px;overflow:hidden}
.m-card{margin:16px 0;padding:24px 20px;border-radius:20px}
.m-t{margin:0 0 14px}
h2.m-t{margin:28px 0 14px;text-wrap:balance}
.m-b>h2.m-t:first-child,.m-card>h2.m-t:first-child{margin-top:0}
.m-t .ul{margin:0;padding-left:1.2em}.m-t .ul li{margin:0 0 10px}
.m-i,.m-vid{display:block;width:100%;height:auto;margin:16px auto;border-radius:16px}
.m-bleed{width:100%;max-width:100%;margin-left:0;margin-right:0}
.m-tx{border-radius:0}
.m-card .m-bleed,.m-b .m-b .m-bleed{width:100%;margin-left:0;margin-right:0}
.m-vid{position:relative;overflow:hidden;border-radius:12px}
.m-a{display:block;-webkit-tap-highlight-color:transparent}
.m-a:active .m-i{transform:scale(.985);transition:transform .15s ease}
.m a:focus-visible{outline:3px solid ${fg};outline-offset:3px}
</style>`;
  const head = `<header class="m-h"><a href="../../#work" aria-label="Back to all work"><svg width="14" height="14" viewBox="0 0 14 14" aria-hidden="true"><path d="M9 2 4 7l5 5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Back</a>` +
    `<span class="m-name">${esc(name)}</span><a class="m-go" href="../../#contact">Get in touch</a></header>`;
  const block = `<div class="m" id="m">${head}<main class="m-body">${html}</main></div>`;
  page = page.replace('</head>', `${A}\n${css}\n${B}\n</head>`)
             .replace(/(<main class="stage")/, `${A}${block}${B}\n$1`);
  writeFileSync(file, page);
  const words = html.replace(/<[^>]+>/g, ' ').split(/\s+/).filter(Boolean).length;
  console.log(`${slug.padEnd(14)} ${shots.length} images, ${words} words of text`);
}

const slugs = process.argv.slice(2).length ? process.argv.slice(2)
  : readdirSync(join(ROOT, 'home', 'work')).filter(d => existsSync(join(ROOT, 'home', 'work', d, 'index.html')));
const b = await browser();
try { for (const s of slugs) await build(b, s); } finally { b.close(); }
