"""Figures for Computer Science pre-board 2015-16 (Paper 1 and Paper 2)."""
from cs_b_kit import RF, RL, bare, kmap, circuit, encoder, tree, KM

# ---------------------------------------------------------------- Q12 K-maps
Q12A_ON = [0, 1, 2, 4, 5, 6, 7, 8, 9, 12, 13, 14]
Q12B_OFF = [0, 1, 2, 5, 8, 9, 10]
Q12A_EXPR, Q12A_ROWS = KM.solve("sop", 4, Q12A_ON, list("ABCD"))
Q12B_EXPR, Q12B_ROWS = KM.solve("pos", 4, Q12B_OFF, list("ABCD"))


def fig_q12a_kmap():
    return kmap("sop", Q12A_ON, "ABCD", [c for _, c, _ in Q12A_ROWS])


def fig_q12a_circuit():
    return circuit(Q12A_EXPR, "sop")


def fig_q12b_kmap():
    return kmap("pos", Q12B_OFF, "ABCD", [c for _, c, _ in Q12B_ROWS])


def fig_q12b_circuit():
    return circuit(Q12B_EXPR, "pos", out="X")


# ---------------------------------------------------------------- Q13
def fig_q13a_mux4():
    """4:1 MUX at gate level: inverters for S1, S0; four 3-input ANDs; one 4-input OR.
    Y = S1'S0'I0 + S1'S0 I1 + S1 S0'I2 + S1 S0 I3."""
    f = RL.Fig(300, 226)
    ys1, ys0 = 198.0, 214.0
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
    for x, yb, lab in ((s1x, ys1, "S1"), (s1nx, ys1, "S1&prime;"), (s0x, ys0, "S0"),
                       (s0nx, ys0, "S0&prime;")):
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
    lanes = [1, 0, 0, 1]      # outer gates take the outer lane: no wire crosses another
    for k, (o, pin) in enumerate(zip(outs, g5["in"])):
        RF.wire(f, o, pin, mid=222 + 7 * lanes[k])
    f.t(g5["out"][0] + 4, 120, "Y", size=9.5, anchor="start", weight="700")
    return bare(f.svg(), scale=1.8)


def fig_q13a_block():
    """4:1 MUX as a block, with the select table beside it."""
    f = RL.Fig(300, 142)
    x, y0, bh = 70.0, 12.0, 92.0
    f.poly([(x, y0), (x + 46, y0 + 12), (x + 46, y0 + bh - 12), (x, y0 + bh)], close=True)
    f.t(x + 23, y0 + bh / 2 - 3, "4 : 1", size=8.5, weight="700")
    f.t(x + 23, y0 + bh / 2 + 8, "MUX", size=8, weight="700")
    for i in range(4):
        y = y0 + bh * (i + 1) / 5
        f.line(36, y, x, y, 1.2)
        f.t(32, y + 3.2, "I<sub>%d</sub>" % i, size=8.5, anchor="end", weight="700")
    f.line(x + 46, y0 + bh / 2, x + 76, y0 + bh / 2, 1.2)
    f.t(x + 79, y0 + bh / 2 + 3.2, "Y", size=9, anchor="start", weight="700")
    for i, lab in enumerate(("S1", "S0")):
        sx = x + 15 + i * 16.0
        yb = y0 + bh - (sx - x) * 12 / 46          # meets the sloping bottom edge exactly
        f.line(sx, yb, sx, y0 + bh + 18, 1.2)
        f.t(sx, y0 + bh + 27, lab, size=8, weight="700")
    tx = 196
    rows = [("S1", "S0", "Y"), ("0", "0", "I<sub>0</sub>"), ("0", "1", "I<sub>1</sub>"),
            ("1", "0", "I<sub>2</sub>"), ("1", "1", "I<sub>3</sub>")]
    for r, row in enumerate(rows):
        for c, v in enumerate(row):
            f.t(tx + c * 28, 26 + r * 18, v, size=9, weight="700" if r == 0 else None)
    f.line(tx - 14, 31, tx + 70, 31, 1.0)
    return bare(f.svg(), scale=1.8)


def fig_q13b_nornor():
    """NOR-NOR form of (A + D')(B' + A)(D' + C)."""
    return circuit("(A+D')(B'+A)(D'+C)", "pos", uni="nor")


def fig_q13c_xnor_nor():
    """XNOR from four NOR gates: G1 = (A+B)', G2 = (A+G1)' = A'B, G3 = (B+G1)' = AB',
    X = (G2+G3)' = A'B' + AB."""
    f = RL.Fig(305, 110)
    ya, yb = 22.0, 88.0
    g1 = RF.gOR(f, 70, 55, 2, inv=True)
    g2 = RF.gOR(f, 140, 27, 2, inv=True)
    g3 = RF.gOR(f, 140, 83, 2, inv=True)
    g4 = RF.gOR(f, 212, 55, 2, inv=True)
    f.t(10, g2["in"][0][1] + 3.2, "A", size=9.5, weight="700", anchor="end")
    f.t(10, g3["in"][1][1] + 3.2, "B", size=9.5, weight="700", anchor="end")
    # A: straight to G2 top input, tapped at x=30 down to G1 top input
    f.line(12, g2["in"][0][1], g2["in"][0][0], g2["in"][0][1], 1.2)
    f.line(30, g2["in"][0][1], 30, g1["in"][0][1], 1.2)
    f.line(30, g1["in"][0][1], g1["in"][0][0], g1["in"][0][1], 1.2)
    RF.dot(f, 30, g2["in"][0][1])
    # B: straight to G3 bottom input, tapped at x=42 up to G1 bottom input
    f.line(12, g3["in"][1][1], g3["in"][1][0], g3["in"][1][1], 1.2)
    f.line(42, g3["in"][1][1], 42, g1["in"][1][1], 1.2)
    f.line(42, g1["in"][1][1], g1["in"][1][0], g1["in"][1][1], 1.2)
    RF.dot(f, 42, g3["in"][1][1])
    # G1 output to G2 bottom and G3 top
    ox, oy = g1["out"]
    f.line(ox, oy, 116, oy, 1.2)
    f.line(116, g2["in"][1][1], 116, g3["in"][0][1], 1.2)
    f.line(116, g2["in"][1][1], g2["in"][1][0], g2["in"][1][1], 1.2)
    f.line(116, g3["in"][0][1], g3["in"][0][0], g3["in"][0][1], 1.2)
    RF.dot(f, 116, oy)
    RF.wire(f, g2["out"], g4["in"][0], mid=196)
    RF.wire(f, g3["out"], g4["in"][1], mid=196)
    f.t(g1["out"][0] - 4, g1["out"][1] - 9, "(A+B)&prime;", size=7.5)
    f.t(g2["out"][0] + 2, g2["out"][1] - 6, "A&prime;B", size=7.5, anchor="start")
    f.t(g3["out"][0] + 2, g3["out"][1] + 11, "AB&prime;", size=7.5, anchor="start")
    f.t(g4["out"][0] + 3, g4["out"][1] + 3.2, "X = A &#8857; B", size=8.5, anchor="start",
        weight="700")
    return bare(f.svg(), scale=2.0)


# ---------------------------------------------------------------- Q14
def fig_q14b_encoder():
    ins = ["D%d" % i for i in range(8)]
    wiring = {"A2": ["D4", "D5", "D6", "D7"], "A1": ["D2", "D3", "D6", "D7"],
              "A0": ["D1", "D3", "D5", "D7"]}
    return encoder(ins, ["A2", "A1", "A0"], wiring)


def fig_q14c_circuit():
    """The printed circuit, redrawn: Out = (B + C + D')(D' + C + A)(D + C')."""
    f = RL.Fig(300, 190)
    o1 = RF.gOR(f, 150, 32, 3)
    o2 = RF.gOR(f, 150, 84, 3)
    o3 = RF.gOR(f, 150, 146, 2)
    an = RF.gAND(f, 226, 84, 3)
    xC, xD = 26.0, 56.0
    # B -> OR1 in0
    f.t(12, o1["in"][0][1] + 3.2, "B", size=9.5, weight="700", anchor="end")
    f.line(14, o1["in"][0][1], o1["in"][0][0], o1["in"][0][1], 1.2)
    # C -> OR1 in1, bus down at xC
    f.t(12, o1["in"][1][1] + 3.2, "C", size=9.5, weight="700", anchor="end")
    f.line(14, o1["in"][1][1], o1["in"][1][0], o1["in"][1][1], 1.2)
    yCn = 172.0
    f.line(xC, o1["in"][1][1], xC, yCn, 1.2)
    RF.dot(f, xC, o1["in"][1][1])
    # C -> OR2 in1 (crosses the D line without joining)
    f.line(xC, o2["in"][1][1], o2["in"][1][0], o2["in"][1][1], 1.2)
    RF.dot(f, xC, o2["in"][1][1])
    # C -> NOT -> C' -> OR3 in1
    f.line(xC, yCn, 66, yCn, 1.2)
    nc = RF.gNOT(f, 70, yCn, lead=4)
    RF.wire(f, nc["out"], o3["in"][1], mid=118)
    # D -> NOT -> D' bus at x=116 -> OR1 in2, OR2 in0
    yD = 60.0
    f.t(38, yD + 3.2, "D", size=9.5, weight="700", anchor="end")
    f.line(40, yD, 70, yD, 1.2)
    nd = RF.gNOT(f, 74, yD, lead=4)
    xDn = 120.0
    f.line(nd["out"][0], yD, xDn, yD, 1.2)
    f.line(xDn, o1["in"][2][1], xDn, o2["in"][0][1], 1.2)
    f.line(xDn, o1["in"][2][1], o1["in"][2][0], o1["in"][2][1], 1.2)
    f.line(xDn, o2["in"][0][1], o2["in"][0][0], o2["in"][0][1], 1.2)
    RF.dot(f, xDn, yD)
    # D also straight down at xD -> OR3 in0
    f.line(xD, yD, xD, o3["in"][0][1], 1.2)
    f.line(xD, o3["in"][0][1], o3["in"][0][0], o3["in"][0][1], 1.2)
    RF.dot(f, xD, yD)
    # A -> OR2 in2
    f.t(96, o2["in"][2][1] + 3.2, "A", size=9.5, weight="700", anchor="end")
    f.line(98, o2["in"][2][1], o2["in"][2][0], o2["in"][2][1], 1.2)
    # ORs -> AND
    RF.wire(f, o1["out"], an["in"][0], mid=200)
    RF.wire(f, o2["out"], an["in"][1], mid=200)
    RF.wire(f, o3["out"], an["in"][2], mid=206)
    f.t(an["out"][0] + 3, an["out"][1] + 3.2, "Out", size=9.5, anchor="start", weight="700")
    return bare(f.svg(), scale=2.0)


def fig_q14c_labelled():
    """Same circuit with the output of every gate written on it."""
    s = fig_q14c_circuit()
    extra = ('<text x="196" y="26" font-size="7.5" text-anchor="middle" fill="currentColor">B+C+D&#8242;</text>'
             '<text x="182" y="96" font-size="7" text-anchor="middle" fill="currentColor">A+C+D&#8242;</text>'
             '<text x="196" y="160" font-size="7.5" text-anchor="middle" fill="currentColor">C&#8242;+D</text>'
             '<text x="94" y="54" font-size="7.5" text-anchor="middle" fill="currentColor">D&#8242;</text>'
             '<text x="100" y="166" font-size="7.5" text-anchor="middle" fill="currentColor">C&#8242;</text>')
    return s.replace("</svg>", extra + "</svg>")


# ---------------------------------------------------------------- Q18, Q19
def fig_q18_list():
    """The list in the question: Start -> 22 -> 33 -> 44 -> 55 -> 66, with the
    link fields F1..F5 (F5 holds null)."""
    f = RL.Fig(380, 70)
    bw, bh, gap, x0, y = 46.0, 24.0, 22.0, 46.0, 34.0
    f.t(8, y + 4, "Start", size=9, anchor="start")
    f.arrow(32, y, x0 - 3, y, 1.2)
    for i, v in enumerate([22, 33, 44, 55, 66]):
        x = x0 + i * (bw + gap)
        f.rect(x, y - bh / 2, bw, bh, r=2.5, fill="#fff")
        f.line(x + bw * 0.58, y - bh / 2, x + bw * 0.58, y + bh / 2, 1.1)
        f.t(x + bw * 0.29, y + 3.6, str(v), size=10, weight="600")
        f.t(x + bw * 0.79, y + bh / 2 + 12, "F%d" % (i + 1), size=8)
        if i < 4:
            f.circ(x + bw * 0.79, y, 1.9, fill="currentColor", sw=0)
            f.arrow(x + bw * 0.79, y, x + bw + gap - 3, y, 1.2)
        else:
            f.t(x + bw * 0.79, y + 3.2, "&#8709;", size=10)
            f.t(x + bw * 0.79, y - bh / 2 - 4, "null", size=7.5)
    return bare(f.svg(), scale=2.0)


Q19_TREE = ("2", ("7", ("2", None, None), ("6", ("5", None, None), ("11", None, None))),
            ("5", None, ("9", ("4", None, None), None)))


def fig_q19_tree():
    return tree(Q19_TREE)
