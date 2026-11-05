"""Figures for the Mathematics pre-board 2025-26 (maths_2025_26)."""
import math
from svg import Fig

BLUE, RED, GREEN, PURP, SHADE = "#1f4e8c", "#c0392b", "#1f7a3a", "#7a4ea3", "#cfe6ff"


def _axes(f, X, Y, xmin, xmax, ymin, ymax, xl="x", yl="y"):
    f.arrow(X(xmin), Y(0), X(xmax), Y(0), w=1.2)
    f.arrow(X(0), Y(ymin), X(0), Y(ymax), w=1.2)
    f.text(X(xmax) - 2, Y(0) + 18, xl, italic=True, anchor="end")
    f.text(X(0) + 8, Y(ymax) + 12, yl, italic=True, anchor="start")


def _poly(X, Y, pts):
    return "M " + " L ".join(f"{X(u):.1f} {Y(v):.1f}" for u, v in pts)


# ------------------------------------------------------------------ Q1(x)
def _curve_pts():
    pts = []
    for i in range(0, 121):
        u = -3.3 + 3.3 * i / 120
        if u < -2.1:
            v = -0.45 * math.sin(math.pi * (u + 2.1) / -1.6)   # dip of depth 0.45 centred at -2.9..-2.1
        else:
            v = 0.95 * math.sin(math.pi * (u + 2.1) / 2.1)
        pts.append((u, v))
    for i in range(1, 121):
        u = 2.9 * i / 120
        if u <= 0.9:
            v = 1.05 * math.sin(math.pi * u / 1.8) ** 0.6
        elif u <= 2.3:
            v = 0.35 + 0.7 * (0.5 + 0.5 * math.cos(math.pi * (u - 0.9) / 1.4))
        else:
            v = 0.35 + 0.35 * (u - 2.3) ** 1.3
        pts.append((u, v))
    return pts


def _q1x(name, line):
    f = Fig(440, 250, name)
    s, ox, oy = 62, 220, 160
    X = lambda u: ox + s * u
    Y = lambda v: oy - s * v
    _axes(f, X, Y, -3.3, 3.3, -1.3, 2.1, "x", "f(x)")
    f.path(_poly(X, Y, _curve_pts()), color=BLUE, w=2)
    f.text(X(0) - 8, Y(0) + 18, "O", italic=True, size=14, anchor="end")
    if line:
        k = 0.6
        f.line(X(-3.2), Y(k), X(3.2), Y(k), color=RED, w=1.5, dash="6 4")
        f.text(X(-3.2), Y(k) - 6, "y = k", italic=True, size=12, color=RED, anchor="start")
        pts = _curve_pts()
        for (u1, v1), (u2, v2) in zip(pts, pts[1:]):
            if (v1 - k) * (v2 - k) < 0:
                uc = u1 + (k - v1) * (u2 - u1) / (v2 - v1)
                f.circle(X(uc), Y(k), 3.5, fill=RED, color=RED)
    return f.svg()


def fig_q1x_curve():
    return _q1x("fig_q1x_curve", False)


def fig_q1x_ans():
    return _q1x("fig_q1x_ans", True)


# ------------------------------------------------------------------ Q10 Bayes tree
def fig_q10_tree():
    f = Fig(520, 270, "fig_q10_tree")
    f.circle(40, 135, 4, fill="#111")
    rows = [("A (offline)", "0.40", "0.20", 50), ("B (online)", "0.35", "0.30", 135), ("C (recorded)", "0.25", "0.50", 220)]
    for name, p, q, yy in rows:
        f.line(44, 135, 180, yy, color=BLUE)
        f.text(105, (135 + yy) / 2 + (16 if yy > 135 else -8), p, size=12, color=BLUE)
        f.circle(185, yy, 4, fill="#111")
        f.text(195, yy + 4, name, size=13, anchor="start")
        f.line(290, yy, 380, yy - 20, color=GREEN)
        f.line(290, yy, 380, yy + 20, color="#888")
        f.text(335, yy - 18, q, size=12, color=GREEN)
        f.text(386, yy - 16, "E: Excellent", size=12, anchor="start", color=GREEN)
        f.text(386, yy + 24, "not E", size=12, anchor="start", color="#666")
    f.text(260, 262, "P(E) = 0.08 + 0.105 + 0.125 = 0.31", size=13)
    return f.svg()


# ------------------------------------------------------------------ Q12 cylinder
def fig_q12_cylinder():
    f = Fig(300, 270, "fig_q12_cylinder")
    cx, top, bot, rx, ry = 150, 50, 215, 95, 22
    f.raw(f'<ellipse cx="{cx}" cy="{top}" rx="{rx}" ry="{ry}" fill="none" stroke="#111" stroke-width="1.6"/>')
    f.raw(f'<path d="M {cx-rx} {bot} A {rx} {ry} 0 0 0 {cx+rx} {bot}" fill="none" stroke="#111" stroke-width="1.6"/>')
    f.raw(f'<path d="M {cx-rx} {bot} A {rx} {ry} 0 0 1 {cx+rx} {bot}" fill="none" stroke="#111" stroke-width="1.2" stroke-dasharray="5 4"/>')
    f.line(cx - rx, top, cx - rx, bot)
    f.line(cx + rx, top, cx + rx, bot)
    f.line(cx, top, cx, bot, w=1.2, dash="5 4")
    f.line(cx, bot, cx + rx, bot, color=RED, w=1.6)
    f.text(cx + rx / 2, bot - 6, "r", italic=True, size=15, color=RED)
    f.text(cx + 8, (top + bot) / 2, "h", italic=True, size=15, anchor="start", color=BLUE)
    f.circle(cx, bot, 2.5, fill="#111")
    f.text(150, 262, "closed cylinder, V = 539/2 cubic units", size=12)
    return f.svg()


# ------------------------------------------------------------------ Q12 OR dolphin path
def fig_q12or_path():
    f = Fig(460, 300, "fig_q12or_path")
    sx, sy, ox, oy = 340, 170, 60, 250
    X = lambda u: ox + sx * u
    Y = lambda v: oy - sy * v
    _axes(f, X, Y, 0, 1.15, 0, 1.35, "t", "h(t)")
    h = lambda t: 0.5 * (-7 * t * t + 3 * t + 2)
    f.path(_poly(X, Y, [(i / 100, h(i / 100)) for i in range(101)]), color=BLUE, w=2)
    tm, hm = 3 / 14, 65 / 56
    f.line(X(tm), Y(0), X(tm), Y(hm), dash="4 3", w=1)
    f.line(X(0), Y(hm), X(tm), Y(hm), dash="4 3", w=1)
    f.circle(X(tm), Y(hm), 3.5, fill=RED, color=RED)
    f.text(X(tm) + 8, Y(hm) - 8, "max (3/14, 65/56)", size=12, anchor="start", color=RED)
    f.text(X(tm), Y(0) + 16, "3/14", size=12)
    f.text(X(0) - 6, Y(1) + 4, "1", size=12, anchor="end")
    f.circle(X(0), Y(1), 3, fill="#111")
    f.text(X(1), Y(0) + 16, "1", size=12)
    f.text(X(0) - 6, Y(0) + 16, "O", size=12, anchor="end")
    f.text(X(0.62), Y(0.95), "h(t) = ½(−7t² + 3t + 2)", italic=True, size=13, color=BLUE, anchor="start")
    f.text(X(0.1), Y(0.55), "rising", size=12, color=GREEN)
    f.text(X(0.85), Y(0.6), "falling", size=12, color=GREEN, anchor="start")
    return f.svg()


# ------------------------------------------------------------------ Q16 pyramid
def _q16(name, C, withG):
    f = Fig(360, 260, name)
    A, B, D = (170, 30), (60, 220), (300, 185)
    f.line(*A, *B); f.line(*A, *D); f.line(*B, *D)
    f.line(*A, *C, dash="5 4", w=1.3); f.line(*B, *C, dash="5 4", w=1.3); f.line(*C, *D, dash="5 4", w=1.3)
    if withG:   # letters only on the figure; coordinates in the caption line
        G = ((B[0] + C[0] + D[0]) / 3, (B[1] + C[1] + D[1]) / 3)
        f.line(*A, *G, color=RED, w=1.6)
        f.circle(*G, 3, fill=RED, color=RED)
        f.text(G[0] + 7, G[1] + 5, "G", italic=True, size=14, color=RED, anchor="start")
        f.text(A[0], A[1] - 8, "A", size=14)
        f.text(B[0] - 6, B[1] + 6, "B", size=14, anchor="end")
        f.text(C[0] + 7, C[1] - 2, "C", size=14, anchor="start")
        f.text(D[0] + 6, D[1] + 5, "D", size=14, anchor="start")
        f.text(180, 248, "A(0,1,2)  B(3,0,1)  C(4,3,6)  D(2,3,2)  G(3,2,3)", size=12)
        return f.svg()
    f.text(A[0], A[1] - 8, "A(0, 1, 2)", size=13)
    f.text(B[0] - 4, B[1] + 18, "B(3, 0, 1)", size=13)
    f.text(C[0] - 6, C[1] - 6, "C(4, 3, 6)", size=13, anchor="end")
    f.text(D[0] + 4, D[1] + 18, "D(2, 3, 2)", size=13, anchor="middle")
    return f.svg()


def fig_q16_pyramid():
    """As printed: C hidden almost directly below A; no G."""
    return _q16("fig_q16_pyramid", (175, 175), False)


def fig_q16_centroid():
    """Answer figure: C moved back-left so that AG is distinct from AC."""
    return _q16("fig_q16_centroid", (120, 150), True)


# ------------------------------------------------------------------ Q17 triangle on a line
def fig_q17_triangle():
    f = Fig(380, 230, "fig_q17_triangle")
    A, B, C, D = (190, 35), (110, 180), (265, 180), (190, 180)
    f.arrow(190, 185, 30, 185 - 0.0, w=1.4)
    f.arrow(190, 185, 350, 185, w=1.4)
    f.line(*A, B[0], 185); f.line(*A, C[0], 185)
    f.line(A[0], A[1], D[0], 185, dash="5 4", w=1.2)
    f.rect(D[0], 175, 10, 10, w=1)
    for (px, lab) in ((B[0], "B"), (D[0], "D"), (C[0], "C")):
        f.circle(px, 185, 3, fill="#111")
        f.text(px, 205, lab, size=13, bold=True)
    f.text(A[0], A[1] - 8, "A(0, 2, 3)", size=13, bold=True)
    f.text(187, 222, "line (x+3)/5 = (y−1)/2 = (z+4)/3,   BC = 5", size=12)
    return f.svg()


# ------------------------------------------------------------------ Q18 area
def fig_q18_area():
    f = Fig(440, 330, "fig_q18_area")
    sx, sy, ox, oy = 62, 18, 60, 140
    X = lambda u: ox + sx * u
    Y = lambda v: oy - sy * v
    yv = lambda u: u * (4 - u)
    up = [(i * 4 / 80, yv(i * 4 / 80)) for i in range(81)]
    f.path(_poly(X, Y, up) + " Z", color="none", fill=SHADE)
    dn = [(4 + i / 40, yv(4 + i / 40)) for i in range(41)]
    f.path(_poly(X, Y, dn) + f" L {X(5):.1f} {Y(0):.1f} Z", color="none", fill="#ffd6cc")
    _axes(f, X, Y, -0.6, 5.9, -6.3, 6.2)
    f.path(_poly(X, Y, [(-0.3 + i * 5.6 / 140, yv(-0.3 + i * 5.6 / 140)) for i in range(141)]), color=BLUE, w=2)
    f.line(X(5), Y(0), X(5), Y(-5), w=1.2)
    f.circle(X(2), Y(4), 3, fill="#111")
    f.line(X(2), Y(4), X(2), Y(0), dash="4 3", w=1)
    f.text(X(2) + 6, Y(4) - 8, "(2, 4)", size=12, anchor="start")
    f.text(X(4) - 6, Y(0) + 16, "4", size=12, anchor="end")
    f.text(X(5) + 5, Y(0) - 6, "5", size=12, anchor="start")
    f.circle(X(5), Y(-5), 3, fill="#111")
    f.text(X(5) + 6, Y(-5) + 4, "(5, −5)", size=12, anchor="start")
    f.text(X(0) - 6, Y(0) - 6, "O", size=12, anchor="end")
    f.text(X(2), Y(1.6), "32/3", size=14, bold=True)
    f.text(X(4.62), Y(-1.5), "7/3", size=13, bold=True)
    f.text(X(2.6), Y(-4.5), "y = x(4 − x)", italic=True, size=13, color=BLUE, anchor="end")
    return f.svg()


# ------------------------------------------------------------------ Q22 LPP (books)
def fig_q22_lpp():
    f = Fig(470, 420, "fig_q22_lpp")
    s, ox, oy = 14, 55, 370
    X = lambda u: ox + s * u
    Y = lambda v: oy - s * v
    reg = [(0, 0), (16, 0), (12, 6), (0, 14)]
    f.path(_poly(X, Y, reg) + " Z", color="none", fill=SHADE)
    for g in range(4, 28, 4):
        f.line(X(g), Y(0), X(g), Y(25), color="#e6e6e6", w=0.8)
        f.text(X(g), Y(0) + 16, str(g), size=11)
        f.line(X(0), Y(g), X(27), Y(g), color="#e6e6e6", w=0.8)
        f.text(X(0) - 6, Y(g) + 4, str(g), size=11, anchor="end")
    _axes(f, X, Y, 0, 28, 0, 26.5, "x", "y")
    f.line(X(0), Y(24), X(17.3), Y(-2), color=RED, w=1.8)          # 3x + 2y = 48
    f.line(X(0), Y(14), X(24), Y(-2), color=GREEN, w=1.8)          # 2x + 3y = 42
    f.line(X(0), Y(18), X(19.5), Y(-1.5), color=PURP, w=1.3, dash="6 4")  # x + y = 18
    f.text(X(4.2), Y(19), "3x + 2y = 48", italic=True, size=12, color=RED, anchor="start")
    f.text(X(17.5), Y(3.3), "2x + 3y = 42", italic=True, size=12, color=GREEN, anchor="start")
    f.text(X(19.7), Y(-1.5) + 12, "Z = 18", italic=True, size=12, color=PURP, anchor="start")
    for (u, v, lab, dx, dy, an) in ((0, 0, "O", -6, 16, "end"), (16, 0, "(16, 0)", -10, -6, "end"),
                                    (12, 6, "P(12, 6)", 8, -6, "start"), (0, 14, "(0, 14)", 8, -6, "start")):
        f.circle(X(u), Y(v), 3.5, fill="#111")
        f.text(X(u) + dx, Y(v) + dy, lab, size=12, anchor=an, bold=True)
    f.text(X(5.5), Y(5), "Feasible", size=13, bold=True)
    f.text(X(5.5), Y(5) + 16, "region", size=13, bold=True)
    return f.svg()


# ------------------------------------------------------------------ Q22 OR (given feasible region)
def _q22or(name, ans):
    f = Fig(470, 420, name)
    s, ox, oy = 6.4, 55, 370
    X = lambda u: ox + s * u
    Y = lambda v: oy - s * v
    reg = [(0, 0), (25, 0), (20, 10), (0, 20)]
    f.path(_poly(X, Y, reg) + " Z", color="none", fill="#d6d6d6" if not ans else SHADE)
    if ans:
        for g in range(10, 60, 10):
            f.line(X(g), Y(0), X(g), Y(54), color="#e6e6e6", w=0.8)
            f.text(X(g), Y(0) + 16, str(g), size=11)
            f.line(X(0), Y(g), X(58), Y(g), color="#e6e6e6", w=0.8)
            if g != 20:
                f.text(X(0) - 6, Y(g) + 4, str(g), size=11, anchor="end")
    _axes(f, X, Y, -5, 60, -5, 57, "X", "Y")
    f.line(X(-2), Y(54), X(29), Y(-8), w=1.8, color=RED if ans else "#111")     # 2x + y = 50
    f.line(X(-1), Y(20.5), X(52), Y(-6), w=1.8, color=GREEN if ans else "#111")   # x + 2y = 40
    lab = "B(20, 10)" if ans else "B"
    for (u, v, t, dx, dy, an) in ((0, 50, "D(0, 50)", 6, 4, "start"), (0, 20, "C(0, 20)", -8, -10, "end"),
                                  (20, 10, lab, 6, -8, "start"), (40, 0, "E(40, 0)", 2, -8, "middle"),
                                  (25, 0, "A(25, 0)", -6, -7, "end")):
        f.circle(X(u), Y(v), 3, fill="#111")
        f.text(X(u) + dx, Y(v) + dy, t, size=12, anchor=an, bold=True)
    if ans:
        f.line(X(0), Y(30), X(30), Y(0), color=PURP, w=1.3, dash="6 4")
        f.text(X(31), Y(5) , "z = 30", italic=True, size=12, color=PURP, anchor="start")
        f.text(X(18), Y(42), "2x + y = 50", italic=True, size=12, color=RED, anchor="start")
        f.text(X(37), Y(9), "x + 2y = 40", italic=True, size=12, color=GREEN, anchor="start")
    return f.svg()


def fig_q22or_region():
    return _q22or("fig_q22or_region", False)


def fig_q22or_ans():
    return _q22or("fig_q22or_ans", True)
