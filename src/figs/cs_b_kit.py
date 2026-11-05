"""Shared helpers for the 2015-16 and 2016-17 Computer Science modules (agent B).

* Gate / K-map drawing comes from the validated kit in class12/Computers/src
  (rev_fig, rev_lib, kmapsolve), whose figures draw in currentColor and are
  wrapped in <div><figure>; ``bare()`` strips that wrapper so a figure function
  returns a plain <svg> in fixed colours, as this site's kit expects.
  The decoder/encoder drawers in rev_fig are broken (unwired complements), so
  ``encoder()`` here is the corrected one from Sample-Papers-2027/computers_lib_a.
* ``jcode()`` / ``jout()`` read Java source and recorded run output from
  src/checks/java/<module>/, so the page shows only code that compiled and ran.
"""
import os, re, sys, html

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
CS_SRC = os.path.join(os.path.dirname(os.path.dirname(SRC)), "Computers", "src")
if CS_SRC not in sys.path:
    sys.path.append(CS_SRC)          # appended: never shadows this site's modules

import rev_fig as RF                 # noqa: E402
import rev_lib as RL                 # noqa: E402
import kmapsolve as KM               # noqa: E402

JAVA = os.path.join(SRC, "checks", "java")
P = "&prime;"


# ------------------------------------------------------------------ svg adapt
def bare(svg_html, scale=None):
    """rev_lib figure HTML -> a bare <svg> in black, tspans given real shifts."""
    m = re.search(r"<svg.*?</svg>", svg_html, re.S)
    s = m.group(0)
    s = s.replace('<tspan class="tsub">', '<tspan baseline-shift="sub" font-size="75%">')
    s = s.replace('<tspan class="tsup">', '<tspan baseline-shift="super" font-size="75%">')
    s = s.replace('<tspan class="tit">', '<tspan font-style="italic">')
    s = s.replace('<tspan class="tbf">', '<tspan font-weight="700">')
    s = s.replace('var(--surface, #fff)', '#fff')
    s = s.replace(' class=""', '')
    st = "color:#111;font-family:'Times New Roman',serif"
    if scale:
        w = float(re.search(r'viewBox="0 0 ([\d.]+)', s).group(1))
        st += ";max-width:%dpx" % int(w * scale)
    s = s.replace("<svg ", '<svg style="%s" ' % st, 1)
    return s


# ------------------------------------------------------------------ K-maps
GRAY = [0, 1, 3, 2]


def kmap(kind, cells, names, groups=None, letters=None):
    """4-variable K-map: Gray-code headings, cell numbers in the corner, the
    value in the middle, each group ringed (wrap-round groups drawn open at
    both edges).  For POS the headings are sum terms and the 0s are grouped.
    ``letters`` optionally labels each group ring (drawn beside it)."""
    a, b, c, d = names
    if kind == "sop":
        rh = [a + P + b + P, a + P + b, a + b, a + b + P]
        ch = [c + P + d + P, c + P + d, c + d, c + d + P]
        on, off = "1", "0"
    else:
        rh = [a + "+" + b, a + "+" + b + P, a + P + "+" + b + P, a + P + "+" + b]
        ch = [c + "+" + d, c + "+" + d + P, c + P + "+" + d + P, c + P + "+" + d]
        on, off = "0", "1"
    cw, chh, x0, y0 = 52.0, 40.0, 84.0, 40.0
    f = RL.Fig(x0 + 4 * cw + 18, y0 + 4 * chh + 16)
    f.line(x0 - 32, y0 - 28, x0, y0, 1.0)
    f.t(x0 - 4, y0 - 22, c + d, size=8.5, anchor="end")
    f.t(x0 - 30, y0 - 4, a + b, size=8.5, anchor="start")
    for j in range(4):
        f.t(x0 + cw * j + cw / 2, y0 - 7, ch[j], size=9)
    for i in range(4):
        f.t(x0 - 12, y0 + chh * i + chh / 2 + 3.5, rh[i], size=9, anchor="end")
    pos = {}
    for i in range(4):
        for j in range(4):
            n = GRAY[i] * 4 + GRAY[j]
            pos[n] = (i, j)
            x, y = x0 + cw * j, y0 + chh * i
            f.rect(x, y, cw, chh, sw=1.0)
            f.t(x + cw - 2.5, y + 8, str(n), size=6.5, anchor="end")
            f.t(x + cw / 2, y + chh / 2 + 4.5, on if n in cells else off, size=12,
                weight="700" if n in cells else None)

    def runs(v):
        if len(v) == 4:
            return [(0, 3, False, False)]
        if v == [0, 3]:
            return [(0, 0, True, False), (3, 3, False, True)]
        if len(v) == 3 or (len(v) == 2 and v[1] - v[0] != 1):
            raise ValueError("not a K-map group: %r" % v)
        return [(v[0], v[-1], False, False)]

    for gi, g in enumerate(groups or []):
        rows = sorted({pos[n][0] for n in g})
        cols = sorted({pos[n][1] for n in g})
        pad = 4.5 + 3.6 * (gi % 4)
        for r0, r1, ot, ob in runs(rows):
            for c0, c1, ol, orr in runs(cols):
                x1 = x0 + cw * c0 + pad - (pad + 5 if ol else 0)
                x2 = x0 + cw * (c1 + 1) - pad + (pad + 5 if orr else 0)
                y1 = y0 + chh * r0 + pad - (pad + 5 if ot else 0)
                y2 = y0 + chh * (r1 + 1) - pad + (pad + 5 if ob else 0)
                f.rect(x1, y1, x2 - x1, y2 - y1, r=9, sw=1.6,
                       dash="5 2.5" if gi % 2 else None)
    return bare(f.svg(), scale=1.9)


def kmap_groups(kind, cells, names):
    """kmapsolve's minimal cover: (expression, [(term, cells, size)])."""
    return KM.solve(kind, 4, cells, list(names))


def circuit(expr, kind, uni=None, out="F", scale=2.0):
    """Two-level gate diagram of a reduced expression (rev_fig.sop_circuit)."""
    if kind == "sop":
        terms = [t.strip() for t in expr.split("+")]
    else:
        terms = re.findall(r"\(([^)]*)\)", expr) or [expr]
    svg = RF.sop_circuit(terms, expr=None, pos=(kind == "pos"), uni=uni)
    if out != "F":
        svg = svg.replace('font-weight="700">F</text>', 'font-weight="700">%s</text>' % out)
    return bare(svg, scale=scale)


def encoder(inputs, outputs, wiring, scale=2.0):
    """Encoder as OR gates (corrected drawer from Sample-Papers-2027): every
    input is a vertical line; each output's OR gate is wired to its inputs."""
    xb = [18.0 + 15.0 * k for k in range(len(inputs))]
    x_g = xb[-1] + 30.0
    gap = 12.0
    hs = [RF.body_h(len(wiring[o])) for o in outputs]
    ys, y = [], 30.0
    for hh in hs:
        ys.append(y + hh / 2)
        y += hh + gap
    h = y + 4
    f = RL.Fig(x_g + RF.BW + 40, h)
    for k, lbl in enumerate(inputs):
        f.t(xb[k], 12, lbl, size=7.5, weight="700")
        f.line(xb[k], 16, xb[k], h - 6, 1.2)
    for o, yy in zip(outputs, ys):
        g = RF.gOR(f, x_g, yy, len(wiring[o]))
        for (px, py), s in zip(g["in"], wiring[o]):
            bxx = xb[inputs.index(s)]
            f.line(bxx, py, px, py, 1.2)
            RF.dot(f, bxx, py)
        f.t(g["out"][0] + 3, yy + 3.2, o, size=8.5, anchor="start", weight="700")
    return bare(f.svg(), scale=scale)


def tree(t, scale=2.2):
    return bare(RL.tree(t, r=11, dx=32, dy=42), scale=scale)


# ------------------------------------------------------------------ Java
def _read(module, fname):
    return open(os.path.join(JAVA, module, fname)).read()


def jcode(module, fname):
    """The ANSWER regions of a tested Java file, HTML-escaped, in a code block."""
    s = _read(module, fname)
    parts = re.findall(r"// BEGIN ANSWER\n(.*?)// END ANSWER\n", s, re.S)
    if not parts:
        raise ValueError("no ANSWER region in %s/%s" % (module, fname))
    src = "\n".join(p.rstrip("\n") for p in parts)
    # de-indent a method-only region
    lines = src.split("\n")
    ind = min(len(l) - len(l.lstrip()) for l in lines if l.strip())
    src = "\n".join(l[ind:] for l in lines)
    return '<pre class="code">%s</pre>' % html.escape(src, quote=False)


def jout(module, name):
    """Recorded run: input shown, then the program's output (written by the check)."""
    d = os.path.join(JAVA, module)
    inp = open(os.path.join(d, name + ".in")).read() if os.path.exists(os.path.join(d, name + ".in")) else ""
    out = open(os.path.join(d, name + ".out")).read()
    s = ""
    if inp.strip():
        s += '<p><b>Input</b></p><pre class="code">%s</pre>' % html.escape(inp.rstrip("\n"), quote=False)
    s += '<p><b>Output</b></p><pre class="code">%s</pre>' % html.escape(out.rstrip("\n"), quote=False)
    return s


def tbl(header, rows):
    h = "".join("<th>%s</th>" % x for x in header)
    b = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows)
    return '<div class="tbl"><table><tr>%s</tr>%s</table></div>' % (h, b)
