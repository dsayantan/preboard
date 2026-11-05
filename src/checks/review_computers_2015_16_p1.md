# Review — computers_2015_16_p1 (independent reviewer)

Source rendered at 120/300/400 dpi; every item compared with the image; syllabus ISC-2027.pdf (Class XII) read.

## Findings and fixes
- **fig_q13a_mux4 (figure).** The four AND outputs were routed to the OR with lanes [0,1,1,0]: gate 1's
  and gate 2's output wires crossed twice just before the OR (likewise gates 3/4), reading as a tangle/short.
  Changed to lanes [1,0,0,1] (outer gates take the outer lane); re-rendered — no wire crosses another.
- **fig_q13a_block (figure).** S1/S0 select leads poked ~2 units into the MUX body. Now end exactly on the
  sloping bottom edge.
- **Q16 / Q15 Java (layout/comment).** Comment "private-to-class access of A's array" was wrong (arr is not
  private) — reworded; two over-long comments in PackRun shortened. Re-ran: outputs unchanged.

## Checked and correct
- Q1 absorption + truth table. Q2: image shows ↑; read as NAND it is not a tautology (P=Q=0); ∧ reading
  (modus ponens) is the evident intent — note kept, table correct. Q3 = A + D′ ✓. Q4: bars are over (AB) only
  in each bracket (confirmed at 300 dpi) — expression = AB′·A′B = 0, complement 1 ✓. Q5 π(1,3,5), maxterms ✓.
  Q6, Q8 ✓. Q7 third term Ā B C̄ (confirmed) → X = 1 ✓. Q9 ABC/*E/F+ ✓. Q10 base address 4000 ✓ (note fine).
- Q11: recursive call printed `permute`; reading it as ppp is the only traceable reading. Re-ran: 12 lines,
  trace table matches output.
- Q12(a) C′ + A′B + A′D′ + BD′; Q12(b) (B+C)(B+D)(A+C+D′): K-maps Gray order, groups, circuits traced ✓.
- Q13(b) NOR-NOR ✓, Q13(c) XNOR from 4 NORs ✓. Q14(a) = 1 ✓. Q14(b) encoder wiring ✓.
- Q14(c): circuit re-traced at 400 dpi — OR(B,C,D′), OR(D′,C,A), OR(D,C′); C/D crossing has a hop, not a
  join; redrawn figure matches. Out = C′D′ + CD + ABC′ ✓ (truth table checked).
- Q15–Q18, Q20 Java re-run by the check (all outputs regenerated from runs; MIDSORT gives the paper's
  wofelr / toeblru exactly; Q18 prints 44,55,66 and 44,33,22 as the paper's examples).
- Q19(a) tree read from image: 2(7(2,6(5,11)),5(–,9(4,–))); traversals ✓. Q19(b) O(NM) ✓.
- Filter: Q19(c) quick sort exclusion confirmed (sorting named in syllabus is bubble/selection/insertion;
  borderline since unit 14 says "various sorting algorithms", but quick sort is not taught). All other items in:
  interfaces (12b), super (12a), recursion (11), linked-list programs (13b "algorithm and programming"), tree
  traversals (conceptual), Big-O (14). No file handling / wrapper / stream items.
- Page built (no ERROR) and every slice viewed: math renders, figures placed; long code lines scroll (overflow-x:auto).

Items checked 27 (26 kept, 1 excluded). Errors: transcription 0, filter 0, answer 0, figure 2, layout/comment 1.
