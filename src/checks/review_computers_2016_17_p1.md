# Review — computers_2016_17_p1 (independent reviewer)

## Findings and fixes
- **Q6(a) (transcription + answer).** At 600 dpi the paper prints **(A⊕B⊕C)′ = A⊙B⊕C** — the second operator
  is ⊕, not ⊙. The module had A⊙B⊙C and concluded "the paper is wrong / the law fails". As printed the law is
  TRUE: (A⊙B)⊕C = (A⊕B)′⊕C = (A⊕B⊕C)′. Rewrote the question and the answer (truth table with an
  (A⊙B)⊕C column, all 8 rows equal, law verified, one-line reason), recall updated. Check script now asserts the
  printed law holds (and that the ⊙⊙ misreading would not).

## Checked and correct
- 1(a) ST; 1(b); 1(c) π(1,5,6,7) and the four maxterms; 1(d); 1(e) contrapositive ✓.
- 2(a) final/finally (final is syllabus unit 7; finally kept as part of exception handling, unit 5(c) —
  borderline but in); 2(b); 2(c) W = 5 (column major, base at [1][1]); 2(d); 2(e) RPN
  P T Q / G R K + * M / N J − * S / * + L + (hand-derived) ✓.
- Q3 mystery(8) → 0 0 0 : 2 4 8 (re-run) ✓.
- 4(a) B′ + C′D + AC; 4(b) (A+B′)(B+C′+D′)(A′+C+D′); K-maps and circuits traced ✓.
- 5(a) I = EG + FGH, π list, G(E+F)(E+H) ✓. 5(b) truth table matches image row for row; F1 Σ(0,5,7),
  F2 Σ(2,3,5), F3 Σ(1,6,7); decoder figure traced lead by lead (every OR input lands on the right D line; all
  other contacts are plain crossings without dots) ✓.
- 6(b) circuit re-traced at 600 dpi: AND3 inputs are AB (from AND1's output tap) and C — matches redrawn
  figure; F1 = A⊕B⊕C, F2 = AB+BC+CA ✓. 6(c) BCD encoder wiring ✓. 6(d) F = P′a + P′b + ab ✓.
- Q7–Q11 Java re-run by the check; series values 12.333…, 2.7083 hand-checked; Retire PF/gratuity ✓; Pipe
  (input-restricted dequeue) behaviour ✓.
- 12(a) tree read from image: A(B(C(E(–,I),F(–,J)),D(G,H(K,L))),M) — I, J right children; traversals ✓.
  12(b) addList ✓.
- Filter: nothing out of 2027 (no file handling, wrapper/stream, extra sorts; tree item is conceptual).
- Page rebuilt and viewed (6(a) slice re-checked).

Items checked 28 (all kept). Errors: transcription 1, answer 1 (same item), filter 0, figure 0, layout 0.
