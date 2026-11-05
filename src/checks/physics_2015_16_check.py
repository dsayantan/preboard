"""Recompute every numerical answer in physics_2015_16.py (Heritage pre-board 2015-16, Paper 1)."""
import math, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(HERE, ".."), os.path.join(HERE, "..", "figs")]
e, h, c, me, eps0, k = 1.6e-19, 6.6e-34, 3e8, 9e-31, 8.85e-12, 9e9
ok = []
def chk(name, got, want, rel=6e-3):
    assert abs(got - want) <= rel * abs(want), f"{name}: got {got}, printed {want}"
    ok.append(name)

# 1A(ii) network: c,d dead ends
chk("1A(ii) R_af", 10 + 50 + 80, 140)
chk("1A(iii) real depth", 30 * 4 / 3, 40)
chk("1A(iv) r3/r2", 9 / 4, 2.25)
chk("1B(i) E", 2e-3 / 5e-6, 400)
Cs = 3 * 6 / 9; chk("1B(iii) V3", Cs * 120 / 3, 80)
chk("1B(iv) vd ratio", 1 / 2**2, 0.25)
chk("1B(vi) I6/I9", (1 / 6) / (1 / 9), 1.5)
chk("1B(xiii) r Li++", 53 / 3, 17.7)
chk("1B(xiv) E=mc2", 1e-3 * c**2, 9e13)
# 1B(vii) direction: v = +x (away from wire), I = +y, B at P (to the right of wire) = -z
import numpy as np
I_dir = np.array([0, 1, 0]); r_hat = np.array([1, 0, 0]); B = np.cross(I_dir, r_hat)
assert (B == np.array([0, 0, -1])).all(); F = np.cross(np.array([1, 0, 0]), B)
assert (F == I_dir).all(); ok.append("1B(vii) force parallel to I")
# 2(b)
V = 4e-6 * 400 / 6e-6; chk("2b V", V, 266.7)
loss = 0.5 * 4e-6 * 400**2 - 0.5 * 6e-6 * V**2; chk("2b loss", loss, 0.107)
chk("2b loss formula", 4e-6 * 2e-6 / (2 * 6e-6) * 400**2, 0.107)
# 3(b)
chk("3b dU", k * 1e-10 * (1 / 0.03 - 1 / 0.10), 21)
# 4(b): bridge
AB, BC, DC = 12, 0.5, 1; x = AB / BC * DC - 6; chk("4b x", x, 18)
# brute check with nodal analysis: V_B == V_D for x=18
def nodal(x):
    G = lambda r: 1 / r
    # nodes A(1V), C(0V); unknown B, D
    gAB, gBC, gAD, gDC = G(12), G(0.5), G(x + 6), G(1)
    VB = gAB / (gAB + gBC); VD = gAD / (gAD + gDC); return VB - VD
assert abs(nodal(18)) < 1e-12; ok.append("4b nodal")
chk("5a F", e * 3e7 * 10, 4.8e-11)
chk("6a r_alpha/r_p", 1 / 2, 0.5)
eps = 0.15 * 0.5 * 2; I = eps / 3; chk("6b F", 0.15 * I * 0.5, 3.75e-3)
# 7(b)
XL = 100 * math.tan(math.radians(60)); XC = XL; Z = math.hypot(100, XL - XC)
chk("7b I", 200 / Z, 2); chk("7b P", (200 / Z) ** 2 * 100, 400)
# 8(b)
r = (5 + 3) / (5 - 3)  # (a1+a2)/(a1-a2) = 5/3 -> a1/a2
a1a2 = (5 / 3 + 1) / (5 / 3 - 1); chk("8b a1/a2", a1a2, 4); chk("8b width ratio", a1a2**2, 16)
chk("8b check Imax/Imin", (a1a2 + 1) ** 2 / (a1a2 - 1) ** 2, 25 / 9)
# 9(b)
th = math.degrees(math.asin(6200e-10 / 1.24e-6)); chk("9b 2theta", 2 * th, 60)
# 10(b)
v = 1 / (1 / 10 - 1 / 12); chk("10b v", v, 60); chk("10b f mirror", (v - 10) / 2, 25)
# 11(b)
vo = 1 / (1 / 2 - 1 / 2.4); chk("11b vo", vo, 12); mo = vo / 2.4; me_ = 1 + 25 / 5
chk("11b M", mo * me_, 30); chk("11b ue", 1 / (1 / 5 + 1 / 25), 4.17)
# 12(a)
slope = 8 / ((30 - 10) * 1e14)  # eV per Hz
chk("12a nu0", 10e14, 1e15); chk("12a phi", slope * 10e14, 4); chk("12a h", slope * e, 6.4e-34)
chk("12a Vs", slope * 30e14 - 4, 8)
chk("12b ratio", math.sqrt(1 / 4), 0.5)
# 13(a) Bohr radius value
r1 = eps0 * h**2 / (math.pi * me * e**2); chk("13a r1 (approx 0.53 A with paper constants)", r1, 0.53e-10, rel=0.03)
# 14(b)
dm = 3 * 4.002604 - 12.0; chk("14b dm", dm, 0.007812); chk("14b Q", dm * 931, 7.27)
print(f"{len(ok)} checks passed")
