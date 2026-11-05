"""Figures for Computer Science Pre-Board 2013-14 (Paper 1).  Helpers: computers_a_lib."""
from computers_a_lib import RF, RL, clean, kmap, two_level, tree, lbl, P

ABCD = ["A", "B", "C", "D"]

# ---- data the check script re-uses -------------------------------------------
Q8_TERMS = ["AB'", "A'B", "A'C'"]
Q13_TERMS = ["AB", "ACD"]
Q14A = dict(cells=[1, 6, 7, 8, 9, 10, 14, 15], groups=[[1, 9], [6, 7, 14, 15], [8, 10]],
            terms=["B'C'D", "BC", "AB'D'"])
Q14B = dict(cells=[0, 2, 3, 4, 5, 11, 12, 13], groups=[[0, 2], [3, 11], [4, 5, 12, 13]],
            terms=["A+B+D", "B+C'+D'", "B'+C"])
Q15_DATA = ["D'", "D", "D", "D'", "1", "0", "0", "1"]
Q22_TREE = ("R", ("A", ("C", None, ("D", None, None)), ("B", None, None)),
            ("3", ("5", ("8", None, None), None), ("6", None, ("9", None, None))))
Q10_BST = ("50", ("30", ("20", None, None), ("40", None, None)),
           ("70", ("60", None, None), ("80", None, None)))


def fig_q2_xor():
    """(P xor Q xor R)' and  P xor Q xnor R, side by side as two circuits."""
    f = RL.Fig(300, 150)
    for k, (yy, last, name) in enumerate(((40, "xor+not", "(P⊕Q⊕R)′"),
                                          (112, "xnor", "P⊕Q ⊙ R"))):
        g1 = RF.gOR(f, 50, yy - 10, 2, xor=True)
        for (px, py), s in zip(g1["in"], "PQ"):
            f.line(18, py, px, py, 1.2)
            lbl(f, 14, py + 3.2, s, anchor="end")
        if last == "xor+not":
            g2 = RF.gOR(f, 120, yy, 2, xor=True)
        else:
            g2 = RF.gOR(f, 120, yy, 2, xor=True, inv=True)
        RF.wire(f, g1["out"], g2["in"][0], mid=100)
        f.line(18, g2["in"][1][1], g2["in"][1][0], g2["in"][1][1], 1.2)
        lbl(f, 14, g2["in"][1][1] + 3.2, "R", anchor="end")
        o = g2["out"]
        if last == "xor+not":
            n = RF.gNOT(f, o[0] + 8, o[1], lead=8)
            o = n["out"]
        f.t(o[0] + 4, o[1] + 3.5, name, size=9.5, anchor="start", weight="700")
        f.t(150, yy + 30, "(a) XOR, XOR, then NOT" if k == 0 else "(b) XOR, then XNOR", size=8.5)
    return clean(f.svg(), 560)


def fig_q8_nand():
    return two_level(Q8_TERMS, "sop", ["A", "B", "C"], uni="nand", comp="nand",
                     expr="F = AB′ + A′B + A′C′  (NAND gates only)", maxw=560)


def fig_q10_bst():
    return tree(Q10_BST, 300)


def fig_q13_kmap():
    return kmap(ABCD, "sop", [11, 12, 13, 14, 15], [[12, 13, 14, 15], [11, 15]])


def fig_q13_circ():
    return two_level(Q13_TERMS, "sop", ABCD, comp="avail", out="X", expr="X = AB + ACD", maxw=420)


def fig_q14a_kmap():
    return kmap(ABCD, "sop", Q14A["cells"], Q14A["groups"])


def fig_q14a_circ():
    return two_level(Q14A["terms"], "sop", ABCD, comp="avail",
                     expr="F = B′C′D + BC + AB′D′", maxw=480)


def fig_q14b_kmap():
    return kmap(ABCD, "pos", Q14B["cells"], Q14B["groups"])


def fig_q14b_circ():
    return two_level(Q14B["terms"], "pos", ABCD, comp="avail",
                     expr="F = (A+B+D)(B+C′+D′)(B′+C)", maxw=480)


def fig_q15_mux():
    """8:1 MUX: selects S2 S1 S0 = A B C, data I0..I7 = D', D, D, D', 1, 0, 0, 1."""
    f = RL.Fig(300, 250)
    x, y0, bh = 170.0, 20.0, 170.0
    f.poly([(x, y0), (x + 50, y0 + 14), (x + 50, y0 + bh - 14), (x, y0 + bh)], close=True)
    f.t(x + 25, y0 + bh / 2 - 4, "8 : 1", size=9, weight="700")
    f.t(x + 25, y0 + bh / 2 + 8, "MUX", size=8.5, weight="700")
    xd, xdn = 18.0, 66.0
    ys = [y0 + bh * (i + 1) / 9.0 for i in range(8)]
    lbl(f, xd, 12, "D")
    f.line(xd, 16, xd, ys[3], 1.2)
    n = RF.gNOT(f, 32, 24, lead=5)
    f.line(xd, 24, n["in"][0][0], 24, 1.2)
    RF.dot(f, xd, 24)
    f.line(n["out"][0], 24, xdn, 24, 1.2)
    f.line(xdn, 24, xdn, ys[3], 1.2)
    f.t(xdn + 3, 20, "D\u2032", size=8, anchor="start")
    for i, s in enumerate(Q15_DATA):
        y = ys[i]
        f.t(x - 3, y - 2.5, "I%d" % i, size=7, anchor="end")
        if s in ("0", "1"):
            f.line(140, y, x, y, 1.2)
            f.t(136, y + 3.5, "logic %s" % s, size=8.5, anchor="end", weight="700")
        else:
            src = xd if s == "D" else xdn
            f.line(src, y, x, y, 1.2)
            if i != 3:
                RF.dot(f, src, y)
    f.line(x + 50, y0 + bh / 2, x + 80, y0 + bh / 2, 1.2)
    f.t(x + 84, y0 + bh / 2 + 3.5, "F", size=10, anchor="start", weight="700")
    for k, (s, v) in enumerate((("S2", "A"), ("S1", "B"), ("S0", "C"))):
        sx = x + 12 + 13 * k
        ytop = y0 + bh - 14 * (sx - x) / 50.0
        f.line(sx, ytop, sx, y0 + bh + 22, 1.2)
        f.t(sx, y0 + bh + 32, v, size=9, weight="700")
    f.t(x + 25, y0 + bh + 48, "select lines S2 S1 S0 = A B C", size=8.5)
    return clean(f.svg(), 520)


def fig_q16a_block():
    """Full adder = two half adders + OR.  HA1(A,B) -> S1, C1; HA2(S1,Cin) -> SUM, C2;
    CARRY = C1 + C2."""
    f = RL.Fig(330, 150)
    def ha(x, y, n):
        f.rect(x, y, 56, 56, r=4)
        f.t(x + 28, y + 22, "HALF", size=8.5, weight="700")
        f.t(x + 28, y + 33, "ADDER %d" % n, size=8.5, weight="700")
        f.t(x + 5, y + 16, "a", size=7, anchor="start"); f.t(x + 5, y + 46, "b", size=7, anchor="start")
        f.t(x + 51, y + 16, "s", size=7, anchor="end"); f.t(x + 51, y + 46, "c", size=7, anchor="end")
        return {"a": (x, y + 13), "b": (x, y + 43), "s": (x + 56, y + 13), "c": (x + 56, y + 43)}
    h1 = ha(60, 14, 1)
    h2 = ha(160, 36, 2)
    for s_, pin in (("A", h1["a"]), ("B", h1["b"])):
        f.line(24, pin[1], pin[0], pin[1], 1.2); lbl(f, 18, pin[1] + 3.5, s_, anchor="end", size=10)
    # C (carry in) to HA2 b
    f.line(24, 112, 140, 112, 1.2); lbl(f, 18, 115.5, "C", anchor="end", size=10)
    f.line(140, 112, 140, h2["b"][1], 1.2); f.line(140, h2["b"][1], h2["b"][0], h2["b"][1], 1.2)
    # S1 -> HA2 a
    RF.wire(f, h1["s"], h2["a"], mid=136)
    f.t(h1["s"][0] + 3, h1["s"][1] - 4, "A\u2295B", size=7.5, anchor="start")
    # HA2 s -> SUM
    f.line(h2["s"][0], h2["s"][1], 300, h2["s"][1], 1.2)
    f.t(300, h2["s"][1] - 4, "SUM", size=9, anchor="end", weight="700")
    g = RF.gOR(f, 255, 112, 2)
    RF.wire(f, h2["c"], g["in"][0], mid=240)
    f.t(h2["c"][0] + 3, h2["c"][1] - 4, "C(A\u2295B)", size=7.5, anchor="start")
    # C1 -> OR lower input, routed below the C line
    f.line(h1["c"][0], h1["c"][1], 124, h1["c"][1], 1.2)
    f.line(124, h1["c"][1], 124, 132, 1.2)
    f.line(124, 132, 232, 132, 1.2); f.line(232, 132, 232, g["in"][1][1], 1.2)
    f.line(232, g["in"][1][1], g["in"][1][0], g["in"][1][1], 1.2)
    f.t(h1["c"][0] + 3, h1["c"][1] - 4, "AB", size=7.5, anchor="start")
    f.t(g["out"][0] + 3, g["out"][1] + 3.5, "CARRY", size=9, anchor="start", weight="700")
    return clean(f.svg(), 560, extra=10)


def fig_q16a_gates():
    return clean(RF.full_adder(cap=None), 480, extra=24)


def fig_q16b_not():
    f = RL.Fig(170, 60)
    g = RF.gAND(f, 60, 30, 2, inv=True)
    xs = g["in"][0][0] - 6
    f.line(18, 30, xs, 30, 1.2)
    f.line(xs, g["in"][0][1], xs, g["in"][1][1], 1.2)
    for px, py in g["in"]:
        f.line(xs, py, px, py, 1.2)
    RF.dot(f, xs, 30)
    lbl(f, 14, 33, "A", anchor="end")
    f.t(g["out"][0] + 3, 33.5, "(A·A)′ = A′", size=9, anchor="start", weight="700")
    return clean(f.svg(), 300)


def fig_q16b_and():
    return clean(RF.from_universal("NAND", "AND", cap=None), 380)


def fig_q16b_or():
    return clean(RF.or_from_nand(cap=None), 380)


def fig_q22_tree():
    return tree(Q22_TREE, 360)
