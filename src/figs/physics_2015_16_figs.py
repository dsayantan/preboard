"""Figures for Heritage pre-board 2015-16 Physics Paper 1 (theory)."""
import math
from svg import Fig
from physb_draw import (dot, resistor, cell_h, cell_v, meter, key, ray, convex_lens, arrow_obj, axes,
                        polyline, hatch_line, mid_arrow, arc, ang, inductor_v, parallel_pair, diode_h,
                        dipole_torque_pair, bohr_orbit, microscope, BLUE, RED, GREEN, GREY, ORANGE)

# ================================================================== QUESTION figures (theory)
def fig_q1a2_network():
    f = Fig(420, 170, "fig_q1a2_network")
    yt, yb = 40, 130
    xa, xb, xc = 30, 200, 380
    resistor(f, xa, yt, xb, yt); resistor(f, xb, yt, xc, yt)
    resistor(f, xa, yb, xb, yb); resistor(f, xb, yb, xc, yb)
    resistor(f, xb, yt, xb, yb, n=5)
    for x, y, lab, dy in ((xa, yt, "a", -10), (xb, yt, "b", -10), (xc, yt, "c", -10),
                          (xa, yb, "d", 22), (xb, yb, "e", 22), (xc, yb, "f", 22)):
        dot(f, x, y, 3.5)
        f.text(x, y + dy, lab, italic=True)
    f.text(115, yt - 12, "10 Ω", size=13); f.text(290, yt - 12, "20 Ω", size=13)
    f.text(115, yb + 24, "40 Ω", size=13); f.text(290, yb + 24, "80 Ω", size=13)
    f.text(214, 90, "50 Ω", size=13, anchor="start")
    return f.svg()


def _wire_charge(f, with_force):
    xw, yP, a = 90, 120, 160
    f.line(xw, 20, xw, 220, w=2.2)
    f.arrow(xw, 175, xw, 135, w=2.2)
    f.text(xw - 10, 160, "I", italic=True, anchor="end")
    f.line(xw, yP, xw + a, yP, dash="4 4", color=GREY)
    f.circle(xw + a, yP, 5, fill=RED, color=RED)
    f.text(xw + a - 10, yP - 10, "+Q", size=13, anchor="end")
    f.text(xw + a, yP + 22, "P", size=13)
    f.arrow(xw + a + 7, yP, xw + a + 55, yP, color=GREEN, w=2)
    f.text(xw + a + 56, yP + 20, "v", italic=True, bold=True, color=GREEN)
    f.line(xw, yP + 45, xw + a, yP + 45, color=GREY, w=1)
    f.arrow(xw + a / 2, yP + 45, xw + 2, yP + 45, color=GREY, w=1)
    f.arrow(xw + a / 2, yP + 45, xw + a - 2, yP + 45, color=GREY, w=1)
    f.text(xw + a / 2, yP + 40, "a", italic=True)
    if with_force:
        cx, cy = xw + a + 30, yP + 40
        f.circle(cx, cy, 9, color=BLUE)
        f.line(cx - 6, cy - 6, cx + 6, cy + 6, color=BLUE); f.line(cx - 6, cy + 6, cx + 6, cy - 6, color=BLUE)
        f.text(cx + 14, cy + 5, "B (into page)", size=12, color=BLUE, anchor="start")
        f.arrow(xw + a, yP - 8, xw + a, yP - 70, color=RED, w=2.4)
        f.text(xw + a + 8, yP - 52, "F = Q v × B", size=13, color=RED, anchor="start")
        f.text(xw + a + 8, yP - 36, "(parallel to I)", size=12, color=RED, anchor="start")


def fig_q1b7_wire():
    f = Fig(340, 240, "fig_q1b7_wire")
    _wire_charge(f, False)
    return f.svg()


def fig_a1b7_force():
    f = Fig(400, 240, "fig_a1b7_force")
    _wire_charge(f, True)
    return f.svg()


def _bridge(f, uid):
    A, B, C, D = (60, 150), (190, 40), (320, 150), (190, 260)
    # AB : 6 Ω + 6 Ω in series
    m = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
    resistor(f, *A, *m, n=4, amp=5); resistor(f, *m, *B, n=4, amp=5)
    f.text(98, 92, "6Ω", size=13, anchor="end"); f.text(150, 52, "6Ω", size=13, anchor="end")
    # BC : 1 Ω || 1 Ω
    parallel_pair(f, *B, *C, gap=13, amp=4, n=5)
    f.text(272, 80, "1Ω", size=13, anchor="start"); f.text(232, 118, "1Ω", size=13, anchor="end")
    # AD : x Ω + 6 Ω in series
    m2 = ((A[0] + D[0]) / 2, (A[1] + D[1]) / 2)
    resistor(f, *A, *m2, n=4, amp=5); resistor(f, *m2, *D, n=4, amp=5)
    f.text(90, 214, "x Ω", size=13, anchor="end"); f.text(150, 262, "6Ω", size=13, anchor="end")
    # DC : 2 Ω || 2 Ω
    parallel_pair(f, *D, *C, gap=13, amp=4, n=5)
    f.text(232, 186, "2Ω", size=13, anchor="end"); f.text(282, 236, "2Ω", size=13, anchor="start")
    for P, lab, dx, dy in ((A, "A", -12, 5), (B, "B", 0, -10), (C, "C", 13, 5), (D, "D", 0, 22)):
        dot(f, *P, 3.5)
        f.text(P[0] + dx, P[1] + dy, lab, bold=True)
    # battery loop
    f.line(A[0], A[1], 25, A[1]); f.line(25, A[1], 25, 300); f.line(C[0], C[1], 355, C[1]); f.line(355, C[1], 355, 300)
    f.line(25, 300, 186, 300); f.line(194, 300, 355, 300)
    cell_h(f, 190, 300, plus_left=True)


def fig_q4b_bridge():
    f = Fig(380, 325, "fig_q4b_bridge")
    _bridge(f, "fig_q4b_bridge")
    return f.svg()


def fig_q6b_rod():
    f = Fig(400, 200, "fig_q6b_rod")
    for i in range(9):
        for j in range(5):
            x, y = 22 + i * 44, 22 + j * 40
            f.text(x, y + 5, "×", size=14, color=GREY)
    x0, x1, y0, y1 = 70, 290, 45, 155
    f.line(x0, y0, x1 + 12, y0, w=1.8); f.line(x0, y1, x1 + 12, y1, w=1.8)
    resistor(f, x0, y0, x0, y1, n=5, amp=6)
    f.line(x1, y0 - 14, x1, y1 + 14, w=4, color=BLUE)
    f.text(x1, y0 - 18, "P", bold=True); f.text(x1, y1 + 30, "Q", bold=True)
    f.arrow(x1 + 6, 100, x1 + 60, 100, color=RED, w=2.2)
    f.text(x1 + 64, 105, "v", italic=True, bold=True, color=RED, anchor="start")
    f.text(40, 100, "B", italic=True, bold=True, color=BLUE)
    f.text(40, 86, "→", size=11, color=BLUE)
    return f.svg()


def _ek_graph(f, annotate):
    ox, oy, sx, sy = 70, 150, 9.0, 14.0     # 1 unit of 10^14 Hz = 9 px, 1 eV = 14 px
    X = lambda v: ox + v * sx
    Y = lambda e: oy - e * sy
    f.line(X(0), Y(-5), X(0), Y(9.5)); f.arrow(X(0), Y(8.6), X(0), Y(9.6))
    f.arrow(X(0), Y(0), X(36), Y(0))
    for e in (-4, -2, 2, 4, 6, 8):
        f.line(X(0) - 4, Y(e), X(0), Y(e)); f.text(X(0) - 7, Y(e) + 4, str(e), size=11, anchor="end")
    f.text(X(0) - 7, Y(0) + 4, "0", size=11, anchor="end")
    for v in (10, 20, 30):
        f.line(X(v), Y(0), X(v), Y(0) + 4); f.text(X(v) + 2, Y(0) + 16, str(v), size=11)
    f.text(X(36) + 6, Y(0) + 4, "ν (× 10¹⁴ Hz)", size=12, anchor="start")
    f.text(X(0) - 8, Y(9.6), "Eₖ (eV)", size=12, anchor="end")
    f.line(X(0), Y(-4), X(30), Y(8), w=2, color=BLUE)
    f.line(X(0), Y(8), X(30), Y(8), dash="4 3", color=GREY, w=1)
    f.line(X(30), Y(8), X(30), Y(0), dash="4 3", color=GREY, w=1)
    dot(f, X(10), Y(0), 3); f.text(X(10) - 4, Y(0) - 8, "A", size=12)
    dot(f, X(30), Y(8), 3); f.text(X(30) + 6, Y(8) + 2, "B", size=12, anchor="start")
    if annotate:
        f.text(X(11), Y(-2.4), "ν₀ = 10 × 10¹⁴ Hz", size=12, color=RED, anchor="start")
        f.text(X(0) + 8, Y(-4) + 4, "intercept −φ = −4 eV", size=12, color=RED, anchor="start")
        f.text(X(17), Y(5.5), "slope = h (in eV s)", size=12, color=RED, anchor="end")


def fig_q12a_graph():
    f = Fig(500, 250, "fig_q12a_graph")
    _ek_graph(f, False)
    return f.svg()


def fig_a12a_graph():
    f = Fig(500, 250, "fig_a12a_graph")
    _ek_graph(f, True)
    return f.svg()


# ================================================================== ANSWER figures (theory)
def fig_a1b9_xc():
    f = Fig(340, 230, "fig_a1b9_xc")
    ox, oy = 50, 190
    axes(f, ox, oy, 320, 20, "f", "X", ysub="C")
    pts = [(ox + 10 + t, oy - 2400 / (t + 14)) for t in range(4, 255, 4)]
    polyline(f, pts, color=BLUE, w=2.2)
    f.text(230, 150, "X", italic=True, sub="C", size=14, color=BLUE)
    f.text(244, 150, " = 1/(2πfC)", size=13, color=BLUE, anchor="start")
    f.text(ox - 6, oy + 14, "O", size=12)
    return f.svg()


def fig_a2a_dipole():
    return dipole_torque_pair("fig_a2a_dipole")


def fig_a3a_gauss():
    f = Fig(380, 300, "fig_a3a_gauss")
    cx, top, bot, r = 160, 70, 230, 60
    f.line(cx, 15, cx, 285, w=2.5, color=RED)
    for y in range(30, 280, 22):
        f.text(cx + 8, y + 5, "+", size=12, color=RED)
    f.text(cx - 8, 25, "λ", italic=True, color=RED, anchor="end")
    # cylinder
    for y, dash in ((top, None), (bot, None)):
        f.raw(f'<ellipse cx="{cx}" cy="{y}" rx="{r}" ry="14" fill="none" stroke="{BLUE}" stroke-width="1.6"/>')
    f.line(cx - r, top, cx - r, bot, color=BLUE); f.line(cx + r, top, cx + r, bot, color=BLUE)
    # radius
    f.line(cx, 150, cx + r, 150, dash="4 3")
    f.text(cx + r / 2, 144, "r", italic=True)
    # E arrows radially outward on curved surface
    for y in (110, 190):
        f.arrow(cx + r, y, cx + r + 50, y, color=GREEN, w=2)
        f.arrow(cx - r, y, cx - r - 50, y, color=GREEN, w=2)
    f.text(cx + r + 54, 115, "E", italic=True, bold=True, color=GREEN, anchor="start")
    # dA on caps (along axis) perpendicular to E
    f.arrow(cx + 30, top, cx + 30, top - 40, color=ORANGE, w=1.8)
    f.text(cx + 36, top - 28, "dA (cap): E ⊥ dA", size=12, color=ORANGE, anchor="start")
    f.arrow(cx + 30, bot, cx + 30, bot + 40, color=ORANGE, w=1.8)
    # length l
    f.line(cx + r + 75, top, cx + r + 75, bot, color=GREY, w=1)
    f.arrow(cx + r + 75, 150, cx + r + 75, top + 2, color=GREY, w=1)
    f.arrow(cx + r + 75, 150, cx + r + 75, bot - 2, color=GREY, w=1)
    f.text(cx + r + 82, 155, "l", italic=True, anchor="start")
    f.text(cx - r - 10, 270, "Gaussian cylinder", size=12, color=BLUE, anchor="end")
    return f.svg()


def fig_a5b_hysteresis():
    f = Fig(400, 300, "fig_a5b_hysteresis")
    ox, oy = 200, 150
    f.arrow(20, oy, 385, oy); f.arrow(ox, 285, ox, 15)
    f.text(380, oy + 20, "H", italic=True); f.text(ox - 10, 22, "B", italic=True, anchor="end")
    # loop: upper branch from (-Hs,-Bs) up to (Hs,Bs) passing through (-Hc,0) and (0,Br); lower is mirror
    def up(h):  # descending branch (coming back from +sat)
        return 110 * math.tanh((h + 45) / 40)
    hs = [h for h in range(-160, 161, 4)]
    upper = [(ox + h, oy - up(h)) for h in hs]
    lower = [(ox - h, oy + up(h)) for h in hs]
    polyline(f, upper, color=BLUE, w=2.2); polyline(f, lower, color=BLUE, w=2.2)
    mid_arrow(f, ox - 80, oy - up(-80), ox - 84, oy - up(-84), color=BLUE, size=9)
    mid_arrow(f, ox + 80, oy + up(-80), ox + 84, oy + up(-84), color=BLUE, size=9)
    br = up(0)
    dot(f, ox, oy - br, 3.5, RED); f.text(ox - 8, oy - br - 8, "Bᵣ (retentivity)", size=12, color=RED, anchor="end")
    dot(f, ox - 45, oy, 3.5, RED); f.text(ox - 52, oy - 8, "−H꜀ (coercivity)", size=12, color=RED, anchor="end")
    f.text(255, 225, "area of loop = energy lost", size=12, anchor="start")
    f.text(255, 241, "per unit volume per cycle", size=12, anchor="start")
    return f.svg()


def fig_a7a_phasor():
    f = Fig(380, 210, "fig_a7a_phasor")
    ox, oy = 70, 90
    f.arrow(ox, oy, ox + 140, oy, color=RED, w=2.4)
    f.text(ox + 146, oy + 5, "V", italic=True, bold=True, color=RED, anchor="start")
    f.arrow(ox, oy, ox, oy + 90, color=BLUE, w=2.4)
    f.text(ox + 8, oy + 92, "I (lags V by 90°)", size=13, color=BLUE, anchor="start")
    arc(f, ox, oy, 30, 0, 90, color=GREY)
    f.text(ox + 30, oy + 32, "90°", size=12, anchor="start")
    f.text(ox - 4, 25, "rotating anticlockwise at ω", size=12, anchor="start")
    f.text(210, 160, "P = VI cos 90° = 0", size=14, anchor="start")
    return f.svg()


def fig_a9b_slit():
    f = Fig(460, 240, "fig_a9b_slit")
    sx, cy, half = 70, 120, 14
    f.line(sx, 15, sx, cy - half, w=4); f.line(sx, cy + half, sx, 225, w=4)
    f.text(sx - 10, cy - 20, "a", italic=True, anchor="end")
    for y in (40, 60, 80):
        f.arrow(15, cy - 8 + (y - 40) * 0.4, sx - 4, cy - 8 + (y - 40) * 0.4, color=GREY, w=1)
    scr = 330
    f.line(scr, 15, scr, 225, w=2)
    f.line(sx, cy, scr, cy, dash="4 3", color=GREY, w=1)
    th = math.radians(30)
    for s in (1, -1):
        y = cy - s * (scr - sx) * math.tan(th) * 0.55
        f.line(sx, cy, scr, y, color=RED, w=1.4)
    arc(f, sx, cy, 60, -16.0, 0, color=RED)
    arc(f, sx, cy, 66, 0, 16.0, color=RED)
    f.text(sx + 72, cy - 10, "θ", italic=True, color=RED, anchor="start")
    f.text(sx + 78, cy + 26, "θ", italic=True, color=RED, anchor="start")
    # intensity curve on the screen (sinc^2), drawn to the right of the screen
    pts = []
    ys = (scr - sx) * math.tan(th) * 0.55
    for k in range(-100, 101):
        b = k / 100 * 2.6 * math.pi
        I = 1.0 if b == 0 else (math.sin(b) / b) ** 2
        pts.append((scr + 6 + 100 * I, cy + k / 100 * 2.6 * ys))
    polyline(f, pts, color=BLUE, w=1.8)
    f.text(scr + 70, 30, "intensity", size=12, color=BLUE)
    f.text(scr - 6, cy - ys - 4, "1st min", size=11, anchor="end")
    f.text(scr - 6, cy + ys + 12, "1st min", size=11, anchor="end")
    f.text(200, 236, "angular width of central maximum = 2θ, a sin θ = λ", size=12)
    return f.svg()


def fig_a10a_refraction():
    f = Fig(540, 310, "fig_a10a_refraction")
    cy = 200
    O, C, I = (40, cy), (360, cy), (510, cy)
    R = 110
    h = 75
    N = (C[0] - math.sqrt(R * R - h * h), cy - h)
    P = (C[0] - R, cy)
    f.line(15, cy, 505, cy, color=GREY, w=1)
    # surface arc
    f.path(f"M {C[0]-R*math.cos(math.radians(50)):.1f} {cy-R*math.sin(math.radians(50)):.1f} "
           f"A {R} {R} 0 0 0 {C[0]-R*math.cos(math.radians(50)):.1f} {cy+R*math.sin(math.radians(50)):.1f}",
           color=BLUE, w=2.2)
    f.text(120, 60, "μ₁ (rarer)", size=13); f.text(450, 60, "μ₂ (denser)", size=13)
    # normal through C and N, extended outward
    ux, uy = (N[0] - C[0]) / R, (N[1] - C[1]) / R
    f.line(C[0], C[1], N[0] + ux * 60, N[1] + uy * 60, dash="5 4", color=GREEN, w=1.3)
    # rays
    ray(f, [O, N], color=RED)
    ray(f, [N, I], color=RED)
    d = ((N[0] - O[0]), (N[1] - O[1])); L = math.hypot(*d)
    f.line(N[0], N[1], N[0] + d[0] / L * 90, N[1] + d[1] / L * 90, dash="3 3", color=RED, w=1)
    # perpendicular NM
    f.line(N[0], N[1], N[0], cy, dash="2 3", color=GREY, w=1)
    for pt, lab, dx in ((O, "O", 0), (P, "P", -8), (C, "C", 0), (I, "I", 0), ((N[0], cy), "M", 9)):
        dot(f, *pt, 3)
        f.text(pt[0] + dx, cy + 18, lab, size=13)
    f.text(N[0] - 4, N[1] - 8, "N", size=13, anchor="end")
    # angles
    arc(f, *O, 48, ang(*O, *N), 0, color="#333")
    f.text(O[0] + 54, cy - 4, "α", italic=True, anchor="start")
    arc(f, *I, 44, 180, ang(*I, *N), color="#333")
    f.text(I[0] - 50, cy - 4, "β", italic=True, anchor="end")
    arc(f, *C, 26, 180, ang(*C, *N), color="#333")
    f.text(C[0] - 30, cy - 8, "γ", italic=True, anchor="end")
    a_in = ang(*N, N[0] + d[0], N[1] + d[1]); a_nc = ang(*N, *C); a_r = ang(*N, *I)
    arc(f, *N, 46, a_in, a_nc, color=RED)
    f.text(N[0] + 52, N[1] + 2, "i", italic=True, color=RED, anchor="start")
    arc(f, *N, 30, a_r, a_nc, color=GREEN)
    f.text(N[0] + 21, N[1] + 34, "r", italic=True, color=GREEN, anchor="start")
    f.text(270, 300, "u = −PO,  v = +PI,  R = +PC   (angles opened out for clarity)", size=12)
    return f.svg()


def fig_a10b_lensmirror():
    s = 6.0                       # px per cm
    f = Fig(500, 200, "fig_a10b_lensmirror")
    cy = 95
    xo = 20
    X = lambda d: xo + d * s      # d measured in cm from the object
    xl, xm, xi = X(12), X(22), X(72)
    f.line(10, cy, 490, cy, color=GREY, w=1)
    convex_lens(f, xl, cy, 60, t=10)
    f.text(xl, cy - 66, "L (f = 10 cm)", size=12, color=BLUE)
    # convex mirror: arc of radius 50 cm centred at I (= its centre of curvature)
    Rm = 50 * s
    hm = 60
    ang_m = math.degrees(math.asin(hm / Rm))
    x_top = xi - Rm * math.cos(math.radians(ang_m))
    f.path(f"M {x_top:.1f} {cy-hm} A {Rm} {Rm} 0 0 0 {x_top:.1f} {cy+hm}", color="#111", w=2.4)
    for k in range(-5, 6):
        yy = cy + k * 11
        xx = xi - math.sqrt(Rm * Rm - (yy - cy) ** 2)
        f.line(xx, yy, xx + 7, yy + 5, color="#555", w=1)
    f.text(xm + 40, cy - hm + 4, "convex mirror", size=12, anchor="start")
    dot(f, xo, cy, 3.5)
    f.text(xo, cy + 18, "O", size=13)
    dot(f, xi, cy, 3.5)
    f.text(xi, cy + 18, "I = C", size=13)
    for hl in (40, -40):
        y_l = cy - hl
        y_m = cy - hl * (1 - 10 / 60)
        xm_hit = xi - math.sqrt(Rm * Rm - (y_m - cy) ** 2)
        y_m = cy - hl * (1 - (xm_hit - xl) / (xi - xl))
        ray(f, [(xo, cy), (xl, y_l), (xm_hit, y_m)], color=RED)
        f.line(xm_hit, y_m, xi, cy, dash="4 4", color=RED, w=1)
    # dimension lines
    yd = 185
    for a_, b_, lab in ((xo, xl, "12 cm"), (xl, xm, "10 cm"), (xm, xi, "R = 50 cm")):
        f.line(a_, yd - 5, a_, yd + 5, color=GREY, w=1); f.line(b_, yd - 5, b_, yd + 5, color=GREY, w=1)
        f.line(a_, yd, b_, yd, color=GREY, w=1)
        f.text((a_ + b_) / 2, yd - 5, lab, size=11)
    return f.svg()


def fig_a11b_micro():
    svg, _ = microscope("fig_a11b_micro")
    return svg


def fig_a13a_bohr():
    return bohr_orbit("fig_a13a_bohr")


def fig_a15a_fwr():
    f = Fig(640, 280, "fig_a15a_fwr")
    yt, ym, yb = 50, 140, 230
    # primary
    f.line(32, 90, 60, 90); f.line(32, 190, 60, 190)
    dot(f, 32, 90, 3); dot(f, 32, 190, 3)
    f.text(28, 145, "a.c.", size=12, anchor="end"); f.text(28, 160, "in", size=12, anchor="end")
    inductor_v(f, 60, 90, 190, n=5, right=True)
    f.line(84, 70, 84, 210, w=1.4); f.line(90, 70, 90, 210, w=1.4)
    inductor_v(f, 114, yt, yb, n=8, right=False)
    f.text(116, yt - 8, "S₁", size=12); f.text(116, yb + 18, "S₂", size=12)
    # centre tap
    dot(f, 114, ym, 3)
    f.text(104, ym - 6, "T", size=12, anchor="end")
    # diodes to common cathode node at x=330
    f.line(114, yt, 210, yt); diode_h(f, 220, yt, size=14); f.line(227, yt, 330, yt)
    f.text(220, yt - 14, "D₁", size=12)
    f.line(114, yb, 210, yb); diode_h(f, 220, yb, size=14); f.line(227, yb, 330, yb)
    f.text(220, yb + 22, "D₂", size=12)
    f.line(330, yt, 330, yb)
    dot(f, 330, ym, 3)
    # load from cathode node to centre tap
    resistor(f, 330, ym, 114, ym, n=6, amp=7)
    f.text(222, ym - 14, "R", italic=True, sub="L", size=14)
    f.text(322, ym - 6, "+", size=14, bold=True, anchor="end"); f.text(130, ym - 6, "−", size=14, bold=True, anchor="start")
    f.arrow(250, ym + 18, 190, ym + 18, color=RED, w=1.4)
    f.text(220, ym + 34, "same direction both halves", size=11, color=RED)
    # waveforms
    x0, x1 = 380, 625
    for y0, lab in ((80, "input"), (215, "output")):
        f.arrow(x0, y0, x1, y0, w=1); f.arrow(x0, y0 + 50, x0, y0 - 55, w=1)
        f.text(x1, y0 + 16, "t", italic=True, anchor="end")
        f.text(x0 + 4, y0 - 46, lab, size=12, anchor="start")
    inp = [(x0 + t, 80 - 38 * math.sin(t / 220 * 4 * math.pi)) for t in range(0, 221, 2)]
    out = [(x0 + t, 215 - 38 * abs(math.sin(t / 220 * 4 * math.pi))) for t in range(0, 221, 2)]
    polyline(f, inp, color=BLUE, w=1.8); polyline(f, out, color=RED, w=1.8)
    for k_, lab_ in enumerate(("D₁", "D₂", "D₁", "D₂")):
        f.text(x0 + 27 + 55 * k_, 232, lab_, size=11, color=RED)
    return f.svg()


# ================================================================== PRACTICAL paper (Paper 2) — sample data and figures
P1_F_TRUE, P1_F_APPROX = 15.0, 15.1                  # lens used to generate readings; f from a distant object
P1_U = [70.0, 60.0, 50.0, 40.0, 30.0, 20.0]
P1_V = [19.2, 19.9, 21.5, 23.9, 30.2, 59.6]          # sample readings, cm, least count 0.1 cm
P1_X = [round(u - P1_F_APPROX, 1) for u in P1_U]
P1_Y = [round(100 / (v - P1_F_APPROX), 1) for v in P1_V]


def _fit(xs, ys):
    n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
    m = sum((a - mx) * (b - my) for a, b in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)
    return m, my - m * mx


P1_M, P1_C = _fit(P1_X, P1_Y)
P1_XA, P1_XB = 10.0, 50.0                            # slope-triangle points read off the best-fit line
P2_R = [1, 2, 3, 4, 5]
P2_V = [2.40, 2.05, 1.75, 1.55, 1.35]                # voltmeter least count 0.05 V
P2_I = [0.78, 0.66, 0.56, 0.50, 0.44]                # ammeter least count 0.02 A
P2_D = [0.041, 0.040, 0.039, 0.040]                  # micrometer readings of diameter, cm (LC 0.001 cm)


def fig_p1_bench():
    f = Fig(560, 190, "fig_p1_bench")
    yb, ya = 140, 60
    f.line(20, yb, 470, yb, w=2.2)
    xo, xl, xi = 40, 290, 400
    for x in (xo, xl, xi):
        f.rect(x - 6, ya + 12, 12, yb - ya - 12, fill="#ccc", w=1)
    f.line(xo - 10, ya, 505, ya, dash="6 4", color=GREY, w=1)
    arrow_obj(f, xo, ya + 14, 14)
    f.text(xo, ya - 16, "O", bold=True)
    convex_lens(f, xl, ya, 26, t=10)
    f.text(xl, ya - 32, "L", bold=True)
    arrow_obj(f, xi, ya + 14, 14)
    f.text(xi + 12, ya + 12, "I", italic=True, anchor="start")
    f.line(xi, ya - 2, xi, ya - 30, dash="2 2", color=RED)
    f.arrow(xi, ya - 30, xi, ya - 3, color=RED, w=1.2)
    f.text(xi, ya - 34, "I′ (image)", size=12, color=RED)
    f.text(540, ya - 14, "observer's eye", size=12, anchor="end")
    f.raw(f'<path d="M 522 {ya-8} Q 536 {ya} 522 {ya+8} Q 513 {ya} 522 {ya-8} Z" fill="#555"/>')
    f.text(xo, yb + 18, "0 cm", size=12); f.text(xl, yb + 18, "70.0 cm", size=12)
    yd = yb + 36
    for a_, b_, lab in ((xo, xl, "u"), (xl, xi, "v")):
        f.line(a_, yd, b_, yd, color=GREY, w=1)
        f.arrow((a_ + b_) / 2, yd, a_ + 2, yd, color=GREY, w=1); f.arrow((a_ + b_) / 2, yd, b_ - 2, yd, color=GREY, w=1)
        f.text((a_ + b_) / 2, yd - 4, lab, italic=True)
    return f.svg()


def fig_p1_graph():
    f = Fig(540, 395, "fig_p1_graph")
    ox, oy, sx, sy = 60, 350, 7.6, 12.0
    X = lambda x: ox + x * sx
    Y = lambda y: oy - y * sy
    for gx in range(0, 61, 5):
        f.line(X(gx), Y(0), X(gx), Y(27), color="#e3e3e3", w=0.8)
    for gy in range(0, 28, 1):
        f.line(X(0), Y(gy), X(60), Y(gy), color="#eeeeee" if gy % 5 else "#dcdcdc", w=0.8)
    f.arrow(X(0), Y(0), X(62), Y(0)); f.arrow(X(0), Y(0), X(0), Y(28.5))
    for gx in range(0, 61, 10):
        f.text(X(gx), Y(0) + 16, str(gx), size=11)
    for gy in range(0, 28, 5):
        f.text(X(0) - 6, Y(gy) + 4, str(gy), size=11, anchor="end")
    f.text(X(60), Y(0) + 36, "x = u − f  (cm)", size=13, anchor="end")
    f.text(X(0) + 6, Y(28.2), "y = 100/(v − f)  (cm⁻¹)", size=13, anchor="start")
    m, c = P1_M, P1_C
    f.line(X(0), Y(c), X(58), Y(c + m * 58), color=BLUE, w=1.8)
    for x, y in zip(P1_X, P1_Y):
        f.circle(X(x), Y(y), 4.5, color=RED, w=1.4)
        dot(f, X(x), Y(y), 1.4, RED)
    xa, xb = P1_XA, P1_XB
    ya, yb = c + m * xa, c + m * xb
    f.line(X(xa), Y(ya), X(xb), Y(ya), color=GREEN, dash="5 3", w=1.3)
    f.line(X(xb), Y(ya), X(xb), Y(yb), color=GREEN, dash="5 3", w=1.3)
    dot(f, X(xa), Y(ya), 3, GREEN); dot(f, X(xb), Y(yb), 3, GREEN)
    f.text(X(xa) - 4, Y(ya) - 8, f"P({xa:.1f}, {ya:.2f})", size=11, color=GREEN, anchor="end")
    f.text(X(xb) - 6, Y(yb) - 8, f"Q({xb:.1f}, {yb:.2f})", size=11, color=GREEN, anchor="end")
    f.text((X(xa) + X(xb)) / 2, Y(ya) + 16, f"Δx = {xb-xa:.1f}", size=12, color=GREEN)
    f.text(X(xb) + 6, (Y(ya) + Y(yb)) / 2, f"Δy = {yb-ya:.2f}", size=12, color=GREEN, anchor="start")
    f.text(X(4), Y(21), f"m = Δy/Δx = {(yb-ya)/(xb-xa):.3f} cm⁻²", size=13, color=BLUE, anchor="start")
    f.text(X(30), Y(26.5), "Graph of y against x (sample readings)", size=13, bold=True)
    return f.svg()


def fig_p2_circuit():
    f = Fig(560, 230, "fig_p2_circuit")
    yt, yw, yv = 40, 130, 195
    xA, xB = 40, 470
    f.line(xA, yw, xA, yt); f.line(xA, yt, 176, yt)
    cell_h(f, 180, yt, plus_left=True)
    f.text(180, yt - 18, "E (4 V)", size=12)
    f.line(184, yt, 222, yt); key(f, 230, yt); f.line(238, yt, 270, yt)
    f.rect(270, yt - 12, 70, 24, fill="#fff"); f.text(305, yt + 5, "R.B.", size=13, bold=True)
    f.line(340, yt, 380, yt); meter(f, 393, yt, "A"); f.line(406, yt, xB, yt)
    f.text(414, yt - 6, "+", size=12, anchor="start")
    f.line(xB, yt, xB, yw)
    f.line(xA, yw, xB, yw, w=3, color="#444")
    dot(f, xA, yw, 4); dot(f, xB, yw, 4)
    f.text(xA - 10, yw + 5, "A", bold=True, anchor="end"); f.text(xB + 10, yw + 5, "B", bold=True, anchor="start")
    xC = xA + (xB - xA) * 0.8
    f.line(xA, yw, xA, yv); f.line(xA, yv, 240, yv); meter(f, 253, yv, "V"); f.line(266, yv, xC, yv)
    f.line(xC, yv, xC, yw + 8)
    f.raw(f'<path d="M {xC-6} {yw+16} L {xC} {yw+4} L {xC+6} {yw+16} Z" fill="#111"/>')
    f.text(xC + 10, yw + 26, "J (at C)", size=12, anchor="start")
    f.text(232, yv - 8, "+", size=12, anchor="end")
    f.line(xA, yw - 12, xC, yw - 12, color=GREY, w=1)
    f.arrow((xA + xC) / 2, yw - 12, xA + 2, yw - 12, color=GREY, w=1)
    f.arrow((xA + xC) / 2, yw - 12, xC - 2, yw - 12, color=GREY, w=1)
    f.text((xA + xC) / 2, yw - 16, "AC = 80.0 cm", size=12)
    return f.svg()
