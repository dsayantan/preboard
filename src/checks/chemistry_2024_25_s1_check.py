"""Recompute every number in data/chemistry_2024_25_s1.py and check every balanced equation."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chem2526_common import near, balanced, done

# 1(B)(v) / 1(A)(iv) spin-only
near("1Aiv mu Cu2+", math.sqrt(1 * 3), 1.73)
# 1(C)
near("1C t1/2", 0.693 / 2.5e-15, 2.77e14)
k3 = 2.303 / 300 * math.log10(3)
near("1C k from 1/3 in 5 min (note)", k3, 3.66e-3); near("1C t1/2 from that k (note)", 0.693 / k3, 189)
# Q2 [H+] for acetic acid (Ka 1.8e-5)
near("Q2 [H+] 1 M", math.sqrt(1.8e-5 * 1), 4.2e-3, rel=0.02); near("Q2 [H+] 0.1 M", math.sqrt(1.8e-5 * 0.1), 1.3e-3, rel=0.04)
# Q5  Ea/500 = (Ea-20)/400
Ea = 20 * 500 / (500 - 400); near("Q5 Ea", Ea, 100)
# Q10
E0 = -0.14 - (-1.66); near("Q10 E0", E0, 1.52)
Qr = 0.01 ** 2 / 0.015 ** 3; near("Q10 Q", Qr, 29.63); near("Q10 logQ", math.log10(Qr), 1.472)
E = E0 - 0.0591 / 6 * math.log10(Qr); near("Q10 E", E, 1.5055, rel=0.001)
# Q13
near("Q13 Kf from 0.6 g NaCl", 3.8 / (2 * (0.6 / 58.5) / 0.010), 1.85)
near("Q13 molal NaCl", (0.6 / 58.5) / 0.010, 1.026)
near("Q13 m glucose", (0.6 / 180) / 0.010, 0.333)
near("Q13 dTf glucose", 1.86 * (0.6 / 180) / 0.010, 0.62)
pts1 = [(0.3, 1.9), (0.4, 2.5), (0.5, 3.0), (0.6, 3.8), (0.8, 5.1), (1.0, 6.4)]
b = sum(m * t for m, t in pts1) / sum(m * m for m, t in pts1)
near("Q13 slope ~6.3 per g", b, 6.3, rel=0.03)
near("Q13 expected at 0.5 g", b * 0.5, 3.15, rel=0.03)
# Q15
near("Q15 mu", math.sqrt(15), 3.87)
# Q16 OR
Lm = 7.896e-5 * 1000 / 0.00241; a = Lm / 390.5
near("Q16 Lm", Lm, 32.76); near("Q16 alpha", a, 0.0839)
near("Q16 Ka", 0.00241 * a * a / (1 - a), 1.85e-5); near("Q16 Ka approx", 0.00241 * a * a, 1.70e-5)
near("Q16 E cell (c)", 0.40 - (-0.80), 1.20)
# Q17 invert sugar rotation
near("Q17 invert", (52.5 - 92.4) / 2, -19.95)
# Q18
near("Q18 x", math.log(4e-3 / 2e-3, 2), 1); near("Q18 k", 2e-3 / 1.0, 2e-3)
for r in (2e-3 / 1, 4e-3 / 2, 8e-3 / 4, 2e-3 / 1, 2e-3 / 1): near("Q18 k each", r, 2e-3)
# Q19 pKb (literature) dimethylamine stronger: just ordering, no numbers
# Q21 I
xA = (700 - 600) / (700 - 450); near("Q21 xA", xA, 0.40)
near("Q21 yA", 450 * xA / 600, 0.30); near("Q21 yB", 700 * (1 - xA) / 600, 0.70)
M = 50 * 0.0821 / (0.500 * 1.23e-4); near("Q21 M polymer", M, 6.67e4)
# Q21 II
x = 2e-5 / (1000 / 18 + 2e-5); near("Q21II x", x, 3.6e-7); near("Q21II p", 5.32e4 * x, 1.92e-2)
near("Q21II sucrose dTb", 0.05 * 180 / 342, 0.026, rel=0.02)
near("Q21II acetic dTb", 3.07 * (10 / 180) / 0.525, 0.33, rel=0.02)
near("Q21II glucose/water dTb with Kb .52 (consistency)", 0.52 * (10 / 180) / 0.5, 0.058, rel=0.02)

for name, eq in [
    ("1Aiii dry distillation", "C4H6O4Ca -> C3H6O + CaCO3"),
    ("1Aiii iodoform", "C3H6O + 3 I2 + 4 NaOH -> CHI3 + C2H3O2Na + 3 NaI + 3 H2O"),
    ("1Bi carbylamine", "C3H9N + CHCl3 + 3 KOH -> C4H7N + 3 KCl + 3 H2O"),
    ("1Bi reduction", "C4H7N + 4 H -> C4H11N"),
    ("1Biii side chain", "C7H8 + Cl2 -> C7H7Cl + HCl"),
    ("Q3 iodoform", "C8H8O + 3 I2 + 4 NaOH -> C7H5O2Na + CHI3 + 3 NaI + 3 H2O"),
    ("Q3 Ag", "2 CHI3 + 6 Ag -> C2H2 + 6 AgI"),
    ("Q4 KCN", "C2H5Br + KCN -> C3H5N + KBr"),
    ("Q4 Gattermann", "C6H5N2Cl -> C6H5Cl + N2"),
    ("Q6 HNO2", "C2H7N + HNO2 -> C2H6O + N2 + H2O"),
    ("Q6 amide", "C2H7NO2 -> C2H5NO + H2O"),
    ("Q6 Hofmann", "C2H5NO + Br2 + 4 KOH -> CH5N + K2CO3 + 2 KBr + 2 H2O"),
    ("Q8 elim", "C3H7Cl + KOH -> C3H6 + KCl + H2O"),
    ("Q8 HBr", "C3H6 + HBr -> C3H7Br"),
    ("Q8 Finkelstein", "C3H7Br + NaI -> C3H7I + NaBr"),
    ("Q8 Grignard", "C3H7I + Mg -> C3H7MgI"),
    ("Q9 SOCl2", "C7H6O2 + SOCl2 -> C7H5OCl + SO2 + HCl"),
    ("Q9 NH3", "C7H5OCl + 2 NH3 -> C7H7NO + NH4Cl"),
    ("Q9 Hofmann", "C7H7NO + Br2 + 4 KOH -> C6H7N + K2CO3 + 2 KBr + 2 H2O"),
    ("Q9 diazo", "C6H7N + NaNO2 + 2 HCl -> C6H5N2Cl + NaCl + 2 H2O"),
    ("Q9OR PCl5", "C7H6O2 + PCl5 -> C7H5OCl + POCl3 + HCl"),
    ("Q9OR Rosenmund", "C7H5OCl + H2 -> C7H6O + HCl"),
    ("Q9OR benzoin", "2 C7H6O -> C14H12O2"),
    ("Q10 cell", "2 Al + 3 Sn^2+ -> 2 Al^3+ + 3 Sn"),
    ("Q11 FeCl3", "6 C6H6O + FeCl3 -> [Fe(C6H5O)6]^3- + 3 H+ + 3 HCl"),
    ("Q11 Lucas", "C3H8O + HCl -> C3H7Cl + H2O"),
    ("Q12 CuCN", "C6H5N2Cl + CuCN -> C7H5N + N2 + CuCl"),
    ("Q12 hydrolysis", "C7H5N + 2 H2O + H+ -> C7H6O2 + NH4+"),
    ("Q12 Sn/HCl", "C6H5NO2 + 6 H -> C6H7N + 2 H2O"),
    ("Q12 Br2", "C6H7N + 3 Br2 -> C6H4Br3N + 3 HBr"),
    ("Q12 salt", "C6H7N + H2SO4 -> C6H9NO4S"),
    ("Q12 sulphanilic", "C6H9NO4S -> C6H7NO3S + H2O"),
    ("Q14 hydrazone", "C3H6O + N2H4 -> C3H8N2 + H2O"),
    ("Q14 WK", "C3H8N2 -> C3H8 + N2"),
    ("Q14 Perkin", "C7H6O + C4H6O3 -> C9H8O2 + C2H4O2"),
    ("Q16 anode", "Pb + SO4^2- -> PbSO4 + 2 e-"),
    ("Q16 cathode", "PbO2 + SO4^2- + 4 H+ + 2 e- -> PbSO4 + 2 H2O"),
    ("Q16 overall", "Pb + PbO2 + 2 H2SO4 -> 2 PbSO4 + 2 H2O"),
    ("Q17 sucrose", "C12H22O11 + H2O -> C6H12O6 + C6H12O6"),
    ("Q17 HI (as H)", "C6H12O6 + 14 H -> C6H14 + 6 H2O"),
    ("Q19 coupling", "C6H5N2Cl + C6H6O + NaOH -> C12H10N2O + NaCl + H2O"),
    ("Q19 carbylamine", "C6H7N + CHCl3 + 3 KOH -> C7H5N + 3 KCl + 3 H2O"),
    ("Q20 oxalic", "2 KMnO4 + 3 H2SO4 + 5 H2C2O4 -> K2SO4 + 2 MnSO4 + 10 CO2 + 8 H2O"),
    ("Q20 oxalic ionic", "2 MnO4^- + 5 C2O4^2- + 16 H+ -> 2 Mn^2+ + 10 CO2 + 8 H2O"),
    ("Q20 dichromate", "K2Cr2O7 + 7 H2SO4 + 6 FeSO4 -> K2SO4 + Cr2(SO4)3 + 3 Fe2(SO4)3 + 7 H2O"),
    ("Q20 dichromate ionic", "Cr2O7^2- + 6 Fe^2+ + 14 H+ -> 2 Cr^3+ + 6 Fe^3+ + 7 H2O"),
]:
    balanced(name, eq)
done()
