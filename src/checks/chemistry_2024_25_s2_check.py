"""Recompute every number in data/chemistry_2024_25_s2.py and check every balanced equation."""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chem2526_common import near, balanced, done

R = 8.314
# 1(A)(ii) oxidation state of Co in [Co(NH3)5(NO2)]+ : x - 1 = +1
near("1Aii Co ox", 1 + 1, 2)
# 1(C)
near("1C(ii) % left", 100 * 0.5 ** (250 / 50), 3.125)
near("1C(iii) factor", 3 ** 2 * 2, 18)
# Q2
near("Q2 Leq", 1000 * 1.65e-4 / 0.02, 8.25); near("Q2 Lm", 1000 * 1.65e-4 / 0.01, 16.5)
# Q5
near("Q5 Ea", 3163 * 2.303 * R, 6.06e4)
lk = -3163 / 293 + 11.9; near("Q5 logk", lk, 1.105); near("Q5 k", 10 ** lk, 12.7)
near("Q5 t1/2", 0.693 / 10 ** lk, 0.0544); near("Q5 t1/2 s", 0.693 / 10 ** lk * 60, 3.3, rel=0.02)
# Q7 spin-only
near("Q7 mu", math.sqrt(1 * 3), 1.73)
# Q10
E = 0.80 + 0.25; near("Q10 E", E, 1.05)
lK = 2 * E / 0.0591; near("Q10 logK", lK, 35.53); near("Q10 K", 10 ** lK, 3.4e35, rel=0.02)
near("Q10 work kJ", 2 * 96500 * E / 1000, 202.7)
# Q13
dTc = 4.9 * 2 * 1000 / (122 * 25); near("Q13 dTf calc", dTc, 3.21); near("Q13 iA", 1.62 / dTc, 0.504)
near("Q13 iB", 6.8 / (0.15 * 0.0821 * 310), 1.78); near("Q13 CRT", 0.15 * 0.0821 * 310, 3.818)
# Q15 CFSE (units of Delta_o)
near("Q15 low spin d4", 4 * -0.4, -1.6); near("Q15 high spin d4", 3 * -0.4 + 0.6, -0.6)
# Q16
near("Q16 E", 0.34 + 0.76, 1.10); near("Q16 dG kJ", -2 * 96500 * 1.10 / 1000, -212.3)
n = 5 * 2 * 3600 / (2 * 96500); near("Q16 OR mol Ni", n, 0.187); near("Q16 OR g Ni", n * 58.69, 10.9)
# Q18
rows = [(0.20, 0.05, 6e-3), (0.40, 0.05, 1.2e-2), (0.80, 0.10, 4.8e-2)]
x = math.log(rows[1][2] / rows[0][2]) / math.log(rows[1][0] / rows[0][0]); near("Q18 x", x, 1)
y = math.log(rows[2][2] / rows[1][2] / (rows[2][0] / rows[1][0]) ** x) / math.log(rows[2][1] / rows[1][1]); near("Q18 y", y, 1)
for i, (a, b, r) in enumerate(rows):
    near(f"Q18 k run {i+1}", r / (a * b), 0.6)
# Q20 charges
near("Q20 Pt", 0 - 0 + 1 + 1, 2)
near("Q20 Prussian blue charge", 4 * 3 + 3 * (2 - 6), 0)
# Q21(i)
dT = 68.04 - 61.7; near("Q21 dTb", dT, 6.34)
near("Q21 M", 3.63 * 6.21 * 1000 / (dT * 24.0), 148)
# Q21(ii)
dTf = 1.86 * 0.0711; near("Q21ii dTf calc", dTf, 0.132); near("Q21ii i", 0.320 / dTf, 2.42)
near("Q21ii dTf i=3", 3 * dTf, 0.397)
C = (60 / 1e-9) / 6.023e23; near("Q21ii C", C, 9.96e-14)
near("Q21ii pi atm", C * 0.0821 * 293, 2.40e-12); near("Q21ii pi Pa", C * 1000 * R * 293, 2.4e-7, rel=0.02)
near("Q21ii sucrose dTb", 0.05 * 180 / 342, 0.026, rel=0.02)
near("Q21ii AcOH dTb", 3.07 * (10 / 180) / (500 * 1.049 / 1000), 0.3, rel=0.1)

for name, eq in [
    ("1Biii SOCl2", "C2H6O + SOCl2 -> C2H5Cl + SO2 + HCl"),
    ("1Aiii ozonolysis (net)", "C3H6 + O3 + H2O -> C2H4O + CH2O + H2O2"),
    ("Q3 Fehling", "C3H6O + 2 Cu^2+ + 5 OH^- -> C3H5O2^- + Cu2O + 3 H2O"),
    ("Q3 bisulphite", "C3H6O + NaHSO3 -> C3H7O4SNa"),
    ("Q4 KCN", "CH3Br + KCN -> C2H3N + KBr"),
    ("Q4 grignard", "CH3Br + Mg -> CH3MgBr"),
    ("Q4 imine", "C2H3N + CH3MgBr -> C3H6NMgBr"),
    ("Q4 imine hydrolysis", "C3H6NMgBr + 2 H2O -> C3H6O + NH3 + Mg(OH)Br"),
    ("Q4 chlorination", "C6H6 + Cl2 -> C6H5Cl + HCl"),
    ("Q4 Fittig", "2 C6H5Cl + 2 Na -> C12H10 + 2 NaCl"),
    ("Q6 amide", "C7H6O2 + NH3 -> C7H7NO + H2O"),
    ("Q6 Hofmann", "C7H7NO + Br2 + 4 KOH -> C6H7N + K2CO3 + 2 KBr + 2 H2O"),
    ("Q8a", "C6H6O + NaOH -> C6H5ONa + H2O"),
    ("Q8a Williamson", "C6H5ONa + CH3I -> C7H8O + NaI"),
    ("Q8b add", "C3H6O + CH3MgBr -> C4H9OMgBr"),
    ("Q8b hydrolysis", "C4H9OMgBr + H2O -> C4H10O + Mg(OH)Br"),
    ("Q9a oxidation", "C8H10 + 6 O -> C7H6O2 + CO2 + 2 H2O"),
    ("Q9a sodalime", "C7H6O2 + 2 NaOH -> C6H6 + Na2CO3 + H2O"),
    ("Q9b SOCl2", "C2H4O2 + SOCl2 -> C2H3OCl + SO2 + HCl"),
    ("Q9b Rosenmund", "C2H3OCl + H2 -> C2H4O + HCl"),
    ("Q9OR Cannizzaro", "2 CH2O + NaOH -> CH4O + CHO2Na"),
    ("Q9OR Cu", "CH4O -> CH2O + H2"),
    ("Q9OR acidify", "CHO2Na + HCl -> CH2O2 + NaCl"),
    ("Q10 cell", "Ni + 2 Ag+ -> Ni^2+ + 2 Ag"),
    ("Q11 iodoform", "C2H6O + 4 I2 + 6 NaOH -> CHI3 + CHO2Na + 5 NaI + 5 H2O"),
    ("Q11 FeCl3", "6 C6H6O + FeCl3 -> [Fe(OC6H5)6]^3- + 3 H+ + 3 HCl"),
    ("Q12 reduction", "C6H5NO2 + 6 H -> C6H7N + 2 H2O"),
    ("Q12 diazotisation", "C6H7N + NaNO2 + 2 HCl -> C6H5N2Cl + NaCl + 2 H2O"),
    ("Q12 KI", "C6H5N2Cl + KI -> C6H5I + KCl + N2"),
    ("Q12 KCN", "CH3Cl + KCN -> C2H3N + KCl"),
    ("Q12 LiAlH4", "C2H3N + 4 H -> C2H7N"),
    ("Q12 carbylamine", "C2H7N + CHCl3 + 3 KOH -> C3H5N + 3 KCl + 3 H2O"),
    ("Q14 hydrazone", "C3H6O + N2H4 -> C3H8N2 + H2O"),
    ("Q14 WK", "C3H8N2 -> C3H8 + N2"),
    ("Q14 Perkin", "C7H6O + C4H6O3 -> C9H8O2 + C2H4O2"),
    ("Q14 benzoin", "2 C7H6O -> C14H12O2"),
    ("Q16 Daniell", "Zn + Cu^2+ -> Zn^2+ + Cu"),
    ("Q16 OR Ni", "Ni^2+ + 2 e^- -> Ni"),
    ("Q16 OR anode", "Pb + SO4^2- -> PbSO4 + 2 e^-"),
    ("Q16 OR cathode", "PbO2 + SO4^2- + 4 H+ + 2 e^- -> PbSO4 + 2 H2O"),
    ("Q16 OR overall", "Pb + PbO2 + 2 H2SO4 -> 2 PbSO4 + 2 H2O"),
    ("Q17 acid", "C2H5NO2 + H+ -> C2H6NO2+"),
    ("Q17 base", "C2H5NO2 + OH^- -> C2H4NO2^- + H2O"),
    ("Q18 rxn", "2 NO2 + F2 -> 2 NO2F"),
    ("Q19 Dow", "C6H5Cl + 2 NaOH -> C6H5ONa + NaCl + H2O"),
    ("Q19 acidify", "C6H5ONa + HCl -> C6H6O + NaCl"),
    ("Q19 sulphonation", "C6H6O + 2 H2SO4 -> C6H6O7S2 + 2 H2O"),
    ("Q19 nitration", "C6H6O7S2 + 3 HNO3 -> C6H3N3O7 + 2 H2SO4 + H2O"),
    ("Q19 coupling", "C6H5N2Cl + C6H6O + NaOH -> C12H10N2O + NaCl + H2O"),
    ("Q19 phenoxide", "C6H6O + NaOH -> C6H5ONa + H2O"),
    ("Q19 Kolbe", "C6H5ONa + CO2 -> C7H5O3Na"),
    ("Q19 salicylic", "C7H5O3Na + HCl -> C7H6O3 + NaCl"),
    ("Q21 Na2SO4", "Na2SO4 -> 2 Na+ + SO4^2-"),
]:
    balanced(name, eq)
# review additions: ionic charges in mhchem prose must carry ^ (else '-' renders as a bond), and the
# Q16 alternative is printed as plain "OR" (no "(ii)" label)
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "chemistry_2024_25_s2.py")).read()
for bad in (r"\ce{-COO-}", r"\ce{-NH3+}"):
    assert bad not in _src, f"charge rendered as bond: {bad}"
assert 'Q("16 OR"' in _src and 'Q("16(ii) OR"' not in _src
print("ok  review text checks")
done()
