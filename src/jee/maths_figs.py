"""Figures for the JEE Main mock tests — Mathematics (solutions only).

Each is drawn to scale with the Plot helper of the 2013-14 figure module.
"""
from maths_2013_14_figs import Plot, lin, SHADE, BLUE, RED, GREEN

ORANGE = "#d35400"


# ---------------------------------------------------------------- Test 1: y^2 = x and y = x - 2
def fig_jt1_area():
    p = Plot("fig_jt1_area", (-1, 5.2), (-1.8, 2.8), W=460, H=330)
    # region: for y in [-1, 2], x from y^2 to y+2
    left = [(y * y, y) for y in [-1 + 3 * i / 60 for i in range(61)]]
    right = [(y + 2, y) for y in [2 - 3 * i / 60 for i in range(61)]]
    p.poly(left + right)
    p.axes(xt=(1, 2, 3, 4), yt=(-1, 1, 2))
    p.curve([(y * y, y) for y in [-1.6 + 3.85 * i / 100 for i in range(101)]], color=BLUE)
    p.curve([(x, x - 2) for x in (0.3, 4.8)], color=RED)
    p.dot(4, 2, "(4, 2)", dx=-10, dy=-10, anchor="end")
    p.dot(1, -1, "(1, −1)", dx=-8, dy=16, anchor="end")
    p.label(1.6, 1.75, "y² = x", italic=True, size=13, color=BLUE, anchor="end")
    p.label(4.75, 1.85, "y = x − 2", italic=True, size=13, color=RED, anchor="start")
    p.label(1.7, 0.5, "9/2", bold=True, size=14)
    return p.f.svg()


# ---------------------------------------------------------------- Test 1: LPP, Z = 3x + 5y
def fig_jt1_lpp():
    p = Plot("fig_jt1_lpp", (-6, 78), (-6, 78), W=440, H=430, pad=40)
    p.poly([(0, 0), (60, 0), (50, 20), (40, 30), (0, 50)])
    p.axes(xt=(20, 40, 60), yt=(20, 40, 60))
    p.curve([(0, 70), (70, 0)], color=BLUE, w=1.6)
    p.curve([(0, 50), (76, 12)], color=RED, w=1.6)
    p.curve([(60, 0), (21, 78)], color=GREEN, w=1.6)
    p.label(8, 69, "x + y = 70", size=12, color=BLUE, anchor="start")
    p.label(63, 25, "x + 2y = 100", size=12, color=RED, anchor="start")
    p.label(30, 72, "2x + y = 120", size=12, color=GREEN, anchor="start")
    p.dot(60, 0, "(60, 0)", dx=-8, dy=28, anchor="end", size=11)
    p.dot(50, 20, "(50, 20)", dx=-8, dy=14, anchor="end", size=11)
    p.dot(40, 30, "(40, 30)", dx=-6, dy=16, anchor="end", size=11, color=ORANGE)
    p.dot(0, 50, "(0, 50)", dx=8, dy=-6, size=11)
    p.label(18, 14, "feasible", size=13)
    return p.f.svg()


# ---------------------------------------------------------------- Test 2: x = 3 + 2y - y^2, y from -1 to 3
def fig_jt2_area():
    p = Plot("fig_jt2_area", (-1.2, 5.2), (-1.8, 3.8), W=420, H=360)
    g = lambda y: 3 + 2 * y - y * y
    p.poly([(g(y), y) for y in [-1 + 4 * i / 80 for i in range(81)]] + [(0, 3), (0, -1)])
    p.axes(xt=(1, 2, 3, 4), yt=(-1, 1, 2, 3))
    p.curve([(g(y), y) for y in [-1.5 + 5 * i / 100 for i in range(101)]], color=BLUE)
    p.dot(4, 1, "(4, 1)", dx=8, dy=4)
    p.dot(0, 3, "(0, 3)", dx=8, dy=-6)
    p.dot(0, -1, "(0, −1)", dx=8, dy=14)
    p.label(4.4, 2.6, "x = 3 + 2y − y²", italic=True, size=13, color=BLUE)
    p.label(1.6, 0.9, "32/3", bold=True, size=14)
    return p.f.svg()


# ---------------------------------------------------------------- Test 2: LPP, Z = 3x + 2y
def fig_jt2_lpp():
    p = Plot("fig_jt2_lpp", (-4, 46), (-4, 56), W=420, H=440, pad=40)
    p.poly([(0, 0), (25, 0), (20, 10), (0, 20)])
    p.axes(xt=(10, 20, 40), yt=(10, 20, 30, 40, 50))
    p.curve([(0, 50), (27.5, -5)], color=BLUE, w=1.6)
    p.curve([(0, 20), (44, -2)], color=RED, w=1.6)
    p.label(4, 48, "2x + y = 50", size=12, color=BLUE, anchor="start")
    p.label(30, 7, "x + 2y = 40", size=12, color=RED, anchor="start")
    p.dot(25, 0, "(25, 0)", dx=8, dy=14, size=11)
    p.dot(20, 10, "(20, 10)", dx=8, dy=-6, size=11, color=ORANGE)
    p.dot(0, 20, "(0, 20)", dx=8, dy=-8, size=11)
    p.label(8, 6, "feasible", size=13)
    return p.f.svg()


# ---------------------------------------------------------------- Test 3: y = x(3 - x), 0 <= x <= 4
def fig_jt3_area():
    p = Plot("fig_jt3_area", (-0.8, 4.8), (-4.8, 3.2), W=440, H=380)
    y = lambda x: x * (3 - x)
    p.poly(lin(y, 0, 3) + [(3, 0)])
    p.poly(lin(y, 3, 4) + [(4, 0)], fill="#ffd6cc")
    p.axes(xt=(1, 2, 3), yt=(-4, -2, 2))
    p.curve(lin(y, -0.4, 4.3, 120), color=BLUE)
    p.f.line(p.X(4), p.Y(0), p.X(4), p.Y(-4), w=1.2, dash="4 3")
    p.dot(4, -4, "(4, −4)", dx=8, dy=4)
    p.dot(1.5, 2.25, "(3/2, 9/4)", dx=8, dy=-6)
    p.label(1.5, 0.8, "9/2", bold=True, size=14)
    p.label(3.62, -1.0, "11/6", bold=True, size=13)
    p.label(2.6, -3.3, "y = x(3 − x)", italic=True, size=13, color=BLUE, anchor="end")
    return p.f.svg()


# ---------------------------------------------------------------- Test 3: LPP, Z = 5x + 4y
def fig_jt3_lpp():
    p = Plot("fig_jt3_lpp", (-1.2, 14), (-1.2, 14), W=420, H=420, pad=40)
    p.poly([(0, 0), (4, 0), (3, 3), (0, 4)])
    p.axes(xt=(2, 4, 6, 8, 10, 12), yt=(2, 6, 8, 10, 12))
    p.curve([(0, 4), (13.5, -0.5)], color=BLUE, w=1.6)
    p.curve([(4, 0), (-0.4, 13.2)], color=RED, w=1.6)
    p.label(7.5, 2.2, "x + 3y = 12", size=12, color=BLUE, anchor="start")
    p.label(1.2, 11.5, "3x + y = 12", size=12, color=RED, anchor="start")
    p.dot(4, 0, "(4, 0)", dx=8, dy=-8, size=11)
    p.dot(3, 3, "(3, 3)", dx=8, dy=-6, size=11, color=ORANGE)
    p.dot(0, 4, "(0, 4)", dx=-8, dy=-6, anchor="end", size=11)
    p.label(1.4, 1.2, "feasible", size=12)
    return p.f.svg()
