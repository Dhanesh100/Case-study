# -*- coding: utf-8 -*-
"""Add the loading experience to the portfolio pages. Idempotent: run it after any rebuild.

    python3 tools/add-ux.py            # home/index.html and every home/work/*/index.html

What it adds, all inline (pages stay self-contained, no requests):
  1. A loader overlay: page name + a progress bar driven by the first screen's images and the
     fonts. Leaves as soon as they are in; never stays longer than 4s; without JS it leaves by CSS.
  2. Case studies: every background image loads only near the viewport, behind a soft shimmer.
     The style keeps `var(--b0, none)` where the url was; the url moves to data-bg.
  3. Cross-document view transitions, and hover-prefetch of internal pages.
Reduced motion: no shimmer, no fades, no bar animation."""
import glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A, B = '<!-- ux:start -->', '<!-- ux:end -->'

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
img.fade{opacity:0;transition:opacity .5s ease}img.fade.ok{opacity:1}
@media (prefers-reduced-motion:reduce){#ldr,.ldr-bar i,[data-bg]::before,img.fade{transition:none}[data-bg]::before{animation:none}
  @view-transition{navigation:none}}
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
    im.classList.add('fade');
    var p=new Promise(function(r){ im.addEventListener('load',r); im.addEventListener('error',r); }).then(function(){ im.classList.add('ok'); });
    if(im.getBoundingClientRect().top<vh&&im.loading!=='lazy') wait(p);
  });
  if(document.fonts&&document.fonts.ready) wait(document.fonts.ready);
  prog(); setTimeout(finish,4000);
  /* back/forward cache: never show a stale loader */
  addEventListener('pageshow',function(e){ if(e.persisted) finish(); });

  /* hovering a link to another page fetches it, so the click lands on a warm page */
  var seen={};
  document.addEventListener('pointerover',function(e){
    var a=e.target.closest&&e.target.closest('a[href]'); if(!a) return;
    var u=new URL(a.href,location.href); if(u.origin!==location.origin||u.pathname===location.pathname||seen[u.pathname]) return;
    seen[u.pathname]=1; var l=document.createElement('link'); l.rel='prefetch'; l.href=u.pathname; document.head.appendChild(l);
  },{passive:true});
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
    tok = dict(bg='rgb(%d,%d,%d)' % bg, fg='#fff' if dark else '#151515',
               track='rgba(255,255,255,.16)' if dark else 'rgba(0,0,0,.1)',
               sk='rgba(255,255,255,.04)' if dark else 'rgba(0,0,0,.04)',
               sk2='rgba(255,255,255,.10)' if dark else 'rgba(0,0,0,.08)',
               name=name, kicker='Case study' if case else 'Portfolio')
    if case: s = lazy_bgs(s)
    s = s.replace('</head>', '%s\n%s\n%s\n</head>' % (A, CSS % tok, B), 1)
    s = re.sub(r'<body([^>]*)>', lambda m: '<body%s>\n%s%s%s' % (m.group(1), A, OVERLAY % tok, B), s, count=1)
    s = s.replace('</body>', '%s\n%s\n%s\n</body>' % (A, JS, B), 1)
    open(path, 'w').write(s)
    print('%-40s %s, %d lazy images' % (os.path.relpath(path, ROOT), 'dark' if dark else 'light', s.count('data-bg=')))


if __name__ == '__main__':
    for p in [os.path.join(ROOT, 'home', 'index.html')] + sorted(glob.glob(os.path.join(ROOT, 'home', 'work', '*', 'index.html'))):
        apply(p)
