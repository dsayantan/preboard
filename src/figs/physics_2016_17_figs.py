"""Figures for Heritage pre-board 2016-17 Physics Paper 1."""
import math
from svg import Fig
from physb_draw import (dot, resistor, cell_h, cell_v, meter, key, ray, convex_lens, arrow_obj, axes,
                        polyline, mid_arrow, arc, ang, capacitor_h, inductor_h, ac_source, diode_h, diode_v,
                        dipole_torque_pair, bohr_orbit, microscope, BLUE, RED, GREEN, GREY, ORANGE)


# ================================================================== QUESTION figures
def _three_branch(f, annotate):
    yt, yb = 30, 230
    xs = (60, 180, 300)
    f.line(xs[0], yt, xs[2], yt); f.line(xs[0], yb, xs[2], yb)
    dot(f, xs[1], yt, 3); dot(f, xs[1], yb, 3)
    # left: cell (+ on top) then 2 ohm
    f.line(xs[0], yt, xs[0], 76); cell_v(f, xs[0], 80, plus_top=True); f.line(xs[0], 84, xs[0], 120)
    resistor(f, xs[0], 120, xs[0], 200, n=5); f.line(xs[0], 200, xs[0], yb)
    f.text(xs[0] - 18, 85, "16 V", size=13, anchor="end"); f.text(xs[0] - 14, 165, "2 Ω", size=13, anchor="end")
    # middle: cell (+ at bottom) then 4 ohm
    f.line(xs[1], yt, xs[1], 76); cell_v(f, xs[1], 80, plus_top=False); f.line(xs[1], 84, xs[1], 120)
    resistor(f, xs[1], 120, xs[1], 200, n=5); f.line(xs[1], 200, xs[1], yb)
    f.text(xs[1] - 18, 85, "16 V", size=13, anchor="end"); f.text(xs[1] + 14, 165, "4 Ω", size=13, anchor="start")
    # right: cell (+ on top) only
    f.line(xs[2], yt, xs[2], 76); cell_v(f, xs[2], 80, plus_top=True); f.line(xs[2], 84, xs[2], yb)
    f.text(xs[2] + 16, 85, "20 V", size=13, anchor="start")
    if annotate:
        f.text(xs[1] + 6, yt - 8, "T", size=12, anchor="start"); f.text(xs[1] + 6, yb + 16, "M", size=12, anchor="start")
        f.arrow(xs[0] + 14, 135, xs[0] + 14, 185, color=RED, w=1.8); f.text(xs[0] + 20, 150, "2 A", size=12, color=RED, anchor="start")
        f.arrow(xs[1] - 14, 135, xs[1] - 14, 185, color=RED, w=1.8); f.text(xs[1] - 20, 150, "9 A", size=12, color=RED, anchor="end")
        f.arrow(xs[2] + 14, 185, xs[2] + 14, 135, color=RED, w=1.8); f.text(xs[2] + 20, 165, "11 A", size=12, color=RED, anchor="start")


def fig_q1b3_cells():
    f = Fig(360, 245, "fig_q1b3_cells")
    _three_branch(f, False)
    return f.svg()


def fig_a1b3_cells():
    f = Fig(380, 250, "fig_a1b3_cells")
    _three_branch(f, True)
    return f.svg()


def _loop_field(f, annotate):
    for i in range(7):
        for j in range(6):
            dot(f, 20 + i * 48, 20 + j * 40, 3, "#333")
    x0, y0, s = 92, 62, 130
    f.rect(x0, y0, s, s, w=2.2, color=BLUE)
    for (x, y, lab, dx, dy) in ((x0, y0, "A", -10, -6), (x0 + s, y0, "B", 10, -6),
                                (x0 + s, y0 + s, "C", 10, 18), (x0, y0 + s, "D", -10, 18)):
        f.text(x + dx, y + dy, lab, italic=True, bold=True, size=15)
    f.arrow(x0 + s + 18, y0 + s / 2, x0 + s + 75, y0 + s / 2, color=RED, w=2.4)
    f.text(x0 + s + 78, y0 + s / 2 + 5, "v", italic=True, bold=True, color=RED, anchor="start")
    if annotate:
        for x in (x0, x0 + s):
            f.arrow(x + (12 if x == x0 else -12), y0 + 35, x + (12 if x == x0 else -12), y0 + s - 35, color=GREEN, w=2)
        f.text(170, 252, "B out of page; q(v × B) on + charges points A→D and B→C (green)", size=11, color=GREEN)


def fig_q1b6_loop():
    f = Fig(340, 240, "fig_q1b6_loop")
    _loop_field(f, False)
    return f.svg()


def fig_a1b6_loop():
    f = Fig(360, 262, "fig_a1b6_loop")
    _loop_field(f, True)
    return f.svg()


def fig_q1b8_airlens():
    f = Fig(340, 220, "fig_q1b8_airlens")
    f.rect(20, 20, 300, 180, fill="#d9dde3", w=1.6)
    cx, cy, h, t = 170, 110, 88, 24
    f.path(f"M {cx} {cy-h} Q {cx+t*2} {cy} {cx} {cy+h} Q {cx-t*2} {cy} {cx} {cy-h} Z", fill="#ffffff", w=1.8)
    f.text(cx, cy + 5, "Air", size=15, bold=True)
    f.text(255, cy + 5, "Glass", size=15, bold=True)
    f.text(70, cy + 5, "Glass", size=15, bold=True)
    return f.svg()


def fig_q1b14_diode():
    f = Fig(420, 90, "fig_q1b14_diode")
    y = 55
    dot(f, 30, y, 4); dot(f, 390, y, 4)
    f.text(30, y - 16, "+4 V", size=14, bold=True)
    f.text(390, y - 16, "+1 V", size=14, bold=True)
    f.line(30, y, 160, y); diode_h(f, 170, y, size=16); f.line(178, y, 240, y)
    f.text(170, y - 16, "p-n", size=13, italic=True)
    resistor(f, 240, y, 340, y, n=5, amp=6, lead=8); f.line(340, y, 390, y)
    f.text(290, y - 16, "300 Ω", size=13)
    return f.svg()


def fig_q4a_junction():
    f = Fig(320, 260, "fig_q4a_junction")
    TL, TR, BR, BL = (90, 80), (230, 80), (230, 190), (90, 190)
    f.line(*TL, *TR, w=2); f.line(*TR, *BR, w=2); f.line(*BR, *BL, w=2); f.line(*BL, *TL, w=2)
    mid_arrow(f, *TL, *TR, size=9); mid_arrow(f, *TR, *BR, size=9); mid_arrow(f, *BR, *BL, size=9); mid_arrow(f, *BL, *TL, size=9)
    f.line(30, 20, *TL, w=2); mid_arrow(f, 30, 20, *TL, size=9); f.text(70, 34, "15 A", size=14, bold=True, anchor="start")
    f.line(290, 20, *TR, w=2); mid_arrow(f, 290, 20, *TR, size=9); f.text(250, 34, "3 A", size=14, bold=True, anchor="end")
    f.line(30, 250, *BL, w=2); mid_arrow(f, 30, 250, *BL, size=9); f.text(70, 246, "5 A", size=14, bold=True, anchor="start")
    f.line(*BR, 290, 250, w=2); mid_arrow(f, *BR, 290, 250, size=9); f.text(272, 228, "i", size=15, italic=True, bold=True, anchor="start")
    f.text(80, 140, "8 A", size=14, bold=True, anchor="end")
    return f.svg()


def _bent_wire(f, annotate):
    ox, oy, r = 150, 140, 70
    f.line(ox, 10, ox, oy - r, w=2.2)
    f.arrow(ox, 20, ox, 50, w=2.2)
    f.text(ox + 10, 40, "I", italic=True, anchor="start")
    # semicircle on the left from top (ox, oy-r) to bottom (ox, oy+r), anticlockwise on page
    f.path(f"M {ox} {oy-r} A {r} {r} 0 0 0 {ox} {oy+r}", w=2.2)
    mid_arrow(f, ox - r, oy - 4, ox - r, oy + 4, size=10)
    f.line(ox, oy + r, 330, oy + r, w=2.2)
    mid_arrow(f, ox + 40, oy + r, ox + 80, oy + r, size=10)
    mid_arrow(f, 290, oy + r, 330, oy + r, size=10)
    f.line(ox, oy - r, ox, oy - 8, dash="3 3", color=GREY)
    dot(f, ox, oy, 6)
    f.text(ox + 14, oy + 6, "O", size=15, anchor="start")
    f.line(ox, oy + 8, ox, oy + r - 2, dash="3 3", color=GREY)
    f.text(ox + 8, oy + r / 2 + 6, "r", italic=True, anchor="start")
    if annotate:
        f.text(ox - r - 8, oy - 40, "semicircle:", size=11, color=BLUE, anchor="end")
        f.text(ox - r - 8, oy - 26, "μ₀I/4r, out", size=11, color=BLUE, anchor="end")
        f.text(250, oy + r - 10, "straight wire: μ₀I/4πr, out", size=11, color=BLUE)
        f.text(ox + 24, 40, "line passes through O: B = 0", size=11, color=BLUE, anchor="start")
        f.circle(ox + 40, oy - 20, 8, color=RED); dot(f, ox + 40, oy - 20, 2.5, RED)
        f.text(ox + 52, oy - 16, "B at O (out of page)", size=11, color=RED, anchor="start")


def fig_q5a_wire():
    f = Fig(340, 230, "fig_q5a_wire")
    _bent_wire(f, False)
    return f.svg()


def fig_a5a_wire():
    f = Fig(360, 230, "fig_a5a_wire")
    _bent_wire(f, True)
    return f.svg()


def fig_q7b_lcr():
    f = Fig(420, 160, "fig_q7b_lcr")
    yt, yb = 50, 125
    f.line(30, yt, 76, yt); capacitor_h(f, 80, yt); f.line(84, yt, 160, yt)
    f.text(80, yt - 18, "4 μF", size=13)
    inductor_h(f, 160, 240, yt, n=6); f.line(240, yt, 290, yt)
    f.text(200, yt - 16, "2 H", size=13)
    resistor(f, 290, yt, 380, yt, n=5, lead=8); f.line(380, yt, 395, yt)
    f.text(335, yt - 16, "500 Ω", size=13)
    f.line(30, yt, 30, yb); f.line(395, yt, 395, yb)
    f.line(30, yb, 200, yb); ac_source(f, 212, yb); f.line(224, yb, 395, yb)
    f.text(212, yb + 28, "ε = 300 sin (500 t)", size=13)
    return f.svg()


def fig_q15a_logic():
    f = Fig(440, 150, "fig_q15a_logic")
    yA, yB = 40, 70
    f.circle(28, yA, 4); f.circle(28, yB, 4)
    f.text(14, yA + 5, "A", bold=True, anchor="end"); f.text(14, yB + 5, "B", bold=True, anchor="end")
    # NOR gate P
    gx = 120
    f.line(32, yA, gx + 8, yA); f.line(32, yB, gx + 8, yB)
    f.path(f"M {gx} 25 Q {gx+20} 55 {gx} 85 Q {gx+55} 85 {gx+85} 55 Q {gx+55} 25 {gx} 25 Z", fill="#d8d8d8", w=1.8)
    f.text(gx + 32, 60, "P", size=14, bold=True)
    f.circle(gx + 90, 55, 5, fill="#fff")
    # AND gate Q
    qx = 280
    f.line(gx + 95, 55, qx, 55)
    f.line(qx, 85, qx - 30, 85); f.line(qx - 30, 85, qx - 30, 120); f.line(qx - 30, 120, 80, 120); f.line(80, 120, 80, yB)
    dot(f, 80, yB, 3)
    f.path(f"M {qx} 40 L {qx+30} 40 A 30 30 0 0 1 {qx+30} 100 L {qx} 100 Z", fill="#d8d8d8", w=1.8)
    f.text(qx + 25, 76, "Q", size=14, bold=True)
    f.line(qx + 60, 70, 400, 70); f.circle(404, 70, 4)
    f.text(414, 75, "X", bold=True, anchor="start")
    f.line(qx, 55, qx, 55)
    return f.svg()


# ================================================================== ANSWER figures
def fig_a1a1_square():
    f = Fig(300, 230, "fig_a1a1_square")
    a = 120
    p1, p2, p3, p4 = (70, 180), (70 + a, 180), (70 + a, 180 - a), (70, 180 - a)
    f.rect(70, 60, a, a, color=GREY, w=1)
    f.line(*p1, *p3, dash="5 4", color=RED)
    for p, lab, dx, dy in ((p1, "q₁", -12, 18), (p2, "q₂", 12, 18), (p3, "q₃", 12, -8)):
        f.circle(*p, 8, fill="#fbe3e0", color=RED)
        f.text(p[0] + dx, p[1] + dy, lab, size=14)
    f.text(70 + a / 2, 198, "a", italic=True)
    f.text(70 + a / 2 - 12, 120, "√2 a", size=13, color=RED, anchor="end")
    f.text(70 + a + 12, 125, "a", italic=True, anchor="start")
    f.text(150, 222, "q₂ adjacent to q₁, q₃ diagonally opposite", size=12)
    return f.svg()


def fig_a2a_pendulum():
    f = Fig(320, 260, "fig_a2a_pendulum")
    sx, sy = 120, 20
    L = 160
    th = math.atan(4.0 / 7.84)
    bx, by = sx + L * math.sin(th), sy + L * math.cos(th)
    f.line(40, sy, 220, sy, w=3)
    f.line(sx, sy, bx, by, w=1.6)
    f.line(sx, sy, sx, sy + L + 10, dash="4 3", color=GREY)
    arc(f, sx, sy, 40, 90, 90 - math.degrees(th), color=GREY)
    f.text(sx + 8, sy + 56, "θ", italic=True, anchor="start")
    f.circle(bx, by, 9, fill="#fbe3e0", color=RED)
    f.arrow(bx, by + 9, bx, by + 75, color=BLUE, w=2.2)
    f.text(bx + 8, by + 60, "mg", size=13, color=BLUE, anchor="start")
    f.arrow(bx + 9, by, bx + 48, by, color=GREEN, w=2.2)
    f.text(bx + 52, by + 5, "qE", size=13, color=GREEN, anchor="start")
    ux, uy = (sx - bx) / L, (sy - by) / L
    f.arrow(bx + ux * 10, by + uy * 10, bx + ux * 80, by + uy * 80, color=RED, w=2.2)
    f.text(bx + ux * 60 + 10, by + uy * 60, "T", italic=True, color=RED, anchor="start")
    f.text(260, 40, "E →", size=14, color=GREEN)
    return f.svg()


def fig_a2b_dipole():
    return dipole_torque_pair("fig_a2b_dipole")


def fig_a3b_qv():
    f = Fig(320, 230, "fig_a3b_qv")
    ox, oy = 50, 195
    f.raw(f'<path d="M {ox} {oy} L 260 {oy} L 260 45 Z" fill="#dde8f8" stroke="none"/>')
    axes(f, ox, oy, 300, 20, "q", "")
    f.text(ox + 8, 26, "p.d. v", italic=True, anchor="start")
    f.line(ox, oy, 260, 45, color=BLUE, w=2.2)
    f.line(260, 45, 260, oy, dash="4 3", color=GREY)
    f.line(ox, 45, 260, 45, dash="4 3", color=GREY)
    f.text(260, oy + 18, "Q", italic=True); f.text(ox - 6, 50, "V", italic=True, anchor="end")
    f.text(226, 180, "W = ½QV", size=13, color=BLUE)
    f.text(140, 95, "slope = 1/C", size=12, anchor="end")
    for xx in (170, 180):
        f.line(xx, oy, xx, oy - (xx - ox) * 150 / 210, color=RED, w=1)
    f.text(175, oy - 120, "dW = (q/C)dq", size=11, color=RED)
    return f.svg()


def fig_a4b_metrebridge():
    f = Fig(520, 280, "fig_a4b_metrebridge")
    yw, yg = 170, 70
    xA, xC = 50, 470
    f.line(xA, yw, xC, yw, w=3, color="#444")
    f.rect(xA - 10, yw + 4, xC - xA + 20, 14, fill="#f1e7c8", w=1)
    for k in range(0, 101, 10):
        x = xA + (xC - xA) * k / 100
        f.line(x, yw + 4, x, yw + 10, w=1)
    f.text(xA, yw + 34, "0 cm", size=11); f.text(xC, yw + 34, "100 cm", size=11)
    f.text(xA - 14, yw - 8, "A", bold=True, anchor="end"); f.text(xC + 14, yw - 8, "C", bold=True, anchor="start")
    # thick strips with gaps
    f.line(xA, yw, xA, yg, w=4); f.line(xC, yw, xC, yg, w=4)
    f.line(xA, yg, 120, yg, w=4); resistor(f, 120, yg, 200, yg, n=5, lead=6); f.line(200, yg, 320, yg, w=4)
    resistor(f, 320, yg, 400, yg, n=5, lead=6); f.line(400, yg, xC, yg, w=4)
    f.text(160, yg - 14, "X", italic=True, size=15); f.text(360, yg - 14, "R (R.B.)", size=13)
    xB = 260
    f.text(xB, yg - 10, "B", bold=True)
    xJ = xA + (xC - xA) * 0.45
    f.line(xB, yg, xB, 105); meter(f, xB, 118, "G"); f.line(xB, 131, xB, 140); f.line(xB, 140, xJ, 155)
    f.raw(f'<path d="M {xJ-5} {yw-14} L {xJ} {yw-2} L {xJ+5} {yw-14} Z" fill="#111"/>')
    f.text(xJ - 10, yw - 10, "J", bold=True, anchor="end")
    f.text(xJ, yw + 50, "D (null point)", size=12)
    # l marker
    f.line(xA, yw + 60, xJ, yw + 60, color=GREY, w=1)
    f.arrow((xA + xJ) / 2, yw + 60, xA + 2, yw + 60, color=GREY, w=1)
    f.arrow((xA + xJ) / 2, yw + 60, xJ - 2, yw + 60, color=GREY, w=1)
    f.text((xA + xJ) / 2, yw + 56, "l", italic=True)
    f.line(xJ, yw + 60, xC, yw + 60, color=GREY, w=1)
    f.arrow((xJ + xC) / 2, yw + 60, xJ + 2, yw + 60, color=GREY, w=1)
    f.arrow((xJ + xC) / 2, yw + 60, xC - 2, yw + 60, color=GREY, w=1)
    f.text((xJ + xC) / 2, yw + 56, "100 − l", italic=True)
    # cell and key
    yc = 260
    f.line(xA, yw, xA - 30, yw); f.line(xA - 30, yw, xA - 30, yc); f.line(xC, yw, xC + 30, yw); f.line(xC + 30, yw, xC + 30, yc)
    f.line(xA - 30, yc, 216, yc); cell_h(f, 220, yc, plus_left=True); f.line(224, yc, 292, yc); key(f, 300, yc); f.line(308, yc, xC + 30, yc)
    f.text(220, yc - 16, "E", italic=True)
    return f.svg()


def fig_a5b_zf():
    f = Fig(340, 230, "fig_a5b_zf")
    ox, oy = 50, 200
    axes(f, ox, oy, 320, 20, "f", "Z")
    f0x = 160
    pts = []
    for k in range(1, 270):
        x = ox + 2 + k
        fr = (x - ox) / (f0x - ox)
        z = math.sqrt(1 + (2.2 * (fr - 1 / fr)) ** 2)
        y = oy - 30 * z
        if y > 25:
            pts.append((x, y))
    polyline(f, pts, color=BLUE, w=2.2)
    f.line(f0x, oy, f0x, oy - 30, dash="4 3", color=GREY)
    f.line(ox, oy - 30, f0x, oy - 30, dash="4 3", color=GREY)
    f.text(ox - 6, oy - 26, "R", italic=True, anchor="end")
    f.text(f0x, oy + 18, "f₀", italic=True)
    f.text(f0x + 40, oy - 14, "Z", sub="min", size=12, anchor="start")
    f.text(f0x + 64, oy - 14, "= R at f₀", size=12, anchor="start")
    return f.svg()


def fig_a6b_voltmeter():
    f = Fig(380, 120, "fig_a6b_voltmeter")
    y = 60
    dot(f, 30, y, 4); dot(f, 350, y, 4)
    f.line(30, y, 90, y); meter(f, 105, y, "G", r=15); f.line(120, y, 180, y)
    resistor(f, 180, y, 300, y, n=6, lead=10); f.line(300, y, 350, y)
    f.text(105, y + 34, "G = 50 Ω", size=12); f.text(240, y - 18, "R = 1950 Ω (series)", size=12)
    f.text(30, y + 26, "+", size=14, bold=True); f.text(350, y + 26, "−", size=14, bold=True)
    f.text(190, y + 50, "range 0 – 20 V, Ig = 10 mA", size=12)
    return f.svg()


def fig_a7a_torque():
    f = Fig(520, 260, "fig_a7a_torque")
    # left: front view of loop PQRS in field B (to the right), axis vertical
    x0, y0, w_, h_ = 40, 50, 140, 150
    for yy in (40, 90, 140, 190, 240):
        f.arrow(20, yy, 230, yy, color=GREY, w=1)
    f.text(226, 32, "B", italic=True, bold=True, color=GREY)
    f.rect(x0, y0, w_, h_, w=2.2, color=BLUE)
    for (x, y, lab, dx, dy) in ((x0, y0, "P", -10, -4), (x0 + w_, y0, "Q", 10, -4), (x0 + w_, y0 + h_, "R", 10, 16), (x0, y0 + h_, "S", -10, 16)):
        f.text(x + dx, y + dy, lab, bold=True)
    mid_arrow(f, x0, y0 + h_, x0, y0, color=BLUE, size=10)
    mid_arrow(f, x0 + w_, y0, x0 + w_, y0 + h_, color=BLUE, size=10)
    f.text(x0 + w_ / 2, y0 + h_ + 34, "front view (plane of loop ∥ B: θ = 90°)", size=11)
    f.text(x0 - 14, y0 + h_ / 2, "l", italic=True, anchor="end"); f.text(x0 + w_ / 2, y0 - 8, "b", italic=True)
    # forces on PS (out of page) and QR (into page)
    f.circle(x0 + w_, y0 + 40, 7, color=RED); dot(f, x0 + w_, y0 + 40, 2, RED)
    f.circle(x0, y0 + 40, 7, color=RED)
    f.line(x0 - 5, y0 + 35, x0 + 5, y0 + 45, color=RED); f.line(x0 - 5, y0 + 45, x0 + 5, y0 + 35, color=RED)
    f.text(x0 + 10, y0 + 28, "F (into)", size=10, color=RED, anchor="start")
    f.text(x0 + w_ - 10, y0 + 28, "F (out)", size=10, color=RED, anchor="end")
    # right: top view
    cx, cy = 390, 130
    for yy in (60, 100, 160, 200):
        f.arrow(270, yy, 510, yy, color=GREY, w=1)
    f.text(505, 52, "B", italic=True, bold=True, color=GREY)
    th = math.radians(60)          # angle between normal and B
    # loop seen edge-on: a line of length b perpendicular to the normal
    nx, ny = math.cos(th), -math.sin(th)
    px, py = -ny, nx
    half = 70
    a1 = (cx + px * half, cy + py * half); a2 = (cx - px * half, cy - py * half)
    f.line(*a1, *a2, w=3, color=BLUE)
    f.arrow(cx, cy, cx + nx * 60, cy + ny * 60, color=GREEN, w=2)
    f.text(cx + nx * 64, cy + ny * 64, "n", italic=True, bold=True, color=GREEN)
    f.line(cx, cy, cx + 80, cy, dash="4 3", color=GREY)
    arc(f, cx, cy, 30, 0, -60, color=GREEN)
    f.text(cx + 36, cy - 12, "θ", italic=True, color=GREEN, anchor="start")
    # forces F = IlB perpendicular to B (up/down in this view) at the two edges
    f.arrow(a1[0], a1[1], a1[0], a1[1] + 50, color=RED, w=2.2)
    f.arrow(a2[0], a2[1], a2[0], a2[1] - 50, color=RED, w=2.2)
    f.text(a1[0] + 6, a1[1] + 44, "F = IlB", size=12, color=RED, anchor="start")
    f.text(a2[0] - 6, a2[1] - 40, "F", size=12, color=RED, anchor="end")
    # perpendicular distance between the lines of action = b sin θ
    yb_ = max(a1[1], a2[1]) + 70
    f.line(a1[0], a1[1] + 50, a1[0], yb_, dash="2 3", color=GREY, w=1)
    f.line(a2[0], a2[1], a2[0], yb_, dash="2 3", color=GREY, w=1)
    f.line(a1[0], yb_ - 6, a2[0], yb_ - 6, color="#333", w=1)
    f.text((a1[0] + a2[0]) / 2, yb_ - 10, "b sin θ", size=12)
    f.text(cx, 250, "top view", size=11)
    return f.svg()


def fig_a8a_lensmaker():
    f = Fig(560, 260, "fig_a8a_lensmaker")
    cy = 150
    xl = 280
    f.line(10, cy, 550, cy, color=GREY, w=1)
    convex_lens(f, xl, cy, 90, t=26)
    O, I1, I = (40, cy), (530, cy), (430, cy)
    h = 55
    # first surface hit point (left face) and second (right face)
    N1 = (xl - 11, cy - h); N2 = (xl + 11, cy - h + 6)
    ray(f, [O, N1, N2], color=RED)
    ray(f, [N2, I], color=RED)
    f.line(N2[0], N2[1], I1[0], I1[1], dash="4 4", color=RED, w=1)
    for p, lab in ((O, "O"), (I, "I"), (I1, "I₁")):
        dot(f, *p, 3); f.text(p[0], cy + 18, lab, size=13)
    f.text(xl - 40, cy - 100, "R₁ (first surface)", size=12, anchor="end")
    f.text(xl + 40, cy - 100, "R₂ (second surface)", size=12, anchor="start")
    f.text(110, 215, "medium μ₁", size=13); f.text(xl, 30, "lens μ₂", size=13, color=BLUE); f.text(470, 215, "medium μ₁", size=13)
    f.text(xl, 250, "I₁: image by surface 1 alone = virtual object for surface 2", size=12)
    f.line(xl - 10, cy + 100, xl - 10, cy + 108, color=GREY); f.line(xl + 10, cy + 100, xl + 10, cy + 108, color=GREY)
    f.text(xl, cy + 122, "thin: t ≈ 0", size=11)
    return f.svg()


def fig_a8b_prism():
    f = Fig(480, 345, "fig_a8b_prism")
    A = (210, 30); B = (60, 30 + 150 * math.sqrt(3)); C = (360, 30 + 150 * math.sqrt(3))
    f.path(f"M {A[0]} {A[1]} L {B[0]} {B[1]} L {C[0]} {C[1]} Z", fill="#e8f0fb", color=BLUE, w=2)
    f.text(A[0], A[1] - 8, "A", bold=True); f.text(B[0] - 10, B[1] + 6, "B", bold=True, anchor="end"); f.text(C[0] + 10, C[1] + 6, "C", bold=True, anchor="start")
    # entry point on AB at t, ray normal to AB enters undeviated
    t = 0.35
    P = (A[0] + (B[0] - A[0]) * t, A[1] + (B[1] - A[1]) * t)
    nAB = (math.cos(math.radians(-30)), math.sin(math.radians(-30)))   # inward normal of AB (up-right)
    # outward of AB is (-cos30, +sin30)? compute: AB direction
    dx, dy = B[0] - A[0], B[1] - A[1]; L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
    nin = (-uy, ux) if (-uy * (C[0] - P[0]) + ux * (C[1] - P[1])) > 0 else (uy, -ux)
    start = (P[0] - nin[0] * 90, P[1] - nin[1] * 90)
    # hit AC: solve P + s*nin on line A->C
    ex_, ey_ = C[0] - A[0], C[1] - A[1]
    den = nin[0] * ey_ - nin[1] * ex_
    s = ((A[0] - P[0]) * ey_ - (A[1] - P[1]) * ex_) / den
    Q = (P[0] + nin[0] * s, P[1] + nin[1] * s)
    acx, acy = ex_ / math.hypot(ex_, ey_), ey_ / math.hypot(ex_, ey_)
    R_ = (Q[0] + acx * 110, Q[1] + acy * 110)   # grazing along AC, onward towards C
    ray(f, [start, P, Q, R_], color=RED)
    # normal at Q
    nAC = (acy, -acx)
    f.line(Q[0] - nAC[0] * 60, Q[1] - nAC[1] * 60, Q[0] + nAC[0] * 60, Q[1] + nAC[1] * 60, dash="4 3", color=GREEN)
    a_in = ang(*P, *Q); a_n = ang(Q[0], Q[1], Q[0] + nAC[0], Q[1] + nAC[1])
    a_n2 = ang(Q[0], Q[1], Q[0] - nAC[0], Q[1] - nAC[1])
    nn = a_n if abs((a_n - a_in + 540) % 360 - 180) < 90 else a_n2
    # mark the angle of incidence INSIDE the glass: between the ray (towards P) and the inward normal
    arc(f, *Q, 28, (nn + 180) % 360, (a_in + 180) % 360, color=GREEN)
    f.text(Q[0] - 36, Q[1] + 4, "60°", size=12, color=GREEN, anchor="end")
    f.text(Q[0] + nAC[0] * 60 + 4, Q[1] + nAC[1] * 60 - 6, "normal", size=11, color=GREEN, anchor="start")
    f.text(185, 312, "angle of incidence at AC = 60° = critical angle", size=12, color=GREEN)
    f.text(R_[0] + 10, R_[1] - 4, "grazing emergence", size=12, color=RED, anchor="start")
    f.text(R_[0] + 10, R_[1] + 12, "(e = 90°)", size=12, color=RED, anchor="start")
    f.text(start[0] + 30, start[1] - 22, "normal incidence", size=12, anchor="middle")
    f.text(175, 240, "glass μg = 1.45", size=13, color=BLUE)
    f.text(210, 334, "prism immersed in liquid of refractive index μl", size=12)
    return f.svg()


def fig_a9a_micro():
    svg, _ = microscope("fig_a9a_micro")
    return svg


def fig_a11a_cylinder():
    f = Fig(460, 230, "fig_a11a_cylinder")
    s = 12.0
    x0, yb = 50, 190
    W, Hw = 30 * s, 7 * s
    f.raw(f'<rect x="{x0}" y="{yb-Hw}" width="{W}" height="{Hw}" fill="#d6e9f8"/>')
    f.line(x0, yb - Hw - 50, x0, yb, w=2); f.line(x0 + W, yb - Hw - 50, x0 + W, yb, w=2); f.line(x0, yb, x0 + W, yb, w=2)
    S = (x0 + W / 2, yb)
    dot(f, *S, 4, RED); f.text(S[0], yb + 18, "S", bold=True)
    rr = 3 * math.sqrt(7) * s
    for sgn in (1, -1):
        Pp = (S[0] + sgn * rr, yb - Hw)
        f.line(*S, *Pp, color=RED, w=1.6)
        f.line(Pp[0], Pp[1], Pp[0] + sgn * 70, Pp[1], color=RED, w=1.6)   # grazing along the surface
    f.line(S[0], yb, S[0], yb - Hw - 30, dash="4 3", color=GREY)
    arc(f, *S, 30, -90, ang(*S, S[0] + rr, yb - Hw), color=GREEN)
    f.text(S[0] + 16, yb - 38, "C", italic=True, color=GREEN, anchor="start")
    f.line(S[0], yb - Hw - 6, S[0] + rr, yb - Hw - 6, color=BLUE, w=1.4)
    f.text(S[0] + rr / 2, yb - Hw - 12, "r", italic=True, color=BLUE)
    f.text(x0 + W + 8, yb - Hw / 2, "h = 7 cm", size=12, anchor="start")
    f.text(x0 + 8, yb - 10, "water μ = 4/3", size=12, anchor="start")
    f.text(x0 + W / 2, 18, "only light inside this circle (radius r) escapes", size=12)
    return f.svg()


def fig_a11b_angles():
    f = Fig(360, 250, "fig_a11b_angles")
    cx, cy = 180, 120
    f.raw(f'<rect x="20" y="{cy}" width="320" height="120" fill="#e8f0fb"/>')
    f.line(20, cy, 340, cy, w=2)
    f.line(cx, 10, cx, 240, dash="4 3", color=GREY)
    L = 100
    inc = (cx - L * math.sin(math.radians(60)), cy - L * math.cos(math.radians(60)))
    refl = (cx + L * math.sin(math.radians(60)), cy - L * math.cos(math.radians(60)))
    refr = (cx + L * math.sin(math.radians(30)), cy + L * math.cos(math.radians(30)))
    ray(f, [inc, (cx, cy)], color=RED); ray(f, [(cx, cy), refl], color=RED); ray(f, [(cx, cy), refr], color=BLUE)
    arc(f, cx, cy, 34, -90, -150, color=RED); f.text(cx - 26, cy - 40, "60°", size=12, color=RED, anchor="end")
    arc(f, cx, cy, 34, -90, -30, color=RED); f.text(cx + 26, cy - 40, "60°", size=12, color=RED, anchor="start")
    arc(f, cx, cy, 40, 90, 60, color=BLUE); f.text(cx - 8, cy + 60, "r = 30°", size=12, color=BLUE, anchor="end")
    arc(f, cx, cy, 22, -30, 60, color=GREEN); f.text(cx + 30, cy + 14, "90°", size=12, color=GREEN, anchor="start")
    f.text(40, cy - 8, "air", size=12, anchor="start"); f.text(40, cy + 22, "glass", size=12, anchor="start")
    return f.svg()


def fig_a12a_bohr():
    return bohr_orbit("fig_a12a_bohr")


def _zener_symbol(f, x, yc):
    """Zener diode on a vertical wire, cathode at the TOP (reverse biased when top is +)."""
    s = 14
    f.raw(f'<path d="M {x-s/2} {yc+s/2} L {x} {yc-s/2} L {x+s/2} {yc+s/2} Z" fill="#111"/>')
    f.path(f"M {x-s/2-4} {yc-s/2+4} L {x-s/2} {yc-s/2} L {x+s/2} {yc-s/2} L {x+s/2+4} {yc-s/2-4}", w=2)


def fig_a14a_zener():
    f = Fig(480, 200, "fig_a14a_zener")
    yt, yb = 50, 160
    dot(f, 30, yt, 4); dot(f, 30, yb, 4)
    f.text(22, yt + 4, "+", size=15, bold=True, anchor="end"); f.text(22, yb + 4, "−", size=15, bold=True, anchor="end")
    f.text(40, 112, "unregulated", size=11, anchor="start"); f.text(40, 126, "input Vᵢ", size=11, anchor="start")
    f.line(30, yt, 80, yt); resistor(f, 80, yt, 190, yt, n=5, lead=8); f.line(190, yt, 420, yt)
    f.text(135, yt - 14, "Rs", italic=True)
    f.line(30, yb, 420, yb)
    xz = 250
    f.line(xz, yt, xz, 98); _zener_symbol(f, xz, 105); f.line(xz, 112, xz, yb)
    f.text(xz + 16, 108, "Zener (reverse bias)", size=11, anchor="start")
    xr = 380
    resistor(f, xr, yt, xr, yb, n=5)
    f.text(xr + 12, 108, "Rʟ", italic=True, anchor="start")
    dot(f, 420, yt, 4); dot(f, 420, yb, 4)
    f.text(440, 100, "V₀", size=13, anchor="start"); f.text(440, 116, "= Vz", size=13, anchor="start")
    dot(f, xz, yt, 3); dot(f, xz, yb, 3); dot(f, xr, yt, 3); dot(f, xr, yb, 3)
    f.arrow(100, yt + 16, 170, yt + 16, color=RED, w=1.2); f.text(135, yt + 32, "I", italic=True, color=RED)
    return f.svg()


def fig_a14a_zener_iv():
    f = Fig(380, 260, "fig_a14a_zener_iv")
    ox, oy = 220, 110
    f.arrow(20, oy, 365, oy); f.arrow(ox, 250, ox, 15)
    f.text(360, oy - 8, "V (forward)", size=12, anchor="end"); f.text(ox + 6, 22, "I (mA)", size=12, anchor="start")
    f.text(24, oy + 18, "reverse V", size=12, anchor="start"); f.text(ox + 6, 245, "I (μA → mA)", size=12, anchor="start")
    fw = [(ox + v, oy - 2.2 * math.exp((v - 40) / 9)) for v in range(0, 80)]
    fw = [(x, y) for x, y in fw if y > 20]
    polyline(f, fw, color=BLUE, w=2.2)
    xz = 90
    rv = [(ox - v, oy + 0.02 * v) for v in range(0, ox - xz)] + [(xz - 2, oy + 30), (xz - 6, oy + 130)]
    polyline(f, rv, color=BLUE, w=2.2)
    f.line(xz, oy, xz, oy - 10, color="#333")
    f.text(xz, oy - 14, "−Vz", size=12)
    f.text(xz + 12, oy + 100, "breakdown: V ≈ Vz", size=11, color=RED, anchor="start")
    f.text(xz + 12, oy + 114, "for a wide range of I", size=11, color=RED, anchor="start")
    return f.svg()
