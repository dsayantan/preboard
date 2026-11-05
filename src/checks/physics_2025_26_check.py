"""Recompute every numerical answer of physics_2025_26 (theory) from the question data."""
import math
h, c, e, me, eps0, R = 6.6e-34, 3e8, 1.6e-19, 9.1e-31, 8.85e-12, 1.097e7
ok = True
def chk(name, got, want, rel=0.01):
    global ok
    good = abs(got - want) <= rel * abs(want)
    ok &= good
    print(f"{'ok ' if good else 'BAD'} {name}: computed {got:.5g}, printed {want:.5g}")

chk("1A(iii) ammeter R", 480*20/500, 19.2); chk("1A(iii) I", 30/(40.8 + 480*20/500), 0.5)
chk("1A(iv) L mH", 2*3e-2/(8-2)*1e3, 10)
# 1A(v): concave mirror f=-10, real image: u<f -> v negative (3rd quadrant)
for u in (-12, -20, -60):
    v = 1/(1/-10 - 1/u); ok &= v < 0; print("1A(v) u", u, "v", round(v, 2), "(negative)")
chk("1A(v) (2f,2f) on curve", 1/(1/-10 - 1/-20), -20)
chk("1B(ii) h", e*4.12e-15, 6.59e-34)
chk("1B(iv) L", 2*h/(2*math.pi), 2.1e-34)
lam = 1/(R*(1/9 - 1/16)); chk("1B(v) lambda nm", lam*1e9, 1875); ok &= 700e-9 < lam < 1e-3
chk("1B(vi) 2m0c^2 MeV", 2*me*c**2/e/1e6, 1.02)
chk("4(a) t min", 20*(1/4), 5)
chk("6(a) i", (59.5 + 38.5)/2, 49)
chk("7 Balmer/Lyman", (4/R)/(1/R), 4); chk("7 Paschen/Lyman", (9/R)/(1/R), 9)
E = h*c/198e-9; chk("9 E J", E, 1.0e-18); chk("9 E eV", E/e, 6.25); chk("9 p", h/198e-9, 3.33e-27)
C12 = 3*6/9; chk("10 C12", C12, 2); chk("10 CAB", C12 + 10, 12); chk("10 Q1 uC", C12*50, 100)
chk("10 V1+V2", 100/3 + 100/6, 50)
X = 2*60/40; chk("11 X", X, 3); S = 2*X/(X - 2); chk("11 S", S, 6); chk("11 parallel", X*S/(X + S), 2)
emf = 3e-2*1*2; chk("15 emf", emf, 0.06); chk("15 I", emf/6, 0.01)
# 15 direction: v=+x, B=-z ; force on +charge q v x B
v = (1, 0, 0); B = (0, 0, -1)
F = (v[1]*B[2]-v[2]*B[1], v[2]*B[0]-v[0]*B[2], v[0]*B[1]-v[1]*B[0])
print("15 force on + charge in MN:", F, "(+y = towards M, top rail) -> N to M in rod, A to C through R")
ok &= F[1] > 0
d = 5*600e-9*0.80/0.48e-3; chk("16 d m", d, 5e-3); chk("16 beta mm", 600e-9*0.8/d*1e3, 0.096)
# 18(a)II: air -> glass reading (the one the data force): r = 40 - 15 = 25
n = math.sin(math.radians(40))/math.sin(math.radians(25)); chk("18a n", n, 1.521)
chk("18a C deg", math.degrees(math.asin(1/n)), 41.1); ok &= 1.4 < n < 1.9
# rejected glass -> air reading gives an unphysical glass index
n_alt = math.sin(math.radians(55))/math.sin(math.radians(40)); chk("18a rejected n", n_alt, 1.27); ok &= n_alt < 1.4
r_emerge = math.degrees(math.asin(n*math.sin(math.radians(40)))); chk("18a n=1.52 from inside emerges at", r_emerge, 77.9, rel=0.001)
# lens figure: f1=40, f2=60, u=-60
v1 = 1/(1/40 + 1/-60); chk("18a fig v1", v1, 120); vv = 1/(1/60 + 1/v1); chk("18a fig v", vv, 40)
chk("18a fig F", 1/(1/40 + 1/60), 24); chk("18a fig v via F", 1/(1/24 + 1/-60), 40)
chk("18b C fibre", math.degrees(math.asin(1.337/1.4905)), 63.8)
r = e**2/(2*eps0*h*c); chk("19a v1/c", r, 1/137, rel=0.005); chk("19a v1", r*c, 2.19e6)
dm = 2*2.014102 - 4.002604; chk("19b dm", dm, 0.0256); chk("19b Q MeV", dm*931.5, 23.8)
chk("19b Q J", dm*931.5e6*e, 3.8e-12)
chk("19b Q MeV 3sf", round(dm*931.5, 1), 23.8, rel=1e-9)
print("ALL OK" if ok else "FAILURES")
