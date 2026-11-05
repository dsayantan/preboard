# Review: maths_2025_26 (Heritage Pre-Board 2025-26, Mathematics, SET-1)

Reviewer: an independent agent, not the writer. I rendered every page of the source (9 pages: 7 printed, 2 blank) at 110 dpi and the dense spots (1(x) graph, Q5, 16(OR)) at 400 dpi.
Syllabus: Maths/Syllabus/ISC-2027.pdf, Class XII units. I applied the site-wide Section C rule from review_maths_2013_14.md and review_maths_2016_17.md.

## Findings and changes
- **19(i) [filter]**: this was wrongly excluded as "commerce". Marginal revenue is dR/dx, a rate of change (Applications of Derivatives). I restored it and gave a full answer: R = 1500x − 2x² − x³, MR = 1500 − 4x − 3x², which is 1160 at x = 10. Answer (a).
- **Q20 [filter]**: this was wrongly excluded (marginal revenue). I restored it. p = (100 − x)/4, R = (100x − x²)/4, MR = (100 − 2x)/4 = 0 gives x = 50, and R'' < 0.
- **Q20 (OR) [filter]**: this was wrongly excluded (average cost). It asks where a function decreases, which is calculus. I restored it. AC = 200/x + 20 − x/2, so d(AC)/dx = −200/x² − ½ < 0 for every x > 0, and AC falls for all x > 0. A note adds that C is realistic only while MC = 20 − x > 0.
- **19(iii) [filter]**: break-even. The paper gives C(x) explicitly, so the only step is to form R = 280x and solve R(x) = C(x), i.e. 70x ≥ 7000. That is plain algebra with no commerce theory, so I **kept** it as an application of a linear function, as the coordinator's rule allows. Answer: at least 100 items.
- **19(iv) [filter, still excluded]**: building a cost function from fixed and variable costs needs no calculus at all; it is pure old Section C cost-and-revenue vocabulary. I kept the exclusion and reworded it in the shared form: "Commerce application without calculus (forming a cost function from fixed and variable costs) — not in the ISC 2027 Class XII syllabus; of the old Section C only Linear Programming (and calculus applications) remain."
- **COMMERCE wording [filter]**: I replaced the old "Section C application of calculus … abolished" text, which contradicted the rule, with the wording above.
- **Section C note and intro note**: rewritten to list what is kept and what is excluded, and why.
- **1(x) [answer]**: the answer said a line y = k with "small k > 0" cuts the curve at four points. That is wrong: a small k gives three. Four needs k between the right-hand dip and the lower hump (k = 0.6 in the figure). Text corrected. The check now asserts 4 crossings at k = 0.6 and 3 at k = 0.1 on the plotted curve.
- **Q16 [figure]**: the qfig had a G and an AG line that are not in the printed figure, and the AG line lay almost on top of AC. I removed G from the qfig, which now matches the print. I added an afig `fig_q16_centroid` with C moved back-left so that AG is clearly separate, G at the centroid of the drawn BCD, letters on the figure and the coordinates (with G(3,2,3)) in a caption line. No labels collide. The check asserts G = (3,2,3).
- **16(OR) [transcription note]**: at 400 dpi the hat sits over "3x" (\(\widehat{3x}j\)), not over "3xj". Note corrected. The reading 3x ĵ is unchanged.
- **1(xiv) [answer note]**: added a note on the NCERT convention (continuity is judged only at points of the domain). The paper plainly intends "at every integer, so infinitely many", and the boxed answer stands.
- **2(OR) [answer note]**: added that some keys print a < −1. At a = −1, f' = 1 + cos x ≥ 0 with isolated zeros, so f is still strictly increasing and a ≤ −1 is correct. Added a check for this.

## Doubts from the brief, settled from the images
- Q5: the minus sign in the denominator is confirmed at 400 dpi. As printed, the integral diverges at x = 5/2. I kept the solution of the evident "+" version (5/2) and the note.
- Q7: the identity holds for 0 < x ≤ 1. x = 1 works (cot(π/2) = 0 gives cos 0 = 1). For −1 ≤ x < 0 the left side equals −x. The note and the domain restriction in the answer are correct.
- 1(ix): the leading "If f(x) =" is a misprint; ignoring it is right. Answer (d) 1/(1 − x) verified.
- 12(OR)(c): the question states the domain t ≥ 0 and asks "true or false? Justify", so the intended catch is the domain. **False**: h is increasing on [0, 3/14). The answer also explains that the bare quadratic increases on (−∞, 3/14). Kept.
- 2(OR): a ≤ −1 (see above).
- 1(xiv): every integer, infinitely many points (see above).

## Items checked and found correct
- Transcription of every item against the images (intro, section headings, all wording, numbers, options, marks, the OR pairs, the Q11 and Q21 tables, the empty seventh column of Q21): correct apart from the 16(OR) note above.
- Exclusions verified: 19(ii), 19(v) and Q21 are regression, which is absent from ISC 2027.
- I solved every answer independently and compared it step by step: 1(i)–(xv); 2 and 2(OR); 3 (x = 3, −5); 4 (tan⁻¹(35/13)); 5 and 5(OR); 6 (y = 0); 7; 8 and 8(OR); 9 (sympy differentiation confirms the antiderivative); 10 (25/62); 10(OR) (1/4, 3/4); 11 (2, 3, 4; cofactors and adj rechecked); 12 (r = 7/2, h = 7); 12(OR) (1, False, 65/56 at 3/14); 13 (0.006 / 0.092 / 0.398 / 0.504, mean 2.4); 14 (xy cos(y/x) = −π, verified by implicit differentiation against the ODE); 14(OR) (π²/4, checked numerically); 15(i)–(v); 16 (√11, 3√10); 16(OR) (0 < x < 2); 17 (5√21/2); 17(OR) (2x + 3y + 5z = 8); 18 (13); 22 (12, 6 gives 18); 22(OR) (B(20,10), z max 30). All correct. The recall panels are relevant and accurate.
- Figures rendered and read: fig_q1x_curve (matches the printed curve: cusp at O, humps, dips); fig_q1x_ans (four computed intersection dots on the curve); fig_q10_tree (all branch values); fig_q12_cylinder (h on the axis, r on the base, as printed); fig_q12or_path (h(0) = 1, max (3/14, 65/56), root at t = 1); fig_q17_triangle (A above, B-D-C on the line, right angle at D); fig_q18_area (roots 0 and 4, vertex (2,4), (5,−5), shading on [0,4] above the axis and [4,5] below, to scale); fig_q22_lpp (both lines on their intercepts, region on the origin side of both, corners O, (16,0), P(12,6), (0,14) labelled, dashed x + y = 18 through P only); fig_q22or_region and fig_q22or_ans (lines through D/A and C/E, region OABC containing O, B(20,10), dashed z = 30 through B only).
- Check script: 68 checks pass (60 before, plus 8 added: 19i, 19iii, 20, 20or, 16 G, 1x ×2, 2or).
- Build: no ERROR (kept 50, excluded 4, figures 12). Page: all 27 slices read. The maths renders, nothing overflows, figures sit where they belong, and the restored Section C items appear in place with their answers.

## Summary
Items checked: 54 (50 kept, 4 excluded).

Errors found:
- Transcription: 0. One editorial note was inaccurate (16(OR)) and is corrected.
- Filter: 4 items wrongly excluded and now restored: 19(i), 19(iii), Q20, Q20(OR). One exclusion reason reworded (19(iv)).
- Answer: 1 (1(x) intersection count). Two notes added (1(xiv), 2(OR)).
- Figure: 1 (Q16: G was not printed, and AG overlapped AC; split into a qfig and a new afig).
- Layout: 0.

Unresolved: none.

Note for the kit: `preview.py --page` cleans out only the `slice*` files, so `pair*.png` and `full.png` left in the same folder by an earlier run go stale. I deleted them here.
