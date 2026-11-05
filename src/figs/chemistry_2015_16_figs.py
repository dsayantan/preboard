"""Figures for Chemistry pre-board 2015-16 (agent B)."""
import math
from svg import Fig
from chemistry_1517_lib import (INK, ACC, WARM, MUTED, LIG, box_row, chem, F)


# ------------------------------------------------------------------ helpers
def _atom(f, x, y, parts, size=15, color=INK, bg=True):
    if bg:
        f.raw(f'<circle cx="{x}" cy="{y-5}" r="{size*0.8:.1f}" fill="#fff"/>')
    chem(f, x, y, parts, size=size, color=color)


def _curly(f, x1, y1, cx, cy, x2, y2, color=WARM):
    f.path(f"M {x1} {y1} Q {cx} {cy} {x2} {y2}", color=color, w=1.5, arrow=True)


# ------------------------------------------------------------------ Q1(d)(iii)
def fig_pt_cis_trans():
    f = Fig(470, 210, "fig_pt_cis_trans")

    def sq(cx, cy, cl_pos, title):
        pos = {"N": (0, -55), "E": (62, 0), "S": (0, 55), "W": (-62, 0)}
        for k, (dx, dy) in pos.items():
            f.line(cx, cy, cx + dx * 0.72, cy + dy * 0.72, w=1.6)
        _atom(f, cx, cy + 5, [("Pt", "")], 16)
        for k, (dx, dy) in pos.items():
            lab = [("Cl", "")] if k in cl_pos else F("NH3")
            _atom(f, cx + dx, cy + dy + 5, lab, 14, color=(WARM if k in cl_pos else ACC))
        f.text(cx, cy + 92, title, size=14, bold=True)

    sq(115, 85, ("N", "E"), "cis-isomer")
    sq(345, 85, ("N", "S"), "trans-isomer")
    f.line(230, 15, 230, 175, color=MUTED, dash="4 4")
    f.text(235, 202, "square planar [Pt(NH₃)₂Cl₂]: the two Cl adjacent (cis) or opposite (trans)",
           size=11.5, color=MUTED)
    return f.svg()


# ------------------------------------------------------------------ Q5(b)
def fig_co_en2cl2_optical():
    f = Fig(560, 292, "fig_co_en2cl2_optical")

    def octa(cx, cy, s, title):
        # octahedral positions (x multiplied by s so that s=-1 is a true mirror image)
        P = {"U": (0, -78), "D": (0, 78), "L": (-80, 0), "R": (80, 0),
             "Fr": (-40, 34), "Bk": (40, -34)}
        P = {k: (cx + s * dx, cy + dy) for k, (dx, dy) in P.items()}
        for k, (x, y) in P.items():
            if k == "Bk":
                f.line(cx, cy, x, y, color=MUTED, w=1.4, dash="4 3")
            else:
                f.line(cx, cy, x, y, w=2.4 if k == "Fr" else 1.6)
        # ethylenediamine chelate rings, drawn outside the octahedron
        for a, b in (("L", "D"), ("R", "Bk")):
            (x1, y1), (x2, y2) = P[a], P[b]
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            vx, vy = mx - cx, my - cy
            L = math.hypot(vx, vy)
            qx, qy = mx + vx / L * 40, my + vy / L * 40
            f.path(f"M {x1} {y1} Q {qx} {qy} {x2} {y2}", color=ACC, w=2)
            f.text(mx + vx / L * 34, my + vy / L * 34 + 5, "en", size=13, italic=True, color=ACC)
        _atom(f, cx, cy + 5, [("Co", "")], 15)
        for k in ("U", "Fr"):
            _atom(f, P[k][0], P[k][1] + 5, [("Cl", "")], 14, color=WARM)
        for k in ("L", "D", "R", "Bk"):
            _atom(f, P[k][0], P[k][1] + 5, [("N", "")], 14, color=ACC)
        f.text(cx, 262, title, size=13, bold=True)

    octa(140, 125, 1, "cis-isomer I")
    octa(420, 125, -1, "its mirror image II")
    f.line(280, 20, 280, 240, color=MUTED, dash="6 5")
    f.text(280, 14, "mirror", size=12, color=MUTED)
    f.text(280, 286, "cis-[Co(en)\u2082Cl\u2082]\u207a: non-superimposable mirror images (enantiomers)",
           size=12, color=MUTED)
    return f.svg()


# ------------------------------------------------------------------ Q5(c)
def fig_fecn6_vbt():
    f = Fig(470, 300, "fig_fecn6_vbt")
    x0 = 188
    heads = [(x0 + 55, "3d"), (x0 + 140 + 11, "4s"), (x0 + 177 + 33, "4p")]
    for x, h in heads:
        f.text(x, 22, h, size=13, italic=True)

    def row(y, label, d, s, p):
        chem(f, x0 - 14, y + 15, label, size=13, anchor="end")
        box_row(f, x0, y, d)
        box_row(f, x0 + 140, y, s)
        box_row(f, x0 + 177, y, p)

    row(34, [("Fe (Z = 26) [Ar] 3d",""),("6","p"),(" 4s",""),("2","p")], ["ud", "u", "u", "u", "u"], ["ud"], ["", "", ""])
    row(80, [("Fe",""),("3+","p"),("  [Ar] 3d",""),("5","p")], ["u", "u", "u", "u", "u"], [""], ["", "", ""])
    f.text(235, 128, "strong-field CN⁻: the five 3d electrons pair up", size=12, color=MUTED)
    row(140, F("Fe^3+ in [Fe(CN)6]^3−"), ["ud", "ud", "u", "L", "L"], ["L"], ["L", "L", "L"])
    # bracket under the six hybrid orbitals
    xb1, xb2 = x0 + 66, x0 + 177 + 66
    f.path(f"M {xb1} 168 L {xb1} 176 L {xb2} 176 L {xb2} 168", color=LIG, w=1.3)
    chem(f, (xb1 + xb2) / 2, 194, [("d",""),("2","p"),("sp",""),("3","p"),(" hybridisation (inner orbital)","")], size=13, color=LIG)
    f.text(235, 220, "x x = electron pair donated by each CN⁻ ligand", size=12, color=LIG)
    f.text(235, 248, "Octahedral; 1 unpaired electron → paramagnetic", size=13, bold=True)
    f.text(235, 270, "μ = √[n(n+2)] = √3 = 1.73 BM (low-spin, inner-orbital)", size=12.5)
    return f.svg()


# ------------------------------------------------------------------ Q3(c)
def fig_azeotropes():
    f = Fig(700, 330, "fig_azeotropes")

    def panel(x0, title, maxbp, ex1, ex2):
        W, H, y0 = 230, 180, 230
        f.arrow(x0, y0, x0 + W + 14, y0)
        f.arrow(x0, y0, x0, y0 - H - 14)
        f.line(x0 + W, y0, x0 + W, y0 - H + 10, color=MUTED, w=1)
        f.text(x0 + W / 2, y0 + 34, "mole fraction of B \u2192", size=12)
        f.text(x0 - 4, y0 + 16, "0", size=11); f.text(x0 + W, y0 + 16, "1", size=11)
        f.text(x0 + 6, y0 - H - 8, "boiling point", size=12, anchor="start")
        f.text(x0 + W / 2, 18, title, size=13, bold=True)
        TA, TB, xa = 110, 70, 0.6
        Taz = 35 if not maxbp else 160
        X = lambda u: x0 + u * W
        Y = lambda h: y0 - h
        hl = lambda u: 2 * u - u * u            # rises fast, flat at u = 1
        hv = lambda u: u * u * (3 - 2 * u)      # rises slowly, flat at u = 1
        def curve(fast):
            pts = []
            for k in range(0, 61):
                x = k / 60
                if x <= xa:
                    u, T0 = x / xa, TA
                else:
                    u, T0 = (1 - x) / (1 - xa), TB
                h = hl(u) if fast else hv(u)
                pts.append(f"{X(x):.1f} {Y(T0 + (Taz - T0) * h):.1f}")
            return "M " + " L ".join(pts)
        # the vapour (dew) curve always lies above the liquid (bubble) curve
        liq, vap = (curve(True), curve(False)) if not maxbp else (curve(False), curve(True))
        f.path(liq, color=ACC, w=2)
        f.path(vap, color=WARM, w=2, dash="6 4")
        f.circle(X(xa), Y(Taz), 3.5, fill=INK)
        f.line(X(xa), Y(Taz), X(xa), y0, color=MUTED, w=1, dash="3 3")
        f.text(X(xa), y0 + 16, "azeotrope", size=11)
        f.text(X(xa), Y(Taz) + (22 if not maxbp else -10),
               "minimum b.p." if not maxbp else "maximum b.p.", size=11, bold=True)
        f.text(X(0) - 6, Y(TA) + 4, "A", size=12, anchor="end", italic=True)
        f.text(X(1) + 6, Y(TB) + 4, "B", size=12, anchor="start", italic=True)
        f.text(x0 + W / 2, 296, ex1, size=11.5, color=MUTED)
        f.text(x0 + W / 2, 314, ex2, size=11.5, color=MUTED)

    panel(50, "Minimum-boiling azeotrope", False,
          "+ve deviation from Raoult's law", "e.g. ethanol (95.6%) + water, 351 K")
    panel(420, "Maximum-boiling azeotrope", True,
          "\u2212ve deviation from Raoult's law", "e.g. HNO₃ (68%) + water, 393.5 K")
    f.line(326, 100, 356, 100, color=ACC, w=2); f.text(341, 116, "liquid", size=11)
    f.line(326, 136, 356, 136, color=WARM, w=2, dash="6 4"); f.text(341, 152, "vapour", size=11)
    return f.svg()


# ------------------------------------------------------------------ Q4(b)
def fig_ag_conc_cell():
    f = Fig(560, 290, "fig_ag_conc_cell")
    # beakers
    for bx, conc, sign, role in ((70, "0.001 M", "−", "anode"), (350, "0.1 M", "+", "cathode")):
        f.path(f"M {bx} 130 L {bx} 260 L {bx+140} 260 L {bx+140} 130", w=2)
        f.rect(bx + 2, 160, 136, 98, color="none", fill="#e6f1f7")
        f.rect(bx + 60, 100, 18, 140, fill="#c0c0c0", color=INK, w=1.3)   # Ag rod
        f.text(bx + 84, 118, "Ag", size=12, bold=True, anchor="start")
        chem(f, bx + 112, 205, F("AgNO3"), size=12)
        f.text(bx + 112, 222, conc, size=12)
        f.text(bx + (52 if sign == "\u2212" else 86), 74, f"{sign}  {role}", size=13, bold=True,
               color=WARM, anchor=("end" if sign == "\u2212" else "start"))
    # salt bridge
    f.path("M 180 185 L 180 115 L 380 115 L 380 185", w=12, color="#d9d2b0")
    f.text(280, 108, "salt bridge (KNO₃ in agar)", size=11.5)
    # external circuit
    f.line(139, 100, 139, 40); f.line(139, 40, 250, 40)
    f.line(310, 40, 419, 40); f.line(419, 40, 419, 100)
    f.circle(280, 40, 20, fill="#fff"); f.text(280, 46, "V", size=15, bold=True)
    f.arrow(170, 26, 240, 26, color=LIG, w=2)
    f.arrow(320, 26, 390, 26, color=LIG, w=2)
    f.text(280, 15, "e⁻ flow in the external wire: dilute side → concentrated side",
           size=11.5, color=LIG)
    f.text(140, 282, "Ag → Ag⁺ + e⁻  (oxidation)", size=11.5)
    f.text(420, 282, "Ag⁺ + e⁻ → Ag  (reduction)", size=11.5)
    return f.svg()


# ------------------------------------------------------------------ Q9(c)(i)
def fig_ester_mech():
    f = Fig(660, 470, "fig_ester_mech")

    def acid_c(cx, cy, top, right, left="CH3", topdouble=False, bottom=None, charge_c=False,
               top_col=INK, right_col=INK):
        """Draw left–C–right with a group above (and optionally below) the carbon."""
        chem(f, cx - 14, cy + 5, F(left), 14, anchor="end")
        f.line(cx - 13, cy, cx - 7, cy)
        chem(f, cx, cy + 5, [("C", "")] + ([("+", "p")] if charge_c else []), 14)
        f.line(cx + 8, cy, cx + 15, cy)
        chem(f, cx + 16, cy + 5, right if isinstance(right, list) else F(right), 14, anchor="start",
             color=right_col)
        if topdouble:
            f.line(cx - 3, cy - 10, cx - 3, cy - 28); f.line(cx + 3, cy - 10, cx + 3, cy - 28)
        else:
            f.line(cx, cy - 10, cx, cy - 28)
        chem(f, cx, cy - 32, top if isinstance(top, list) else F(top), 14, color=top_col)
        if bottom:
            f.line(cx, cy + 9, cx, cy + 26)
            chem(f, cx, cy + 42, bottom if isinstance(bottom, list) else F(bottom), 14)

    f.text(10, 20, "Step 1 — protonation of the carbonyl oxygen (makes C more electrophilic)",
           size=12, anchor="start", bold=True)
    acid_c(80, 80, "O", "OH", topdouble=True)
    _curly(f, 74, 40, 110, 22, 140, 52)
    f.text(160, 70, "+  H", size=14); f.text(178, 63, "+", size=10)
    f.text(225, 82, "⇌", size=22)
    acid_c(320, 80, "OH", "OH", charge_c=True)
    f.text(395, 83, "+", size=14)
    chem(f, 450, 85, F("C2H5–O–H"), 14)
    _curly(f, 437, 70, 390, 40, 330, 72)
    f.text(560, 70, "ethanol attacks C⁺", size=11.5, color=WARM)
    f.text(560, 86, "with its lone pair", size=11.5, color=WARM)

    f.text(10, 140, "Steps 2–4 — ethanol adds (tetrahedral intermediate); a proton moves to an OH, which leaves as water",
           size=12, anchor="start", bold=True)
    acid_c(90, 200, "OH", [("O", ""), ("+", "p"), ("(H)C", ""), ("2", "b"), ("H", ""), ("5", "b")],
           bottom="OH")
    f.text(260, 202, "⇌", size=22)
    acid_c(350, 200, "OH", "OC2H5", bottom=[("O", ""), ("H", ""), ("2", "b"), ("+", "p")])
    # loss of water: C–O bond to O, and top O lone pair into C=O
    _curly(f, 354, 213, 376, 222, 349, 228)
    _curly(f, 343, 160, 312, 172, 346, 182)
    f.text(470, 196, "curly arrows: the C–OH₂⁺ bond breaks,", size=11.5, color=WARM, anchor="start")
    f.text(470, 212, "the OH lone pair forms C=O", size=11.5, color=WARM, anchor="start")

    f.text(10, 290, "Step 5 — loss of H⁺ gives the ester and regenerates the catalyst",
           size=12, anchor="start", bold=True)
    acid_c(90, 350, [("O", ""), ("+", "p"), ("–H", "")], "OC2H5", topdouble=True)
    f.text(200, 353, "+  H₂O", size=14, anchor="start")
    f.text(290, 352, "⇌", size=22)
    acid_c(380, 350, "O", "OC2H5", topdouble=True, right_col=ACC)
    f.text(470, 353, "+  H⁺", size=14, anchor="start")
    f.text(380, 390, "ethyl acetate", size=12, bold=True)
    f.text(330, 425, "The –OC₂H₅ group of the ester (green), oxygen included, comes from the alcohol; the OH lost",
           size=11.5, color=MUTED)
    f.text(330, 442, "as water comes from the acid — proved with ¹⁸O-labelled ethanol (acyl–oxygen fission).",
           size=11.5, color=MUTED)
    return f.svg()


# ------------------------------------------------------------------ Q10(c)(iii)
def _fischer_glucose(f, x, y0, title=True):
    rows = [("CHO", None), ("H", "R"), ("HO", "L"), ("H", "R"), ("H", "R"), ("CH2OH", None)]
    for k, (lab, side) in enumerate(rows):
        y = y0 + k * 34
        if side is None:
            chem(f, x, y + 5, F(lab), 15)
        else:
            f.line(x - 30, y, x - 9, y); f.line(x + 9, y, x + 30, y)
            chem(f, x, y + 5, [("C", "")], 15)
            if side == "R":
                chem(f, x - 34, y + 5, [("H", "")], 14, anchor="end")
                chem(f, x + 34, y + 5, [("OH", "")], 14, anchor="start")
            else:
                chem(f, x - 34, y + 5, [("HO", "")], 14, anchor="end")
                chem(f, x + 34, y + 5, [("H", "")], 14, anchor="start")
        f.text(x - 88, y + 5, f"{k+1}", size=11, color=MUTED)
        if k < 5:
            f.line(x, y + 9, x, y + 25)


def _haworth(f, cx, cy, alpha):
    C4, C5, O, C1, C2, C3 = ((cx - 72, cy), (cx - 32, cy - 30), (cx + 32, cy - 30),
                             (cx + 72, cy), (cx + 40, cy + 30), (cx - 40, cy + 30))
    # back edges thin, front edges heavy
    f.path(f"M {C4[0]} {C4[1]} L {C5[0]} {C5[1]} L {O[0]-10} {O[1]}", w=1.4)
    f.path(f"M {O[0]+9} {O[1]+5} L {C1[0]} {C1[1]}", w=1.4)
    f.path(f"M {C1[0]} {C1[1]} L {C2[0]} {C2[1]} L {C3[0]} {C3[1]} L {C4[0]} {C4[1]}", w=4.5)
    chem(f, O[0], O[1] + 5, [("O", "")], 15)

    def sub(p, d, lab, col=INK, dx=0):
        f.line(p[0], p[1], p[0], p[1] + d)
        chem(f, p[0] + dx, p[1] + d + ((-9 if lab == "CH2OH" else -4) if d < 0 else 14), F(lab), 13, color=col)

    sub(C5, -34, "CH2OH"); sub(C5, 14, "H", dx=10)
    sub(C4, -28, "H"); sub(C4, 28, "OH")
    sub(C3, -20, "OH"); sub(C3, 28, "H")
    sub(C2, -20, "H"); sub(C2, 28, "OH")
    if alpha:
        sub(C1, -28, "H"); sub(C1, 28, "OH", ACC)
    else:
        sub(C1, -28, "OH", ACC); sub(C1, 28, "H")
    for p, n, dx, dy in ((C1, "1", 10, -6), (C2, "2", 10, 14), (C3, "3", -12, 14),
                         (C4, "4", -12, -6), (C5, "5", -12, -6)):
        f.text(p[0] + dx, p[1] + dy, n, size=10, color=MUTED)


def fig_glucose_structures():
    f = Fig(680, 350, "fig_glucose_structures")
    f.text(110, 22, "Open chain (Fischer)", size=13, bold=True)
    _fischer_glucose(f, 110, 52)
    f.text(110, 262, "D-(+)-glucose", size=13)
    f.text(110, 280, "OH on C5 to the right → D", size=11, color=MUTED)
    f.line(225, 20, 225, 330, color=MUTED, dash="4 4")
    f.text(450, 22, "Pyranose (ring) forms — Haworth projection", size=13, bold=True)
    _haworth(f, 335, 145, True)
    _haworth(f, 565, 145, False)
    f.text(335, 252, "α-D-glucopyranose", size=13, bold=True)
    f.text(565, 252, "β-D-glucopyranose", size=13, bold=True)
    f.text(450, 284, "The C5–OH adds to the C1=O group: a six-membered ring containing one O.", size=11.5, color=MUTED)
    f.text(450, 302, "Right-hand groups of the Fischer projection point down in the ring;", size=11.5, color=MUTED)
    f.text(450, 320, "α and β (anomers) differ only at C1 (OH down / up).", size=11.5, color=MUTED)
    return f.svg()
