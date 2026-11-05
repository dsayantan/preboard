# Independent review — maths_2024_25_s1 (Heritage Pre-Board 2024-25, Set 1, Mathematics)

Reviewer worked from the page images (`pdftoppm -r 200`, all 9 pages; page 9 is blank), the ISC 2027
syllabus (`Maths/Syllabus/ISC-2027.pdf`), and an independent sympy pass
(`/var/tmp/pbrev-rev-maths2425a/ind.py`) before reading the given answers.

## Findings (fixed)

1. **Q10 — layout.** The Bayes display (general formula + substitution + 14/29 on one line) overflowed the
   answer column: the final "= 14/29" was clipped at the right edge. Split into two display lines.
   Check `10-display-split` added (verifies no single display holds both the formula and 14/29), plus
   `10-bayes` recomputing 14/29 with exact fractions.
2. **Q19(iii) — answer wording (minor).** Statement 1 as printed omits "linear"; the answer silently read it as
   the linearity assumption. Added one sentence saying so, so the student sees why (c) is still the key.

## Judgement calls re-checked against the image

- **1(iv)** Image confirmed: Reason ends "Hence, or otherwise, the degree … is not defined." Degree is 2
  (cube/square away the 3/2 power), so Assertion false; only option consistent with a false Assertion is
  (d). Writer's (d) with the note on the contradictory last sentence — accepted.
- **Q2** Image confirmed: z = e^{−cos⁻¹x} is given and only d²y/dx² asked. Answer for y alone re-derived
  (sympy: difference 0); the note's y/z = e^{π/2} reading is correct. Accepted.
- **Q12** Image confirmed: "when y(π/4) = 1" (bold). Particular solution as printed
  cot(y/x) = log|4x/π| + cot(4/π) verified; general solution verified by substitution into the DE (sympy 0).
  Note offering the textbook intent (y = π/4 at x = 1 → cot(y/x) = log|ex|) correct. Accepted.
- **Q22** Image confirmed: "x ≤ 0, y ≤ 0". Note's claim (printed version: max 0 at origin) correct; intended
  version Z_max = 410 at (40, 30), corners O, A(60,0), B(50,20), C(40,30), D(0,50) all verified. Accepted.
- **Q19(iii)** Image confirmed (both statements as transcribed). (c) is the intended key; see finding 2.

## Transcription (every item compared word for word with the image)

Instructions, Section headings, 1(i)–1(xv), Q2, Q2 OR, Q3, Q4, Q5, Q5 OR, Q6, Q7, Q8, Q9, Q9 OR, Q10, Q10 OR,
Q11, Q12, Q12 OR, Q13, Q13 OR, Q14, Q15(i)–(v), Q16, Q16 OR, Q17, Q17 OR, Q18, Q19(i)–(v), Q20, Q20 OR,
Q21, Q21 OR, Q22 — all match (values, signs, options, marks, numbering; printed slips such as "scaler",
"atleast", "(iii) & (v)" kept as printed). No errors found.

## Filter

- Kept items all inside ISC 2027 (Relations & Functions, ITF, Matrices/Determinants, Continuity &
  Differentiability, Applications of Derivatives, Integrals, Application of Integrals, Differential Equations
  — homogeneous first-order first-degree listed, Vectors, 3-D incl. planes, LPP, Probability incl. Bayes and
  random variable/mean). Section C calculus-based cost/revenue (19(i), 19(v), Q20, Q20 OR) kept per the
  settled decision.
- Excluded 19(ii), 19(iv), Q21, Q21 OR — correlation/regression, not in the 2027 syllabus. Correct.

## Answers (independently solved; all agree)

1(i) 9 (b) ✓ · 1(ii) 0 (c) ✓ · 1(iii) e^{13π/18} (b) ✓ · 1(iv) (d) ✓ · 1(v) 64/361 (b) ✓ · 1(vi) 0 (d) ✓ ·
1(vii) (d) ✓ · 1(viii) 1 (b) ✓ · 1(ix) (c) ✓ · 1(x) (a) ✓ · 1(xi) 2/7 ✓ · 1(xii) 3, 3/2 ✓ · 1(xiii)
transitive only ✓ · 1(xiv) graph (3) ✓ · 1(xv) 3/28 ✓ · Q2 ✓ · Q2 OR a = 1/27, f''(1) = 20/27 ✓ · Q3 4 ✓ ·
Q4 (4, 4) ✓ · Q5 2√tan x ✓ · Q5 OR eˣ/(1+x²) ✓ · Q6 x = 5 (−5 rejected) ✓ · Q7 proof steps valid ✓ ·
Q8 ½(x cos⁻¹x − √(1−x²)) (derivative checked numerically) ✓ · Q9 inc (0,1),(2,5), dec (1,2) ✓ · Q9 OR
(sympy 0) ✓ · Q10 14/29 ✓ · Q10 OR 0.49 ✓ · Q11 (1, 2, 3), adj A checked ✓ · Q12 ✓ · Q12 OR −(π/2)log 2 ✓ ·
Q13 AB = 4/√5, T = (4+√5)/6 h ✓, T'' > 0 ✓ · Q13 OR h = 432/r², S = 2πr² + 864π/r, r = 6, 216π ✓ ·
Q14 3/5, {14,15,16,17,19}, table, 4/7, 16.4 ✓ · Q15(i) (a) ✓ · (ii) −1 ✓ · (iii) −1 ✓ · (iv) 3 ✓ · (v) ✓ ·
Q16 π/4, 3π/4 ✓ · Q16 OR 300 ✓ · Q17 d = 12, −48 ✓ · Q17 OR direction (2,1,−2) ✓ · Q18 21/2 ✓ ·
Q19(i) 6 ✓ · Q19(iii) (c) ✓ · Q19(v) 12, 25 ✓ · Q20 ₹35, P = 626000 ✓ · Q20 OR 40 ✓ · Q22 410 at (40,30) ✓.
Recall panels read for every item: correct and relevant.

## Figures (all 14 rendered and read)

fig_q1vii_graph (matches printed |x| graph and labels) ✓ · fig_q1xiv_graphs (four shapes as printed) ✓ ·
fig_q1xiv_ans (x = k meets graph 3 three times) ✓ · fig_q2or_coaster ✓ · fig_q2or_ans (zeros −9, −1, 3;
(0, −1)) ✓ · fig_q3_abssin ✓ · fig_q4_tangent (curve concave, tangent x+y = 8 at (4,4), intercept 8) ✓ ·
fig_q9_growth (max (1,6), min (2,5)) ✓ · fig_q10_tree (0.28, 0.30) ✓ · fig_q13_swim (A, B, H, S as printed) ✓
· fig_q13_geometry ✓ · fig_q13or_cans ✓ · fig_q18_area (no intersection, (3,11), (3,3)) ✓ · fig_q22_lpp
(lines by intercepts, region OABCD on origin side, iso-profit line through (0,58.6)/(82,0) touches only C) ✓.

## Page

Built (`kept 50, excluded 4, figures 14`, no ERROR); all 29 preview slices read before and after the fix.
KaTeX renders throughout; only overflow was Q10 (fixed). Checks: 66 passed.
