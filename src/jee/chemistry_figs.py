"""New figures for the JEE Main mock tests, Chemistry (src/jee/chemistry_t{1,2,3}.py).

Each fig_jc_* returns an SVG string.  Ids are prefixed by the function name (svg.Fig uid).
Existing figures from the pre-board papers are imported by the test modules directly.
"""
import math
from svg import Fig
from chemistry_1517_lib import chem, F, INK, ACC, WARM, MUTED

RED = "#b03a2e"


def _hex(f, cx, cy, r, doubles=(), w=1.6):
    """Benzene-type ring, pointy top.  Vertex k at angle -90+60k (v0 top, v1 upper right,
    v2 lower right, v3 bottom, v4 lower left, v5 upper left).  `doubles` lists the ring
    bonds (k, k+1) drawn double (inner line).  Returns the vertex list."""
    V = [(cx + r * math.cos(math.radians(-90 + 60 * k)), cy + r * math.sin(math.radians(-90 + 60 * k)))
         for k in range(6)]
    for k in range(6):
        (x1, y1), (x2, y2) = V[k], V[(k + 1) % 6]
        f.line(round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1), color=INK, w=w)
        if k in doubles:
            # inner line, shortened, pulled 18% toward the centre
            s = 0.18
            ax, ay = x1 + (cx - x1) * s, y1 + (cy - y1) * s
            bx, by = x2 + (cx - x2) * s, y2 + (cy - y2) * s
            t = 0.12
            ax, ay, bx, by = ax + (bx - ax) * t, ay + (by - ay) * t, bx - (bx - ax) * t, by - (by - ay) * t
            f.line(round(ax, 1), round(ay, 1), round(bx, 1), round(by, 1), color=INK, w=w)
    return V


def _dbl(f, x1, y1, x2, y2, gap=3.0, color=INK, w=1.5):
    """A double bond drawn as two parallel lines."""
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy)
    nx, ny = -dy / L * gap / 2, dx / L * gap / 2
    f.line(round(x1 + nx, 1), round(y1 + ny, 1), round(x2 + nx, 1), round(y2 + ny, 1), color=color, w=w)
    f.line(round(x1 - nx, 1), round(y1 - ny, 1), round(x2 - nx, 1), round(y2 - ny, 1), color=color, w=w)


# ---------------------------------------------------------------- 1. SN1 of tert-butyl bromide
def fig_jc_sn1_tbubr():
    f = Fig(640, 230, "fig_jc_sn1_tbubr")

    def tbu(cx, cy, right=None, plus=False):
        # central C with three CH3 (up, lower-left, upper-left) and a group to the right
        f.line(cx, cy - 10, cx, cy - 40, w=1.4)
        chem(f, cx, cy - 46, F("CH3"), size=14)
        f.line(cx - 8, cy + 6, cx - 34, cy + 26, w=1.4)
        chem(f, cx - 44, cy + 40, F("H3C"), size=14)
        f.line(cx - 10, cy - 6, cx - 38, cy - 18, w=1.4)
        chem(f, cx - 58, cy - 18, F("H3C"), size=14)
        chem(f, cx, cy + 5, [("C", "")], size=16)
        if plus:
            f.text(cx + 12, cy - 6, "+", size=16, color=RED, bold=True)
        if right:
            f.line(cx + 9, cy, cx + 40, cy, w=1.4)
            chem(f, cx + 56, cy + 5, F(right), size=15)

    # step 1
    f.text(20, 22, "Step 1 (slow, rate-determining): ionisation", size=13, anchor="start", bold=True)
    tbu(90, 90, right="Br")
    # curved arrow: from the C-Br bond to Br
    f.path("M 115 86 Q 128 62 146 80", color=RED, w=1.4, arrow=True)
    f.arrow(185, 88, 245, 88, color=INK)
    f.text(215, 80, "slow", size=12, color=MUTED)
    tbu(320, 90, plus=True)
    f.text(395, 95, "+", size=16)
    chem(f, 425, 95, [("Br", ""), ("−", "p")], size=15)
    f.text(470, 70, "planar 3° carbocation", size=12, anchor="start", color=ACC)
    f.text(470, 88, "(sp², stabilised by +I and", size=12, anchor="start", color=ACC)
    f.text(470, 104, "hyperconjugation of 9 C–H)", size=12, anchor="start", color=ACC)

    # step 2
    f.text(20, 160, "Step 2 (fast): attack by the nucleophile on either face", size=13, anchor="start", bold=True)
    chem(f, 70, 205, [("(CH", ""), ("3", "b"), (")", ""), ("3", "b"), ("C", ""), ("+", "p")], size=15)
    f.text(130, 205, "+", size=15)
    chem(f, 165, 205, [("OH", ""), ("−", "p")], size=15)
    f.arrow(200, 200, 260, 200)
    f.text(230, 192, "fast", size=12, color=MUTED)
    chem(f, 320, 205, [("(CH", ""), ("3", "b"), (")", ""), ("3", "b"), ("C–OH", "")], size=15)
    f.text(400, 205, "rate = k[(CH₃)₃CBr]", size=13, anchor="start", color=WARM)
    return f.svg()


# ---------------------------------------------------------------- 2. p-nitrophenoxide resonance
def fig_jc_p_nitrophenoxide():
    f = Fig(560, 270, "fig_jc_p_nitrophenoxide")
    r = 38

    def nitro(N, single_both):
        nx, ny = N
        chem(f, nx, ny + 5, [("N", "")], size=15)
        f.text(nx + 11, ny - 6, "+", size=13, color=RED, bold=True)
        # O lower-left and O lower-right
        lo, ro = (nx - 30, ny + 34), (nx + 30, ny + 34)
        if single_both:
            f.line(nx - 6, ny + 8, lo[0] + 6, lo[1] - 12, w=1.4)
        else:
            _dbl(f, nx - 6, ny + 8, lo[0] + 6, lo[1] - 12)
        f.line(nx + 6, ny + 8, ro[0] - 6, ro[1] - 12, w=1.4)
        chem(f, lo[0], lo[1] + 4, [("O", "")] + ([("−", "p")] if single_both else []), size=15)
        chem(f, ro[0], ro[1] + 4, [("O", ""), ("−", "p")], size=15)

    # left: aromatic phenoxide, charge on phenolic O
    cx, cy = 130, 120
    V = _hex(f, cx, cy, r, doubles=(0, 2, 4))
    f.line(V[0][0], V[0][1], V[0][0], V[0][1] - 26, w=1.4)
    chem(f, V[0][0], V[0][1] - 32, [("O", ""), ("−", "p")], size=15)
    f.line(V[3][0], V[3][1], V[3][0], V[3][1] + 22, w=1.4)
    nitro((V[3][0], V[3][1] + 32), single_both=False)
    # arrows pushing the O lone pair into the ring (for the reader)
    f.path(f"M {V[0][0]-8} {V[0][1]-30} Q {V[0][0]-30} {V[0][1]-20} {V[0][0]-6} {V[0][1]-6}",
           color=RED, w=1.2, arrow=True)

    # resonance arrow
    f.arrow(205, 120, 265, 120)
    f.arrow(265, 120, 205, 120)

    # right: quinonoid form, charge on the nitro oxygen
    cx2 = 370
    V2 = _hex(f, cx2, cy, r, doubles=(1, 4))
    _dbl(f, V2[0][0], V2[0][1], V2[0][0], V2[0][1] - 24)
    chem(f, V2[0][0], V2[0][1] - 32, [("O", "")], size=15)
    _dbl(f, V2[3][0], V2[3][1], V2[3][0], V2[3][1] + 20)
    nitro((V2[3][0], V2[3][1] + 32), single_both=True)

    f.text(130, 258, "phenoxide (charge on O of ring)", size=12, color=MUTED)
    f.text(370, 258, "quinonoid form (charge on O of –NO₂)", size=12, color=MUTED)
    f.text(470, 70, "–R of p-NO₂", size=13, color=ACC, anchor="start")
    f.text(470, 88, "spreads the", size=13, color=ACC, anchor="start")
    f.text(470, 106, "negative charge", size=13, color=ACC, anchor="start")
    return f.svg()


# ---------------------------------------------------------------- 3. cleavage of methyl tert-butyl ether by HI
def fig_jc_mtbe_hi():
    f = Fig(660, 200, "fig_jc_mtbe_hi")
    # protonated ether: H3C-O(+)(H)-C(CH3)3
    chem(f, 40, 85, F("H3C"), size=15)
    f.line(62, 80, 92, 80, w=1.4)
    chem(f, 102, 85, [("O", "")], size=16)
    f.text(90, 70, "+", size=14, color=RED, bold=True)
    f.line(102, 90, 102, 112, w=1.4)
    chem(f, 102, 128, [("H", "")], size=15)
    f.line(112, 80, 145, 80, w=1.4)
    chem(f, 152, 85, [("C", "")], size=16)
    f.line(152, 70, 152, 48, w=1.4); chem(f, 152, 42, F("CH3"), size=14)
    f.line(152, 92, 152, 112, w=1.4); chem(f, 152, 128, F("CH3"), size=14)
    f.line(162, 80, 190, 80, w=1.4); chem(f, 210, 85, F("CH3"), size=14)
    # curved arrow: C-O bond electrons go to O
    f.path("M 130 76 Q 120 52 106 68", color=RED, w=1.3, arrow=True)
    f.text(40, 25, "protonated ether (from CH₃–O–C(CH₃)₃ + H⁺)", size=12, anchor="start", color=MUTED)

    f.arrow(240, 80, 300, 80)
    f.text(270, 72, "slow, Sₙ1", size=12, color=MUTED)

    chem(f, 345, 85, F("CH3OH"), size=15)
    f.text(390, 85, "+", size=15)
    chem(f, 450, 85, [("(CH", ""), ("3", "b"), (")", ""), ("3", "b"), ("C", ""), ("+", "p")], size=15)
    f.text(450, 112, "stable 3° carbocation", size=12, color=ACC)

    f.arrow(505, 80, 560, 80)
    chem(f, 533, 70, [("I", ""), ("−", "p")], size=14)
    chem(f, 610, 85, [("(CH", ""), ("3", "b"), (")", ""), ("3", "b"), ("C–I", "")], size=15)

    f.text(330, 170, "Products: CH₃OH + (CH₃)₃C–I   (the halide goes to the 3° carbon)",
           size=13, color=WARM)
    return f.svg()


# ---------------------------------------------------------------- 4. salicylate: intramolecular H-bond
def fig_jc_salicylate():
    f = Fig(420, 250, "fig_jc_salicylate")
    cx, cy, r = 170, 150, 40
    V = _hex(f, cx, cy, r, doubles=(1, 3, 5))
    # carboxylate on v0
    C = (V[0][0], V[0][1] - 32)
    f.line(V[0][0], V[0][1], C[0], C[1] + 2, w=1.4)
    O1, O2 = (C[0] - 32, C[1] - 22), (C[0] + 32, C[1] - 22)
    _dbl(f, C[0] - 3, C[1] - 2, O1[0] + 6, O1[1] + 4)
    f.line(C[0] + 3, C[1] - 2, O2[0] - 6, O2[1] + 4, w=1.4)
    chem(f, O1[0] - 4, O1[1], [("O", "")], size=15)
    chem(f, O2[0] + 4, O2[1], [("O", ""), ("−", "p")], size=15)
    # phenolic OH on v1, pointing outward then H toward O2
    ang = math.radians(-30)
    Op = (V[1][0] + 30 * math.cos(ang), V[1][1] + 30 * math.sin(ang))
    f.line(round(V[1][0], 1), round(V[1][1], 1), round(Op[0] - 6, 1), round(Op[1] + 4, 1), w=1.4)
    chem(f, Op[0] + 2, Op[1] + 5, [("O", "")], size=15)
    H = (Op[0] + 2, Op[1] - 30)
    f.line(round(Op[0] + 2, 1), round(Op[1] - 8, 1), round(H[0], 1), round(H[1] + 6, 1), w=1.4)
    chem(f, H[0], H[1], [("H", "")], size=15)
    f.line(round(H[0] - 8, 1), round(H[1] - 6, 1), O2[0] + 16, O2[1] - 4, color=RED, w=1.4, dash="4 3")
    f.text(290, 60, "intramolecular H-bond", size=12, color=RED, anchor="start")
    f.text(290, 76, "(six-membered ring)", size=12, color=RED, anchor="start")
    f.text(210, 238, "o-hydroxybenzoate ion: the extra stabilisation of the anion", size=12, color=MUTED)
    return f.svg()


# ---------------------------------------------------------------- 5. invert sugar: rotation bar
def fig_jc_invert_rotation():
    f = Fig(600, 170, "fig_jc_invert_rotation")
    x0, x1, y = 40, 480, 90
    lo, hi = -100, 80

    def X(v):
        return x0 + (v - lo) / (hi - lo) * (x1 - x0)

    f.line(x0, y, x1, y, w=1.4)
    for v in range(-100, 81, 20):
        f.line(X(v), y - 5, X(v), y + 5, w=1)
        f.text(X(v), y + 22, f"{v}°" if v else "0", size=11, color=MUTED)
    for v, lab, col, dy, anc, dx in ((66.5, "sucrose +66.5\u00b0", INK, -36, "start", 6),
                                     (52.5, "glucose +52.5\u00b0", ACC, -36, "end", -6),
                                     (-92.4, "fructose \u221292.4\u00b0", WARM, -36, "start", 6),
                                     (-19.95, "invert sugar \u221219.95\u00b0", RED, -36, "middle", 0)):
        f.line(X(v), y, X(v), y + dy, color=col, w=1.6)
        f.circle(X(v), y, 4, color=col, fill=col)
        f.text(X(v) + dx, y + dy - 4, lab, size=12, color=col, anchor=anc)
    f.text(260, 160, "specific rotation [α]D: equimolar mixture = (52.5 − 92.4)/2", size=12, color=MUTED)
    return f.svg()


# ---------------------------------------------------------------- 6. acetophenone: iodoform and oxidation
def fig_jc_acetophenone_tests():
    """T1 Q15: acetophenone -> CHI3 + benzoate (iodoform); -> benzoic acid C7H6O2 (vigorous oxidation).
    Reuses the ring helpers of chemistry_2024_25_figs; drops that paper's lettering (A-D) and ethyne step."""
    from chemistry_2024_25_figs import mol, T
    f = Fig(600, 250, "fig_jc_acetophenone_tests")
    mol(f, 70, 130, {0: "COCH3"}, None)
    T(f, 70, 190, "acetophenone, C8H8O", size=11, color=MUTED)
    f.arrow(115, 115, 255, 75)
    T(f, 180, 80, "I2 / NaOH", size=12)
    mol(f, 320, 75, {0: "COO^− Na^+"}, None)
    f.text(372, 81, "+", size=18)
    T(f, 420, 81, "CHI3", size=16)
    f.text(420, 101, "yellow ppt (iodoform)", size=11, color=MUTED)
    f.arrow(115, 145, 255, 195)
    T(f, 175, 192, "KMnO4 / H^+, heat", size=11)
    mol(f, 320, 205, {0: "COOH"}, None)
    T(f, 420, 210, "benzoic acid, C7H6O2", size=12, color=MUTED)
    return f.svg()
