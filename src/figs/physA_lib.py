"""Drawing helpers shared by physics_2013_14_figs.py and physics_2014_15_figs.py (agent A).

No fig_* functions here, so preview.py has nothing to render in this module.
"""
import math
from svg import Fig

BLUE, RED, GREEN, GREY, ORANGE = "#1f5fbf", "#c0392b", "#1e8449", "#777777", "#d35400"


def resistor(f, x1, y1, x2, y2, n=6, amp=6, lead=None, color="#111", w=1.6):
    """Zig-zag resistor between two points (any orientation)."""
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    px, py = -uy, ux
    zl = min(L * 0.6, 12 * n) if lead is None else L - 2 * lead
    a = (L - zl) / 2
    pts = [(x1, y1), (x1 + ux * a, y1 + uy * a)]
    for k in range(2 * n):
        s = a + zl * (k + 0.5) / (2 * n)
        sg = amp if k % 2 == 0 else -amp
        pts.append((x1 + ux * s + px * sg, y1 + uy * s + py * sg))
    pts.append((x1 + ux * (L - a), y1 + uy * (L - a)))
    pts.append((x2, y2))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    f.path(d, color=color, w=w)


def cell(f, x, y, horizontal=True, plus_first=True, gap=6, long=22, short=12, color="#111"):
    """Cell symbol centred at (x, y).  For a horizontal wire the plates are vertical.
    plus_first: the long (+) plate is on the left (horizontal) / top (vertical)."""
    a, b = (long, short) if plus_first else (short, long)
    if horizontal:
        f.line(x - gap / 2, y - a / 2, x - gap / 2, y + a / 2, color=color, w=2)
        f.line(x + gap / 2, y - b / 2, x + gap / 2, y + b / 2, color=color, w=3.2 if b == short else 2)
    else:
        f.line(x - a / 2, y - gap / 2, x + a / 2, y - gap / 2, color=color, w=2)
        f.line(x - b / 2, y + gap / 2, x + b / 2, y + gap / 2, color=color, w=3.2 if b == short else 2)


def capacitor(f, x, y, horizontal=True, gap=7, plate=24, color="#111"):
    if horizontal:
        f.line(x - gap / 2, y - plate / 2, x - gap / 2, y + plate / 2, color=color, w=2.2)
        f.line(x + gap / 2, y - plate / 2, x + gap / 2, y + plate / 2, color=color, w=2.2)
    else:
        f.line(x - plate / 2, y - gap / 2, x + plate / 2, y - gap / 2, color=color, w=2.2)
        f.line(x - plate / 2, y + gap / 2, x + plate / 2, y + gap / 2, color=color, w=2.2)


def dot(f, x, y, r=3, color="#111"):
    f.circle(x, y, r, color=color, fill=color, w=1)


def cross(f, x, y, s=4, color="#555"):
    """Symbol for a field into the page."""
    f.line(x - s, y - s, x + s, y + s, color=color, w=1.2)
    f.line(x - s, y + s, x + s, y - s, color=color, w=1.2)


def acsource(f, x, y, r=11, color="#111"):
    f.circle(x, y, r, color=color, fill="#fff")
    f.path(f"M {x-7} {y} C {x-4} {y-8}, {x-1} {y-8}, {x} {y} S {x+4} {y+8}, {x+7} {y}", color=color, w=1.4)


def arc(f, cx, cy, r, a1, a2, color="#111", w=1.2):
    """Arc of radius r round (cx, cy) between math-angles a1, a2 (degrees, y up, counter-clockwise
    positive), always the smaller of the two arcs."""
    d = (a2 - a1 + 540) % 360 - 180      # into (-180, 180]
    b = a1 + d
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
    x2, y2 = cx + r * math.cos(math.radians(b)), cy - r * math.sin(math.radians(b))
    sweep = 0 if d > 0 else 1
    f.path(f"M {x1:.1f} {y1:.1f} A {r} {r} 0 0 {sweep} {x2:.1f} {y2:.1f}", color=color, w=w)


def ang(x1, y1, x2, y2):
    """math-angle (degrees, y up) of the direction from point 1 to point 2 in SVG coordinates."""
    return math.degrees(math.atan2(-(y2 - y1), x2 - x1))


def axes(f, ox, oy, w, h, xlab, ylab, xl_sub=None, yl_sub=None, color="#111"):
    f.arrow(ox, oy, ox + w, oy, color=color)
    f.arrow(ox, oy, ox, oy - h, color=color)
    f.text(ox + w - 4, oy + 22, xlab, size=14, anchor="end", italic=True, sub=xl_sub)
    f.text(ox + 6, oy - h + 4, ylab, size=14, anchor="start", italic=True, sub=yl_sub)


def lens(f, x, y, h, bulge=9, color=BLUE, fill="#e8f1fb", concave=False):
    """Thin convex lens symbol (biconvex outline) centred at (x, y), height 2h."""
    if not concave:
        f.path(f"M {x} {y-h} Q {x+2*bulge} {y} {x} {y+h} Q {x-2*bulge} {y} {x} {y-h} Z", color=color, w=1.4, fill=fill)
    else:
        f.path(f"M {x-bulge} {y-h} L {x+bulge} {y-h} Q {x} {y} {x+bulge} {y+h} L {x-bulge} {y+h} Q {x} {y} {x-bulge} {y-h} Z",
               color=color, w=1.4, fill=fill)


def object_arrow(f, x, y0, y1, color="#111", w=2.2):
    f.arrow(x, y0, x, y1, color=color, w=w)
