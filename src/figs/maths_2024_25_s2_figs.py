"""Figures for the Mathematics pre-board 2024-25, Set 2 (maths_2024_25_s2)."""
import math
from svg import Fig

BLUE, RED, GREEN, PURP, SHADE, GREY = "#1f4e8c", "#c0392b", "#1f7a3a", "#7a4ea3", "#cfe6ff", "#777"


def _axes(f, X, Y, xmin, xmax, ymin, ymax, xl="x", yl="y", w=1.2):
    f.arrow(X(xmin), Y(0), X(xmax), Y(0), w=w)
    f.arrow(X(0), Y(ymin), X(0), Y(ymax), w=w)
    f.text(X(xmax) - 2, Y(0) + 18, xl, italic=True, anchor="end")
    f.text(X(0) + 8, Y(ymax) + 12, yl, italic=True, anchor="start")


def _halo(f, x, y, txt, color, size=14):
    """Label sitting on a line: white halo so the line does not strike through it."""
    from html import escape
    f.raw(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" text-anchor="middle" fill="{color}" '
          f'stroke="#fff" stroke-width="5" paint-order="stroke" font-style="italic" font-weight="bold" '
          f'font-family="Times New Roman,serif">{escape(txt)}</text>')


def _poly(X, Y, pts):
    return "M " + " L ".join(f"{X(u):.1f} {Y(v):.1f}" for u, v in pts)


# ------------------------------------------------------------------ Q1(v): four graphs
def fig_q1v_graphs():
    """Four panels as printed: (a) jump, (b) hole, (c) infinite jump, (d) both sides -> -inf."""
    f = Fig(640, 520, "fig_q1v_graphs")

    def panel(px, py, letter, caption, draw):
        # local frame: origin at (px + 50, py + oy), x0 at local u = 150
        f.text(px + 6, py + 18, f"({letter})", size=15, anchor="start")
        draw(px, py)
        f.text(px + 150, py + 238, caption, size=13, italic=True)

    def ax(px, py, oy):
        f.arrow(px + 30, py + oy, px + 270, py + oy, w=1.1)
        f.arrow(px + 60, py + 222, px + 60, py + 25, w=1.1)
        f.text(px + 268, py + oy + 16, "x", italic=True, size=13)
        f.text(px + 68, py + 32, "y", italic=True, size=13, anchor="start")
        f.text(px + 54, py + oy + 16, "O", size=13, anchor="end")

    def a(px, py):
        oy = 190
        ax(px, py, oy)
        x0 = px + 200
        f.path(f"M {px+35} {py+70} Q {px+150} {py+75} {x0} {py+125}", color=BLUE, w=2)
        f.circle(x0, py + 125, 3.5, fill=BLUE, color=BLUE)
        f.path(f"M {x0} {py+160} Q {x0+20} {py+150} {x0+28} {py+110}", color=BLUE, w=2)
        f.circle(x0, py + 160, 3.5, fill="#fff", color=BLUE)
        f.line(x0, py + 125, x0, py + oy, dash="3 3", w=1, color=GREY)
        f.text(x0, py + oy + 16, "x₀", italic=True, size=13)

    def b(px, py):
        oy = 190
        ax(px, py, oy)
        x0 = px + 200
        pts = [(px + 35 + i * 2.2, py + 120 - 60 * ((i * 2.2) / 240) ** 3 * 2.2) for i in range(110)]
        # smooth: y decreases slightly then rises
        pts = []
        for i in range(0, 121):
            u = 35 + i * 2.0                       # 35 .. 275 local
            t = (u - 90) / 160
            v = 120 - 70 * max(t, 0) ** 2.4 + 6 * (min(t, 0)) ** 2
            pts.append((px + u, py + v))
        d = "M " + " L ".join(f"{a_:.1f} {b_:.1f}" for a_, b_ in pts if a_ < px + 268)
        f.path(d, color=BLUE, w=2)
        t = (200 - 90) / 160
        yh = py + 120 - 70 * t ** 2.4
        f.circle(x0, yh, 3.5, fill="#fff", color=BLUE)
        f.line(x0, yh + 4, x0, py + oy, dash="3 3", w=1, color=GREY)
        f.text(x0, py + oy + 16, "x₀", italic=True, size=13)

    def c(px, py):
        oy = 130
        ax(px, py, oy)
        x0 = px + 175
        f.line(x0, py + 30, x0, py + 222, dash="3 3", w=1, color=GREY)
        k = 260.0
        L = []
        for i in range(0, 400):
            u = 35 + i * 0.35                     # local x, up to x0 - 6
            gap = (x0 - px) - u
            if gap < 2.5:
                break
            v = oy + k / gap
            if v > 220:
                break
            L.append((px + u, py + v))
        f.path("M " + " L ".join(f"{a_:.1f} {b_:.1f}" for a_, b_ in L), color=BLUE, w=2)
        R = []
        for i in range(0, 400):
            u = (x0 - px) + 2.5 + i * 0.25
            if u > 255:
                break
            v = oy - k / (u - (x0 - px))
            if v < 32:
                continue
            R.append((px + u, py + v))
        f.path("M " + " L ".join(f"{a_:.1f} {b_:.1f}" for a_, b_ in R), color=BLUE, w=2)
        f.text(x0 + 10, py + oy + 18, "x₀", italic=True, size=13, anchor="start")

    def d(px, py):
        oy = 55
        f.arrow(px + 240, py + oy, px + 30, py + oy, w=1.1)
        ax(px, py, oy)
        x0 = px + 190
        f.line(x0, py + 30, x0, py + 222, dash="3 3", w=1, color=GREY)
        k = 1500.0
        L, R = [], []
        for i in range(0, 600):
            u = 62 + i * 0.25
            gap = (x0 - px) - u
            if gap < 2:
                break
            v = oy + k / gap - k / ((x0 - px) - 62)
            if v > 205:
                break
            L.append((px + u, py + v))
        for i in range(0, 600):
            u = 262 - i * 0.25
            gap = u - (x0 - px)
            if gap < 2:
                break
            v = oy + k / gap - k / (262 - (x0 - px))
            if v > 205:
                break
            R.append((px + u, py + v))
        f.path("M " + " L ".join(f"{a_:.1f} {b_:.1f}" for a_, b_ in L), color=BLUE, w=2, arrow=True)
        f.path("M " + " L ".join(f"{a_:.1f} {b_:.1f}" for a_, b_ in R), color=BLUE, w=2, arrow=True)
        f.text(x0 + 4, py + oy + 16, "x₀", italic=True, size=13, anchor="start")

    panel(0, 0, "a", "lim f(x) as x→x₀⁺  ≠  lim f(x) as x→x₀⁻", a)
    panel(320, 0, "b", "f(x) is not defined at x = x₀", b)
    panel(0, 260, "c", "f(x) is not continuous at x = x₀", c)
    panel(320, 260, "d", "f(x) is continuous at x = x₀", d)
    return f.svg()


# ------------------------------------------------------------------ Q5 horizontal tangent
def fig_q5_tangent():
    f = Fig(400, 300, "fig_q5_tangent")
    s, ox, oy = 48, 210, 120
    X = lambda u: ox + s * u
    Y = lambda v: oy - s * v * 0.75
    _axes(f, X, Y, -4.2, 3.5, -3, 2.9)
    yv = lambda u: u * u + 2 * u - 1
    pts = [(-3.6 + i * 5.4 / 120, yv(-3.6 + i * 5.4 / 120)) for i in range(121)]
    pts = [(u, v) for u, v in pts if v <= 2.6]
    f.path(_poly(X, Y, pts), color=BLUE, w=2)
    f.line(X(-3.2), Y(-2), X(1.4), Y(-2), color=RED, w=1.5, dash="6 4")
    f.circle(X(-1), Y(-2), 3.5, fill="#111")
    f.text(X(-1), Y(-2) + 20, "(−1, −2)", size=13, bold=True)
    f.text(X(1.5), Y(-2) + 4, "y = −2", italic=True, size=12, color=RED, anchor="start")
    f.text(X(0) - 6, Y(0) + 16, "O", size=12, anchor="end")
    f.text(X(1.25), Y(2.3), "y = x² + 2x − 1", italic=True, size=13, color=BLUE, anchor="start")
    return f.svg()


# ------------------------------------------------------------------ Q10 OR tree
def fig_q10or_tree():
    f = Fig(520, 250, "fig_q10or_tree")
    root = (40, 125)
    boxes = [("Box I", "1/3", "2/3", 45), ("Box II", "1/3", "3/5", 125), ("Box III", "1/3", "1/2", 205)]
    for name, pb, pe, y in boxes:
        f.line(root[0], root[1], 190, y, w=1.4)
        f.text(108, root[1] + (y - root[1]) * 68 / 150 + (16 if y > 125 else -7), pb, size=13, color=BLUE)
        f.text(200, y + 5, name, size=14, bold=True, anchor="start")
        f.line(265, y, 380, y, w=1.4)
        f.text(322, y - 7, pe, size=13, color=RED)
        f.text(388, y + 5, "1 W, 1 R", size=13, anchor="start")
    f.circle(*root, 4, fill="#111")
    f.text(260, 242, "P(one white and one red | box), drawing 2 without replacement", size=12, color=GREY)
    return f.svg()


# ------------------------------------------------------------------ Q11 window
def _window(name, labels):
    f = Fig(300, 260, name)
    L, R, T, B = 90, 210, 120, 220
    apex = ((L + R) / 2, T - (R - L) * math.sqrt(3) / 2)
    if labels:
        f.path(f"M {L} {T} L {L} {B} L {R} {B} L {R} {T}", w=1.8)
    else:
        f.rect(L, T, R - L, B - T, w=1.8)
    f.path(f"M {L} {T} L {apex[0]:.1f} {apex[1]:.1f} L {R} {T}", w=1.8)
    if labels:
        f.text((L + R) / 2, B + 20, "x", italic=True, size=15)
        f.text(L - 10, (T + B) / 2 + 5, "y", italic=True, size=15, anchor="end")
        f.text(R + 10, (T + B) / 2 + 5, "y", italic=True, size=15, anchor="start")
        f.text((L + apex[0]) / 2 - 10, (T + apex[1]) / 2, "x", italic=True, size=15, anchor="end")
        f.text((R + apex[0]) / 2 + 10, (T + apex[1]) / 2, "x", italic=True, size=15, anchor="start")
        f.line(L, T, R, T, dash="4 3", w=1, color=GREY)
        f.text((L + R) / 2, T + 18, "x", italic=True, size=13, color=GREY)
    return f.svg()


def fig_q11_window():
    return _window("fig_q11_window", False)


def fig_q11_window_ans():
    return _window("fig_q11_window_ans", True)


# ------------------------------------------------------------------ Q11 OR half cylinder
def fig_q11or_halfcyl():
    f = Fig(420, 230, "fig_q11or_halfcyl")
    r = 60
    dx, dy = 230, -95                      # receding direction of the length h
    A1, A2 = (40, 185), (40 + 2 * r, 185)   # front base edge (diameter)
    c1 = (40 + r, 185)
    # front semicircle
    f.path(f"M {A1[0]} {A1[1]} A {r} {r} 0 0 1 {A2[0]} {A2[1]}", w=1.6)
    f.line(*A1, *A2, w=1.6)
    # back semicircle (hidden part dashed)
    B1, B2 = (A1[0] + dx, A1[1] + dy), (A2[0] + dx, A2[1] + dy)
    f.path(f"M {B1[0]} {B1[1]} A {r} {r} 0 0 1 {B2[0]} {B2[1]}", w=1.6, dash="5 4")
    f.path(f"M {B1[0]+r*0.12:.1f} {B1[1]-r*0.48:.1f} A {r} {r} 0 0 1 {B2[0]} {B2[1]}", w=1.6)
    f.line(*B1, *B2, w=1.2, dash="5 4")
    # long edges
    f.line(*A2, *B2, w=1.6)                                  # right base edge
    f.line(*A1, *B1, w=1.2, dash="5 4")                     # left base edge (hidden)
    f.line(c1[0], c1[1] - r, c1[0] + dx, c1[1] - r + dy, w=1.6)   # top ridge
    # dimension h along the right base edge
    off = 14
    f.arrow((A2[0] + B2[0]) / 2 + off * 0.4, (A2[1] + B2[1]) / 2 + off, A2[0] + off * 0.4, A2[1] + off, w=1)
    f.arrow((A2[0] + B2[0]) / 2 + off * 0.4, (A2[1] + B2[1]) / 2 + off, B2[0] + off * 0.4, B2[1] + off, w=1)
    f.text((A2[0] + B2[0]) / 2 + 22, (A2[1] + B2[1]) / 2 + 24, "h", italic=True, size=15, bold=True)
    # dimension r on the front base (centre to right end)
    f.arrow(c1[0] + r / 2, A1[1] + 18, c1[0], A1[1] + 18, w=1)
    f.arrow(c1[0] + r / 2, A1[1] + 18, A2[0], A1[1] + 18, w=1)
    f.text(c1[0] + r / 2, A1[1] + 36, "r", italic=True, size=15, bold=True)
    f.circle(*c1, 2.5, fill="#111")
    return f.svg()


# ------------------------------------------------------------------ Q15(i) parallelogram
def fig_q15i_par():
    f = Fig(380, 200, "fig_q15i_par")
    O, A, B = (50, 160), (260, 160), (130, 50)
    C = (A[0] + B[0] - O[0], A[1] + B[1] - O[1])
    f.arrow(*O, *A, w=1.8, color=BLUE)
    f.arrow(*O, *B, w=1.8, color=BLUE)
    f.line(*A, *C, w=1.4)
    f.line(*B, *C, w=1.4)
    f.arrow(*O, *C, w=1.6, color=RED)
    f.arrow(*B, *A, w=1.6, color=GREEN)
    f.text((O[0] + A[0]) / 2, O[1] + 20, "a", italic=True, bold=True, size=15, color=BLUE)
    f.text((O[0] + B[0]) / 2 - 12, (O[1] + B[1]) / 2, "b", italic=True, bold=True, size=15, color=BLUE)
    _halo(f, O[0] + 0.72 * (C[0] - O[0]), O[1] + 0.72 * (C[1] - O[1]) + 5, "a + b", RED)
    _halo(f, B[0] + 0.25 * (A[0] - B[0]), B[1] + 0.25 * (A[1] - B[1]) + 5, "a − b", GREEN)
    f.text(O[0] - 6, O[1] + 4, "O", size=13, anchor="end")
    f.text(A[0] + 4, A[1] + 16, "A", size=13, anchor="start")
    f.text(B[0] - 6, B[1] - 4, "B", size=13, anchor="end")
    f.text(C[0] + 6, C[1] - 4, "C", size=13, anchor="start")
    return f.svg()


# ------------------------------------------------------------------ Q17 OR tower
def fig_q17or_tower():
    f = Fig(470, 300, "fig_q17or_tower")
    f.path("M 30 285 L 300 285 L 450 135 L 100 135 Z", w=1.4)
    P = (215, 25)
    pts = {"A": (115, 230), "Q": (215, 255), "C": (270, 220), "B": (310, 175)}
    for k, (u, v) in pts.items():
        f.line(P[0], P[1], u, v, w=1.6)
        f.circle(u, v, 2.5, fill="#111")
    f.circle(*P, 3, fill="#111")
    f.text(P[0], P[1] - 8, "P (2, 3, 1)", size=14)
    f.text(108, 252, "A (1, 0, 2)", size=13)
    f.text(207, 274, "Q (43/29, 77/29, 9/29)", size=13, anchor="end")
    f.text(278, 222, "C (1, 2, 1)", size=13, anchor="start")
    f.text(317, 178, "B (3, −1, 1)", size=13, anchor="start")
    return f.svg()


# ------------------------------------------------------------------ Q18 area between parabolas (a = 1/9)
def fig_q18_area():
    f = Fig(400, 380, "fig_q18_area")
    s, ox, oy = 28, 50, 335
    X = lambda u: ox + s * u
    Y = lambda v: oy - s * v
    up = [(i * 9 / 90, math.sqrt(9 * i * 9 / 90)) for i in range(91)]       # y = 3 sqrt x  (x = y^2/9)
    lo = [(9 - i * 9 / 90, (9 - i * 9 / 90) ** 2 / 9) for i in range(91)]   # y = x^2/9 back to O
    f.path(_poly(X, Y, up + lo) + " Z", color="none", fill=SHADE)
    for g in range(3, 12, 3):
        f.line(X(g), Y(0), X(g), Y(11), color="#e6e6e6", w=0.8)
        f.text(X(g), Y(0) + 16, str(g), size=11)
        f.line(X(0), Y(g), X(11.5), Y(g), color="#e6e6e6", w=0.8)
        f.text(X(0) - 6, Y(g) + 4, str(g), size=11, anchor="end")
    _axes(f, X, Y, -0.5, 12.3, -0.5, 11.8)
    f.path(_poly(X, Y, [(i * 10 / 100, (i * 10 / 100) ** 2 / 9) for i in range(101)]), color=BLUE, w=2)
    f.path(_poly(X, Y, [(i * 11.5 / 115, math.sqrt(i * 11.5 / 115 * 9)) for i in range(116)]), color=RED, w=2)
    f.circle(X(9), Y(9), 3.5, fill="#111")
    f.text(X(9) + 8, Y(9) + 14, "(9, 9)", size=12, bold=True, anchor="start")
    f.text(X(10.2), Y(11.4), "y = x²/9", italic=True, size=13, color=BLUE, anchor="end")
    f.text(X(11.8), Y(8.9), "x = y²/9", italic=True, size=13, color=RED, anchor="end")
    f.text(X(0) - 6, Y(0) + 16, "O", size=12, anchor="end")
    f.text(X(4.8), Y(4.2), "27", size=14, bold=True)
    return f.svg()


# ------------------------------------------------------------------ Q20 AC curve
def fig_q20_ac():
    f = Fig(450, 300, "fig_q20_ac")
    sx, sy, ox, oy = 26, 6, 50, 270
    X = lambda u: ox + sx * u
    Y = lambda v: oy - sy * v
    ac = lambda u: u + 5 + 36 / u
    pts = [(1.6 + i * 12.4 / 120, ac(1.6 + i * 12.4 / 120)) for i in range(121)]
    _axes(f, X, Y, -0.5, 14.5, -1, 43, "x", "AC")
    for g in (6, 12):
        f.text(X(g), Y(0) + 16, str(g), size=11)
    f.path(_poly(X, Y, pts), color=BLUE, w=2)
    f.circle(X(6), Y(17), 3.5, fill="#111")
    f.line(X(6), Y(17), X(6), Y(0), dash="4 3", w=1)
    f.line(X(6), Y(17), X(0), Y(17), dash="4 3", w=1)
    f.text(X(0) - 6, Y(17) + 4, "17", size=11, anchor="end")
    f.text(X(6) + 8, Y(17) + 22, "(6, 17)", size=12, bold=True, anchor="start")
    f.text(X(2.3), Y(36), "AC falls", size=12, color=RED, anchor="start")
    f.text(X(9.0), Y(13), "AC rises", size=12, color=GREEN, anchor="start")
    f.text(X(14.3), Y(26), "AC = x + 5 + 36/x", italic=True, size=13, color=BLUE, anchor="end")
    return f.svg()


# ------------------------------------------------------------------ Q22 LPP (soap)
def fig_q22_lpp():
    f = Fig(460, 360, "fig_q22_lpp")
    s, ox, oy = 26, 55, 320
    X = lambda u: ox + s * u
    Y = lambda v: oy - s * v
    reg = [(0, 0), (10, 0), (8, 2), (0, 6)]
    f.path(_poly(X, Y, reg) + " Z", color="none", fill=SHADE)
    for g in range(2, 15, 2):
        f.line(X(g), Y(0), X(g), Y(11), color="#e6e6e6", w=0.8)
        f.text(X(g), Y(0) + 16, str(g), size=11)
        if g <= 10:
            f.line(X(0), Y(g), X(14.5), Y(g), color="#e6e6e6", w=0.8)
            if g != 6:
                f.text(X(0) - 6, Y(g) + 4, str(g), size=11, anchor="end")
    _axes(f, X, Y, 0, 15, 0, 11.3, "x", "y")
    f.line(X(0), Y(6), X(13.5), Y(-0.75), color=RED, w=1.8)       # x + 2y = 12
    f.line(X(0), Y(10), X(11), Y(-1), color=GREEN, w=1.8)        # x + y = 10
    # Z = 32000 : 3x + 4y = 32 through (8,2): (0,8) .. (32/3, 0)
    f.line(X(3), Y(5.75), X(10.9), Y(-0.175), color=PURP, w=1.3, dash="6 4")
    f.text(X(10.6), Y(1.3), "x + 2y = 12", italic=True, size=12, color=RED, anchor="start")
    f.text(X(0.7), Y(10.0), "x + y = 10", italic=True, size=12, color=GREEN, anchor="start")
    f.text(X(2.9), Y(6.15), "Z = 32000", italic=True, size=12, color=PURP, anchor="end")
    for (u, v, lab, dx, dy, an) in ((0, 0, "O", -6, 16, "end"), (10, 0, "A(10, 0)", 0, 32, "middle"),
                                    (8, 2, "P(8, 2)", 8, -6, "start"), (0, 6, "C(0, 6)", -8, 4, "end")):
        f.circle(X(u), Y(v), 3.5, fill="#111")
        f.text(X(u) + dx, Y(v) + dy, lab, size=12, anchor=an, bold=True)
    f.text(X(3.6), Y(2.3), "Feasible region", size=13, bold=True)
    return f.svg()


# ------------------------------------------------------------------ Q14 distribution of S
def fig_q14_dist():
    f = Fig(380, 260, "fig_q14_dist")
    ox, oy, bw, sx, sy = 60, 220, 28, 70, 400
    X = lambda u: ox + 35 + sx * u
    Y = lambda v: oy - sy * v
    probs = [(0, "1/4", 0.25), (1, "3/8", 0.375), (2, "1/4", 0.25), (3, "1/8", 0.125)]
    for s_, lab, pv in probs:
        f.rect(X(s_) - bw / 2, Y(pv), bw, oy - Y(pv), fill=SHADE, color=BLUE, w=1.4)
        f.text(X(s_), Y(pv) - 6, lab, size=13, bold=True)
        f.text(X(s_), oy + 18, str(s_), size=13)
    f.arrow(ox, oy, 350, oy, w=1.2)
    f.arrow(ox, oy, ox, 25, w=1.2)
    f.text(345, oy + 18, "s", italic=True, size=14)
    f.text(ox + 6, 30, "P(S = s)", italic=True, size=13, anchor="start")
    xm = X(1.25)
    f.line(xm, oy, xm, Y(0.43), color=RED, w=1.4, dash="5 4")
    f.text(xm + 4, Y(0.45), "E(S) = 5/4", size=12, color=RED, anchor="start")
    return f.svg()
