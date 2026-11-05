# Review: maths_2016_17 (Heritage Pre-Board 2016-17, Mathematics)

Reviewer: independent agent (not the writer). Source: all 4 pages rendered at 150 dpi, dense spots at 400/600 dpi.
Syllabus: Maths/Syllabus/ISC-2027.pdf, Class XII theory section (pp. 8-13) read.

## Findings and changes
- 13(b) [answer note]: answer is correct for the printed prices (C(800,0), Rs 4; no positive-rice minimum, verified:
  Z >= 4 + 0.01y on the region). Added to the note that with prices where neither food dominates (e.g. wheat Rs 4/kg,
  rice Rs 6/kg) the optimum is the mixed corner B (400 g wheat, 200 g rice) at Rs 2.80, which is what the question's
  last line evidently expects. Check extended ("13b textbook prices", "13b textbook min").
- 15(a) [transcription note]: note said both price and weight columns were shifted; on the image the base-price column
  is aligned with the commodities and only the current-price and weight columns are shifted one row up (20.00 / 40
  sit in the header row). Note reworded. Values as read were already right. (Excluded item.)
- 6(b) [transcription note]: at 600 dpi the mark after y is faint, but the gap between y and "=" is the width of a
  superscript (no such gap where there is no exponent elsewhere on the page), supporting the y^2 reading. Note now
  states this evidence. Both readings remain worked; both figures correct.
- 3(b) [check]: added a sympy check that the RHS is defined only for x <= 0 or x >= 1 (x = 2 inside).

## Writer's doubts — settled
- 6(b): y^2 = 2x - x^2 confirmed as the better reading (see above). Kept main answer pi/4 - 1/2, alternative 1/6.
- 13(b): "0.5gm of proteins" (second) confirmed on the image; misprint for carbohydrates is the only sensible reading.
  Prices Rs 5/kg and Rs 20/kg confirmed. Answer stands; note extended.
- 12(b): ISC 2027 says "Random variable and its probability distribution, mean of random variable" — no variance.
  Question kept (distribution and mean are in syllabus); SD shown with the existing note. Agree.
- 4(a) Lagrange's MVT: Applications of Derivatives lists rate of change, increasing/decreasing, tangent/normal,
  maxima/minima only; no Rolle/LMVT anywhere in Class XII. Exclusion correct.
- 10(b) scalar triple product: Vector Algebra lists dot and cross product (and their properties/applications) only;
  no box product / coplanarity by [a b c]; 3-D unit has no triple product either. Exclusion correct.
- 3(a) Boolean algebra: absent from the Class XII (and Class XI) syllabus. Exclusion correct.

## Items checked and found correct
- Transcription of all 38 items against the page images: wording, numbers, marks, numbering, order (3(b) before 3(a)
  as printed), intro, section notes, both tables. Correct.
- Exclusions verified against the syllabus wording: 1(c), 4(b) conics (Class XI); 1(d) limits (Class XI "Limits and
  Derivatives"; no limits/L'Hospital in XII); 1(g), 7(a), 7(b) regression/Spearman (absent); 1(h), 9(a) complex
  numbers (Class XI); 3(a); 4(a); 10(a) ("Proofs of geometrical theorems by using Vector algebra are excluded");
  10(b); 13(a), 14(a), 14(b), 15(a), 15(b) commerce/statistics (absent; Unit 6 is Linear Programming only).
- Answers solved independently and compared step by step: 1(a) P, Q; 1(b) tan^-1 11/2; 1(e) -x cot(x/2)+C;
  1(f) pi/4; 1(i) 105/221; 1(j) separation correct; 2(a) R1 sum, column ops, expansion valid; 2(b) all nine
  cofactors, A^-1, (1,2,5); 3(b) both cases, x = 2 only; 5(a); 5(b) 1000/(27 pi); 6(a) sqrt2 sin^-1(sin x - cos x);
  6(b); 8(a) 55/221, 1/51; 8(b) 4/7; 9(b) x^2+y^2=2x; 11(a) 3 sqrt30; 11(b) 35x+7y-7z=45; 12(a) 55/118;
  12(b) distribution, mean 3/4, SD 3/4 (= sqrt(npq)); 13(b). All correct; recall panels relevant and correct.
- Figures (rendered, read): fig_q6b_circle — centre (1,0), r 1, segment above chord OP; fig_q6b_parabola — roots 0,2,
  vertex (1,1) on y = x, to scale; fig_q13b_lpp — intercepts, B(400,200), region on far side of both lines,
  dashed x+4y=800 through C and (0,200). All correct, labels clear.
- Check script: 51 checks pass. Build: no ERROR (kept 21, excluded 17, figures 3). Page: all 15 slices read; math
  renders, no overflow, figures placed correctly.

## Summary
Items checked 38 (21 kept, 17 excluded). Errors: transcription 0 (one inaccurate editorial note fixed, 15(a));
filter 0; answer 0 (one note extended, 13(b)); figure 0; layout 0. Unresolved: none.

## Follow-up (coordinator)
- 14(b) restored: marginal cost / marginal average cost is differentiation (rate of change, quotient rule), in the 2027 syllabus — same rule the 2013-14/2015-16 review applied to cost-function questions. Answer added; sympy check added (MC = x^2+6x-7, MAC identity).
- COMMERCE exclusion wording changed to "Financial mathematics" for 13(a), 14(a); 15(a)/(b) index numbers and moving averages unchanged.
