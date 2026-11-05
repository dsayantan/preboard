# Review: chemistry_2024_25_s2 (Heritage Pre-Board 2024-25, Chemistry, Set 2)

Reviewer: independent agent (not the writer). Source `PreBoard-PYQ/2024-25/SET-2/Chemistry.docx` was converted with
LibreOffice to `/var/tmp/pbrev-rev-chem2425b/Chemistry.pdf` (9 pp). Every page was rendered and read. The doubtful
spots were checked again at 300 dpi and in `word/document.xml`.
Syllabus: `Chemistry/Syllabus/ISC-2027.pdf` (pdftotext, Class XII units searched).

## Findings (fixed)

| item | kind | what was wrong | change |
|---|---|---|---|
| 16 OR | transcription (numbering) | Labelled `16(ii) OR`. The paper prints only "OR" before the alternative and numbers the alternative's own parts (i), (ii), so "(ii)" was invented. (Q9 and Q21 do print (i)/(ii), so their labels stay.) | Renamed `16 OR`. The check script asserts it. |
| 17 | layout/answer rendering | Prose `\ce{-COO-}` and `\ce{-NH3+}` rendered the trailing sign as a bond dash, so "the −COO⁻ is protonated" showed as "−COO−" with no charge. | Changed to `\ce{-COO^-}` and `\ce{-NH3^+}`. Re-rendered and checked. The check script asserts the bad forms are gone. |

## Writer's flagged readings, re-judged against the image

- **1(A)(ii)**: the image (300 dpi) and the docx XML both print `[Co(NH3)5(NO2)]Cl`, with **one** Cl. With the printed formula: CN 6, Co +2. The writer's answer "six; +2" is correct for the printed formula. The note says the familiar compound is `…Cl2` (Co +3), which is right. Kept.
- **1(A)(iv)**: [CuCl4]²⁻. Cu²⁺ is d⁹, so 1 unpaired electron. Cl⁻ is weak field, so the textbook answer is sp³, tetrahedral (both "1" and "tetrahedral" are in the word list). The note on the flattened tetrahedron and square-planar salts is accurate. Kept.
- **1(B)(vii)**: Actinoids form more complexes. The 5f orbitals take part in bonding, the 4f do not. This is the standard NCERT reasoning, so (a) is correct. Kept.
- **Q2**: For 0.01 M H2SO4, N = 0.02. κ = 1.65×10⁻⁴ gives Λeq = 8.25 and Λm = 16.5. So 16.5 is the molar, not the equivalent, conductivity, and the data are not justified. Recomputed; correct.
- **Q21 OR**: Transcription matches (Kf printed "1.86ºC mol⁻¹", and the note on the unit is apt).
  - (a) 0.1322 °C; i = 2.42. Correct.
  - (b) 6×10¹⁰ particles/L, C = 9.96×10⁻¹⁴ M, π = 2.40×10⁻¹² atm (2.43×10⁻⁷ Pa). Correct.
  - (c) Sucrose: ΔTb = 0.05×180/342 = 0.026 °C, so the boiling point is lower. Acetic acid: bp ≈ 118 °C, Kb 3.07, 500 mL ≈ 524 g, ΔTb ≈ 0.33 °C. "No" in both cases. Correct.

## Transcription: checked and correct

The instructions block matches. So do these items: 1(A)(i), (iii), (iv); 1(B)(i)–(vii) (options and order); 1(C) (passage and the three parts); Q3–Q15; Q16(i); Q17–Q21(i). This covers every value, unit, sign and exponent:

- Q5: log k = −3163/T + 11.9.
- Q13: data 2 g/25 g/1.62 K/4.9, 0.15 M/6.8 atm/310 K.
- Q18: the table.
- Q20: the Co misprint "C_O" is noted.
- Q21(i)(b): 6.21 g/24.0 g/68.04/61.7/3.63.

The highlighted words in the docx (yellow) are editorial, not content. The paper prints no diagrams, so no qfig is needed.

## Syllabus filter

There are 0 excluded and 35 kept. Every kept topic is in ISC 2027 Class XII:

- Solutions: azeotropes, colligative properties, van 't Hoff factor, osmotic pressure.
- Electrochemistry: equivalent and molar conductance, Faraday's laws, the lead storage battery, cell emf, ΔG and K.
- Kinetics.
- d- and f-block: lanthanoids and actinoids.
- Coordination: VBT, CFT/CFSE, isomerism, IUPAC.
- Haloalkanes: SOCl2, SN1, Fittig.
- Alcohols/phenols: Dow's, Kolbe's, azo test, nitration and sulphonation of phenol, Williamson.
- Carbonyls: ozonolysis, Rosenmund, Wolff–Kishner, Perkin, benzoin, Cannizzaro.
- Amines: Hofmann, diazotisation, carbylamine.
- Biomolecules: isoelectric point, DNA bases.

All were confirmed by name in the syllabus text. No item touches the settled OUT topics: equilibrium, ionic equilibrium, solid state, p-block, metallurgy, polymers, surface chemistry.

## Answers: solved independently, then compared (all agree)

- 1(A)(i) gram-equivalent; volume.
- 1(A)(iii) ethanal + formaldehyde.
- 1(B):
  - (i) (c), m > p > o.
  - (ii) (d).
  - (iii) (c).
  - (iv) (b).
  - (v) (b), Zn²⁺ d¹⁰.
  - (vi) (b).
- 1(C) third order; 3.125 %; 18 times.
- Q3 propanal, with +I and steric reasoning; the Fehling equation balances (charge and atoms).
- Q4 CH3CN + CH3MgBr, then hydrolysis (balanced); Cl2/FeCl3 then Fittig.
- Q5 Ea 60.6 kJ/mol, k 12.7 min⁻¹, t½ 0.0544 min.
- Q6 benzoic acid → benzamide → aniline (Hofmann; equation balanced).
- Q7 Fe³⁺ d⁵ low spin, d²sp³, 1 unpaired electron: Suhail is right.
- Q8 Williamson; MeMgBr on acetone.
- Q9(a) benzoic acid, then benzene. 6[O] balance checked.
- Q9(b) CH3COCl, then CH3CHO.
- Q9 OR: HCHO, CH3OH, HCOONa, HCOOH.
- Q10 K = 3.4×10³⁵; 202.7 kJ.
- Q11 iodoform (balanced); FeCl3 (balanced including charge).
- Q12 aniline, PhN2Cl, PhI; CH3CN, EtNH2, EtNC.
- Q13 i = 0.504 and 1.78: association vs dissociation; the order is correct.
- Q14 the three name reactions are correct.
- Q15 −1.6Δo(+P) and −0.6Δo.
- Q16 Zn + Cu²⁺, 1.10 V, −212.3 kJ.
- Q16 OR 0.187 mol (10.9 g); the lead-accumulator half-reactions are correct.
- Q17 is correct.
- Q18 first order in each, k = 0.6 L mol⁻¹ min⁻¹ (consistent across all three runs).
- Q19:
  - (a) Dow's process.
  - (b) phenol-2,4-disulphonic acid, then picric acid. Both equations balanced by hand.
  - (c) orange azo dye.
  - (d) Kolbe.
- Q20 diamminechloridonitrito-N-platinum(II); iron(III) hexacyanidoferrate(II); ionisation isomerism; d²sp³ diamagnetic; cis chiral, trans achiral.
- Q21(i) osmotic pressure; M = 148 g/mol; i ≈ 2.

The check script passes (all numbers and balances). Recall panels were read and are correct and relevant.

Minor, left as is: Q15(i) gives the conventional textbook "no ligands, no splitting" account for anhydrous CuSO4. Strictly, sulphate coordinates and the absorption moves to the IR, and the text hedges with "in the visible region". That is acceptable for ISC.

## Figures (11): rendered and checked

- fig_b_cucl4_vbt: d⁹, sp³ boxes (4s + 3×4p). OK.
- fig_b_fecn6_vbt: 2,2,1 + two ligand d; d²sp³ brace; 1 unpaired. OK.
- fig_b_conh36_vbt: d⁶ paired, d²sp³, diamagnetic. OK.
- fig_b_cu_dd: free ion d⁹ unsplit; t2g⁶eg³ with Δo and hν. OK.
- fig_b_mn_cft: low-spin t2g⁴ (one pair); high-spin t2g³eg¹; CFSE labels match the text. OK.
- fig_b_daniell: Zn(−) anode left, Cu(+) cathode right; e⁻ flow Zn→Cu; Cl⁻ toward the anode, K⁺ toward the cathode. OK.
- fig_b_cocl2en2_optical: Cl cis (top/left); each en spans cis positions; the right-hand drawing is an exact mirror reflection. OK.
- fig_b_trans_cocl2en2: Cl trans; both en equatorial; mirror plane as stated. OK.
- fig_b_picric: SO3H at 2,4; NO2 at 2,4,6. OK.
- fig_b_azo: N=N double bond; OH para. OK.
- fig_b_kolbe: COO⁻Na⁺ ortho to OH; acidification. OK.

No label collisions.

## Page

`python3 src/build.py chemistry_2024_25_s2` builds `chemistry/2024-25-set-2.html` (kept 35, excluded 0, figures 11) with no ERROR. All 24 preview slices were read. KaTeX and mhchem render, there is no raw `\(`, nothing overflows, and the figures sit at their placeholders.

## Summary

35 items checked (35 kept, 0 excluded) and 11 figures. Errors found: 2.

- Transcription/numbering: 1 (16 OR label).
- Layout/rendering: 1 (Q17 ionic charges).
- Filter: 0.
- Answer: 0.
- Figure: 0.

Nothing unresolved. The 1(A)(ii) printed formula (one Cl) is a likely setter's slip and is answered as printed, with a note.
