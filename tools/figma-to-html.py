# -*- coding: utf-8 -*-
"""Figma frame (REST JSON with geometry=paths) -> absolutely positioned HTML.
Handles: SOLID/IMAGE/GRADIENT_LINEAR fills (bottom-first stacking), FILL/FIT/STRETCH(crop)/TILE
images, clipsContent, corner radii, DROP/INNER shadows, LAYER/BACKGROUND blur, strokes by align,
opacity, text with style runs/case/decoration/links, vectors as inline SVG, one-level masks."""
import json, math, re, sys, html as H

def q(s): return s.replace('"', "'")

def r2(v): return ('%.2f' % v).rstrip('0').rstrip('.') if abs(v - round(v)) > 1e-3 else str(int(round(v)))
def rgba(c, op=1.0):
    a = c.get('a', 1) * op
    return 'rgba(%d,%d,%d,%s)' % (round(c['r']*255), round(c['g']*255), round(c['b']*255), r2(round(a, 3)) if a < 0.999 else '1')

FONT = {'PP Neue Montreal TT': 'PP Neue Montreal', 'PP Neue Montreal': 'PP Neue Montreal',
        'PP Pangram Sans': 'PP Pangram Sans', 'PP Eiko': 'PP Eiko'}
FALLBACK = {'PP Eiko': 'Didot, Georgia, serif', 'Gloock': 'Georgia, serif', 'Helvetica Neue': 'Helvetica, Arial, sans-serif',
            'Invesco Editor': 'Georgia, "Times New Roman", serif',
            'SF Pro Display': '-apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif',
            'SF Compact Text': '-apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif',
            'Graphik': '-apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif'}
def ffam(f):
    fam = FONT.get(f, f)
    return '"%s", %s' % (fam, FALLBACK.get(fam, '-apple-system, BlinkMacSystemFont, "Helvetica Neue", Arial, sans-serif'))

class Conv:
    def __init__(self, imgmap, links, warn, videos=None):
        self.imgmap = imgmap; self.links = links; self.warn = warn; self.videos = videos or {}; self.extra_cls = {}; self.extra_html = {}
        self.uid = 0; self.fonts = set(); self.used_imgs = {}

    # ── paints ──────────────────────────────────────────────────────────
    def gradient(self, f, w, h):
        hp = f.get('gradientHandlePositions') or []
        stops = f.get('gradientStops') or []
        op = f.get('opacity', 1)
        if len(hp) < 2 or not stops: return None
        x0, y0, x1, y1 = hp[0]['x']*w, hp[0]['y']*h, hp[1]['x']*w, hp[1]['y']*h
        dx, dy = x1-x0, y1-y0
        if abs(dx) + abs(dy) < 1e-6: return None
        ang = math.degrees(math.atan2(dx, -dy)) % 360
        a = math.radians(ang)
        ux, uy = math.sin(a), -math.cos(a)
        L = abs(w*math.sin(a)) + abs(h*math.cos(a))
        cx, cy = w/2, h/2
        t0 = (x0-cx)*ux + (y0-cy)*uy; t1 = (x1-cx)*ux + (y1-cy)*uy
        parts = []
        for s in stops:
            t = t0 + s['position']*(t1-t0)
            parts.append('%s %s%%' % (rgba(s['color'], op), r2((t + L/2)/L*100)))
        return 'linear-gradient(%sdeg, %s)' % (r2(ang), ', '.join(parts))

    def image(self, f, w, h, node):
        ref = f.get('imageRef')
        if ref not in self.imgmap:
            self.warn('missing image %s on %s' % (ref, node.get('name'))); return None
        mode = f.get('scaleMode', 'FILL')
        src = self.imgmap[ref]
        need = self.used_imgs.setdefault(ref, [0, 0])
        if mode == 'STRETCH' and f.get('imageTransform'):
            (a, b, tx), (c, d, ty) = f['imageTransform']
            if abs(b) > 1e-3 or abs(c) > 1e-3: self.warn('rotated image crop on %s' % node.get('name'))
            a = a or 1; d = d or 1
            fw, fh = w/a, h/d
            need[0] = max(need[0], fw); need[1] = max(need[1], fh)
            return 'url("%s") %spx %spx / %spx %spx no-repeat' % (src, r2(-tx*fw), r2(-ty*fh), r2(fw), r2(fh))
        need[0] = max(need[0], w); need[1] = max(need[1], h)
        if mode == 'FIT':  return 'url("%s") center / contain no-repeat' % src
        if mode == 'TILE':
            sf = f.get('scalingFactor', 1)
            return 'url("%s") 0 0 / %s%% repeat' % (src, r2(sf*100))
        if mode == 'STRETCH': return 'url("%s") 0 0 / 100%% 100%% no-repeat' % src
        return 'url("%s") center / cover no-repeat' % src

    def background(self, node, w, h):
        layers = []
        for f in node.get('fills') or []:
            if f.get('visible', True) is False: continue
            t = f['type']
            if t == 'SOLID':
                col = rgba(f['color'], f.get('opacity', 1)); layers.append('linear-gradient(%s,%s)' % (col, col))
            elif t == 'GRADIENT_LINEAR':
                g = self.gradient(f, w, h)
                if g: layers.append(g)
            elif t == 'IMAGE':
                if f.get('opacity', 1) < 0.999:
                    vis = [g for g in node.get('fills') or [] if g.get('visible', True) is not False]
                    if len(vis) == 1 and not node.get('children'):
                        self._fill_op = f['opacity']      # sole fill, no children: element opacity is exact
                        i = self.image(f, w, h, node)
                        if i: layers.append(i)
                        continue
                    if f is vis[-1]:
                        # top fill: draw it as its own faded layer above the fills beneath
                        i = self.image(f, w, h, node)
                        if i: self._overlay = (i, f['opacity'])
                        continue
                    else:
                        self.warn('image fill opacity %.2f ignored on %s' % (f['opacity'], node.get('name')))
                i = self.image(f, w, h, node)
                if i: layers.append(i)
            else:
                self.warn('fill type %s on %s' % (t, node.get('name')))
        if not layers: return ''
        return ', '.join(reversed(layers))     # Figma: last fill on top; CSS: first layer on top

    # ── node ────────────────────────────────────────────────────────────
    def box(self, node, parent):
        b = node.get('absoluteBoundingBox') or {}
        pb = parent.get('absoluteBoundingBox') or {'x': 0, 'y': 0}
        return b.get('x', 0)-pb['x'], b.get('y', 0)-pb['y'], b.get('width', 0), b.get('height', 0)

    def effects(self, node, is_text=False, is_svg=False):
        shadows, filt, back = [], [], []
        for e in node.get('effects') or []:
            if e.get('visible', True) is False: continue
            t = e['type']; r = e.get('radius', 0)
            if t in ('DROP_SHADOW', 'INNER_SHADOW'):
                o = e.get('offset', {'x': 0, 'y': 0}); col = rgba(e['color'])
                if is_text or is_svg:
                    filt.append('drop-shadow(%spx %spx %spx %s)' % (r2(o['x']), r2(o['y']), r2(r/2), col))
                else:
                    shadows.append('%s%spx %spx %spx %spx %s' % ('inset ' if t == 'INNER_SHADOW' else '',
                                    r2(o['x']), r2(o['y']), r2(r), r2(e.get('spread', 0)), col))
            elif t == 'LAYER_BLUR': filt.append('blur(%spx)' % r2(r/2))
            elif t == 'BACKGROUND_BLUR': back.append('blur(%spx)' % r2(r/2))
        return shadows, filt, back

    def radius(self, node):
        if node['type'] == 'ELLIPSE': return '50%'
        rr = node.get('rectangleCornerRadii')
        if rr and any(rr): return ' '.join('%spx' % r2(v) for v in rr)
        cr = node.get('cornerRadius')
        return '%spx' % r2(cr) if cr else ''

    def strokes(self, node):
        out = {'shadow': [], 'outline': ''}
        st = [s for s in node.get('strokes') or [] if s.get('visible', True) is not False and s['type'] == 'SOLID']
        w = node.get('strokeWeight', 0)
        if not st or not w: return out
        col = rgba(st[0]['color'], st[0].get('opacity', 1))
        align = node.get('strokeAlign', 'INSIDE')
        isw = node.get('individualStrokeWeights')
        if isw:   # per-side, inside
            t, r, b, l = isw.get('top', 0), isw.get('right', 0), isw.get('bottom', 0), isw.get('left', 0)
            for (x, y, v) in ((0, t, t), (-r, 0, r), (0, -b, b), (l, 0, l)):
                if v: out['shadow'].append('inset %spx %spx 0 0 %s' % (r2(x), r2(y), col))
            return out
        if node.get('strokeDashes'): self.warn('dashed stroke drawn solid on %s' % node.get('name'))
        if align == 'INSIDE': out['shadow'].append('inset 0 0 0 %spx %s' % (r2(w), col))
        elif align == 'OUTSIDE': out['outline'] = 'outline:%spx solid %s;' % (r2(w), col)
        else: out['outline'] = 'outline:%spx solid %s;outline-offset:-%spx;' % (r2(w), col, r2(w/2))
        return out

    def svg(self, node, x, y, w, h):
        paths = []
        fills = [f for f in node.get('fills') or [] if f.get('visible', True) is not False]
        fill_col = rgba(fills[-1]['color'], fills[-1].get('opacity', 1)) if fills and fills[-1]['type'] == 'SOLID' else None
        if fills and fills[-1]['type'] == 'IMAGE':
            f = fills[-1]; self.uid += 1; cid = 'vc%d' % self.uid
            bgv = self.image(f, w, h, node)   # registers the image size need
            src = self.imgmap.get(f.get('imageRef'), '')
            if f.get('scaleMode') == 'STRETCH' and f.get('imageTransform'):
                (a, b, tx), (c2, d, ty) = f['imageTransform']; a = a or 1; d = d or 1
                fw, fh = w/a, h/d
                img = '<image href="%s" x="%s" y="%s" width="%s" height="%s" preserveAspectRatio="none" clip-path="url(#%s)"/>' % (src, r2(-tx*fw), r2(-ty*fh), r2(fw), r2(fh), cid)
            else:
                pa = 'xMidYMid meet' if f.get('scaleMode') == 'FIT' else 'xMidYMid slice'
                img = '<image href="%s" x="0" y="0" width="%s" height="%s" preserveAspectRatio="%s" clip-path="url(#%s)"/>' % (src, r2(w), r2(h), pa, cid)
            cp = ''.join('<path d="%s" fill-rule="%s"/>' % (g['path'], 'evenodd' if g.get('windingRule') == 'EVENODD' else 'nonzero') for g in node.get('fillGeometry') or [])
            paths.append('<defs><clipPath id="%s">%s</clipPath></defs>%s' % (cid, cp, img))
        elif fills and fills[-1]['type'] == 'GRADIENT_LINEAR':
            f = fills[-1]; self.uid += 1; gid = 'vg%d' % self.uid
            hp = f.get('gradientHandlePositions') or [{'x': 0, 'y': 0}, {'x': 1, 'y': 0}]
            st = ''.join('<stop offset="%s" stop-color="rgb(%d,%d,%d)" stop-opacity="%s"/>' % (
                r2(s['position']), round(s['color']['r']*255), round(s['color']['g']*255), round(s['color']['b']*255),
                r2(s['color'].get('a', 1) * f.get('opacity', 1))) for s in f.get('gradientStops') or [])
            paths.append('<defs><linearGradient id="%s" gradientUnits="objectBoundingBox" x1="%s" y1="%s" x2="%s" y2="%s">%s</linearGradient></defs>' % (
                gid, r2(hp[0]['x']), r2(hp[0]['y']), r2(hp[1]['x']), r2(hp[1]['y']), st))
            fill_col = 'url(#%s)' % gid
        elif fills and not fill_col: self.warn('non-solid vector fill on %s' % node.get('name'))
        for g in node.get('fillGeometry') or []:
            if fill_col: paths.append('<path d="%s" fill="%s" fill-rule="%s"/>' % (g['path'], fill_col, 'evenodd' if g.get('windingRule') == 'EVENODD' else 'nonzero'))
        st = [s for s in node.get('strokes') or [] if s.get('visible', True) is not False and s['type'] == 'SOLID']
        if st:
            sc = rgba(st[0]['color'], st[0].get('opacity', 1))
            for g in node.get('strokeGeometry') or []:
                paths.append('<path d="%s" fill="%s" fill-rule="%s"/>' % (g['path'], sc, 'evenodd' if g.get('windingRule') == 'EVENODD' else 'nonzero'))
        if not paths: return ''
        _, filt, _ = self.effects(node, is_svg=True)
        style = 'left:%spx;top:%spx;width:%spx;height:%spx;' % (r2(x), r2(y), r2(max(w, 0.01)), r2(max(h, 0.01)))
        if node.get('opacity', 1) < 0.999: style += 'opacity:%s;' % r2(node['opacity'])
        if filt: style += 'filter:%s;' % ' '.join(filt)
        return '<svg class="v" style="%s" viewBox="0 0 %s %s" preserveAspectRatio="none" aria-hidden="true" overflow="visible">%s</svg>' % (
            q(style), r2(max(w, 0.01)), r2(max(h, 0.01)), ''.join(paths))

    def text(self, node, x, y, w, h):
        s = node.get('style', {})
        chars = node.get('characters', '')
        ov = node.get('characterStyleOverrides') or []
        tbl = node.get('styleOverrideTable') or {}
        fam = s.get('fontFamily', 'PP Neue Montreal'); wt = s.get('fontWeight', 400)
        self.fonts.add((FONT.get(fam, fam), wt, s.get('italic', False)))
        fills = [f for f in node.get('fills') or [] if f.get('visible', True) is not False]
        col = rgba(fills[-1]['color'], fills[-1].get('opacity', 1)) if fills and fills[-1]['type'] == 'SOLID' else '#000'
        lh = s.get('lineHeightPx'); ls = s.get('letterSpacing', 0)
        auto = node.get('textAutoResize', 'NONE')
        css = ['left:%spx' % r2(x), 'top:%spx' % r2(y), 'width:%spx' % r2(w + (1 if auto == 'WIDTH_AND_HEIGHT' else 0)),
               'font-family:%s' % ffam(fam), 'font-weight:%s' % wt, 'font-size:%spx' % r2(s.get('fontSize', 16)),
               'color:%s' % col]
        if auto != 'WIDTH_AND_HEIGHT': css.append('height:%spx' % r2(h))
        if lh: css.append('line-height:%spx' % r2(lh))
        if ls: css.append('letter-spacing:%spx' % r2(ls))
        al = s.get('textAlignHorizontal', 'LEFT')
        if al != 'LEFT': css.append('text-align:%s' % {'CENTER': 'center', 'RIGHT': 'right', 'JUSTIFIED': 'justify'}[al])
        va = s.get('textAlignVertical', 'TOP')
        if va != 'TOP' and auto != 'WIDTH_AND_HEIGHT':
            css.append('display:flex;flex-direction:column;justify-content:%s' % {'CENTER': 'center', 'BOTTOM': 'flex-end'}[va])
        tc = s.get('textCase')
        if tc in ('UPPER', 'LOWER', 'TITLE'): css.append('text-transform:%s' % {'UPPER': 'uppercase', 'LOWER': 'lowercase', 'TITLE': 'capitalize'}[tc])
        td = s.get('textDecoration')
        if td in ('UNDERLINE', 'STRIKETHROUGH'): css.append('text-decoration:%s' % ('underline' if td == 'UNDERLINE' else 'line-through'))
        if s.get('italic'): css.append('font-style:italic')
        one_line = '\n' not in chars and lh and h <= lh * 1.5
        if auto == 'WIDTH_AND_HEIGHT' or one_line: css.append('white-space:nowrap')
        if node.get('opacity', 1) < 0.999: css.append('opacity:%s' % r2(node['opacity']))
        _, filt, _ = self.effects(node, is_text=True)
        if filt: css.append('filter:%s' % ' '.join(filt))
        lt = node.get('lineTypes') or []
        is_list = bool(lt) and any(t != 'NONE' for t in lt)
        def runs_in(a, b):
            out, cur, start = [], None, a
            for i in range(a, b + 1):
                k = (ov[i] if i < len(ov) else 0) if i < b else None
                if k != cur:
                    if cur is not None: out.append((cur, chars[start:i]))
                    cur, start = k, i
            return out
        def render(rs):
            return ''.join(self._seg(k, t, tbl, fam, wt) for k, t in rs)
        if is_list:
            lines, pos, items = chars.split('\n'), 0, []
            for ln in lines:
                items.append('<li>%s</li>' % render(runs_in(pos, pos + len(ln))))
                pos += len(ln) + 1
            ls_gap = s.get('listSpacing', 0)
            tagl = 'ol' if all(t == 'ORDERED' for t in lt) else 'ul'
            css.append('--li-gap:%spx' % r2(ls_gap))
            body = '<%s class="ul">%s</%s>' % (tagl, ''.join(items), tagl)
        else:
            body = render(runs_in(0, len(chars)))
        link = (s.get('hyperlink') or {}).get('url') or self.links.get(node['id'])
        tag = 'a' if link else 'div'
        attr = ' href="%s"' % H.escape(link) if link else ''
        if link and link.startswith('http'): attr += ' target="_blank" rel="noopener"'
        if any(x.startswith('display:flex') for x in css):
            body = '<span class="tv">%s</span>' % body   # one flex item, so runs stay inline
        return '<%s class="t"%s style="%s">%s</%s>' % (tag, attr, q(';'.join(css)), body, tag)

    def _seg(self, k, t, tbl, fam, wt):
            seg = H.escape(t).replace('\n', '<br>')
            st = tbl.get(str(k)) if k else None
            if st:
                rc = []
                if 'fontFamily' in st or 'fontWeight' in st:
                    f2 = st.get('fontFamily', fam); w2 = st.get('fontWeight', wt)
                    self.fonts.add((FONT.get(f2, f2), w2, st.get('italic', False)))
                    if 'fontFamily' in st: rc.append('font-family:%s' % ffam(f2))
                    rc.append('font-weight:%s' % w2)
                if 'fontSize' in st: rc.append('font-size:%spx' % r2(st['fontSize']))
                if st.get('fills'):
                    f0 = st['fills'][-1]
                    if f0['type'] == 'SOLID': rc.append('color:%s' % rgba(f0['color'], f0.get('opacity', 1)))
                if st.get('textDecoration') == 'UNDERLINE': rc.append('text-decoration:underline')
                if st.get('italic'): rc.append('font-style:italic')
                if 'letterSpacing' in st: rc.append('letter-spacing:%spx' % r2(st['letterSpacing']))
                link = (st.get('hyperlink') or {}).get('url')
                tag = 'a href="%s"' % H.escape(link) if link else 'span'
                seg = '<%s style="%s">%s</%s>' % (tag, q(';'.join(rc)), seg, tag.split()[0])
            return seg

    def node(self, node, parent, depth=0):
        if node.get('visible', True) is False: return ''
        t = node['type']
        x, y, w, h = self.box(node, parent)
        if t == 'TEXT': return self.text(node, x, y, w, h)
        if t in ('VECTOR', 'BOOLEAN_OPERATION', 'STAR', 'LINE', 'REGULAR_POLYGON'):
            return self.svg(node, x, y, w, h)
        css = ['left:%spx' % r2(x), 'top:%spx' % r2(y), 'width:%spx' % r2(w), 'height:%spx' % r2(h)]
        self._fill_op = None; self._overlay = None
        bg = self.background(node, w, h)
        if bg: css.append('background:%s' % bg)
        fop = self._fill_op
        rad = self.radius(node)
        if rad: css.append('border-radius:%s' % rad)
        od = node.get('overflowDirection') or 'NONE'
        scr = ''
        if od != 'NONE':
            b0 = node.get('absoluteBoundingBox') or {}
            ks = [k['absoluteBoundingBox'] for k in node.get('children') or [] if k.get('visible', True) is not False and k.get('absoluteBoundingBox')]
            over_x = ks and max(k['x'] + k['width'] for k in ks) - (b0['x'] + b0['width']) > 8
            over_y = ks and max(k['y'] + k['height'] for k in ks) - (b0['y'] + b0['height']) > 8
            if od in ('HORIZONTAL_SCROLLING', 'BOTH') and over_x: scr += ' sx'
            if od in ('VERTICAL_SCROLLING', 'BOTH') and over_y: scr += ' sy'
        if scr:
            css.append('overflow-x:%s;overflow-y:%s' % ('auto' if 'sx' in scr else 'hidden', 'auto' if 'sy' in scr else 'hidden'))
        elif node.get('clipsContent'): css.append('overflow:hidden')
        shadows, filt, back = self.effects(node)
        st = self.strokes(node)
        allsh = st['shadow'] + shadows
        if allsh: css.append('box-shadow:%s' % ', '.join(allsh))
        if st['outline']: css.append(st['outline'].rstrip(';'))
        if filt: css.append('filter:%s' % ' '.join(filt))
        if back: css.append('-webkit-backdrop-filter:%s;backdrop-filter:%s' % (' '.join(back), ' '.join(back)))
        op = node.get('opacity', 1) * (fop or 1)
        if op < 0.999: css.append('opacity:%s' % r2(op))
        kids = node.get('children') or []
        out = []
        if self._overlay:
            rad = self.radius(node)
            out.append('<div class="n" style="%s"></div>' % q('left:0;top:0;width:100%%;height:100%%;background:%s;opacity:%s%s' % (
                self._overlay[0], r2(self._overlay[1]), (';border-radius:' + rad) if rad else '')))
        vid = self.videos.get(node['id'])
        if vid:
            # Figma video fill: the API only exposes the first frame, which here is the empty
            # pre-load state. Play the real recording; poster is a populated frame.
            out.append('<video class="vid" muted playsinline poster="%s" data-src="%s" data-start="%s" aria-label="%s"></video>' % vid)
        i = 0
        while i < len(kids):
            k = kids[i]
            if k.get('isMask') and k.get('visible', True) is not False:
                # Figma: a mask clips the siblings above it. Approximate with its bounding box.
                mx, my, mw, mh = self.box(k, node)
                inner = ''.join(self.node(s, k, depth+1) for s in kids[i+1:])
                geo = k.get('fillGeometry') or []
                if geo:
                    clip = 'clip-path:path(%s);' % ('"%s"' % ' '.join(g['path'] for g in geo))
                else:
                    rr = self.radius(k)
                    clip = 'overflow:hidden;' + (('border-radius:%s;' % rr) if rr else '')
                    self.warn('mask on %s approximated by its bounds' % k.get('name'))
                out.append('<div class="n" style="left:%spx;top:%spx;width:%spx;height:%spx;%s">%s</div>' % (
                    r2(mx), r2(my), r2(mw), r2(mh), q(clip), inner))
                break
            out.append(self.node(k, node, depth+1)); i += 1
        link = self.links.get(node['id'])
        tag = 'a' if link else 'div'
        attr = ''
        if link:
            attr = ' href="%s"' % H.escape(link)
            if link.startswith('http'): attr += ' target="_blank" rel="noopener"'
            lab = self.links.get(node['id'] + ':label')
            if lab: attr += ' aria-label="%s"' % H.escape(lab)
        cls = 'n' + scr + (' lk' if link else '') + ((' ' + self.extra_cls[node['id']]) if node['id'] in self.extra_cls else '')
        if node['id'] in self.extra_html: out.append(self.extra_html[node['id']])
        return '<%s class="%s"%s style="%s">%s</%s>' % (tag, cls, attr, q(';'.join(css)), ''.join(out), tag)
