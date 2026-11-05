# Review — computers_2013_14_p1 (independent reviewer)

Source rendered at 110 and 300 dpi (all 4 pages); tree (FIG:1) and Q3 cropped at 300 dpi.

## Findings and changes
- **Q22(c) transcription note (wrong):** the question carried "[In the original the edge from 3 to 5 is not
  visible in print …]". At 300 dpi the 3–5 edge is clearly printed (5 below-left of 3, 8 below-left of 5).
  Note removed; the tree and the three traversals were already right. Check added (3→5 left, 5→8 left, note gone).
- **Q18 exclusion reason (imprecise):** said file handling "is not in the ISC 2027 syllabus". It *is* in the
  syllabus — as Class XI Unit 11(b) (FileInputStream/FileOutputStream, FileReader/FileWriter). Exclusion kept
  (Class XII Unit 5(c) has only Scanner/Printer), reason rewritten to say it is Class XI.
- **K-map figures (layout, shared lib `computers_a_lib.kmap`):** group rings were drawn over the small cell
  numbers (12/13/15/14 etc. half-hidden). Cell numbers are now drawn last on a white patch. Check added.

## Settled doubtful readings
- Q6 index base: DATA[30][40] is a Java/C declaration ⇒ indices 0..29, 0..39, base = DATA[0][0] ⇒ **2874**
  is the answer the data implies; the 1-based alternative (2710) stays as a note. Recomputed: 1234+4·410 = 2874.
- Q12: code as printed does not compile (Strings, Return, non-static methods); tracing the intended program
  is right. Output "\n z=16" → blank line then " z=16". Re-run.
- Q21 "accepts num if line is empty": evidently "if not full"; the note and code are right. Dequeue re-traced.
- Q9 (quick/merge sort) out: Class XII Unit 10 lists only bubble, selection, insertion. Confirmed.
- Q18 file merge out: Class XI topic (see above). Confirmed.
- Q22(a) program to build a binary tree out: Unit 13(b) "binary trees, tree traversals (Conceptual)". Confirmed.
- Nothing kept is out: multiplexer, adders, NAND universality (Unit 2(b)); K-maps, canonical forms (Unit 1);
  infix→postfix, dequeue (13(a)); BST definition / traversals (13(b) conceptual); Big O (14); recursion (11);
  inheritance (12). No C++ or old-hardware items in this paper.

## Items checked and found correct (solved independently first)
Q1 idempotent ✓ · Q2 truth table 8 rows ✓ · Q3 overline placement read at 300 dpi (bar over the bracket,
p̄, q̄, p̄); F = 1 ✓ · Q4 AB−CD/*E+ ✓ · Q5 Π(0,1,4) ✓ · Q6 2874 ✓ · Q7 AB′ ✓ · Q8 AB′+A′B+A′C′ ✓ ·
Q10 ✓ · Q11 ✓ (Java re-run) · Q12 ✓ · Q13 X = AB + ACD, Σ(11–15) ✓ · Q14(a) BC + B′C′D + AB′D′ (minimal,
3 terms needed) ✓ · Q14(b) (B′+C)(A+B+D)(B+C′+D′) ✓ · Q15(a) I0..I7 = D′,D,D,D′,1,0,0,1 ✓ · Q15(b) ✓ ·
Q16(a)(b) ✓ · Q17 Time (6:35 + 3:45 = 10:20) ✓ · Q19 recursive reverse ✓ · Q20 ✓ · Q21 ✓ · Q22(b) ✓ ·
Q22(c) post D C B A 8 5 9 6 3 R, in C D A B R 8 5 3 6 9, pre R A C D B 3 5 8 6 9 ✓.
Recall panels: relevant and correct.

## Figures (every gate traced in the PNG)
fig_q2_xor ✓ · fig_q8_nand (gate taps A·B′, A′·B, A′·C′) ✓ · fig_q10_bst ✓ · fig_q13_kmap/circ ✓ ·
fig_q14a_kmap/circ (B′C′D, BC, AB′D′) ✓ · fig_q14b_kmap/circ (POS headings, A+B+D, B+C′+D′, B′+C) ✓ ·
fig_q15_mux (D, D′ taps to the right inputs) ✓ · fig_q16a_block/gates ✓ · fig_q16b_not/and/or ✓ ·
fig_q22_tree vs page image ✓.

## Page
Built (kept 26, excluded 3, figures 16, no ERROR); all 21 slices read: math renders, no overflow.
Checks: 120, 0 failed; 6 Java programs run.
