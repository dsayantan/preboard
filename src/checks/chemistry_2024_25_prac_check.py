"""Recompute every number in data/chemistry_2024_25_prac.py and check the equations."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chem2526_common import near, balanced, done

Mk = 39 + 55 + 4 * 16; near("KMnO4 Mr", Mk, 158)
Mm = 2 * 18 + 96 + 56 + 96 + 6 * 18; near("Mohr Mr", Mm, 392)
near("Mohr Mr from atoms", 2 * 14 + 20 * 1 + 2 * 32 + 14 * 16 + 56 + 0, 392)  # N2H20Fe S2O14
M1 = 1.05 / Mk; near("M1", M1, 0.006646, rel=1e-3)
# sample titres
for a, b, v in [(0.00, 21.40, 21.40), (0.00, 21.10, 21.10), (0.50, 21.60, 21.10)]:
    near(f"titre {a}->{b}", b - a, v, rel=1e-6)
V = 21.10
M2 = 5 * M1 * V / 20; near("M2", M2, 0.035056, rel=2e-4)
near("M2 from the printed (rounded) M1 0.006646", 5 * 0.006646 * V / 20, 0.035058, rel=1e-5)
near("strength from printed M2", 0.035058 * Mm, 13.74, rel=1e-3)
s = M2 * Mm; near("strength", s, 13.74, rel=1e-3)
p = s / 14.5 * 100; near("purity", p, 94.8, rel=1e-3)
near("generated purity ~95% gives titre", 0.95 * 14.5 / Mm * 20 / (5 * M1), 21.15, rel=2e-3)
near("per-mL M2 coefficient", 5 * M1 / 20, 0.0016615, rel=1e-3)
near("per-mL strength", 5 * M1 / 20 * Mm, 0.6513, rel=1e-3)
near("per-mL purity", 5 * M1 / 20 * Mm / 14.5 * 100, 4.492, rel=1e-3)
near("100% titre", 14.5 / Mm * 20 / (5 * M1), 22.26, rel=1e-3)

for name, eq in [
    ("Q1 molecular (printed)", "2 KMnO4 + 8 H2SO4 + 10 N2H20FeS2O14 -> K2SO4 + 2 MnSO4 + 10 N2H8SO4 + 5 Fe2(SO4)3 + 68 H2O"),
    ("Q1 ionic (printed)", "2 MnO4^- + 10 Fe^2+ + 16 H+ -> 2 Mn^2+ + 10 Fe^3+ + 8 H2O"),
    ("Q2a HCl", "C6H7N + HCl -> C6H8NCl"),
    ("Q2a Br2", "C6H7N + 3 Br2 -> C6H4Br3N + 3 HBr"),
    ("Q2a diazo", "C6H7N + HNO2 + H+ -> C6H5N2+ + 2 H2O"),
    ("Q2b Fehling (glucose)", "C6H12O6 + 2 Cu^2+ + 5 OH- -> C6H11O7^- + Cu2O + 3 H2O"),
    ("Q2b Tollens (glucose)", "C6H12O6 + 2 [Ag(NH3)2]+ + 3 OH- -> C6H11O7^- + 2 Ag + 4 NH3 + 2 H2O"),
    ("Q3 HNO3", "2 NO3^- + H2SO4 -> 2 HNO3 + SO4^2-"),
    ("Q3 decomp", "4 HNO3 -> 4 NO2 + O2 + 2 H2O"),
    ("Q3 Cu", "Cu + 4 HNO3 -> Cu(NO3)2 + 2 NO2 + 2 H2O"),
    ("Q3 FeSO4", "6 FeSO4 + 3 H2SO4 + 2 HNO3 -> 3 Fe2(SO4)3 + 2 NO + 4 H2O"),
    ("Q3 ring", "FeSO4 + NO + 5 H2O -> [Fe(H2O)5NO]SO4"),
    ("Q3 PbCl2", "Pb^2+ + 2 Cl- -> PbCl2"),
    ("Q3 PbCrO4", "Pb^2+ + CrO4^2- -> PbCrO4"),
    ("Q3 PbI2", "Pb^2+ + 2 I- -> PbI2"),
]:
    balanced(name, eq)
# the page must carry the printed-M1 value and the glucose identification
_d = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "chemistry_2024_25_prac.py")).read()
assert "0.035056" not in _d and _d.count("0.035058") == 3, "M2 must be 0.035058 everywhere"
assert "glucose" in _d.split('Q("2(b)"')[1].split('Q("3"')[0], "2(b) must identify glucose"
done()
