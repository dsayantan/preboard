"""Recompute every number in data/chemistry_2025_26_s2.py and check every balanced equation."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chem2526_common import near, balanced, done

R = 8.314
# 1(C)
near("1C L0 HAc", 91.0 + 426.1 - 126.4, 390.7)
G = 0.01161 * 31.6; near("1C cell const", G, 0.3669); near("1C kappa HCl", G / 29.2, 1.256e-2)
# Q2
x = (313 - 293) / (293 * 313); near("Q2 dT", x, 2.181e-4)
near("Q2 Ea", math.log10(4) * 2.303 * R / x, 5.29e4)
# Q5
M = 1.754 * 342 / 10; near("Q5 M", M, 59.99); near("Q5 i", 60.06 / M, 1.001); near("Q5 i (paper wording)", M / 60.06, 0.999)
# Q7
L = 7.896e-5 * 1000 / 0.00241; a = L / 390
near("Q7 Lm", L, 32.76); near("Q7 alpha", a, 0.0840); near("Q7 Ka", 0.00241 * a * a / (1 - a), 1.86e-5)
# Q10
near("Q10 Ea", 3163 * 2.303 * R, 6.06e4)
lk = -3163 / 293 + 11.9; near("Q10 logk", lk, 1.105); near("Q10 k", 10 ** lk, 12.7)
near("Q10 t1/2", 0.693 / 10 ** lk, 0.0544); near("Q10 t1/2 s", 0.693 / 10 ** lk * 60, 3.3, rel=0.02)
# Q16
near("Q16 E", 0.34 + 0.76, 1.10); near("Q16 dG kJ", -2 * 96500 * 1.10 / 1000, -212.3)
n = 5 * 2 * 3600 / (2 * 96500); near("Q16ii mol Ni", n, 0.187); near("Q16ii g Ni", n * 58.69, 10.9)
# Q17
near("Q17 iii", 3 ** 2 * 2, 18)
# Q20
dT = 68.04 - 61.7; near("Q20 dTb", dT, 6.34)
near("Q20 M", 3.63 * 6.21 * 1000 / (dT * 24.0), 148)
near("Q20 i", 6.8 / (0.15 * 0.0821 * 310), 1.78)
# Q21 spin-only moments
near("Q21 mu 5", math.sqrt(5 * 7), 5.92); near("Q21 mu 1", math.sqrt(3), 1.73)

for name, eq in [
    ("1Aiv allyl", "C3H6 + Cl2 -> C3H5Cl + HCl"),
    ("1Biii KCN", "C2H5Br + KCN -> C3H5N + KBr"),
    ("1Bv Ca salt", "2 C2H4O2 + Ca(OH)2 -> C4H6O4Ca + 2 H2O"),
    ("1Bv distil", "C4H6O4Ca -> C3H6O + CaCO3"),
    ("Q3 KCN", "CH3Br + KCN -> C2H3N + KBr"),
    ("Q3 imine hydrolysis", "C3H6NMgBr + 2 H2O -> C3H6O + NH3 + Mg(OH)Br"),
    ("Q3 chlorination", "C6H6 + Cl2 -> C6H5Cl + HCl"),
    ("Q3 Fittig", "2 C6H5Cl + 2 Na -> C12H10 + 2 NaCl"),
    ("Q6 picric", "C6H6O + 3 HNO3 -> C6H3N3O7 + 3 H2O"),
    ("Q6 hydroboration", "6 C3H6 + B2H6 -> 2 C9H21B"),
    ("Q6 oxidation", "C9H21B + 3 H2O2 -> 3 C3H8O + B(OH)3"),
    ("Q9 cross aldol", "C3H6O + C4H8O -> C7H14O2"),
    ("Q9OR amide", "C2H7NO2 -> C2H5NO + H2O"),
    ("Q11 sandmeyer", "C6H5N2Cl -> C6H5Cl + N2"),
    ("Q12 Williamson", "C2H5Br + C2H5ONa -> C4H10O + NaBr"),
    ("Q12 Dow", "C6H5Cl + 2 NaOH -> C6H5ONa + NaCl + H2O"),
    ("Q12 grignard", "C3H7OMgBr + H2O -> C3H8O + Mg(OH)Br"),
    ("Q13a", "2 KMnO4 + 5 H2C2O4 + 3 H2SO4 -> K2SO4 + 2 MnSO4 + 10 CO2 + 8 H2O"),
    ("Q13a ionic", "2 MnO4^- + 5 C2O4^2- + 16 H+ -> 2 Mn^2+ + 10 CO2 + 8 H2O"),
    ("Q13b", "K2Cr2O7 + 3 SO2 + H2SO4 -> K2SO4 + Cr2(SO4)3 + H2O"),
    ("Q13b ionic", "Cr2O7^2- + 3 SO2 + 2 H+ -> 2 Cr^3+ + 3 SO4^2- + H2O"),
    ("Q14 HI", "C4H10O + HI -> C2H5I + C2H6O"),
    ("Q14 HI excess", "C4H10O + 2 HI -> 2 C2H5I + H2O"),
    ("Q14 Hofmann", "C2H5NO + Br2 + 4 KOH -> CH5N + K2CO3 + 2 KBr + 2 H2O"),
    ("Q14 ammonolysis", "C2H5Br + 2 NH3 -> C2H7N + NH4Br"),
    ("Q16 Daniell", "Zn + Cu^2+ -> Zn^2+ + Cu"),
    ("Q16ii anode", "Pb + SO4^2- -> PbSO4 + 2 e^-"),
    ("Q16ii cathode", "PbO2 + SO4^2- + 4 H+ + 2 e^- -> PbSO4 + 2 H2O"),
    ("Q16ii overall", "Pb + PbO2 + 2 H2SO4 -> 2 PbSO4 + 2 H2O"),
    ("Q18 KI", "C6H5N2Cl + KI -> C6H5I + KCl + N2"),
    ("Q18 nitrile hydrolysis", "C7H5N + 2 H2O + H+ -> C7H6O2 + NH4+"),
    ("Q18 amide", "C7H9NO2 -> C7H7NO + H2O"),
    ("Q19 cyanohydrin", "C7H6O + HCN -> C8H7NO"),
    ("Q19 cannizzaro", "2 CH2O + NaOH -> CH4O + CHO2Na"),
    ("Q19 haloform", "C4H8O + 3 I2 + 4 NaOH -> CHI3 + C3H5O2Na + 3 NaI + 3 H2O"),
    ("Q19 dehydration", "C4H10O -> C4H8 + H2O"),
    ("Q21 AgNO3", "[Co(NH3)5SO4]Cl + AgNO3 -> [Co(NH3)5SO4]NO3 + AgCl"),
    ("Q21 BaCl2", "[Co(NH3)5Cl]SO4 + BaCl2 -> [Co(NH3)5Cl]Cl2 + BaSO4"),
]:
    balanced(name, eq)
done()
