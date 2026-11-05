"""Figures for Physics Pre-Board 2025-26 (theory, physics_2025_26) and practical (physics_2025_26_prac).
y grows downward.  Long thin plate of a cell = positive terminal."""
import math
from svg import Fig

BLUE, RED, GREEN, GREY, ORANGE = "#1f4e9c", "#c0392b", "#1e7b34", "#888", "#b9770e"


# ----------------------------------------------------------------- helpers
def _dot(f, x, y, r=3, color="#111"):
    f.circle(x, y, r, color=color, fill=color, w=1)


def _res(f, x1, y1, x2, y2, n=6, amp=6, color="#111"):
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    nx, ny = -uy, ux
    lead = L * 0.15
    pts = [(x1, y1), (x1 + ux * lead, y1 + uy * lead)]
    body = L - 2 * lead
    for i in range(1, 2 * n):
        t = lead + body * i / (2 * n)
        s = amp if i % 2 else -amp
        pts.append((x1 + ux * t + nx * s, y1 + uy * t + ny * s))
    pts += [(x2 - ux * lead, y2 - uy * lead), (x2, y2)]
    f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), color=color)


def _cap_h(f, xc, y, h=22, gap=8):
    """capacitor on a horizontal wire; wire must stop at xc±gap/2"""
    f.line(xc - gap / 2, y - h / 2, xc - gap / 2, y + h / 2, w=2.4)
    f.line(xc + gap / 2, y - h / 2, xc + gap / 2, y + h / 2, w=2.4)


def _cell_h(f, xc, y, plus_left=True, gap=7):
    xl, xr = xc - gap / 2, xc + gap / 2
    ll, lr = (26, 12) if plus_left else (12, 26)
    f.line(xl, y - ll / 2, xl, y + ll / 2, w=2.2)
    f.line(xr, y - lr / 2, xr, y + lr / 2, w=3.2 if plus_left else 2.2)


def _meter(f, x, y, letter, r=13):
    f.circle(x, y, r, fill="#fff")
    f.text(x, y + 5, letter, size=14, bold=True)


def _axes(f, ox, oy, x2, y2, xlab, ylab, x1=None, y1=None):
    """axes with origin (ox,oy); x axis to x2, y axis up to y2."""
    f.arrow(ox if x1 is None else x1, oy, x2, oy)
    f.arrow(ox, oy if y1 is None else y1, ox, y2)
    f.text(x2 - 2, oy + 20, xlab, size=14, italic=True, anchor="end")
    f.text(ox - 6, y2 - 4, ylab, size=14, italic=True, anchor="end")


def _arc(f, cx, cy, r, a1, a2, color="#111", w=1.2):
    """arc from angle a1 to a2 (degrees, maths sense, y up) -- always the minor arc."""
    d = (a2 - a1 + 180) % 360 - 180
    a2 = a1 + d
    p1 = (cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1)))
    p2 = (cx + r * math.cos(math.radians(a2)), cy - r * math.sin(math.radians(a2)))
    sweep = 0 if d > 0 else 1
    f.path(f"M {p1[0]:.1f} {p1[1]:.1f} A {r} {r} 0 0 {sweep} {p2[0]:.1f} {p2[1]:.1f}", color=color, w=w)


def _vtext(f, x, y, s, size=13):
    f.raw(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="middle" fill="#111" '
          f'font-family="Arial,sans-serif" transform="rotate(-90 {x} {y})">{s}</text>')


def _lens(f, x, y, h, color=BLUE, bulge=8):
    f.path(f"M {x} {y-h} Q {x+2*bulge} {y} {x} {y+h} Q {x-2*bulge} {y} {x} {y-h} Z", color=color, fill="#e8f1fb")


def _diode(f, x1, x2, y, color="#111"):
    """diode on a horizontal wire from x1 to x2, pointing right (anode left, cathode right)."""
    xm = (x1 + x2) / 2
    f.line(x1, y, xm - 10, y, color=color)
    f.path(f"M {xm-10} {y-11} L {xm-10} {y+11} L {xm+8} {y} Z", color=color, fill=color)
    f.line(xm + 8, y - 11, xm + 8, y + 11, color=color, w=2.4)
    f.line(xm + 8, y, x2, y, color=color)


def _coil_v(f, x, y1, y2, n, right=True, color="#111"):
    r = (y2 - y1) / (2 * n)
    sweep = 1 if right else 0
    d = f"M {x} {y1}"
    for _ in range(n):
        d += f" a {r:.2f} {r:.2f} 0 0 {sweep} 0 {2*r:.2f}"
    f.path(d, color=color)


# ----------------------------------------------------------------- QUESTION figures
def fig_q1a6_photo():
    """Q1(A)(vi): the four options, redrawn."""
    f = Fig(560, 330, "fig_q1a6_photo")
    panels = [("(a)", 20, 10), ("(b)", 290, 10), ("(c)", 20, 170), ("(d)", 290, 170)]
    for lab, X, Y in panels:
        f.rect(X, Y, 250, 150, color=RED, w=1.4)
        f.text(X + 18, Y + 26, lab, size=14)
        ox, oy = X + 70, Y + 115
        f.line(ox, oy, X + 238, oy)
        f.line(ox, oy, ox, Y + 15)
        f.text(X + 154, oy + 22, "INTENSITY OF LIGHT", size=10, bold=True, italic=True)
        _vtext(f, ox - 22, Y + 65, "PHOTOELECTRIC", size=8)
        _vtext(f, ox - 12, Y + 65, "CURRENT", size=8)
    # (a) linear rise then saturation
    f.path("M 90 125 L 160 55 L 255 55", color="#222", w=2)
    # (b) concave-up, rising steeply
    f.path("M 360 125 C 430 125 460 110 470 40", color="#222", w=2)
    # (c) falling line to zero
    f.path("M 90 195 L 190 285", color="#222", w=2)
    # (d) straight line through origin
    f.path("M 360 285 L 530 207", color="#222", w=2)
    return f.svg()


def fig_q2_vx():
    f = Fig(400, 170, "fig_q2_vx")
    ox, oy, s = 60, 130, 90
    _axes(f, ox, oy, 380, 20, "x", "V")
    f.path(f"M {ox} {oy} L {ox+s} {oy-80} L {ox+2*s} {oy-80} L {ox+3*s} {oy}", color=BLUE, w=2.2)
    f.line(ox + s, oy - 80, ox + s, oy, color=BLUE, w=1.4)
    f.line(ox + 2 * s, oy - 80, ox + 2 * s, oy, color=BLUE, w=1.4)
    for i, t in enumerate(["0", "1", "2", "3"]):
        f.text(ox + i * s + (8 if i == 0 else 0), oy + 20, t, size=13, bold=True)
    return f.svg()


def fig_q8_em():
    """Q8: schematic redraw of the two photographs."""
    f = Fig(560, 240, "fig_q8_em")
    f.rect(5, 5, 550, 230, color="#334", w=1.4)
    # fig-1: greenhouse
    f.circle(55, 40, 18, color=ORANGE, fill="#fde9b8")
    f.path("M 40 200 L 40 120 L 140 75 L 240 120 L 240 200 Z", color="#556", fill="#eef4f7")
    for x in (80, 120, 160, 200):
        f.line(x, 200, x, 120 - (x - 40) * 0 if False else 120, color="#99a", w=0.8)
    f.line(40, 200, 240, 200, color="#556")
    for (x1, y1, x2, y2) in ((70, 55, 110, 150), (90, 45, 150, 165), (60, 70, 90, 175)):
        f.path(_wavy(x1, y1, x2, y2, 4, 6), color=ORANGE, w=1.4, arrow=True)
    # long-wave radiation re-emitted inside, reflected back by glass
    f.path(_wavy(150, 185, 185, 110, 4, 5), color=RED, w=1.4, arrow=True)
    f.path(_wavy(185, 112, 215, 180, 3, 5), color=RED, w=1.4, arrow=True)
    f.path(_wavy(210, 120, 250, 40, 4, 5), color=RED, w=1.0, arrow=True, dash="3 2")
    f.text(140, 225, "fig-1", size=13)
    # fig-2: welder
    f.circle(340, 95, 22, color="#333", fill="#d9c7b0")       # head
    f.rect(350, 80, 22, 30, color="#111", fill="#222", rx=3)  # dark visor
    f.path("M 330 117 L 315 190 L 380 190 L 365 117 Z", color="#333", fill="#c9d3dc")  # body
    f.line(365, 140, 420, 160, color="#333", w=3)              # arm + torch
    f.line(420, 160, 445, 170, color="#555", w=4)
    # arc and sparks
    ax, ay = 452, 174
    for a in range(0, 360, 30):
        r1, r2 = 6, 26 + (a % 60) / 3
        f.line(ax + r1 * math.cos(math.radians(a)), ay + r1 * math.sin(math.radians(a)),
               ax + r2 * math.cos(math.radians(a)), ay + r2 * math.sin(math.radians(a)), color=ORANGE, w=1.3)
    f.circle(ax, ay, 5, color=ORANGE, fill="#fff6c8")
    f.path("M 400 205 L 545 185 L 545 215 L 400 230 Z", color="#555", fill="#9aa3ab")  # pipe
    f.text(430, 225, "fig-2", size=13)
    return f.svg()


def _wavy(x1, y1, x2, y2, n, a):
    L = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / L, (y2 - y1) / L
    nx, ny = -uy, ux
    pts = []
    for i in range(0, 8 * n + 1):
        t = i / (8 * n)
        s = a * math.sin(2 * math.pi * n * t) if t < 0.85 else 0
        pts.append((x1 + ux * L * t + nx * s, y1 + uy * L * t + ny * s))
    return "M " + " L ".join(f"{p:.1f} {q:.1f}" for p, q in pts)


def fig_q10_caps():
    f = Fig(420, 220, "fig_q10_caps")
    xa, xb = 110, 300
    yt, ym, yb = 50, 125, 190
    # A and B nodes on the left/right of the parallel block
    f.line(xa, yt, xa, ym); f.line(xb, yt, xb, ym)
    # top branch C1, C2
    f.line(xa, yt, 166, yt); _cap_h(f, 170, yt); f.line(174, yt, 236, yt); _cap_h(f, 240, yt); f.line(244, yt, xb, yt)
    f.text(170, 22, "C", size=14, bold=True, sub="1"); f.text(170, 82, "3 μF", size=13)
    f.text(240, 22, "C", size=14, bold=True, sub="2"); f.text(240, 82, "6 μF", size=13)
    # bottom branch C3
    f.line(xa, ym, 201, ym); _cap_h(f, 205, ym); f.line(209, ym, xb, ym)
    f.text(205, 104, "C", size=14, bold=True, sub="3"); f.text(205, 155, "10 μF", size=13)
    # node A at middle-left and B at middle-right
    f.line(xa, 88, 40, 88); f.line(40, 88, 40, yb)
    f.line(xb, 88, 380, 88); f.line(380, 88, 380, yb)
    _dot(f, xa, 88); _dot(f, xb, 88)
    f.text(xa - 14, 82, "A", size=14, bold=True); f.text(xb + 14, 82, "B", size=14, bold=True)
    f.line(40, yb, 205, yb); _cell_h(f, 209, yb); f.line(213, yb, 380, yb)
    f.text(210, yb + 26, "50 V", size=13)
    return f.svg()


def fig_q11_bridge():
    f = Fig(520, 240, "fig_q11_bridge")
    y = 135
    f.line(40, y, 480, y, w=2.2)                       # wire
    f.text(46, y + 20, "0 cm", size=12, anchor="start"); f.text(480, y + 20, "100 cm", size=12, anchor="end")
    # thick strips
    f.path("M 40 135 L 40 60 L 90 60", w=3); f.path("M 480 135 L 480 60 L 430 60", w=3)
    f.path("M 210 60 L 310 60", w=3)
    _res(f, 90, 60, 210, 60); f.text(150, 40, "2 Ω", size=14)
    _res(f, 310, 60, 430, 60); f.text(370, 40, "X", size=14, italic=True)
    # galvanometer from centre strip to jockey at 40 cm
    xj = 40 + 0.40 * 440
    f.line(260, 60, 260, 82); _meter(f, 260, 95, "G")
    f.line(258, 108, xj + 2, y - 6)
    f.path(f"M {xj-5} {y-12} L {xj} {y} L {xj+5} {y-12}", fill="#111")
    f.text(xj, y + 20, "40 cm", size=12)
    # battery + key
    f.line(40, y, 40, 205); f.line(480, y, 480, 205)
    f.line(40, 205, 196, 205); _cell_h(f, 200, 205); f.line(204, 205, 300, 205)
    f.circle(310, 205, 8, fill="#fff"); _dot(f, 310, 205, 2)
    f.line(318, 205, 480, 205)
    f.text(200, 228, "E", size=13); f.text(310, 228, "K", size=13)
    return f.svg()


def fig_q13_patterns():
    f = Fig(600, 220, "fig_q13_patterns")
    # A: rings crowding outward (radius ∝ √k), dark centre spot
    cx, cy = 100, 115
    f.raw('<clipPath id="fig_q13_patterns-cA"><rect x="20" y="30" width="160" height="170"/></clipPath>')
    f.raw('<g clip-path="url(#fig_q13_patterns-cA)">')
    for k in range(1, 40):
        r = 17 * math.sqrt(k)
        f.circle(cx, cy, r, w=2.4 if k < 6 else 1.4)
    f.raw('</g>')
    f.circle(cx, cy, 7, color="#666", fill="#777")
    f.text(12, 30, "A", size=20, bold=True, anchor="start")
    # B: equally spaced grey/white rings, white centre
    cx = 300
    f.rect(225, 35, 150, 165, color="none", fill="#fff", w=0)
    f.raw('<clipPath id="fig_q13_patterns-cB"><rect x="225" y="35" width="150" height="165"/></clipPath>')
    f.raw('<g clip-path="url(#fig_q13_patterns-cB)">')
    for k in range(1, 7):
        f.circle(cx, cy, 16 * k - 2, color="#8a8a8a", w=10)
    f.raw('</g>')
    f.text(220, 30, "B", size=20, bold=True, anchor="start")
    # C: dark field, wide bright central disc, faint secondary ring
    cx = 490
    f.rect(415, 40, 150, 160, color="#000", fill="#111")
    f.circle(cx, cy, 70, color="#777", w=12)
    f.circle(cx, cy, 47, color="#fff", fill="#fff")
    f.circle(cx, cy, 30, color="#111", w=2.6)
    f.text(420, 30, "C", size=20, bold=True, anchor="start")
    return f.svg()


def _rails(f, ans):
    # crosses
    for x in range(30, 400, 60):
        for y in (25, 75, 120, 165, 215):
            f.text(x, y + 5, "×", size=15, color="#444")
    yt, yb = 50, 190
    f.line(50, yt, 360, yt, w=2); f.line(50, yb, 360, yb, w=2)
    _res(f, 50, yt, 50, yb, n=5, amp=7)
    f.text(30, yt - 6, "A", size=15, bold=True); f.text(380, yt + 4, "B", size=15, bold=True)
    f.text(30, yb + 14, "C", size=15, bold=True); f.text(380, yb + 6, "D", size=15, bold=True)
    f.text(72, 125, "R", size=15, bold=True)
    xm = 220
    f.line(xm, yt - 6, xm, yb + 6, w=3)
    f.text(xm, yt - 12, "M", size=15, bold=True); f.text(xm, yb + 24, "N", size=15, bold=True)
    f.arrow(400, 110, 400, yt + 2, w=1.2); f.arrow(400, 130, 400, yb - 2, w=1.2)
    f.text(408, 125, "1 m", size=13, anchor="start")
    if ans:
        f.arrow(xm + 6, 120, xm + 70, 120, color=BLUE, w=2.2)
        f.text(xm + 72, 112, "v = 2 m/s", size=13, color=BLUE, anchor="start")
        f.arrow(xm - 8, 160, xm - 8, 85, color=RED, w=2.2)
        f.text(xm - 14, 125, "I", size=15, italic=True, color=RED, anchor="end")
        f.arrow(170, yt - 8, 100, yt - 8, color=RED, w=2)
        f.arrow(35, 95, 35, 150, color=RED, w=2)
        f.arrow(100, yb + 8, 170, yb + 8, color=RED, w=2)


def fig_q15_rails():
    f = Fig(450, 235, "fig_q15_rails")
    _rails(f, False)
    return f.svg()


# ----------------------------------------------------------------- ANSWER figures
def fig_q1a5_vu():
    """v against u for a concave mirror (f = -10), real images only, Cartesian signs."""
    f = Fig(360, 300, "fig_q1a5_vu")
    ox, oy, s = 300, 40, 4   # origin near top-right so the 3rd quadrant shows
    f.arrow(20, oy, 345, oy); f.arrow(ox, 290, ox, 15)
    f.text(340, oy - 8, "u", size=14, italic=True); f.text(ox + 10, 22, "v", size=14, italic=True, anchor="start")
    f.text(30, oy - 8, "u negative", size=11, anchor="start", color=GREY)
    f.text(ox + 6, 280, "v negative", size=11, anchor="start", color=GREY)
    fl = -10
    pts = []
    u = -10.6
    while u >= -65:
        v = 1 / (1 / fl - 1 / u)
        if v >= -62:
            pts.append((ox + s * u, oy - s * v))
        u -= 0.4
    f.path("M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts), color=BLUE, w=2.2)
    # asymptotes u = f, v = f
    f.line(ox + s * fl, oy, ox + s * fl, 290, color=GREY, w=1, dash="4 3")
    f.line(20, oy - s * fl, ox, oy - s * fl, color=GREY, w=1, dash="4 3")
    f.text(ox + s * fl, oy - 6, "u = f", size=11, color=GREY)
    f.text(30, oy - s * fl - 5, "v = f", size=11, color=GREY, anchor="start")
    f.line(ox + s * -20, oy - s * -20, ox + s * -20, oy, color=GREY, w=0.8, dash="2 3")
    _dot(f, ox + s * -20, oy - s * -20, 3, BLUE)
    f.text(ox + s * -20 - 6, oy - s * -20 + 16, "(2f, 2f)", size=11, color=GREY, anchor="end")
    f.text(130, 230, "3rd quadrant", size=13, color=RED)
    return f.svg()


def fig_q2_ex():
    f = Fig(400, 210, "fig_q2_ex")
    ox, oy, s = 60, 105, 90
    f.arrow(ox, oy, 380, oy); f.arrow(ox, 195, ox, 15)
    f.text(376, oy + 20, "x (m)", size=13, italic=True, anchor="end")
    f.text(ox - 6, 22, "E", size=14, italic=True, anchor="end")
    h = 55
    f.path(f"M {ox} {oy+h} L {ox+s} {oy+h}", color=RED, w=2.6)
    f.path(f"M {ox+s} {oy} L {ox+2*s} {oy}", color=RED, w=3.2)
    f.path(f"M {ox+2*s} {oy-h} L {ox+3*s} {oy-h}", color=RED, w=2.6)
    for x in (ox + s, ox + 2 * s, ox + 3 * s):
        f.line(x, oy - h, x, oy + h, color=GREY, w=0.8, dash="3 3")
    for i, t in enumerate(["0", "1", "2", "3"]):
        f.text(ox + i * s + (8 if i == 0 else 6), oy + 18, t, size=13)
    f.text(ox - 6, oy + h + 5, "−V₀", size=13, anchor="end")
    f.text(ox - 6, oy - h + 5, "+V₀", size=13, anchor="end")
    f.line(ox - 4, oy + h, ox + 4, oy + h); f.line(ox - 4, oy - h, ox + 4, oy - h)
    f.text(ox + 0.5 * s + 40, oy + h + 22, "slope of V +ve ⇒ E −ve", size=11, color=GREY)
    f.text(ox + 2.5 * s, oy - h - 10, "slope −ve ⇒ E +ve", size=11, color=GREY)
    return f.svg()


def fig_q7_levels():
    """Energy levels of H (schematic spacing) with the three series limits."""
    f = Fig(470, 290, "fig_q7_levels")
    E = {1: -13.6, 2: -3.4, 3: -1.51, 4: -0.85}
    Y = {1: 265, 2: 150, 3: 100, 4: 68}
    f.line(70, 30, 380, 30, dash="5 3"); f.text(64, 34, "n = ∞", size=12, anchor="end"); f.text(386, 34, "0 eV", size=11, anchor="start")
    for n, e in E.items():
        f.line(70, Y[n], 380, Y[n]); f.text(64, Y[n] + 4, f"n = {n}", size=12, anchor="end")
        f.text(386, Y[n] + 4, f"{e} eV", size=11, anchor="start")
    for x, nf, name, col in ((120, 1, "Lyman limit", RED), (210, 2, "Balmer limit", GREEN), (300, 3, "Paschen limit", BLUE)):
        f.arrow(x, 30, x, Y[nf] - 1, color=col, w=2)
        f.text(x + 5, (30 + Y[nf]) / 2 + (40 if nf == 1 else 0), name, size=11, color=col, anchor="start")
    f.text(225, 285, "(spacing schematic, not to scale)", size=10, color=GREY)
    return f.svg()


def fig_q9_vs_nu():
    f = Fig(400, 260, "fig_q9_vs_nu")
    ox, oy = 90, 170
    f.arrow(40, oy, 380, oy); f.arrow(ox, 245, ox, 15)
    f.text(376, oy + 20, "ν", size=15, italic=True, anchor="end")
    f.text(ox - 6, 22, "V", size=15, italic=True, anchor="end", sub="s")
    nu0 = 190
    m = 0.75
    f.line(nu0, oy, 360, oy - m * (360 - nu0), color=RED, w=2.4)
    f.line(ox, oy + m * (nu0 - ox), nu0, oy, color=RED, w=1.4, dash="5 4")
    f.text(nu0, oy + 20, "ν₀", size=14, italic=True)
    f.text(ox - 8, oy + m * (nu0 - ox) + 5, "−φ₀/e", size=13, anchor="end")
    # slope triangle
    x1, x2 = 250, 320
    f.line(x1, oy - m * (x1 - nu0), x2, oy - m * (x1 - nu0), color=GREY, w=1)
    f.line(x2, oy - m * (x1 - nu0), x2, oy - m * (x2 - nu0), color=GREY, w=1)
    f.text(300, oy - m * (x1 - nu0) + 18, "slope = h/e", size=13, color=GREY)
    f.text(ox - 8, oy + 5, "O", size=12, anchor="end")
    return f.svg()


def fig_q11a_new():
    f = Fig(420, 150, "fig_q11a_new")
    y = 50
    _res(f, 30, y, 130, y); f.text(80, 30, "2 Ω", size=13)
    f.line(130, y, 170, y); _dot(f, 170, y)
    f.line(170, y, 170, y - 25); f.line(170, y, 170, y + 25)
    _res(f, 170, y - 25, 290, y - 25); f.text(230, y - 37, "X = 3 Ω", size=13)
    _res(f, 170, y + 25, 290, y + 25); f.text(230, y + 50, "S = 6 Ω (in parallel)", size=13)
    f.line(290, y - 25, 290, y + 25); _dot(f, 290, y); f.line(290, y, 330, y)
    f.text(210, 135, "right gap = 3 × 6 / (3 + 6) = 2 Ω ⇒ null at 50 cm", size=12, color=GREY)
    return f.svg()


def fig_q11b_ampere():
    f = Fig(340, 300, "fig_q11b_ampere")
    cx, cy, r = 160, 150, 100
    f.circle(cx, cy, r, color=BLUE, w=1.6)
    # current out of page
    f.circle(cx, cy, 10, fill="#fff", w=1.8); _dot(f, cx, cy, 3)
    f.text(cx - 16, cy + 26, "I (out of page)", size=12, anchor="middle")
    # radius
    f.line(cx, cy, cx + r, cy, color=GREY, dash="4 3"); f.text(cx + 55, cy - 6, "r", size=15, italic=True)
    # point X at rightmost point; B tangent upward (anticlockwise as seen)
    _dot(f, cx + r, cy, 4)
    f.text(cx + r + 8, cy + 18, "X", size=15, bold=True, anchor="start")
    f.arrow(cx + r, cy, cx + r, cy - 60, color=RED, w=2.2)
    f.text(cx + r + 8, cy - 46, "B", size=15, bold=True, color=RED, anchor="start")
    # circulation arrows (anticlockwise on screen)
    for a in (60, 150, 240, 330):
        t = math.radians(a)
        x, y = cx + r * math.cos(t), cy - r * math.sin(t)
        dx, dy = -math.sin(t), -math.cos(t)
        f.arrow(x - 8 * dx, y - 8 * dy, x + 10 * dx, y + 10 * dy, color=BLUE, w=2)
    f.text(cx - 70, cy - 82, "dl", size=14, italic=True, color=BLUE)
    f.text(cx, 290, "Amperian loop: circle of radius r, centre on the wire", size=11, color=GREY)
    return f.svg()


def fig_q12a_phasor():
    f = Fig(360, 300, "fig_q12a_phasor")
    ox, oy = 70, 170
    f.line(40, oy, 340, oy, color=GREY, w=1)
    sx = 180  # V_R length
    vl, vc = 120, 50
    f.arrow(ox, oy, ox + sx, oy, color=GREEN, w=2.4)
    f.text(ox + sx - 10, oy + 20, "V", size=14, color=GREEN, sub="R")
    f.arrow(ox, oy, 330, oy, color="#555", w=1) if False else None
    f.text(ox + sx + 60, oy + 20, "I", size=14, italic=True)
    f.arrow(ox + sx + 20, oy + 6, ox + sx + 75, oy + 6, color="#555", w=1.2)
    f.arrow(ox, oy, ox, oy - vl, color=RED, w=2.4); f.text(ox - 8, oy - vl + 4, "V", size=14, color=RED, anchor="end", sub="L")
    f.arrow(ox, oy, ox, oy + vc, color=BLUE, w=2.4); f.text(ox - 8, oy + vc + 4, "V", size=14, color=BLUE, anchor="end", sub="C")
    # V_L - V_C drawn at the tip of V_R
    f.line(ox + sx, oy, ox + sx, oy - (vl - vc), color=ORANGE, w=1.6, dash="5 3")
    f.text(ox + sx + 6, oy - 30, "V", size=13, color=ORANGE, anchor="start", sub="L")
    f.text(ox + sx + 24, oy - 30, "− V", size=13, color=ORANGE, anchor="start", sub="C")
    f.arrow(ox, oy, ox + sx, oy - (vl - vc), color="#111", w=2.6)
    f.text(ox + 95, oy - 52, "V", size=15, bold=True)
    _arc(f, ox, oy, 45, 0, math.degrees(math.atan2(vl - vc, sx)))
    f.text(ox + 55, oy - 6, "φ", size=14, italic=True)
    return f.svg()


def fig_q12b_resonance():
    f = Fig(420, 270, "fig_q12b_resonance")
    ox, oy = 60, 230
    _axes(f, ox, oy, 400, 15, "ω", "I")
    w0, Im = 210, 170
    pts = []
    for i in range(0, 141):
        w = 70 + i * 2.3
        x = w
        # resonance curve I = Im / sqrt(1 + Q^2 (w/w0 - w0/w)^2)
        Q = 3.2
        I = Im / math.sqrt(1 + Q * Q * (w / w0 - w0 / w) ** 2)
        pts.append((x, oy - I))
    f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), color=BLUE, w=2.4)
    # half-power points
    Q = 3.2
    yh = oy - Im / math.sqrt(2)
    # solve w/w0 - w0/w = ±1/Q
    a = 1 / Q
    w2 = w0 * (a + math.sqrt(a * a + 4)) / 2
    w1 = w0 * (-a + math.sqrt(a * a + 4)) / 2
    f.line(ox, oy - Im, w0, oy - Im, color=GREY, w=1, dash="4 3")
    f.line(w0, oy - Im, w0, oy, color=GREY, w=1, dash="4 3")
    f.line(ox, yh, w2 + 30, yh, color=GREY, w=1, dash="4 3")
    f.line(w1, yh, w1, oy, color=GREY, w=1, dash="4 3"); f.line(w2, yh, w2, oy, color=GREY, w=1, dash="4 3")
    f.text(ox - 6, oy - Im + 5, "I₀", size=13, anchor="end")
    f.text(ox - 6, yh + 5, "I₀/√2", size=13, anchor="end")
    f.text(w0, oy + 18, "ω₀", size=13); f.text(w1 - 4, oy + 18, "ω₁", size=13); f.text(w2 + 4, oy + 18, "ω₂", size=13)
    f.arrow((w1 + w2) / 2, oy - 30, w1 + 1, oy - 30, color=RED, w=1.4)
    f.arrow((w1 + w2) / 2, oy - 30, w2 - 1, oy - 30, color=RED, w=1.4)
    f.text(w2 + 8, oy - 40, "bandwidth", size=12, color=RED, anchor="start")
    f.text(w2 + 8, oy - 25, "Δω = ω₂ − ω₁", size=12, color=RED, anchor="start")
    f.text(w0 + 6, oy - Im - 6, "resonance (current amplitude I₀)", size=11, color=GREY, anchor="start")
    return f.svg()


def fig_q15_ans():
    f = Fig(470, 235, "fig_q15_ans")
    _rails(f, True)
    return f.svg()


def fig_q18_lenses():
    """Two thin convex lenses in contact, f1 = 40, f2 = 60 (units), u = -60: I1 at +120, I at +40."""
    f = Fig(580, 210, "fig_q18_lenses")
    s, xl, y0 = 2, 230, 120
    f.line(20, y0, 570, y0, color=GREY, w=1)
    _lens(f, xl - 5, y0, 70); _lens(f, xl + 5, y0, 70, color=GREEN)
    f.text(xl - 10, y0 - 76, "L₁", size=13, color=BLUE, anchor="end"); f.text(xl + 12, y0 - 76, "L₂", size=13, color=GREEN, anchor="start")
    xo, xi, xi1 = xl - 60 * s, xl + 40 * s, xl + 120 * s
    h = 50
    f.line(xo, y0, xl, y0 - h, color=RED, w=1.8)
    f.arrow(xo, y0, xo + 0.55 * (xl - xo), y0 - 0.55 * h, color=RED, w=1.8)
    # final refracted ray to I (and a bit beyond)
    f.line(xl, y0 - h, xi, y0, color=RED, w=1.8)
    f.arrow(xl, y0 - h, xl + 0.6 * (xi - xl), y0 - 0.6 * h, color=RED, w=1.8)
    f.line(xi, y0, xi + 40, y0 + h * 40 / (xi - xl), color=RED, w=1.8)
    # ray if L1 alone (dashed) to I1
    f.line(xl, y0 - h, xi1, y0, color=BLUE, w=1.2, dash="5 4")
    for x, t in ((xo, "O"), (xi, "I"), (xi1, "I₁")):
        _dot(f, x, y0, 3)
        f.text(x, y0 + 20, t, size=14, bold=True)
    f.text((xo + xl) / 2, y0 + 44, "u", size=14, italic=True)
    f.arrow((xo + xl) / 2 - 10, y0 + 40, xo, y0 + 40, w=1); f.arrow((xo + xl) / 2 + 10, y0 + 40, xl, y0 + 40, w=1)
    f.text((xl + xi) / 2, y0 + 64, "v", size=14, italic=True)
    f.arrow((xl + xi) / 2 - 8, y0 + 60, xl, y0 + 60, w=1); f.arrow((xl + xi) / 2 + 8, y0 + 60, xi, y0 + 60, w=1)
    f.text((xl + xi1) / 2 + 80, y0 + 82, "v₁", size=14, italic=True)
    f.line(xl, y0 + 78, xi1, y0 + 78, color=GREY, w=0.8)
    f.line(xi1, y0 + 72, xi1, y0 + 84, color=GREY, w=0.8)
    f.text(xi1, y0 - 14, "(image by L₁ alone)", size=10, color=BLUE)
    return f.svg()


def fig_q18_refraction():
    """Ray in air meets the air-glass interface at i = 40°, refracts towards the normal at r = 25° in the glass:
    deviation 15°  =>  n = sin 40°/sin 25° = 1.52."""
    f = Fig(380, 290, "fig_q18_refraction")
    cx, cy, L = 190, 145, 120
    f.rect(20, cy, 340, 130, color="none", fill="#e8f1fb", w=0)
    f.line(20, cy, 360, cy, w=1.8)
    f.text(30, cy + 22, "glass (denser)", size=12, anchor="start")
    f.text(30, cy - 10, "air (rarer)", size=12, anchor="start")
    f.line(cx, 20, cx, 275, color=GREY, w=1, dash="5 4"); f.text(cx + 4, 30, "N", size=12, anchor="start")
    i, r = math.radians(40), math.radians(25)
    xs, ys = cx - L * math.sin(i), cy - L * math.cos(i)          # incident ray comes down from upper left
    f.line(xs, ys, cx, cy, color=RED, w=2)
    f.arrow(xs, ys, xs + 0.6 * (cx - xs), ys + 0.6 * (cy - ys), color=RED, w=2)
    xe, ye = cx + L * math.sin(r), cy + L * math.cos(r)           # refracted ray bends towards the normal
    f.arrow(cx, cy, xe, ye, color=RED, w=2)
    # undeviated direction (dashed): continuation of the incident ray
    f.line(cx, cy, cx + L * math.sin(i), cy + L * math.cos(i), color=GREY, w=1, dash="4 3")
    _arc(f, cx, cy, 40, 90, 90 + 40)
    f.text(cx - 122, cy - 52, "i = 40°", size=12, anchor="start")
    _arc(f, cx, cy, 50, 270, 270 + 25)
    f.text(cx - 8, cy + 72, "r = 25°", size=12, anchor="end")
    _arc(f, cx, cy, 92, 270 + 25, 270 + 40, color=ORANGE)
    f.text(cx + 100, cy + 104, "δ = 15°", size=12, color=ORANGE, anchor="start")
    return f.svg()


def fig_q18_huygens():
    """Reflection by Huygens: i = 30°.  BC = AD = ct;  triangles ABC, CDA congruent."""
    f = Fig(520, 300, "fig_q18_huygens")
    i = math.radians(30)
    ys = 240
    A = (120, ys); Lw = 300; C = (A[0] + Lw, ys)
    d = (math.sin(i), math.cos(i))            # incident direction (down-right)
    dr = (math.sin(i), -math.cos(i))          # reflected direction (up-right)
    ct = Lw * math.sin(i)
    B = (C[0] - ct * d[0], C[1] - ct * d[1])
    D = (A[0] + ct * dr[0], A[1] + ct * dr[1])
    f.rect(20, ys, 480, 40, color="none", fill="#e6e6e6", w=0)
    f.line(20, ys, 500, ys, w=2.2)
    f.text(30, ys + 26, "X", size=13, bold=True, anchor="start"); f.text(490, ys + 26, "Y", size=13, bold=True, anchor="end")
    # incident rays
    k = 120
    f.arrow(A[0] - k * d[0], A[1] - k * d[1], A[0] - 0.4 * k * d[0], A[1] - 0.4 * k * d[1], color=RED, w=1.8)
    f.line(A[0] - k * d[0], A[1] - k * d[1], A[0], A[1], color=RED, w=1.8)
    f.arrow(B[0] - 60 * d[0], B[1] - 60 * d[1], B[0] - 10 * d[0], B[1] - 10 * d[1], color=RED, w=1.8)
    f.line(B[0] - 60 * d[0], B[1] - 60 * d[1], C[0], C[1], color=RED, w=1.8)
    # reflected rays
    f.arrow(A[0], A[1], D[0] + 40 * dr[0], D[1] + 40 * dr[1], color=GREEN, w=1.8)
    f.arrow(C[0], C[1], C[0] + 80 * dr[0], C[1] + 80 * dr[1], color=GREEN, w=1.8)
    # wavefronts
    f.line(A[0], A[1], B[0], B[1], color=BLUE, w=2)
    f.line(C[0], C[1], D[0], D[1], color=BLUE, w=2)
    # secondary wavelet from A
    f.path(f"M {A[0]-ct:.1f} {ys} A {ct:.1f} {ct:.1f} 0 0 1 {A[0]+ct:.1f} {ys}", color=GREY, w=1, dash="4 3")
    # normals
    for P in (A, C):
        f.line(P[0], ys, P[0], ys - 150, color=GREY, w=1, dash="5 4")
    _arc(f, A[0], A[1], 38, 90, 90 + 30); f.text(A[0] - 12, A[1] - 44, "i", size=14, italic=True)
    _arc(f, C[0], C[1], 38, 90, 90 - 30); f.text(C[0] + 14, C[1] - 44, "r", size=14, italic=True)
    for P, t, dx, dy in ((A, "A", -6, 20), (B, "B", 12, -6), (C, "C", 6, 20), (D, "D", -6, -10)):
        _dot(f, P[0], P[1], 3)
        f.text(P[0] + dx, P[1] + dy, t, size=14, bold=True)
    f.text((B[0] + C[0]) / 2 + 22, (B[1] + C[1]) / 2, "ct", size=13, italic=True)
    f.text((A[0] + D[0]) / 2 - 18, (A[1] + D[1]) / 2 + 4, "ct", size=13, italic=True)
    return f.svg()


def fig_q18_fibre():
    f = Fig(640, 170, "fig_q18_fibre")
    f.rect(20, 30, 420, 110, color="#555", fill="#eef2f6")
    f.rect(20, 55, 420, 60, color=BLUE, fill="#dbe8f7")
    f.line(440, 40, 452, 40, color=GREY, w=1); f.text(456, 44, "cladding Y (n = 1.337)", size=12, anchor="start")
    f.line(440, 85, 452, 85, color=GREY, w=1); f.text(456, 89, "core X (n = 1.4905)", size=12, anchor="start", color=BLUE)
    # zig-zag at 72° to the normal (> C = 63.8°), computed so the reflections really are total
    th = math.radians(72); t = math.tan(th)
    pts = [(20, 100)]; y, up = 100, True
    while True:
        x0, y0 = pts[-1]; y1 = 55 if up else 115
        x1 = x0 + abs(y1 - y0) * t
        if x1 >= 440:
            pts.append((440, y0 + (440 - x0) / t * (-1 if up else 1))); break
        pts.append((x1, y1)); up = not up
    f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), color=RED, w=1.8)
    f.arrow(pts[0][0], pts[0][1], pts[0][0] + 0.5 * (pts[1][0] - pts[0][0]), pts[0][1] + 0.5 * (pts[1][1] - pts[0][1]), color=RED, w=1.8)
    P = pts[2]                                   # a reflection on the lower boundary
    f.line(P[0], P[1], P[0], P[1] - 52, color=GREY, w=1, dash="4 3")
    _arc(f, P[0], P[1], 26, 90, 90 + 72)
    f.text(P[0] - 34, P[1] - 30, "θ", size=12, italic=True)
    f.text(P[0] + 6, P[1] - 40, "θ = 72° > C = 63.8°", size=10, anchor="start")
    f.text(230, 160, "total internal reflection at each core–cladding boundary (angle > C)", size=11, color=GREY)
    return f.svg()


def fig_q19_bohr():
    f = Fig(320, 270, "fig_q19_bohr")
    cx, cy, r = 150, 135, 95
    f.circle(cx, cy, r, color=GREY)
    f.circle(cx, cy, 11, color=RED, fill="#f7d4cf"); f.text(cx, cy + 5, "+e", size=11)
    ex, ey = cx + r * math.cos(math.radians(40)), cy - r * math.sin(math.radians(40))
    f.circle(ex, ey, 7, color=BLUE, fill="#cfe0f7"); f.text(ex + 12, ey - 6, "−e", size=12, anchor="start")
    f.line(cx, cy, ex, ey, color=GREY, w=1, dash="4 3")
    f.text((cx + ex) / 2 - 8, (cy + ey) / 2 - 6, "r", size=15, italic=True)
    t = math.radians(40)
    vx, vy = -math.sin(t), -math.cos(t)
    f.arrow(ex, ey, ex + 55 * vx, ey + 55 * vy, color=GREEN, w=2.2)
    f.text(ex + 55 * vx - 8, ey + 55 * vy, "v", size=15, italic=True, color=GREEN, anchor="end")
    ux, uy = (cx - ex) / r, (cy - ey) / r
    f.arrow(ex + 9 * ux, ey + 9 * uy, ex + 45 * ux, ey + 45 * uy, color=RED, w=2.2)
    f.text(ex + 30 * ux + 14, ey + 30 * uy + 14, "F", size=14, italic=True, color=RED)
    f.text(cx, 258, "Coulomb force provides the centripetal force", size=11, color=GREY)
    return f.svg()


def fig_q19_bea():
    f = Fig(460, 300, "fig_q19_bea")
    ox, oy = 60, 270
    _axes(f, ox, oy, 440, 15, "A", "")
    f.text(ox + 10, 24, "BE/A (MeV)", size=13, anchor="start")
    sx = 1.55   # px per unit A
    sy = 20     # px per MeV
    data = [(2, 1.11), (3, 2.57), (4, 7.07), (6, 5.33), (7, 5.6), (9, 6.46), (12, 7.68), (16, 7.98), (20, 8.03),
            (28, 8.45), (40, 8.55), (56, 8.79), (80, 8.71), (100, 8.6), (120, 8.5), (150, 8.3), (180, 8.05),
            (208, 7.87), (238, 7.57)]
    X = lambda a: ox + sx * a
    Y = lambda e: oy - sy * e
    # smooth-ish: straight segments except the 4He peak plotted as a point
    main = [p for p in data if p[0] not in (4,)]
    f.path("M " + " L ".join(f"{X(a):.1f} {Y(e):.1f}" for a, e in main), color=BLUE, w=2.2)
    _dot(f, X(4), Y(7.07), 3, BLUE); f.text(X(4) + 6, Y(7.07) - 6, "⁴He", size=11, anchor="start")
    _dot(f, X(56), Y(8.79), 3, RED); f.text(X(56) + 4, Y(8.79) + 18, "⁵⁶Fe (8.8 MeV)", size=11, color=RED, anchor="start")
    for e in (2, 4, 6, 8):
        f.line(ox - 4, Y(e), ox, Y(e)); f.text(ox - 8, Y(e) + 4, str(e), size=11, anchor="end")
    for a in (50, 100, 150, 200):
        f.line(X(a), oy, X(a), oy + 4); f.text(X(a), oy + 18, str(a), size=11)
    # regions
    f.rect(X(0) + 1, Y(10.6), X(30) - X(0), 20, color="none", fill="#fde3d0", w=0)
    f.text(X(15), Y(10.6) + 14, "fusion", size=11, color=ORANGE)
    f.rect(X(40), Y(10.6), X(120) - X(40), 20, color="none", fill="#d8eed8", w=0)
    f.text(X(80), Y(10.6) + 14, "most stable", size=11, color=GREEN)
    f.rect(X(170), Y(10.6), X(240) - X(170), 20, color="none", fill="#f7d4d4", w=0)
    f.text(X(205), Y(10.6) + 14, "fission", size=11, color=RED)
    return f.svg()


def fig_q20_fwr():
    f = Fig(520, 300, "fig_q20_fwr")
    # primary
    _coil_v(f, 120, 70, 230, 6, right=True)
    f.line(120, 70, 50, 70); f.line(120, 230, 50, 230)
    f.circle(50, 150, 16, fill="#fff"); f.path("M 40 150 Q 45 140 50 150 T 60 150", w=1.4)
    f.line(50, 70, 50, 134); f.line(50, 166, 50, 230)
    f.text(25, 155, "AC", size=12, anchor="end") if False else f.text(50, 262, "AC input", size=12)
    f.line(140, 60, 140, 240, w=2); f.line(146, 60, 146, 240, w=2)   # core
    # secondary, centre-tapped
    _coil_v(f, 166, 60, 240, 8, right=False)
    # (left-bulging coil drawn at x=166 bulges to the left; leads go right)
    f.line(166, 60, 230, 60); f.line(166, 240, 230, 240)
    f.line(166, 150, 230, 150); _dot(f, 166, 150)
    f.text(180, 50, "S₁", size=12); f.text(180, 262, "S₂", size=12); f.text(190, 142, "T", size=12)
    # diodes
    _diode(f, 230, 340, 60); f.text(285, 42, "D₁", size=13)
    _diode(f, 230, 340, 240); f.text(285, 268, "D₂", size=13)
    f.line(340, 60, 400, 60); f.line(340, 240, 400, 240); f.line(400, 60, 400, 240)
    _dot(f, 400, 150); f.text(410, 146, "P", size=13, bold=True, anchor="start")
    # load between P and centre tap T
    f.line(400, 150, 360, 150); _res(f, 360, 150, 250, 150, n=5)
    f.line(250, 150, 230, 150)
    f.text(305, 176, "R", size=14, italic=True, sub="L")
    # output terminals
    f.line(400, 150, 470, 150) if False else None
    f.line(360, 150, 360, 185); f.line(250, 150, 250, 185)
    _dot(f, 360, 185); _dot(f, 250, 185)
    f.text(365, 200, "+", size=14); f.text(250, 202, "−", size=16)
    f.text(305, 205, "output", size=12)
    f.arrow(345, 128, 265, 128, color=RED, w=1.4)
    f.text(305, 120, "I (same direction in both halves)", size=10, color=RED)
    f.text(450, 290, "centre-tap full-wave rectifier", size=11, color=GREY)
    return f.svg()


def fig_q20_waves():
    f = Fig(480, 260, "fig_q20_waves")
    def wave(oy, rect, label, col):
        ox = 60
        f.line(ox, oy, 460, oy, color=GREY, w=1)
        f.arrow(ox, oy + 50, ox, oy - 60, w=1.2)
        pts = []
        for i in range(0, 361):
            t = i / 360 * 2
            v = math.sin(2 * math.pi * t)
            if rect:
                v = abs(v)
            pts.append((ox + i * 1.1, oy - 45 * v))
        f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), color=col, w=2)
        f.text(ox - 8, oy - 50, label, size=12, anchor="end")
        f.text(462, oy + 16, "t", size=13, italic=True, anchor="end")
    wave(70, False, "V in", BLUE)
    wave(200, True, "V out", RED)
    for k in range(1, 4):
        x = 60 + k * 99
        f.line(x, 20, x, 215, color=GREY, w=0.6, dash="3 3")
    for k, t in enumerate(["D₁", "D₂", "D₁", "D₂"]):
        f.text(60 + 49.5 + 99 * k, 132, t, size=11, color=RED)
    return f.svg()


# ================================================================= PRACTICAL (physics_2025_26_prac)
def _pin_stand(f, x, ybase, h=60):
    f.rect(x - 8, ybase - h, 16, h, fill="#fff")
    for k in range(0, h, 7):
        f.line(x - 8, ybase - h + k + 7, x + 8, ybase - h + k, w=0.8)


def fig_p1_bench():
    """Figure 1 of the practical paper: O at 0 cm, lens L, image pin I at 100 cm end, eye."""
    f = Fig(560, 240, "fig_p1_bench")
    yb, ya = 170, 70
    f.line(60, yb, 480, yb, w=2)
    for x in (80, 270, 440):
        _pin_stand(f, x, yb)
    f.arrow(80, yb - 60, 80, ya + 2, w=2); f.text(80, ya - 8, "O", size=15)
    _lens(f, 270, ya, 38, color="#111", bulge=9); f.text(270, ya + 4, "L", size=14)
    f.line(270, ya + 38, 270, yb - 60, w=1)
    f.arrow(440, yb - 60, 440, ya + 2, w=2); f.text(452, ya + 4, "I", size=14, anchor="start")
    f.arrow(440, ya - 34, 440, ya - 4, dash="3 3", w=1.4); f.text(452, ya - 30, "I′", size=14, anchor="start")
    f.line(80, ya, 470, ya, dash="5 4", w=1.2)
    # eye
    f.path("M 490 60 Q 505 70 490 80", w=1.6); f.path("M 490 60 L 510 70 L 490 80", w=1.6)
    f.circle(493, 70, 4, fill="#111")
    f.text(80, yb + 22, "0 cm", size=14); f.text(440, yb + 22, "100 cm", size=14)
    f.line(80, yb + 4, 80, yb + 10); f.line(440, yb + 4, 440, yb + 10)
    f.arrow(170, yb + 44, 82, yb + 44, w=1.4); f.arrow(185, yb + 44, 268, yb + 44, w=1.4)
    f.text(177, yb + 49, "u", size=14, italic=True)
    f.arrow(350, yb + 44, 272, yb + 44, w=1.4); f.arrow(365, yb + 44, 438, yb + 44, w=1.4)
    f.text(357, yb + 49, "v", size=14, italic=True)
    return f.svg()


def fig_p2_circuit():
    """Figure 2: E (+ left), R.B., key K, ammeter (− left, + right) across the whole wire AB;
    voltmeter (+ at A) from A to jockey J at C, AC = x cm."""
    f = Fig(560, 270, "fig_p2_circuit")
    yt, yw, yv = 50, 140, 210
    xa, xb = 100, 470
    f.line(xa, yt, xa, yv, w=3)               # thick lead A
    f.line(xa, yt, 166, yt); _cell_h(f, 170, yt); f.line(174, yt, 220, yt)
    f.text(160, yt - 18, "+", size=14); f.text(182, yt - 18, "−", size=16); f.text(170, yt - 22, "E", size=14)
    f.rect(220, yt - 14, 70, 28, fill="#fff"); f.text(255, yt + 5, "R.B.", size=13)
    f.line(290, yt, 340, yt)
    f.circle(350, yt, 9, fill="#fff"); _dot(f, 350, yt, 2.5); f.text(350, yt - 18, "K", size=14)
    f.line(359, yt, 390, yt); _meter(f, 404, yt, "A"); f.line(417, yt, xb, yt); f.line(xb, yt, xb, yw)
    f.text(386, yt - 16, "−", size=16); f.text(422, yt - 16, "+", size=14)
    # wire AB
    f.line(xa, yw, xb, yw, w=2.4)
    _dot(f, xa, yw, 4); _dot(f, xb, yw, 4)
    f.text(xa - 10, yw + 6, "A", size=15, anchor="end"); f.text(xb + 10, yw + 6, "B", size=15, anchor="start")
    f.text(xa - 10, yw + 24, "0 cm", size=13, anchor="end"); f.text(xb + 10, yw + 24, "100 cm", size=13, anchor="start")
    xc = xa + 0.8 * (xb - xa)
    f.arrow(xa + 120, yw - 18, xa + 4, yw - 18, w=1.4); f.arrow(xa + 180, yw - 18, xc - 2, yw - 18, w=1.4)
    f.text(xa + 150, yw - 13, "x cm", size=14); f.text(xc + 10, yw - 14, "C", size=14, anchor="start")
    # voltmeter A -> J at C
    f.line(xa, yv, 252, yv); _meter(f, 265, yv, "V")
    f.path(f"M 278 {yv} Q {xc - 10} {yv} {xc} {yw + 6}", arrow=True)
    f.text(xc + 10, yw + 30, "J", size=14, anchor="start")
    f.text(252, yv + 24, "+", size=14); f.text(280, yv + 26, "−", size=16)
    return f.svg()


def fig_p1_graph():
    """y = u + v against x = u v, sample readings, best-fit line y = 0.0662 x + 0.47, slope triangle."""
    f = Fig(660, 470, "fig_p1_graph")
    X = [1208.00, 932.50, 906.00, 913.50, 964.00, 1008.00]
    Y = [80.40, 62.30, 60.20, 61.10, 64.10, 67.40]
    x0, x1, y0, y1 = 880, 1220, 58, 82
    L, R_, T, B = 80, 570, 30, 400
    px = lambda x: L + (x - x0) / (x1 - x0) * (R_ - L)
    py = lambda y: B - (y - y0) / (y1 - y0) * (B - T)
    # grid: small squares every 10 (x) and 1 (y); bold every 50 / 5
    for xv in range(880, 1221, 10):
        f.line(px(xv), T, px(xv), B, color="#cfe3cf" if xv % 50 else "#9cc59c", w=0.6 if xv % 50 else 1)
    for yv in range(58, 83):
        f.line(L, py(yv), R_, py(yv), color="#cfe3cf" if (yv - 58) % 4 else "#9cc59c", w=0.6 if (yv - 58) % 4 else 1)
    f.line(L, B, R_, B, w=1.6); f.line(L, B, L, T, w=1.6)
    for xv in range(900, 1221, 50):
        f.text(px(xv), B + 18, str(xv), size=11)
    for yv in range(58, 83, 4):
        f.text(L - 6, py(yv) + 4, str(yv), size=11, anchor="end")
    f.text(L - 6, B + 18, "(880, 58)", size=10, anchor="end")
    f.text((L + R_) / 2, B + 40, "x = uv (cm²)", size=13)
    _vtext(f, 28, (T + B) / 2, "y = u + v (cm)", size=13)
    f.text((L + R_) / 2, 18, "Graph of y against x", size=13, bold=True)
    S, C = 0.0662, 0.47
    xa, xb = 890, 1215
    f.line(px(xa), py(S * xa + C), px(xb), py(S * xb + C), color=BLUE, w=1.4)
    for x, y in zip(X, Y):
        f.circle(px(x), py(y), 5, color=RED, w=1.4); _dot(f, px(x), py(y), 1.4, RED)
    # slope triangle on two non-plotted points P(920, 61.37), Q(1200, 79.91)
    P = (920, 61.37); Qp = (1200, 79.91)
    f.line(px(P[0]), py(P[1]), px(Qp[0]), py(P[1]), color=ORANGE, w=1.2, dash="5 3")
    f.line(px(Qp[0]), py(P[1]), px(Qp[0]), py(Qp[1]), color=ORANGE, w=1.2, dash="5 3")
    _dot(f, px(P[0]), py(P[1]), 3, ORANGE); _dot(f, px(Qp[0]), py(Qp[1]), 3, ORANGE)
    f.text(px(P[0]) + 4, py(P[1]) + 18, "P (920, 61.37)", size=11, color=ORANGE, anchor="start")
    f.text(px(Qp[0]) - 6, py(Qp[1]) - 8, "Q (1200, 79.91)", size=11, color=ORANGE, anchor="end")
    f.text((px(P[0]) + px(Qp[0])) / 2, py(P[1]) + 18, "Δx = 280 cm²", size=11, color=ORANGE)
    f.text(px(Qp[0]) + 6, (py(P[1]) + py(Qp[1])) / 2, "Δy = 18.54", size=11, color=ORANGE, anchor="start")
    f.text(px(Qp[0]) + 6, (py(P[1]) + py(Qp[1])) / 2 + 14, "cm", size=11, color=ORANGE, anchor="start")
    return f.svg()
