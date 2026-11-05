"""Figures for the Mathematics pre-board 2016-17 (maths_2016_17)."""
import math
from svg import Fig


def _axes(f, X, Y, xmin, xmax, ymin, ymax, xl="x", yl="y"):
    f.arrow(X(xmin), Y(0), X(xmax), Y(0), w=1.2)
    f.arrow(X(0), Y(ymin), X(0), Y(ymax), w=1.2)
    f.text(X(xmax) - 4, Y(0) + (34 if " " in xl else 18), xl, italic=True, anchor="end")
    f.text(X(0) + 8, Y(ymax) + 10, yl, italic=True, anchor="start")


def fig_q6b_circle():
    """Main reading: y^2 = 2x - x^2 (circle centre (1,0), r = 1) and y = x."""
    f = Fig(420, 330, "fig_q6b_circle")
    s, ox, oy = 120, 70, 200
    X = lambda u: ox + s * u
    Y = lambda v: oy - s * v
    # shaded minor segment: from (0,0) up the circle to (1,1), back down the line
    pts = [(X(1 - math.cos(t)), Y(math.sin(t))) for t in [i * (math.pi / 2) / 40 for i in range(41)]]
    d = "M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts) + f" L {X(0):.1f} {Y(0):.1f} Z"
    f.path(d, color="none", fill="#9ecbff")
    _axes(f, X, Y, -0.4, 2.55, -1.15, 1.4)
    f.circle(X(1), Y(0), s, color="#1f4e8c", w=1.8)
    f.line(X(-0.3), Y(-0.3), X(1.35), Y(1.35), color="#c0392b", w=1.8)
    f.circle(X(1), Y(0), 2.5, fill="#111")
    f.text(X(1) + 4, Y(0) + 17, "C(1, 0)", size=12)
    f.circle(X(1), Y(1), 3, fill="#111")
    f.text(X(1) - 8, Y(1) - 10, "P(1, 1)", size=13, anchor="end")
    f.text(X(0) - 6, Y(0) - 7, "O", size=13, anchor="end")
    f.text(X(2) + 4, Y(0) + 17, "2", size=12, anchor="start")
    f.text(X(1.42), Y(1.42) + 2, "y = x", italic=True, size=13, color="#c0392b", anchor="start")
    f.text(X(1.78), Y(1.0), "y² = 2x − x²", italic=True, size=13, color="#1f4e8c", anchor="start")
    f.line(X(1), Y(0), X(1), Y(1), dash="4 3", w=1)
    return f.svg()


def fig_q6b_parabola():
    """Alternative reading: y = 2x - x^2 and y = x."""
    f = Fig(400, 290, "fig_q6b_parabola")
    s, ox, oy = 120, 70, 210
    X = lambda u: ox + s * u
    Y = lambda v: oy - s * v
    xs = [i / 40 for i in range(41)]
    d = "M " + " L ".join(f"{X(u):.1f} {Y(2*u - u*u):.1f}" for u in xs) + f" L {X(0):.1f} {Y(0):.1f} Z"
    f.path(d, color="none", fill="#9ecbff")
    _axes(f, X, Y, -0.4, 2.5, -0.55, 1.45)
    xs = [-0.2 + i * 2.4 / 80 for i in range(81)]
    f.path("M " + " L ".join(f"{X(u):.1f} {Y(2*u - u*u):.1f}" for u in xs), color="#1f4e8c", w=1.8)
    f.line(X(-0.3), Y(-0.3), X(1.3), Y(1.3), color="#c0392b", w=1.8)
    f.circle(X(1), Y(1), 3, fill="#111")
    f.text(X(1) - 8, Y(1) - 10, "(1, 1)", size=13, anchor="end")
    f.text(X(0) - 6, Y(0) - 7, "O", size=13, anchor="end")
    f.text(X(2) - 8, Y(0) + 17, "2", size=12, anchor="end")
    f.text(X(1.35), Y(1.35), "y = x", italic=True, size=13, color="#c0392b", anchor="start")
    f.text(X(1.75), Y(0.62), "y = 2x − x²", italic=True, size=13, color="#1f4e8c", anchor="start")
    return f.svg()


def fig_q13b_lpp():
    """2x + y >= 1000, x + 2y >= 800, x, y >= 0;  Z = 0.005x + 0.02y."""
    f = Fig(520, 420, "fig_q13b_lpp")
    s = 0.3  # px per gram
    ox, oy = 60, 370
    X = lambda u: ox + s * u
    Y = lambda v: oy - s * v
    xmax, ymax = 1350, 1150
    # feasible (unbounded) region, clipped to the drawing window
    reg = [(0, ymax), (0, 1000), (400, 200), (800, 0), (xmax, 0), (xmax, ymax)]
    f.path("M " + " L ".join(f"{X(u):.1f} {Y(v):.1f}" for u, v in reg) + " Z", color="none", fill="#cfe6ff")
    for g in range(200, 1400, 200):
        f.line(X(g), Y(0), X(g), Y(ymax), color="#e3e3e3", w=0.8)
        f.text(X(g), Y(0) + 16, str(g), size=11)
    for g in range(200, 1200, 200):
        f.line(X(0), Y(g), X(xmax), Y(g), color="#e3e3e3", w=0.8)
        f.text(X(0) - 6, Y(g) + 4, str(g), size=11, anchor="end")
    _axes(f, X, Y, 0, xmax + 60, 0, ymax + 70, "x (g wheat)", "y (g rice)")
    f.line(X(0), Y(1000), X(520), Y(-40), color="#c0392b", w=1.8)          # 2x + y = 1000
    f.line(X(0), Y(400), X(880), Y(-40), color="#1f7a3a", w=1.8)          # x + 2y = 800
    f.line(X(0), Y(200), X(800), Y(0), color="#7a4ea3", w=1.4, dash="6 4")  # Z = 4 iso-cost line x + 4y = 800
    f.text(X(130), Y(870) + 4, "2x + y = 1000", italic=True, size=12, color="#c0392b", anchor="start")
    f.raw(f'<text x="{X(620):.1f}" y="{Y(90)-9:.1f}" font-size="12" font-style="italic" fill="#1f7a3a" font-family="Times New Roman,serif" text-anchor="middle" transform="rotate(26.57 {X(620):.1f} {Y(90)-9:.1f})">x + 2y = 800</text>')
    f.raw(f'<text x="{X(180):.1f}" y="{Y(155)-5:.1f}" font-size="12" font-style="italic" fill="#7a4ea3" font-family="Times New Roman,serif" text-anchor="middle" transform="rotate(14.04 {X(180):.1f} {Y(155)-5:.1f})">Z = 4</text>')
    for (u, v, lab, dx, dy, an) in ((0, 1000, "A(0, 1000)", 8, -4, "start"), (400, 200, "B(400, 200)", 8, -8, "start"),
                                    (800, 0, "C(800, 0)", 6, -10, "start")):
        f.circle(X(u), Y(v), 3.5, fill="#111")
        f.text(X(u) + dx, Y(v) + dy, lab, size=12, anchor=an, bold=True)
    f.text(X(950), Y(800), "Feasible region", size=14, bold=True)
    f.text(X(950), Y(800) + 17, "(unbounded)", size=12)
    return f.svg()
