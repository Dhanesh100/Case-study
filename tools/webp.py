# -*- coding: utf-8 -*-
"""Re-encode the portfolio's PNG/JPEG images as WebP, using headless Chrome's encoder (this Mac
has no cwebp; sips reads WebP but cannot write it). Idempotent.

    python3 tools/webp.py                 # every image under home/
    python3 tools/webp.py home/work/kingdom

A file is replaced only when the WebP is at least 10% smaller. Every reference to it in any
home/**/index.html is rewritten, then the original is deleted. Transparency is kept."""
import base64, glob, html as H, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
QUALITY = 0.82
TMP = os.environ.get('TMPDIR', '/tmp')


def encode(paths):
    page = os.path.join(TMP, '_webp.html')
    open(page, 'w').write('<pre id=o></pre><script>var L=%s,r={},n=L.length;L.forEach(function(p){var i=new Image();'
        'i.onload=function(){var c=document.createElement("canvas");c.width=i.naturalWidth;c.height=i.naturalHeight;'
        'c.getContext("2d").drawImage(i,0,0);r[p]=c.toDataURL("image/webp",%s);if(!--n)o.textContent=JSON.stringify(r)};'
        'i.onerror=function(){if(!--n)o.textContent=JSON.stringify(r)};i.src="file://"+p})</script>' % (json.dumps(paths), QUALITY))
    dom = subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--allow-file-access-from-files',
                          '--virtual-time-budget=60000', '--dump-dom', 'file://' + page], capture_output=True, text=True).stdout
    m = re.search(r'<pre id="o">(.*?)</pre>', dom, re.S)
    return json.loads(H.unescape(m.group(1))) if m and m.group(1) else {}


def main(base):
    imgs = sorted(p for p in glob.glob(os.path.join(base, '**', '*.*'), recursive=True)
                  if p.lower().endswith(('.png', '.jpg', '.jpeg')) and '/video/' not in p)
    pages = glob.glob(os.path.join(ROOT, 'home', '**', 'index.html'), recursive=True)
    texts = {p: open(p).read() for p in pages}
    before = after = 0
    for i in range(0, len(imgs), 25):
        for src, url in encode(imgs[i:i + 25]).items():
            if not url.startswith('data:image/webp'): continue
            data = base64.b64decode(url.split(',', 1)[1]); old = os.path.getsize(src)
            if len(data) > old * 0.9: continue
            dst = os.path.splitext(src)[0] + '.webp'
            open(dst, 'wb').write(data)
            for p in pages:                       # rewrite every reference, relative to that page
                rel = os.path.relpath(src, os.path.dirname(p))
                texts[p] = texts[p].replace(rel, os.path.splitext(rel)[0] + '.webp')
            os.remove(src); before += old; after += len(data)
    for p, t in texts.items():
        if open(p).read() != t: open(p, 'w').write(t)
    print('%s: %.1f MB -> %.1f MB' % (os.path.relpath(base, ROOT), before / 1e6, after / 1e6))


if __name__ == '__main__':
    main(os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(ROOT, 'home'))
