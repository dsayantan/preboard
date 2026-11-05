"""Shared drawing helpers for the Computer Science pre-board papers 2013-14 and 2014-15
(agent A).  Not a figure module itself: the fig_* functions live in
computers_2013_14_figs.py and computers_2014_15_figs.py.

The gate kit (gAND/gOR/gNOT, wire, dot) and the tree / linked-list drawers are the
validated ones in class12/Computers/src (rev_fig.py, rev_lib.py), drawn in
currentColor; `clean()` turns their output into a bare, fixed-colour <svg> for this
site.  Their decoder_gates()/encoder() are known to be broken and are NOT used here.

`two_level()` draws an AND-OR / OR-AND / NAND-NAND circuit from a netlist that
`two_level_eval()` also simulates, so the check script can prove the drawn circuit
computes the intended function over every input row.
"""
import os
import re
import sys

_CS = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "..", "..", "Computers", "src")
_CS = os.path.normpath(_CS)
if _CS not in sys.path:
    sys.path.append(_CS)

import rev_fig as RF   # noqa: E402
import rev_lib as RL   # noqa: E402

P = "&prime;"
INK = "#111"


def clean(html, maxw=None, extra=0):
    """rev_lib/rev_fig output (div > figure > svg) -> bare <svg> in fixed colours."""
    m = re.search(r"<svg\b.*?</svg>", html, re.S)
    s = m.group(0)
    s = s.replace('<tspan class="tsub">', '<tspan baseline-shift="sub" font-size="75%">')
    s = s.replace('<tspan class="tsup">', '<tspan baseline-shift="super" font-size="75%">')
    s = s.replace('<tspan class="tit">', '<tspan font-style="italic">')
    s = s.replace('<tspan class="tbf">', '<tspan font-weight="700">')
    s = s.replace("var(--surface, #fff)", "#fff").replace("currentColor", INK)
    s = s.replace(' class=""', "")
    s = s.replace("&prime;", "′").replace("&middot;", "·").replace("&oplus;", "⊕")
    s = s.replace("&rarr;", "→").replace("&nbsp;", " ")
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', s)
    w = float(vb.group(1))
    if extra:
        s = s.replace(vb.group(0), 'viewBox="0 0 %g %s"' % (w + extra, vb.group(2)), 1)
        w += extra
    mw = maxw if maxw else min(520, w * 2.3)
    s = s.replace("<svg ", '<svg style="max-width:%dpx" font-family="Times New Roman,serif" ' % mw, 1)
    return s


def lbl(f, x, y, s, size=9, anchor="middle", weight="700"):
    f.t(x, y, s, size=size, anchor=anchor, weight=weight)


# ---------------------------------------------------------------- K-maps
GRAY2 = [0, 1, 3, 2]


def kmap(names, kind, cells, groups=(), maxw=None):
    """K-map (3 or 4 variables) in Gray-code order.

    kind 'sop': `cells` are the minterms (1s); 'pos': the maxterms (0s).
    Rows are the first half of the variables, columns the second half
    (3 variables: A | BC).  Each group (a list of cell numbers) is ringed;
    a group that wraps an edge is drawn as open-ended pieces at both edges.
    """
    n = len(names)
    rv, cv = (names[:1], names[1:]) if n == 3 else (names[:2], names[2:])
    rcodes = [0, 1] if len(rv) == 1 else GRAY2
    ccodes = GRAY2

    def head(vs, code, pos):
        bits = [(code >> (len(vs) - 1 - k)) & 1 for k in range(len(vs))]
        if not pos:
            return "".join(v + ("" if b else P) for v, b in zip(vs, bits))
        return "+".join(v + (P if b else "") for v, b in zip(vs, bits))

    pos = kind == "pos"
    on, off = ("0", "1") if pos else ("1", "0")
    cw, ch, x0, y0 = 54.0, 40.0, 76.0, 44.0
    nr, nc = len(rcodes), 4
    f = RL.Fig(x0 + nc * cw + 14, y0 + nr * ch + 14)
    f.line(x0 - 34, y0 - 30, x0, y0, 1.0)
    f.t(x0 - 4, y0 - 22, "".join(cv) if not pos else "+".join(cv), size=9, anchor="end")
    f.t(x0 - 32, y0 - 4, "".join(rv) if not pos else "+".join(rv), size=9, anchor="start")
    for j, c in enumerate(ccodes):
        f.t(x0 + cw * j + cw / 2, y0 - 10, head(cv, c, pos), size=9.5)
    for i, r in enumerate(rcodes):
        f.t(x0 - 12, y0 + ch * i + ch / 2 + 3.5, head(rv, r, pos), size=9.5, anchor="end")
    where = {}
    idx = []          # cell numbers: drawn last, on a white patch, so no ring hides them
    for i, r in enumerate(rcodes):
        for j, c in enumerate(ccodes):
            num = (r << len(cv)) | c
            where[num] = (i, j)
            x, y = x0 + cw * j, y0 + ch * i
            f.rect(x, y, cw, ch, sw=1.0)
            idx.append((x + cw - 3, y + 8, str(num)))
            f.t(x + cw / 2, y + ch / 2 + 5, on if num in cells else off, size=13,
                weight="700" if num in cells else None)

    def runs(v, total):
        if len(v) == total:
            return [(0, total - 1, False, False)]
        if total == 4 and v == [0, 3]:
            return [(0, 0, True, False), (3, 3, False, True)]
        if v != list(range(v[0], v[-1] + 1)):
            raise ValueError("not a rectangle: %r" % v)
        return [(v[0], v[-1], False, False)]

    for gi, g in enumerate(groups):
        for c in g:
            assert c in cells, ("group cell %d is not a %s" % (c, on))
        rows = sorted({where[c][0] for c in g})
        cols = sorted({where[c][1] for c in g})
        assert len(rows) * len(cols) == len(g), "group %r is not a rectangle" % (g,)
        pad = 6.0 + 3.0 * (gi % 3)
        for r0, r1, ot, ob in runs(rows, nr):
            for c0, c1, ol, orr in runs(cols, nc):
                x1 = x0 + cw * c0 + pad - (pad + 6 if ol else 0)
                x2 = x0 + cw * (c1 + 1) - pad + (pad + 6 if orr else 0)
                y1 = y0 + ch * r0 + pad - (pad + 6 if ot else 0)
                y2 = y0 + ch * (r1 + 1) - pad + (pad + 6 if ob else 0)
                f.rect(x1, y1, x2 - x1, y2 - y1, r=9, sw=1.7,
                       dash="5 2.5" if gi % 2 else None)
    for tx, ty, s in idx:
        f.rect(tx - 4.2 * len(s) - 0.8, ty - 6.2, 4.2 * len(s) + 1.6, 7.6, fill="#fff", sw=0)
        f.t(tx, ty, s, size=7, anchor="end")
    return clean(f.svg(), maxw or 380)


# ------------------------------------------------------- two-level circuits
def parse_term(t):
    """"AB'C" -> [('A',0),('B',1),('C',0)]  (1 = complemented)."""
    t = t.replace("&prime;", "'").replace("′", "'").replace("+", "").replace(" ", "")
    out, i = [], 0
    while i < len(t):
        v = t[i]
        i += 1
        neg = 0
        if i < len(t) and t[i] == "'":
            neg, i = 1, i + 1
        out.append((v, neg))
    return out


def two_level_eval(terms, kind, uni, env):
    """Simulate the netlist two_level() draws.  env: name -> 0/1."""
    lits = [parse_term(t) for t in terms]

    def lit(v, neg):
        return env[v] ^ neg

    if uni == "nand":
        lvl1 = []
        for L in lits:
            if len(L) == 1:      # a lone literal enters the output NAND complemented
                v, neg = L[0]
                lvl1.append(1 - lit(v, neg))
            else:
                lvl1.append(1 - min(lit(v, n) for v, n in L))
        return 1 - min(lvl1)
    if kind == "sop":
        return max(min(lit(v, n) for v, n in L) for L in lits)
    return min(max(lit(v, n) for v, n in L) for L in lits)


def two_level(terms, kind, names, uni=None, comp="avail", out="F", expr=None, maxw=None):
    """Draw the two-level circuit for `terms`.

    kind  'sop' (AND then OR) or 'pos' (OR then AND); uni='nand' for NAND-NAND (sop).
    comp  'avail' : every literal needed is a labelled input bus (variables and their
                    complements available as inputs, as the question allows);
          'not'   : true buses only, complements made by NOT gates;
          'nand'  : complements made by NAND gates with their inputs tied.
    """
    lits = [parse_term(t) for t in terms]
    need = []                      # literals in bus order
    for v in names:
        for neg in (0, 1):
            if any((v, neg) in L for L in lits) or (uni == "nand" and any(
                    len(L) == 1 and L[0] == (v, 1 - neg) for L in lits)):
                need.append((v, neg))
    # for NAND-NAND a lone literal x is fed to the output gate as x'
    feed1 = {}
    f_tmp = None
    nb = len(need)
    widest = max(len(L) for L in lits)
    bh = RF.body_h(widest)
    pitch = max(bh + 12.0, 26.0)
    gate_l1 = "NAND" if uni == "nand" else ("AND" if kind == "sop" else "OR")
    gate_l2 = "NAND" if uni == "nand" else ("OR" if kind == "sop" else "AND")

    if comp == "avail":
        bus_x = {lv: 18.0 + 14.0 * k for k, lv in enumerate(need)}
        head = 26.0
        x_g1 = 18.0 + 14.0 * nb + 22.0
    else:
        trues = [v for v in names if any(lv[0] == v for lv in need)]
        compl = [v for v in trues if (v, 1) in need]
        bus_x = {}
        for k, v in enumerate(trues):
            bus_x[(v, 0)] = 18.0 + 12.0 * k
        xinv = 18.0 + 12.0 * len(trues) + 14.0
        for k, v in enumerate(compl):
            bus_x[(v, 1)] = xinv + (40.0 if comp == "nand" else 28.0) + 12.0 * k
        head = 30.0 + 22.0 * len(compl)
        x_g1 = max(bus_x.values()) + 26.0
    top = head + 8 + bh / 2
    rows = len(lits)
    x_g2 = x_g1 + RF.BW + 34.0 + 5.0 * rows
    h = top + (rows - 1) * pitch + bh / 2 + (30 if expr else 14)
    h = max(h, top + RF.body_h(rows) / 2 + 20)
    w = x_g2 + RF.BW + RF.body_h(rows) / 2 + 70.0
    f = RL.Fig(w, h)
    bot = h - (24 if expr else 8)

    # buses
    if comp == "avail":
        for (v, neg), x in bus_x.items():
            lbl(f, x, 12, v + (P if neg else ""), size=9)
            f.line(x, 16, x, bot, 1.2)
    else:
        for v in trues:
            x = bus_x[(v, 0)]
            lbl(f, x, 12, v, size=9.5)
            f.line(x, 16, x, bot, 1.2)
        for k, v in enumerate(compl):
            y = 30.0 + 22.0 * k
            xt = bus_x[(v, 0)]
            if comp == "nand":
                g = RF.gAND(f, xinv + 8, y, 2, inv=True, lead=5.0)
                xs = g["in"][0][0] - 4
                f.line(xt, y, xs, y, 1.2)
                f.line(xs, g["in"][0][1], xs, g["in"][1][1], 1.2)
                for px, py in g["in"]:
                    f.line(xs, py, px, py, 1.2)
                RF.dot(f, xs, y)
            else:
                g = RF.gNOT(f, xinv + 6, y, lead=5.0)
                f.line(xt, y, g["in"][0][0], y, 1.2)
            RF.dot(f, xt, y)
            xc = bus_x[(v, 1)]
            f.line(g["out"][0], y, xc, y, 1.2)
            f.line(xc, y, xc, bot, 1.2)
            f.t(xc + 2.5, y - 3.5, v + P, size=8, anchor="start")

    # first level
    outs = []
    for i, L in enumerate(lits):
        y = top + i * pitch
        if len(L) == 1:
            v, neg = L[0]
            src = (v, 1 - neg) if uni == "nand" else (v, neg)
            x = bus_x[src]
            o = (x_g1 + RF.BW + 10.0, y)
            f.line(x, y, o[0], y, 1.2)
            RF.dot(f, x, y)
            outs.append(o)
            continue
        g = RF.gate(f, gate_l1, x_g1, y, len(L))
        for (px, py), lv in zip(g["in"], L):
            x = bus_x[lv]
            f.line(x, py, px, py, 1.2)
            RF.dot(f, x, py)
        outs.append(g["out"])
    ymid = top + (rows - 1) * pitch / 2
    g2 = RF.gate(f, gate_l2, x_g2, ymid, rows)
    lanes = sorted(range(rows), key=lambda i: -abs(i - (rows - 1) / 2.0))
    for i, (o, pin) in enumerate(zip(outs, g2["in"])):
        RF.wire(f, o, pin, mid=x_g2 - 9.0 - 5.0 * lanes.index(i))
    f.t(g2["out"][0] + 3, g2["out"][1] + 3.5, out, size=10, anchor="start", weight="700")
    if expr:
        f.t(w / 2, h - 8, expr, size=9.5)
    return clean(f.svg(), maxw)


def tree(t, maxw=None):
    return clean(RL.tree(t, r=11, dx=32, dy=40), maxw)


def llist(vals, head="ptr_start", maxw=None):
    """Singly linked list: [item | ptr] boxes, each ptr arrow to the next node, last
    ptr = null; a labelled external reference points at the first node."""
    bw, bh, gap = 44, 22, 22
    hx = 8 + len(head) * 5.2
    x0 = hx + 22
    n = len(vals)
    w = x0 + n * (bw + gap) + 30
    f = RL.Fig(w, 50)
    y = 25
    f.t(6, y + 3.5, head, size=9, anchor="start", weight="700")
    f.arrow(hx, y, x0 - 2, y, 1.2)
    for i, v in enumerate(vals):
        x = x0 + i * (bw + gap)
        f.rect(x, y - bh / 2, bw, bh, r=2.5, fill="#fff")
        f.line(x + bw * 0.6, y - bh / 2, x + bw * 0.6, y + bh / 2, 1.1)
        f.t(x + bw * 0.3, y + 3.5, str(v), size=9.5, weight="700")
        f.circ(x + bw * 0.8, y, 1.9, fill="currentColor", sw=0)
        if i < n - 1:
            f.arrow(x + bw * 0.8, y, x + bw + gap - 2, y, 1.2)
        else:
            f.arrow(x + bw * 0.8, y, x + bw + 10, y, 1.2)
            f.t(x + bw + 13, y + 3.5, "null", size=8.5, anchor="start")
    f.t(x0 + bw * 0.3, y + bh / 2 + 11, "item", size=7.5)
    f.t(x0 + bw * 0.8, y + bh / 2 + 11, "ptr", size=7.5)
    return clean(f.svg(), maxw)
