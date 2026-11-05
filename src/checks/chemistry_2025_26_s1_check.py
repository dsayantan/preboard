"""Recompute every number in data/chemistry_2025_26_s1.py and check every balanced equation."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chem2526_common import near, balanced, done

R = 8.314
# 1(C)
near("1C E_left", 0.34 - 0.16, 0.18)
near("1C Nernst left (note)", 0.34 + 0.0591 / 2 * math.log10(0.15), 0.316)
near("1C Nernst emf (note)", 0.0591 / 2 * math.log10(1 / 0.15), 0.024, rel=0.03)
near("1C [Cu2+] for 0.18 V (note)", 10 ** ((0.18 - 0.34) / (0.0591 / 2)), 4e-6, rel=0.1)
# 1(B)(ii)
near("1Bii mol AgCl", 0.01 * 0.100 * 1, 0.001)
near("1Bi mu Fe2+", math.sqrt(4 * 6), 4.90)
# Q2
k = 0.693 / 5730
near("Q2 k", k, 1.209e-4)
near("Q2 t", 2.303 / k * math.log10(10), 1.904e4)
# Q5
i = 1.88 / (0.52 * 2); near("Q5 i", i, 1.81); near("Q5 alpha", i - 1, 0.81, rel=0.02)
# Q7
near("Q7 Ag/I2", 0.88 - 0.54, 0.34); near("Q7 I", -0.44 - 0.88, -1.32); near("Q7 II", -0.44 + 2.37, 1.93)
# Q10
x = (410 - 350) / (350 * 410); near("Q10 dT term", x, 4.181e-4)
near("Q10 Ea", math.log10(6) * 2.303 * R / x, 3.563e4)
# Q16(i)
Q = 1.2 * 15 * 60; E = 0.3605 * 96500 / Q
near("Q16a Q", Q, 1080); near("Q16a E", E, 32.2); near("Q16a valency", 96 / E, 2.98)
lg = (0.46 - 0.422) / (0.0591 / 2); near("Q16b log", lg, 1.286)
near("Q16b ratio", 10 ** lg, 19.32); near("Q16b Ag+", math.sqrt(0.10 / 10 ** lg), 0.072)
# Q16(ii)
L = 1.65e-4 * 1000 / 0.01; a = L / (349.1 + 40.9)
near("Q16ii Lm", L, 16.5); near("Q16ii alpha", a, 0.0423)
near("Q16ii Ka", 0.01 * a * a / (1 - a), 1.87e-5); near("Q16ii Ka approx", 0.01 * a * a, 1.79e-5)
# Q17
near("Q17 n12", math.log(34 / 25) / math.log(1.13 / 0.84), 1.04)
near("Q17 n23", math.log(25 / 18) / math.log(0.84 / 0.62), 1.08)
ks = [34e-5 / 1.13e-2, 25e-5 / 0.84e-2, 18e-5 / 0.62e-2]
for j, (kk, w) in enumerate(zip(ks, (3.01e-2, 2.98e-2, 2.90e-2))): near(f"Q17 k{j+1}", kk, w)
near("Q17 k mean", sum(ks) / 3, 2.96e-2); near("Q17 k'", sum(ks) / 6, 1.48e-2)
# Q21
near("Q21 NaCl pi", 10.5 / 2 * 400 / 298, 7.05)
near("Q21 urea check", 28.5 / 60 * 0.0821 * 298, 11.6)
near("Q21 T2", 298 * (11.6 + 1.153) / 11.6, 327.6)
mg = 50 / 62; near("Q21 mol glycol", mg, 0.8065); near("Q21 water left g", mg / (9.3 / 1.86) * 1000, 161.3)
near("Q21 ice", 200 - mg / (9.3 / 1.86) * 1000, 38.7)
xA = (700 - 600) / (700 - 450); near("Q21 xA", xA, 0.40); near("Q21 yA", 450 * xA / 600, 0.30)
near("Q21 yB", 700 * (1 - xA) / 600, 0.70)

# equations
for name, eq in [
    ("1Aiii hydrolysis", "C6H5N2Cl + H2O -> C6H5OH + N2 + HCl"),
    ("1Aiii Br2", "C6H5OH + 3 Br2 -> C6H3Br3O + 3 HBr"),
    ("1Aiv P2O5", "C2H5NO -> C2H3N + H2O"),
    ("Q3 reduce", "C6H5NO2 + 6 H -> C6H7N + 2 H2O"),
    ("Q3 diazo", "C6H7N + NaNO2 + 2 HCl -> C6H5N2Cl + NaCl + 2 H2O"),
    ("Q3 tribromo", "C6H7N + 3 Br2 -> C6H4Br3N + 3 HBr"),
    ("Q6 HI", "C2H4O + 4 HI -> C2H6 + H2O + 2 I2"),
    ("Q6 urotropine", "6 CH2O + 4 NH3 -> C6H12N4 + 6 H2O"),
    ("Q7 Ag+/I-", "2 Ag+ + 2 I- -> 2 Ag + I2"),
    ("Q8 chromite", "4 FeCr2O4 + 8 Na2CO3 + 7 O2 -> 8 Na2CrO4 + 2 Fe2O3 + 8 CO2"),
    ("Q8 acidify", "2 Na2CrO4 + H2SO4 -> Na2Cr2O7 + Na2SO4 + H2O"),
    ("Q8 KCl", "Na2Cr2O7 + 2 KCl -> K2Cr2O7 + 2 NaCl"),
    ("Q8 sulphite", "K2Cr2O7 + 4 H2SO4 + 3 Na2SO3 -> K2SO4 + Cr2(SO4)3 + 3 Na2SO4 + 4 H2O"),
    ("Q9 tollens formic", "HCOOH + 2 [Ag(NH3)2]+ + 2 OH- -> 2 Ag + CO2 + 2 H2O + 4 NH3"),
    ("Q11 carbylamine", "C6H7N + CHCl3 + 3 KOH -> C7H5N + 3 KCl + 3 H2O"),
    ("Q11 Hofmann", "C2H5NO + Br2 + 4 KOH -> CH5N + K2CO3 + 2 KBr + 2 H2O"),
    ("Q12 HNO2", "C2H7N + HNO2 -> C2H6O + N2 + H2O"),
    ("Q12 tollens", "C2H4O + 2 [Ag(NH3)2]+ + 3 OH- -> C2H3O2^- + 2 Ag + 4 NH3 + 2 H2O"),
    ("Q12 ester", "C2H4O2 + C2H6O -> C4H8O2 + H2O"),
    ("Q12OR nitration", "C6H6 + HNO3 -> C6H5NO2 + H2O"),
    ("Q12OR acetyl", "C6H7N + C4H6O3 -> C8H9NO + C2H4O2"),
    ("Q12OR final", "C6H4N3O2BF4 + NaNO2 -> C6H4N2O4 + N2 + NaBF4"),
    ("Q13a", "K2Cr2O7 + 3 H2S + 4 H2SO4 -> K2SO4 + Cr2(SO4)3 + 7 H2O + 3 S"),
    ("Q13a ionic", "Cr2O7^2- + 8 H+ + 3 H2S -> 2 Cr^3+ + 3 S + 7 H2O"),
    ("Q13b", "2 KMnO4 + 10 FeSO4 + 8 H2SO4 -> K2SO4 + 2 MnSO4 + 5 Fe2(SO4)3 + 8 H2O"),
    ("Q13b ionic", "MnO4^- + 5 Fe^2+ + 8 H+ -> Mn^2+ + 5 Fe^3+ + 4 H2O"),
    ("Q14 sandmeyer", "C6H5N2Cl -> C6H5Cl + N2"),
    ("Q14 WF", "C6H5Cl + 2 Na + CH3Cl -> C7H8 + 2 NaCl"),
    ("Q14 Fittig", "2 C6H5Cl + 2 Na -> C12H10 + 2 NaCl"),
    ("Q15 glyala", "C2H5NO2 + C3H7NO2 -> C5H10N2O3 + H2O"),
    ("Q16b cell", "Cu + 2 Ag+ -> Cu^2+ + 2 Ag"),
    ("Q18 haloform", "C8H8O + 3 I2 + 4 NaOH -> C7H5O2Na + CHI3 + 3 NaI + 3 H2O"),
    ("Q18 clemmensen", "C5H10O + 4 H -> C5H12 + H2O"),
    ("Q19 carbylamine", "CH5N + CHCl3 + 3 KOH -> C2H3N + 3 KCl + 3 H2O"),
    ("Q20 thiocyanate", "Fe^3+ + SCN- -> [Fe(SCN)]^2+"),
]:
    balanced(name, eq)
done()
