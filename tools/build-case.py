# -*- coding: utf-8 -*-
"""Build one case-study page from a Figma frame, in the same shell as home/work/invesco/.

    python3 tools/build-case.py <slug>

Reads   $FIGMA_CACHE/geo-<node>.json   (GET /v1/files/<key>/nodes?ids=<node>&geometry=paths)
        $FIGMA_CACHE/imagefills.json   (GET /v1/files/<key>/images)
Writes  home/work/<slug>/index.html and home/work/<slug>/img/*

The page config (node, title, links) lives in PAGES below, so a rebuild is one command."""
import hashlib, json, os, re, subprocess, sys, urllib.request
sys.path.insert(0, os.path.dirname(__file__))
import importlib.util
spec = importlib.util.spec_from_file_location('f2h', os.path.join(os.path.dirname(__file__), 'figma-to-html.py'))
f2h = importlib.util.module_from_spec(spec); spec.loader.exec_module(f2h)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.environ.get('FIGMA_CACHE', 'figma-out')
RESUME = 'https://drive.google.com/file/d/1t6k4iGsR7Wti509n0RL9tXD6VJzWaM1Q/view?usp=sharing'

# links by node name (first match wins); 'next' is the Next Project card
PAGES = {
    'kingdom': dict(node='241:20349', title='Kingdom OTT — building family bonds through streaming',
                    desc='Case study: Kingdom OTT, a family-first streaming app for U.S. viewers.',
                    next=('3 SPRE-min', '../shapoorji/', 'Shapoorji Pallonji Real Estate', None)),
    'shapoorji': dict(node='241:19898', title='Shapoorji Pallonji Real Estate — 680% lead growth',
                      desc="Case study: the Shapoorji Pallonji Real Estate website — 680% lead growth for India's top developer.",
                      # the frame's card points at Altin, which has no page; the home page's order puts ICICI next
                      next=('6 Altin-min', '../icici/', 'ICICI Ozone', '../../img/work-ozone.png')),
    'icici': dict(node='241:20128', title="ICICI Bank's Ozone — one-stop campus services",
                  desc="Case study: ICICI Bank's Ozone app — a one-stop solution for campus efficiency.",
                  next=('2 Kotak Bank-min', '../kotak/', 'Kotak Bank', None)),
}

FONTFILES = {('PP Eiko', 300): 'PPEiko-Regular', ('PP Eiko', 400): 'PPEiko-Regular', ('PP Eiko', 500): 'PPEiko-Medium',
             ('PP Eiko', 900): 'PPEiko-Black',
             ('PP Neue Montreal', 375): 'PPNeueMontreal-Regular', ('PP Neue Montreal', 400): 'PPNeueMontreal-Regular',
             ('PP Neue Montreal', 500): 'PPNeueMontreal-Medium', ('PP Neue Montreal', 700): 'PPNeueMontreal-Bold',
             ('PP Pangram Sans', 500): 'PPPangramSans-Medium', ('PP Pangram Sans', 600): 'PPPangramSans-Semibold',
             ('PP Pangram Sans', 700): 'PPPangramSans-Bold', ('PP Pangram Sans', 800): 'PPPangramSans-Extrabold',
             ('Inter', 400): 'Inter-Regular', ('Roboto', 500): 'Roboto-Medium', ('Gloock', 400): 'Gloock-Regular'}

CTA = ('<span class="cta" aria-hidden="true"><span class="cta-t">View case study</span><svg viewBox="0 0 20 20" aria-hidden="true">'
       '<path d="M6 14 L14 6 M7.5 6 H14 V12.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
       'stroke-linejoin="round"/></svg></span>')


def walk(n):
    yield n
    for k in n.get('children') or []:
        yield from walk(k)


def has_alpha(path):
    """True only if some pixel is actually see-through. Screenshots often carry an unused alpha
    channel; those go out as JPEG. sips writes 32-bit BGRA BMP, so alpha is every 4th byte."""
    out = subprocess.run(['sips', '-g', 'hasAlpha', path], capture_output=True, text=True).stdout
    if 'yes' not in out: return False
    bmp = os.path.join(CACHE, '_alpha.bmp')
    subprocess.run(['sips', '-s', 'format', 'bmp', path, '--out', bmp], capture_output=True, check=True)
    b = open(bmp, 'rb').read()
    off = int.from_bytes(b[10:14], 'little'); bpp = int.from_bytes(b[28:30], 'little')
    return bpp != 32 or min(b[off + 3::4]) < 250


def dims(path):
    out = subprocess.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', path], capture_output=True, text=True).stdout
    return int(re.search(r'pixelWidth: (\d+)', out).group(1)), int(re.search(r'pixelHeight: (\d+)', out).group(1))


def main(slug):
    cfg = PAGES[slug]
    out_dir = os.path.join(ROOT, 'home', 'work', slug)
    img_dir = os.path.join(out_dir, 'img'); os.makedirs(img_dir, exist_ok=True)
    raw_dir = os.path.join(CACHE, 'raw'); os.makedirs(raw_dir, exist_ok=True)
    geo = json.load(open(os.path.join(CACHE, 'geo-%s.json' % cfg['node'].replace(':', '-'))))
    frame = list(geo['nodes'].values())[0]['document']
    fills = json.load(open(os.path.join(CACHE, 'imagefills.json')))['meta']['images']
    W, H = round(frame['absoluteBoundingBox']['width']), round(frame['absoluteBoundingBox']['height'])

    # images: download once, decide jpg/png by alpha
    refs = {f['imageRef'] for n in walk(frame) if n.get('visible', True) is not False
            for f in n.get('fills') or [] if f['type'] == 'IMAGE' and f.get('imageRef')}
    imgmap, rawpath = {}, {}
    for ref in sorted(refs):
        raw = os.path.join(raw_dir, ref)
        if not os.path.exists(raw):
            urllib.request.urlretrieve(fills[ref], raw)
        ext = 'png' if has_alpha(raw) else 'jpg'
        name = '%s.%s' % (hashlib.sha1(ref.encode()).hexdigest()[:10], ext)
        imgmap[ref] = 'img/' + name; rawpath[ref] = (raw, name, ext)

    links, warns = {}, []
    conv = f2h.Conv(imgmap, links, warns.append)
    nx_name, nx_href, nx_label, nx_img = cfg['next']
    conv.prepare(frame)
    nx_done = False
    for n in walk(frame):
        nm = n['name']
        if nm == 'Component 22':
            links.setdefault(n['id'], '../../#contact')
        elif n['type'] == 'FRAME' and any(k.get('characters') == 'Back' for k in n.get('children') or []):
            links[n['id']] = '../../#work'; links[n['id'] + ':label'] = 'Back to all work'
        elif nm == 'Resume' and n['type'] == 'INSTANCE':
            pass                                    # its text node carries the Drive hyperlink
        elif nm == nx_name and not nx_done:          # the card frame and its art can share a name; link the outer one
            links[n['id']] = nx_href; nx_done = True
            links[n['id'] + ':label'] = 'Next project: %s — view case study' % nx_label
            conv.extra_cls[n['id']] = 'nx'
            conv.extra_html[n['id']] = CTA
            if nx_img:                               # swap the card art for the linked project's
                n['children'] = []; n['fills'] = [{'type': 'IMAGE', 'imageRef': '_next', 'scaleMode': 'FILL'}]
                imgmap['_next'] = nx_img
    node = conv.node                                 # Conv already appends extra_html after the children

    hdr = [c for c in frame['children'] if c['name'] == 'Header' and c.get('visible', True) is not False][0]
    body = ''.join(node(c, frame) for c in frame['children'] if c is not hdr)
    hdr_html = node(hdr, frame)
    # images: resize to 2x the largest box they fill, never upscale
    for ref, (raw, name, ext) in rawpath.items():
        if ref not in conv.used_imgs: continue           # e.g. the replaced next-card art
        need = conv.used_imgs.get(ref, [0, 0])
        ow, oh = dims(raw)
        s = min(1.0, max(2 * need[0] / ow if ow else 1, 2 * need[1] / oh if oh else 1))
        dst = os.path.join(img_dir, name)
        cmd = ['sips', '-s', 'format', 'jpeg' if ext == 'jpg' else 'png']
        if ext == 'jpg': cmd += ['-s', 'formatOptions', '82']
        if s < 0.98: cmd += ['--resampleWidth', str(max(1, round(ow * s)))]
        subprocess.run(cmd + [raw, '--out', dst], capture_output=True, check=True)

    bg = f2h.rgba(frame['fills'][0]['color']) if frame.get('fills') else '#fff'
    faces = []
    for fam, wt, it in sorted(conv.fonts, key=lambda x: (str(x[0]), x[1])):
        f = FONTFILES.get((fam, wt))
        if f: faces.append('@font-face{font-family:"%s";src:url("../../fonts/%s.woff2") format("woff2");font-weight:%s;font-display:swap}' % (fam, f, wt))
        else: warns.append('no font file for %s %s — system fallback' % (fam, wt))

    shell = open(os.path.join(ROOT, 'home', 'work', 'invesco', 'index.html')).read()
    css = shell[shell.index('*{box-sizing'):shell.index('</style>')]
    css = re.sub(r'\.canvas\{position:relative;width:1440px;height:\d+px;margin:0 auto;background:[^;]+;',
                 '.canvas{position:relative;width:1440px;height:%dpx;margin:0 auto;background:%s;' % (H, bg), css)
    # a blank line inside a Figma list is spacing, not an empty bullet
    css += '.t .ul li:empty{list-style:none;height:0;margin-bottom:4px}\n'
    css = css.replace('html,body{margin:0;background:#fff}', 'html,body{margin:0;background:%s}' % bg)
    script = shell[shell.index('<script>'):shell.index('</body>')].replace('H=19860', 'H=%d' % H)

    page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<title>%s · Dhanesh Shetye</title>\n<meta name="description" content="%s">\n<style>\n%s\n%s</style>\n</head>\n<body>\n'
            '<div class="hdr-wrap" id="hdr">%s</div>\n<main class="stage" id="stage"><div class="canvas" id="canvas">%s</div></main>\n%s</body>\n</html>\n') % (
        cfg['title'], cfg['desc'], '\n'.join(faces), css, hdr_html, body, script)
    open(os.path.join(out_dir, 'index.html'), 'w').write(page)
    for w in sorted(set(warns)): print('  warn:', w)
    print('%s: %d x %d, %d images, %d KB html' % (slug, W, H, len(rawpath), len(page) // 1024))


if __name__ == '__main__':
    main(sys.argv[1])
