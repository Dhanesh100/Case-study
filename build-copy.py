#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate COPY-<VERSION>.md from the live markup in index.html.

The copy document is derived, never hand-written, so it cannot drift from what
is actually published.  Run after every change to a version panel:

    python3 build-copy.py v10
"""
import io, re, sys, html as H

VER = (sys.argv[1] if len(sys.argv) > 1 else 'v10').lower()
SRC, OUT = 'index.html', 'COPY-%s.md' % VER.upper()

doc = io.open(SRC, encoding='utf-8').read()


def strip(s):
    """Markup -> plain text, keeping em-dash/rupee entities readable."""
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = H.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()


def panel(name):
    a = doc.index('<div role="tabpanel" id="panel-%s"' % name)
    nxt = [m.start() for m in re.finditer(r'<div role="tabpanel" id="panel-', doc) if m.start() > a]
    return doc[a:nxt[0]] if nxt else doc[a:]


p = panel(VER)
hero = p[:re.search(r'<section class="v5-sec"', p).start()]   # hero only — keeps the
                                               # summary regex from running on
                                               # into the sections below it
out = []
W = out.append

title = strip(re.search(r'<h1 class="v5-h1">([\s\S]*?)</h1>', hero).group(1))
W('# CoverSure Policy Portfolio — %s copy\n' % VER.upper())
W('Every word on the page, surface and *See more*.')
W('**Generated from the live markup by `build-copy.py`, so it cannot drift from what is published.**\n')
W('**Live:** <https://dhanesh100.github.io/Case-study/#%s>\n' % VER)
W('---\n')

# ── hero ──────────────────────────────────────────────────────────────────
W('## Hero\n')
W('**Headline** — %s\n' % title)
for cls, label in [('v5-context', 'Product context'), ('v5-dek', 'Standfirst'), ('v4-meta', 'Meta')]:
    m = re.search(r'<p class="%s"[^>]*>([\s\S]*?)</p>' % cls, hero)
    if m:
        W('**%s** — %s\n' % (label, strip(m.group(1))))
m = re.search(r'<div class="v9-sum">([\s\S]*?)<p class="v9-sum-f">', hero)
if m:
    s = m.group(1)
    k = re.search(r'<p class="v9-sum-k">([\s\S]*?)</p>', s)
    if k:
        W('### One-screen summary\n')
        W('**%s**\n' % strip(k.group(1)))
    for d in re.finditer(r'<dt>([\s\S]*?)</dt>\s*<dd>([\s\S]*?)</dd>', s):
        W('- **%s** — %s' % (strip(d.group(1)), strip(d.group(2))))
    f = re.search(r'<p class="v9-sum-f">([\s\S]*?)</p>', hero)
    if f:
        W('\n%s\n' % strip(f.group(1)))
for cls, label in [('sc-honest', 'Honesty note'), ('sc-howto', 'How to read')]:
    m = re.search(r'<p class="%s"[^>]*>([\s\S]*?)</p>' % cls, hero)
    if m:
        W('**%s** — %s\n' % (label, strip(m.group(1))))
W('---\n')

# ── sections ──────────────────────────────────────────────────────────────
overlays = {}
for m in re.finditer(r'<div class="sc-ov" id="(%s-ov-\d+)"[\s\S]*?\n</div>\n' % VER, doc):
    overlays[m.group(1)] = m.group(0)

for sec in re.finditer(r'<section class="v5-sec"[^>]*>([\s\S]*?)</section>', p):
    s = sec.group(1)
    tag = re.search(r'<p class="v5-tag">(\d+)<b>([\s\S]*?)</b>', s)
    h2 = re.search(r'<h2 class="v5-title">([\s\S]*?)</h2>', s)
    W('## %s · %s\n' % (tag.group(1), strip(tag.group(2))))
    W('**Title** — %s\n' % strip(h2.group(1)))
    t = re.search(r'<p class="v5-take">([\s\S]*?)</p>', s)
    if t:
        W('**Lead** — %s\n' % strip(t.group(1)))

    # worked-example cards
    for ex in re.finditer(r'<li class="v10-exi">([\s\S]*?)</li>', s):
        e = ex.group(1)
        n = re.search(r'<p class="ex-n">([\s\S]*?)</p>', e)
        t2 = re.search(r'<h3 class="ex-t">([\s\S]*?)</h3>', e)
        W('**%s · %s**\n' % (strip(n.group(1)), strip(t2.group(1))))
        for d in re.finditer(r'<dt>([\s\S]*?)</dt><dd>([\s\S]*?)</dd>', e):
            W('- *%s* — %s' % (strip(d.group(1)), strip(d.group(2))))
        W('')

    # definition / branch lists
    for d in re.finditer(r'<(?:div class="v4-ev"|div class="v5-br[^"]*")><dt>([\s\S]*?)</dt><dd>([\s\S]*?)</dd>', s):
        W('- **%s** — %s' % (strip(d.group(1)), strip(d.group(2))))

    # before / after
    for c in re.finditer(r'<span class="ba-tag">([\s\S]*?)</span>\s*<div class="ba-card[^"]*">([\s\S]*?)</div>', s):
        W('- **%s** — %s' % (strip(c.group(1)), strip(c.group(2))))

    # tables
    for tb in re.finditer(r'<table>([\s\S]*?)</table>', s):
        body = tb.group(1)
        cap = re.search(r'<caption[^>]*>([\s\S]*?)</caption>', body)
        if cap:
            W('\n**%s**\n' % strip(cap.group(1)))
        heads = [strip(x) for x in re.findall(r'<th>([\s\S]*?)</th>', body)]
        if heads:
            W('| ' + ' | '.join(heads) + ' |')
            W('|' + '---|' * len(heads))
        for tr in re.finditer(r'<tr>((?:\s*<td>[\s\S]*?</td>)+)\s*</tr>', body):
            cells = [strip(x) for x in re.findall(r'<td>([\s\S]*?)</td>', tr.group(1))]
            W('| ' + ' | '.join(cells) + ' |')
        W('')

    # diagram alt text + caption
    for f in re.finditer(r'<svg viewBox="[^"]*" role="img" aria-label="([^"]*)"', s):
        W('\n**Diagram** — %s\n' % strip(f.group(1)))
    for c in re.finditer(r'<p class="v9-cap">([\s\S]*?)</p>', s):
        W('*Caption* — %s\n' % strip(c.group(1)))

    # screens
    for sh in re.finditer(r'data-screen="([^"]+)"></div><p class="sc-cap">([\s\S]*?)</p>', s):
        W('- *Screen · %s* — %s' % (sh.group(1), strip(sh.group(2))))

    # flow + notices
    for fl in re.finditer(r'<p class="sc-flow">([\s\S]*?)</p>', s):
        W('\n**Flow** — %s\n' % strip(fl.group(1)))
    for nt in re.finditer(r'<p class="sc-notice">([\s\S]*?)</p>', s):
        W('\n**Note** — %s\n' % strip(nt.group(1)))

    # the See-more panel behind this section
    mo = re.search(r'data-open="(%s-ov-\d+)"' % VER, s)
    if mo and mo.group(1) in overlays:
        ov = overlays[mo.group(1)]
        k = re.search(r'<span class="sc-skill">([\s\S]*?)</span>', ov)
        ot = re.search(r'<h3 class="sc-ov-title"[^>]*>([\s\S]*?)</h3>', ov)
        W('\n### See more — %s: “%s”\n' % (strip(k.group(1)), strip(ot.group(1))))
        for b in re.finditer(r'<div class="sc-sec"><h4>([\s\S]*?)</h4>([\s\S]*?)</div>', ov):
            W('**%s**\n' % strip(b.group(1)))
            for para in re.finditer(r'<p[^>]*>([\s\S]*?)</p>', b.group(2)):
                W('%s\n' % strip(para.group(1)))
    W('---\n')

# ── close ─────────────────────────────────────────────────────────────────
m = re.search(r'<footer class="sc-close">([\s\S]*?)</footer>', p)
if m:
    W('## Close\n')
    for c, lab in [('sc-close-line', 'Line'), ('sc-close-sub', 'Sub')]:
        x = re.search(r'<p class="%s">([\s\S]*?)</p>' % c, m.group(1))
        if x:
            W('**%s** — %s\n' % (lab, strip(x.group(1))))

text = '\n'.join(out) + '\n'
io.open(OUT, 'w', encoding='utf-8').write(text)
print('wrote %s — %d words, %d lines' % (OUT, len(text.split()), text.count('\n')))
