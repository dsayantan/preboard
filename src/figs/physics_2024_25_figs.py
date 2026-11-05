"""Figures for Physics Pre-Board 2024-25 (theory, physics_2024_25).
y grows downward.  In every cell symbol the LONG thin plate is the positive terminal."""
import math
from svg import Fig

BLUE, RED, GREEN, GREY, ORANGE, PURPLE = "#1f4e9c", "#c0392b", "#1e7b34", "#888", "#b9770e", "#6c3483"


# ----------------------------------------------------------------- helpers
def _dot(f, x, y, r=3, color="#111"):
    f.circle(x, y, r, color=color, fill=color, w=1)


def _unit(x1, y1, x2, y2):
    L = math.hypot(x2 - x1, y2 - y1)
    return (x2 - x1) / L, (y2 - y1) / L, L


def _res(f, x1, y1, x2, y2, n=5, amp=6, color="#111", lead=0.25):
    """zig-zag resistor occupying the whole segment (leads included)."""
    ux, uy, L = _unit(x1, y1, x2, y2)
    nx, ny = -uy, ux
    ld = L * lead
    pts = [(x1, y1), (x1 + ux * ld, y1 + uy * ld)]
    body = L - 2 * ld
    for i in range(1, 2 * n):
        t = ld + body * i / (2 * n)
        s = amp if i % 2 else -amp
        pts.append((x1 + ux * t + nx * s, y1 + uy * t + ny * s))
    pts += [(x2 - ux * ld, y2 - uy * ld), (x2, y2)]
    f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), color=color)


def _cell(f, x1, y1, x2, y2, plus_at_start=True, gap=7, color="#111"):
    """wire from (x1,y1) to (x2,y2) with a cell in the middle; long plate (+) nearer the start if plus_at_start."""
    ux, uy, L = _unit(x1, y1, x2, y2)
    nx, ny = -uy, ux
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    pa = (mx - ux * gap / 2, my - uy * gap / 2)     # plate nearer start
    pb = (mx + ux * gap / 2, my + uy * gap / 2)     # plate nearer end
    f.line(x1, y1, pa[0], pa[1], color=color)
    f.line(pb[0], pb[1], x2, y2, color=color)
    la, lb = (26, 12) if plus_at_start else (12, 26)
    for (px, py), l, w in ((pa, la, 2.0 if la > 20 else 3.4), (pb, lb, 2.0 if lb > 20 else 3.4)):
        f.line(px - nx * l / 2, py - ny * l / 2, px + nx * l / 2, py + ny * l / 2, color=color, w=w)


def _cap_h(f, xc, y, h=24, gap=8):
    f.line(xc - gap / 2, y - h / 2, xc - gap / 2, y + h / 2, w=2.4)
    f.line(xc + gap / 2, y - h / 2, xc + gap / 2, y + h / 2, w=2.4)


def _meter(f, x, y, letter, r=13):
    f.circle(x, y, r, fill="#fff")
    f.text(x, y + 5, letter, size=14, bold=True)


def _axes(f, ox, oy, x2, y2, xlab, ylab, x1=None, y1=None, size=14):
    f.arrow(ox if x1 is None else x1, oy, x2, oy)
    f.arrow(ox, oy if y1 is None else y1, ox, y2)
    f.text(x2 - 2, oy + 20, xlab, size=size, italic=True, anchor="end")
    f.text(ox - 6, y2 + 4, ylab, size=size, italic=True, anchor="end")


def _arc(f, cx, cy, r, a1, a2, color="#111", w=1.2):
    """arc from angle a1 to a2 (degrees, maths sense, y up) -- always the minor arc."""
    d = (a2 - a1 + 180) % 360 - 180
    a2 = a1 + d
    p1 = (cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1)))
    p2 = (cx + r * math.cos(math.radians(a2)), cy - r * math.sin(math.radians(a2)))
    sweep = 0 if d > 0 else 1
    f.path(f"M {p1[0]:.1f} {p1[1]:.1f} A {r} {r} 0 0 {sweep} {p2[0]:.1f} {p2[1]:.1f}", color=color, w=w)


def _vtext(f, x, y, s, size=13, color="#111"):
    f.raw(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="middle" fill="{color}" '
          f'font-family="Times New Roman,serif" transform="rotate(-90 {x} {y})">{s}</text>')


def _rtext(f, x, y, s, ang, size=13, color="#111"):
    f.raw(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="middle" fill="{color}" '
          f'font-family="Times New Roman,serif" transform="rotate({ang} {x} {y})">{s}</text>')


def _lens(f, x, y, h, color=BLUE, bulge=8):
    f.path(f"M {x} {y-h} Q {x+2*bulge} {y} {x} {y+h} Q {x-2*bulge} {y} {x} {y-h} Z", color=color, fill="#e8f1fb")


def _diode(f, x1, x2, y, color="#111", label=None):
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


def _lab(f, x, y, parts, size=13, color="#111", anchor="middle", italic=False):
    """text made of (string, is_subscript) parts, e.g. [("X", 0), ("L", 1), (" = 2πfL", 0)]."""
    from html import escape
    st = ' font-style="italic"' if italic else ""
    t = "".join(f'<tspan baseline-shift="sub" font-size="{size*0.72:.1f}">{escape(a)}</tspan>' if sb else escape(a)
                for a, sb in parts)
    f.raw(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{color}" '
          f'font-family="Times New Roman,serif"{st}>{t}</text>')


def _poly(pts):
    return "M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts)


# ================================================================= QUESTION figures
def fig_q1a1_charges():
    """Q1(A)(i): X (+q) at the top of an equilateral triangle, Y (-q) bottom left, Z (+q) bottom right;
    the four candidate paths A (left), B (curving down-left), C (right), D (curving down-right)."""
    f = Fig(340, 210, "fig_q1a1_charges")
    X, Y, Z = (170, 50), (110, 154), (230, 154)
    for P, lab, q in ((X, "X", "+q"), (Y, "Y", "−q"), (Z, "Z", "+q")):
        _dot(f, P[0], P[1], 6)
    f.text(170, 32, "X (+q)", size=13, bold=True)
    f.text(110, 180, "Y (−q)", size=13, bold=True)
    f.text(230, 180, "Z (+q)", size=13, bold=True)
    f.arrow(162, 50, 45, 50, dash="5 3"); f.text(32, 55, "A", size=14, bold=True)
    f.arrow(178, 50, 295, 50, dash="5 3"); f.text(308, 55, "C", size=14, bold=True)
    f.path("M 164 54 Q 125 60 100 86", dash="5 3", arrow=True); f.text(90, 92, "B", size=14, bold=True)
    f.path("M 176 54 Q 215 62 232 100", dash="5 3", arrow=True); f.text(244, 108, "D", size=14, bold=True)
    return f.svg()


def fig_q1a2_bridge():
    """Q1(A)(ii): A-B 10 V cell (+ at A), B-C resistor R, A-C 100 ohm, A-D ammeter, D-C 4 V cell (+ at D)."""
    f = Fig(300, 380, "fig_q1a2_bridge")
    A, B, C, D = (60, 190), (150, 40), (240, 190), (150, 340)
    _cell(f, A[0], A[1], B[0], B[1], plus_at_start=True)
    f.text(78, 108, "10 V", size=13, anchor="end")
    _res(f, B[0], B[1], C[0], C[1], n=4)
    f.text(212, 108, "R", size=15, italic=True, anchor="start")
    _res(f, A[0], A[1], C[0], C[1], n=4, lead=0.35)
    f.text(150, 176, "100 Ω", size=13)
    # A -> ammeter -> D
    mx, my = 95, 248
    ux, uy, L = _unit(A[0], A[1], D[0], D[1])
    f.line(A[0], A[1], mx - ux * 14, my - uy * 14)
    f.line(mx + ux * 14, my + uy * 14, D[0], D[1])
    _meter(f, mx, my, "A", r=14)
    _cell(f, D[0], D[1], C[0], C[1], plus_at_start=True)
    f.text(212, 284, "4 V", size=13, anchor="start")
    for P, t, dx, dy in ((A, "A", -14, 5), (B, "B", 0, -10), (C, "C", 14, 5), (D, "D", 0, 24)):
        _dot(f, P[0], P[1], 2.5)
        f.text(P[0] + dx, P[1] + dy, t, size=15, bold=True)
    return f.svg()


def fig_q1a3_cells():
    """Q1(A)(iii): E1, E2, E3 (2 V each) in series in the upper branch, E4 (6 V) in the lower branch;
    every positive (long) plate faces the left terminal (+)."""
    f = Fig(520, 170, "fig_q1a3_cells")
    yt, yb, ym = 50, 120, 85
    f.line(20, ym, 80, ym); f.line(80, yt, 80, yb)
    f.line(440, ym, 500, ym); f.line(440, yt, 440, yb)
    f.text(24, ym - 8, "+", size=16, anchor="start"); f.text(496, ym - 8, "−", size=16, anchor="end")
    xs = [80, 160, 260, 340, 440]
    _cell(f, 80, yt, 230, yt)
    _cell(f, 230, yt, 300, yt)
    _cell(f, 300, yt, 370, yt)
    f.line(370, yt, 440, yt)
    for x, lab in ((155, "E₁"), (265, "E₂"), (335, "E₃")):
        f.text(x + 10, yt - 18, lab, size=13, anchor="start")
        f.text(x + 10, yt + 26, "2 V", size=12, anchor="start")
    _cell(f, 80, yb, 440, yb)
    f.text(270, yb - 16, "E₄", size=13, anchor="start"); f.text(270, yb + 28, "6 V", size=12, anchor="start")
    return f.svg()


def fig_q1b4_vsf():
    """Q1(B)(iv): V_s against f — solid line from the threshold on the f-axis, dashed extension to the V_s axis."""
    f = Fig(340, 280, "fig_q1b4_vsf")
    ox, oy = 50, 170
    f.arrow(30, oy, 320, oy); f.arrow(ox, 265, ox, 18)
    f.text(316, oy + 22, "f", size=15, italic=True, anchor="end")
    f.text(ox - 6, 26, "V", size=15, italic=True, anchor="end", sub="S")
    f.text(ox - 10, oy + 18, "0", size=13, anchor="end")
    x0 = 145
    f.line(x0, oy, 300, oy - 155 * (300 - x0) / 250 * 1.05, w=1.6)
    k = 155 / 250 * 1.05
    f.line(ox, oy + k * (x0 - ox), x0, oy, dash="5 4")
    return f.svg()


def fig_q5_parts():
    """Q5(a): the lens (focal length f) cut along the dashed principal axis; Fig 1 = the two upper halves side by side;
    Fig 2 = an upper half beside a lower (inverted) half."""
    f = Fig(520, 200, "fig_q5_parts")
    def biconvex(x, y, h, w):
        f.path(f"M {x} {y-h} Q {x+w} {y} {x} {y+h} Q {x-w} {y} {x} {y-h} Z", fill="#e8f1fb", color=BLUE)
    def upper(x, y, h, w):     # upper half: flat edge at y (the cut), apex at y-h
        f.path(f"M {x-w/2:.1f} {y} Q {x-w/2:.1f} {y-h*0.55:.1f} {x} {y-h} Q {x+w/2:.1f} {y-h*0.55:.1f} {x+w/2:.1f} {y} Z",
               fill="#e8f1fb", color=BLUE)
    def lower(x, y, h, w):     # lower half: flat edge at y, apex at y+h
        f.path(f"M {x-w/2:.1f} {y} Q {x-w/2:.1f} {y+h*0.55:.1f} {x} {y+h} Q {x+w/2:.1f} {y+h*0.55:.1f} {x+w/2:.1f} {y} Z",
               fill="#e8f1fb", color=BLUE)
    biconvex(70, 95, 70, 30)
    f.line(20, 95, 125, 95, dash="5 4", w=1.2)
    f.text(70, 190, "f", size=15, bold=True, italic=True)
    upper(200, 110, 70, 50); upper(250, 110, 70, 50)
    f.text(225, 145, "Fig 1", size=14)
    f.text(320, 100, "and", size=15, bold=True)
    upper(410, 120, 70, 50); lower(460, 75, 70, 50)
    f.text(435, 175, "Fig 2", size=14)
    return f.svg()


def fig_q6_prism():
    """Q6: right-angled prism ABC (90 deg at B, 45 deg at C); a ray enters AB normally and, at AC, leaves along AC."""
    f = Fig(440, 240, "fig_q6_prism")
    A, B, C = (130, 25), (130, 205), (310, 205)
    f.path(_poly([A, B, C, A]), fill="#eef4fb", color="#111", w=1.8)
    f.rect(130, 190, 15, 15, w=1)
    yr = 110
    xh = A[0] + (yr - A[1])          # point on AC (45 deg: x - 130 = y - 25)
    f.arrow(20, yr, 90, yr); f.line(90, yr, xh, yr)
    # emergent ray along AC, heavy
    f.arrow(xh, yr, xh + 70, yr + 70, w=2.6)
    _arc(f, C[0], C[1], 38, 180, 135)
    f.text(C[0] - 52, C[1] - 10, "45°", size=12)
    f.text(A[0], A[1] - 8, "A", size=14, bold=True)
    f.text(B[0] - 4, B[1] + 20, "B", size=14, bold=True)
    f.text(C[0] + 6, C[1] + 20, "C", size=14, bold=True)
    return f.svg()


def _q11_layout(f, show_currents):
    L, Mx, R = 90, 300, 410
    T, Bm = 60, 190
    # left cell (+ at top)
    f.line(L, T, L, 112); f.line(L, 138, L, Bm)
    f.line(L - 13, 121, L + 13, 121, w=2.0); f.line(L - 6, 129, L + 6, 129, w=3.4)
    f.text(L - 20, 130, "3 V, 2 Ω", size=13, anchor="end")
    _res(f, L, T, Mx, T, n=5, lead=0.4); f.text((L + Mx) / 2, T - 14, "2.5 Ω", size=13)
    _res(f, L, Bm, Mx, Bm, n=5, lead=0.4); f.text((L + Mx) / 2, Bm + 26, "4 Ω", size=13)
    _res(f, Mx, T, Mx, Bm, n=5, lead=0.35); f.text(Mx - 14, (T + Bm) / 2 + 5, "2 Ω", size=13, anchor="end")
    _res(f, Mx, T, R, T, n=4, lead=0.3); f.text((Mx + R) / 2, T - 14, "5 Ω", size=13)
    # diagonal R -> bottom node: 3.5 ohm near the top, the 2 V cell near the bottom (+ towards bottom node)
    P1 = (R, T); P2 = (Mx, Bm)
    ux, uy, Ld = _unit(P1[0], P1[1], P2[0], P2[1])
    Pm = (P1[0] + ux * Ld * 0.5, P1[1] + uy * Ld * 0.5)
    _res(f, P1[0], P1[1], Pm[0], Pm[1], n=4, lead=0.2)
    _cell(f, Pm[0], Pm[1], P2[0], P2[1], plus_at_start=False)
    ang = math.degrees(math.atan2(P2[1] - P1[1], P2[0] - P1[0])) - 180
    _rtext(f, 392, 120, "3.5 Ω", ang, size=13)
    _rtext(f, 358, 178, "2 V, 0.5 Ω", ang, size=13)
    for P, t, dx, dy in (((Mx, T), "P", 0, -8), ((Mx, Bm), "Q", 0, 20)):
        _dot(f, P[0], P[1], 3)
        if show_currents:
            f.text(P[0] + dx + 10, P[1] + dy, t, size=14, bold=True, anchor="start")
    if show_currents:
        f.arrow(150, T + 14, 215, T + 14, color=RED, w=1.6); f.text(185, T + 32, "I₁", size=14, color=RED)
        f.arrow(Mx + 14, 105, Mx + 14, 150, color=GREEN, w=1.6); f.text(Mx + 20, 132, "I₂", size=14, color=GREEN, anchor="start")
        f.arrow(330, T + 14, 380, T + 14, color=BLUE, w=1.6); f.text(355, T + 32, "I₃", size=14, color=BLUE)
        f.arrow(240, Bm - 14, 150, Bm - 14, color=RED, w=1.6); f.text(195, Bm - 22, "I₁", size=14, color=RED)


def fig_q11_circuit():
    f = Fig(480, 240, "fig_q11_circuit")
    _q11_layout(f, False)
    return f.svg()


def _q16_levels(f, arrow):
    f.rect(20, 15, 300, 300, w=1.2)
    f.text(30, 35, "Diagram 1", size=13, bold=True, anchor="start")
    f.arrow(50, 300, 50, 45, w=2.6)
    _vtext(f, 36, 220, "energy / eV", size=12)
    E = [-0.378, -0.544, -0.850, -1.51, -3.40]
    ys = {}
    for e in E:
        y = 300 - (e + 3.40) / (3.40 - 0.30) * 255 + 0
        ys[e] = y
        f.line(70, y, 245, y, w=1.2)
    # labels (the top two lines are close: offset the labels)
    f.text(252, ys[-0.378] + 1, "−0.378", size=12, anchor="start")
    f.text(252, ys[-0.544] + 11, "−0.544", size=12, anchor="start")
    f.text(252, ys[-0.850] + 4, "−0.850", size=12, anchor="start")
    f.text(252, ys[-1.51] + 4, "−1.51", size=12, anchor="start")
    f.text(252, ys[-3.40] + 4, "−3.40", size=12, anchor="start")
    if arrow:
        f.arrow(160, ys[-1.51], 160, ys[-3.40] - 2, color=RED, w=2.4)
        f.text(168, (ys[-1.51] + ys[-3.40]) / 2, "658 nm", size=13, color=RED, anchor="start")
        f.text(168, (ys[-1.51] + ys[-3.40]) / 2 + 18, "(1.89 eV)", size=12, color=RED, anchor="start")
    # Diagram 2
    X0 = 350
    f.text(X0, 35, "Diagram 2", size=13, bold=True, anchor="start")
    f.rect(X0, 55, 250, 45, color=GREY, w=1)
    scale = 250 / (680 - 400)
    for lam in (411, 435, 488, 658):
        x = X0 + (lam - 400) * scale
        f.line(x, 55, x, 100, w=1.4)
        f.text(x, 116, str(lam), size=12)
    f.arrow(X0, 128, X0 + 262, 128, w=1.6)
    f.text(X0 + 125, 148, "λ / nm", size=13, italic=True)


def fig_q16_diagrams():
    f = Fig(620, 330, "fig_q16_diagrams")
    _q16_levels(f, False)
    return f.svg()


# ================================================================= ANSWER figures
def fig_a1a1_forces():
    """Forces on X: attraction towards Y, repulsion away from Z, equal magnitudes; resultant along XA."""
    f = Fig(340, 210, "fig_a1a1_forces")
    X, Y, Z = (190, 70), (130, 174), (250, 174)
    f.line(X[0], X[1], Y[0], Y[1], color=GREY, w=0.8, dash="2 3")
    f.line(X[0], X[1], Z[0], Z[1], color=GREY, w=0.8, dash="2 3")
    f.line(Y[0], Y[1], Z[0], Z[1], color=GREY, w=0.8, dash="2 3")
    for P in (X, Y, Z):
        _dot(f, P[0], P[1], 6)
    f.text(X[0] + 14, X[1] - 8, "X (+q)", size=13, bold=True, anchor="start")
    f.text(Y[0], Y[1] + 24, "Y (−q)", size=13, bold=True)
    f.text(Z[0], Z[1] + 24, "Z (+q)", size=13, bold=True)
    L = 80
    fy = (X[0] - L * 0.5, X[1] + L * math.sqrt(3) / 2)    # towards Y
    fz = (X[0] - L * 0.5, X[1] - L * math.sqrt(3) / 2)    # away from Z
    f.arrow(X[0], X[1], fy[0], fy[1], color=BLUE, w=2)
    f.text(fy[0] - 8, fy[1] + 2, "F", size=14, color=BLUE, anchor="end", sub="XY")
    f.arrow(X[0], X[1], fz[0], fz[1], color=GREEN, w=2)
    f.text(fz[0] - 6, fz[1] + 10, "F", size=14, color=GREEN, anchor="end", sub="XZ")
    f.line(fy[0], fy[1], X[0] - L, X[1], color=GREY, w=1, dash="4 3")
    f.line(fz[0], fz[1], X[0] - L, X[1], color=GREY, w=1, dash="4 3")
    f.arrow(X[0], X[1], X[0] - L - 2, X[1], color=RED, w=2.6)
    f.text(X[0] - L - 8, X[1] + 5, "initial F (along XA)", size=13, color=RED, anchor="end")
    _arc(f, X[0], X[1], 26, 180, 240, color=GREY)
    _arc(f, X[0], X[1], 30, 120, 180, color=GREY)
    f.text(X[0] - 40, X[1] + 26, "60°", size=11, color=GREY)
    f.text(X[0] - 40, X[1] - 18, "60°", size=11, color=GREY)
    return f.svg()


def _a1a1_trajectory(stop_y=0.40, dt=2e-4):
    """Integrate the motion of X (+q, released from rest at the apex) under Y (-q) and Z (+q), both fixed.
    Units: side of the triangle = 1, k q^2 / m = 1.  Returns the list of (x, y) points, y measured up from YZ."""
    Y, Z = (-0.5, 0.0), (0.5, 0.0)
    x, y, vx, vy = 0.0, math.sqrt(3) / 2, 0.0, 0.0
    pts = [(x, y)]
    while y > stop_y:
        dyx, dyy = x - Y[0], y - Y[1]; ry = math.hypot(dyx, dyy) ** 3
        dzx, dzy = x - Z[0], y - Z[1]; rz = math.hypot(dzx, dzy) ** 3
        ax = -dyx / ry + dzx / rz
        ay = -dyy / ry + dzy / rz
        vx += ax * dt; vy += ay * dt; x += vx * dt; y += vy * dt
        pts.append((x, y))
    return pts


def fig_a1a1_path():
    """The actual path of X, computed numerically (side = 120 px): it starts along XA (the initial force) and bends
    downwards towards Y, because once X has moved left it is nearer to Y (attraction grows) and farther from Z."""
    f = Fig(340, 210, "fig_a1a1_path")
    s, ox, oy = 120, 190, 174            # YZ midpoint at (190, 174); y up in physics -> minus on screen
    P = lambda q: (ox + s * q[0], oy - s * q[1])
    X, Y, Z = P((0, math.sqrt(3) / 2)), P((-0.5, 0)), P((0.5, 0))
    f.line(X[0], X[1], 60, X[1], color=GREY, w=1, dash="4 3"); f.text(52, X[1] + 5, "A", size=14, bold=True, anchor="end")
    pts = [P(q) for q in _a1a1_trajectory()]
    f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts[::40] + [pts[-1]]), color=RED, w=2.2, arrow=True)
    f.text(pts[-1][0] - 10, pts[-1][1] + 6, "B", size=14, bold=True, color=RED, anchor="end")
    f.arrow(X[0], X[1], X[0] - 46, X[1], color=BLUE, w=1.6)
    f.text(X[0] - 22, X[1] - 8, "initial F", size=11, color=BLUE)
    for Q_, t in ((X, "X (+q)"), (Y, "Y (−q)"), (Z, "Z (+q)")):
        _dot(f, Q_[0], Q_[1], 6)
    f.text(X[0] + 12, X[1] - 8, "X (+q)", size=13, bold=True, anchor="start")
    f.text(Y[0], Y[1] + 24, "Y (−q)", size=13, bold=True)
    f.text(Z[0], Z[1] + 24, "Z (+q)", size=13, bold=True)
    return f.svg()


def fig_a1a2_bridge():
    """Answer: no current in A-D-C; current I circulates A -> C -> B -> A through the 10 V cell."""
    f = Fig(300, 380, "fig_a1a2_bridge")
    A, B, C, D = (60, 190), (150, 40), (240, 190), (150, 340)
    _cell(f, A[0], A[1], B[0], B[1], plus_at_start=True)
    f.text(78, 108, "10 V", size=13, anchor="end")
    _res(f, B[0], B[1], C[0], C[1], n=4)
    f.text(212, 108, "R", size=15, italic=True, anchor="start")
    _res(f, A[0], A[1], C[0], C[1], n=4, lead=0.35)
    f.text(150, 176, "100 Ω", size=13)
    mx, my = 95, 248
    ux, uy, L = _unit(A[0], A[1], D[0], D[1])
    f.line(A[0], A[1], mx - ux * 14, my - uy * 14)
    f.line(mx + ux * 14, my + uy * 14, D[0], D[1])
    _meter(f, mx, my, "A", r=14)
    _cell(f, D[0], D[1], C[0], C[1], plus_at_start=True)
    f.text(212, 284, "4 V", size=13, anchor="start")
    for P, t, dx, dy in ((A, "A", -14, 5), (B, "B", 0, -10), (C, "C", 14, 5), (D, "D", 0, 24)):
        _dot(f, P[0], P[1], 2.5)
        f.text(P[0] + dx, P[1] + dy, t, size=15, bold=True)
    f.arrow(110, 205, 190, 205, color=RED, w=1.8); f.text(150, 222, "I", size=14, color=RED, italic=True)
    f.arrow(236, 132, 206, 80, color=RED, w=1.8)
    f.text(120, 300, "I = 0", size=13, color=RED, anchor="end")
    return f.svg()


def fig_a1b4_vsf():
    """Answer: slope triangle on the V_s-f line; slope = h/e, intercepts f0 and -phi0/e."""
    f = Fig(360, 290, "fig_a1b4_vsf")
    ox, oy = 50, 170
    f.arrow(30, oy, 340, oy); f.arrow(ox, 275, ox, 18)
    f.text(336, oy + 22, "f", size=15, italic=True, anchor="end")
    f.text(ox - 6, 26, "V", size=15, italic=True, anchor="end", sub="S")
    x0 = 145; k = 0.62
    line = lambda x: oy - k * (x - x0)
    f.line(x0, oy, 320, line(320), color=BLUE, w=2)
    f.line(ox, line(ox), x0, oy, color=BLUE, w=1.4, dash="5 4")
    xa, xb = 200, 290
    f.line(xa, line(xa), xb, line(xa), color=RED, w=1.4)
    f.line(xb, line(xa), xb, line(xb), color=RED, w=1.4)
    f.text((xa + xb) / 2, line(xa) + 18, "Δf", size=13, color=RED)
    f.text(xb + 6, (line(xa) + line(xb)) / 2 + 4, "ΔV", size=13, color=RED, anchor="start", sub="S")
    f.text(x0, oy + 20, "f₀", size=14)
    f.text(ox + 6, line(ox) + 5, "−φ₀/e", size=13, anchor="start")
    _lab(f, 200, 58, [("slope = ΔV", 0), ("S", 1), ("/Δf = h/e", 0)], size=13, anchor="middle")
    return f.svg()


def fig_a3b_xlxc():
    f = Fig(380, 270, "fig_a3b_xlxc")
    ox, oy = 50, 235
    _axes(f, ox, oy, 360, 15, "f", "X")
    k = 0.75; A = 4200
    f.line(ox, oy, 330, oy - k * (330 - ox), color=RED, w=2.2)
    pts = [(ox + t, oy - A / t) for t in [x / 2 for x in range(30, 561)] if A / t < 215]
    f.path(_poly(pts), color=BLUE, w=2.2)
    _lab(f, 300, oy - k * (330 - ox) + 4, [("X", 0), ("L", 1), (" = 2πfL", 0)], color=RED, anchor="end")
    _lab(f, 340, oy - A / 290 - 10, [("X", 0), ("C", 1), (" = 1/(2πfC)", 0)], color=BLUE, anchor="end")
    t0 = math.sqrt(A / k)
    f.line(ox + t0, oy - k * t0, ox + t0, oy, color=GREY, w=1, dash="4 3")
    f.text(ox + t0, oy + 18, "f₀", size=13)
    _lab(f, ox + t0 + 8, oy - k * t0 + 4, [("X", 0), ("L", 1), (" = X", 0), ("C", 1)], size=12, color=GREY, anchor="start")
    return f.svg()


def fig_a5a_parts():
    """Answer: in both arrangements each piece is a lens of focal length f; the two act as thin lenses in contact."""
    f = Fig(460, 150, "fig_a5a_parts")
    def upper(x, y, h, w):
        f.path(f"M {x-w/2:.1f} {y} Q {x-w/2:.1f} {y-h*0.55:.1f} {x} {y-h} Q {x+w/2:.1f} {y-h*0.55:.1f} {x+w/2:.1f} {y} Z",
               fill="#e8f1fb", color=BLUE)
    def lower(x, y, h, w):
        f.path(f"M {x-w/2:.1f} {y} Q {x-w/2:.1f} {y+h*0.55:.1f} {x} {y+h} Q {x+w/2:.1f} {y+h*0.55:.1f} {x+w/2:.1f} {y} Z",
               fill="#e8f1fb", color=BLUE)
    upper(80, 95, 70, 50); upper(130, 95, 70, 50)
    f.text(80, 118, "f", size=14, italic=True); f.text(130, 118, "f", size=14, italic=True)
    f.text(105, 142, "Fig 1: F = f/2", size=13, color=RED)
    upper(310, 105, 70, 50); lower(360, 60, 70, 50)
    f.text(310, 128, "f", size=14, italic=True); f.text(360, 50, "f", size=14, italic=True)
    f.text(335, 142, "Fig 2: F = f/2", size=13, color=RED)
    return f.svg()


def fig_a5b_newton():
    """Convex lens f = 10 (scale 9 px/unit): object at u = -15 (x = 5 beyond F1), image at v = +30 (y = 20 beyond F2)."""
    s = 9
    f = Fig(520, 250, "fig_a5b_newton")
    O = (190, 115)
    fl, u, v = 10, -15, 30
    h = 4; hi = h * v / u
    X = lambda d: O[0] + d * s
    Y = lambda hh: O[1] - hh * s
    f.line(20, O[1], 505, O[1], color=GREY, w=1)
    _lens(f, O[0], O[1], 70)
    for d, t in ((-fl, "F₁"), (fl, "F₂")):
        _dot(f, X(d), O[1], 3); f.text(X(d), O[1] + 18, t, size=13)
    f.arrow(X(u), O[1], X(u), Y(h), color=GREEN, w=2.4); f.text(X(u) - 6, Y(h) - 4, "A", size=13, anchor="end")
    f.arrow(X(v), O[1], X(v), Y(hi), color=RED, w=2.4); f.text(X(v) + 6, Y(hi) + 6, "A′", size=13, anchor="start")
    # ray 1: parallel, then through F2
    f.line(X(u), Y(h), O[0], Y(h), color=ORANGE, w=1.5)
    f.line(O[0], Y(h), X(v), Y(hi), color=ORANGE, w=1.5)
    # ray 2: through optical centre
    f.line(X(u), Y(h), X(v), Y(hi), color=PURPLE, w=1.5)
    # ray 3: through F1, then parallel
    yl = h + (0 - h) * (0 - u) / (-fl - u)     # height where the F1-ray meets the lens
    f.line(X(u), Y(h), O[0], Y(yl), color="#16a085", w=1.5)
    f.line(O[0], Y(yl), X(v), Y(yl), color="#16a085", w=1.5)
    # x and y dimension lines
    yd = O[1] + 52
    f.line(X(u), yd, X(-fl), yd, color=BLUE, w=1.2); f.line(X(u), yd - 5, X(u), yd + 5, color=BLUE); f.line(X(-fl), yd - 5, X(-fl), yd + 5, color=BLUE)
    f.text((X(u) + X(-fl)) / 2, yd + 18, "x", size=15, italic=True, color=BLUE)
    yd2 = O[1] - 50
    f.line(X(fl), yd2, X(v), yd2, color=BLUE, w=1.2); f.line(X(fl), yd2 - 5, X(fl), yd2 + 5, color=BLUE); f.line(X(v), yd2 - 5, X(v), yd2 + 5, color=BLUE)
    f.text((X(fl) + X(v)) / 2, yd2 - 8, "y", size=15, italic=True, color=BLUE)
    f.text(O[0] + 6, O[1] + 18, "O", size=13, anchor="start")
    f.text(O[0], 240, "u = −(f + x),  v = +(f + y)", size=12, color=GREY)
    return f.svg()


def fig_a6_prism():
    f = Fig(440, 250, "fig_a6_prism")
    A, B, C = (130, 25), (130, 205), (310, 205)
    f.path(_poly([A, B, C, A]), fill="#eef4fb", color="#111", w=1.8)
    f.rect(130, 190, 15, 15, w=1)
    yr = 110
    xh = A[0] + (yr - A[1])
    f.arrow(20, yr, 90, yr, color=RED, w=1.8); f.line(90, yr, xh, yr, color=RED, w=1.8)
    f.arrow(xh, yr, xh + 72, yr + 72, color=RED, w=2.4)
    # normal to AC at the point of incidence: AC direction (1,1)/√2, normal (1,-1)/√2
    n = 60
    f.line(xh - n / math.sqrt(2), yr + n / math.sqrt(2), xh + n / math.sqrt(2), yr - n / math.sqrt(2), color=GREY, w=1, dash="5 4")
    f.text(xh + n / math.sqrt(2) + 4, yr - n / math.sqrt(2) - 2, "N", size=12, color=GREY, anchor="start")
    _arc(f, xh, yr, 30, 180, 225, color=BLUE)
    f.text(xh - 38, yr + 22, "i = 45°", size=12, color=BLUE, anchor="end")
    _arc(f, xh, yr, 24, 45, -45, color=GREEN)
    f.text(xh + 32, yr + 4, "e = 90°", size=12, color=GREEN, anchor="start")
    _arc(f, C[0], C[1], 38, 180, 135)
    f.text(C[0] - 52, C[1] - 10, "45°", size=12)
    f.text(A[0], A[1] - 8, "A", size=14, bold=True)
    f.text(B[0] - 4, B[1] + 20, "B", size=14, bold=True)
    f.text(C[0] + 6, C[1] + 20, "C", size=14, bold=True)
    f.text(60, yr - 10, "normal incidence on AB", size=11, color=GREY)
    f.text(220, 240, "i at AC = C (critical angle) = 45°", size=12, color=RED)
    return f.svg()


def fig_a9_parallel():
    f = Fig(360, 230, "fig_a9_parallel")
    xl, xr = 90, 270
    y1, y2 = 50, 120
    f.line(xl, y1, xl, y2); f.line(xr, y1, xr, y2)
    for y, lab, q in ((y1, "C₁", "+Q₁  −Q₁"), (y2, "C₂", "+Q₂  −Q₂")):
        f.line(xl, y, 176, y); _cap_h(f, 180, y); f.line(184, y, xr, y)
        f.text(180, y - 18, lab, size=14, bold=True)
        f.text(180, y + 30, q, size=11, color=GREY)
    _dot(f, xl, 85); _dot(f, xr, 85)
    f.text(xl - 10, 80, "A", size=14, bold=True, anchor="end"); f.text(xr + 10, 80, "B", size=14, bold=True, anchor="start")
    f.line(xl, 85, 40, 85); f.line(40, 85, 40, 195)
    f.line(xr, 85, 320, 85); f.line(320, 85, 320, 195)
    f.line(40, 195, 176, 195); f.line(184, 195, 320, 195)
    f.line(176, 182, 176, 208, w=2.0); f.line(184, 188, 184, 202, w=3.4)
    f.text(180, 222, "V", size=14, italic=True)
    f.arrow(60, 175, 60, 105, color=RED, w=1.4); f.text(66, 145, "Q = Q₁ + Q₂", size=12, color=RED, anchor="start")
    return f.svg()


def fig_a10_cube():
    """Charge q at the centre of an imaginary cube of side 10 cm; the given plate is one face."""
    f = Fig(320, 250, "fig_a10_cube")
    a, dx, dy = 140, 55, -45
    x0, y0 = 70, 220
    F = [(x0, y0), (x0 + a, y0), (x0 + a, y0 - a), (x0, y0 - a)]
    Bk = [(x + dx, y + dy) for x, y in F]
    # the given plate = top face, shaded
    top = [F[3], F[2], Bk[2], Bk[3]]
    f.path(_poly(top) + " Z", fill="#f6d5cf", color=RED, w=2)
    f.path(_poly(F) + " Z", color="#111", w=1.4)
    f.line(F[1][0], F[1][1], Bk[1][0], Bk[1][1]); f.line(F[2][0], F[2][1], Bk[2][0], Bk[2][1])
    f.line(Bk[1][0], Bk[1][1], Bk[2][0], Bk[2][1])
    f.line(F[0][0], F[0][1], Bk[0][0], Bk[0][1], dash="4 3", color=GREY)
    f.line(Bk[0][0], Bk[0][1], Bk[1][0], Bk[1][1], dash="4 3", color=GREY)
    f.line(Bk[0][0], Bk[0][1], Bk[3][0], Bk[3][1], dash="4 3", color=GREY)
    cx, cy = x0 + a / 2 + dx / 2, y0 - a / 2 + dy / 2
    _dot(f, cx, cy, 5, color=BLUE); f.text(cx + 10, cy + 5, "q = 2 μC", size=13, color=BLUE, anchor="start")
    tx, ty = x0 + a / 2 + dx / 2, y0 - a + dy / 2
    f.line(cx, cy, tx, ty, color=BLUE, w=1, dash="3 3")
    f.text(cx - 6, (cy + ty) / 2 + 4, "5 cm", size=12, color=BLUE, anchor="end")
    f.text(x0 + a / 2, y0 + 20, "10 cm", size=12)
    f.text(Bk[2][0] - 10, Bk[2][1] - 10, "given plate (side 10 cm)", size=12, color=RED, anchor="end")
    return f.svg()


def fig_a11_circuit():
    f = Fig(480, 240, "fig_a11_circuit")
    _q11_layout(f, True)
    return f.svg()


def fig_a12_loop():
    """Circular coil, radius r, centre O; element dl tangent; dB at O perpendicular to the plane."""
    f = Fig(380, 250, "fig_a12_loop")
    O = (170, 125); R = 90
    f.circle(O[0], O[1], R, w=2)
    _dot(f, O[0], O[1], 3); f.text(O[0] - 8, O[1] + 18, "O", size=14, bold=True)
    a = math.radians(140)
    P = (O[0] + R * math.cos(a), O[1] - R * math.sin(a))
    t = (-math.sin(a), -math.cos(a))           # anticlockwise tangent on screen
    f.arrow(P[0] - 20 * t[0], P[1] - 20 * t[1], P[0] + 24 * t[0], P[1] + 24 * t[1], color=RED, w=2.4)
    f.text(P[0] - 30, P[1] - 4, "dl", size=14, color=RED, italic=True, anchor="end")
    f.line(P[0], P[1], O[0], O[1], color=BLUE, w=1.4, dash="5 3")
    f.text((P[0] + O[0]) / 2 + 6, (P[1] + O[1]) / 2 - 4, "r", size=14, italic=True, color=BLUE, anchor="start")
    # current arrows round the loop (anticlockwise as seen)
    for ang in (20, 260):
        b = math.radians(ang)
        Q = (O[0] + R * math.cos(b), O[1] - R * math.sin(b))
        tq = (-math.sin(b), -math.cos(b))
        f.arrow(Q[0] - 8 * tq[0], Q[1] - 8 * tq[1], Q[0] + 8 * tq[0], Q[1] + 8 * tq[1], w=2.2)
    f.text(O[0] + R + 8, O[1] - 24, "I", size=15, italic=True, anchor="start")
    # B out of the page at O (anticlockwise current)
    f.circle(O[0] + 30, O[1] + 4, 9, color=GREEN, w=1.6); _dot(f, O[0] + 30, O[1] + 4, 2.5, color=GREEN)
    f.text(O[0], O[1] + 50, "dB out of the page", size=12, color=GREEN)
    f.text(O[0], 240, "dl ⊥ r everywhere: θ = 90°", size=12, color=GREY)
    return f.svg()


def fig_a13a_phasor():
    """Phasors to scale: I0 = 0.447 A; V_R0 = 44.7 V, V_L0 = 178.9 V, V_C0 = 268.3 V (scale 0.55 px/V)."""
    f = Fig(420, 290, "fig_a13a_phasor")
    s = 0.55
    ox, oy = 90, 125
    VR, VL, VC = 44.72, 178.89, 268.33
    f.line(40, oy, 400, oy, color=GREY, w=1)
    f.arrow(ox + 150, oy, ox + 210, oy, color="#555", w=1.2); f.text(ox + 216, oy + 5, "I", size=14, italic=True, anchor="start")
    f.arrow(ox, oy, ox + VR * s, oy, color=GREEN, w=2.6)
    _lab(f, ox + 8, oy - 14, [("V", 0), ("R0", 1), (" = 44.7 V", 0)], size=12, color=GREEN, anchor="start")
    f.arrow(ox, oy, ox, oy - VL * s, color=RED, w=2.4)
    _lab(f, ox - 8, oy - VL * s + 8, [("V", 0), ("L0", 1), (" = 178.9 V", 0)], size=12, color=RED, anchor="end")
    f.arrow(ox, oy, ox, oy + VC * s, color=BLUE, w=2.4)
    _lab(f, ox - 8, oy + VC * s - 4, [("V", 0), ("C0", 1), (" = 268.3 V", 0)], size=12, color=BLUE, anchor="end")
    d = (VC - VL) * s
    f.line(ox + VR * s, oy, ox + VR * s, oy + d, color=ORANGE, dash="5 3")
    _lab(f, ox + VR * s + 8, oy + d / 2 + 4, [("V", 0), ("C0", 1), (" − V", 0), ("L0", 1), (" = 89.4 V", 0)], size=12, color=ORANGE, anchor="start")
    f.arrow(ox, oy, ox + VR * s, oy + d, color="#111", w=2.6)
    f.text(ox + VR * s + 8, oy + d + 16, "V₀ = 100 V", size=13, anchor="start")
    _arc(f, ox, oy, 18, 0, -math.degrees(math.atan2(d, VR * s)))
    f.text(ox + 4, oy + 32, "φ", size=13, italic=True, anchor="start")
    f.text(ox + 140, oy - 80, "V₀ lags I by φ = 63.4°", size=12, color=GREY, anchor="start")
    _lab(f, ox + 140, oy - 62, [("(X", 0), ("C", 1), (" > X", 0), ("L", 1), (": current leads)", 0)], size=12, color=GREY, anchor="start")
    return f.svg()


def fig_a15a_huygens():
    """Refraction of a plane wavefront at XY: v1 > v2; BC = v1 t, AE = v2 t; i = 50 deg, n2/n1 = 1.5."""
    f = Fig(520, 360, "fig_a15a_huygens")
    i = math.radians(50); ratio = 1 / 1.5
    r = math.asin(math.sin(i) * ratio)
    ys = 175
    A = (150, ys); AC = 230; C = (A[0] + AC, ys)
    d = (math.sin(i), math.cos(i))
    v1t = AC * math.sin(i)
    B = (C[0] - v1t * d[0], C[1] - v1t * d[1])
    v2t = AC * math.sin(r)
    dr = (math.sin(r), math.cos(r))
    E = (A[0] + v2t * dr[0], A[1] + v2t * dr[1])
    f.rect(15, ys, 490, 175, color="none", fill="#eaf2fb", w=0)
    f.line(15, ys, 505, ys, w=2.2)
    f.text(25, ys - 8, "X", size=13, bold=True, anchor="start"); f.text(495, ys - 8, "Y", size=13, bold=True, anchor="end")
    f.text(505, 26, "medium 1: speed v₁, refractive index μ₁", size=12, anchor="end")
    f.text(25, 342, "medium 2: speed v₂ (< v₁), refractive index μ₂", size=12, anchor="start")
    k = 120
    f.line(A[0] - k * d[0], A[1] - k * d[1], A[0], A[1], color=RED, w=1.8)
    f.arrow(A[0] - k * d[0], A[1] - k * d[1], A[0] - 0.45 * k * d[0], A[1] - 0.45 * k * d[1], color=RED, w=1.8)
    f.line(B[0] - 70 * d[0], B[1] - 70 * d[1], C[0], C[1], color=RED, w=1.8)
    f.arrow(B[0] - 70 * d[0], B[1] - 70 * d[1], B[0] - 20 * d[0], B[1] - 20 * d[1], color=RED, w=1.8)
    f.arrow(A[0], A[1], E[0] + 50 * dr[0], E[1] + 50 * dr[1], color=GREEN, w=1.8)
    f.arrow(C[0], C[1], C[0] + 110 * dr[0], C[1] + 110 * dr[1], color=GREEN, w=1.8)
    f.line(A[0], A[1], B[0], B[1], color=BLUE, w=2.2)
    f.line(C[0], C[1], E[0], E[1], color=BLUE, w=2.2)
    f.path(f"M {A[0]-v2t:.1f} {ys} A {v2t:.1f} {v2t:.1f} 0 0 0 {A[0]+v2t:.1f} {ys}", color=GREY, w=1, dash="4 3")
    for P in (A, C):
        f.line(P[0], ys - 130, P[0], ys + 140, color=GREY, w=1, dash="5 4")
    _arc(f, A[0], A[1], 40, 90, 90 + 50); f.text(A[0] - 14, A[1] - 46, "i", size=14, italic=True)
    _arc(f, A[0], A[1], 46, 270, 270 + math.degrees(r)); f.text(A[0] + 30, A[1] + 50, "r", size=14, italic=True)
    for P, t, dx, dy in ((A, "A", -12, 18), (B, "B", 8, -10), (C, "C", 8, -8), (E, "E", -14, 6)):
        _dot(f, P[0], P[1], 3)
        f.text(P[0] + dx, P[1] + dy, t, size=14, bold=True)
    f.text((B[0] + C[0]) / 2 + 26, (B[1] + C[1]) / 2 - 2, "v₁t", size=13, italic=True)
    f.text((A[0] + E[0]) / 2 - 30, (A[1] + E[1]) / 2 + 12, "v₂t", size=13, italic=True)
    return f.svg()


def fig_a15b_single_slit():
    f = Fig(460, 230, "fig_a15b_single_slit")
    ox, oy = 230, 190
    f.arrow(20, oy, 445, oy); f.arrow(ox, oy + 10, ox, 18)
    f.text(450, oy - 8, "sin θ", size=13, italic=True, anchor="end")
    f.text(ox + 8, 26, "I", size=15, italic=True, anchor="start")
    s = 60    # px per (lambda/a)
    pts = []
    for k in range(-400, 401):
        b = k / 400 * 3.5 * math.pi          # beta = pi a sin(theta)/lambda
        I = 1.0 if b == 0 else (math.sin(b) / b) ** 2
        x = ox + b / math.pi * s
        pts.append((x, oy - 155 * I))
    f.path(_poly(pts), color=BLUE, w=2.2)
    for n, t in ((1, "λ/a"), (2, "2λ/a"), (3, "3λ/a")):
        f.text(ox + n * s, oy + 18, t, size=11)
        f.text(ox - n * s, oy + 18, "−" + t, size=11)
    f.text(ox + 1.43 * s + 6, oy - 155 * 0.047 - 8, "I₀/22", size=10, color=GREY, anchor="start")
    f.text(ox - 8, 46, "I₀", size=12, anchor="end")
    f.text(ox + 2.46 * s + 6, oy - 155 * 0.016 - 8, "I₀/62", size=10, color=GREY, anchor="start")
    return f.svg()


def fig_a16_levels():
    f = Fig(620, 330, "fig_a16_levels")
    _q16_levels(f, True)
    return f.svg()


def fig_a18a_telescope():
    """Astronomical telescope, final image at D. f_o = 24, f_e = 6, D = 25 (scale 11 px/unit).
    Object at infinity: rays at angle alpha with tan(alpha) = 4/24, so I' is at F_o (24 behind the objective), height -4.
    Eyepiece: v_e = -25 -> u_e = -150/31 = -4.839; final image height -4 x 25/4.839 = -20.67, 25 in front of the eyepiece."""
    s = 11
    fo, fe, D = 24.0, 6.0, 25.0
    ue = 1 / (1 / -D - 1 / fe)
    h1 = -4.0
    hf = h1 * (-D) / ue
    xI = fo; xe = fo - ue; xF = xe - D
    f = Fig(640, 360, "fig_a18a_telescope")
    ox, oy = 110, 75
    X = lambda x: ox + x * s
    Y = lambda y: oy - y * s
    f.line(10, oy, 630, oy, color=GREY, w=1)
    _lens(f, X(0), oy, 52, bulge=6); _lens(f, X(xe), oy, 72, bulge=5)
    f.text(X(0) + 8, oy - 58, "Objective", size=13, anchor="start"); f.text(X(xe) + 8, oy - 62, "Eyepiece", size=13, anchor="start")
    _dot(f, X(fo), oy, 2.5); f.text(X(fo) + 3, oy - 8, "F₀", size=13, anchor="start")
    _dot(f, X(xe - fe), oy, 2.5); f.text(X(xe - fe) - 3, oy - 8, "Fₑ", size=13, anchor="end")
    m = h1 / fo
    outs = []
    for y0, col in ((3.5, RED), (0.0, ORANGE), (-3.5, PURPLE)):
        f.line(X(-9), Y(y0 - m * 9), X(0), Y(y0), color=col, w=1.5)
        f.arrow(X(-9), Y(y0 - m * 9), X(-5), Y(y0 - m * 5), color=col, w=1.5)
        mm = (h1 - y0) / fo
        ye = y0 + mm * xe
        f.line(X(0), Y(y0), X(xe), Y(ye), color=col, w=1.5)
        dxp, dyp = xe - xF, ye - hf
        t = 12 / dxp
        f.line(X(xe), Y(ye), X(xe + dxp * t), Y(ye + dyp * t), color=col, w=1.5)
        f.arrow(X(xe), Y(ye), X(xe + dxp * t * 0.55), Y(ye + dyp * t * 0.55), color=col, w=1.5)
        f.line(X(xF), Y(hf), X(xe), Y(ye), color=col, w=0.8, dash="4 3")
        outs.append(ye + dyp * t)
    f.arrow(X(xI), oy, X(xI), Y(h1), color=GREEN, w=2.6); f.text(X(xI) - 4, Y(h1) + 14, "I′", size=14, color=GREEN, anchor="end")
    f.arrow(X(xF), oy, X(xF), Y(hf), color=BLUE, w=2.6, dash="6 3"); f.text(X(xF) - 8, Y(hf) + 4, "I (final image)", size=13, color=BLUE, anchor="end")
    ex = X(xe + 12) + 8; ey = Y(sum(outs) / 3)
    f.path(f"M {ex} {ey-18} Q {ex+16} {ey} {ex} {ey+18}", w=1.8)
    f.text(ex + 18, ey + 5, "eye", size=13, anchor="start")
    yd = Y(hf) + 24
    f.line(X(xF), yd, X(xe), yd, color=GREY, w=1); f.line(X(xF), yd - 5, X(xF), yd + 5, color=GREY); f.line(X(xe), yd - 5, X(xe), yd + 5, color=GREY)
    f.text((X(xF) + X(xe)) / 2, yd + 17, "D = 25 cm (least distance of distinct vision)", size=12, color=GREY)
    yd2 = oy + 90
    f.line(X(0), yd2, X(fo), yd2, color=GREY, w=1); f.line(X(0), yd2 - 5, X(0), yd2 + 5, color=GREY); f.line(X(fo), yd2 - 5, X(fo), yd2 + 5, color=GREY)
    f.text((X(0) + X(fo)) / 2, yd2 - 6, "f₀", size=14, color=GREY)
    f.line(X(xI), yd2, X(xe), yd2, color=GREY, w=1); f.line(X(xe), yd2 - 5, X(xe), yd2 + 5, color=GREY)
    f.text((X(xI) + X(xe)) / 2, yd2 - 6, "uₑ", size=14, color=GREY)
    f.text(X(-9) - 4, Y(3.5 - m * 9) + 4, "α", size=15, italic=True, anchor="end")
    f.text(ex - 4, ey + 40, "β", size=15, italic=True)
    return f.svg()


def fig_a18b_ydse():
    f = Fig(520, 280, "fig_a18b_ydse")
    xs, xsc = 90, 440
    cy = 140; hd = 45
    S1, S2 = (xs, cy - hd), (xs, cy + hd)
    f.line(xs, 20, xs, S1[1] - 6, w=3); f.line(xs, S1[1] + 6, xs, S2[1] - 6, w=3); f.line(xs, S2[1] + 6, xs, 260, w=3)
    f.line(xsc, 20, xsc, 260, w=3)
    f.line(xs, cy, xsc, cy, color=GREY, w=1, dash="5 4")
    P = (xsc, cy - 95)
    f.line(S1[0], S1[1], P[0], P[1], color=RED, w=1.4)
    f.line(S2[0], S2[1], P[0], P[1], color=RED, w=1.4)
    f.line(xs, cy, P[0], P[1], color=GREY, w=1, dash="3 3")
    # foot of perpendicular from S1 on S2P
    ux, uy, L = _unit(S2[0], S2[1], P[0], P[1])
    t = (S1[0] - S2[0]) * ux + (S1[1] - S2[1]) * uy
    N = (S2[0] + ux * t, S2[1] + uy * t)
    f.line(S1[0], S1[1], N[0], N[1], color=BLUE, w=1.2)
    _dot(f, N[0], N[1], 2.5, color=BLUE); f.text(N[0] + 4, N[1] + 14, "N", size=13, color=BLUE, anchor="start")
    for Q, t_, dx in ((S1, "S₁", -8), (S2, "S₂", -8)):
        _dot(f, Q[0], Q[1], 3); f.text(Q[0] + dx, Q[1] + 5, t_, size=14, anchor="end")
    _dot(f, P[0], P[1], 3); f.text(P[0] + 8, P[1] + 5, "P", size=14, bold=True, anchor="start")
    _dot(f, xsc, cy, 3); f.text(xsc + 8, cy + 5, "O", size=14, bold=True, anchor="start")
    f.line(xsc + 26, cy, xsc + 26, P[1], color=GREEN, w=1.2); f.text(xsc + 32, (cy + P[1]) / 2, "y", size=14, italic=True, color=GREEN, anchor="start")
    f.text(xs - 30, cy + 5, "d", size=14, italic=True, anchor="end")
    f.line(xs - 22, S1[1], xs - 22, S2[1], color=GREY, w=1)
    f.line(xs, 255, xsc, 255, color=GREY, w=1); f.text((xs + xsc) / 2, 250, "D", size=14, italic=True)
    th = math.degrees(math.atan2(cy - P[1], xsc - xs))
    _arc(f, xs, cy, 70, 0, th, color=GREEN); f.text(xs + 76, cy - 8, "θ", size=13, italic=True, anchor="start")
    f.text(N[0] - 2, N[1] - 10, "90°", size=10, color=BLUE, anchor="end")
    f.text(60, 275, "path difference S₂P − S₁P = S₂N = d sin θ", size=12, color=BLUE, anchor="start")
    return f.svg()


def _rails(f, answer):
    yt, yb = 50, 190
    f.line(40, yt, 420, yt, w=2.2); f.line(40, yb, 420, yb, w=2.2)
    _res(f, 60, yt, 60, yb, n=5, lead=0.3)
    f.text(46, 125, "R", size=15, italic=True, anchor="end")
    xr = 270
    for x in range(100, 420, 40):
        for y in range(75, 180, 35):
            if xr - 20 < x < xr + 150 and 95 < y < 160:
                continue
            f.line(x - 5, y - 5, x + 5, y + 5, color=GREY, w=1); f.line(x - 5, y + 5, x + 5, y - 5, color=GREY, w=1)
    f.text(400, 30, "B (into page)", size=12, color=GREY, anchor="end")
    xr = 270
    f.line(xr, yt - 8, xr, yb + 8, color="#333", w=5)
    f.text(xr + 8, yt - 10, "P", size=14, bold=True, anchor="start"); f.text(xr + 8, yb + 22, "Q", size=14, bold=True, anchor="start")
    f.arrow(xr + 12, 120, xr + 70, 120, color=GREEN, w=2.2); f.text(xr + 76, 115, "v", size=15, italic=True, color=GREEN, anchor="start")
    f.line(xr - 30, yt + 10, xr - 30, yb - 10, color=GREY, w=1); f.text(xr - 36, 100, "l", size=15, italic=True, anchor="end")
    if answer:
        f.arrow(xr + 12, 170, xr + 12, 82, color=RED, w=2); f.text(xr + 18, 98, "I", size=14, italic=True, color=RED, anchor="start")
        f.arrow(150, yt - 12, 90, yt - 12, color=RED, w=1.6)
        f.arrow(xr - 12, 168, xr - 70, 168, color=BLUE, w=2.2); f.text(xr - 76, 173, "F", size=13, color=BLUE, anchor="end", sub="B")
        f.text(xr + 92, 140, "(and F", size=13, color=GREEN, anchor="start", sub="ext"); f.text(xr + 146, 140, ")", size=13, color=GREEN, anchor="start")


def fig_a19a_rails():
    f = Fig(450, 230, "fig_a19a_rails")
    _rails(f, True)
    return f.svg()


def fig_a19b_lcr():
    f = Fig(420, 190, "fig_a19b_lcr")
    y = 50
    f.line(40, y, 90, y); _res(f, 90, y, 170, y, n=4, lead=0.15); f.text(130, y - 16, "R", size=14, italic=True)
    f.line(170, y, 200, y)
    # inductor (loops)
    d = f"M 200 {y}"
    for _ in range(4):
        d += " a 9 9 0 0 1 18 0"
    f.path(d); f.text(236, y - 18, "L", size=14, italic=True)
    f.line(272, y, 300, y); _cap_h(f, 304, y); f.line(308, y, 380, y); f.text(304, y - 18, "C", size=14, italic=True)
    f.line(40, y, 40, 150); f.line(380, y, 380, 150)
    f.line(40, 150, 194, 150); f.line(226, 150, 380, 150)
    f.circle(210, 150, 16, fill="#fff"); f.path("M 200 150 Q 205 140 210 150 T 220 150", w=1.4)
    f.text(210, 182, "V = V₀ sin ωt", size=13)
    f.arrow(110, 72, 170, 72, color=RED, w=1.4); f.text(140, 90, "I = I₀ sin(ωt − φ)", size=11, color=RED)
    return f.svg()


def fig_a19b_phasor():
    f = Fig(360, 300, "fig_a19b_phasor")
    ox, oy = 70, 170
    f.line(40, oy, 340, oy, color=GREY, w=1)
    sx, vl, vc = 170, 125, 50
    f.arrow(ox, oy, ox + sx, oy, color=GREEN, w=2.4)
    f.text(ox + sx - 10, oy + 20, "V", size=14, color=GREEN, sub="R")
    f.text(ox + sx + 66, oy + 22, "I₀", size=14, italic=True)
    f.arrow(ox + sx + 20, oy + 6, ox + sx + 75, oy + 6, color="#555", w=1.2)
    f.arrow(ox, oy, ox, oy - vl, color=RED, w=2.4); f.text(ox - 8, oy - vl + 4, "V", size=14, color=RED, anchor="end", sub="L")
    f.arrow(ox, oy, ox, oy + vc, color=BLUE, w=2.4); f.text(ox - 8, oy + vc + 4, "V", size=14, color=BLUE, anchor="end", sub="C")
    f.line(ox + sx, oy, ox + sx, oy - (vl - vc), color=ORANGE, w=1.6, dash="5 3")
    _lab(f, ox + sx + 6, oy - 30, [("V", 0), ("L", 1), (" − V", 0), ("C", 1)], size=13, color=ORANGE, anchor="start")
    f.arrow(ox, oy, ox + sx, oy - (vl - vc), color="#111", w=2.6)
    f.text(ox + 92, oy - 50, "V₀", size=15, bold=True)
    _arc(f, ox, oy, 45, 0, math.degrees(math.atan2(vl - vc, sx)))
    f.text(ox + 55, oy - 6, "φ", size=14, italic=True)
    _lab(f, 190, 285, [("drawn for X", 0), ("L", 1), (" > X", 0), ("C", 1), (" (V leads I)", 0)], size=12, color=GREY)
    return f.svg()


def fig_a20_bias():
    """Forward-bias circuit: battery -> potential divider (rheostat) -> milliammeter -> diode; voltmeter across diode.
    Reverse bias: battery reversed, microammeter."""
    f = Fig(480, 270, "fig_a20_bias")
    # battery at bottom
    yb, yt = 210, 60
    f.line(40, yb, 214, yb); f.line(226, yb, 420, yb)
    f.line(214, yb - 13, 214, yb + 13, w=2.0); f.line(226, yb - 6, 226, yb + 6, w=3.4)
    f.text(206, yb - 14, "+", size=14); f.text(234, yb - 14, "−", size=14)
    f.text(220, yb + 30, "battery", size=11, color=GREY)
    # rheostat as potential divider: resistor between the battery terminals, slider
    f.line(40, yb, 40, 150); f.line(420, yb, 420, 150)
    _res(f, 40, 150, 420, 150, n=8, lead=0.1)
    f.arrow(300, 115, 300, 142, w=1.4); f.text(306, 120, "sliding contact (rheostat)", size=11, anchor="start", color=GREY)
    # from the + end of the divider through mA to diode, back to slider
    f.line(40, 150, 40, yt); f.line(40, yt, 110, yt); _meter(f, 124, yt, "mA", r=14); f.line(138, yt, 200, yt)
    _diode(f, 200, 280, yt)
    f.text(228, yt + 26, "p", size=13); f.text(252, yt + 26, "n", size=13)
    f.line(280, yt, 300, yt); f.line(300, yt, 300, 115)
    # voltmeter across the diode
    f.line(200, yt, 200, 30); f.line(280, yt, 280, 30)
    f.line(200, 30, 226, 30); f.line(254, 30, 280, 30); _meter(f, 240, 30, "V", r=13)
    f.text(140, 105, "p-n junction diode (forward biased)", size=11, color=GREY)
    f.text(240, 262, "reverse bias: battery terminals interchanged, mA replaced by μA", size=11, color=GREY)
    return f.svg()


def fig_a20_iv():
    f = Fig(420, 320, "fig_a20_iv")
    ox, oy = 250, 170
    f.arrow(20, oy, 405, oy); f.arrow(ox, 310, ox, 15)
    f.text(405, oy - 8, "V (volt)", size=12, anchor="end")
    f.text(ox + 6, 22, "I (mA)", size=12, anchor="start")
    f.text(ox + 6, 305, "I (μA)", size=12, anchor="start")
    f.text(30, oy - 8, "−V", size=12, anchor="start")
    # forward: negligible current until the knee (~0.7 V), then a steep rise (scale 150 px per volt)
    pts = []
    for k in range(0, 121):
        v = k / 120 * 0.85
        pts.append((ox + v * 150, oy - min(3 * math.exp((v - 0.6) / 0.045), 150)))
    pts = [p for p in pts if p[1] > 21]
    f.path(_poly(pts), color=RED, w=2.2)
    f.line(ox + 0.7 * 150, oy, ox + 0.7 * 150, oy + 8)
    f.text(ox + 0.7 * 150, oy + 22, "≈0.7 V (knee)", size=11)
    # reverse: tiny constant microamp current, then breakdown
    xb = 70
    f.path(f"M {ox} {oy} L {ox-8} {oy+14} L {xb} {oy+18} L {xb-6} {oy+130}", color=BLUE, w=2.2)
    f.text(xb + 4, oy + 160, "breakdown voltage", size=11, color=BLUE, anchor="start")
    f.text(150, oy + 40, "reverse saturation current (μA)", size=10, color=BLUE)
    f.text(ox + 50, 50, "forward bias", size=12, color=RED, anchor="start")
    f.text(60, 120, "reverse bias", size=12, color=BLUE, anchor="start")
    return f.svg()


def fig_a20_fwr():
    f = Fig(520, 300, "fig_a20_fwr")
    _coil_v(f, 120, 70, 230, 6, right=True)
    f.line(120, 70, 50, 70); f.line(120, 230, 50, 230)
    f.circle(50, 150, 16, fill="#fff"); f.path("M 40 150 Q 45 140 50 150 T 60 150", w=1.4)
    f.line(50, 70, 50, 134); f.line(50, 166, 50, 230)
    f.text(50, 262, "AC input", size=12)
    f.line(140, 60, 140, 240, w=2); f.line(146, 60, 146, 240, w=2)
    _coil_v(f, 166, 60, 240, 8, right=False)
    f.line(166, 60, 230, 60); f.line(166, 240, 230, 240)
    f.line(166, 150, 230, 150); _dot(f, 166, 150)
    f.text(180, 50, "S₁", size=12); f.text(180, 262, "S₂", size=12); f.text(190, 142, "T", size=12)
    _diode(f, 230, 340, 60); f.text(285, 42, "D₁", size=13)
    _diode(f, 230, 340, 240); f.text(285, 268, "D₂", size=13)
    f.line(340, 60, 400, 60); f.line(340, 240, 400, 240); f.line(400, 60, 400, 240)
    _dot(f, 400, 150); f.text(410, 146, "P", size=13, bold=True, anchor="start")
    f.line(400, 150, 360, 150); _res(f, 360, 150, 250, 150, n=5)
    f.line(250, 150, 230, 150)
    f.text(305, 176, "R", size=14, italic=True, sub="L")
    f.line(360, 150, 360, 185); f.line(250, 150, 250, 185)
    _dot(f, 360, 185); _dot(f, 250, 185)
    f.text(365, 200, "+", size=14); f.text(250, 202, "−", size=16)
    f.text(305, 205, "output", size=12)
    f.arrow(345, 128, 265, 128, color=RED, w=1.4)
    f.text(305, 120, "I (same direction in both halves)", size=10, color=RED)
    f.text(450, 290, "centre-tap full-wave rectifier", size=11, color=GREY)
    return f.svg()


def fig_a20_waves():
    f = Fig(480, 260, "fig_a20_waves")
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
        f.path(_poly(pts), color=col, w=2)
        f.text(ox - 8, oy - 50, label, size=12, anchor="end")
        f.text(462, oy + 16, "t", size=13, italic=True, anchor="end")
    wave(70, False, "input", BLUE)
    wave(200, True, "output", RED)
    for k in range(1, 4):
        x = 60 + k * 99
        f.line(x, 20, x, 215, color=GREY, w=0.6, dash="3 3")
    for k, t in enumerate(["D₁ on", "D₂ on", "D₁ on", "D₂ on"]):
        f.text(60 + 49.5 + 99 * k, 132, t, size=11, color=RED)
    return f.svg()
