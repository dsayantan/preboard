"""Figures for Computer Science Pre-Board 2014-15 (Paper 1).  Helpers: computers_a_lib."""
from computers_a_lib import RF, RL, clean, kmap, two_level, tree, llist, lbl, P

ABCD = ["A", "B", "C", "D"]

Q1E = dict(cells=[2, 3, 4, 6, 7], groups=[[2, 3, 6, 7], [4, 6]])
Q4A = dict(cells=[3, 4, 6, 7, 11, 12, 14, 15], groups=[[3, 7, 11, 15], [4, 6, 12, 14]],
           terms=["CD", "BD'"])
Q4B = dict(cells=[0, 8, 10, 12, 13, 14, 15], groups=[[12, 13, 14, 15], [8, 10, 12, 14], [0, 8]],
           terms=["A'+B'", "A'+D", "B+C+D"])
Q5 = dict(names=["G", "T", "A", "B"], cells=[7, 11, 15], groups=[[7, 15], [11, 15]],
          terms=["TAB", "GAB"])
Q6_TERMS = ["X'Y", "XY'"]
Q13_TREE = ("A", ("B", ("D", None, None), ("E", ("H", None, ("K", None, None)), None)),
            ("C", ("F", None, None), ("G", ("I", None, None), ("J", ("L", None, None), None))))
Q13_RIGHT_C = ("G", ("I", None, None), ("J", ("L", None, None), None))
Q13_LIST = [12, 7, 25, 4]


def fig_q1c_or():
    return clean(RF.or_from_nand(cap=None), 380)


def fig_q1e_kmap():
    return kmap(["X", "Y", "Z"], "sop", Q1E["cells"], Q1E["groups"], maxw=360)


def fig_q4a_kmap():
    return kmap(ABCD, "sop", Q4A["cells"], Q4A["groups"])


def fig_q4a_circ():
    return two_level(Q4A["terms"], "sop", ABCD, comp="avail", expr="F = CD + BD′", maxw=380)


def fig_q4b_kmap():
    return kmap(ABCD, "pos", Q4B["cells"], Q4B["groups"])


def fig_q4b_circ():
    return two_level(Q4B["terms"], "pos", ABCD, comp="avail",
                     expr="F = (A′+B′)(A′+D)(B+C+D)", maxw=460)


def fig_q5_kmap():
    return kmap(Q5["names"], "sop", Q5["cells"], Q5["groups"])


def fig_q5_circ():
    return two_level(Q5["terms"], "sop", Q5["names"], comp="avail", out="S",
                     expr="S = TAB + GAB", maxw=380)


def fig_q6_nand():
    return two_level(Q6_TERMS, "sop", ["X", "Y"], uni="nand", comp="nand", out="D",
                     expr="D = X′Y + XY′  (NAND gates only)", maxw=460)


def fig_q6c_fa():
    return clean(RF.full_adder(cap=None), 480, extra=24)


def fig_q7a_mux():
    """4:1 multiplexer at gate level: Y = S1'S0'I0 + S1'S0 I1 + S1 S0'I2 + S1 S0 I3."""
    f = RL.Fig(300, 222)
    ys1, ys0 = 196.0, 212.0
    s1x, s1nx, s0x, s0nx = 44.0, 78.0, 96.0, 130.0
    f.t(10, ys1 + 3.2, "S1", size=8.5, weight="700", anchor="end")
    f.t(10, ys0 + 3.2, "S0", size=8.5, weight="700", anchor="end")
    f.line(12, ys1, 50, ys1, 1.2)
    n1 = RF.gNOT(f, 54, ys1, lead=4)
    f.line(n1["out"][0], ys1, s1nx, ys1, 1.2)
    f.line(12, ys0, 102, ys0, 1.2)
    n2 = RF.gNOT(f, 106, ys0, lead=4)
    f.line(n2["out"][0], ys0, s0nx, ys0, 1.2)
    RF.dot(f, s1x, ys1)
    RF.dot(f, s0x, ys0)
    tops = 50.0
    for x, yb, lab in ((s1x, ys1, "S1"), (s1nx, ys1, "S1" + P), (s0x, ys0, "S0"), (s0nx, ys0, "S0" + P)):
        f.line(x, tops, x, yb, 1.2)
        f.t(x, tops - 4, lab, size=7.5)
    sel = [(s1nx, s0nx), (s1nx, s0x), (s1x, s0nx), (s1x, s0x)]
    outs = []
    for i in range(4):
        y = 66 + i * 34
        g = RF.gAND(f, 160, y, 3)
        px, py = g["in"][0]
        f.line(14, py, px, py, 1.2)
        f.t(12, py + 3, "I<sub>%d</sub>" % i, size=8.5, anchor="end", weight="700")
        for sx, (qx, qy) in zip(sel[i], g["in"][1:]):
            f.line(sx, qy, qx, qy, 1.2)
            RF.dot(f, sx, qy)
        outs.append(g["out"])
    g5 = RF.gOR(f, 246, 117, 4)
    lanes = [1, 0, 0, 1]   # outer gates take the outer lane, so no output wire crosses another
    for k, (o, pin) in enumerate(zip(outs, g5["in"])):
        RF.wire(f, o, pin, mid=222 + 7 * lanes[k])
    f.t(g5["out"][0] + 4, 120, "Y", size=9.5, anchor="start", weight="700")
    return clean(f.svg(), 520, extra=10)


def fig_q7c_given():
    """The circuit printed in Q7(c): (1)=AND(X,Y); (2)=AND((1),Z); (3)=NOT((2));
    F = AND((3),(1))."""
    f = RL.Fig(330, 130)
    g1 = RF.gAND(f, 60, 26, 2)
    for (px, py), s in zip(g1["in"], "XY"):
        f.line(18, py, px, py, 1.2)
        lbl(f, 14, py + 3.5, s, anchor="end", size=10)
    g2 = RF.gAND(f, 140, 54, 2)
    yz = g2["in"][1][1]
    f.line(18, yz, g2["in"][1][0], yz, 1.2)
    lbl(f, 14, yz + 3.5, "Z", anchor="end", size=10)
    xn = g1["out"][0] + 6
    RF.wire(f, g1["out"], g2["in"][0], mid=xn + 14)
    RF.dot(f, xn, g1["out"][1])
    f.t(g1["out"][0] + 2, g1["out"][1] - 5, "(1)", size=8.5, anchor="start")
    n = RF.gNOT(f, 214, 88, lead=6)
    RF.wire(f, g2["out"], n["in"][0], mid=g2["out"][0] + 12)
    f.t(g2["out"][0] + 2, g2["out"][1] - 5, "(2)", size=8.5, anchor="start")
    g3 = RF.gAND(f, 262, 98, 2)
    RF.wire(f, n["out"], g3["in"][0], mid=n["out"][0] + 4)
    f.t(n["out"][0] - 2, n["out"][1] - 6, "(3)", size=8.5, anchor="start")
    # branch of (1) down to the last gate
    f.line(xn, g1["out"][1], xn, 118, 1.2)
    f.line(xn, 118, 250, 118, 1.2)
    f.line(250, 118, 250, g3["in"][1][1], 1.2)
    f.line(250, g3["in"][1][1], g3["in"][1][0], g3["in"][1][1], 1.2)
    f.t(g3["out"][0] + 3, g3["out"][1] + 3.5, "F(X,Y,Z)", size=9, anchor="start", weight="700")
    return clean(f.svg(), 560, extra=30)


def fig_q7c_answer():
    """F = X.Y.Z' : a 3-input AND gate with the Z input inverted."""
    f = RL.Fig(200, 80)
    g = RF.gAND(f, 100, 40, 3)
    for (px, py), s in zip(g["in"][:2], "XY"):
        f.line(24, py, px, py, 1.2)
        lbl(f, 20, py + 3.5, s, anchor="end", size=10)
    pz = g["in"][2]
    n = RF.gNOT(f, 54, pz[1], lead=5)
    f.line(24, pz[1], n["in"][0][0], pz[1], 1.2)
    lbl(f, 20, pz[1] + 3.5, "Z", anchor="end", size=10)
    f.line(n["out"][0], pz[1], pz[0], pz[1], 1.2)
    f.t(n["out"][0] + 2, pz[1] + 11, "Z" + P, size=8, anchor="start")
    f.t(g["out"][0] + 3, 43.5, "F = XYZ" + P, size=9.5, anchor="start", weight="700")
    return clean(f.svg(), 380, extra=20)


def fig_q13a_list():
    return llist(Q13_LIST, head="ptr_start", maxw=440)


def fig_q13b_tree():
    return tree(Q13_TREE, 380)


def fig_q13b_right():
    return tree(Q13_RIGHT_C, 200)
