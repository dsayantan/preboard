"""Tiny SVG helper shared by all figure modules.

    from svg import Fig
    def fig_example():
        f = Fig(320, 200, "fig_example")          # width, height in user units; uid = unique prefix
        f.line(20, 100, 300, 100)                  # stroke defaults: black, 1.6
        f.arrow(40, 150, 140, 150, color="#c0392b")
        f.text(150, 40, "E", italic=True, size=15) # plain text only; use sub="0" for subscripts
        f.circle(160, 100, 30, fill="none")
        f.path("M 10 10 Q 50 50 90 10", fill="none")
        return f.svg()
Arrow markers are created per figure with ids prefixed by uid, so ids never clash on a page.
"""
from html import escape

class Fig:
    def __init__(self, w, h, uid):
        self.w, self.h, self.uid, self.el, self.cols = w, h, uid, [], set()
    def _mk(self, color):
        self.cols.add(color)
        return f"{self.uid}-ah-{color.strip('#')}"
    def line(self, x1, y1, x2, y2, color="#111", w=1.6, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.el.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"{d}/>')
    def arrow(self, x1, y1, x2, y2, color="#111", w=1.6, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.el.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"{d} marker-end="url(#{self._mk(color)})"/>')
    def path(self, d, color="#111", w=1.6, fill="none", arrow=False, dash=None):
        m = f' marker-end="url(#{self._mk(color)})"' if arrow else ""
        ds = f' stroke-dasharray="{dash}"' if dash else ""
        self.el.append(f'<path d="{d}" stroke="{color}" stroke-width="{w}" fill="{fill}"{m}{ds}/>')
    def circle(self, cx, cy, r, color="#111", w=1.6, fill="none"):
        self.el.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke="{color}" stroke-width="{w}" fill="{fill}"/>')
    def rect(self, x, y, w_, h_, color="#111", w=1.6, fill="none", rx=0):
        self.el.append(f'<rect x="{x}" y="{y}" width="{w_}" height="{h_}" rx="{rx}" stroke="{color}" stroke-width="{w}" fill="{fill}"/>')
    def text(self, x, y, s, size=14, italic=False, bold=False, anchor="middle", color="#111", sub=None, sup=None):
        st = (' font-style="italic"' if italic else "") + (' font-weight="bold"' if bold else "")
        t = escape(s)
        if sub: t += f'<tspan baseline-shift="sub" font-size="{size*0.72:.1f}">{escape(sub)}</tspan>'
        if sup: t += f'<tspan baseline-shift="super" font-size="{size*0.72:.1f}">{escape(sup)}</tspan>'
        self.el.append(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{color}" '
                       f'font-family="Times New Roman,serif"{st}>{t}</text>')
    def raw(self, s):
        self.el.append(s)
    def svg(self):
        defs = "".join(f'<marker id="{self.uid}-ah-{c.strip("#")}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
                       f'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
                       for c in sorted(self.cols))
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" role="img">'
                f'<defs>{defs}</defs>{"".join(self.el)}</svg>')
