#!/usr/bin/env python3
"""Regenerate scan/index.html from the scan panel inside index.html.

Run from the repo root after editing the scan panel:
    python3 build-scan.py

Extracts the scan panel + overlays, inlines each of the 11 screen exports
exactly once (rather than cloning them from the other panels at runtime),
and writes a standalone self-contained file.
"""
import io, re, sys

SRC, OUT = 'index.html', 'scan/index.html'
KEYS = ['none', 'pending', 'member', 'group', 'inactive', 'family',
        'home', 'one', 'fullfam', 'life', 'kyp']

h = io.open(SRC, encoding='utf-8').read()

# ── style, plus an explicit dark stamp for hosts that set one ──
style = h[h.index('<style>'): h.index('</style>') + 8]
m = re.search(r'@media \(prefers-color-scheme: dark\) \{\s*'
              r'(:root:not\(\[data-theme="light"\]\) \{.*?\n    \})\s*\n  \}', style, re.S)
if not m:
    sys.exit('dark token block not found')
dark = re.sub(r':root:not\(\[data-theme="light"\]\)', ':root[data-theme="dark"]', m.group(1))
style = style.replace('</style>',
                      '\n  /* explicit dark choice, where the host stamps one */\n  ' + dark + '\n</style>')

# ── the scan panel and its overlays ────────────────────────────
start = h.index('<div role="tabpanel" id="panel-scan"')
panel = h[start: h.index('\n<script>', start)]

# ── inline the screens: each key is used exactly once ──────────
lib, seen = {}, set()
for mm in re.finditer(r'<img\s+src="(data:[^"]+)"\s+alt="([^"]*)"', h):
    if mm.group(1) in seen:
        continue
    seen.add(mm.group(1))
    if len(lib) < len(KEYS):
        lib[KEYS[len(lib)]] = (mm.group(1), mm.group(2))

def embed(mo):
    key = mo.group(1)
    if key not in lib:
        sys.exit('unknown screen key: ' + key)
    src, alt = lib[key]
    return ('<div class="sc-frame"><img src="%s" alt="%s" loading="lazy" decoding="async"></div>'
            % (src, alt))

panel, n = re.subn(r'<div class="sc-frame" data-screen="([a-z]+)"></div>', embed, panel)
if n != 11:
    sys.exit('expected 11 screen slots, replaced %d' % n)

# ── standalone: no longer a tabpanel; repo-relative links must resolve ──
panel = panel.replace(
    '<div role="tabpanel" id="panel-scan" aria-labelledby="tab-scan" tabindex="0">',
    '<main id="panel-scan">', 1)
panel = panel.replace('</div>\n\n<!-- ═══════════════ OVERLAYS',
                      '</main>\n\n<!-- ═══════════════ OVERLAYS', 1)
panel = panel.replace('href="measurement/"',
                      'href="https://dhanesh100.github.io/Case-study/measurement/"')

JS = '''<script>
  (function () {
    'use strict';
    var FOCUSABLE = 'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';
    var openOverlay = null, lastFocused = null;

    function close() {
      if (!openOverlay) { return; }
      openOverlay.hidden = true;
      document.body.classList.remove('sc-locked');
      if (lastFocused && lastFocused.focus) { lastFocused.focus(); }
      openOverlay = null; lastFocused = null;
    }

    function open(id, trigger) {
      var ov = document.getElementById(id);
      if (!ov) { return; }
      if (openOverlay) { close(); }
      lastFocused = trigger || document.activeElement;
      ov.hidden = false;
      document.body.classList.add('sc-locked');
      openOverlay = ov;
      var body = ov.querySelector('.sc-ov-body');
      if (body) { body.scrollTop = 0; }
      var x = ov.querySelector('.sc-ov-x');
      if (x) { x.focus(); }
    }

    document.addEventListener('click', function (e) {
      var opener = e.target.closest ? e.target.closest('[data-open]') : null;
      if (opener) { e.preventDefault(); open(opener.getAttribute('data-open'), opener); return; }
      if (!openOverlay) { return; }
      if (e.target.closest('[data-close]') || e.target.classList.contains('sc-ov-scrim')) {
        e.preventDefault(); close();
      }
    });

    document.addEventListener('keydown', function (e) {
      if (!openOverlay) { return; }
      if (e.key === 'Escape') { e.preventDefault(); close(); return; }
      if (e.key !== 'Tab') { return; }
      var panel = openOverlay.querySelector('.sc-ov-panel');
      var items = [].slice.call(panel.querySelectorAll(FOCUSABLE)).filter(function (el) {
        return el.offsetParent !== null;
      });
      if (!items.length) { return; }
      var first = items[0], last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });

    var b = document.getElementById('sc-btn-before'), a = document.getElementById('sc-btn-after');
    var bp = document.getElementById('sc-pane-before'), ap = document.getElementById('sc-pane-after');
    if (b && a && bp && ap) {
      var flip = function (isBefore) {
        b.setAttribute('aria-pressed', String(isBefore));
        a.setAttribute('aria-pressed', String(!isBefore));
        bp.hidden = !isBefore; ap.hidden = isBefore;
      };
      b.addEventListener('click', function () { flip(true); });
      a.addEventListener('click', function () { flip(false); });
    }
  })();
</script>'''

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CoverSure Policy Portfolio — Dhanesh Shetye</title>
<meta name="description" content="Seven capabilities on one screen, each attached to a condition about when it becomes useful to that user. A product design case study in six decisions, with the reasoning behind each one.">
<meta name="author" content="Dhanesh Shetye">
<meta name="color-scheme" content="light dark">
<meta property="og:title" content="CoverSure Policy Portfolio">
<meta property="og:description" content="I turned a discovery problem into a rule set. Six design decisions on CoverSure's Policy Portfolio.">
<meta property="og:type" content="article">
'''

io.open(OUT, 'w', encoding='utf-8').write(
    HEAD + style + '\n<body>\n' + panel + '\n' + JS + '\n</body>\n</html>\n')
print('wrote %s' % OUT)
