# -*- coding: utf-8 -*-
"""Add the loading experience to the portfolio pages. Idempotent: run it after any rebuild.

    python3 tools/add-ux.py            # home/index.html and every home/work/*/index.html

What it adds, all inline (pages stay self-contained, no requests):
  1. A loader overlay: page name + a progress bar driven by the first screen's images and the
     fonts. Leaves as soon as they are in; never stays longer than 4s; without JS it leaves by CSS.
  2. Case studies: every background image loads only near the viewport, behind a soft shimmer.
     The style keeps `var(--b0, none)` where the url was; the url moves to data-bg.
  3. Cross-document view transitions, and hover-prefetch of internal pages.
  4. Case studies: a reading-progress bar and a back-to-top button.
  5. Link-preview tags (Open Graph, Twitter). `--og` also renders each page's og.jpg.
  6. Screen recordings get a pause/play control; a user's pause sticks.
  7. Every :hover rule in the page's own CSS is moved behind (hover:hover) and (pointer:fine), so a
     tap on a phone never leaves a card grown or a button stuck in its hover state.
Reduced motion: no shimmer, no fades, no bar animation; recordings wait to be played.
Error state: an image that fails stops shimmering and is retried, then retried again on reconnect."""
import glob, html as H, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A, B = '<!-- ux:start -->', '<!-- ux:end -->'
SITE = 'https://dhanesh100.github.io/Case-study/'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

META = '''<meta property="og:type" content="website"><meta property="og:site_name" content="Dhanesh Shetye">
<meta property="og:title" content="%(title)s"><meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(url)s"><meta property="og:image" content="%(url)sog.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><link rel="canonical" href="%(url)s">'''

AIDS = '<div id="rp" aria-hidden="true"><i></i></div><button id="totop" type="button" aria-label="Back to top">' \
       '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 15V5M5.5 9.5 10 5l4.5 4.5" fill="none" stroke="currentColor" ' \
       'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg></button>'

CSS = '''<style>
@view-transition{navigation:auto}
#ldr{position:fixed;inset:0;z-index:1000;display:flex;align-items:center;justify-content:center;background:%(bg)s;color:%(fg)s;
  transition:opacity .45s cubic-bezier(.2,.75,.2,1),visibility 0s .45s;animation:ldr-bail 0s 6s forwards}
#ldr.out{opacity:0;visibility:hidden}
@keyframes ldr-bail{to{opacity:0;visibility:hidden}}
.ldr-in{width:min(320px,72vw);text-align:center}
.ldr-k{font:500 12px/16px "PP Neue Montreal",-apple-system,"Helvetica Neue",Arial,sans-serif;letter-spacing:.16em;text-transform:uppercase;opacity:.6}
.ldr-n{margin:10px 0 22px;font:500 clamp(26px,4vw,40px)/1.1 "PP Eiko",Didot,Georgia,serif;letter-spacing:-.01em}
.ldr-bar{height:2px;border-radius:2px;background:%(track)s;overflow:hidden}
.ldr-bar i{display:block;height:100%%;width:100%%;background:currentColor;transform:scaleX(.04);transform-origin:0 50%%;
  transition:transform .5s cubic-bezier(.2,.75,.2,1)}
[data-bg]::before{content:"";position:absolute;inset:0;border-radius:inherit;pointer-events:none;
  background:linear-gradient(100deg,%(sk)s 30%%,%(sk2)s 50%%,%(sk)s 70%%) 0 0/300%% 100%%;
  animation:sk 1.4s linear infinite;transition:opacity .5s ease}
[data-bg].ok::before{opacity:0;animation:none}
@keyframes sk{from{background-position:100%% 0}to{background-position:0 0}}
img.ld-in{opacity:0;transition:opacity .5s ease}img.ld-in.ok{opacity:1}
#rp{position:fixed;left:0;top:0;right:0;height:3px;z-index:60;pointer-events:none}
#rp i{display:block;height:100%%;background:%(fg)s;transform:scaleX(0);transform-origin:0 50%%}
#totop{position:fixed;right:24px;bottom:24px;z-index:60;width:48px;height:48px;padding:0;border:0;border-radius:50%%;
  background:%(btn)s;color:%(btnfg)s;display:grid;place-items:center;cursor:pointer;box-shadow:0 8px 24px -8px rgba(0,0,0,.35);
  opacity:0;transform:translateY(12px);visibility:hidden;transition:opacity .3s ease,transform .3s ease,visibility 0s .3s}
#totop.on{opacity:1;transform:none;visibility:visible;transition:opacity .3s ease,transform .3s ease}
#totop.on:active{transform:scale(.94);transition:transform .12s cubic-bezier(.23,1,.32,1)}
a.t,.t a[href],.m-body a[href]{transition:opacity .2s ease}
@media (hover:hover) and (pointer:fine){#totop:hover{transform:translateY(-2px)}a.t:hover,.t a[href]:hover,.m-body a[href]:hover{opacity:.62}.vc:hover{opacity:1}}
[data-bg].err::before{animation:none;opacity:1;background:%(sk2)s}
.vc{position:absolute;right:14px;bottom:14px;z-index:3;width:44px;height:44px;padding:0;border:0;border-radius:50%%;display:grid;place-items:center;
  cursor:pointer;background:rgba(17,17,17,.62);color:#fff;-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);opacity:.85;
  transition:opacity .2s ease,transform .12s cubic-bezier(.23,1,.32,1)}
.vc svg{width:18px;height:18px}.vc:active{transform:scale(.94)}.vc:focus-visible{outline:3px solid #fff;outline-offset:2px}
#totop:focus-visible{outline:3px solid %(fg)s;outline-offset:3px}
#totop svg{width:20px;height:20px}
@media (prefers-reduced-motion:reduce){#ldr,.ldr-bar i,[data-bg]::before,img.ld-in,#totop{transition:none}[data-bg]::before{animation:none}
  @view-transition{navigation:none}}
/* View-case-study pill follows the pointer (mouse only: html.cf is set by script) */
html.cf .card .cta,html.cf a.nx .cta{left:0;top:0;right:auto;bottom:auto;height:38px;min-width:0;gap:7px;padding:0 13px 0 15px;
  pointer-events:none;opacity:0;scale:.6;transform-origin:0 0;box-shadow:0 8px 22px -8px rgba(0,0,0,.45);
  transition:opacity .2s ease,scale .25s cubic-bezier(.2,.75,.2,1)}
html.cf .card .cta-t,html.cf a.nx .cta-t{max-width:none;opacity:1;font-size:13.5px;line-height:18px;letter-spacing:.3px;transition:none}
html.cf .card .cta svg,html.cf a.nx .cta svg{width:15px;height:15px;flex:0 0 15px;transform:none}
@media (hover:hover) and (pointer:fine){html.cf .card:hover .cta,html.cf a.nx:hover .cta{opacity:1;scale:1;gap:7px;padding:0 13px 0 15px}}
html.cf .card.nudge .cta::before{animation:none}
html.cf .card:focus-visible .cta,html.cf a.nx:focus-visible .cta{opacity:1;scale:1;translate:none!important;left:auto;top:auto;right:20px;bottom:20px}
</style>
<noscript><style>#ldr{display:none}[data-bg]::before{display:none}</style></noscript>'''

OVERLAY = '<div id="ldr" role="progressbar" aria-label="Loading %(name)s" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">' \
          '<div class="ldr-in"><div class="ldr-k">%(kicker)s</div><div class="ldr-n">%(name)s</div>' \
          '<div class="ldr-bar"><i></i></div></div></div>'

JS = r'''<script>
/* loading experience — see tools/add-ux.py */
(function(){
  var ldr=document.getElementById('ldr'), bar=ldr&&ldr.querySelector('.ldr-bar i'), t0=Date.now(), done=false;
  var vh=innerHeight*1.15, waits=[], got=0;
  function prog(){ var p=waits.length?got/waits.length:1; if(bar) bar.style.transform='scaleX('+(.04+.96*p)+')';
    if(ldr) ldr.setAttribute('aria-valuenow',Math.round(p*100)); if(got>=waits.length) finish(); }
  function finish(){ if(done||!ldr) return; done=true; if(bar) bar.style.transform='scaleX(1)';
    setTimeout(function(){ ldr.classList.add('out'); setTimeout(function(){ ldr.remove(); },600); }, Date.now()-t0<150?0:220); }
  function wait(p){ waits.push(p); p.then(function(){ got++; prog(); }); }

  /* case studies: background images near the viewport, behind a shimmer */
  var bgs=[].slice.call(document.querySelectorAll('[data-bg]'));
  function load(el){
    if(el._p) return el._p;
    var urls=el.getAttribute('data-bg').split('|');
    el._p=Promise.all(urls.map(function(u){ return new Promise(function(r){ var im=new Image(); im.onload=function(){ r(1); }; im.onerror=function(){ r(0); }; im.src=u; }); }))
      .then(function(ok){
        if(ok.indexOf(0)>-1){ el.classList.add('err'); el._p=null; failed.push(el); retrySoon(); return; }
        el.classList.remove('err');
        urls.forEach(function(u,i){ el.style.setProperty('--b'+i,'url("'+u+'")'); }); el.classList.add('ok'); });
    return el._p;
  }
  /* error state: a shimmer that never ends would claim it is still loading. A failed image goes to a
     still placeholder, is retried once a few seconds later, and again whenever the connection returns. */
  var failed=[], rt=0, tries=0;
  function retry(){ rt=0; var f=failed; failed=[]; f.forEach(load); }
  function retrySoon(){ if(!rt&&tries<1){ tries++; rt=setTimeout(retry,4000); } }
  addEventListener('online',function(){ tries=0; retry(); });
  /* load by vertical distance only: images off to the side inside a sideways row, or further down a
     phone screen, are clipped from any IntersectionObserver until scrolled to, and would show as
     placeholders mid-swipe. A phone screen's images go with the phone. */
  var pendingBg=bgs.map(function(el){ return {el:el, ref:el.closest('.sy')||el}; });
  function nearBg(){ nearBg.q=0; var lo=-1200, hi=innerHeight+1200;
    pendingBg=pendingBg.filter(function(it){ var r=it.ref.getBoundingClientRect(); if(r.bottom>lo&&r.top<hi){ load(it.el); return false; } return true; });
    if(!pendingBg.length){ removeEventListener('scroll',qBg); removeEventListener('resize',qBg); } }
  function qBg(){ if(!nearBg.q) nearBg.q=requestAnimationFrame(nearBg); }
  addEventListener('scroll',qBg,{passive:true}); addEventListener('resize',qBg); nearBg();
  bgs.forEach(function(el){ if(el.getBoundingClientRect().top<vh) wait(load(el)); });

  /* home: plain images fade in; the first screen's count toward the loader */
  [].slice.call(document.querySelectorAll('img')).forEach(function(im){
    if(im.complete&&im.naturalWidth) return;
    im.classList.add('ld-in');
    var p=new Promise(function(r){ im.addEventListener('load',r); im.addEventListener('error',r); }).then(function(){ im.classList.add('ok'); });
    if(im.getBoundingClientRect().top<vh&&im.loading!=='lazy') wait(p);
  });
  if(document.fonts&&document.fonts.ready) wait(document.fonts.ready);
  prog(); setTimeout(finish,4000);
  /* back/forward cache: never show a stale loader */
  addEventListener('pageshow',function(e){ if(e.persisted) finish(); });

  /* case studies: reading progress, and a way back to the top once you are a screen down */
  var rp=document.querySelector('#rp i'), tt=document.getElementById('totop'), tick=false;
  function upd(){ tick=false; var h=document.documentElement.scrollHeight-innerHeight, y=scrollY;
    if(rp) rp.style.transform='scaleX('+(h>0?Math.min(1,y/h):0)+')'; if(tt) tt.classList.toggle('on',y>innerHeight); }
  if(rp||tt){
    addEventListener('scroll',function(){ if(!tick){ tick=true; requestAnimationFrame(upd); } },{passive:true});
    addEventListener('resize',upd); upd();
    if(tt) tt.addEventListener('click',function(){
      scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'});
      var f=document.querySelector('#hdr a'); if(f) f.focus({preventScroll:true}); });
  }

  /* hovering a link to another page fetches it, so the click lands on a warm page */
  var seen={};
  document.addEventListener('pointerover',function(e){
    var a=e.target.closest&&e.target.closest('a[href]'); if(!a) return;
    var u=new URL(a.href,location.href); if(u.origin!==location.origin||u.pathname===location.pathname||seen[u.pathname]) return;
    seen[u.pathname]=1; var l=document.createElement('link'); l.rel='prefetch'; l.href=u.pathname; document.head.appendChild(l);
  },{passive:true});
})();

/* Screen recordings loop, so each gets a pause/play control (WCAG 2.2.2: motion over 5s needs one).
   A pause sticks: scrolling away and back doesn't restart it. Under reduced motion nothing autoplays,
   and this button is how to opt in. If a recording fails to load, its poster stays and the button goes. */
(function(){
  var vids=[].slice.call(document.querySelectorAll('video.vid')); if(!vids.length) return;
  var still=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var PLAY='<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M6.5 4.5v11l9-5.5z" fill="currentColor"/></svg>',
      PAUSE='<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M6 4.5h2.6v11H6zM11.4 4.5H14v11h-2.6z" fill="currentColor"/></svg>';
  vids.forEach(function(v){
    var held=still, orig=v.play.bind(v), b=document.createElement('button');
    v.play=function(){ return held?Promise.resolve():orig(); };
    b.type='button'; b.className='vc';
    function paint(){ var on=!v.paused&&!held; b.innerHTML=on?PAUSE:PLAY; b.setAttribute('aria-label',(on?'Pause':'Play')+' screen recording'); }
    b.addEventListener('click',function(){
      if(!v.paused&&!held){ held=true; v.pause(); }
      else{ held=false;
        if(!v.getAttribute('src')){ v.preload='auto'; v.src=v.getAttribute('data-src'); }
        var p=orig(); if(p&&p.catch) p.catch(function(){}); }
      paint();
    });
    ['play','pause'].forEach(function(e){ v.addEventListener(e,paint); });
    v.addEventListener('error',function(){ b.hidden=true; });
    v.parentNode.appendChild(b); paint();
  });
})();

/* View-case-study pill: on a mouse, it trails the pointer inside the card it belongs to */
(function(){
  if(!matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  var cards=[].slice.call(document.querySelectorAll('.card, a.nx'));
  if(!cards.length) return;
  document.documentElement.classList.add('cf');
  var still=matchMedia('(prefers-reduced-motion: reduce)').matches;
  cards.forEach(function(card){
    var pill=card.querySelector('.cta'); if(!pill) return;
    var x=0,y=0,tx=0,ty=0,run=false,live=false;
    function aim(e){
      var r=card.getBoundingClientRect(),kx=card.offsetWidth/r.width,ky=card.offsetHeight/r.height;
      var px=(e.clientX-r.left)*kx+14, py=(e.clientY-r.top)*ky+18;
      tx=Math.max(12,Math.min(px,card.offsetWidth-pill.offsetWidth-12));
      ty=Math.max(12,Math.min(py,card.offsetHeight-pill.offsetHeight-12));
    }
    function frame(){
      var k=still?1:.28; x+=(tx-x)*k; y+=(ty-y)*k;
      pill.style.translate=x.toFixed(1)+'px '+y.toFixed(1)+'px';
      if(live&&(Math.abs(tx-x)>.3||Math.abs(ty-y)>.3)) requestAnimationFrame(frame); else run=false;
    }
    function go(){ if(!run){run=true;requestAnimationFrame(frame);} }
    card.addEventListener('pointerenter',function(e){ if(e.pointerType!=='mouse')return; live=true; aim(e); x=tx; y=ty; go(); });
    card.addEventListener('pointermove',function(e){ if(e.pointerType!=='mouse')return; aim(e); go(); });
    card.addEventListener('pointerleave',function(){ live=false; });
  });
})();
</script>'''


def lum(rgb):
    r, g, b = [int(x) / 255 for x in rgb[:3]]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _skip(css, i):
    """index just past a comment or string starting at i, else i"""
    if css.startswith('/*', i):
        j = css.find('*/', i + 2); return len(css) if j < 0 else j + 2
    if css[i] in '"\'':
        q, j = css[i], i + 1
        while j < len(css) and css[j] != q: j += 2 if css[j] == '\\' else 1
        return j + 1
    return i


def _split_top(sel):
    out, d, cur = [], 0, ''
    for c in sel:
        if c in '([': d += 1
        elif c in ')]': d -= 1
        if c == ',' and d == 0: out.append(cur); cur = ''
        else: cur += c
    return out + [cur]


def gate_hover(css, inside=False):
    """Move every :hover selector behind @media (hover:hover) and (pointer:fine). Rules keep their
    order; comma lists are split so the non-hover selectors stay put. Idempotent."""
    out, i, n = [], 0, len(css)
    while i < n:
        j = i
        while j < n and css[j] not in '{}':
            k = _skip(css, j); j = k if k != j else j + 1
        if j >= n or css[j] == '}': out.append(css[i:]); break
        d, k = 0, j
        while k < n:
            m = _skip(css, k)
            if m != k: k = m; continue
            if css[k] == '{': d += 1
            elif css[k] == '}':
                d -= 1
                if d == 0: break
            k += 1
        pre, body = css[i:j], css[j + 1:k]
        head = re.match(r'(\s*(?:/\*.*?\*/\s*)*)(.*)$', pre, re.S)
        lead, sel = head.group(1), head.group(2)
        if sel.lstrip().startswith('@'):
            if re.match(r'\s*@(media|supports|container|layer)\b', sel):
                hov = inside or 'hover:hover' in sel.replace(' ', '')
                out.append(pre + '{' + gate_hover(body, hov) + '}')
            else:
                out.append(pre + '{' + body + '}')
        elif inside or ':hover' not in sel:
            out.append(pre + '{' + body + '}')
        else:
            parts = _split_top(sel)
            h = [p for p in parts if ':hover' in p]; r = [p for p in parts if ':hover' not in p]
            res = lead
            if r: res += ','.join(r).rstrip() + '{' + body + '}'
            res += '@media (hover:hover) and (pointer:fine){' + ','.join(h).strip() + '{' + body + '}}'
            out.append(res)
        i = k + 1
    return ''.join(out)


def strip(s):
    return re.sub(r'\s*' + re.escape(A) + r'.*?' + re.escape(B), '', s, flags=re.S)


def lazy_bgs(s):
    """url('img/x') in a style attribute -> var(--bN, none), with the url listed in data-bg."""
    def tag(m):
        attrs = m.group(0)
        if 'data-bg=' in attrs: return attrs
        st = re.search(r'style="([^"]*)"', attrs)
        if not st or "url('" not in st.group(1): return attrs
        urls = []
        def sub(u):
            if not re.match(r"url\('(img/|\.\./\.\./img/)", u.group(0)): return u.group(0)
            urls.append(u.group(1)); return 'var(--b%d, none)' % (len(urls) - 1)
        new = re.sub(r"url\('([^']+)'\)", sub, st.group(1))
        if not urls: return attrs
        return attrs.replace(st.group(0), 'data-bg="%s" style="%s"' % ('|'.join(urls), new))
    return re.sub(r'<(?:div|a)\s[^>]*>', tag, s)


def apply(path):
    s = strip(open(path).read())
    case = 'id="canvas"' in s
    bg = (255, 255, 255)
    m = re.search(r'\.canvas\{[^}]*background:(?:linear-gradient\()?rgba?\((\d+),(\d+),(\d+)', s)
    if case and m: bg = tuple(int(x) for x in m.groups())
    dark = lum(bg) < 0.4
    title = re.search(r'<title>(.*?)</title>', s).group(1)
    name = title.split(' — ')[0].split(' · ')[0] if case else 'Dhanesh Shetye'
    url = SITE + os.path.relpath(os.path.dirname(path), ROOT) + '/'
    desc = re.search(r'<meta name="description" content="([^"]*)"', s).group(1)
    tok = dict(url=url, title=title, desc=desc,
               btn='#fff' if dark else '#151515', btnfg='#151515' if dark else '#fff',
               bg='rgb(%d,%d,%d)' % bg, fg='#fff' if dark else '#151515',
               track='rgba(255,255,255,.16)' if dark else 'rgba(0,0,0,.1)',
               sk='rgba(255,255,255,.04)' if dark else 'rgba(0,0,0,.04)',
               sk2='rgba(255,255,255,.10)' if dark else 'rgba(0,0,0,.08)',
               name=name, kicker='Case study' if case else 'Portfolio')
    if case: s = lazy_bgs(s)
    s = re.sub(r'(<style[^>]*>)(.*?)(</style>)', lambda m: m.group(1) + gate_hover(m.group(2)) + m.group(3), s, flags=re.S)
    # outside links open in a new tab (case-study source links came through from Figma without it)
    def ext(m):
        t = m.group(0)
        if 'target=' in t or 'dhanesh100.github.io' in t: return t
        return t[:-1] + ' target="_blank" rel="noopener">'
    s = re.sub(r'<a\s[^>]*href="https?://[^"]*"[^>]*>', ext, s)
    s = s.replace('</head>', '%s\n%s\n%s\n%s\n</head>' % (A, META % tok, CSS % tok, B), 1)
    s = re.sub(r'<body([^>]*)>', lambda m: '<body%s>\n%s%s%s%s' % (m.group(1), A, OVERLAY % tok, AIDS if case else '', B), s, count=1)
    pop = os.path.relpath(os.path.join(ROOT, 'home', 'pop.js'), os.path.dirname(path))
    extra = '<script src="%s" defer></script>' % pop
    if case: extra += '\n<script src="%s" defer></script>' % pop.replace('pop.js', 'scroll.js')
    s = s.replace('</body>', '%s\n%s\n%s\n%s\n</body>' % (A, JS, extra, B), 1)
    open(path, 'w').write(s)
    print('%-40s %s, %d lazy images' % (os.path.relpath(path, ROOT), 'dark' if dark else 'light', s.count('data-bg=')))


def og_image(path):
    """og.jpg, 1200x630: the page's first screen at 1440x756, after the loader has gone."""
    out = os.path.join(os.path.dirname(path), 'og.jpg'); png = out + '.png'
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--allow-file-access-from-files',
                    '--virtual-time-budget=9000', '--window-size=1440,756', '--screenshot=' + png, 'file://' + path], capture_output=True)
    subprocess.run(['sips', '-s', 'format', 'jpeg', '-s', 'formatOptions', '80', '--resampleWidth', '1200', png, '--out', out], capture_output=True)
    os.remove(png)


if __name__ == '__main__':
    for p in [os.path.join(ROOT, 'home', 'index.html')] + sorted(glob.glob(os.path.join(ROOT, 'home', 'work', '*', 'index.html'))):
        apply(p)
        if '--og' in sys.argv: og_image(p)
