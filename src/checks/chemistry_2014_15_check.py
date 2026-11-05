"""Recompute every numerical answer in chemistry_2014_15 (theory) and chemistry_2014_15_prac."""
import math
ok = True
def chk(name, got, want, tol=5e-3):
    global ok
    good = abs(got - want) <= tol * max(1, abs(want))
    ok &= good
    print(f"{'ok ' if good else 'BAD'} {name}: computed {got:.6g}, printed {want}")

# 1(a)(ii) [E(en)2(C2O4)]NO2 : x + 0 + (-2) = +1
chk("1(a)(ii) oxidation state", 1 - (-2), 3)
# 1(b)(iii) E(cell) for X = Zn, Y = Ni
E = {"Zn": -0.76, "Ni": -0.23, "Fe": -0.44}
for X, Y in (("Ni", "Zn"), ("Fe", "Zn"), ("Zn", "Ni"), ("Ni", "Fe")):
    print(f"   X={X}, Y={Y}: E = {E[Y]-E[X]:+.2f} V")
chk("1(b)(iii) E for X=Zn,Y=Ni", E["Ni"] - E["Zn"], 0.53)
# 1(c)(i) t1/2 constant: 50 % in 2 h, 75 % in 4 h
k1 = math.log(1/0.5)/2; k2 = math.log(1/0.25)/4
chk("1(c)(i) k from 50%/2h vs 75%/4h equal", k1, k2)

# 2(a) phenol in 1 kg solvent, Kf 14, dTf 7
m = 75.2 / 94
chk("2(a) molality", m, 0.8)
dTc = 14 * m
chk("2(a) dTf calc", dTc, 11.2)
i = 7 / dTc
chk("2(a) i", i, 0.625)
a = 2 * (1 - i)
chk("2(a) alpha (dimerised fraction)", a, 0.75)

# 2(b) mole fraction of cane sugar, molality 0.4445
nw = 1000 / 18
x = 0.4445 / (0.4445 + nw)
chk("2(b) x sugar", x, 0.007937, 1e-3)

# 3(a) first-order ester hydrolysis
t = [0, 75, 119, 193]; V = [9.62, 12.10, 13.10, 14.75]; Vinf = 21.05
ks = []
for ti, Vi in zip(t[1:], V[1:]):
    k = 2.303 / ti * math.log10((Vinf - V[0]) / (Vinf - Vi))
    ks.append(k)
    print(f"   t={ti}: Vinf-Vt={Vinf-Vi:.2f}, k={k:.5f} min^-1")
chk("3(a) k75", ks[0], 3.26e-3, 2e-3)
chk("3(a) k119", ks[1], 3.05e-3, 2e-3)
chk("3(a) k193", ks[2], 3.09e-3, 2e-3)
print("   log10(Vinf-Vt):", [round(math.log10(Vinf - v), 4) for v in V])
# least-squares slope of log(Vinf-Vt) v t
y = [math.log10(Vinf - v) for v in V]
n = 4; sx = sum(t); sy = sum(y); sxx = sum(q*q for q in t); sxy = sum(p*q for p, q in zip(t, y))
slope = (n*sxy - sx*sy)/(n*sxx - sx*sx); icpt = (sy - slope*sx)/n
print(f"   best fit: slope {slope:.6f}, intercept {icpt:.4f}, k = -2.303*slope = {-2.303*slope:.5f}")
chk("3(a) k from slope", -2.303*slope, 3.07e-3, 2e-3)

# 4(c) charge on metal ion
Q = 4 * 45 * 60
chk("4(c) Q", Q, 10800)
z = (Q / 96500) / (2.977 / 106.4)
chk("4(c) z", z, 4.0, 1e-2)

# 4(d) Daniell cell
Ecell = 0.339 + 0.761
chk("4(d) Ecell", Ecell, 1.100)
dG = -2 * 96500 * Ecell
chk("4(d) dG (J)", dG, -212300)

# 7(b) spin-only moment, 1 unpaired e
chk("7(b) mu (BM)", math.sqrt(1 * 3), 1.73)

# ---------------- practical (chemistry_2014_15_prac): KMnO4 / Mohr's salt
Mk = 1.15 / 158
chk("P1(i) M KMnO4", Mk, 0.007278, 1e-4)
titre, Vp = 22.20, 20.0
Mfe = 5 * Mk * titre / Vp
chk("P1(ii) M Mohr's salt", Mfe, 0.04040, 1e-4)
s = Mfe * 392
chk("P1(iii) g/L", s, 15.84, 1e-3)
chk("P1(iv) purity %", s / 17.2 * 100, 92.1, 1e-3)
print("expected titre at 100 % purity (mL):", round((17.2/392) * 20 / (5 * Mk), 2))
# review: unconfirmed practical observations must not be asserted as fact
import os
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "chemistry_2014_15_prac.py")).read()
_good = 'Pink to salmon/orange-red' not in _src and "could not be confirmed" in _src
ok &= _good
print(("ok " if _good else "BAD") + " chemistry_2014_15_prac: unconfirmed observation flagged, not asserted")
print("ALL OK" if ok else "FAILURES")
