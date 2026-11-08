/* Phone-screen scrollers (.sy) on the case studies.
   1. Nudge: the first times a phone comes into view, its screen glides up and back (a "peek"),
      and a small "Scroll" chip sits on it, so people see the design continues below.
      Stops for good as soon as they scroll it themselves. Reduced motion: chip only.
   2. Latch: a page scroll that is already under way keeps scrolling the page when a phone slides
      under the pointer. The phone only takes the wheel when a gesture starts on it. */
(function () {
  var phones = [].slice.call(document.querySelectorAll('.sy')).filter(function (e) { return e.scrollHeight > e.clientHeight + 40; });
  if (!phones.length) return;
  var still = matchMedia('(prefers-reduced-motion: reduce)').matches;

  var st = document.createElement('style');
  st.textContent =
    '.sy-chip{position:absolute;z-index:4;pointer-events:none;display:flex;align-items:center;gap:6px;padding:8px 14px 8px 10px;border-radius:999px;' +
      'background:rgba(21,21,21,.82);color:#fff;font:600 13px/16px "PP Neue Montreal",-apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif;letter-spacing:.3px;' +
      '-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);box-shadow:0 8px 24px rgba(0,0,0,.18);transform:translateX(-50%);transition:opacity .4s ease}' +
    '.sy-chip svg{animation:sy-b 1.4s ease-in-out 4}' +
    '.sy-chip.gone{opacity:0}' +
    '@keyframes sy-b{0%,100%{transform:translateY(-2px)}50%{transform:translateY(3px)}}' +
    '@media (prefers-reduced-motion:reduce){.sy-chip svg{animation:none}}';
  document.head.appendChild(st);

  phones.forEach(function (sy) {
    var used = false, shown = 0, timer = 0, anim = 0, visible = false;
    var chip = document.createElement('div');
    chip.className = 'sy-chip'; chip.setAttribute('aria-hidden', 'true');
    chip.innerHTML = '<svg width="16" height="16" viewBox="0 0 16 16"><path d="M8 3v10M4 9l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Scroll';
    function place() {
      chip.style.left = (sy.offsetLeft + sy.offsetWidth / 2) + 'px';
      chip.style.top = (sy.offsetTop + sy.offsetHeight - 64) + 'px';
    }
    place(); sy.parentNode.appendChild(chip);
    var rq = 0; addEventListener('resize', function () { if (!rq) rq = requestAnimationFrame(function () { rq = 0; place(); }); });

    function stop() {
      if (used) return; used = true; cancelAnimationFrame(anim); clearTimeout(timer);
      chip.classList.add('gone');
    }
    ['wheel', 'pointerdown', 'touchstart', 'keydown'].forEach(function (t) { sy.addEventListener(t, stop, { passive: true }); });

    /* one peek: up ~22% of a screen and back, 1.8s */
    function peek() {
      if (used || !visible || shown >= 3) return;
      shown++;
      var d = Math.min(240, sy.scrollHeight - sy.clientHeight, sy.clientHeight * 0.32), t0 = 0, from = sy.scrollTop;
      function step(t) {
        if (used) return;
        t0 = t0 || t; var p = Math.min(1, (t - t0) / 1800);
        var k = p < .45 ? ease(p / .45) : (p < .6 ? 1 : 1 - ease((p - .6) / .4));
        sy.scrollTop = from + d * k;
        if (p < 1) anim = requestAnimationFrame(step); else timer = setTimeout(peek, 3800);
      }
      anim = requestAnimationFrame(step);
    }
    function ease(x) { return x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; }

    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (es) {
        visible = es[0].isIntersecting;
        clearTimeout(timer);
        if (visible && !still && !used) timer = setTimeout(peek, 600);
      }, { threshold: 0.6 }).observe(sy);
    }
  });

  /* scroll latch */
  var lastT = 0, origin = null;
  addEventListener('wheel', function (e) {
    var now = performance.now(), sy = e.target.closest && e.target.closest('.sy');
    if (now - lastT > 320) origin = sy;           /* a new gesture: remember where it started */
    lastT = now;
    if (sy && origin !== sy && !e.ctrlKey && Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
      e.preventDefault();
      scrollBy(0, e.deltaMode === 1 ? e.deltaY * 40 : e.deltaY);
    }
  }, { passive: false, capture: true });
})();
