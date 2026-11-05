"""Recompute every numerical answer of physics_2014_15 from the question data (paper's constants)."""
import math
h, c, e, me, pi = 6.6e-34, 3e8, 1.6e-19, 9e-31, 3.14
eps0, mu0 = 8.85e-12, 4*math.pi*1e-7
ok = True
def chk(name, got, want, rel=0.01):
    global ok
    g = abs(got - want) <= rel*abs(want) if want else abs(got) < 1e-12
    ok &= g; print(f"{'ok ' if g else 'BAD'} {name}: computed {got:.5g}, printed {want:.5g}")

chk("1A(ii) B'/B (N, R doubled)", (2/2), 1)
chk("1A(v) telescope L", 0.27 + 0.15, 0.42)
a = e*250/me; chk("1B(i) a", a, 4.44e13); chk("1B(i) t", math.sqrt(2*2/a), 3.0e-7)
# 1B(ii): five +q at hexagon vertices, -q at centre: |F| = k q^2 / L^2 (L=1, kq^2=1)
Fx = Fy = 0
for k in range(5):
    t = math.radians(60*k); Fx += math.cos(t); Fy += math.sin(t)   # attraction towards each vertex
chk("1B(ii) |F| in units kq^2/L^2", math.hypot(Fx, Fy), 1)
print("    direction (deg):", round(math.degrees(math.atan2(Fy, Fx))), "(empty vertex at 300 deg -> opposite vertex 120 deg)")
ok &= round(math.degrees(math.atan2(Fy, Fx))) == 120
chk("1B(iii) V", 2*50/(1 + 4), 20)
I = 10/(2 + 0.5); Ib = I/2; chk("1B(iv) I", I, 4); chk("1B(iv) VA-VB", Ib*3 - Ib*1, 4)
chk("1B(v) I", 6*2 + 15, 27)
chk("1B(xiii) E eV (nu = 1e15)", h*1e15/e, 4.125)
chk("1B(xiv) L", 2*h/(2*pi), 2.10e-34)
C = eps0*90e-4/2.5e-3; U = 0.5*C*800**2
chk("2(b) C", C, 3.19e-11); chk("2(b) U", U, 1.02e-5); chk("2(b) U/K", U/3, 3.4e-6); chk("2(b) KU", 3*U, 3.06e-5)
chk("3(a) p/(qa)", math.sqrt(1 + 1 + 2*math.cos(math.radians(60))), math.sqrt(3))
# 4(a) network by nodal analysis: A-C R, C-T, T-B, T-M, C-M, M-B, C-D, D-B (R = 1)
import numpy as np
nodes = ["A", "C", "T", "M", "D", "B"]; idx = {n: i for i, n in enumerate(nodes)}
G = np.zeros((6, 6))
for a_, b_ in (("A","C"),("C","T"),("T","B"),("T","M"),("C","M"),("M","B"),("C","D"),("D","B")):
    i, j = idx[a_], idx[b_]; G[i,i] += 1; G[j,j] += 1; G[i,j] -= 1; G[j,i] -= 1
Gr = G[:5, :5]; Iv = np.zeros(5); Iv[0] = 1          # inject 1 A at A, B grounded
V = np.linalg.solve(Gr, Iv); chk("4(a) R_AB / R", V[0], 5/3)
n = 750/1.5; B = 0.5*4*pi*1e-7*n*10; A = pi*0.02**2
chk("5(b) B_end", B, 3.14e-3); chk("5(b) phi", B*A, 3.94e-6)
emf = 0.15*0.5*2; Ir = emf/3; chk("6(b) emf", emf, 0.15); chk("6(b) I", Ir, 0.05); chk("6(b) F", 0.15*Ir*0.5, 3.75e-3)
XL = 2*math.pi*50*0.1; XC = 1/(2*math.pi*50*30e-6)
chk("7(b) XL", XL, 31.4); chk("7(b) XC", XC, 106.1); chk("7(b) phi deg", math.degrees(math.atan((XC - XL)/20)), 75.0)
chk("7(b) Z", math.hypot(20, XC - XL), 77.3)
chk("8(a) ratio", ((1.5/(4/3)) - 1)/(1.5 - 1), 0.25)
f = 20
for m, want_u in ((-2, -30), (2, -10)):
    u = f*(1 - m)/m          # from 1/(mu) - 1/u = 1/f
    chk(f"9(b) u for m={m}", u, want_u); chk(f"9(b) check m", (1/(1/f + 1/u))/u, m)
v1 = 1/(1/10 - 1/20); chk("10(a) lens v1", v1, 20)
um = -(30 - v1); vm = 1/(1/(-5) - 1/um); chk("10(a) mirror v", vm, -10)
u3 = -(30 - abs(vm)); v3 = 1/(1/10 + 1/u3); chk("10(a) final v (from lens, other side)", v3, 20)
vo = 1/(1/2 - 1/2.4); chk("11(b) vo", vo, 12); chk("11(b) M", vo/2.4*(1 + 25/5), 30)
dm = 2*1.007276 + 2*1.008665 - 4.001506; chk("13(b) dm", dm, 0.030376); chk("13(b) BE", dm*931, 28.3)
cross = lambda a, b: (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
# 1B(vi): wire along +y, P at +x; B of wire at P = I_hat x r_hat = y x x = -z (into page); F = Q v x B, v = +x
Bp = cross((0, 1, 0), (1, 0, 0)); Fq = cross((1, 0, 0), Bp)
print("1B(vi) B at P", Bp, "F", Fq); ok &= Bp == (0, 0, -1) and Fq == (0, 1, 0)
# 6(b): v = +x, B = -z: force on +charge in rod v x B = +y (Q -> P, P at top); F on rod I l x B with l = +y
Fc = cross((1, 0, 0), (0, 0, -1)); Fr = cross((0, 1, 0), (0, 0, -1))
print("6(b) v x B", Fc, "rod force", Fr); ok &= Fc == (0, 1, 0) and Fr == (-1, 0, 0)
# 5(b) (review): end-face field = half the inside field, checked numerically from Biot-Savart on the axis
# B_axis(z) of a finite solenoid (length l, radius r) = mu0 n I/2 (cos a1 - cos a2); at an end of a long one -> 1/2
l, r_ = 1.5, 0.02
end = 0.5*((l)/math.hypot(l, r_) - 0); mid = 0.5*2*(l/2)/math.hypot(l/2, r_)
chk("5(b) B_end/B_mid (Biot-Savart, on axis)", end/mid, 0.5, rel=0.002)
print("ALL OK" if ok else "FAILURES")
