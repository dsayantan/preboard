"""Figures for Computer Science pre-board 2016-17 (Paper 1 and Paper 2)."""
from cs_b_kit import RF, RL, bare, kmap, circuit, encoder, tree, KM

# ---------------------------------------------------------------- Q1(d)
def fig_q1d_gate():
    return bare(RF.single("XNOR", ("A", "B"), "X = A &#8857; B"), scale=1.8)


def fig_q1d_basic():
    """XNOR from basic gates: X = AB + A'B' (complements made with NOT gates)."""
    f = RL.Fig(250, 110)
    xa, xb, xna, xnb = 20.0, 34.0, 70.0, 84.0
    f.t(xa, 10, "A", size=9, weight="700")
    f.t(xb, 10, "B", size=9, weight="700")
    f.line(xa, 14, xa, 92, 1.2)
    f.line(xb, 14, xb, 92, 1.2)
    na = RF.gNOT(f, 46, 20, lead=4)
    nb = RF.gNOT(f, 46, 36, lead=4)
    f.line(xa, 20, na["in"][0][0], 20, 1.2); RF.dot(f, xa, 20)
    f.line(xb, 36, nb["in"][0][0], 36, 1.2); RF.dot(f, xb, 36)
    f.line(na["out"][0], 20, xna, 20, 1.2); f.line(xna, 20, xna, 92, 1.2)
    f.line(nb["out"][0], 36, xnb, 36, 1.2); f.line(xnb, 36, xnb, 92, 1.2)
    f.t(xna + 3, 17, "A&prime;", size=7.5, anchor="start")
    f.t(xnb + 3, 33, "B&prime;", size=7.5, anchor="start")
    g1 = RF.gAND(f, 120, 56, 2)
    g2 = RF.gAND(f, 120, 84, 2)
    for (px, py), bx in zip(g1["in"], (xa, xb)):
        f.line(bx, py, px, py, 1.2); RF.dot(f, bx, py)
    for (px, py), bx in zip(g2["in"], (xna, xnb)):
        f.line(bx, py, px, py, 1.2); RF.dot(f, bx, py)
    g3 = RF.gOR(f, 178, 70, 2)
    RF.wire(f, g1["out"], g3["in"][0], mid=160)
    RF.wire(f, g2["out"], g3["in"][1], mid=160)
    f.t(g1["out"][0] + 1, g1["out"][1] - 4, "AB", size=7.5, anchor="start")
    f.t(g2["out"][0] + 1, g2["out"][1] + 10, "A&prime;B&prime;", size=7.5, anchor="start")
    f.t(g3["out"][0] + 3, 73, "X", size=9.5, anchor="start", weight="700")
    return bare(f.svg(), scale=2.0)


# ---------------------------------------------------------------- Q4 K-maps
Q4A_ON = [0, 1, 2, 3, 5, 8, 9, 10, 11, 13, 14, 15]
Q4B_OFF = [3, 4, 5, 6, 7, 9, 11, 13]
Q4A_EXPR, Q4A_ROWS = KM.solve("sop", 4, Q4A_ON, list("ABCD"))
Q4B_EXPR, Q4B_ROWS = KM.solve("pos", 4, Q4B_OFF, list("ABCD"))
Q5_OFF = [0, 1, 2, 3, 4, 5, 6, 8, 9, 12, 13]
Q5_EXPR, Q5_ROWS = KM.solve("pos", 4, Q5_OFF, list("EFGH"))


def fig_q4a_kmap():
    return kmap("sop", Q4A_ON, "ABCD", [c for _, c, _ in Q4A_ROWS])


def fig_q4a_circuit():
    return circuit(Q4A_EXPR, "sop")


def fig_q4b_kmap():
    return kmap("pos", Q4B_OFF, "ABCD", [c for _, c, _ in Q4B_ROWS])


def fig_q4b_circuit():
    return circuit(Q4B_EXPR, "pos")


def fig_q5a_kmap():
    return kmap("pos", Q5_OFF, "EFGH", [c for _, c, _ in Q5_ROWS])


def fig_q5a_circuit():
    return circuit("(G)(E+F)(E+H)", "pos", out="I")


# ---------------------------------------------------------------- Q5(b) decoder
def fig_q5b_decoder():
    """3-to-8 decoder (inputs x y z, x the MSB) with three OR gates:
    F1 = D0 + D5 + D7,  F2 = D2 + D3 + D5,  F3 = D1 + D6 + D7."""
    f = RL.Fig(360, 262)
    bx0, bx1, by0, by1 = 50.0, 106.0, 12.0, 250.0
    f.rect(bx0, by0, bx1 - bx0, by1 - by0, r=3)
    f.t((bx0 + bx1) / 2, 126, "3 &#215; 8", size=9, weight="700")
    f.t((bx0 + bx1) / 2, 138, "DECODER", size=8, weight="700")
    for i, (lab, y) in enumerate((("x", 72.0), ("y", 131.0), ("z", 190.0))):
        f.line(16, y, bx0, y, 1.2)
        f.t(12, y + 3.2, lab, size=9.5, anchor="end", weight="700")
        f.t(bx0 + 3, y + 3, "2" if i == 0 else ("1" if i == 1 else "0"), size=6.5, anchor="start")
    dy = {i: 26.0 + 30.0 * i for i in range(8)}
    gates = [("F1", [0, 5, 7], 41.0), ("F2", [2, 3, 5], 131.0), ("F3", [1, 6, 7], 221.0)]
    cols, ci = {}, 0
    for name, ins, gy in gates:
        for d in ins:
            cols[(name, d)] = 130.0 + 14.0 * ci
            ci += 1
    reach = {d: max([x for (n, dd), x in cols.items() if dd == d] + [bx1 + 12]) for d in range(8)}
    for d in range(8):
        f.line(bx1, dy[d], reach[d], dy[d], 1.2)
        f.t(bx1 + 3, dy[d] - 2.5, "D%d" % d, size=7, anchor="start")
    for name, ins, gy in gates:
        g = RF.gOR(f, 282, gy, 3)
        for (px, py), d in zip(g["in"], ins):
            cx = cols[(name, d)]
            f.line(cx, dy[d], cx, py, 1.2)
            RF.dot(f, cx, dy[d])
            f.line(cx, py, px, py, 1.2)
        f.t(g["out"][0] + 3, gy + 3.2, name, size=9, anchor="start", weight="700")
    return bare(f.svg(), scale=2.1)


# ---------------------------------------------------------------- Q6(b)
def _q6b(f):
    g1 = RF.gAND(f, 80, 29, 2)
    g2 = RF.gOR(f, 80, 70, 2)
    g3 = RF.gAND(f, 150, 115, 2)
    g4 = RF.gOR(f, 150, 160, 2)
    g5 = RF.gAND(f, 150, 205, 2)
    o2 = RF.gOR(f, 220, 45, 2)
    a1 = RF.gAND(f, 310, 160, 2)
    o1 = RF.gOR(f, 362, 190, 2)
    yA, yB = g1["in"][0][1], g1["in"][1][1]
    f.t(10, yA + 3.2, "A", size=9.5, weight="700", anchor="end")
    f.t(10, yB + 3.2, "B", size=9.5, weight="700", anchor="end")
    f.line(12, yA, g1["in"][0][0], yA, 1.2)
    f.line(12, yB, g1["in"][1][0], yB, 1.2)
    f.line(40, yA, 40, g2["in"][1][1], 1.2); RF.dot(f, 40, yA)
    f.line(40, g2["in"][1][1], g2["in"][1][0], g2["in"][1][1], 1.2)
    f.line(55, yB, 55, g2["in"][0][1], 1.2); RF.dot(f, 55, yB)
    f.line(55, g2["in"][0][1], g2["in"][0][0], g2["in"][0][1], 1.2)
    xab, xapb = 116.0, 126.0
    # AB: to the F2 OR gate and down to the ABC gate
    RF.wire(f, g1["out"], o2["in"][0], mid=200)
    f.line(xab, 29, xab, g5["in"][0][1], 1.2); RF.dot(f, xab, 29)
    f.line(xab, g5["in"][0][1], g5["in"][0][0], g5["in"][0][1], 1.2)
    # A + B: to (A+B)C and (A+B)+C
    f.line(g2["out"][0], 70, xapb, 70, 1.2)
    f.line(xapb, 70, xapb, g4["in"][0][1], 1.2)
    f.line(xapb, g3["in"][0][1], g3["in"][0][0], g3["in"][0][1], 1.2); RF.dot(f, xapb, g3["in"][0][1])
    f.line(xapb, g4["in"][0][1], g4["in"][0][0], g4["in"][0][1], 1.2)
    # C
    yC = g3["in"][1][1]
    f.t(10, yC + 3.2, "C", size=9.5, weight="700", anchor="end")
    f.line(12, yC, g3["in"][1][0], yC, 1.2)
    xc = 100.0
    f.line(xc, yC, xc, g5["in"][1][1], 1.2); RF.dot(f, xc, yC)
    f.line(xc, g4["in"][1][1], g4["in"][1][0], g4["in"][1][1], 1.2); RF.dot(f, xc, g4["in"][1][1])
    f.line(xc, g5["in"][1][1], g5["in"][1][0], g5["in"][1][1], 1.2)
    # F2 = AB + (A+B)C
    RF.wire(f, g3["out"], o2["in"][1], mid=206)
    f.line(o2["out"][0], 45, 392, 45, 1.2)
    f.t(395, 48, "F", size=9.5, anchor="start", weight="700")
    f.t(401, 51, "2", size=6.5, anchor="start", weight="700")
    # F2' and F1
    f.line(262, 45, 262, 150, 1.2); RF.dot(f, 262, 45)
    n = RF.gNOT(f, 270, 150, lead=6)
    f.line(262, 150, n["in"][0][0], 150, 1.2)
    RF.wire(f, n["out"], a1["in"][0], mid=300)
    RF.wire(f, g4["out"], a1["in"][1], mid=290)
    RF.wire(f, a1["out"], o1["in"][0], mid=350)
    RF.wire(f, g5["out"], o1["in"][1], mid=340)
    f.line(o1["out"][0], 190, 392, 190, 1.2)
    f.t(395, 193, "F", size=9.5, anchor="start", weight="700")
    f.t(401, 196, "1", size=6.5, anchor="start", weight="700")
    return dict(g1=g1, g2=g2, g3=g3, g4=g4, g5=g5, o2=o2, a1=a1, o1=o1, n=n)


def fig_q6b_circuit():
    """The printed circuit, redrawn gate for gate."""
    f = RL.Fig(410, 225)
    _q6b(f)
    return bare(f.svg(), scale=2.1)


def fig_q6b_labelled():
    f = RL.Fig(410, 225)
    g = _q6b(f)
    lab = lambda gate, s, dx=2, dy=-4: f.t(gate["out"][0] + dx, gate["out"][1] + dy, s, size=7, anchor="start")
    lab(g["g1"], "AB")
    lab(g["g2"], "A+B", dx=-6, dy=10)
    lab(g["g3"], "(A+B)C", dx=-2, dy=-5)
    lab(g["g4"], "A+B+C", dx=0, dy=-5)
    lab(g["g5"], "ABC", dx=2, dy=-5)
    f.t(286, 142, "F&#8322;&#8242;", size=7, anchor="middle")
    lab(g["a1"], "F&#8322;&#8242;(A+B+C)", dx=1, dy=-5)
    return bare(f.svg(), scale=2.1)


# ---------------------------------------------------------------- Q6(c), (d)
def fig_q6c_encoder():
    ins = ["D%d" % i for i in range(10)]
    wiring = {"A3": ["D8", "D9"], "A2": ["D4", "D5", "D6", "D7"],
              "A1": ["D2", "D3", "D6", "D7"], "A0": ["D1", "D3", "D5", "D7", "D9"]}
    return encoder(ins, ["A3", "A2", "A1", "A0"], wiring, scale=2.2)


def fig_q6d_mux():
    """The block diagram printed in the question."""
    f = RL.Fig(260, 120)
    f.rect(100, 14, 58, 64, r=1)
    f.t(129, 42, "2X1", size=9)
    f.t(129, 58, "MUX", size=9)
    f.line(62, 26, 100, 26, 1.2)
    f.t(56, 29, "a+b", size=9, anchor="end")
    f.t(104, 29, "I", size=7, anchor="start"); f.t(107, 31, "0", size=5.5, anchor="start")
    f.line(62, 56, 100, 56, 1.2)
    f.t(56, 59, "ab", size=9, anchor="end")
    f.t(104, 59, "I", size=7, anchor="start"); f.t(107, 61, "1", size=5.5, anchor="start")
    f.line(158, 46, 196, 46, 1.2)
    f.t(200, 49, "F(P,x,y)", size=9, anchor="start")
    f.line(129, 78, 129, 100, 1.2)
    f.t(129, 112, "P", size=9)
    return bare(f.svg(), scale=1.8)


def fig_q6d_gates():
    """F = P'(a+b) + P(ab) drawn as a 2:1 multiplexer at gate level."""
    f = RL.Fig(270, 120)
    ga = RF.gOR(f, 60, 26, 2)
    gb = RF.gAND(f, 60, 82, 2)
    for g, (s1, s2) in ((ga, ("a", "b")), (gb, ("a", "b"))):
        for (px, py), s in zip(g["in"], (s1, s2)):
            f.line(16, py, px, py, 1.2)
            f.t(13, py + 3.2, s, size=8.5, anchor="end", weight="700")
    yP = 108.0
    f.t(13, yP + 3.2, "P", size=8.5, anchor="end", weight="700")
    f.line(16, yP, 150, yP, 1.2)
    a0 = RF.gAND(f, 160, 40, 2)
    a1 = RF.gAND(f, 160, 82, 2)
    RF.wire(f, ga["out"], a0["in"][0], mid=110)
    RF.wire(f, gb["out"], a1["in"][0], mid=120)
    n = RF.gNOT(f, 108, 60, lead=4)
    f.line(100, yP, 100, 60, 1.2); RF.dot(f, 100, yP)
    f.line(100, 60, n["in"][0][0], 60, 1.2)
    RF.wire(f, n["out"], a0["in"][1], mid=140)
    f.line(150, yP, 150, a1["in"][1][1], 1.2)
    f.line(150, a1["in"][1][1], a1["in"][1][0], a1["in"][1][1], 1.2)
    f.t(n["out"][0] + 2, 56, "P&prime;", size=7.5, anchor="start")
    o = RF.gOR(f, 220, 61, 2)
    RF.wire(f, a0["out"], o["in"][0], mid=205)
    RF.wire(f, a1["out"], o["in"][1], mid=205)
    f.t(o["out"][0] + 3, 64, "F", size=9.5, anchor="start", weight="700")
    f.t(ga["out"][0] + 1, 21, "a+b", size=7, anchor="start")
    f.t(gb["out"][0] + 1, 77, "ab", size=7, anchor="start")
    return bare(f.svg(), scale=2.0)


# ---------------------------------------------------------------- Q12
Q12_TREE = ("A",
            ("B",
             ("C", ("E", None, ("I", None, None)), ("F", None, ("J", None, None))),
             ("D", ("G", None, None), ("H", ("K", None, None), ("L", None, None)))),
            ("M", None, None))


def fig_q12a_tree():
    return tree(Q12_TREE, scale=2.3)


def fig_q12b_list():
    """head -> nodes holding float data, the last ptr null; temp walks the list."""
    f = RL.Fig(330, 76)
    bw, bh, gap, x0, y = 48.0, 24.0, 22.0, 44.0, 30.0
    f.t(6, y + 4, "head", size=9, anchor="start")
    f.arrow(28, y, x0 - 3, y, 1.2)
    vals = ["2.5", "4.0", "1.25", "3.75"]
    for i, v in enumerate(vals):
        x = x0 + i * (bw + gap)
        f.rect(x, y - bh / 2, bw, bh, r=2.5, fill="#fff")
        f.line(x + bw * 0.62, y - bh / 2, x + bw * 0.62, y + bh / 2, 1.1)
        f.t(x + bw * 0.31, y + 3.6, v, size=8.5, weight="600")
        f.circ(x + bw * 0.81, y, 1.9, fill="currentColor", sw=0)
        if i < len(vals) - 1:
            f.arrow(x + bw * 0.81, y, x + bw + gap - 3, y, 1.2)
        else:
            f.arrow(x + bw * 0.81, y, x + bw + 12, y, 1.2)
            f.t(x + bw + 15, y + 3.4, "null", size=8, anchor="start")
    f.t(x0 + bw * 0.31, y - bh / 2 - 4, "data", size=7)
    f.t(x0 + bw * 0.81, y - bh / 2 - 4, "ptr", size=7)
    f.arrow(x0 + 14, 66, x0 + 14, y + bh / 2 + 3, 1.2)
    f.t(x0 + 26, 70, "temp (start)", size=7.5, anchor="start")
    return bare(f.svg(), scale=2.0)


# ---------------------------------------------------------------- Paper 2, Q3
def _pairs(rows):
    f = RL.Fig(150, 26 + 20 * len(rows))
    f.rect(10, 6, 130, 20 + 20 * len(rows), sw=1.1)
    f.line(60, 6, 60, 26 + 20 * len(rows), 1.0)
    f.t(35, 20, "Pair", size=9, weight="700")
    f.t(100, 20, "Difference", size=9, weight="700")
    for i, (p, d) in enumerate(rows):
        y = 26 + 20 * i
        f.line(10, y, 140, y, 1.0)
        f.t(35, y + 14, p, size=9)
        f.t(100, y + 14, d, size=9)
    return bare(f.svg(), scale=1.6)


def fig_p2q3_pairs1():
    return _pairs([("5,3", "2"), ("3,21", "18"), ("21,10", "11"), ("10,12", "2"), ("12,7", "5")])


def fig_p2q3_pairs2():
    return _pairs([("19,0", "19"), ("0,-5", "5"), ("-5,4", "9"), ("4,7", "3"), ("7,10", "3")])
