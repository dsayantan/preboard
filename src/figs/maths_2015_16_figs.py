"""Figures for the Mathematics pre-board 2015-16 (answers only; the paper prints no diagram)."""
from svg import Fig
from maths_2013_14_figs import Plot, lin, _tree, BLUE, RED, GREEN, GREY, SHADE


def fig_area_sideways_parabola():
    """x = 8 + 2y - y^2 (vertex (9,1)), the y-axis, y = -1 and y = 3; area 92/3."""
    p = Plot("m1516-area", (-2, 11), (-3, 5), W=460, H=360)
    ys = [-1 + 4 * i / 80 for i in range(81)]
    p.poly([(0, -1)] + [(8 + 2 * y - y * y, y) for y in ys] + [(0, 3)])
    p.axes(xt=[2, 4, 6, 8], yt=[-1, 1, 3])
    p.curve([(8 + 2 * y - y * y, y) for y in [-2.6 + 7.2 * i / 120 for i in range(121)]])
    p.curve([(0, -1), (10.5, -1)], color=RED, dash="6 4", w=1.4)
    p.curve([(0, 3), (10.5, 3)], color=RED, dash="6 4", w=1.4)
    p.dot(5, -1, "(5, −1)", dx=8, dy=16)
    p.dot(5, 3, "(5, 3)", dx=8, dy=-8)
    p.dot(9, 1, "V(9, 1)", dx=8, dy=-6)
    p.dot(8, 0, None)
    p.label(10.4, -1.35, "y = −1", size=13, color=RED, italic=True, anchor="end")
    p.label(10.4, 3.25, "y = 3", size=13, color=RED, italic=True, anchor="end")
    p.label(7.8, 4.45, "x = 8 + 2y − y²", size=14, color=BLUE, italic=True, anchor="start")
    p.label(3.2, 1.15, "Area", size=14)
    return p.f.svg()


def fig_lpp_nuts_bolts():
    """max Z = 2.5x + y; x + 3y <= 12, 3x + y <= 12, x, y >= 0. Feasible region OABC."""
    p = Plot("m1516-lpp", (-1, 13), (-1.4, 13), W=440, H=420)
    p.poly([(0, 0), (4, 0), (3, 3), (0, 4)])
    p.axes(xt=[2, 4, 6, 8, 10, 12], yt=[2, 4, 6, 8, 10, 12], xl="x", yl="y")
    p.curve(lin(lambda x: (12 - x) / 3, 0, 12), color=RED)
    p.curve(lin(lambda x: 12 - 3 * x, 0, 4), color=GREEN)
    p.curve(lin(lambda x: 10.5 - 2.5 * x, 0, 4.2), color=GREY, dash="5 4", w=1.4)
    p.dot(4, 0, "A(4, 0)", dx=6, dy=-10)
    p.dot(3, 3, "B(3, 3)", dx=10, dy=-4)
    p.dot(0, 4, "C(0, 4)", dx=-6, dy=-8, anchor="end")
    p.label(9.5, 1.4, "x + 3y = 12", size=13, color=RED, italic=True)
    p.label(1.7, 10.2, "3x + y = 12", size=13, color=GREEN, italic=True, anchor="start")
    p.label(5.8, 7.6, "dashed: 2.5x + y = 10.5", size=12, color="#555", italic=True, anchor="start")
    p.label(1.4, 1.4, "OABC", size=13)
    return p.f.svg()


def fig_open_box():
    """Open box, square base side x, height h (oblique sketch)."""
    f = Fig(340, 230, "m1516-box")
    x0, y0, s, hh, dx, dy = 70, 190, 160, 80, 60, -40
    front = [(x0, y0), (x0 + s, y0), (x0 + s, y0 - hh), (x0, y0 - hh)]
    f.path("M " + " L ".join(f"{a},{b}" for a, b in front) + " Z", fill="#e8f0fb")
    f.path(f"M {x0 + s},{y0} L {x0 + s + dx},{y0 + dy} L {x0 + s + dx},{y0 + dy - hh} L {x0 + s},{y0 - hh} Z", fill="#d6e4f7")
    # open top rim (back edges)
    f.line(x0, y0 - hh, x0 + dx, y0 + dy - hh)
    f.line(x0 + dx, y0 + dy - hh, x0 + s + dx, y0 + dy - hh)
    # hidden edges
    f.line(x0, y0, x0 + dx, y0 + dy, dash="4 3", w=1.1)
    f.line(x0 + dx, y0 + dy, x0 + s + dx, y0 + dy, dash="4 3", w=1.1)
    f.line(x0 + dx, y0 + dy, x0 + dx, y0 + dy - hh, dash="4 3", w=1.1)
    f.text(x0 + s / 2, y0 + 20, "x", italic=True, size=16)
    f.text(x0 + s + dx / 2 + 12, y0 + dy / 2 + 8, "x", italic=True, size=16, anchor="start")
    f.text(x0 - 10, y0 - hh / 2 + 5, "h", italic=True, size=16, anchor="end")
    f.text(x0 + s / 2 + 30, y0 + dy - hh - 10, "open top", size=13, color="#555")
    return f.svg()


def fig_tree_urns():
    return _tree("m1516-tree", "", [
        ("1/3", "Urn 1", [("4/10", "black"), ("6/10", "red")]),
        ("1/3", "Urn 2", [("6/8", "black"), ("2/8", "red")]),
        ("1/3", "Urn 3", [("8/9", "black"), ("1/9", "red")]),
    ], H=300)
