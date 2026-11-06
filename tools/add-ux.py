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
Reduced motion: no shimmer, no fades, no bar animation."""
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
#totop:hover{transform:translateY(-2px)}
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
html.cf .card:hover .cta,html.cf a.nx:hover .cta{opacity:1;scale:1;gap:7px;padding:0 13px 0 15px}
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
    el._p=Promise.all(urls.map(function(u){ return new Promise(function(r){ var im=new Image(); im.onload=im.onerror=r; im.src=u; }); }))
      .then(function(){ urls.forEach(function(u,i){ el.style.setProperty('--b'+i,'url("'+u+'")'); }); el.classList.add('ok'); });
    return el._p;
  }
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ load(e.target); io.unobserve(e.target); } }); },{rootMargin:'1200px 0px'});
    bgs.forEach(function(el){ io.observe(el); });
  } else bgs.forEach(load);
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
    s = s.replace('</head>', '%s\n%s\n%s\n%s\n</head>' % (A, META % tok, CSS % tok, B), 1)
    s = re.sub(r'<body([^>]*)>', lambda m: '<body%s>\n%s%s%s%s' % (m.group(1), A, OVERLAY % tok, AIDS if case else '', B), s, count=1)
    s = s.replace('</body>', '%s\n%s\n%s\n</body>' % (A, JS, B), 1)
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
