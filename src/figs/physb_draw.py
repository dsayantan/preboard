"""Drawing primitives for the Physics 2015-16 / 2016-17 figure modules (agent B).
No fig_* functions here: this module is a helper only.
Conventions: y grows downward.  Long thin plate of a cell = positive terminal.
"""
import math
from svg import Fig

BLUE, RED, GREEN, GREY, ORANGE = "#1f4e9c", "#c0392b", "#1e7b34", "#888", "#b9770e"


def dot(f, x, y, r=3, color="#111"):
    f.circle(x, y, r, color=color, fill=color, w=1)


def resistor(f, x1, y1, x2, y2, n=6, amp=6, lead=None, color="#111"):
    """Zigzag between (x1,y1) and (x2,y2) with straight leads."""
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    nx, ny = -uy, ux
    lead = L * 0.2 if lead is None else lead
    pts = [(x1, y1), (x1 + ux * lead, y1 + uy * lead)]
    body = L - 2 * lead
    for i in range(1, 2 * n):
        t = lead + body * i / (2 * n)
        s = amp if i % 2 else -amp
        pts.append((x1 + ux * t + nx * s, y1 + uy * t + ny * s))
    pts += [(x2 - ux * lead, y2 - uy * lead), (x2, y2)]
    f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), color=color)


def cell_h(f, xc, y, plus_left=True, long=24, short=12, gap=7, w=2.2):
    """Cell on a horizontal wire; caller draws wire up to xc-gap/2 and from xc+gap/2."""
    xl, xr = xc - gap / 2, xc + gap / 2
    ll, lr = (long, short) if plus_left else (short, long)
    f.line(xl, y - ll / 2, xl, y + ll / 2, w=w)
    f.line(xr, y - lr / 2, xr, y + lr / 2, w=w + (1.2 if not plus_left else 1.2))


def cell_v(f, x, yc, plus_top=True, long=24, short=12, gap=7, w=2.2):
    yt, yb = yc - gap / 2, yc + gap / 2
    lt, lb = (long, short) if plus_top else (short, long)
    f.line(x - lt / 2, yt, x + lt / 2, yt, w=w)
    f.line(x - lb / 2, yb, x + lb / 2, yb, w=w)


def capacitor_h(f, xc, y, h=22, gap=8):
    f.line(xc - gap / 2, y - h / 2, xc - gap / 2, y + h / 2, w=2.2)
    f.line(xc + gap / 2, y - h / 2, xc + gap / 2, y + h / 2, w=2.2)


def capacitor_v(f, x, yc, w_=22, gap=8):
    f.line(x - w_ / 2, yc - gap / 2, x + w_ / 2, yc - gap / 2, w=2.2)
    f.line(x - w_ / 2, yc + gap / 2, x + w_ / 2, yc + gap / 2, w=2.2)


def inductor_h(f, x1, x2, y, n=5):
    r = (x2 - x1) / (2 * n)
    d = f"M {x1} {y}"
    for i in range(n):
        d += f" a {r} {r} 0 0 1 {2*r} 0"
    f.path(d)


def meter(f, cx, cy, label, r=13):
    f.circle(cx, cy, r, fill="#fff")
    f.text(cx, cy + 5, label, size=13, bold=True)


def ac_source(f, cx, cy, r=12):
    f.circle(cx, cy, r, fill="#fff")
    f.path(f"M {cx-7} {cy} q 3.5 -7 7 0 t 7 0")


def key(f, cx, cy):
    f.circle(cx, cy, 8, fill="#fff")
    dot(f, cx, cy, 2)
    f.text(cx, cy - 12, "K", size=12)


def diode_h(f, x, y, size=12, right=True, color="#111", fill="#111"):
    """Triangle pointing right (anode left) centred at x."""
    s = size
    if right:
        f.raw(f'<path d="M {x-s/2} {y-s/2} L {x+s/2} {y} L {x-s/2} {y+s/2} Z" fill="{fill}" stroke="{color}" stroke-width="1.4"/>')
        f.line(x + s / 2, y - s / 2, x + s / 2, y + s / 2, color=color, w=2)
    else:
        f.raw(f'<path d="M {x+s/2} {y-s/2} L {x-s/2} {y} L {x+s/2} {y+s/2} Z" fill="{fill}" stroke="{color}" stroke-width="1.4"/>')
        f.line(x - s / 2, y - s / 2, x - s / 2, y + s / 2, color=color, w=2)


def diode_v(f, x, y, size=12, up=True, color="#111"):
    s = size
    if up:   # arrow (conventional current) points up: cathode on top
        f.raw(f'<path d="M {x-s/2} {y+s/2} L {x} {y-s/2} L {x+s/2} {y+s/2} Z" fill="{color}" stroke="{color}" stroke-width="1.4"/>')
        f.line(x - s / 2, y - s / 2, x + s / 2, y - s / 2, color=color, w=2)
    else:
        f.raw(f'<path d="M {x-s/2} {y-s/2} L {x} {y+s/2} L {x+s/2} {y-s/2} Z" fill="{color}" stroke="{color}" stroke-width="1.4"/>')
        f.line(x - s / 2, y + s / 2, x + s / 2, y + s / 2, color=color, w=2)


def mid_arrow(f, x1, y1, x2, y2, color="#111", size=7):
    """Filled arrow head at the midpoint of a segment, pointing from 1 to 2."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    nx, ny = -uy, ux
    tip = (mx + ux * size / 2, my + uy * size / 2)
    b1 = (mx - ux * size / 2 + nx * size / 2.2, my - uy * size / 2 + ny * size / 2.2)
    b2 = (mx - ux * size / 2 - nx * size / 2.2, my - uy * size / 2 - ny * size / 2.2)
    f.raw(f'<path d="M {tip[0]:.1f} {tip[1]:.1f} L {b1[0]:.1f} {b1[1]:.1f} L {b2[0]:.1f} {b2[1]:.1f} Z" fill="{color}"/>')


def ray(f, pts, color=RED, w=1.4, dash=None, arrows=True):
    """Polyline ray; a mid-arrow on every segment."""
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        f.line(x1, y1, x2, y2, color=color, w=w, dash=dash)
        if arrows and math.hypot(x2 - x1, y2 - y1) > 25:
            mid_arrow(f, x1, y1, x2, y2, color=color)


def convex_lens(f, x, cy, h, t=10, color=BLUE):
    f.path(f"M {x} {cy-h} Q {x+t} {cy} {x} {cy+h} Q {x-t} {cy} {x} {cy-h} Z", color=color, fill="#e8f0fb", w=1.4)


def concave_lens(f, x, cy, h, t=10, color=BLUE):
    f.path(f"M {x-t} {cy-h} L {x+t} {cy-h} Q {x+2} {cy} {x+t} {cy+h} L {x-t} {cy+h} Q {x-2} {cy} {x-t} {cy-h} Z",
           color=color, fill="#e8f0fb", w=1.4)


def arrow_obj(f, x, y0, h, color="#111", w=2):
    """Object/image arrow standing on the axis at y0, height h (positive = upward)."""
    f.arrow(x, y0, x, y0 - h, color=color, w=w)


def axes(f, x0, y0, x1, y1, xl="", yl="", xsub=None, ysub=None):
    """Axes with origin (x0,y0); x-axis to x1, y-axis up to y1."""
    f.arrow(x0, y0, x1, y0)
    f.arrow(x0, y0, x0, y1)
    if xl:
        f.text(x1 - 4, y0 + 20, xl, italic=True, sub=xsub, anchor="end")
    if yl:
        f.text(x0 - 6, y1 + 6, yl, italic=True, sub=ysub, anchor="end")


def polyline(f, pts, color="#111", w=1.8, dash=None):
    f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), color=color, w=w, dash=dash)


def hatch_line(f, x1, y1, x2, y2, side=1, n=8, ln=7, color="#555"):
    """Short hatch marks along a line (for a mirror's back)."""
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    nx, ny = -uy * side, ux * side
    for i in range(n + 1):
        px, py = x1 + ux * L * i / n, y1 + uy * L * i / n
        f.line(px, py, px + (nx + ux) * ln * 0.7, py + (ny + uy) * ln * 0.7, color=color, w=1)


# ------------------------------------------------------------------ reusable composite drawings
def dipole_torque_pair(uid):
    """Two panels: dipole perpendicular to E (max torque) and parallel to E (zero torque)."""
    f = Fig(560, 230, uid)
    for k, (x0, title) in enumerate(((20, "(i) θ = 90°: τ = pE (maximum)"), (300, "(ii) θ = 0°: τ = 0 (stable)"))):
        for yy in (40, 80, 120, 160, 200):
            f.arrow(x0, yy, x0 + 240, yy, color=GREY, w=1.1)
        f.text(x0 + 232, 32, "E", italic=True, size=15, color=GREY)
        cx, cy = x0 + 120, 120
        if k == 0:
            p1, p2 = (cx, cy + 50), (cx, cy - 50)   # -q bottom, +q top : p upward, perpendicular to E
        else:
            p1, p2 = (cx - 55, cy), (cx + 55, cy)   # -q left, +q right : p along E
        f.line(*p1, *p2, w=2.4)
        f.circle(*p2, 9, fill="#fbe3e0", color=RED)
        f.text(p2[0], p2[1] + 5, "+", size=15, bold=True, color=RED)
        f.circle(*p1, 9, fill="#dde8f8", color=BLUE)
        f.text(p1[0], p1[1] + 5, "−", size=15, bold=True, color=BLUE)
        if k == 0:
            f.arrow(p2[0] + 12, p2[1], p2[0] + 60, p2[1], color=RED, w=2)
            f.text(p2[0] + 62, p2[1] - 6, "qE", size=13, color=RED, anchor="start")
            f.arrow(p1[0] - 12, p1[1], p1[0] - 60, p1[1], color=BLUE, w=2)
            f.text(p1[0] - 62, p1[1] - 6, "qE", size=13, color=BLUE, anchor="end")
            f.arrow(cx + 26, cy + 18, cx + 26, cy - 22, color=GREEN, w=2)
            f.text(cx + 32, cy, "p", italic=True, bold=True, color=GREEN, anchor="start")
        else:
            f.arrow(p2[0] + 12, p2[1], p2[0] + 50, p2[1], color=RED, w=2)
            f.text(p2[0] + 30, p2[1] - 10, "qE", size=13, color=RED)
            f.arrow(p1[0] - 12, p1[1], p1[0] - 50, p1[1], color=BLUE, w=2)
            f.text(p1[0] - 30, p1[1] - 10, "qE", size=13, color=BLUE)
            f.arrow(cx - 20, cy + 26, cx + 20, cy + 26, color=GREEN, w=2)
            f.text(cx, cy + 46, "p", italic=True, bold=True, color=GREEN)
        f.text(x0 + 120, 225, title, size=13)
    return f.svg()


def bohr_orbit(uid):
    f = Fig(380, 270, uid)
    cx, cy, r = 170, 135, 95
    f.circle(cx, cy, r, color=GREY, w=1.2)
    f.circle(cx, cy, 11, fill="#fbe3e0", color=RED)
    f.text(cx, cy + 5, "+e", size=11, color=RED, bold=True)
    ex, ey = cx + r * math.cos(math.radians(-30)), cy + r * math.sin(math.radians(-30))
    f.circle(ex, ey, 7, fill="#dde8f8", color=BLUE)
    f.text(ex + 10, ey - 8, "e", italic=True, anchor="start", sup="−")
    # radius drawn to the left
    f.line(cx - 11, cy, cx - r, cy, dash="4 3")
    f.text(cx - r / 2, cy - 6, "r", italic=True)
    # centripetal (electrostatic) force towards nucleus
    ux, uy = (cx - ex) / r, (cy - ey) / r
    f.arrow(ex + ux * 9, ey + uy * 9, ex + ux * 48, ey + uy * 48, color=RED, w=2)
    f.text(ex + ux * 30 + 4, ey + uy * 30 + 18, "F", italic=True, color=RED, anchor="start")
    # velocity: tangent, motion anticlockwise on the page
    a_ = math.radians(-30)
    tx, ty = math.sin(a_), -math.cos(a_)
    f.arrow(ex + tx * 9, ey + ty * 9, ex + tx * 55, ey + ty * 55, color=GREEN, w=2)
    f.text(ex + tx * 55 - 6, ey + ty * 55 - 6, "v", italic=True, color=GREEN, anchor="end")
    f.text(cx, cy + r + 22, "F = e²/(4πε₀r²) supplies the centripetal force mv²/r", size=12)
    return f.svg()


def microscope(uid, s=24.0, h0=8.0, fo=2.0, u=2.4, fe=5.0, D=25.0, label_values=False):
    """Compound microscope, final image at D.  Everything computed from the lens formula.
    s = px per cm horizontally; h0 = object height in px (vertical scale is separate)."""
    vo = 1 / (1 / fo - 1 / u)            # real-is-positive form for a convex lens, object real
    mo = vo / u
    ue = 1 / (1 / fe + 1 / D)            # object distance for eyepiece giving virtual image at D
    me = D / ue
    x_obj = -u
    x_img1 = vo
    x_eye = vo + ue
    x_fin = x_eye - D
    xmin, xmax = x_fin - 1.5, x_eye + fe + 2.5
    W = (xmax - xmin) * s
    h1 = h0 * mo
    h2 = h1 * me
    lo_h, le_h = max(h0 * 3.0, 30), max(h1 * 1.6, 40)
    cy = max(lo_h, le_h) + 26
    H = cy + h2 + 40
    f = Fig(round(W), round(H), uid)
    X = lambda xc: (xc - xmin) * s
    f.line(X(xmin + 0.2), cy, X(xmax - 0.2), cy, color=GREY, w=1)
    convex_lens(f, X(0), cy, lo_h, t=7)
    convex_lens(f, X(x_eye), cy, le_h, t=9)
    f.text(X(0), cy - lo_h - 6, "Objective", size=12, color=BLUE)
    f.text(X(x_eye), cy - le_h - 6, "Eyepiece", size=12, color=BLUE)
    for xx, lab in ((-fo, "Fₒ"), (fo, "Fₒ"), (x_eye - fe, "Fₑ"), (x_eye + fe, "Fₑ")):
        dot(f, X(xx), cy, 2.5)
        f.text(X(xx), cy + 16, lab, size=12, italic=True)
    # object (upright, above axis), image 1 (inverted, below), final (inverted, below, bigger)
    arrow_obj(f, X(x_obj), cy, h0, color="#111")
    f.text(X(x_obj) - 4, cy - h0 - 4, "AB", size=12, anchor="end")
    arrow_obj(f, X(x_img1), cy, -h1, color="#555")
    f.text(X(x_img1) + 4, cy + h1 + 12, "A′B′", size=12, anchor="start")
    arrow_obj(f, X(x_fin), cy, -h2, color=GREY, w=1.6)
    f.text(X(x_fin) - 4, cy + h2 + 14, "A″B″ (at D)", size=12, anchor="start")
    # objective rays from object tip (y = cy - h0)
    yt = cy - h0
    yi = cy + h1
    ray(f, [(X(x_obj), yt), (X(0), yt), (X(x_img1), yi)], color=RED)
    ray(f, [(X(x_obj), yt), (X(0), cy), (X(x_img1), yi)], color=RED)
    # eyepiece rays from image-1 tip: parallel ray and central ray
    ye_par = yi
    # parallel ray hits eyepiece at height yi, refracts through far focus x_eye+fe on axis
    x_f2 = x_eye + fe
    slope = (cy - ye_par) / ((x_f2 - x_eye) * s)
    xe_end = X(xmax - 0.4)
    ray(f, [(X(x_img1), yi), (X(x_eye), yi), (xe_end, yi + slope * (xe_end - X(x_eye)))], color=GREEN)
    # backward extension of the refracted parallel ray to the final image tip
    yfin = cy + h2
    f.line(X(x_eye), yi, X(x_fin), yfin, color=GREEN, dash="5 4", w=1.1)
    # central ray through eyepiece centre
    sl2 = (cy - yi) / ((x_eye - x_img1) * s)
    ray(f, [(X(x_img1), yi), (X(x_eye), cy), (xe_end, cy + sl2 * (xe_end - X(x_eye)))], color=GREEN)
    f.line(X(x_eye), cy, X(x_fin), yfin, color=GREEN, dash="5 4", w=1.1)
    # eye
    f.text(X(x_eye) + (xe_end - X(x_eye)) / 2, cy - le_h + 4, "to eye", size=12)
    # distance D marker
    yD = H - 14
    f.line(X(x_fin), yD, X(x_eye), yD, color=GREY, w=1)
    f.arrow(X(x_fin) + (X(x_eye) - X(x_fin)) / 2, yD, X(x_fin), yD, color=GREY, w=1)
    f.arrow(X(x_fin) + (X(x_eye) - X(x_fin)) / 2, yD, X(x_eye), yD, color=GREY, w=1)
    f.text((X(x_fin) + X(x_eye)) / 2, yD - 5, "D = 25 cm", size=12)
    return f.svg(), dict(vo=vo, mo=mo, ue=ue, me=me, x_fin=x_fin)


def arc(f, cx, cy, r, a1, a2, color="#111", w=1.2):
    """Small arc (|a2-a1| < 180) about (cx,cy); angles in degrees measured on screen (y down)."""
    d = (a2 - a1 + 540) % 360 - 180
    a2 = a1 + d
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    x2, y2 = cx + r * math.cos(math.radians(a2)), cy + r * math.sin(math.radians(a2))
    sweep = 1 if d > 0 else 0
    f.path(f"M {x1:.1f} {y1:.1f} A {r} {r} 0 0 {sweep} {x2:.1f} {y2:.1f}", color=color, w=w)


def ang(x1, y1, x2, y2):
    """Screen angle (deg) of the direction from point 1 to point 2."""
    return math.degrees(math.atan2(y2 - y1, x2 - x1))


def inductor_v(f, x, y1, y2, n=5, right=True):
    r = (y2 - y1) / (2 * n)
    sw = 1 if right else 0
    d = f"M {x} {y1}"
    for i in range(n):
        d += f" a {r} {r} 0 0 {sw} 0 {2*r}"
    f.path(d)


def parallel_pair(f, x1, y1, x2, y2, gap=11, frac=0.22, labels=("", ""), amp=5, n=4):
    """Two equal resistors in parallel between two points (along any direction)."""
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    nx, ny = -uy, ux
    a = (x1 + ux * L * frac, y1 + uy * L * frac)
    b = (x2 - ux * L * frac, y2 - uy * L * frac)
    f.line(x1, y1, *a)
    f.line(*b, x2, y2)
    for s in (1, -1):
        a1 = (a[0] + nx * gap * s, a[1] + ny * gap * s)
        b1 = (b[0] + nx * gap * s, b[1] + ny * gap * s)
        f.line(*a, *a1)
        f.line(*b, *b1)
        resistor(f, *a1, *b1, n=n, amp=amp, lead=6)
    return (nx, ny)
