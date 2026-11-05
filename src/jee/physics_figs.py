"""Figures for the JEE Main mock tests — Physics.  Every fig_* returns an SVG string."""
import math
from svg import Fig
from physb_draw import dot, resistor, ray, convex_lens, mid_arrow, BLUE, RED, GREEN, GREY

__all__ = ["fig_jp_t1_zener", "fig_jp_t3_rails", "fig_jp_t3_lens_mirror"]


def _zener(f, x, yc):
    """Zener on a vertical wire, cathode (bent bar) at the top: reverse biased when the top is +."""
    s = 16
    f.raw(f'<path d="M {x-s/2} {yc+s/2} L {x} {yc-s/2} L {x+s/2} {yc+s/2} Z" fill="#111"/>')
    f.path(f"M {x-s/2-5} {yc-s/2+5} L {x-s/2} {yc-s/2} L {x+s/2} {yc-s/2} L {x+s/2+5} {yc-s/2-5}", w=2)


def fig_jp_t1_zener():
    """Zener regulator: 10 V supply, 200 ohm series resistor, 6 V Zener, 600 ohm load."""
    f = Fig(460, 220, "fig_jp_t1_zener")
    yt, yb = 50, 175
    xs, xz, xl = 50, 260, 380
    # supply (battery, long plate = + at top)
    f.line(xs, yt, xs, 100); f.line(xs, 122, xs, yb)
    f.line(xs - 14, 100, xs + 14, 100, w=2.2)        # long plate (+)
    f.line(xs - 7, 108, xs + 7, 108, w=3.4)          # short plate (-)
    f.line(xs - 14, 116, xs + 14, 116, w=2.2)
    f.line(xs - 7, 122, xs + 7, 122, w=3.4)
    f.text(xs - 22, 104, "+", size=15, bold=True, anchor="end")
    f.text(xs - 22, 128, "−", size=15, bold=True, anchor="end")
    f.text(xs + 22, 115, "10 V", size=14, anchor="start")
    # top rail with series resistor
    f.line(xs, yt, 100, yt)
    resistor(f, 100, yt, 210, yt, n=5, lead=8)
    f.text(155, yt - 14, "200 Ω", size=14)
    f.line(210, yt, xl, yt)
    f.line(xs, yb, xl, yb)
    # Zener, cathode up
    yc = (yt + yb) / 2
    f.line(xz, yt, xz, yc - 8); _zener(f, xz, yc); f.line(xz, yc + 8, xz, yb)
    f.text(xz - 16, yc - 4, "V", italic=True, size=14, sub="Z", anchor="end")
    f.text(xz - 16, yc + 14, "= 6 V", size=14, anchor="end")
    # load
    resistor(f, xl, yt, xl, yb, n=5)
    f.text(xl + 14, yc - 4, "R", italic=True, size=14, sub="L", anchor="start")
    f.text(xl + 14, yc + 14, "= 600 Ω", size=14, anchor="start")
    for x in (xz, xl):
        dot(f, x, yt); dot(f, x, yb)
    return f.svg()


def fig_jp_t3_rails():
    """Rod MN sliding on rails AB, CD (0.5 m apart) closed by R = 4 ohm, field into the page."""
    f = Fig(470, 210, "fig_jp_t3_rails")
    yt, yb = 50, 160
    xr, x0, x1 = 60, 60, 440
    # crosses for B into page
    for gx in range(110, 440, 50):
        for gy in (75, 135):
            f.line(gx - 5, gy - 5, gx + 5, gy + 5, color=GREY, w=1.2)
            f.line(gx - 5, gy + 5, gx + 5, gy - 5, color=GREY, w=1.2)
    f.text(190, 32, "field 0.2 T into page", size=13, italic=False, anchor="middle", color="#555")
    # rails
    f.line(x0, yt, x1, yt, w=2.2); f.line(x0, yb, x1, yb, w=2.2)
    f.text(x0 + 4, yt - 8, "A", size=14, anchor="start"); f.text(x1, yt - 8, "B", size=14, anchor="end")
    f.text(x0 + 4, yb + 20, "C", size=14, anchor="start"); f.text(x1, yb + 20, "D", size=14, anchor="end")
    # resistor across the left end
    resistor(f, xr, yt, xr, yb, n=5)
    f.text(xr - 12, (yt + yb) / 2 + 5, "R", italic=True, size=15, anchor="end")
    # rod MN
    xm = 300
    f.line(xm, yt - 12, xm, yb + 12, color=BLUE, w=4)
    f.text(xm + 8, yt - 14, "M", size=14, anchor="start", color=BLUE)
    f.text(xm + 8, yb + 26, "N", size=14, anchor="start", color=BLUE)
    f.arrow(xm + 12, (yt + yb) / 2, xm + 75, (yt + yb) / 2, color=RED, w=2)
    f.text(xm + 82, (yt + yb) / 2 + 5, "v", italic=True, size=15, anchor="start", color=RED)
    # separation
    f.line(185, yt + 4, 185, yb - 4, color="#555", w=1, dash="4 3")
    f.text(192, (yt + yb) / 2 + 5, "0.5 m", size=13, anchor="start", color="#555")
    return f.svg()


def fig_jp_t3_lens_mirror():
    """Object O 15 cm before a convex lens (f = 10 cm); convex mirror 20 cm behind the lens.
    The lens alone would image O at 30 cm, i.e. 10 cm behind the mirror, at the mirror's centre C,
    so the rays meet the mirror normally and retrace their path.  Scale 12 px per cm."""
    s = 12.0
    cy = 120
    xO = 40
    xL = xO + 15 * s          # lens
    xM = xL + 20 * s          # mirror pole
    xC = xL + 30 * s          # centre of curvature = lens image point
    R = xC - xM               # 10 cm
    f = Fig(int(xC + 50), 250, "fig_jp_t3_lens_mirror")
    f.line(15, cy, xC + 40, cy, color=GREY, w=1)
    convex_lens(f, xL, cy, 70)
    f.text(xL, cy - 80, "lens, f = 10 cm", size=13)
    # convex mirror: arc of circle centre C, radius R, bulging towards the lens
    a = math.radians(38)
    yA, yB = cy - R * math.sin(a), cy + R * math.sin(a)
    xA = xC - R * math.cos(a)
    f.path(f"M {xA:.1f} {yA:.1f} A {R:.1f} {R:.1f} 0 0 0 {xA:.1f} {yB:.1f}", w=2.4)
    for k in range(7):  # hatching on the back (silvered) side
        t = -a + 2 * a * k / 6
        px, py = xC - R * math.cos(t), cy + R * math.sin(t)
        f.line(px, py, px + 8, py + 4, color="#555", w=1)
    f.text(xM - 6, yA - 8, "convex mirror", size=13, anchor="start")
    # object
    dot(f, xO, cy, 4)
    f.text(xO, cy + 24, "O", size=14)
    dot(f, xC, cy, 3, color=GREEN)
    f.text(xC, cy + 22, "C (= I′)", size=13, color=GREEN)
    # two rays: O -> lens edge -> towards C, meeting the mirror normally
    for h in (-46, 46):
        yl = cy + h
        dx, dy = xC - xL, cy - yl
        L = math.hypot(dx, dy)
        px, py = xC - R * dx / L, cy - R * dy / L
        ray(f, [(xO, cy), (xL, yl), (px, py)], color=RED)
        f.line(px, py, xC, cy, color=RED, w=1, dash="4 3")
    # distances
    yd = 222
    for x1, x2, lab in ((xO, xL, "15 cm"), (xL, xM, "20 cm"), (xM, xC, "10 cm")):
        f.line(x1, yd, x2, yd, color="#555", w=1)
        f.line(x1, yd - 5, x1, yd + 5, color="#555", w=1); f.line(x2, yd - 5, x2, yd + 5, color="#555", w=1)
        f.text((x1 + x2) / 2, yd - 6, lab, size=12, color="#555")
    return f.svg()
