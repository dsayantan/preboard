"""Recompute every numerical answer of physics_2013_14 (theory) from the question data."""
import math
h, c, e, me = 6.6e-34, 3e8, 1.6e-19, 9e-31
ok = True
def chk(name, got, want, rel=0.01):
    global ok
    good = abs(got - want) <= rel * abs(want)
    ok &= good
    print(f"{'ok ' if good else 'BAD'} {name}: computed {got:.5g}, printed {want:.5g}")

chk("1A(v) 10 parts in parallel (×R)", (1/10)/10, 0.01)
chk("1B(i) E", 2e-3/5e-6, 400)
chk("1B(iv) Irms", 5*math.sqrt(2)/math.sqrt(2), 5)
chk("1B(v) W0 J", h*5e14, 3.3e-19); chk("1B(v) W0 eV", h*5e14/e, 2.06)
th = math.radians(0.1); chk("1B(x) d (m)", 6e-7/th, 3.44e-4)
vo = 1/(1/1.5 - 1/2); ue = 1/(-1/25 - 1/10)
chk("1B(xiv) v_o", vo, 6); chk("1B(xiv) u_e", ue, -7.14); chk("1B(xiv) L", vo - ue, 13.1)
C = 1/(1/8 + 1/16 + 1/24); chk("2(b) C µF", C, 48/11); chk("2(b) Q µC", C*110, 480)
# 6(c): equiconvex glass lens radius R, water plano-concave lens
R = 2/(3*(1/15)); chk("6(c) R", R, 10)
f1 = 1/((1.5 - 1)*(2/R)); chk("6(c) f1", f1, 10)
chk("6(c) water check F", 1/(1/f1 - (4/3 - 1)/R), 15)
mu = 1 + R*(1/f1 - 1/25); chk("6(c) mu", mu, 1.6)
I = 1
for phi, want in ((math.pi/2, 5), (math.pi, 1)):
    chk(f"7(b) phi={phi:.3f}", I + 4*I + 2*math.sqrt(4)*I*math.cos(phi), want)
chk("8(a) B", 5e4/2e6, 0.025)
# direction: electron, v = +x, E = -y; need total force zero; B = -z (into page)
v = (1, 0, 0); B = (0, 0, -1); vxB = (v[1]*B[2]-v[2]*B[1], v[2]*B[0]-v[0]*B[2], v[0]*B[1]-v[1]*B[0])
FB = tuple(-x for x in vxB); FE = (0, +1, 0)  # -e * (-y) = +y
print("8(a) direction: F_B on electron", FB, "F_E on electron", FE, "-> cancel" if FB[1] == -FE[1] else "-> WRONG")
ok &= FB[1] == -FE[1]
E = h*c/198e-9/e; chk("8(b) photon eV", E, 6.25); chk("8(b) V0", E - 2.5, 3.75)
dE = 13.6*(1 - 1/4); chk("8(c) dE", dE, 10.2); chk("8(c) lambda nm", h*c/(dE*e)*1e9, 121)
chk("9(c) J", 2*me*c**2, 1.62e-13); chk("9(c) MeV", 2*me*c**2/e/1e6, 1.01)
# 1B(vii) (restored in review): Th-234 -> Pa-234 + e(-1) + antineutrino: conserve A and Z
A_ok = 234 == 234 + 0; Z_ok = 90 == 91 + (-1)
print("1B(vii) A, Z conserved:", A_ok, Z_ok); ok &= A_ok and Z_ok
print("ALL OK" if ok else "FAILURES")
