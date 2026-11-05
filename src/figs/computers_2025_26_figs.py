"""Figures for Computer Science pre-board 2025-26, Group 4 (computers_2025_26_g4).

Gate primitives, K-maps and trees come from cs_b_kit (which wraps the validated
Computers/src rev_fig / rev_lib / kmapsolve).  The decoder drawer is the
corrected one from Sample-Papers-2027/src/computers_lib_a.py, copied here (that
module imports a different `kit`, so it cannot be imported on this site).
"""
from cs_b_kit import RF, RL, bare, kmap, circuit, tree, KM
from svg import Fig

# ---------------------------------------------------------------- Q3 (smart lighting)
# X = M'L + MLT' + M'L'S   (M is the MSB)
Q3_ON = [1, 3, 4, 5, 6, 7, 12, 13]
Q3_OFF = [0, 2, 8, 9, 10, 11, 14, 15]
Q3_EXPR, Q3_ROWS = KM.solve("pos", 4, Q3_OFF, list("MLTS"))


def fig_q3_kmap():
    return kmap("pos", Q3_OFF, "MLTS", [c for _, c, _ in Q3_ROWS])


def fig_q3_circuit():
    return circuit(Q3_EXPR, "pos", out="X")


# ---------------------------------------------------------------- Q4(i)
Q4_OFF = [0, 1, 2, 3, 5, 7, 8, 10]
Q4_EXPR, Q4_ROWS = KM.solve("pos", 4, Q4_OFF, list("ABCD"))


def fig_q4i_kmap():
    return kmap("pos", Q4_OFF, "ABCD", [c for _, c, _ in Q4_ROWS])


def fig_q4i_circuit():
    return circuit(Q4_EXPR, "pos")


# ---------------------------------------------------------------- Q4(ii) printed circuit
def fig_q4ii_circuit():
    """As printed: (1) = OR(X, Y'), (2) = AND(X, Z), (3) = AND((1), (2)),
    F = OR((3), Z')."""
    f = RL.Fig(300, 150)
    g1 = RF.gOR(f, 90, 32, 2)                      # (1)
    g2 = RF.gAND(f, 90, 96, 2)                     # (2)
    g3 = RF.gAND(f, 160, 64, 2)                    # (3)
    g4 = RF.gOR(f, 220, 84, 2)                     # F
    xX, yX = g1["in"][0][1], g1["in"][0][1]
    # X: straight to OR(1); branch at x=60 down to AND(2) top input
    f.t(12, g1["in"][0][1] + 3.5, "X", size=10, weight="700", anchor="end")
    f.line(16, g1["in"][0][1], g1["in"][0][0], g1["in"][0][1], 1.2)
    f.line(60, g1["in"][0][1], 60, g2["in"][0][1], 1.2)
    f.line(60, g2["in"][0][1], g2["in"][0][0], g2["in"][0][1], 1.2)
    RF.dot(f, 60, g1["in"][0][1])
    # Y -> NOT -> OR(1) second input (crosses the X branch: no dot, no join)
    yY = g1["in"][1][1]
    f.t(12, yY + 3.5, "Y", size=10, weight="700", anchor="end")
    n1 = RF.gNOT(f, 30, yY, lead=4)
    f.line(16, yY, n1["in"][0][0], yY, 1.2)
    f.line(n1["out"][0], yY, g1["in"][1][0], yY, 1.2)
    f.t(64, yY - 3, "Y′", size=7.5, anchor="start")    # right of the X branch at x = 60
    # Z -> AND(2) second input; branch at x=24 down to NOT -> F's second input
    yZ = g2["in"][1][1]
    f.t(12, yZ + 3.5, "Z", size=10, weight="700", anchor="end")
    f.line(16, yZ, g2["in"][1][0], yZ, 1.2)
    RF.dot(f, 24, yZ)
    yN = 132
    f.line(24, yZ, 24, yN, 1.2)
    n2 = RF.gNOT(f, 40, yN, lead=16)
    f.t(n2["out"][0] + 2, yN - 3, "Z′", size=7.5, anchor="start")
    f.line(n2["out"][0], yN, 204, yN, 1.2)
    f.line(204, yN, 204, g4["in"][1][1], 1.2)
    f.line(204, g4["in"][1][1], g4["in"][1][0], g4["in"][1][1], 1.2)
    # (1), (2) -> AND(3) -> F
    RF.wire(f, g1["out"], g3["in"][0], mid=140)
    RF.wire(f, g2["out"], g3["in"][1], mid=140)
    RF.wire(f, g3["out"], g4["in"][0], mid=200)
    f.t(g1["out"][0] + 2, g1["out"][1] - 5, "(1)", size=8.5, anchor="start")
    f.t(g2["out"][0] + 2, g2["out"][1] - 5, "(2)", size=8.5, anchor="start")
    f.t(g3["out"][0] + 1, g3["out"][1] - 5, "(3)", size=8.5, anchor="start")
    f.line(g4["out"][0], g4["out"][1], g4["out"][0] + 12, g4["out"][1], 1.2)
    f.t(g4["out"][0] + 14, g4["out"][1] + 3.5, "F(X,Y,Z)", size=9, anchor="start", weight="700")
    return bare(f.svg(), scale=2.1)


# ---------------------------------------------------------------- Q5(i) decoder
Q5_WORDS = ["0001", "0101", "0111", "1000", "1010", "1100", "1110", "1111"]
Q5_HEX = ["%X" % int(w, 2) for w in Q5_WORDS]


def fig_q5i_decoder():
    """Gate-level decoder: true bus and complemented bus (own inverter) for each
    of A B C D, one 4-input AND per word; a 1 bit takes the true line, a 0 bit
    the complemented line.  (Copied from Sample-Papers-2027 computers_lib_a.)"""
    bits = [("%s = %s" % (w, h), w) for w, h in zip(Q5_WORDS, Q5_HEX)]
    nvar = 4
    names = "ABCD"
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
    # taller than wide: the kit gives it class "tall" (no height cap)
    return bare(f.svg(), scale=1.6)       # 428 px wide, inside the "tall" 440 px cap


# ---------------------------------------------------------------- Q5(ii) printed circuit
def fig_q5ii_circuit():
    """As printed: F4 = NOR(A', AND(A, B'))."""
    f = RL.Fig(220, 100)
    g2 = RF.gOR(f, 140, 40, 2, inv=True)          # NOR -> F4
    g1 = RF.gAND(f, 60, 70, 2)                     # A . B'
    f.t(14, g2["in"][0][1] - 4, "A′", size=10, weight="700", anchor="start")
    f.line(14, g2["in"][0][1], g2["in"][0][0], g2["in"][0][1], 1.2)
    f.t(10, g1["in"][0][1] + 3.5, "A", size=10, weight="700", anchor="end")
    f.line(14, g1["in"][0][1], g1["in"][0][0], g1["in"][0][1], 1.2)
    f.t(10, g1["in"][1][1] + 3.5, "B′", size=10, weight="700", anchor="end")
    f.line(14, g1["in"][1][1], g1["in"][1][0], g1["in"][1][1], 1.2)
    RF.wire(f, g1["out"], g2["in"][1], mid=118)
    f.line(g2["out"][0], g2["out"][1], g2["out"][0] + 14, g2["out"][1], 1.2)
    f.t(g2["out"][0] + 4, g2["out"][1] - 6, "F4", size=10, anchor="start", weight="700")
    return bare(f.svg(), scale=2.0)


# ---------------------------------------------------------------- Q11(ii) tree
Q11_TREE = ("A",
            ("B", ("D", ("H", None, None), ("I", None, None)),
                  ("E", None, ("J", None, None))),
            ("C", ("F", None, None), ("G", None, None)))


def fig_q11_tree():
    return tree(Q11_TREE, scale=2.0)


# ---------------------------------------------------------------- Q11(i) deletion
def fig_q11i_delete():
    """Deleting 30 from 10 -> 20 -> 30 -> 40: prev.link = ptr.link."""
    f = Fig(560, 170, "fig_q11i_delete")
    xs = [40, 160, 280, 400]
    y = 70
    vals = [10, 20, 30, 40]
    for i, (x, v) in enumerate(zip(xs, vals)):
        col = "#999" if v == 30 else "#111"
        f.rect(x, y, 50, 34, color=col, fill="#f3f3f3" if v == 30 else "none")
        f.rect(x + 50, y, 26, 34, color=col)
        f.text(x + 25, y + 22, str(v), size=15, color=col)
        if i < 3:
            dash = "5 4" if v in (20, 30) else None
            c = "#999" if v in (20, 30) else "#111"
            f.arrow(x + 63, y + 17, xs[i + 1] - 2, y + 17, color=c, dash=dash)
        else:
            f.text(x + 63, y + 22, "∅", size=14)
    f.text(26, y - 32, "start", size=13, italic=True, anchor="start")
    f.arrow(40, y - 28, 52, y - 2)
    f.text(xs[1] + 25, y + 70, "prev", size=13, italic=True)
    f.arrow(xs[1] + 25, y + 56, xs[1] + 25, y + 37)
    f.text(xs[2] + 25, y + 70, "ptr", size=13, italic=True)
    f.arrow(xs[2] + 25, y + 56, xs[2] + 25, y + 37)
    f.path("M %d %d C %d %d, %d %d, %d %d" % (xs[1] + 63, y, xs[1] + 100, y - 60,
                                              xs[3] - 40, y - 60, xs[3] + 20, y - 3),
           color="#c0392b", w=2, arrow=True)
    f.text(xs[2] + 38, y - 50, "prev.link = ptr.link", size=13, color="#c0392b")
    return f.svg()


# ---------------------------------------------------------------- Q9 queue
def fig_q9_queue():
    """Repeat with cap = 5 after pushValue(10), (20), (30) and one popValue()."""
    f = Fig(520, 150, "fig_q9_queue")
    x0, y = 60, 50
    vals = ["10", "20", "30", "", ""]
    for i, v in enumerate(vals):
        x = x0 + 60 * i
        grey = i == 0
        f.rect(x, y, 60, 40, fill="#eee" if grey else "none")
        f.text(x + 30, y + 26, v, size=15, color="#999" if grey else "#111")
        f.text(x + 30, y + 58, str(i), size=11, color="#555")
    f.text(x0 - 8, y + 26, "st", size=14, italic=True, anchor="end")
    f.text(x0 + 150, y - 26, "f = 1 (front)", size=12, anchor="start")
    f.path("M %d %d L %d %d L %d %d" % (x0 + 148, y - 30, x0 + 90, y - 30, x0 + 90, y - 2), arrow=True)
    f.text(x0 + 150, y + 96, "r = 2 (rear)", size=12)
    f.arrow(x0 + 150, y + 82, x0 + 150, y + 64)
    f.text(x0 + 30, y + 96, "deleted", size=11, color="#777")
    f.text(x0 + 308, y + 26, "← insert at rear", size=12, anchor="start", color="#2a6")
    f.text(x0 - 2, y - 26, "← delete at front", size=12, anchor="start", color="#c0392b")
    return f.svg()


# ---------------------------------------------------------------- Q3(i) truth table
def fig_q3_truth():
    """Truth table of X(M,L,T,S); rows where X = 0 give the maxterms."""
    rows = 16
    cw, rh, x0, y0 = 46, 22, 10, 30
    cols = ["M", "L", "T", "S", "X", "Maxterm (X = 0)"]
    widths = [cw, cw, cw, cw, cw, 150]
    W = x0 + sum(widths) + 10
    f = Fig(W, y0 + rh * (rows + 1) + 10, "fig_q3_truth")
    x = x0
    for c, w in zip(cols, widths):
        f.text(x + w / 2, y0 + 15, c, size=13, bold=True, italic=(len(c) == 1))
        x += w
    for k in range(rows):
        bits = [(k >> (3 - i)) & 1 for i in range(4)]
        v = 1 if k in Q3_ON else 0
        yy = y0 + rh * (k + 1)
        if not v:
            f.rect(x0, yy, sum(widths), rh, color="none", w=0, fill="#fdecea")
        vals = bits + [v]
        x = x0
        for ci, (val, w) in enumerate(zip(vals, widths)):
            f.text(x + w / 2, yy + 15, str(val), size=13, bold=(ci == 4))
            x += w
        if not v:
            term = "+".join(n + ("′" if b else "") for n, b in zip("MLTS", bits))
            f.text(x + widths[-1] / 2, yy + 15, "(" + term + ")", size=12)
    for k in range(rows + 2):
        f.line(x0, y0 + rh * k, x0 + sum(widths), y0 + rh * k, w=0.8 if k not in (0, 1, rows + 1) else 1.4)
    x = x0
    for w in widths + [0]:
        f.line(x, y0, x, y0 + rh * (rows + 1), w=0.8)
        x += w
    return f.svg()
