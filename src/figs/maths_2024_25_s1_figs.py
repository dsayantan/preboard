"""Figures for the Mathematics pre-board 2024-25, Set 1 (maths_2024_25_s1)."""
import math
from svg import Fig

BLUE, RED, GREEN, PURP, SHADE, GRID = "#1f4e8c", "#c0392b", "#1f7a3a", "#7a4ea3", "#cfe6ff", "#e6e6e6"


def _axes(f, X, Y, xmin, xmax, ymin, ymax, xl="x", yl="y"):
    f.arrow(X(xmin), Y(0), X(xmax), Y(0), w=1.2)
    f.arrow(X(0), Y(ymin), X(0), Y(ymax), w=1.2)
    f.text(X(xmax) - 2, Y(0) + 18, xl, italic=True, anchor="end")
    f.text(X(0) + 8, Y(ymax) + 12, yl, italic=True, anchor="start")


def _poly(X, Y, pts):
    return "M " + " L ".join(f"{X(u):.1f} {Y(v):.1f}" for u, v in pts)


# ------------------------------------------------------------------ Q1(vii)  y = |x|
def fig_q1vii_graph():
    f = Fig(400, 300, "fig_q1vii_graph")
    s, ox, oy = 40, 200, 175
    X = lambda u: ox + s * u
    Y = lambda v: oy - s * v
    for g in range(-4, 5):
        f.line(X(g), Y(-3.3), X(g), Y(3.8), color=GRID, w=0.8)
    for g in range(-3, 4):
        f.line(X(-4.4), Y(g), X(4.4), Y(g), color=GRID, w=0.8)
    _axes(f, X, Y, -4.5, 4.6, -3.4, 4.0, "X", "Y")
    f.text(X(-4.5) + 2, Y(0) + 18, "X′", italic=True, anchor="start")
    f.text(X(0) + 8, Y(-3.4) + 2, "Y′", italic=True, anchor="start")
    for g in (-3, -2, -1, 1, 2, 3, 4):
        f.text(X(g), Y(0) + 16, str(g).replace("-", "−"), size=11)
    for g in (-3, -2, -1, 1, 2, 3):
        f.text(X(0) - 6, Y(g) + 4, str(g).replace("-", "−"), size=11, anchor="end")
    f.arrow(X(0), Y(0), X(3.6), Y(3.6), color=BLUE, w=2)
    f.arrow(X(0), Y(0), X(-3.6), Y(3.6), color=BLUE, w=2)
    for (u, v, lab, dx, an) in ((1, 1, "(1, 1)", 8, "start"), (2, 2, "(2, 2)", 8, "start"),
                                (-1, 1, "(−1, 1)", -8, "end"), (-2, 2, "(−2, 2)", -8, "end")):
        f.circle(X(u), Y(v), 3.5, fill="#111")
        f.text(X(u) + dx, Y(v) + 14, lab, size=12, anchor=an, bold=True)
    f.circle(X(0), Y(0), 3.5, fill="#111")
    f.text(X(0) + 8, Y(0) + 32, "(0, 0)", size=11, anchor="start", bold=True)
    f.text(X(0) - 6, Y(0) + 16, "O", size=11, anchor="end")
    return f.svg()


# ------------------------------------------------------------------ Q1(xiv)  four graphs
def _panel_axes(f, cx, cy, w, h, label):
    f.arrow(cx - w / 2, cy, cx + w / 2, cy, w=1.1)
    f.arrow(cx, cy + h / 2, cx, cy - h / 2, w=1.1)
    f.text(cx + w / 2 - 2, cy + 16, "x", italic=True, size=12, anchor="end")
    f.text(cx + 6, cy - h / 2 + 10, "f(x)", italic=True, size=12, anchor="start")
    f.text(cx, cy + h / 2 + 20, label, size=13, bold=True)


def _q1xiv(name, line):
    f = Fig(640, 200, name)
    cy, w, h = 90, 130, 140
    cs = [80, 240, 400, 560]
    # (1) wave
    c = cs[0]
    _panel_axes(f, c, cy, w, h, "(1)")
    pts = [(c - 5 + 75 * i / 100 - 0, cy - 40 * math.sin(2 * math.pi * i / 100)) for i in range(101)]
    f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), color=BLUE, w=2)
    # (2) wiggle with cusp on the axis
    c = cs[1]
    _panel_axes(f, c, cy, w, h, "(2)")
    pts = []
    for i in range(101):
        u = -1 + 1.9 * i / 100            # -1..0.9; cusp on the vertical axis at u = 0
        v = 0.25 + 0.6 * math.sin(math.pi * abs(u) / (0.75 if u < 0 else 0.6))
        pts.append((c + 55 * u, cy - 40 * v))
    f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), color=BLUE, w=2)
    # (3) sideways S
    c = cs[2]
    _panel_axes(f, c, cy, w, h, "(3)")
    p3 = []
    for i in range(101):
        v = -1 + 2 * i / 100                      # y from -1 to 1
        u = 0.9 * math.sin(1.5 * math.pi * v)     # x = g(y): three crossings of x = 0
        p3.append((c + 45 * u + 5, cy - 50 * v))
    f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in p3), color=BLUE, w=2)
    if line:
        xv = c + 5 + 45 * 0.35
        f.line(xv, cy - 68, xv, cy + 68, color=RED, w=1.6, dash="6 4")
        f.text(xv + 4, cy + 66, "x = k", italic=True, size=11, color=RED, anchor="start")
        for (a, b), (a2, b2) in zip(p3, p3[1:]):
            if (a - xv) * (a2 - xv) < 0:
                yc = b + (xv - a) * (b2 - b) / (a2 - a)
                f.circle(xv, yc, 3.5, fill=RED, color=RED)
    # (4) cube-root-like curve
    c = cs[3]
    _panel_axes(f, c, cy, w, h, "(4)")
    p4 = []
    for i in range(101):
        u = -1 + 2 * i / 100
        v = math.copysign(abs(u) ** (1 / 3), u)
        p4.append((c + 55 * u, cy - 50 * v))
    f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in p4), color=BLUE, w=2)
    return f.svg()


def fig_q1xiv_graphs():
    return _q1xiv("fig_q1xiv_graphs", False)


def fig_q1xiv_ans():
    return _q1xiv("fig_q1xiv_ans", True)


# ------------------------------------------------------------------ Q2 (OR)  roller coaster
def _cubic(u):
    return (u + 9) * (u + 1) * (u - 3) / 27


def _q2or(name, ans):
    f = Fig(480, 300, name)
    sx, sy, ox, oy = 28, 30, 300, 190
    X = lambda u: ox + sx * u
    Y = lambda v: oy - sy * v
    if ans:
        for g in range(-10, 5, 2):
            f.line(X(g), Y(-2.2), X(g), Y(5.8), color=GRID, w=0.8)
    _axes(f, X, Y, -10.4, 5.6, -2.6, 6.0, "x", "y")
    pts = [(-9.8 + 13.4 * i / 200, _cubic(-9.8 + 13.4 * i / 200)) for i in range(201)]
    f.path(_poly(X, Y, pts), color=BLUE, w=2.2)
    if ans:
        for r in (-9, -1, 3):
            f.circle(X(r), Y(0), 3.5, fill="#111")
            f.text(X(r) + (4 if r != -1 else -4), Y(0) + 16, str(r).replace("-", "−"), size=12,
                   anchor="start" if r != -1 else "end")
        f.circle(X(0), Y(-1), 3.5, fill=RED, color=RED)
        f.text(X(0) - 8, Y(-1) + 18, "(0, −1)", size=12, color=RED, anchor="end", bold=True)
        f.text(X(-4.8), Y(5.4), "y = (x+9)(x+1)(x−3)/27", italic=True, size=13, color=BLUE)
    else:
        f.text(X(-5), Y(5.4), "path of the roller coaster", size=12, color="#555")
    f.text(X(0) - 6, Y(0) + 16, "O", size=12, anchor="end")
    return f.svg()


def fig_q2or_coaster():
    return _q2or("fig_q2or_coaster", False)


def fig_q2or_ans():
    return _q2or("fig_q2or_ans", True)


# ------------------------------------------------------------------ Q3  |sin x|
def fig_q3_abssin():
    f = Fig(480, 200, "fig_q3_abssin")
    sx, sy, ox, oy = 62, 90, 40, 150
    X = lambda u: ox + sx * u
    Y = lambda v: oy - sy * v
    pts = [(2 * math.pi * i / 200, abs(math.sin(2 * math.pi * i / 200))) for i in range(201)]
    f.path(_poly(X, Y, pts) + " Z", color="none", fill=SHADE)
    _axes(f, X, Y, -0.3, 6.9, -0.4, 1.45, "x", "y")
    f.path(_poly(X, Y, pts), color=BLUE, w=2.2)
    for u, lab in ((math.pi, "π"), (2 * math.pi, "2π"), (math.pi / 2, "π/2"), (3 * math.pi / 2, "3π/2")):
        f.text(X(u), Y(0) + 16, lab, size=12)
    f.text(X(0) - 6, Y(1) + 4, "1", size=12, anchor="end")
    f.line(X(0) - 3, Y(1), X(0) + 3, Y(1))
    f.text(X(math.pi / 2), Y(0.4), "2", size=15, bold=True)
    f.text(X(3 * math.pi / 2), Y(0.4), "2", size=15, bold=True)
    f.text(X(4.6) + 30, Y(1.25), "y = |sin x|", italic=True, size=13, color=BLUE, anchor="start")
    return f.svg()


# ------------------------------------------------------------------ Q4  sqrt x + sqrt y = 4
def fig_q4_tangent():
    f = Fig(400, 360, "fig_q4_tangent")
    s, ox, oy = 17, 50, 320
    X = lambda u: ox + s * u
    Y = lambda v: oy - s * v
    for g in (4, 8, 12, 16):
        f.line(X(g), Y(0), X(g), Y(17), color=GRID, w=0.8)
        f.line(X(0), Y(g), X(17), Y(g), color=GRID, w=0.8)
        f.text(X(g), Y(0) + 16, str(g), size=11)
        f.text(X(0) - 6, Y(g) + 4, str(g), size=11, anchor="end")
    _axes(f, X, Y, 0, 18.5, 0, 18.3, "x", "y")
    pts = [((4 * i / 100) ** 2, (4 - 4 * i / 100) ** 2) for i in range(101)]
    f.path(_poly(X, Y, pts), color=BLUE, w=2.2)
    f.line(X(0), Y(8), X(8), Y(0), color=RED, w=1.6)          # tangent x + y = 8
    f.line(X(0), Y(0), X(9.5), Y(9.5), color="#999", w=1, dash="4 4")
    f.circle(X(4), Y(4), 3.8, fill="#111")
    f.text(X(4) + 9, Y(4) - 5, "P(4, 4)", size=13, bold=True, anchor="start")
    f.text(X(8) + 16, Y(0) - 6, "45°", size=12, color=RED, anchor="start")
    f.text(X(1.2), Y(9.5), "tangent x + y = 8", italic=True, size=12, color=RED, anchor="start")
    f.text(X(6.5), Y(13.5), "√x + √y = 4", italic=True, size=13, color=BLUE, anchor="start")
    f.text(X(9.6) + 2, Y(9.5) - 2, "y = x", italic=True, size=11, color="#777", anchor="start")
    f.text(X(0) - 6, Y(0) + 16, "O", size=12, anchor="end")
    return f.svg()


# ------------------------------------------------------------------ Q9  growth f(x) = 2x^3 - 9x^2 + 12x + 1
def fig_q9_growth():
    f = Fig(460, 320, "fig_q9_growth")
    sx, sy, ox, oy = 120, 20, 60, 275
    X = lambda u: ox + sx * u
    Y = lambda v: oy - sy * v
    g = lambda u: 2 * u ** 3 - 9 * u ** 2 + 12 * u + 1
    f.raw(f'<rect x="{X(1)}" y="{Y(12.3)}" width="{X(2)-X(1)}" height="{Y(0)-Y(12.3)}" fill="#fde2dc"/>')
    for gx in (1, 2, 3):
        f.text(X(gx), Y(0) + 16, str(gx), size=12)
    for gy in (2, 4, 6, 8, 10):
        f.line(X(0) - 3, Y(gy), X(0) + 3, Y(gy))
        f.text(X(0) - 6, Y(gy) + 4, str(gy), size=11, anchor="end")
    _axes(f, X, Y, 0, 3.25, 0, 12.6, "x", "f(x)")
    pts = [(3.1 * i / 200, g(3.1 * i / 200)) for i in range(201)]
    f.path(_poly(X, Y, pts), color=BLUE, w=2.2)
    for (u, lab, dy) in ((1, "(1, 6) local max", -10), (2, "(2, 5) local min", 20)):
        f.circle(X(u), Y(g(u)), 3.5, fill="#111")
        f.line(X(u), Y(g(u)), X(u), Y(0), dash="4 3", w=1)
        f.text(X(u) + 6, Y(g(u)) + dy, lab, size=12, anchor="start", bold=True)
    f.circle(X(0), Y(1), 3, fill="#111")
    f.text(X(0) - 6, Y(1) + 4, "1", size=11, anchor="end")
    f.text(X(0.5), Y(10.5), "rising", size=13, color=GREEN, bold=True)
    f.text(X(1.5), Y(10.5), "falling", size=13, color=RED, bold=True)
    f.text(X(2.62), Y(10.5), "rising", size=13, color=GREEN, bold=True)
    f.text(X(0) - 6, Y(0) + 16, "O", size=12, anchor="end")
    return f.svg()


# ------------------------------------------------------------------ Q10  Bayes tree
def fig_q10_tree():
    f = Fig(520, 230, "fig_q10_tree")
    f.circle(40, 115, 4, fill="#111")
    rows = [("E₁: meditation & yoga", "1/2", "0.40 × 0.70 = 0.28", 55),
            ("E₂: drug", "1/2", "0.40 × 0.75 = 0.30", 175)]
    for name, p, q, yy in rows:
        f.line(44, 115, 170, yy, color=BLUE)
        f.text(100, (115 + yy) / 2 + (18 if yy > 115 else -8), p, size=13, color=BLUE)
        f.circle(174, yy, 4, fill="#111")
        f.text(166, yy + (-12 if yy < 115 else 22), name, size=12, anchor="end")
        f.line(178, yy, 300, yy - 18, color=RED)
        f.line(178, yy, 300, yy + 18, color="#888")
        f.text(306, yy - 14, "H: heart attack  " + q, size=12, anchor="start", color=RED)
        f.text(306, yy + 22, "no heart attack", size=12, anchor="start", color="#666")
    f.text(260, 225, "P(H) = ½(0.28) + ½(0.30) = 0.29", size=13)
    return f.svg()


# ------------------------------------------------------------------ Q13  swimmer
def _shore(f, x0, x1, y):
    f.line(x0, y, x1, y, w=2)
    for k in range(int(x0) + 4, int(x1), 14):
        f.line(k, y + 2, k - 5, y + 9, color="#7a6a4a", w=1)


def fig_q13_swim():
    f = Fig(440, 230, "fig_q13_swim")
    A, B, H, S = (80, 50), (205, 50), (380, 50), (55, 185)
    _shore(f, 30, 420, 50)
    for (yy, xs) in ((90, (120, 260, 330)), (130, (150, 240, 360)), (170, (130, 280, 390)), (205, (100, 220, 330))):
        for x0 in xs:
            f.line(x0, yy, x0 + 22, yy, color="#8fa9c8", w=1.2)
    f.line(*A, *S, w=1.4)
    f.arrow(S[0], S[1], B[0], B[1] + 2, color=BLUE, w=1.8, dash="6 4")
    f.arrow(B[0], B[1] - 4, H[0] - 6, H[1] - 4, color=GREEN, w=1.6)
    for (p, lab) in ((A, "A"), (B, "B"), (H, "H")):
        f.circle(p[0], p[1], 3.2, fill="#111")
        f.text(p[0], p[1] - 14, lab, size=15, bold=True)
    f.circle(S[0], S[1], 3.2, fill="#111")
    f.text(S[0] - 10, S[1] + 5, "S", size=15, bold=True, anchor="end")
    f.text(225, 225, "sea", size=12, color="#5a7aa8")
    f.text(30, 30, "shore", size=12, color="#7a6a4a", anchor="start")
    return f.svg()


def fig_q13_geometry():
    f = Fig(460, 250, "fig_q13_geometry")
    k = 80                                     # px per km
    ox, oy = 50, 60
    A = (ox, oy); S = (ox, oy + 2 * k); xB = 4 / math.sqrt(5)
    B = (ox + xB * k, oy); H = (ox + 4 * k, oy)
    _shore(f, 30, 420, oy)
    f.line(*A, *S, w=1.4)
    f.rect(A[0], A[1], 9, 9, w=1)
    f.line(*S, *B, color=BLUE, w=2)
    f.line(*B, *H, color=GREEN, w=2.4)
    for (p, lab) in ((A, "A"), (B, "B"), (H, "H")):
        f.circle(p[0], p[1], 3.2, fill="#111")
        f.text(p[0], p[1] - 12, lab, size=15, bold=True)
    f.circle(*S, 3.2, fill="#111")
    f.text(S[0] - 8, S[1] + 5, "S", size=15, bold=True, anchor="end")
    f.text(A[0] - 6, (A[1] + S[1]) / 2 + 4, "2 km", size=12, anchor="end")
    f.text((A[0] + B[0]) / 2, A[1] + 26, "x", italic=True, size=14)
    f.text((B[0] + H[0]) / 2, A[1] + 26, "4 − x", italic=True, size=14, color=GREEN)
    f.text((S[0] + B[0]) / 2 + 12, (S[1] + B[1]) / 2 + 14, "√(4 + x²)  swim at 4 km/h", size=12,
           color=BLUE, anchor="start")
    f.text((B[0] + H[0]) / 2, A[1] + 44, "walk at 6 km/h", size=12, color=GREEN)
    f.text(230, 240, "best landing: AB = x = 4/√5 ≈ 1.79 km", size=13)
    return f.svg()


# ------------------------------------------------------------------ Q13 (OR)  three cans
def _can(f, cx, top, bot, rx, ry=7):
    f.raw(f'<ellipse cx="{cx}" cy="{top}" rx="{rx}" ry="{ry}" fill="none" stroke="#555" stroke-width="1.4"/>')
    f.raw(f'<path d="M {cx-rx} {bot} A {rx} {ry} 0 0 0 {cx+rx} {bot}" fill="none" stroke="#555" stroke-width="1.4"/>')
    f.line(cx - rx, top, cx - rx, bot, color="#555", w=1.4)
    f.line(cx + rx, top, cx + rx, bot, color="#555", w=1.4)


def fig_q13or_cans():
    f = Fig(380, 200, "fig_q13or_cans")
    _can(f, 70, 75, 175, 45)
    _can(f, 190, 55, 175, 35)
    _can(f, 310, 22, 175, 27)
    f.text(190, 196, "closed cylinders, each of volume 432π cm³", size=12)
    return f.svg()


# ------------------------------------------------------------------ Q18  area
def fig_q18_area():
    f = Fig(400, 400, "fig_q18_area")
    sx, sy, ox, oy = 80, 26, 60, 350
    X = lambda u: ox + sx * u
    Y = lambda v: oy - sy * v
    top = [(3 * i / 120, (3 * i / 120) ** 2 + 2) for i in range(121)]
    region = top + [(3, 3), (0, 0)]
    f.path(_poly(X, Y, region) + " Z", color="none", fill=SHADE)
    for g in (1, 2, 3):
        f.text(X(g), Y(0) + 16, str(g), size=12)
    for g in (4, 6, 8, 10):
        f.line(X(0) - 3, Y(g), X(0) + 3, Y(g))
        f.text(X(0) - 6, Y(g) + 4, str(g), size=11, anchor="end")
    _axes(f, X, Y, -0.4, 3.9, -0.6, 12.8, "x", "y")
    f.path(_poly(X, Y, [(-0.4 + 3.75 * i / 120, (-0.4 + 3.75 * i / 120) ** 2 + 2) for i in range(121)]),
           color=BLUE, w=2.2)
    f.line(X(-0.4), Y(-0.4), X(3.7), Y(3.7), color=RED, w=2)
    f.line(X(3), Y(-0.4), X(3), Y(12.3), color=GREEN, w=1.6)
    for (u, v, lab, dx, an) in ((0, 2, "(0, 2)", 6, "start"), (3, 11, "(3, 11)", -8, "end"),
                                (3, 3, "(3, 3)", 8, "start")):
        f.circle(X(u), Y(v), 3.5, fill="#111")
        f.text(X(u) + dx, Y(v) + (4 if u == 3 and v == 3 else -6), lab, size=12, anchor=an, bold=True)
    f.text(X(1.15), Y(10.3), "y = x² + 2", italic=True, size=13, color=BLUE, anchor="start")
    f.text(X(3.08), Y(1.9), "y = x", italic=True, size=13, color=RED, anchor="start")
    f.text(X(3.08), Y(7), "x = 3", italic=True, size=13, color=GREEN, anchor="start")
    f.text(X(1.8), Y(3.6), "A = 21/2", size=14, bold=True)
    f.text(X(0) - 6, Y(0) + 16, "O", size=12, anchor="end")
    return f.svg()


# ------------------------------------------------------------------ Q22  LPP
def fig_q22_lpp():
    f = Fig(470, 420, "fig_q22_lpp")
    s, ox, oy = 3.4, 55, 370
    X = lambda u: ox + s * u
    Y = lambda v: oy - s * v
    reg = [(0, 0), (60, 0), (50, 20), (40, 30), (0, 50)]
    f.path(_poly(X, Y, reg) + " Z", color="none", fill=SHADE)
    for g in range(20, 120, 20):
        f.line(X(g), Y(0), X(g), Y(100), color=GRID, w=0.8)
        f.text(X(g), Y(0) + 16, str(g), size=11)
        f.line(X(0), Y(g), X(115), Y(g), color=GRID, w=0.8)
        f.text(X(0) - 6, Y(g) + 4, str(g), size=11, anchor="end")
    _axes(f, X, Y, 0, 118, 0, 104, "x", "y")
    f.line(X(0), Y(70), X(74), Y(-4), color=RED, w=1.8)             # x + y = 70
    f.line(X(0), Y(50), X(108), Y(-4), color=GREEN, w=1.8)          # x + 2y = 100
    f.line(X(10), Y(100), X(62), Y(-4), color=PURP, w=1.8)          # 2x + y = 120
    f.line(X(0), Y(410 / 7), X(82), Y(0), color="#555", w=1.2, dash="6 4")  # 5x + 7y = 410
    f.text(X(30), Y(43), "x + y = 70", italic=True, size=12, color=RED, anchor="start")
    f.text(X(80), Y(13.5), "x + 2y = 100", italic=True, size=12, color=GREEN, anchor="start")
    f.text(X(37), Y(84), "2x + y = 120", italic=True, size=12, color=PURP, anchor="start")
    for (u, v, lab, dx, dy, an) in ((0, 0, "O", -6, 16, "end"), (60, 0, "A(60, 0)", 4, 32, "middle"),
                                    (50, 20, "B(50, 20)", 10, 8, "start"), (40, 30, "C(40, 30)", 8, -6, "start"),
                                    (0, 50, "D(0, 50)", 8, -8, "start")):
        f.circle(X(u), Y(v), 3.5, fill="#111")
        f.text(X(u) + dx, Y(v) + dy, lab, size=12, anchor=an, bold=True)
    f.text(X(20), Y(18), "Feasible", size=13, bold=True)
    f.text(X(20), Y(18) + 16, "region", size=13, bold=True)
    return f.svg()
