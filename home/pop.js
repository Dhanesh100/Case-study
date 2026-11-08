/* Get In Touch popover — Figma ProSure 249:20848.
   A white panel drops from the top of the screen (bottom corners 40px, shadow 0 32 48 #00000014),
   carrying the "Hey! Let's Work Together" block; a round close button sits 24px under it.
   Opens from every link to #contact whose text says "get in touch". Esc, the scrim and the
   close button dismiss it; focus is kept inside while it is open and returned afterwards. */
(function () {
  var me = document.currentScript;
  var base = me ? me.src.replace(/pop\.js(\?.*)?$/, '') : '/';
  var F = base + 'fonts/';
  var css =
    '@font-face{font-family:"gpEiko";src:url("' + F + 'PPEiko-Black.woff2") format("woff2");font-weight:900;font-display:swap}' +
    '@font-face{font-family:"gpPangram";src:url("' + F + 'PPPangramSans-Semibold.woff2") format("woff2");font-weight:600;font-display:swap}' +
    '@font-face{font-family:"gpPangram";src:url("' + F + 'PPPangramSans-Medium.woff2") format("woff2");font-weight:500;font-display:swap}' +
    '@font-face{font-family:"gpMontreal";src:url("' + F + 'PPNeueMontreal-Regular.woff2") format("woff2");font-weight:400;font-display:swap}' +
    '.gp{position:fixed;inset:0;z-index:2147483000;visibility:hidden;pointer-events:none;color:#262626;-webkit-font-smoothing:antialiased;transition:visibility 0s .38s}' +
    '.gp.on{visibility:visible;pointer-events:auto;transition:visibility 0s}' +
    '.gp *{box-sizing:border-box}' +
    '.gp-sc{position:absolute;inset:0;background:rgba(17,17,17,.36);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);opacity:0;transition:opacity .35s ease}' +
    '.gp.on .gp-sc{opacity:1}' +
    '.gp-p{position:absolute;left:0;right:0;top:0;max-height:calc(100dvh - 112px);overflow:auto;overscroll-behavior:contain;background:#fff;' +
      'border-radius:0 0 40px 40px;box-shadow:0 32px 48px rgba(0,0,0,.08);padding:clamp(56px,13vh,120px) clamp(24px,9.45vw,136px) 0;' +
      'transform:translateY(-104%);transition:transform .55s cubic-bezier(.22,1,.36,1)}' +
    '.gp.on .gp-p{transform:none}.gp:not(.on) .gp-p{transition:transform .36s cubic-bezier(.2,0,0,1)}.gp-p:focus{outline:none}' +
    '.gp-in{max-width:1172px;margin:0 auto;display:flex;justify-content:space-between;gap:40px}' +
    '.gp-h{margin:0;font:900 clamp(64px,7.2vw,104px)/1 gpEiko,"PP Eiko",Didot,Georgia,serif;letter-spacing:-.02em;color:#262626;display:grid;gap:8px}' +
    '.gp-h .l1{display:flex;align-items:center}.gp-h .l1 img{width:.78em;height:auto;margin-left:4px}' +
    '.gp-h .l2{display:flex;gap:.15em}.gp-h .y{color:#ffc821}' +
    '.gp-l{display:grid;gap:24px;align-content:start;width:417px;flex:none}' +
    '.gp-r{display:grid;grid-template-columns:159px 1fr;align-items:start}' +
    '.gp-r small{padding-top:13px;font:600 18px/23px gpPangram,"PP Pangram Sans",system-ui,sans-serif;color:#262626}' +
    '.gp-r a{font:600 56px/73px gpPangram,"PP Pangram Sans",system-ui,sans-serif;color:#262626;text-decoration:none;display:inline-block;position:relative;text-transform:uppercase}' +
    '.gp-r a::after{content:"";position:absolute;left:0;right:100%;bottom:10px;height:3px;background:#ffc821;transition:right .3s ease}' +
    '.gp-r a:focus-visible::after{right:0}@media (hover:hover) and (pointer:fine){.gp-r a:hover::after{right:0}.gp-x:hover{background:#fff;scale:1.08}}' +
    '.gp-r .mail{display:table;margin-top:-12px;padding-left:4px;font:500 20px/26px gpPangram,"PP Pangram Sans",system-ui,sans-serif;text-transform:none}' +
    '.gp-r .mail::after{height:2px;bottom:1px}' +
    '.gp-f{max-width:1172px;margin:clamp(40px,8vh,84px) auto 0;padding:16px 0 18px;border-top:2px solid #737373;text-align:right;font:400 14px/18px gpMontreal,"PP Neue Montreal",system-ui,sans-serif;color:#737373}' +
    '.gp-x{position:absolute;left:50%;top:0;width:64px;height:64px;margin-left:-32px;border:0;border-radius:50%;background:rgba(255,255,255,.96);' +
      '-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px);box-shadow:0 16px 40px rgba(0,0,0,.12);display:grid;place-items:center;cursor:pointer;color:#151515;' +
      'opacity:0;scale:.6;transition:opacity .25s ease,scale .35s cubic-bezier(.34,1.56,.64,1),background .2s}' +
    '.gp.on .gp-x{opacity:1;scale:1;transition-delay:.28s}' +
    '.gp.on .gp-x:active{scale:.94;transition:scale .12s cubic-bezier(.23,1,.32,1)}' +
    '.gp a:focus-visible,.gp-x:focus-visible{outline:2px solid #151515;outline-offset:4px}' +
    'html.gp-lock,html.gp-lock body{overflow:hidden}' +
    '@media (max-width:900px){.gp-in{flex-direction:column}.gp-l{width:100%}.gp-r a{font-size:40px;line-height:54px}}' +
    '@media (max-width:640px){.gp-p{border-radius:0 0 28px 28px;padding:48px 20px 0}.gp-h{font-size:52px;line-height:56px}' +
      '.gp-r{grid-template-columns:1fr}.gp-r small{padding-top:0;font-size:15px;line-height:20px}.gp-r a{font-size:32px;line-height:42px}' +
      '.gp-r .mail{margin-top:-4px;font-size:16px}.gp-l{gap:18px}.gp-f{margin-top:32px}.gp-x{width:56px;height:56px;margin-left:-28px}}' +
    '@media (prefers-reduced-motion:reduce){.gp-p,.gp-sc,.gp-x{transition:opacity .15s ease!important}.gp-p{transform:none}.gp:not(.on) .gp-p{opacity:0}}';

  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  var year = new Date().getFullYear();
  var root = document.createElement('div');
  root.className = 'gp'; root.id = 'gp';
  root.setAttribute('role', 'dialog'); root.setAttribute('aria-modal', 'true');
  root.setAttribute('aria-labelledby', 'gp-h'); root.setAttribute('aria-hidden', 'true');
  root.innerHTML =
    '<div class="gp-sc" data-close></div>' +
    '<div class="gp-p" tabindex="-1"><div class="gp-in">' +
      '<h2 class="gp-h" id="gp-h"><span class="l1">Hey!<img src="' + base + 'img/wave.webp" alt="" width="81" height="80"></span>' +
      '<span class="l2"><span>Let’s</span><span class="y">Work</span></span><span class="y">Together</span></h2>' +
      '<div class="gp-l">' +
        '<div class="gp-r"><small>For project<br>inquiries</small><div><a href="mailto:dhanesh.ns19@gmail.com">Email</a><a class="mail" href="mailto:dhanesh.ns19@gmail.com">dhanesh.ns19@gmail.com</a></div></div>' +
        '<div class="gp-r"><small>For more<br>work shots</small><div><a href="https://dribbble.com/Dhanesh10" target="_blank" rel="noopener">Dribbble</a></div></div>' +
        '<div class="gp-r"><small>For updated<br>work</small><div><a href="https://www.figma.com/design/3juSNaBmkrk7Iz2D4rqSq0/Portfolio-Work-1?node-id=221-29228&amp;t=uAKpDcfVVhRdSt7N-1" target="_blank" rel="noopener">Figma</a></div></div>' +
        '<div class="gp-r"><small>For my work<br>experience</small><div><a href="https://www.linkedin.com/in/dhanesh-n-shetye-10/" target="_blank" rel="noopener">Linkedin</a></div></div>' +
      '</div></div>' +
      '<footer class="gp-f">© ' + year + ' Dhanesh N Shetye</footer>' +
    '</div>' +
    '<button class="gp-x" type="button" aria-label="Close" data-close><svg width="32" height="32" viewBox="0 0 32 32" aria-hidden="true">' +
      '<path d="M8 8l16 16M24 8L8 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></button>';

  var panel = root.querySelector('.gp-p'), xbtn = root.querySelector('.gp-x');
  var last = null, isOpen = false, inerted = [];

  function place() { xbtn.style.top = (panel.getBoundingClientRect().height + 24) + 'px'; }
  function focusables() { return root.querySelectorAll('.gp-p a, .gp-x'); }

  function open(from) {
    if (isOpen) return;
    isOpen = true; last = from || document.activeElement;
    if (!root.parentNode) document.body.appendChild(root);
    panel.scrollTop = 0;
    place();
    root.setAttribute('aria-hidden', 'false');
    document.documentElement.classList.add('gp-lock');
    /* the page behind can't be reached by any means while the dialog is open, not only by Tab */
    [].forEach.call(document.body.children, function (n) { if (n !== root && !n.inert) { n.inert = true; inerted.push(n); } });
    void root.offsetWidth;
    root.classList.add('on');
    setTimeout(function () { if (isOpen) panel.focus({ preventScroll: true }); }, 60);
  }
  function close() {
    if (!isOpen) return;
    isOpen = false;
    root.classList.remove('on');
    root.setAttribute('aria-hidden', 'true');
    document.documentElement.classList.remove('gp-lock');
    inerted.forEach(function (n) { n.inert = false; }); inerted = [];
    if (last && last.focus) last.focus({ preventScroll: true });
  }

  root.addEventListener('click', function (e) { if (e.target.closest('[data-close]')) close(); });
  document.addEventListener('keydown', function (e) {
    if (!isOpen) return;
    if (e.key === 'Escape') { e.preventDefault(); close(); return; }
    if (e.key === 'Tab') {
      var f = focusables(), a = f[0], z = f[f.length - 1];
      if (e.shiftKey && document.activeElement === a) { e.preventDefault(); z.focus(); }
      else if (!e.shiftKey && document.activeElement === z) { e.preventDefault(); a.focus(); }
    }
  });
  addEventListener('resize', function () { if (isOpen) place(); });

  /* Every "Get in touch" button opens it, whatever its href (header #contact links, the case-study
     CTA banners that used to be mailto:, the phone header). The href stays as the no-JS fallback. */
  var GIT = /get\s*in\s*touch/i;
  function trigger(t) {
    var a = t && t.closest && t.closest('a, button, [role="button"]');
    return a && !root.contains(a) && GIT.test(a.textContent) ? a : null;
  }
  [].forEach.call(document.querySelectorAll('a, button'), function (a) {
    if (!GIT.test(a.textContent)) return;
    a.setAttribute('aria-haspopup', 'dialog');
    if (a.getAttribute('aria-label') && !GIT.test(a.getAttribute('aria-label'))) a.setAttribute('aria-label', 'Get in touch');
  });
  document.addEventListener('click', function (e) {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var a = trigger(e.target); if (!a) return;
    e.preventDefault(); e.stopPropagation();
    open(a);
  }, true);

  window.openContact = open;
  if (location.hash === '#get-in-touch') open();
})();
