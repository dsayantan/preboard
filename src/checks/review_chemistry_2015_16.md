# Independent review — chemistry_2015_16 and chemistry_2016_17

Reviewer did not write these modules. Sources rendered at 150 dpi (and 3(b) of 2015-16 at 400 dpi), every
question compared with the module; syllabus `Chemistry/Syllabus/ISC-2027.pdf` read (Class XII theory and
practical); answers re-solved independently; all 12 figures rendered and inspected; both pages rendered
and every slice inspected. Checks: `chemistry_2015_16_check.py`, `chemistry_2016_17_check.py` pass
(numbers + 50 / all equations atom- and charge-balanced).

## Findings and changes

| Module | Item | Kind | What was wrong | Change |
|---|---|---|---|---|
| 2015-16 | 3(d) CaC₂O₄ dissolves in dil. HCl | filter | Excluded as ionic equilibrium, but it is the standard observation in the 2027 practical **oxalate** test (white CaC₂O₄ insoluble in acetic acid, soluble in dil. HCl), and the paper kept the parallel ZnS/Group IV item of 2016-17 on the same grounds | Kept, answered (weak acid H₂C₂O₄ formed, ionic product < K_sp), topic "Practical: qualitative analysis (oxalate)"; equations pass the balance check |
| 2015-16 | 1(c)(ii) answer, box and recall | layout/answer | `\ce{CH3CO-}` / `\ce{CH3CH(OH)-}` render the trailing dash as a negative **charge** (CH₃CO⁻) | `\bond{-}` used; renders as a bond |
| 2015-16 | 10(b)(ii) | layout | same CH₃CO⁻ rendering | same fix |
| 2015-16 | 8(a)(i) note | layout | raw-string `\"` printed literally: `[Printed \"acetaldanilide\"…]` | curly quotes entity |
| 2015-16 | 7(a)(iii) recall | layout | half-equation overflowed the recall panel | split over lines |
| 2015-16 | fig_azeotropes | figure | legend "vapour" collided with the B end-label | legend moved between panels |
| 2015-16 | fig_ester_mech | figure | C–OH₂⁺ curly arrowhead covered the + charge, so the leaving group read as neutral OH₂ | arrow redrawn bond → O |
| 2015-16 | fig_ag_conc_cell, fig_azeotropes | figure (minor) | KNO3 / HNO3 without subscript | ₃ |

No transcription errors found in either paper; no answer errors found.

## Judgement calls settled against the syllabus wording

- 2015-16 2(a)(ii) acetic vs nitric acid pH — **keep**: practical 5, "Comparison of pH of the solutions of strong and weak acids of the same concentration."
- 2015-16 2(c) law of mass action — **keep**: Chemical Kinetics (iii) "Law of mass Action: statement and meaning of active mass. Explanation with an example". Answer framed as rate law, matching (iv).
- 2015-16 7(a)(iii) KI + acidified KMnO₄ — **keep**: d-block (iii) "Oxidising nature in acidic [FeSO₄, (COOH)₂.2H₂O, KI]".
- 2016-17 1(c)(v) ZnS from ammoniacal H₂S — **keep**: practical 7, Group IV Zn²⁺ with the NH₄Cl/NH₄OH buffer note; the question is exactly why Zn²⁺ falls in Group IV.
- 2016-17 1(a)(i) common-ion effect on calcium oxalate — stays excluded (a pure common-ion/K_sp concept; no practical step uses it). Distinct from 2015-16 3(d), which is the oxalate confirmatory observation.

## Exclusions confirmed (none of these appears in the Class XII unit list or the practical list)

Chemical equilibrium (K near unity; K_p–K_c) · ionic equilibrium: pH from [OH⁻] (practical has pH-paper only, no calculation), buffers (dilution; Henderson), K_sp of BaSO₄, Ostwald's dilution law · Lewis acids/bases (3 items) · Wöhler's synthesis (2) · solid state (NaCl geometry ×2, point defects, CsCl density, Cu coordination, ferrimagnetism, NaCl unit cell) · interhalogens (IF₇, ClF₃, reactivity) · AgNO₃ preparation, AgBr photography, AgNO₃ + thiosulphate (d-block compounds limited to K₂Cr₂O₇ and KMnO₄) · ozone (×2), H₂O₂, chlorine + hot NaOH · xenon oxyfluorides · polymers (×3; only a project topic) · metallurgy (Cu matte, cyanide process).

## Doubtful points settled

- 2016-17 Q8(a) marks: printed brackets sit one line low ((ii)[2], (iii)[1], (iv)[1], then [2] between (iv) and (b)); (b) and (c) each carry their own [2] on their own lines, so the stray [2] belongs to (iv) and (i) has lost its bracket. The module's reading (2,1,1,2 = 6, question total 10) is the only one that totals; the note stays.
- 2015-16 1(d)(i) and 2(a)(i) "from aqueous solution": treated as Faraday-law data with a note that Ba/Al are not actually deposited from water — correct handling.
- 2015-16 3(b): re-read at 400 dpi — 0.550 g, 0.045 g, 157 °C, 178.4 °C, K_f 37.70, 93.46 % / 6.54 % are all as printed; no digit misread. M = 144.1 vs C₁₂H₁₀ = 154 (n = 1.87 → 2) is a defect of the paper's data; the note says so. Answer stands.
- 2016-17 3(a)(ii): 298–308 K assumption is the conventional meaning of "temperature coefficient"; E_a = 10.2 kcal (42.7 kJ) mol⁻¹ rechecked (ln form agrees within 0.1 %); the note flags the assumption.

## Items checked and correct (answers re-derived)

2015-16: 1(a)(i),(iii),(iv),(v); 1(b)(i),(iii),(iv),(v); 1(c)(ii)–(v) (κ = 1.30×10⁻³ S cm⁻¹); 1(d)(i) 0.5 mol, (iii) (b), (iv) (c), (vi) (b); 2(a)(i) 1.0×10⁻³ N; 2(a)(ii); 2(b) z = 4; 2(c); 3(b); 3(c); 4(b) 0.118 V, electrons dilute → concentrated; 4(c) X = 0.80 M, Y = 0.20 M; 4(d)(ii),(iii); 5(a)–(c); 6(a),(b); 7(a)(iii); 8(a)(i)–(iii); 8(b)(i)–(iv); 8(c); 9(a) phenol/salicylic/benzoic/benzene; 9(b); 9(c)(i)–(iii) (glycerol, formic acid); 10(a) toluene…nitrobenzene; 10(b)(i)–(iv); 10(c)(i),(iii).
2016-17: 1(a)(ii)–(v); 1(b)(i),(iv),(v); 1(c)(i),(ii),(iii),(v); 1(d)(i) 4, (v) RCN; 2(a)(i) 299.5, (ii); 2(c)(i) 8.01×10⁻²⁰ C; 3(a)(i) 390.6, (ii); 3(c); 3(d) 0.04 m; 4(a) 0.751 V; 4(b)(i); 5(a)–(c); 6(a)(ii); 8(a)(i)–(iv); 8(b); 8(c); 9(a); 9(b) propanal → … → N-methylpropan-1-amine; 9(c); 10(a)(i)–(iv); 10(b); 10(c).

## Figures checked and correct

- fig_co_en2cl2_optical: Cl–Cl cis; each en spans two cis sites (back–right, left–bottom in I); II is the exact x-mirror; no mirror plane in either — enantiomers.
- fig_cof6_cft: e_g above t_2g, t_2g⁴e_g², 4 unpaired. fig_fecl4_cft: e below t₂ (e farther from barycentre than t₂, 3:2), e²t₂³, 5 unpaired.
- fig_fecn6_vbt: 3d⁵ → ↑↓ ↑↓ ↑ + 2 ligand pairs, d²sp³, 1 unpaired. fig_ni_vbt: [NiCl₄]²⁻ sp³ 2 unpaired; [Ni(CN)₄]²⁻ four paired d, one d + 4s + two 4p = dsp², diamagnetic.
- fig_azeotropes: vapour (dew) curve above liquid in both panels, touching at the extremum; +ve deviation → minimum b.p., −ve → maximum b.p.
- fig_ag_conc_cell: anode in 0.001 M (−), cathode 0.1 M (+), electrons left → right, KNO₃ bridge.
- fig_ester_mech (after fix): arrows O→H⁺, ethanol O→C⁺, OH lone pair → C=O, C–OH₂⁺ bond → O.
- fig_glucose_structures: Fischer OH R,L,R,R; Haworth C2 OH down, C3 up, C4 down, CH₂OH up; α C1-OH down (trans to CH₂OH), β up.
- fig_pt_cis_trans, fig_arrhenius_plot (log k vs 1/T, negative slope = −E_a/2.303R, intercept log A), fig_amino_acid_forms (cation → cathode, anion → anode).

## Summary

Items checked: 2015-16 62 (now 47 kept / 15 excluded; was 46 / 16 before 3(d) was restored), 2016-17 59 (38 kept / 21 excluded). 12 figures.
Errors by kind: transcription 0 · filter 1 (3(d) wrongly excluded) · answer 0 (2 notational: CH₃CO⁻ rendered as an anion) · figure 3 (legend collision, hidden charge, subscripts) · layout 3 (literal `\"`, recall overflow, the ce-dash rendering). Unresolved: none; the camphor data defect is the paper's own.
