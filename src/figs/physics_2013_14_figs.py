"""Figures for the Heritage pre-board Physics 2013-14 theory paper and practical paper (agent A)."""
import math
from svg import Fig
from physA_lib import (resistor, cell, capacitor, dot, cross, acsource, arc, ang, axes, lens,
                       BLUE, RED, GREEN, GREY, ORANGE)


# ------------------------------------------------------------------ theory: question figures
def fig_q1b4_ac():
    """1(B)(iv): one cycle of a sinusoidal current of peak 5 sqrt2 A (as printed)."""
    f = Fig(420, 220, "fig_q1b4_ac")
    ox, oy, A = 80, 110, 70
    f.arrow(ox, 200, ox, 18)
    f.arrow(ox, oy, 400, oy)
    pts = []
    for k in range(0, 101):
        t = k / 100
        pts.append((ox + 260 * t, oy - A * math.sin(2 * math.pi * t)))
    f.path("M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts), color=BLUE, w=2)
    f.line(ox, oy - A, 360, oy - A, color=GREY, w=1, dash="5 4")
    f.line(ox, oy + A, 360, oy + A, color=GREY, w=1, dash="5 4")
    f.text(ox - 8, oy - A + 5, "5√2", anchor="end", size=14)
    f.text(ox - 8, oy + A + 5, "−5√2", anchor="end", size=14)
    f.text(ox - 8, oy + 5, "0", anchor="end", size=14)
    f.text(30, 70, "I (A)", size=14, italic=True)
    f.text(ox + 8, 30, "Y", anchor="start", size=13)
    f.text(395, oy - 8, "X", size=13)
    f.text(330, oy + A + 24, "t (second)", size=14, italic=True)
    return f.svg()


def fig_q2b_caps():
    """2(b): 8, 16, 24 µF in series across 110 V (as printed)."""
    f = Fig(440, 200, "fig_q2b_caps")
    top, bot, L, R = 50, 160, 40, 400
    f.line(L, top, R, top); f.line(L, top, L, bot); f.line(R, top, R, bot)
    for x, nm, val in ((110, "C", "8 µF"), (220, "C", "16 µF"), (330, "C", "24 µF")):
        f.raw(f'<rect x="{x-6}" y="{top-14}" width="12" height="28" fill="#fff" stroke="none"/>')
        capacitor(f, x, top)
        f.text(x, top - 20, nm, size=15, sub=str(1 + (x - 110) // 110))
        f.text(x, top + 32, val, size=14)
    f.line(L, bot, 260, bot); f.line(272, bot, R, bot)
    f.raw(f'<rect x="258" y="{bot-14}" width="16" height="28" fill="#fff" stroke="none"/>')
    cell(f, 266, bot, plus_first=True)
    f.text(266, bot + 30, "110 V", size=14)
    return f.svg()


def fig_q6c_lens_mirror():
    """6(c): biconvex glass lens resting on a plane mirror, liquid filling the gap (as printed)."""
    f = Fig(420, 190, "fig_q6c_lens_mirror")
    y0 = 140
    # mirror with hatching
    f.line(40, y0, 360, y0, w=2.4)
    for x in range(46, 360, 14):
        f.line(x, y0 + 2, x - 9, y0 + 13, color=GREY, w=1)
    # liquid (plano-concave) filling between the lower lens surface and the mirror
    f.path(f"M 90 {y0} L 90 {y0-14} Q 200 {y0+14} 310 {y0-14} L 310 {y0} Z", color="none", fill="#cfe8f7")
    # biconvex lens whose lower face touches the mirror at the centre
    f.path(f"M 90 {y0-14} Q 200 {y0-90} 310 {y0-14} Q 200 {y0+14} 90 {y0-14} Z", color=BLUE, w=1.6, fill="#e8eef8")
    f.text(200, 40, "μ = 3/2 (glass)", size=14)
    f.arrow(200, 46, 200, 92, color="#333", w=1.2)
    f.text(372, 120, "μ = 4/3", size=14, anchor="middle")
    f.text(372, 136, "(water)", size=12)
    f.arrow(345, 128, 300, 134, color="#333", w=1.2)
    f.text(200, 178, "plane mirror", size=13)
    return f.svg()


def fig_q10b_transistor():
    """10(b): the printed common-emitter circuit (redrawn).  The printed emitter arrow points IN
    (towards the base) — a p-n-p transistor — and the collector cell has its long (+) plate at the
    bottom (N/O side), i.e. the collector is negative with respect to the emitter, as p-n-p needs."""
    f = Fig(460, 300, "fig_q10b_transistor")
    # transistor circle
    cx, cy = 200, 120
    f.circle(cx, cy, 34)
    f.line(cx - 12, cy - 20, cx - 12, cy + 20, w=3)          # base bar
    f.line(cx - 50, cy, cx - 12, cy)                          # base lead
    f.line(cx - 12, cy - 8, cx + 10, cy - 26)                 # collector
    f.line(cx + 10, cy - 26, cx + 10, cy - 70)
    f.line(cx - 12, cy + 8, cx + 10, cy + 26)                 # emitter
    f.arrow(cx + 10, cy + 26, cx - 3, cy + 15.4)              # arrow pointing in (p-n-p), as printed
    f.line(cx + 10, cy + 26, cx + 10, 250)
    f.text(cx - 22, cy - 18, "b", size=13, italic=True)
    f.text(cx + 20, cy - 34, "c", size=13, italic=True)
    f.text(cx + 20, cy + 34, "e", size=13, italic=True)
    # collector to P - M, load, battery, N
    f.line(cx + 10, cy - 70, 380, cy - 70)
    f.text(cx + 10, cy - 78, "P", size=13)
    f.text(388, cy - 74, "M", size=13, anchor="start")
    resistor(f, 380, cy - 70, 380, 170, n=5)
    f.text(396, 115, "Load", size=13, anchor="start")
    f.line(380, 170, 380, 195)
    cell(f, 380, 201, horizontal=False, plus_first=False)     # long (+) plate at the bottom, as printed
    f.line(380, 207, 380, 250)
    f.line(cx + 10, 250, 380, 250)
    f.text(cx + 10, 268, "O", size=13); f.text(388, 254, "N", size=13, anchor="start")
    # input side: A - source - B, base battery
    f.line(cx - 50, cy, 60, cy)
    f.text(52, cy - 4, "A", size=13, anchor="end")
    f.line(60, cy, 60, 158); acsource(f, 60, 170); f.line(60, 182, 60, 250)
    f.text(52, 254, "B", size=13, anchor="end")
    f.line(60, 250, 120, 250)
    cell(f, 126, 250, plus_first=False)
    f.line(132, 250, cx + 10, 250)
    return f.svg()


def fig_q10c_gates():
    """10(c): NAND gate driving a NAND gate whose two inputs are tied together (as printed)."""
    f = Fig(460, 140, "fig_q10c_gates")
    def nand(x, y):
        f.path(f"M {x} {y-30} L {x+40} {y-30} A 30 30 0 0 1 {x+40} {y+30} L {x} {y+30} Z", fill="#fff")
        f.circle(x + 76, y, 6, fill="#fff")
    nand(90, 70)
    f.line(30, 55, 90, 55); f.line(30, 85, 90, 85)
    f.circle(30, 55, 2.5); f.circle(30, 85, 2.5)
    f.text(20, 60, "A", size=14, anchor="end"); f.text(20, 90, "B", size=14, anchor="end")
    nand(270, 70)
    f.line(172, 70, 230, 70)
    f.line(230, 55, 230, 85); f.line(230, 55, 270, 55); f.line(230, 85, 270, 85)
    dot(f, 230, 70, 2.5)
    f.line(352, 70, 420, 70); f.circle(420, 70, 2.5)
    f.text(430, 75, "Y", size=14, anchor="start")
    return f.svg()


# ------------------------------------------------------------------ theory: answer figures
def fig_a1b3_radial():
    """Radial magnetic field: concave pole pieces round a soft-iron cylinder."""
    f = Fig(360, 230, "fig_a1b3_radial")
    cx, cy, r, R = 180, 115, 40, 78
    f.path(f"M 40 30 L 120 30 L 120 {cy-58} A {R} {R} 0 0 0 120 {cy+58} L 120 200 L 40 200 Z", fill="#f3d6d2", color=RED)
    f.path(f"M 320 30 L 240 30 L 240 {cy-58} A {R} {R} 0 0 1 240 {cy+58} L 240 200 L 320 200 Z", fill="#d6e2f3", color=BLUE)
    f.text(70, 120, "N", size=22, bold=True, color=RED); f.text(290, 120, "S", size=22, bold=True, color=BLUE)
    f.circle(cx, cy, r, fill="#ddd")
    f.text(cx, cy + 5, "soft iron", size=11)
    for a in (-40, -20, 0, 20, 40):
        t = math.radians(a)
        for side in (-1, 1):
            x1 = cx + side * R * math.cos(t) * 0.99; y1 = cy - R * math.sin(t)
            x2 = cx + side * r * math.cos(t); y2 = cy - r * math.sin(t)
            if side == -1:
                f.arrow(x1, y1, x2, y2, color=GREEN, w=1.2)
            else:
                f.arrow(x2, y2, x1, y1, color=GREEN, w=1.2)
    # coil sides (in the gap), shown as small squares
    for side in (-1, 1):
        f.rect(cx + side * 59 - 5, cy - 5, 10, 10, fill="#ffc", color="#111", w=1.2)
    f.text(180, 222, "field lines radial: plane of coil always parallel to B", size=12)
    return f.svg()


def fig_a1b15_visual_angle():
    """Visual angle: the near moon subtends a larger angle at the eye than a far, larger star."""
    f = Fig(520, 190, "fig_a1b15_visual_angle")
    ex, ey = 30, 100
    f.circle(ex, ey, 8, fill="#fff"); f.text(ex, ey - 16, "eye", size=12)
    mx, mr, sx, sr = 150, 24, 440, 34
    f.line(ex, ey, mx, ey - mr, color=BLUE, w=1.2); f.line(ex, ey, mx, ey + mr, color=BLUE, w=1.2)
    f.line(ex, ey, sx, ey - sr, color=ORANGE, w=1, dash="4 3"); f.line(ex, ey, sx, ey + sr, color=ORANGE, w=1, dash="4 3")
    f.circle(mx, ey, mr, fill="#eee", color="#555")
    f.circle(sx, ey, sr, fill="#fff3c4", color=ORANGE)
    f.text(mx, ey + 46, "Moon (small, near)", size=12)
    f.text(sx, ey + 56, "Star (huge, very far)", size=12)
    # both angles are measured AT THE EYE (review fix: β used to be drawn out near the star)
    arc(f, ex, ey, 48, ang(ex, ey, mx, ey - mr), ang(ex, ey, mx, ey + mr), color=BLUE)
    f.text(ex + 40, ey - 12, "α", size=15, italic=True, anchor="end", color=BLUE)
    arc(f, ex, ey, 84, ang(ex, ey, sx, ey - sr), ang(ex, ey, sx, ey + sr), color=ORANGE, w=1.6)
    f.text(ex + 86, ey + 22, "β", size=15, italic=True, anchor="start", color=ORANGE)
    f.text(260, 24, "Apparent size is set by the angle subtended at the eye: α (moon) ≫ β (star)", size=12)
    return f.svg()


def fig_a2a_dipole_equatorial():
    """Field of a dipole at P on the perpendicular bisector: E+ away from +q, E− towards −q."""
    f = Fig(460, 330, "fig_a2a_dipole_equatorial")
    Ax, Bx, y = 130, 330, 270           # −q at A (left), +q at B (right)
    Ox, Py = 230, 110
    f.line(60, y, 400, y, color=GREY, w=1, dash="5 4")
    f.line(Ox, y + 20, Ox, 40, color=GREY, w=1, dash="5 4")
    f.circle(Ax, y, 11, fill="#d6e2f3", color=BLUE); f.text(Ax, y + 5, "−q", size=13)
    f.circle(Bx, y, 11, fill="#f3d6d2", color=RED); f.text(Bx, y + 5, "+q", size=13)
    f.text(Ax, y + 34, "A", size=14); f.text(Bx, y + 34, "B", size=14); f.text(Ox + 10, y + 18, "O", size=14)
    f.arrow(Ox - 60, y + 50, Ox + 60, y + 50, color=GREEN, w=2)
    f.text(Ox + 70, y + 55, "p", size=16, italic=True, bold=True, anchor="start", color=GREEN)
    f.text(Ox - 50, y + 18, "l", size=14, italic=True); f.text(Ox + 50, y + 18, "l", size=14, italic=True)
    f.line(Ax, y, Ox, Py, color="#555", w=1); f.line(Bx, y, Ox, Py, color="#555", w=1)
    dot(f, Ox, Py)
    f.text(Ox + 10, Py + 26, "P", size=15, anchor="start")
    f.text(Ox + 8, (y + Py) / 2 + 18, "r", size=15, italic=True, anchor="start")
    # unit vectors
    L = 70
    dBx, dBy = Ox - Bx, Py - y; n = math.hypot(dBx, dBy); dBx, dBy = dBx / n, dBy / n      # B->P (away from +q)
    dAx, dAy = Ax - Ox, y - Py; n = math.hypot(dAx, dAy); dAx, dAy = dAx / n, dAy / n      # P->A (towards −q)
    f.arrow(Ox, Py, Ox + L * dBx, Py + L * dBy, color=RED, w=2)
    f.text(Ox + L * dBx - 8, Py + L * dBy - 6, "E", size=15, italic=True, color=RED, sub="+", anchor="end")
    f.arrow(Ox, Py, Ox + L * dAx, Py + L * dAy, color=BLUE, w=2)
    f.text(Ox + L * dAx - 8, Py + L * dAy + 14, "E", size=15, italic=True, color=BLUE, sub="−", anchor="end")
    rx = L * (dAx + dBx)
    f.arrow(Ox, Py, Ox + rx, Py, color="#111", w=2.6)
    f.text(Ox + rx - 6, Py - 10, "E (resultant)", size=13, anchor="middle")
    # angle theta at B and at A
    th = math.degrees(math.atan2(y - Py, Bx - Ox))
    arc(f, Bx, y, 34, 180, 180 - th, color=RED)
    f.text(Bx - 44, y - 10, "θ", size=14, italic=True, color=RED)
    arc(f, Ax, y, 34, 0, th, color=BLUE)
    f.text(Ax + 44, y - 10, "θ", size=14, italic=True, color=BLUE)
    return f.svg()


def fig_a6c_liquid_lens():
    """6(c): the object coincides with its image when rays leave the lens + liquid-lens system
    parallel to the axis, strike the mirror normally and retrace their path."""
    f = Fig(440, 300, "fig_a6c_liquid_lens")
    ax, y0 = 160, 250            # axis vertical at x = ax; mirror at y0
    f.line(40, y0, 280, y0, w=2.4)
    for x in range(46, 280, 14):
        f.line(x, y0 + 2, x - 9, y0 + 13, color=GREY, w=1)
    f.path(f"M 70 {y0} L 70 {y0-12} Q {ax} {y0+12} 250 {y0-12} L 250 {y0} Z", color="none", fill="#cfe8f7")
    f.path(f"M 70 {y0-12} Q {ax} {y0-60} 250 {y0-12} Q {ax} {y0+12} 70 {y0-12} Z", color=BLUE, w=1.6, fill="#e8eef8")
    f.line(ax, 20, ax, y0, color=GREY, w=1, dash="5 4")
    Oy = 50
    dot(f, ax, Oy, 3.5, color=RED)
    f.text(ax + 10, Oy - 4, "O ≡ I", size=14, anchor="start", color=RED)
    for xh in (110, 210):
        yl = y0 - 34
        f.line(ax, Oy, xh, yl, color=RED, w=1.4)
        f.arrow(xh, yl, xh, y0 - 4, color=RED, w=1.4)
        f.arrow(xh + 4, y0 - 4, xh + 4, yl + 4, color=GREEN, w=1.2)
    f.text(ax - 62, (Oy + y0) / 2 - 20, "F = 15 cm (water)", size=12, anchor="end")
    f.text(ax - 62, (Oy + y0) / 2 - 4, "or 25 cm (liquid)", size=12, anchor="end")
    # decomposition on the right
    bx = 350
    f.text(bx, 40, "the system =", size=13)
    f.path(f"M {bx-50} 80 Q {bx} 50 {bx+50} 80 Q {bx} 110 {bx-50} 80 Z", color=BLUE, fill="#e8eef8")
    f.text(bx, 128, "convex glass lens f₁", size=12)
    f.text(bx, 150, "+", size=16)
    # plano-concave: flat face on the mirror, concave upper face (the lens's lower face), thin at the centre
    f.path(f"M {bx-50} 200 L {bx+50} 200 L {bx+50} 176 Q {bx} 212 {bx-50} 176 Z", color=BLUE, fill="#cfe8f7")
    f.text(bx, 222, "plano-concave liquid lens f₂", size=12)
    f.text(bx, 244, "(same R as the lens face)", size=11)
    return f.svg()


def fig_a8a_selector():
    """8(a): crossed fields for an undeviated electron: v right, E down, B into the page."""
    f = Fig(450, 230, "fig_a8a_selector")
    for i in range(7):
        for j in range(4):
            cross(f, 60 + 50 * i, 40 + 50 * j)
    f.arrow(420, 30, 420, 120, color=BLUE, w=2.4)
    f.text(428, 80, "E", size=16, italic=True, color=BLUE, anchor="start")
    cx, cy = 180, 115
    f.circle(cx, cy, 10, fill="#ffeeb0"); f.text(cx, cy + 5, "e", size=13)
    f.arrow(cx + 10, cy, cx + 90, cy, color="#111", w=2.2); f.text(cx + 96, cy + 5, "v", size=16, italic=True, anchor="start")
    f.arrow(cx, cy - 10, cx, cy - 70, color=ORANGE, w=2.2)
    f.raw(f'<rect x="{cx+6}" y="{cy-72}" width="214" height="18" fill="#fff"/>')
    f.text(cx + 8, cy - 58, "F = eE (on electron, opposite E)", size=12, anchor="start", color=ORANGE)
    f.arrow(cx, cy + 10, cx, cy + 70, color=GREEN, w=2.2)
    f.raw(f'<rect x="{cx+6}" y="{cy+52}" width="130" height="18" fill="#fff"/>')
    f.text(cx + 8, cy + 66, "F = evB (magnetic)", size=12, anchor="start", color=GREEN)
    f.text(30, 222, "⊗ B into the page", size=13, anchor="start")
    return f.svg()


def fig_a8c_levels():
    """Hydrogen energy levels with the n = 2 → 1 transition (Lyman α)."""
    f = Fig(400, 260, "fig_a8c_levels")
    def y(E):
        return 30 + (0 - E) / 13.6 * 200
    for n, E in ((1, -13.6), (2, -3.4), (3, -1.51)):
        f.line(80, y(E), 300, y(E), w=1.8)
        f.text(310, y(E) + 5, f"n = {n}", size=13, anchor="start")
        f.text(72, y(E) + 5, f"{E:g} eV", size=12, anchor="end")
    f.line(80, y(0), 300, y(0), dash="5 4", color=GREY)
    f.text(310, y(0) + 5, "n = ∞", size=13, anchor="start"); f.text(72, y(0) + 5, "0", size=12, anchor="end")
    f.arrow(190, y(-3.4), 190, y(-13.6) - 2, color=RED, w=2.2)
    f.text(200, (y(-3.4) + y(-13.6)) / 2, "ΔE = 10.2 eV", size=13, anchor="start", color=RED)
    f.text(200, (y(-3.4) + y(-13.6)) / 2 + 18, "λ ≈ 121 nm (UV, Lyman)", size=13, anchor="start", color=RED)
    return f.svg()


def fig_a10a_bands():
    """Energy bands: insulator (wide gap, empty CB) and semiconductor (narrow gap)."""
    f = Fig(460, 260, "fig_a10a_bands")
    def panel(x0, gap_px, title, gap_text, few):
        f.text(x0 + 80, 22, title, size=14, bold=True)
        cb_bot = 50 + 50
        vb_top = cb_bot + gap_px
        f.rect(x0, 50, 160, 50, fill="#eef4ff", color=BLUE)
        f.text(x0 + 80, 80, "conduction band", size=12)
        f.rect(x0, vb_top, 160, 50, fill="#c9d7ef", color=BLUE)
        f.text(x0 + 80, vb_top + 30, "valence band (full)", size=12)
        f.arrow(x0 + 150, cb_bot + gap_px / 2, x0 + 150, cb_bot + 2, color=RED, w=1.2)
        f.arrow(x0 + 150, cb_bot + gap_px / 2, x0 + 150, vb_top - 2, color=RED, w=1.2)
        f.text(x0 + 140, cb_bot + gap_px / 2 + 5, gap_text, size=12, anchor="end", color=RED)
        if few:
            for k in range(3):
                dot(f, x0 + 30 + 30 * k, 90, 2.5, color="#111")
    panel(20, 110, "Insulator", "Eg > 3 eV (≈ 6 eV)", False)
    panel(270, 30, "Semiconductor", "Eg ≈ 1 eV", True)
    f.arrow(8, 240, 8, 50); f.text(14, 46, "E", size=14, italic=True, anchor="start")
    return f.svg()


# ------------------------------------------------------------------ practical
def fig_pr_bench():
    """Practical Q1, Figure 1: optical bench, object pin O at 0 cm, lens L at 70 cm, image pin I."""
    f = Fig(480, 200, "fig_pr_bench")
    ya = 70
    f.line(30, 150, 430, 150, w=2)                     # bench
    f.line(30, ya, 400, ya, color=GREY, w=1, dash="6 4")   # principal axis
    for x in (60, 290, 370):
        f.rect(x - 6, 100, 12, 50, fill="#ddd", color="#555", w=1)
        f.line(x, 100, x, ya + 6)
    f.arrow(60, ya + 6, 60, ya - 14, w=1.8); f.text(60, ya - 22, "O", size=14)
    lens(f, 290, ya, 32, bulge=7); f.text(290, ya - 40, "L", size=14)
    f.arrow(370, ya + 6, 370, ya - 6, w=1.8); f.text(380, ya - 10, "I", size=14, anchor="start")
    f.arrow(370, 22, 370, ya - 2, color=GREY, w=1, dash="3 3"); f.text(370, 16, "I′", size=13)
    f.path("M 445 60 Q 430 70 445 80 Q 460 70 445 60 Z", fill="#fff"); f.circle(442, 70, 3, fill="#111")
    f.text(445, 46, "eye", size=12)
    f.text(60, 172, "0 cm", size=12); f.text(290, 172, "70.0 cm", size=12)
    f.arrow(175, 186, 62, 186, w=1); f.arrow(175, 186, 288, 186, w=1); f.text(175, 182, "u", size=13, italic=True)
    f.arrow(330, 186, 292, 186, w=1); f.arrow(330, 186, 368, 186, w=1); f.text(330, 182, "v", size=13, italic=True)
    return f.svg()


def fig_pr_bridge():
    """Practical Q2, Figure 2: metre bridge with resistance box (x) in gap MD and wire R in gap DN."""
    f = Fig(480, 230, "fig_pr_bridge")
    yt, yw, yb = 40, 140, 200
    Ax, Bx = 50, 430
    f.line(Ax, yt, Ax, yw); f.line(Bx, yt, Bx, yw)
    f.text(Ax - 6, yt + 4, "M", size=13, anchor="end"); f.text(Bx + 6, yt + 4, "N", size=13, anchor="start")
    f.line(Ax, yt, 140, yt); f.rect(140, yt - 10, 60, 20, fill="#fff"); f.line(200, yt, 260, yt)
    f.text(170, yt - 16, "Resistance box (x)", size=12)
    resistor(f, 260, yt, 360, yt, n=6)
    f.line(360, yt, Bx, yt)
    f.text(310, yt - 14, "R (50 cm wire)", size=12)
    dot(f, 260, yt); f.text(258, yt + 18, "D", size=13, anchor="end")
    f.line(Ax, yw, Bx, yw, w=2.6, color="#8a5a00")
    f.text(Ax - 6, yw + 4, "A", size=13, anchor="end"); f.text(Bx + 6, yw + 4, "B", size=13, anchor="start")
    f.text(Ax + 4, yw + 16, "0 cm", size=11, anchor="start"); f.text(Bx - 4, yw + 16, "100 cm", size=11, anchor="end")
    Cx = 220
    f.line(260, yt, 260, 70); f.circle(260, 82, 12, fill="#fff"); f.text(260, 87, "G", size=13)
    f.line(260, 94, 260, 108); f.line(260, 108, Cx, 108); f.arrow(Cx, 108, Cx, yw - 2)
    f.text(Cx + 8, 122, "J", size=13, anchor="start"); f.text(Cx, yw + 16, "C", size=13)
    f.arrow(140, yw + 26, Ax + 2, yw + 26, w=1); f.arrow(140, yw + 26, Cx - 2, yw + 26, w=1)
    f.text(135, yw + 22, "l cm", size=12, italic=True)
    f.line(Ax, yw, Ax, yb); f.line(Bx, yw, Bx, yb)
    f.line(Ax, yb, 140, yb); f.circle(150, yb, 10, fill="#fff"); dot(f, 150, yb, 2)
    f.text(150, yb + 24, "K", size=13)
    f.line(160, yb, 290, yb); f.line(302, yb, Bx, yb)
    f.raw(f'<rect x="288" y="{yb-14}" width="16" height="28" fill="#fff" stroke="none"/>')
    cell(f, 296, yb, plus_first=True); f.text(296, yb + 24, "E", size=13)
    return f.svg()


def _graph(uid, X, Y, xlab, ylab, xmax, ymax, xt, yt, p1, p2, fmt_slope, p1lab, p2lab):
    """Squared-paper style graph: plotted points (circle with dot), best-fit line through p1-p2
    extended, slope triangle on p1-p2 (two points on the line, not plotted points)."""
    f = Fig(480, 360, uid)
    ox, oy, W, H = 60, 310, 390, 280
    sx, sy = W / xmax, H / ymax
    P = lambda x, y: (ox + x * sx, oy - y * sy)
    for k in range(0, int(xmax / xt) + 1):
        x = ox + k * xt * sx
        f.line(x, oy, x, oy - H, color="#e3e8ef", w=0.8)
        f.text(x, oy + 16, f"{k*xt:g}", size=11)
    for k in range(0, int(round(ymax / yt)) + 1):
        y = oy - k * yt * sy
        f.line(ox, y, ox + W, y, color="#e3e8ef", w=0.8)
        f.text(ox - 6, y + 4, f"{k*yt:g}", size=11, anchor="end")
    f.line(ox, oy, ox + W, oy); f.line(ox, oy, ox, oy - H)
    f.text(ox + W / 2, oy + 36, xlab, size=13)
    f.raw(f'<text x="18" y="{oy-H/2}" font-size="13" text-anchor="middle" font-family="Times New Roman,serif" '
          f'transform="rotate(-90 18 {oy-H/2})">{ylab}</text>')
    m = (p2[1] - p1[1]) / (p2[0] - p1[0]); c = p1[1] - m * p1[0]
    f.line(*P(0, c), *P(xmax, m * xmax + c), color=BLUE, w=1.6)
    for x, y in zip(X, Y):
        px, py = P(x, y)
        f.circle(px, py, 4.5, color=RED, w=1.4, fill="#fff"); dot(f, px, py, 1.4, color=RED)
    a, b = P(*p1), P(*p2)
    f.line(a[0], a[1], b[0], a[1], color=GREEN, w=1.2, dash="5 3")
    f.line(b[0], a[1], b[0], b[1], color=GREEN, w=1.2, dash="5 3")
    dot(f, *a, 3, color=GREEN); dot(f, *b, 3, color=GREEN)
    f.text((a[0] + b[0]) / 2, a[1] + 16, "Δx", size=13, italic=True, color=GREEN)
    f.text(b[0] + 6, (a[1] + b[1]) / 2, "Δy", size=13, italic=True, color=GREEN, anchor="start")
    f.text(a[0] + 30, a[1] - 6, p1lab, size=11, anchor="start", color=GREEN)
    f.text(b[0] - 8, b[1] - 8, p2lab, size=11, anchor="end", color=GREEN)
    f.text(ox + 10, oy - H + 14, fmt_slope, size=12, anchor="start", color=BLUE)
    return f.svg()


PR_X1 = [55.0, 45.0, 35.0, 25.0, 15.0, 5.0]
PR_Y1 = [24.4, 19.6, 15.4, 11.0, 6.6, 2.2]
PR_X2 = [1, 2, 3, 4, 5, 6]
PR_Y2 = [0.40, 0.80, 1.21, 1.60, 2.01, 2.39]


def fig_pr_graph1():
    """Practical Q1: y = 100/(v − F) against x = u − F, sample readings."""
    return _graph("fig_pr_graph1", PR_X1, PR_Y1, "x = u − F  (cm)", "y = 100/(v − F)  (cm⁻¹)",
                  60, 28, 10, 4, (4.0, 1.73), (56.0, 24.67), "slope m = 22.94/52.0 = 0.441",
                  "(4.0, 1.73)", "(56.0, 24.67)")


def fig_pr_graph2():
    """Practical Q2: y = l/(100 − l) against x (ohm), sample readings."""
    return _graph("fig_pr_graph2", PR_X2, PR_Y2, "x  (Ω)", "y = l/(100 − l)", 7, 2.8, 1, 0.4,
                  (0.5, 0.20), (6.5, 2.60), "slope S = 2.40/6.0 = 0.400 Ω⁻¹", "(0.50, 0.20)", "(6.50, 2.60)")
