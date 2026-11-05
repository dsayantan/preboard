"""Checks for Chemistry pre-board 2015-16: every numerical answer recomputed, every equation balanced."""
import sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.join(HERE, ".."), os.path.join(HERE, "..", "data"), os.path.join(HERE, "..", "figs")]
import chemistry_2015_16 as M
from chem_balance_1517 import check_module

F, fails = 96500, []
def close(name, got, want, rel=0.01):
    ok = abs(got - want) <= rel * abs(want)
    print(f"{'ok ' if ok else 'BAD'} {name}: computed {got:.6g}, printed {want}")
    if not ok: fails.append(name)

# 1(c)(v) kappa = G*/R
close("1(c)(v) kappa S/cm", 0.5 / 384, 1.30e-3)
# 1(d)(i) Ba2+ + 2e-
close("1(d)(i) mol Ba", 96500 / (2 * F), 0.5)
# 2(a)(i) normality
eq = 9.65 / F; close("2(a)(i) g-eq", eq, 1.0e-4); close("2(a)(i) N", eq / 0.100, 1.0e-3)
close("2(a)(i) M", eq / 3 / 0.100, 3.33e-4)
# 2(b) charge on cation
Q = 4 * 45 * 60; ne = Q / F; nm = 2.977 / 106.4
close("2(b) Q", Q, 10800); close("2(b) mol e", ne, 0.1119); close("2(b) mol M", nm, 0.02798)
close("2(b) z", ne / nm, 4.0)
# 3(b) camphor
dT = 178.4 - 157; Mm = 1000 * 37.70 * 0.045 / (0.550 * dT)
close("3(b) dTf", dT, 21.4); close("3(b) M", Mm, 144)
c, h = 93.46 / 12, 6.54 / 1.008
close("3(b) C:H ratio", c / h, 1.2)
emp = 6 * 12 + 5 * 1.008; close("3(b) n", Mm / emp, 1.87); print("   n rounds to", round(Mm / emp))
assert round(Mm / emp) == 2
# 4(b) concentration cell
Er = 0.80 + 0.0591 * math.log10(0.1); El = 0.80 + 0.0591 * math.log10(0.001)
close("4(b) E right", Er, 0.7409); close("4(b) E left", El, 0.6227); close("4(b) Ecell", Er - El, 0.118)
# 4(c)
k = 0.10 / (0.20 * 0.05); close("4(c) k", k, 10)
close("4(c) X", 0.40 / (k * 0.05), 0.80); close("4(c) Y", 0.80 / (k * 0.40), 0.20)
# 4(d)(iii)
close("4(d)(iii) E cell Cu/Ag", 0.80 - 0.34, 0.46)
# 5(c) spin-only moment, 1 unpaired
close("5(c) mu", math.sqrt(1 * 3), 1.73)

ok, bad, skipped = check_module(M, skip={r"R-C(=O)-NH2 <-> R-C(-O^-)=NH2+",   # resonance, not a reaction
                                        r"M^{z+} + z e- -> M",                 # general half-equation
                                        r"aA + bB -> products"})
print(f"\nequations balanced: {ok}")
for s in skipped: print("   skipped (scheme/resonance):", s)
for b in bad: print("BAD equation", b); fails.append(b[0])
print("\nFAILURES:", fails if fails else "none")
sys.exit(1 if fails else 0)
