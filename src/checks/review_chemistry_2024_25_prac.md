# Review — chemistry_2024_25_prac (Heritage Pre-Board 2024-25, Chemistry Practical)

Source rendered (3 pages) and compared word for word. Syllabus: ISC 2027 practical list (redox titration KMnO₄/ammonium
iron(II) sulphate; organic identification incl. aniline, formaldehyde; carbohydrate tests (glucose); single-salt
analysis with Pb²⁺ and NO₃⁻ in the lists).

## Findings (changed)

- **Q2(b) — answer (identification).** Writer identified C-14 as formaldehyde. The three printed tests (C-14
  *solution* + Fehling's "heat strongly", + Tollens' "heat strongly", + "few drops of caustic soda … heat to boil") are,
  word for word, the school laboratory manual's **glucose** experiment (Experiment 14, as transcribed in
  `class12/Chemistry/src/build_practical_answers.py`); the manual's formaldehyde experiment instead warms in a water bath
  and uses resorcinol/Schiff's. Glucose also explains test (iii): yellow → brown with hot alkali, whereas HCHO gives no
  colour. Rewrote the answer for glucose (carbohydrate — reducing sugar), with balanced gluconate equations for
  Fehling's and Tollens', a note on how test (iii) separates glucose from formaldehyde (and what to report if a pungent,
  colourless result is seen), new topic and recall. Check script: replaced the HCHO equations with the glucose ones
  (balanced) and asserts 2(b) names glucose.
- **Q2(a)(iii) — answer (observation).** Writer left the colour of the NaNO₂/conc. H₂SO₄ test vague ("could not be
  confirmed"). The test is the manual's aniline step, whose recorded observation is a brilliant red dye after water and
  NaOH (diazotisation + coupling). Rewrote the row: reddish-brown, then red/orange-red dye in alkali, no blue/green —
  and stated that (i) and (iii) are what rule out phenol (which also gives a white ppt with bromine water).
- **Q1(ii) — answer (arithmetic consistency).** Shown working uses M₁ = 0.006646 but printed M₂ = 0.035056 (the value
  from the unrounded M₁). 5 × 0.006646 × 21.10 / 20 = **0.035058**; corrected in the working, the strength line and the
  box (strength 13.74 g L⁻¹ and purity 94.8 % unchanged). Check extended to recompute from the printed M₁ and to assert
  the three occurrences.

## Items checked and found correct

- Intro, marks (7 + 4 + 4 + project 10 + file 5 = 30), wording of Q1–Q3 — match the paper.
- Q1 titration realism: KMnO₄ 1.05 g L⁻¹ = 0.006646 M; pure Mohr's salt 14.5 g L⁻¹ would need 22.26 mL for a 20 mL
  pipette; sample titres 21.40 (rough), 21.10, 21.10 (two identical concordant, as ISC requires; no averaging) give
  94.8 % purity — plausible. All burette differences recomputed. Mr 158 and 392 correct. Per-mL formulae
  (0.0016615 V, 0.6513 V, 4.492 V %) recomputed. Upper-meniscus, self-indicator, no warming for Fe²⁺ — correct.
- Q2(a) aniline: (i) dissolves in conc. HCl, no violet colour with FeCl₃ (ISC 2019 Paper 2 used the same test for
  aniline); (ii) white ppt of 2,4,6-tribromoaniline; equations balanced. Identification correct.
- Q3: sample salt Pb(NO₃)₂ — both ions in the 2027 lists; dilute-acid group negative, conc. H₂SO₄ brown NO₂ (paper/Cu),
  sodium-carbonate extract for the wet test (as the syllabus requires), brown-ring test; O.S. in water; Group 0 negative,
  Group I PbCl₂ soluble in hot water, K₂CrO₄ and KI confirmations; group-reagent sequence with H₂S removal and conc. HNO₃
  before Group III, NH₄Cl before NH₄OH — all as the syllabus notes require. Equations balanced.
- No figures in this module (none needed); `chemistry_2024_25_figs.md` already records that.

## Page

Built with no ERROR; all 7 slices read: tables, KaTeX and boxes render, nothing overflows.

Checks: `chemistry_2024_25_prac_check.py` — all pass.
