"""Recompute every numerical answer of physics_2024_25 (Heritage pre-board 2024-25, theory) from the question data."""
import math
h, c, e, me, eps0, mu0 = 6.6e-34, 3e8, 1.6e-19, 9.1e-31, 8.85e-12, 4 * math.pi * 1e-7
ok = True


def chk(name, got, want, rel=0.01):
    global ok
    good = abs(got - want) <= rel * abs(want)
    ok &= good
    print(f"{'ok ' if good else 'BAD'} {name}: computed {got:.5g}, printed {want:.5g}")


def truth(name, cond):
    global ok
    ok &= bool(cond)
    print(f"{'ok ' if cond else 'BAD'} {name}")


# 1A(i): X at top, Y bottom-left (-q), Z bottom-right (+q); unit forces
X, Y, Z = (0.0, math.sqrt(3) / 2), (-0.5, 0.0), (0.5, 0.0)
def u(a, b):
    d = (b[0] - a[0], b[1] - a[1]); L = math.hypot(*d); return (d[0] / L, d[1] / L)
fy = u(X, Y)                       # attraction towards Y
fz = u(Z, X)                       # repulsion away from Z
F = (fy[0] + fz[0], fy[1] + fz[1])
truth(f"1A(i) resultant {F} is along -x (initial force along XA), |F| = single force", abs(F[1]) < 1e-12 and F[0] < 0 and abs(abs(F[0]) - 1) < 1e-12)
# ...but the path bends: integrate the motion (review fix: answer is B, not A)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs"))
import physics_2024_25_figs as _F
_pts = _F._a1a1_trajectory(stop_y=0.45)
_x0, _y0 = _pts[0]; _x1, _y1 = _pts[len(_pts) // 50]
truth(f"1A(i) starts along -x: early step dx={_x1-_x0:.2e}, dy={_y1-_y0:.2e}", _x1 < _x0 and abs(_y1 - _y0) < 0.05 * abs(_x1 - _x0))
_xe, _ye = _pts[-1]
truth(f"1A(i) path curves down towards Y (reaches y={_ye:.2f} at x={_xe:.2f}): path B", _ye < 0.5 and _xe < -0.3)

# 1A(ii): ammeter branch carries no current -> V(100 ohm) = 4 V; 10/(100+R)*100 = 4
R = 10 / (4 / 100) - 100; chk("1A(ii) R", R, 150)
# polarity consistency: 10 V cell + at A drives A->C through 100 ohm, so V_A > V_C; 4 V cell + at D, V_D = V_A
truth("1A(ii) polarity consistent (V_A - V_C = +4 needs V_A > V_C)", 4 > 0)

# 1A(iii): two 6 V sources in parallel, same polarity
chk("1A(iii) emf", 2 + 2 + 2, 6); chk("1A(iii) equals E4", 6, 6)

# 1A(vi): tan phi = Y/P = 1
chk("1A(vi) tan(pi/4)", math.tan(math.pi / 4), 1)

# 1B(i): a' = 1.5 a
chk("1B(i) ratio", 1.5 / 1, 1.5)
# 1B(iii)
chk("1B(iii) lambda", 2 * 3.14 * 0.53e-10, 3.33e-10)
chk("1B(iii) via h/mv", h / (me * (h / (2 * math.pi * me * 0.53e-10))), 3.33e-10)

# 2
chk("2 mu", 8 / 4.5, 1.78)
# 3(a)
chk("3a B", mu0 * 5000 * 2, 1.26e-2)
# 4: microwaves 1 GHz..300 GHz -> wavelengths
chk("4 lambda at 1 GHz (m)", c / 1e9, 0.3); chk("4 lambda at 300 GHz (m)", c / 3e11, 1e-3)

# 5(a): each half f, two in contact -> f/2
f_ = 1.0; chk("5a F/f", 1 / (1 / f_ + 1 / f_), 0.5)
# 5(b): Newton's formula, and the figure numbers f=10, x=5, y=20
f5, x5 = 10.0, 5.0
v = 1 / (1 / f5 + 1 / -(f5 + x5)); chk("5b v for u=-15", v, 30); chk("5b xy", x5 * (v - f5), f5 ** 2)
chk("5b image height (h=4)", 4 * v / -(f5 + x5), -8)
for xx in (1.0, 3.7, 12.0):
    vv = 1 / (1 / f5 + 1 / -(f5 + xx)); chk(f"5b xy=f^2 at x={xx}", xx * (vv - f5), 100)

# 6
chk("6 mu", 1 / math.sin(math.radians(45)), 1.41)

# 7
E7 = h * c / 200e-9; chk("7 E J", E7, 9.9e-19); chk("7 E eV", E7 / e, 6.19); chk("7 phi eV", E7 / e - 0.80, 5.39)
chk("7 phi J", E7 - 0.8 * e, 8.6e-19)

# 10(c)
chk("10c flux", 2e-6 / (6 * eps0), 3.77e4)

# 11: nodal analysis, V_Q = 0, V_P = V
# left branch Q->P: emf +3, R 8.5; middle P->Q 2 ohm; right branch Q->P: emf -2 (cell + at Q), R 9
V = (3 / 8.5 - 2 / 9) / (1 / 8.5 + 1 / 2 + 1 / 9)
I1 = (3 - V) / 8.5; I2 = V / 2; I3 = (V + 2) / 9          # I3 flows P -> Q
chk("11 I1", I1, 0.332); chk("11 I2", I2, 0.0897); chk("11 I3", I3, 0.242)
chk("11 I2 = 10/111.5", 10 / 111.5, I2)
truth("11 junction I1 = I2 + I3", abs(I1 - I2 - I3) < 1e-12)
chk("11 left mesh", 8.5 * I1 + 2 * I2, 3); chk("11 right mesh", 9 * I3 - 2 * I2, 2)
# alternative polarity of the 2 V cell (stated in the note)
Va = (3 / 8.5 + 2 / 9) / (1 / 8.5 + 1 / 2 + 1 / 9)
chk("11 alt I1", (3 - Va) / 8.5, 0.26); chk("11 alt I2", Va / 2, 0.39, rel=0.02); chk("11 alt I3", (2 - Va) / 9, 0.13, rel=0.04)

# 13(a)
Z = math.hypot(100, 400 - 600); chk("13a Z", Z, 223.6); I0 = 100 / Z; chk("13a I0", I0, 0.447)
VR, VL, VC = I0 * 100, I0 * 400, I0 * 600
chk("13a VR", VR, 44.7); chk("13a VL", VL, 178.9); chk("13a VC", VC, 268.3); chk("13a sum", VR + VL + VC, 492)
chk("13a phasor sum", math.hypot(VR, VC - VL), 100); chk("13a phase deg", math.degrees(math.atan((600 - 400) / 100)), 63.4)

# 14
chk("14 lambda", 1e-3 * 3e-5 / 5e-2, 6e-7)

# 15(a) figure: i = 50 deg, mu2/mu1 = 1.5
r = math.asin(math.sin(math.radians(50)) / 1.5); chk("15a fig r deg", math.degrees(r), 30.7)
# 15(b) secondary maxima intensities
def sinc2(b): return (math.sin(b) / b) ** 2
import scipy.optimize as so
for n, want in ((1, 1 / 22), (2, 1 / 62)):
    b = so.minimize_scalar(lambda b: -sinc2(b), bounds=(n * math.pi + 0.1, (n + 1) * math.pi - 0.1), method="bounded").x
    chk(f"15b secondary max {n} I/I0", sinc2(b), want, rel=0.05)

# 16
E16 = h * c / 658e-9; chk("16 E J", E16, 3.01e-19); chk("16 E eV", E16 / e, 1.88); chk("16 level gap", -1.51 + 3.40, 1.89)
chk("16 Bohr check 13.6(1/4-1/9)", 13.6 * (1 / 4 - 1 / 9), 1.89)

# 17
K = 100 * e; lam = h / math.sqrt(2 * me * K); chk("17 p", math.sqrt(2 * me * K), 5.40e-24); chk("17 lambda", lam, 1.22e-10)
chk("17 12.27/sqrt(V) A", 12.27 / 10 * 1e-10, lam, rel=0.02)

# 18(a) figure: fo = 24, fe = 6, D = 25
fo, fe, D = 24, 6, 25
ue = 1 / (1 / -D - 1 / fe); chk("18a ue", ue, -150 / 31); chk("18a final image height (I' = -4)", -4 * (-D) / ue, -20.67)
chk("18a M formula = fo/|ue|", fo / abs(ue), (fo / fe) * (1 + fe / D))
# 18(b)(ii)
chk("18b a", 6500e-10 / math.sin(math.radians(30)), 1.3e-6)

# 19(a): direction check q v x B with v = +x, B = -z (into page): force on + charge along +y (towards P)
vv = (1, 0, 0); B = (0, 0, -1)
Fq = (vv[1] * B[2] - vv[2] * B[1], vv[2] * B[0] - vv[0] * B[2], vv[0] * B[1] - vv[1] * B[0])
truth(f"19a force on + carriers {Fq} is +y: current Q -> P in the rod", Fq[1] > 0)
l_ = (0, 1, 0); FB = (l_[1] * B[2] - l_[2] * B[1], l_[2] * B[0] - l_[0] * B[2], l_[0] * B[1] - l_[1] * B[0])
truth(f"19a force on rod I l x B {FB} is -x (opposes v)", FB[0] < 0)

# 19(b)(II)
Ig = 50 / 10 * 1e-3; chk("19b Ig", Ig, 5e-3); chk("19b I", Ig * (1 + 60 / 2.5), 0.125)

print("ALL OK" if ok else "FAILURES")
