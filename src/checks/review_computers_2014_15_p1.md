# Review — computers_2014_15_p1 (independent reviewer)

Source rendered at 110 and 300 dpi (all 8 pages); Q1–2 block, Q7(c) circuit and Q13(b) tree cropped at 300 dpi.

## Findings and changes
- **Q7(a) figure (4:1 MUX, layout/wiring legibility):** the AND0 and AND1 output wires to the OR crossed and ran
  within a few pixels of each other beside the OR, reading as a short. Lanes changed to `[1, 0, 0, 1]` (outer
  gates on the outer lane) — no crossings now. Check added.
- **Q10 Java (answer bug):** n (words in the longest sentence) was counted with the default whitespace
  tokenizer but the rows were filled with delimiters " ,;:?" — a sentence like "a,b c" gives n too small and
  a word is silently dropped. Both now use " ,;:?". Re-run; sample output unchanged. Check added.
- **Q13(c) note (imprecise):** "the outer loop would not run M times" — made exact: literally, if M ≤ N+1 the
  outer loop runs once (O(N)); if M ≥ N+2 it never terminates. Intended answer O(MN) unchanged.
- **Q2(b) exclusion reason (imprecise):** file handling is in the 2027 syllabus as Class XI Unit 11(b), not
  absent. Exclusion kept (not Class XII); reason rewritten.
- **K-maps (shared lib):** cell numbers hidden by rings — fixed (see 2013-14 log).

## Settled doubtful readings
- Q5: the question's "X(A,B,C,D)" is a slip for S(G,T,A,B); answer S = TAB + GAB = AB(G+T), Σ(7,11,15) ✓.
- Q7(c): at 300 dpi the junction dot is on output (1); its branch runs down, crosses the Z line with **no** dot,
  and enters the last AND with (3). So F = XY·(XYZ)′ = XYZ′ as solved. Redrawn figure matches.
- Q3(a) stray comma in `somefun("001001101",5,)` — misprint; 19 and 9 ✓ (re-run).
- Q11: the superclass method is show(); "display( ) method of the super class" ⇒ super.show() ✓.
- Q12: the closing sentence about class Sales is copied from Q11 — note correct. Squeue re-traced (lim 4).
- Q13(c): loop reusing i — see above.

## Items checked and found correct (solved independently first)
1(a) distributive ✓ · 1(b) Y⇒X, ~Y⇒~X ✓ · 1(c) ✓ · 1(d) Σ(0,2,4,5,6,7) ✓ · 1(e) Y + XZ′, dual Y(X+Z′) ✓ ·
2(a) ✓ · 2(c) X = 3 ✓ · 2(d) ✓ · 2(e) a NOT b AND c d AND OR ✓ · 3(a)(b)(c) ✓ · 4(a) CD + BD′ ✓ ·
4(b) (A′+B′)(A′+D)(B+C+D) ✓ · 5 ✓ · 6(a) D = X′Y+XY′, B = (X+Y)(X′+Y)(X′+Y′) ✓ · 6(b) ✓ · 6(c) ✓ ·
7(a) ✓ · 7(b) Π(0,2,3) ✓ · 7(c) ✓ · 8 DigiNumber ✓ · 9 Collection ✓ · 10 ✓ (after fix) · 11 ✓ · 12 ✓ ·
13(a) ✓ · 13(b) internal A,B,C,E,G,H,J; leaves D,K,F,I,L; preorder A B D E H K C F G I J L ✓ (K right of H,
L left of J, H left of E — confirmed on the page image) · 13(c) ✓.
Filter: Q2(b) only exclusion; everything kept is Class XII 2027 (no C++/old-hardware items).

## Figures (every gate traced in the PNG)
fig_q1c_or ✓ · fig_q1e_kmap ✓ · fig_q4a_kmap/circ ✓ · fig_q4b_kmap/circ (A′+B′, A′+D, B+C+D) ✓ ·
fig_q5_kmap/circ ✓ · fig_q6_nand (X′·Y, X·Y′) ✓ · fig_q6c_fa ✓ · fig_q7a_mux (fixed; AND select taps
S1′S0′, S1′S0, S1S0′, S1S0) ✓ · fig_q7c_given vs page ✓ · fig_q7c_answer ✓ · fig_q13a_list ✓ ·
fig_q13b_tree/right ✓.

## Page
Built (kept 29, excluded 1, figures 16, no ERROR). preview.py --page truncates this page at 32000 px (the end
of Q13(b), Q13(c) and the excluded list were cut off); the tail was rendered separately and read. All fine.
Checks: 178, 0 failed; 9 Java programs run.
