"""Figures for the Mathematics pre-board 2013-14 (answers only; the paper prints no diagram)."""
import math
from svg import Fig

SHADE = "#9ec5f0"
BLUE, RED, GREEN, GREY = "#1f5fb3", "#c0392b", "#2b7a4b", "#888"


class Plot:
    """Cartesian plot: data (x, y) -> svg; draws axes with ticks."""
    def __init__(self, uid, xr, yr, W=460, H=380, pad=36):
        self.f = Fig(W, H, uid)
        self.xr, self.yr, self.W, self.H, self.pad = xr, yr, W, H, pad

    def X(self, x):
        a, b = self.xr
        return self.pad + (x - a) / (b - a) * (self.W - 2 * self.pad)

    def Y(self, y):
        a, b = self.yr
        return self.H - self.pad - (y - a) / (b - a) * (self.H - 2 * self.pad)

    def P(self, x, y):
        return f"{self.X(x):.1f},{self.Y(y):.1f}"

    def axes(self, xt=(), yt=(), xl="x", yl="y", tick_lab=True):
        f = self.f
        f.arrow(self.X(self.xr[0]), self.Y(0), self.X(self.xr[1]) + 8, self.Y(0), color="#333", w=1.2)
        f.arrow(self.X(0), self.Y(self.yr[0]), self.X(0), self.Y(self.yr[1]) - 8, color="#333", w=1.2)
        f.text(self.X(self.xr[1]) + 6, self.Y(0) + 18, xl, italic=True, size=15)
        f.text(self.X(0) - 12, self.Y(self.yr[1]) - 2, yl, italic=True, size=15)
        f.text(self.X(0) - 9, self.Y(0) + 15, "O", size=13)
        for v in xt:
            f.line(self.X(v), self.Y(0) - 3, self.X(v), self.Y(0) + 3, color="#333", w=1)
            if tick_lab:
                f.text(self.X(v), self.Y(0) + 15, str(v), size=11, color="#444")
        for v in yt:
            f.line(self.X(0) - 3, self.Y(v), self.X(0) + 3, self.Y(v), color="#333", w=1)
            if tick_lab:
                f.text(self.X(0) - 6, self.Y(v) + 4, str(v), size=11, color="#444", anchor="end")

    def curve(self, pts, color=BLUE, w=2, dash=None):
        d = "M " + " L ".join(self.P(x, y) for x, y in pts)
        self.f.path(d, color=color, w=w, dash=dash)

    def poly(self, pts, fill=SHADE):
        d = "M " + " L ".join(self.P(x, y) for x, y in pts) + " Z"
        self.f.path(d, color="none", w=0, fill=fill)

    def dot(self, x, y, label=None, dx=8, dy=-8, anchor="start", size=13, color="#111"):
        self.f.circle(self.X(x), self.Y(y), 3.2, color=color, fill=color)
        if label:
            self.f.text(self.X(x) + dx, self.Y(y) + dy, label, size=size, anchor=anchor, color=color)

    def label(self, x, y, s, **kw):
        self.f.text(self.X(x), self.Y(y), s, **kw)


def lin(fn, a, b, n=80):
    return [(a + (b - a) * i / n, fn(a + (b - a) * i / n)) for i in range(n + 1)]


def fig_area_parabola_line():
    """y^2 = 4x and y = 2x - 4 meet at (1,-2) and (4,4); area 9."""
    p = Plot("m1314-area", (-1.5, 7), (-4, 6))
    # shaded region: between x = y^2/4 (left) and x = (y+4)/2 (right), y in [-2, 4]
    ys = [-2 + 6 * i / 80 for i in range(81)]
    region = [(y * y / 4, y) for y in ys] + [((y + 4) / 2, y) for y in reversed(ys)]
    p.poly(region)
    p.axes(xt=[1, 2, 3, 4, 5, 6], yt=[-2, 2, 4])
    p.curve([(y * y / 4, y) for y in [-4 + 9.2 * i / 120 for i in range(121)] if y * y / 4 <= 7])
    p.curve(lin(lambda x: 2 * x - 4, 0.2, 5), color=RED)
    p.dot(1, -2, "B(1, −2)", dx=8, dy=14)
    p.dot(4, 4, "A(4, 4)", dx=10, dy=4)
    p.label(6.1, 4.3, "y² = 4x", size=14, color=BLUE, italic=True)
    p.label(4.4, 5.4, "y = 2x − 4", size=14, color=RED, italic=True, anchor="end")
    p.label(2.2, 1.6, "Area", size=13)
    return p.f.svg()


def fig_lpp_drinks():
    """min C = 10x + 4y; 4x + y >= 80, 2x + y >= 60, x, y >= 0. Feasible region unbounded, above both lines."""
    p = Plot("m1314-lpp", (-6, 52), (-8, 100), W=480, H=420)
    top = 98
    # region: above both lines, x>=0, y>=0 -> polygon clipped at y=top, x=50
    p.poly([(0, top), (0, 80), (10, 40), (30, 0), (50, 0), (50, top)])
    p.axes(xt=[10, 20, 30, 40], yt=[20, 40, 60, 80], xl="x", yl="y")
    p.curve(lin(lambda x: 80 - 4 * x, 0, 20), color=RED)
    p.curve(lin(lambda x: 60 - 2 * x, 0, 30), color=GREEN)
    p.curve(lin(lambda x: (260 - 10 * x) / 4, 0, 26), color=GREY, dash="5 4", w=1.4)
    p.dot(0, 80, "A(0, 80)", dx=8, dy=-6)
    p.dot(10, 40, "B(10, 40)", dx=10, dy=4)
    p.dot(30, 0, "C(30, 0)", dx=6, dy=-10)
    p.label(11, 27, "4x + y = 80", size=13, color=RED, italic=True, anchor="end")
    p.label(31, 14, "2x + y = 60", size=13, color=GREEN, italic=True, anchor="start")
    p.label(34, 70, "feasible region", size=14)
    p.label(34, 62, "(unbounded)", size=13)
    p.label(34, 86, "dashed: 10x + 4y = 260", size=12, color="#555", italic=True)
    return p.f.svg()


def fig_cone_in_sphere():
    """Cross-section: circle radius r, inscribed cone of height h = 4r/3 (drawn to scale)."""
    f = Fig(360, 340, "m1314-cone")
    cx, cy, R = 180, 160, 130
    h = 4 * R / 3
    vy = cy - R               # vertex at top
    by = vy + h               # base level
    rho = math.sqrt(h * (2 * R - h))
    f.circle(cx, cy, R, color=BLUE)
    f.path(f"M {cx} {vy} L {cx - rho:.1f} {by:.1f} L {cx + rho:.1f} {by:.1f} Z", color="#111", w=1.8, fill="#e8f0fb")
    f.line(cx, vy, cx, by, dash="4 3", w=1.2)
    f.circle(cx, cy, 3, fill="#111")
    f.text(cx + 8, cy - 4, "O", size=14, anchor="start")
    f.line(cx, cy, cx + rho, by, color=RED, w=1.4)
    f.text(cx + rho / 2 + 10, (cy + by) / 2 - 2, "r", italic=True, size=16, color=RED)
    f.text(cx - 5, (vy + cy) / 2, "r", italic=True, size=16, color=RED, anchor="end")
    f.line(cx, vy, cx, cy, color=RED, w=1.4)
    f.text(cx - 8, cy + (by - cy) / 2 + 5, "h − r", italic=True, size=15, anchor="end")
    f.text(cx + rho / 2, by + 26, "ρ (base radius)", italic=True, size=14)
    f.line(cx, by, cx + rho, by, color=GREEN, w=1.8)
    f.text(cx, vy - 8, "V", size=14)
    f.text(cx - 4, by + 17, "M", size=13, anchor="end")
    # height bracket on the left
    xb = cx - rho - 26
    f.line(xb, vy, xb, by, w=1)
    f.line(xb - 5, vy, xb + 5, vy, w=1)
    f.line(xb - 5, by, xb + 5, by, w=1)
    f.text(xb - 6, (vy + by) / 2, "h", italic=True, size=16, anchor="end")
    return f.svg()


def _tree(uid, root, branches, W=520, H=None):
    """branches: list of (edge label, node label, [(edge label, leaf label), ...])."""
    n_leaf = sum(len(b[2]) for b in branches)
    H = H or max(200, 46 * n_leaf + 30)
    f = Fig(W, H, uid)
    x0, x1, x2 = 30, 210, 410
    f.circle(x0, H / 2, 4, fill="#111")
    f.text(x0, H / 2 - 10, root, size=13)
    k = 0
    gap = (H - 30) / n_leaf
    for el, nl, leaves in branches:
        ys = [20 + gap * (k + i + 0.5) for i in range(len(leaves))]
        ym = sum(ys) / len(ys)
        f.line(x0, H / 2, x1, ym, w=1.4)
        f.text((x0 + x1) / 2, (H / 2 + ym) / 2 - 6, el, size=13, color=BLUE)
        f.circle(x1, ym, 3.5, fill="#111")
        f.text(x1, ym + 20 if ym > H / 2 + 1 else ym - 9, nl, size=13, anchor="middle")
        for (le, ll), yy in zip(leaves, ys):
            f.line(x1, ym, x2, yy, w=1.2)
            f.text((x1 + x2) / 2, (ym + yy) / 2 - 5, le, size=12, color=RED)
            f.text(x2 + 8, yy + 5, ll, size=13, anchor="start")
        k += len(leaves)
    return f.svg()


def fig_tree_transfer():
    return _tree("m1314-tree1", "", [
        ("5/8", "red moved", [("4/8", "green from Q"), ("4/8", "red from Q")]),
        ("3/8", "green moved", [("5/8", "green from Q"), ("3/8", "red from Q")]),
    ], H=230)


def fig_tree_bolts():
    return _tree("m1314-tree2", "", [
        ("0.25", "M₁", [("0.05", "defective"), ("0.95", "good")]),
        ("0.35", "M₂", [("0.04", "defective"), ("0.96", "good")]),
        ("0.40", "M₃", [("0.02", "defective"), ("0.98", "good")]),
    ], H=300)
