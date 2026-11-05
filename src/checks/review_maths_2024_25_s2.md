# Review — maths_2024_25_s2 (Heritage Pre-Board 2024-25, Set 2, Mathematics)

Independent reviewer. All 8 pages rendered at 200 dpi (/var/tmp/pbrev-rev-maths2425b/p-*.png) and compared
item by item; dense areas (19(ii), 19(iv)/(v), Q14 table) cropped and zoomed. Every kept item solved
independently before reading the module's answer.

## Findings (fixed)

1. **Section B / C headings: invented marks (transcription).** The SEC notes read "Question 15 [5]" and
   "Question 19 [5]"; the paper prints no mark against Q15 or Q19 (only Q1 carries [15]). Removed the "[5]".
2. **19(ii) note (answer / presentation).** Re-read the printed function at 2× zoom: it is exactly
   C(x) = 0.0001x³ − 0.01x² − 20x + 3500 (minus before 0.01x², minus before 20x, plus 3500). So MC(200) = 12 − 4 − 20 = −12
   really is what the paper's function gives; the writer's reading is right. The note was reworded into a
   `note` paragraph that says the function is transcribed as printed, that a negative MC is unrealistic
   (the function is presumably mis-set), and that the answer (c) MC(200) is unaffected because the question
   asks only which expression approximates the cost of the 201st toy.
3. **Checks extended.** `maths_2024_25_s2_check.py` now also asserts the section totals (A 65, B 15, C 15,
   counting each OR pair once) and A + B = A + C = 80 — which is what justifies the inferred 4 marks on
   Q18, Q21 and Q22. 73 checks pass.

## Items specifically asked about

- **19(ii)** — coefficients and signs confirmed (see 2). Answer (c) MC(200) correct.
- **19(iv) exclusion** — kept excluded. The question asks for p = R(x)/x = 4x² + x/5 + 1 at x = 100 (₹40021):
  average revenue, no differentiation. The ISC 2027 syllabus lists no cost/revenue functions at all; the
  settled rule keeps only calculus-based cost/revenue items, and `maths_2025_26.py` likewise excluded its
  non-calculus cost-function item (19(iv)). Consistent.
- **Q14 p, q** — table re-read: p at (card 2 = 1, card 1 = 2), (2, 3), (3, 4); q at (3, 1), (4, 2). So p = 1, q = 2;
  distribution 1/4, 3/8, 1/4, 1/8; P(S ≤ 2) = 7/8; E(S) = 5/4. All correct.
- **1(x)** — A, B re-read: A = [[−3, 2], [−5, 4]], B = [[4, −2], [5, −3]]. AB = BA = −2I (B = −2A⁻¹). Reason true
  (induction) and explains the Assertion → (a). Correct.
- **1(xi)** — a(dy/dx)² + b(dx/dy) = c, clearing 1/p gives ap³ − cp + b = 0, degree 3; Reason is the definition of
  degree including "can be expressed as polynomial" → (a). Correct.
- **Missing marks Q18, Q21, Q22** — confirmed no bracket is printed against any of them. Section B: 5 + 2 + 4 + Q18
  = 15 ⇒ Q18 = 4. Section C: 5 + 2 + Q21 + Q22 = 15; 4 + 4 is the only split consistent with the instructions
  (internal choice in one 4-mark question per section) and the ISC pattern. Notes kept; now machine-checked.

## Transcription — checked correct
Instructions (all 13 lines); Q1(i)–(xv) stems and every option; Q1(v) four graphs and captions; Q2; Q3 and OR
(determinant rows qr rp pq / 5 5 5 / p(q+r) q(r+p) r(p+q)); Q4; Q5 and OR; Q6; Q7 and OR; Q8; Q9; Q10 and OR
(gem table 1/2, 2/3, 3/1); Q11 and OR with both figures; Q12; Q13 and OR; Q14 (both tables); Q15(i)–(v);
Q16 and OR; Q17 and OR (all coordinates incl. Q(43/29, 77/29, 9/29)); Q18; Q19(i)–(v); Q20 and OR; Q21 (data table);
Q22 (machine table, 12 h / 10 h, ₹3000 / ₹4000). No discrepancies besides finding 1.

## Filter — checked
Excluded 19(i), 19(iii), Q21 (correlation/regression — not in ISC 2027) and 19(iv) (see above): correct.
Kept Section B (vectors, 3-D, area — all in units 4, 5, 3(iv)), 19(ii), 19(v), Q20, Q20 OR (derivative-based,
Applications of Derivatives per settled rule), Q22 (LPP, unit 6). 1(xi) and Q13 Differential Equations are in
the 2027 calculus unit. No wrongly kept or wrongly excluded item.

## Answers — independently solved, all correct
1(i) c; 1(ii) c; 1(iii) d; 1(iv) c (126/8568); 1(v) d; 1(vi) b; 1(vii) d; 1(viii) b; 1(ix) d; 1(x) a; 1(xi) a;
1(xii) 81; 1(xiii) 1/x − 1/x²; 1(xiv) 36; 1(xv) 0.6976; Q2 x = 1; Q3 0 (R3 → R3 + R1 valid); Q3 OR k = 6;
Q4 bijection; Q5 (−1, −2); Q5 OR −cot x − cosec x + C; Q6 11/26; Q7 proof (steps valid, division by y′ ≠ 0 noted);
Q7 OR k = −3; Q8 proof (cos ≥ 0 on principal range justified, squaring direction valid);
Q9 x² sin x + 2x cos x − 2 sin x + C; Q10 1/4, 3/4, 3/256; Q10 OR 18/53; Q11 x = 4(6+√3)/11, y = (30−6√3)/11,
A″ < 0; Q11 OR h:2r = π:(π+2), S″ > 0; Q12 66, 22, 12 (|A| = 5, all nine cofactors re-derived);
Q13 2e^{x/y} + log|y| = 2; Q13 OR π/(3√3); Q14 as above; Q15 (i) a, (ii) d, (iii) 3, (iv) 7/5, (v) 2;
Q16 proof; Q16 OR 0 < x < 2; Q17 2x + 3y + 5z = 8 (cross product re-done); Q17 OR 3x + 2y + 4z = 11,
(x−2)/3 = (y−3)/2 = (z−1)/4, 5/√29; Q18 a = 1/9; 19(ii) c; 19(v) 4x − 7/2; Q20 C = x² + 5x + 36, x > 6;
Q20 OR x = 50; Q22 (8, 2), ₹32000. Recall panels read: all relevant and correct.

## Figures — rendered and checked, all correct
fig_q1v_graphs (four panels match the printed ones and captions); fig_q5_tangent (roots −2.41, 0.41 and vertex to
scale); fig_q10or_tree (1/3 and 2/3, 3/5, 1/2); fig_q11_window; fig_q11_window_ans (shared side dashed, perimeter
3x + 2y); fig_q11or_halfcyl (r from centre, h along the length, hidden edges dashed); fig_q14_dist (heights to
scale, mean 1.25); fig_q15i_par (a − b from B to A, a + b from O to C); fig_q17or_tower (all labels as printed);
fig_q18_area (meet at (9, 9), √ branch above parabola); fig_q20_ac (scale checked at x = 1.6, 6, 14);
fig_q22_lpp (corners, origin side, Z = 32000 slope −3/4 touching only P).

## Page
`python3 src/build.py maths_2024_25_s2` → built, no ERROR (kept 49, excluded 4, figures 12).
`preview.py --page maths/2024-25-set-2.html` → 28 slices read: KaTeX renders throughout, no raw delimiters,
no overflow, figures placed in the right questions, excluded list at the end.

## Summary
Items checked: 53 (49 kept, 4 excluded) + 12 figures + page.
Errors: transcription 1 (invented "[5]" on Q15/Q19 headings); filter 0; answer 0 (19(ii) note clarified);
figure 0; layout 0. Unresolved: none. The paper's 19(ii) cost function gives a negative MC at x = 200 as
printed; noted on the slide, answer unaffected.
