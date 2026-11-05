"""Checks for Chemistry pre-board 2016-17: every numerical answer recomputed, every equation balanced."""
import sys, os, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.join(HERE, ".."), os.path.join(HERE, "..", "data"), os.path.join(HERE, "..", "figs")]
import chemistry_2016_17 as M
from chem_balance_1517 import check_module

fails = []
def close(name, got, want, rel=0.01):
    ok = abs(got - want) <= rel * abs(want)
    print(f"{'ok ' if ok else 'BAD'} {name}: computed {got:.6g}, printed {want}")
    if not ok: fails.append(name)

# 2(a)(i) osmotic pressure
pi = 500 / 76; close("2(a)(i) pi atm", pi, 6.579)
Mm = 8 * 0.0821 * 300 / (pi * 0.100); close("2(a)(i) M", Mm, 299.5, 0.002)
# 2(c)(i) e = F / NA
close("2(c)(i) e", 48250 / 6.022e23, 8.01e-20)
close("    actual F/NA check", 96500 / 6.022e23, 1.602e-19)
# 3(a)(i) Kohlrausch
close("3(a)(i) Lambda HAc", 91 + 426.1 - 126.5, 390.6, 1e-6)
# 3(a)(ii) Ea from temperature coefficient 1.75 over 298-308 K
lg = math.log10(1.75); close("3(a)(ii) log 1.75", lg, 0.2430)
T1, T2 = 298, 308
Ea_cal = 2.303 * 1.987 * T1 * T2 / (T2 - T1) * lg
Ea_J = 2.303 * 8.314 * T1 * T2 / (T2 - T1) * lg
close("3(a)(ii) T1T2/dT", T1 * T2 / (T2 - T1), 9178.4)
close("3(a)(ii) Ea cal", Ea_cal, 1.021e4); close("3(a)(ii) Ea kcal", Ea_cal / 1000, 10.2)
close("3(a)(ii) Ea kJ", Ea_J / 1000, 42.7)
# exact ln form as a cross-check (should agree to <0.1%)
close("    ln-form Ea kJ", 8.314 * math.log(1.75) / (1 / T1 - 1 / T2) / 1000, 42.7)
# 3(d) molality
close("3(d) mol glucose", 3.6 / 180, 0.020); close("3(d) molality", 3.6 / 180 / 0.5, 0.040)
# 4(a) Pb | Pb2+ || I- | I2 | Pt
E0 = 0.536 - (-0.126); close("4(a) E0", E0, 0.662)
Q = 0.1 * 0.1 ** 2; E = E0 - 0.0591 / 2 * math.log10(Q)
close("4(a) correction", -0.0591 / 2 * math.log10(Q), 0.0887); close("4(a) Ecell", E, 0.751, 0.001)
# 3(c) Cu/Ag
close("3(c) E0 cell", 0.80 - 0.34, 0.46)
# spin-only moments
close("5(b) mu 5 unpaired", math.sqrt(5 * 7), 5.92); close("5(c) mu 2 unpaired", math.sqrt(2 * 4), 2.83)
# electron counts: CoF6 3- (d6 high spin) and FeCl4- (d5), Ni(II) d8
assert 26 - 3 - 18 == 5 and 27 - 3 - 18 == 6 and 28 - 2 - 18 == 8
print("ok  d-electron counts: Fe3+ d5, Co3+ d6, Ni2+ d8")
# high-spin d6 octahedral: t2g^4 eg^2 -> 4 unpaired ; d5 tetrahedral e^2 t2^3 -> 5
assert 4 == (1 + 1 + 0) + 2 and 5 == 2 + 3

ok, bad, skipped = check_module(M)
print(f"\nequations balanced: {ok}")
for s in skipped: print("   skipped (scheme):", s)
for b in bad: print("BAD equation", b); fails.append(b[0])
print("\nFAILURES:", fails if fails else "none")
sys.exit(1 if fails else 0)
