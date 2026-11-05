"""Figures for Computer Science pre-board 2024-25, Group 4 (computers_2024_25_g4)
and Paper 2 (computers_2024_25_p2).

Gate primitives, K-maps and trees come from cs_b_kit (which wraps the validated
Computers/src rev_fig / rev_lib / kmapsolve).  The gate-level decoder follows the
corrected drawer of Sample-Papers-2027/src/computers_lib_a.py (as in
computers_2025_26_figs): every complemented input has its own inverter and bus.
"""
from cs_b_kit import RF, RL, bare, kmap, circuit, tree, KM
from svg import Fig

# ---------------------------------------------------------------- Q3(a)  SOP
Q3A_ON = [5, 6, 7, 8, 9, 10, 11, 14, 15]
Q3A_EXPR, Q3A_GROUPS = KM.solve("sop", 4, Q3A_ON, list("ABCD"))     # A'BD + BC + AB'


def fig_q3a_kmap():
    return kmap("sop", Q3A_ON, "ABCD", [c for _, c, _ in Q3A_GROUPS])


def fig_q3a_circuit():
    return circuit(Q3A_EXPR, "sop")


# ---------------------------------------------------------------- Q3(b)  POS
Q3B_OFF = [0, 1, 2, 3, 5, 6, 8, 10]
Q3B_EXPR, Q3B_GROUPS = KM.solve("pos", 4, Q3B_OFF, list("ABCD"))    # (A+B)(B+D)(A+C+D')(A+C'+D)


def fig_q3b_kmap():
    return kmap("pos", Q3B_OFF, "ABCD", [c for _, c, _ in Q3B_GROUPS])


def fig_q3b_circuit():
    return circuit(Q3B_EXPR, "pos")


# ---------------------------------------------------------------- Q4(a) decoder
Q4_WORDS = ["0010", "0101", "0111", "1000", "1010", "1100", "1110", "1111"]
Q4_HEX = ["%X" % int(w, 2) for w in Q4_WORDS]


def fig_q4a_decoder():
    """True bus and complemented bus (own inverter) for each of A B C D; one
    4-input AND per word: a 1 bit takes the true line, a 0 bit the complement."""
    bits = [("%s = %s" % (w, h), w) for w, h in zip(Q4_WORDS, Q4_HEX)]
    nvar, names = 4, "ABCD"
    bh = RF.body_h(nvar)
    pitch = bh + 10.0
    xt = [16.0 + 10.0 * i for i in range(nvar)]
    xnot = xt[-1] + 18.0
    xc = [xnot + 30.0 + 12.0 * i for i in range(nvar)]
    ynot = [24.0 + 14.0 * i for i in range(nvar)]
    top = ynot[-1] + 14.0 + bh / 2
    x_g = xc[-1] + 26.0
    h = top + (len(bits) - 1) * pitch + bh / 2 + 10
    f = RL.Fig(x_g + RF.BW + 92, h)
    bot = h - 6
    for i, nm in enumerate(names):
        f.t(xt[i], 11, nm, size=8.5, weight="700")
        f.line(xt[i], 15, xt[i], bot, 1.2)
        g = RF.gNOT(f, xnot, ynot[i], lead=4.0)
        f.line(xt[i], ynot[i], g["in"][0][0], ynot[i], 1.2)
        RF.dot(f, xt[i], ynot[i])
        f.line(g["out"][0], ynot[i], xc[i], ynot[i], 1.2)
        f.line(xc[i], ynot[i], xc[i], bot, 1.2)
        f.t(xc[i] + 2.5, ynot[i] - 3, nm + "&prime;", size=7.5, anchor="start")
    for k, (lbl, pat) in enumerate(bits):
        y = top + k * pitch
        g = RF.gAND(f, x_g, y, nvar)
        for (px, py), i, bit in zip(g["in"], range(nvar), pat):
            bxx = xt[i] if bit == "1" else xc[i]
            f.line(bxx, py, px, py, 1.2)
            RF.dot(f, bxx, py)
        f.t(g["out"][0] + 3, y + 3.2, lbl, size=8, anchor="start", weight="600")
    return bare(f.svg(), scale=1.6)


# ---------------------------------------------------------------- Q4(c) XNOR
def fig_q4c_xnor():
    """The gate as printed: XNOR, inputs A, B, output Y."""
    return bare(RF.single("XNOR", ins=("A", "B"), out="Y"), scale=2.0)


def fig_q4c_xnor_gates():
    """Y = A'B' + AB from basic gates (complements available)."""
    return circuit("A'B' + AB", "sop", out="Y", scale=2.0)


# ---------------------------------------------------------------- Q5(a) MUX
def _cbar(f, x, y, size=16):
    f.text(x, y, "C", size=size)
    f.line(x - 6, y - size * 0.82, x + 6, y - size * 0.82, w=1.3)


def fig_q5a_mux():
    """As printed: 4 x 1 MUX, I3 and I2 tied to C-bar, I1 and I0 tied to C,
    select lines S1 = A, S2 = B, output Z."""
    f = Fig(360, 250, "fig_q5a_mux")
    bx, by, bw, bh = 140, 20, 150, 170
    f.rect(bx, by, bw, bh)
    f.text(bx + bw / 2 + 10, by + 92, "MUX", size=17)
    ys = {"I3": 45, "I2": 80, "I1": 120, "I0": 155}
    for k, y in ys.items():
        f.raw('<text x="%d" y="%d" font-size="14" text-anchor="start" fill="#111" '
              'font-family="Times New Roman,serif">I<tspan baseline-shift="sub" '
              'font-size="10">%s</tspan></text>' % (bx + 6, y + 5, k[1]))
    for (ya, yb), lbl in (((ys["I3"], ys["I2"]), "Cbar"), ((ys["I1"], ys["I0"]), "C")):
        xj = 100
        f.line(xj, ya, bx, ya)
        f.line(xj, yb, bx, yb)
        f.line(xj, ya, xj, yb)
        ym = (ya + yb) / 2
        f.line(60, ym, xj, ym)
        f.circle(xj, ym, 2.5, fill="#111")
        if lbl == "C":
            f.text(45, ym + 6, "C", size=16)
        else:
            _cbar(f, 45, ym + 6)
    f.line(bx + bw, by + bh / 2, bx + bw + 45, by + bh / 2)
    f.text(bx + bw + 56, by + bh / 2 + 6, "Z", size=16)
    for x, s, inp in ((bx + 55, "1", "A"), (bx + 95, "2", "B")):
        f.raw('<text x="%d" y="%d" font-size="14" text-anchor="middle" fill="#111" '
              'font-family="Times New Roman,serif"><tspan>S</tspan><tspan baseline-shift="sub" '
              'font-size="10">%s</tspan></text>' % (x, by + bh - 8, s))
        f.line(x, by + bh, x, by + bh + 32)
        f.text(x, by + bh + 50, inp, size=16)
    return f.svg()


def fig_q5a_xor():
    """Z = A XOR C as a single exclusive-OR gate."""
    return bare(RF.single("XOR", ins=("A", "C"), out="Z"), scale=2.0)


# ---------------------------------------------------------------- Q5(c) truth table
Q5C_ON = {3, 5, 7, 11, 12, 13, 14, 15}      # X = AB + A'BD + CD


def fig_q5c_truth():
    """Truth table of X(A,B,C,D) = AB + A'BD + CD; rows with X = 1 shaded,
    with the criterion that makes them 1."""
    cols = ["A", "B", "C", "D", "X", "Criterion met"]
    widths = [42, 42, 42, 42, 42, 150]
    rh, x0, y0 = 22, 10, 30
    W = x0 + sum(widths) + 10
    f = Fig(W, y0 + rh * 17 + 10, "fig_q5c_truth")
    x = x0
    for c, w in zip(cols, widths):
        f.text(x + w / 2, y0 + 15, c, size=13, bold=True, italic=(len(c) == 1))
        x += w
    for k in range(16):
        A, B, C, D = [(k >> (3 - i)) & 1 for i in range(4)]
        v = 1 if k in Q5C_ON else 0
        yy = y0 + rh * (k + 1)
        if v:
            f.rect(x0, yy, sum(widths), rh, color="none", w=0, fill="#e8f4ea")
        x = x0
        for ci, (val, w) in enumerate(zip([A, B, C, D, v], widths)):
            f.text(x + w / 2, yy + 15, str(val), size=13, bold=(ci == 4))
            x += w
        why = []
        if A and B:
            why.append("1st")
        if B and D and not A:
            why.append("2nd")
        if C and D:
            why.append("3rd")
        if why:
            f.text(x + widths[-1] / 2, yy + 15, ", ".join(why), size=12)
    for k in range(18):
        f.line(x0, y0 + rh * k, x0 + sum(widths), y0 + rh * k, w=1.4 if k in (0, 1, 17) else 0.8)
    x = x0
    for w in widths + [0]:
        f.line(x, y0, x, y0 + rh * 17, w=0.8)
        x += w
    return f.svg()


# ---------------------------------------------------------------- Q8 spiral
def fig_q8_spiral():
    """The paper's 4 x 4 example walked in spiral order; the 7th element (16) ringed."""
    f = Fig(330, 300, "fig_q8_spiral")
    x0, y0, c = 50, 40, 60
    vals = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    order = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (3, 0),
             (2, 0), (1, 0), (1, 1), (1, 2), (2, 2), (2, 1)]
    for i in range(4):
        for j in range(4):
            f.rect(x0 + j * c, y0 + i * c, c, c, w=1.0, color="#999")
            f.text(x0 + j * c + 30, y0 + i * c + 36, str(vals[i][j]), size=17,
                   bold=(i, j) == (3, 3))
    pts = [(x0 + j * c + 30, y0 + i * c + 30) for i, j in order]
    for n, ((ax, ay), (bx, by)) in enumerate(zip(pts, pts[1:])):
        col = "#c0392b" if n < 6 else "#2a6db0"
        dx, dy = (bx - ax) / c, (by - ay) / c
        # run each arrow just off the numbers: horizontal ones below, vertical ones left
        ox, oy = (-16 if dy else 0), (14 if dx else 0)
        f.arrow(ax + dx * 12 + ox, ay + dy * 12 + oy, bx - dx * 12 + ox, by - dy * 12 + oy,
                color=col, w=1.4)
    f.circle(x0 + 3 * c + 30, y0 + 3 * c + 30, 20, color="#c0392b", w=2)
    for k, (i, j) in enumerate(order[:7]):
        f.text(x0 + j * c + 52, y0 + i * c + 14, str(k + 1), size=10, color="#c0392b")
    f.text(165, 22, "count 1 … 7 along the spiral: 7th element = 16", size=13, color="#c0392b")
    return f.svg()


# ---------------------------------------------------------------- Q9 deleting the start node
def fig_q9_delete():
    """void deleteNode(Node first): copy the second node's data into the start
    node and bypass the second node, so the caller's start reference stays valid."""
    f = Fig(560, 240, "fig_q9_delete")
    xs = [40, 170, 300, 430]
    y = 60
    old = ["Red", "Green", "Blue", "Pink"]
    for i, (x, v) in enumerate(zip(xs, old)):
        grey = i == 1
        col = "#999" if grey else "#111"
        f.rect(x, y, 62, 34, color=col, fill="#f3f3f3" if grey else "none")
        f.rect(x + 62, y, 26, 34, color=col)
        if i == 0:
            f.text(x + 31, y + 15, "Red", size=12, color="#999")
            f.line(x + 14, y + 11, x + 48, y + 11, color="#999", w=1.2)
            f.text(x + 31, y + 30, "Green", size=13, color="#c0392b", bold=True)
        else:
            f.text(x + 31, y + 22, v, size=14, color=col)
        if i == 3:
            f.text(x + 75, y + 22, "∅", size=14)
    f.arrow(xs[1] + 75, y + 17, xs[2] - 2, y + 17, color="#999", dash="5 4")
    f.arrow(xs[2] + 75, y + 17, xs[3] - 2, y + 17)
    f.arrow(xs[0] + 75, y + 17, xs[1] - 2, y + 17, color="#999", dash="5 4")
    f.path("M %d %d C %d %d, %d %d, %d %d" % (xs[0] + 75, y + 34, xs[0] + 110, y + 110,
                                              xs[2] - 30, y + 110, xs[2] + 20, y + 37),
           color="#c0392b", w=2, arrow=True)
    f.text(xs[1] + 44, y + 118, "(2)  first.link = second.link", size=13, color="#c0392b")
    f.path("M %d %d C %d %d, %d %d, %d %d" % (xs[1] + 31, y - 4, xs[1] + 10, y - 40,
                                              xs[0] + 60, y - 40, xs[0] + 40, y - 3),
           color="#2a6db0", w=1.8, arrow=True)
    f.text(xs[1] + 60, y - 30, "(1)  first.str = second.str", size=13, color="#2a6db0", anchor="start")
    f.text(xs[0] + 31, y + 160, "first / start", size=13, italic=True)
    f.arrow(xs[0] + 31, y + 146, xs[0] + 31, y + 37)
    f.text(xs[1] + 31, y + 160, "second (removed)", size=13, italic=True, color="#777")
    return f.svg()


# ---------------------------------------------------------------- Q10 tree
Q10_TREE = ("8", ("3", ("1", None, None), ("6", ("4", None, None), ("7", None, None))),
            ("10", None, ("14", ("13", None, None), None)))


def fig_q10_tree():
    return tree(Q10_TREE, scale=2.0)


def fig_q10_recursive():
    """A binary tree = root + left subtree + right subtree, each itself a binary tree."""
    f = Fig(420, 200, "fig_q10_recursive")
    f.circle(210, 40, 20)
    f.text(210, 46, "root", size=13)
    f.line(196, 54, 110, 108)
    f.line(224, 54, 310, 108)
    for cx, lbl in ((110, "left subtree"), (310, "right subtree")):
        f.path("M %d %d L %d %d L %d %d Z" % (cx, 108, cx - 70, 185, cx + 70, 185), fill="#f1f5fb")
        f.text(cx, 160, lbl, size=13)
        f.text(cx, 178, "(a binary tree)", size=11, color="#555")
    return f.svg()


# ---------------------------------------------------------------- Q11 class diagram
def fig_q11_classes():
    """Staff (interface) implemented by Worker; Wages extends Worker."""
    f = Fig(380, 256, "fig_q11_classes")
    def box(x, y, title, lines, italic=False):
        h = 30 + 17 * len(lines)
        f.rect(x, y, 200, h, fill="#fafafa")
        f.line(x, y + 24, x + 200, y + 24, w=1.0)
        f.text(x + 100, y + 17, title, size=13, bold=True, italic=italic)
        for k, s in enumerate(lines):
            f.text(x + 8, y + 40 + 17 * k, s, size=12, anchor="start")
        return h
    box(90, 8, "«interface» Staff", ["display()"], italic=True)
    box(90, 92, "Worker", ["name, basic", "display()"])
    box(90, 186, "Wages", ["hours, rate, wage", "overtime(), display()"])
    f.arrow(190, 92, 190, 57, dash="5 3")
    f.text(200, 76, "implements", size=11, anchor="start", color="#555")
    f.arrow(190, 186, 190, 158)
    f.text(200, 172, "extends", size=11, anchor="start", color="#555")
    return f.svg()


# ---------------------------------------------------------------- Q1(iii) insertion at the beginning
def fig_q1iii_insert():
    """Insert at the beginning: two reference assignments, whatever the list length."""
    f = Fig(520, 150, "fig_q1iii_insert")
    xs = [170, 300, 430]
    y = 80
    for i, (x, v) in enumerate(zip(xs, ["10", "20", "30"])):
        f.rect(x, y, 46, 30)
        f.rect(x + 46, y, 22, 30)
        f.text(x + 23, y + 20, v, size=14)
        if i < 2:
            f.arrow(x + 57, y + 15, xs[i + 1] - 2, y + 15, color="#999", dash="5 4" if i == 0 and False else None)
        else:
            f.text(x + 57, y + 20, "∅", size=13)
    f.rect(30, y, 46, 30, color="#2a6db0")
    f.rect(76, y, 22, 30, color="#2a6db0")
    f.text(53, y + 20, "5", size=14, color="#2a6db0")
    f.arrow(87, y + 15, xs[0] - 2, y + 15, color="#2a6db0", w=2)
    f.text(53, y + 52, "temp", size=12, italic=True, color="#2a6db0")
    f.text(130, y + 52, "(1) temp.link = start", size=12, color="#2a6db0", anchor="start")
    f.text(30, 26, "start", size=13, italic=True, anchor="start")
    f.arrow(60, 30, 60, y - 2, color="#c0392b", w=2)
    f.arrow(80, 24, xs[0] + 10, y - 2, color="#999", dash="4 3")
    f.text(260, 30, "(2) start = temp  — O(1)", size=12, color="#c0392b")
    return f.svg()
