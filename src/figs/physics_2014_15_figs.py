"""Figures for the Heritage pre-board Physics 2014-15 theory paper (agent A)."""
import math
from svg import Fig
from physA_lib import (resistor, cell, capacitor, dot, cross, acsource, arc, ang, axes, lens,
                       BLUE, RED, GREEN, GREY, ORANGE)


def _diode(f, x1, y1, x2, y2, color="#111"):
    """Diode from anode (x1,y1) to cathode (x2,y2) on a horizontal or vertical wire."""
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L; px, py = -uy, ux
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    s = 11
    ax_, ay_ = mx - ux * s, my - uy * s
    cx_, cy_ = mx + ux * s, my + uy * s
    f.line(x1, y1, ax_, ay_, color=color); f.line(cx_, cy_, x2, y2, color=color)
    f.path(f"M {ax_+px*s:.1f} {ay_+py*s:.1f} L {ax_-px*s:.1f} {ay_-py*s:.1f} L {cx_:.1f} {cy_:.1f} Z",
           color=color, fill=color)
    f.line(cx_ + px * s, cy_ + py * s, cx_ - px * s, cy_ - py * s, color=color, w=2.4)


def _st(f, x, y, a, sub, rest="", size=12, anchor="middle", color="#111", italic=False):
    """text 'a' + subscript 'sub' + 'rest' (plain text only)."""
    from html import escape
    st = ' font-style="italic"' if italic else ""
    f.raw(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{color}" '
          f'font-family="Times New Roman,serif"{st}>{escape(a)}<tspan baseline-shift="sub" font-size="{size*0.72:.1f}">'
          f'{escape(sub)}</tspan>{escape(rest)}</text>')


def _bg(f, x, y, w, h):
    f.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff" stroke="none"/>')


# ------------------------------------------------------------------ question figures
def fig_q1b4_cd():
    """1(B)(iv): two 4-ohm branches between C and D, battery 10 V, 0.5 ohm (as printed)."""
    f = Fig(420, 220, "fig_q1b4_cd")
    Cx, Dx, yt, yb, ym = 90, 330, 40, 110, 75
    f.line(Cx, yt, Cx, yb); f.line(Dx, yt, Dx, yb)
    resistor(f, Cx, yt, 210, yt, n=5); resistor(f, 210, yt, Dx, yt, n=5)
    resistor(f, Cx, yb, 210, yb, n=5); resistor(f, 210, yb, Dx, yb, n=5)
    dot(f, 210, yt); dot(f, 210, yb); dot(f, Cx, ym); dot(f, Dx, ym)
    f.text(210, yt - 12, "A", size=14); f.text(210, yb + 24, "B", size=14)
    f.text(150, yt + 24, "1 Ω", size=13); f.text(270, yt + 24, "3 Ω", size=13)
    f.text(150, yb - 12, "3 Ω", size=13); f.text(270, yb - 12, "1 Ω", size=13)
    f.text(Cx + 10, ym + 5, "C", size=14, anchor="start"); f.text(Dx - 10, ym + 5, "D", size=14, anchor="end")
    f.line(Cx, ym, 40, ym); f.line(40, ym, 40, 180); f.line(40, 180, 204, 180)
    f.line(216, 180, 380, 180); f.line(380, 180, 380, ym); f.line(380, ym, Dx, ym)
    cell(f, 210, 180, plus_first=True)
    f.text(210, 208, "10 V, 0.5 Ω", size=13)
    return f.svg()


def _wire_charge(uid, answer):
    f = Fig(380, 240, uid)
    wx, py, a = 70, 120, 200
    f.line(wx, 20, wx, 225, dash="6 4")
    f.arrow(wx, 80, wx, 35, w=2.2)
    f.text(wx - 10, 60, "I", size=15, italic=True, anchor="end")
    f.line(wx, py, wx + a + 70, py, color=GREY, w=1, dash="5 4")
    dot(f, wx + a, py, 4)
    f.text(wx + a, py - 14, "+Q", size=14); f.text(wx + a - 6, py + 22, "P", size=14)
    f.arrow(wx + a + 4, py, wx + a + 70, py, w=2)
    f.text(wx + a + 72, py - 8, "v", size=15, italic=True, bold=True, anchor="start")
    f.arrow(wx + a / 2, py + 80, wx + 2, py + 80, w=1); f.arrow(wx + a / 2, py + 80, wx + a - 2, py + 80, w=1)
    f.line(wx + a, py + 4, wx + a, py + 86, color=GREY, w=0.8, dash="2 3")
    f.text(wx + a / 2, py + 76, "a", size=14, italic=True)
    if answer:
        cross(f, wx + a + 28, py + 32, 6, color=BLUE)
        f.circle(wx + a + 28, py + 32, 10, color=BLUE)
        f.text(wx + a + 44, py + 37, "B (into page)", size=12, anchor="start", color=BLUE)
        f.arrow(wx + a, py - 4, wx + a, py - 80, color=RED, w=2.4)
        f.text(wx + a + 8, py - 70, "F = Q v × B", size=13, anchor="start", color=RED)
        f.text(wx + a + 8, py - 54, "(parallel to I)", size=12, anchor="start", color=RED)
    return f.svg()


def fig_q1b6_wire():
    """1(B)(vi): charge +Q at distance a from a long wire, moving directly away from it (as printed)."""
    return _wire_charge("fig_q1b6_wire", False)


def fig_a1b6_force():
    """1(B)(vi) answer: B at P is into the page (right-hand grip), F = Qv x B points along I."""
    return _wire_charge("fig_a1b6_force", True)


NET = dict(A=(40, 140), C=(150, 140), T=(320, 45), M=(320, 140), B=(480, 140), D=(320, 235))


def _net(uid, labels=False):
    f = Fig(520, 270, uid)
    P = NET
    for a, b in (("A", "C"), ("C", "T"), ("T", "B"), ("T", "M"), ("C", "M"), ("M", "B"), ("C", "D"), ("D", "B")):
        resistor(f, *P[a], *P[b], n=5, amp=5, lead=(math.dist(P[a], P[b]) - 44) / 2)
    for k in ("A", "B"):
        f.circle(*P[k], 4, fill="#111")
    for k in ("C", "T", "M", "D"):
        dot(f, *P[k], 2.5)
    f.text(30, 145, "A", size=15, anchor="end"); f.text(492, 145, "B", size=15, anchor="start")
    for (x, y) in ((95, 128), (222, 74), (418, 74), (336, 97), (235, 128), (400, 128), (222, 218), (418, 218)):
        f.text(x, y, "R", size=14, anchor="start" if x == 336 else "middle")
    if labels:
        for k, (dx, dy) in (("C", (-6, -10)), ("T", (0, -10)), ("M", (12, 18)), ("D", (0, 22))):
            f.text(P[k][0] + dx, P[k][1] + dy, k, size=13, color=BLUE, bold=True)
    return f.svg()


def fig_q4a_net():
    """4(a): the printed resistor network between A and B (redrawn)."""
    return _net("fig_q4a_net")


def fig_a4a_net_labelled():
    """4(a) answer: junctions named; C-T-B-M is a balanced Wheatstone bridge, so TM carries no current."""
    return _net("fig_a4a_net_labelled", True)


def fig_q4b_circuits():
    """4(b): (a) cell + resistor, (b) cell + capacitor, (c) a.c. source + resistor (as printed)."""
    f = Fig(540, 150, "fig_q4b_circuits")
    for k, x0 in enumerate((20, 200, 380)):
        x1, yt, yb = x0 + 140, 40, 110
        f.line(x0, yt, x0, yb); f.line(x1, yt, x1, yb)
        mid = (x0 + x1) / 2
        if k == 0:
            f.line(x0, yt, mid - 4, yt); f.line(mid + 4, yt, x1, yt); cell(f, mid, yt, plus_first=True)
            f.text(mid - 4, yt - 16, "E", size=14, italic=True)
            resistor(f, x0, yb, x1, yb, n=5)
        elif k == 1:
            f.line(x0, yt, mid - 4, yt); f.line(mid + 4, yt, x1, yt); capacitor(f, mid, yt)
            f.line(x0, yb, mid - 4, yb); f.line(mid + 4, yb, x1, yb); cell(f, mid, yb, plus_first=True)
            f.text(mid + 14, yb - 10, "E", size=14, italic=True, anchor="start")
        else:
            f.line(x0, yt, mid - 11, yt); f.line(mid + 11, yt, x1, yt); acsource(f, mid, yt)
            f.text(mid, yt - 18, "E = E₀ sin ωt", size=13, italic=True)
            resistor(f, x0, yb, x1, yb, n=5)
        f.text(mid, 140, f"({'abc'[k]})", size=14)
    return f.svg()


def fig_a4b_graphs():
    """4(b) answer: I-t graphs for the three circuits."""
    f = Fig(560, 170, "fig_a4b_graphs")
    for k, x0 in enumerate((30, 215, 400)):
        oy = 110 if k == 2 else 130
        f.arrow(x0, oy, x0 + 150, oy); f.arrow(x0, 150, x0, 20)
        f.text(x0 + 148, oy + 16, "t", size=13, italic=True); f.text(x0 + 6, 24, "I", size=13, italic=True, anchor="start")
        if k == 0:
            f.line(x0, 60, x0 + 140, 60, color=BLUE, w=2)
            f.text(x0 - 4, 64, "E/R", size=12, anchor="end")
        elif k == 1:
            f.path(f"M {x0} 30 Q {x0+3} 120 {x0+16} 129 L {x0+140} 129", color=BLUE, w=2)
            f.text(x0 + 30, 70, "momentary charging", size=11, anchor="start")
            f.text(x0 + 30, 84, "pulse, then I = 0", size=11, anchor="start")
        else:
            pts = [(x0 + 140 * t / 100, oy - 50 * math.sin(2 * math.pi * 2 * t / 100)) for t in range(101)]
            f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), color=BLUE, w=2)
            f.text(x0 - 4, oy - 46, "I₀", size=12, anchor="end")
        f.text(x0 + 75, 166, f"({'abc'[k]})", size=13)
    return f.svg()


def _rod(uid, answer):
    f = Fig(440, 230, uid)
    for i in range(8):
        for j in range(5):
            cross(f, 40 + 48 * i, 25 + 45 * j, 4)
    yt, yb, xl, xr = 45, 180, 90, 300
    f.line(xl, yt, xr + 30, yt, w=2); f.line(xl, yb, xr + 30, yb, w=2)
    _bg(f, xl - 10, yt + 40, 20, 56)
    resistor(f, xl, yt, xl, yb, n=5)
    f.line(xr, yt - 12, xr, yb + 12, w=4, color="#8a5a00")
    f.text(xr + 6, yt - 16, "P", size=14, anchor="start"); f.text(xr + 6, yb + 26, "Q", size=14, anchor="start")
    _bg(f, xr + 14, 100, 60, 26)
    f.arrow(xr + 6, 112, xr + 60, 112, w=2.2); f.text(xr + 64, 108, "v", size=15, italic=True, bold=True, anchor="start")
    _bg(f, 58, 96, 24, 30)
    f.text(70, 116, "B", size=15, italic=True, bold=True)
    if answer:
        f.arrow(xr - 10, 160, xr - 10, 70, color=RED, w=1.8)
        f.text(xr - 16, 64, "I", size=14, italic=True, color=RED, anchor="end")
        f.arrow(200, yt - 6, 140, yt - 6, color=RED, w=1.6)
        f.arrow(140, yb + 8, 200, yb + 8, color=RED, w=1.6)
        _bg(f, 200, 130, 92, 22)
        f.arrow(xr - 4, 140, xr - 60, 140, color=GREEN, w=2)
        f.text(xr - 64, 146, "F = BIl", size=13, color=GREEN, anchor="end")
        f.text(220, 222, "applied F = BIl to the right keeps v constant", size=12)
    return f.svg()


def fig_q6b_rod():
    """6(b): rod PQ sliding on rails in B into the page, resistor closing the circuit (as printed)."""
    return _rod("fig_q6b_rod", False)


def fig_a6b_rod():
    """6(b) answer: induced current Q→P in the rod (Fleming / v x B), magnetic force BIl opposes v."""
    return _rod("fig_a6b_rod", True)


# ------------------------------------------------------------------ answer figures
def fig_a2a_dipole_torque():
    """Dipole at angle theta to a uniform field: equal, opposite forces form a couple."""
    f = Fig(420, 250, "fig_a2a_dipole_torque")
    for y in (40, 210):
        f.arrow(30, y, 390, y, color=GREY, w=1)
    f.text(398, 44, "E", size=15, italic=True, anchor="start")
    cx, cy, th, l = 210, 125, 40, 80
    t = math.radians(th)
    px_, py_ = cx + l * math.cos(t), cy - l * math.sin(t)
    nx_, ny_ = cx - l * math.cos(t), cy + l * math.sin(t)
    f.line(nx_, ny_, px_, py_, w=1.6)
    f.circle(px_, py_, 10, fill="#f3d6d2", color=RED); f.text(px_, py_ + 5, "+q", size=11)
    f.circle(nx_, ny_, 10, fill="#d6e2f3", color=BLUE); f.text(nx_, ny_ + 5, "−q", size=11)
    f.arrow(px_ + 10, py_, px_ + 80, py_, color=RED, w=2); f.text(px_ + 84, py_ + 5, "qE", size=13, anchor="start", color=RED)
    f.arrow(nx_ - 10, ny_, nx_ - 80, ny_, color=BLUE, w=2); f.text(nx_ - 84, ny_ + 5, "qE", size=13, anchor="end", color=BLUE)
    f.line(cx - 90, cy, cx + 90, cy, color=GREY, w=1, dash="4 3")
    arc(f, cx, cy, 34, 0, th, color="#111")
    f.text(cx + 42, cy - 10, "θ", size=15, italic=True, anchor="start")
    f.arrow(cx, cy, cx + 0.55 * l * math.cos(t), cy - 0.55 * l * math.sin(t), color=GREEN, w=2.4)
    f.text(cx + 10, cy - 30, "p", size=15, italic=True, bold=True, color=GREEN, anchor="end")
    f.line(px_, py_, px_, ny_, color=GREY, w=1, dash="3 3"); f.line(nx_, ny_, px_, ny_, color=GREY, w=1, dash="3 3")
    f.text(px_ + 6, (py_ + ny_) / 2 + 30, "2l sin θ", size=12, anchor="start")
    f.text(cx, 236, "τ = qE · 2l sin θ = pE sin θ (couple, arm ⟂ E)", size=12)
    return f.svg()


def fig_a3a_triangle():
    """3(a): q, -2q, q at the corners = two dipoles of moment qa at 60 deg; resultant sqrt3 qa."""
    f = Fig(420, 300, "fig_a3a_triangle")
    a = 180
    Tx, Ty = 210, 50
    Lx, Ly = Tx - a / 2, Ty + a * math.sqrt(3) / 2
    Rx, Ry = Tx + a / 2, Ly
    f.path(f"M {Tx} {Ty} L {Lx} {Ly} L {Rx} {Ry} Z", color=GREY, w=1)
    f.circle(Tx, Ty, 13, fill="#d6e2f3", color=BLUE); f.text(Tx, Ty + 5, "−2q", size=11)
    for x in (Lx, Rx):
        f.circle(x, Ly, 11, fill="#f3d6d2", color=RED); f.text(x, Ly + 5, "+q", size=11)
    f.text(Lx - 40, (Ty + Ly) / 2, "a", size=14, italic=True); f.text(Rx + 40, (Ty + Ly) / 2, "a", size=14, italic=True)
    f.text(Tx, Ly + 22, "a", size=14, italic=True)
    # dipole moments (from −q to +q), drawn from the apex
    k = 0.62
    f.arrow(Tx, Ty, Tx + k * (Lx - Tx), Ty + k * (Ly - Ty), color=GREEN, w=2.2)
    f.arrow(Tx, Ty, Tx + k * (Rx - Tx), Ty + k * (Ry - Ty), color=GREEN, w=2.2)
    f.text(Tx + k * (Lx - Tx) - 8, Ty + k * (Ly - Ty) - 6, "p₁ = qa", size=13, anchor="end", color=GREEN)
    f.text(Tx + k * (Rx - Tx) + 8, Ty + k * (Ry - Ty) - 6, "p₂ = qa", size=13, anchor="start", color=GREEN)
    f.arrow(Tx, Ty + 12, Tx, Ty + 120, color=RED, w=2.6)
    f.text(Tx, Ty + 142, "p = √3 qa", size=14, color=RED)
    arc(f, Tx, Ty, 40, ang(Tx, Ty, Lx, Ly), ang(Tx, Ty, Rx, Ry), color="#111")
    f.text(Tx, Ty + 56, "60°", size=12)
    return f.svg()


def fig_a3b_solenoid():
    """Long solenoid: N turns, length l, cross-section A, uniform B = mu0 N I / l inside."""
    f = Fig(440, 190, "fig_a3b_solenoid")
    x0, x1, yc, h = 70, 370, 90, 40
    n = 14
    for k in range(n):
        x = x0 + (x1 - x0) * k / (n - 1)
        f.path(f"M {x} {yc-h} C {x+14} {yc-h}, {x+14} {yc+h}, {x} {yc+h}", color="#8a5a00", w=1.6)
        f.path(f"M {x} {yc+h} C {x-8} {yc+h}, {x-8} {yc-h}, {x+ (x1-x0)/(n-1)} {yc-h}" if k < n - 1 else f"M {x} {yc+h} L {x} {yc+h}",
               color="#d9b98a", w=1, dash="3 3")
    f.line(x0, yc + h, 40, yc + h + 30, color="#8a5a00"); f.line(x1, yc + h, 400, yc + h + 30, color="#8a5a00")
    f.arrow(40, yc + h + 30, 52, yc + h + 18 - 6, color=RED, w=1.6)
    f.text(30, yc + h + 44, "I", size=14, italic=True, color=RED)
    f.arrow(110, yc, 330, yc, color=BLUE, w=2.4)
    f.text(220, yc - h - 12, "B = μ₀ N I / l (inside)", size=13, color=BLUE)
    f.arrow(220, yc + h + 26, x0, yc + h + 26, w=1); f.arrow(220, yc + h + 26, x1, yc + h + 26, w=1)
    f.text(220, yc + h + 22, "l", size=14, italic=True)
    f.text(x1 + 34, yc - 18, "area A", size=12, anchor="start")
    return f.svg()


def fig_a7b_phasor():
    """7(b): phasor diagram, current along the reference; V lags I by 75 deg because X_C > X_L."""
    f = Fig(420, 330, "fig_a7b_phasor")
    ox, oy, k = 80, 80, 2.0
    VR, VL, VC = 20 * k, 31.42 * k, 106.10 * k
    f.arrow(ox, oy, ox + 220, oy, color=GREEN, w=2.4)
    f.text(ox + 226, oy + 5, "I (reference)", size=13, anchor="start", color=GREEN)
    f.arrow(ox, oy, ox + VR, oy, color="#111", w=2.6)
    _st(f, ox + 10, oy - 10, "V", "R", "", size=14)
    f.arrow(ox, oy, ox, oy - VL, color=BLUE, w=2); _st(f, ox - 6, oy - VL + 6, "V", "L", "", size=14, anchor="end", color=BLUE)
    f.arrow(ox, oy, ox, oy + VC, color=ORANGE, w=2); _st(f, ox - 6, oy + VC, "V", "C", "", size=14, anchor="end", color=ORANGE)
    f.line(ox, oy + VC - VL, ox + VR, oy + VC - VL, color=GREY, w=1, dash="4 3")
    f.line(ox + VR, oy, ox + VR, oy + VC - VL, color=GREY, w=1, dash="4 3")
    f.arrow(ox, oy, ox, oy + VC - VL, color="#7d3c98", w=1.6, dash="5 3")
    f.raw(f'<text x="{ox-6}" y="{oy+(VC-VL)/2+30}" text-anchor="end" font-size="13" fill="#7d3c98" font-family="Times New Roman,serif">V<tspan baseline-shift="sub" font-size="9">C</tspan><tspan baseline-shift="0"> − V</tspan><tspan baseline-shift="sub" font-size="9">L</tspan></text>')
    f.arrow(ox, oy, ox + VR, oy + VC - VL, color=RED, w=2.6)
    f.text(ox + VR + 8, oy + VC - VL + 4, "E (applied)", size=13, anchor="start", color=RED)
    arc(f, ox, oy, 46, 0, ang(ox, oy, ox + VR, oy + VC - VL), color=RED)
    f.text(ox + 52, oy + 36, "φ = 75°", size=13, anchor="start", color=RED)
    f.text(210, 318, "Current leads the applied e.m.f. by 75°", size=13)
    return f.svg()


def fig_a9a_spherical():
    """Refraction at a convex spherical surface, O in the rarer medium, real image I.
    Angles are opened out so that they can be labelled (schematic)."""
    f = Fig(480, 300, "fig_a9a_spherical")
    y0 = 230
    Ox, Px, Cx, Ix, R = 40, 200, 300, 430, 100
    phi = math.radians(38)
    Ax, Ay = Cx - R * math.cos(phi), y0 - R * math.sin(phi)
    # denser medium shading right of the surface
    f.path(f"M {Px} {y0} A {R} {R} 0 0 1 {Cx - R*math.cos(math.radians(70)):.1f} {y0 - R*math.sin(math.radians(70)):.1f} "
           f"L 470 {y0 - R*math.sin(math.radians(70)):.1f} L 470 {y0+40} L {Px} {y0+40} Z", color="none", fill="#eaf2fb")
    f.path(f"M {Cx - R*math.cos(math.radians(70)):.1f} {y0 - R*math.sin(math.radians(70)):.1f} A {R} {R} 0 0 0 {Px} {y0} "
           f"A {R} {R} 0 0 0 {Cx - R*math.cos(math.radians(-20)):.1f} {y0 - R*math.sin(math.radians(-20)):.1f}",
           color=BLUE, w=2)
    f.line(20, y0, 470, y0, color=GREY, w=1)
    for x, nm in ((Ox, "O"), (Px, "P"), (Cx, "C"), (Ix, "I")):
        dot(f, x, y0, 3); f.text(x, y0 + 20, nm, size=14)
    # rays
    f.line(Ox, y0, Ax, Ay, color=RED, w=1.8); f.arrow(Ox, y0, (Ox + Ax) / 2, (y0 + Ay) / 2, color=RED, w=1.8)
    f.line(Ax, Ay, Ix, y0, color=RED, w=1.8); f.arrow(Ax, Ay, (Ax + Ix) / 2, (Ay + y0) / 2, color=RED, w=1.8)
    # normal through C and A, extended outward to N
    Nx, Ny = Cx + 1.75 * (Ax - Cx), y0 + 1.75 * (Ay - y0)
    f.line(Cx, y0, Nx, Ny, color="#555", w=1, dash="5 3"); f.text(Nx - 6, Ny - 4, "N", size=13, anchor="end")
    dot(f, Ax, Ay, 3); f.text(Ax + 2, Ay - 10, "A", size=14, anchor="start")
    f.line(Ax, Ay, Ax, y0, color=GREY, w=1, dash="2 3"); f.text(Ax - 4, (Ay + y0) / 2 + 16, "h", size=13, italic=True, anchor="end")
    # angles
    arc(f, Ox, y0, 50, 0, ang(Ox, y0, Ax, Ay)); f.text(Ox + 56, y0 - 6, "α", size=14, italic=True, anchor="start")
    arc(f, Ix, y0, 50, 180, ang(Ix, y0, Ax, Ay)); f.text(Ix - 56, y0 - 6, "β", size=14, italic=True, anchor="end")
    arc(f, Cx, y0, 30, 180, ang(Cx, y0, Ax, Ay)); f.text(Cx - 36, y0 - 6, "γ", size=14, italic=True, anchor="end")
    def mark(r, a1, a2, lab, col):
        arc(f, Ax, Ay, r, a1, a2, color=col)
        d = (a2 - a1 + 540) % 360 - 180; m = math.radians(a1 + d / 2)
        f.text(Ax + (r + 12) * math.cos(m), Ay - (r + 12) * math.sin(m) + 5, lab, size=15, italic=True, color=col)
    mark(30, ang(Ax, Ay, Nx, Ny), ang(Ax, Ay, Ox, y0), "i", RED)        # incident ray and outward normal
    mark(40, ang(Ax, Ay, Cx, y0), ang(Ax, Ay, Ix, y0), "r", GREEN)      # refracted ray and inward normal
    f.text(80, 30, "rarer, μ₁", size=13); f.text(420, 30, "denser, μ₂", size=13)
    f.text(240, 290, "(angles exaggerated for labelling — paraxial rays in the derivation)", size=11)
    return f.svg()


def fig_a10a_lens_mirror():
    """10(a): convex lens f = 10 cm, object 20 cm left; concave mirror f = 5 cm, 30 cm right of lens.
    Scale 8 px = 1 cm.  First image I1 at 20 cm (= C of mirror); mirror image I2 at the same place,
    erect w.r.t. O; light returns through the lens and forms the final image I3 at O, real, inverted."""
    f = Fig(500, 260, "fig_a10a_lens_mirror")
    y, s, h = 130, 8, 20
    L = 200; Ob = L - 20 * s; I1 = L + 20 * s; Mp = L + 30 * s; Fm = Mp - 5 * s
    f.line(20, y, 480, y, color=GREY, w=1)
    lens(f, L, y, 70, bulge=8)
    # concave mirror: arc of radius 10 cm (80 px) about C = I1, facing the lens
    Rm = 10 * s
    f.path(f"M {I1 + math.sqrt(Rm*Rm-45*45):.1f} {y-45} A {Rm} {Rm} 0 0 1 {I1 + math.sqrt(Rm*Rm-45*45):.1f} {y+45}", color="#111", w=2.4)
    for yy in range(y - 40, y + 45, 10):
        xx = I1 + math.sqrt(Rm * Rm - (yy - y) ** 2)
        f.line(xx + 1, yy, xx + 8, yy - 6, color=GREY, w=1)
    for x, nm in ((L - 10 * s, "F₁"), (L + 10 * s, "F₂"), (Fm, "Fₘ")):
        dot(f, x, y, 2.5); f.text(x, y + 18, nm, size=12)
    f.text(L, y + 88, "L (f = 10 cm)", size=12); f.text(Mp + 2, y + 66, "M (f = 5 cm)", size=12)
    # object
    f.arrow(Ob, y, Ob, y - h, w=2.4); f.text(Ob - 6, y - h - 4, "O", size=14, anchor="end")
    # pass 1 (blue): object -> lens -> I1 (inverted)
    f.line(Ob, y - h, L, y - h, color=BLUE, w=1.4); f.line(L, y - h, I1, y + h, color=BLUE, w=1.4)
    f.line(Ob, y - h, I1, y + h, color=BLUE, w=1.4)
    f.arrow(Ob, y - h, (Ob + L) / 2, y - h, color=BLUE, w=1.4)
    # I1 (real, inverted), at the centre of curvature of the mirror
    f.line(I1, y, I1, y + h, color=BLUE, w=2, dash="4 2"); f.text(I1 - 4, y + h + 16, "I₁ (= C)", size=12)
    # pass 2 (red): from I1 tip to the mirror and back to I2
    hx = I1 + math.sqrt(Rm * Rm - h * h)
    f.line(I1, y + h, hx, y + h, color=RED, w=1.4); f.arrow(I1, y + h, (I1 + hx) / 2, y + h, color=RED, w=1.4)
    f.line(hx, y + h, I1, y - h, color=RED, w=1.4)
    f.line(I1, y + h, Mp, y, color=RED, w=1.4); f.line(Mp, y, I1, y - h, color=RED, w=1.4)
    f.arrow(Mp, y, (Mp + I1) / 2, y - h / 2, color=RED, w=1.4)
    f.line(I1, y, I1, y - h, color=RED, w=2, dash="4 2"); f.text(I1 + 4, y - h - 6, "I₂", size=12, anchor="start", color=RED)
    # pass 3 (green): I2 acts as object for the lens (light travelling left)
    f.line(I1, y - h, L, y - h, color=GREEN, w=1.4); f.line(L, y - h, Ob, y + h, color=GREEN, w=1.4)
    f.line(I1, y - h, Ob, y + h, color=GREEN, w=1.4)
    f.arrow(L, y - h, (L + Ob) / 2, y, color=GREEN, w=1.4)
    f.arrow(Ob, y, Ob, y + h, color=GREEN, w=2.4); f.text(Ob + 6, y + h + 16, "I₃ (final)", size=12, anchor="start", color=GREEN)
    f.text(250, 20, "final image at O: real, inverted, same size", size=13)
    return f.svg()


def fig_a12a_bohr():
    """Electron in a Bohr orbit: Coulomb attraction supplies the centripetal force."""
    f = Fig(300, 230, "fig_a12a_bohr")
    cx, cy, r = 130, 115, 80
    f.circle(cx, cy, r, color=GREY, w=1, fill="none")
    f.circle(cx, cy, 10, fill="#f3d6d2", color=RED); f.text(cx, cy + 5, "+e", size=11)
    ex, ey = cx + r, cy
    f.circle(ex, ey, 7, fill="#d6e2f3", color=BLUE); f.text(ex + 12, ey + 18, "−e", size=12, anchor="start")
    f.arrow(ex, ey - 7, ex, ey - 70, color="#111", w=2); f.text(ex + 6, ey - 60, "v", size=15, italic=True, anchor="start")
    f.arrow(ex - 8, ey, ex - 52, ey, color=RED, w=2); f.text(ex - 30, ey - 8, "F", size=14, italic=True, color=RED)
    f.line(cx, cy, cx + r * math.cos(math.radians(225)), cy - r * math.sin(math.radians(225)), color=GREY, w=1)
    f.text(cx - 34, cy + 22, "r", size=14, italic=True)
    f.text(150, 222, "ke²/r² = mv²/r ;  mvr = nh/2π", size=12)
    return f.svg()


def fig_a14a_fwr():
    """14(a): centre-tap full-wave rectifier with two diodes; current through R_L is one-way."""
    f = Fig(540, 380, "fig_a14a_fwr")
    yt, yc, yb = 40, 130, 220
    # primary
    for k in range(6):
        y = 60 + 25 * k
        f.path(f"M 70 {y} A 12.5 12.5 0 0 1 70 {y+25}", color="#111")
    f.line(30, 60, 70, 60); f.line(30, 210, 70, 210)
    acsource(f, 30, 135)
    f.line(30, 60, 30, 124); f.line(30, 146, 30, 210)
    f.line(92, 50, 92, 220, w=1.2); f.line(98, 50, 98, 220, w=1.2)
    # secondary (S1 top, S2 bottom, centre tap T)
    for k in range(8):
        y = yt + 22.5 * k
        f.path(f"M 120 {y} A 11.25 11.25 0 0 0 120 {y+22.5}", color="#111")
    f.text(126, yt - 6, "S₁", size=12, anchor="start"); f.text(126, yb + 18, "S₂", size=12, anchor="start")
    f.line(120, yt, 170, yt); f.line(120, yb, 170, yb)
    _diode(f, 170, yt, 270, yt); _diode(f, 170, yb, 270, yb)
    f.text(220, yt - 16, "D₁", size=13); f.text(220, yb + 26, "D₂", size=13)
    f.line(270, yt, 330, yt); f.line(270, yb, 330, yb); f.line(330, yt, 330, yb)
    dot(f, 330, yc); f.text(338, yc + 5, "X", size=13, anchor="start")
    f.line(120, yc, 150, yc); dot(f, 120, yc); f.text(138, yc - 6, "T", size=13)
    resistor(f, 150, yc, 330, yc, n=6)
    _st(f, 240, yc - 14, "R", "L", size=13)
    f.arrow(300, yc + 16, 180, yc + 16, color=RED, w=1.8)
    f.text(240, yc + 32, "current in load: X → T in both half-cycles", size=11, color=RED)
    f.arrow(240, yt + 12, 300, yt + 12, color=BLUE, w=1.2); f.text(305, yt + 16, "1st half", size=10, anchor="start", color=BLUE)
    f.arrow(240, yb - 12, 300, yb - 12, color=GREEN, w=1.2); f.text(305, yb - 8, "2nd half", size=10, anchor="start", color=GREEN)
    f.text(345, yc - 20, "+", size=14, anchor="start"); f.text(150, yc + 22, "−", size=14)
    # waveforms
    def wave(x0, y0, rect, lab):
        f.arrow(x0, y0, x0 + 190, y0, w=1); f.line(x0, y0 + 40, x0, y0 - 45, w=1)
        pts = []
        for t in range(0, 201):
            v = math.sin(2 * math.pi * 2 * t / 200)
            if rect:
                v = abs(v)
            pts.append((x0 + 180 * t / 200, y0 - 35 * v))
        f.path("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), color=BLUE if not rect else RED, w=1.8)
        f.text(x0 + 95, y0 + 56, lab, size=12)
        f.text(x0 + 188, y0 + 16, "t", size=12, italic=True)
    wave(40, 310, False, "input a.c. across S₁S₂")
    wave(300, 310, True, "output across load (unidirectional)")
    return f.svg()
