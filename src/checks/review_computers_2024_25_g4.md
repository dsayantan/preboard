# Independent review — computers_2024_25_g4 (CS pre-board 2024-25, Theory, Group 4)

The source is `SET-1/COMPUTER THEORY.pdf`. I rendered all 9 pages at 110 dpi, and page 4 at 400 dpi so I could
read the 4(b) law and the 5(a) MUX symbol by symbol. The syllabus is `Computers/Syllabus/ISC-2027.pdf`,
Class XII theory and practical.

## Findings and fixes

1. **5(a) MUX: the select-bit order is a convention, not fixed by the paper.** The figure labels the select
   lines S1 and S2 but does not say which is the MSB. The answer (S1 = A as MSB, giving Z = A ⊕ C) is right under
   the usual convention. I added a note that taking S2 = B as the MSB gives Z = B ⊕ C, and that the candidate
   should state which convention they use. I also added a check line that confirms the alternative over all 8 rows.
   I checked the wiring against the 400 dpi crop: C̄ goes to I3 and I2, C goes to I1 and I0, S1 = A, S2 = B. The
   redrawn qfig matches.
2. **1(iv) encoder answer: added a clarifying note.** The answer B (both statements false) stands. The note
   explains that each input *line* carries a binary 0/1 level, and that the assertion is false because it is about
   which number system the inputs represent. Without the note, the answer could be misread as wrong.

## Points the caller asked me to re-check

- **4(b).** I re-read the line at 400 dpi in two crops, and the text layer agrees:
  `A=>(B∧C)= (A=>B)∧ (B=>C)`. The second implication really is **B ⇒ C**. I re-derived the truth table by hand
  (8 rows): the two sides differ only in row A=0, B=1, C=0 (L = 1, R = 0). So the proposition as printed is
  **not valid**, and the writer's table, conclusion and note (that the valid law has A ⇒ C) are correct.
- **1(iv).** Answer B, with a note added (finding 2).
- **1(vii).** Re-traced: it prints 1, 3, 9, 27. p becomes 81 but is never printed, and trick() is void. Answer
  b) 27 (the last value displayed) is the best option, and the explanation says why 81 is wrong. Correct.
- **Q7 stray digits.** The "673" at the top of page 6 is the second output line of the example. It is the
  odd-positioned digits of 65723 (6, 7, 3), and the transcription note says so. Correct.
- **Q8 method signature.** The member table prints `void element_k()` with "returns", and the closing
  instruction says `int element_k()`. The answer follows the int version and notes the conflict. Correct.
- **Q9 semantics.** The prototype `void deleteNode(Node first)` has no search key, so "start/first node
  containing str" means the head node. Java passes references by value, so copying the second node's data into the
  head and unlinking the second node is the only way the method itself can remove the head. The empty-list and
  one-node cases are handled, and the note gives the usual ISC answer `start = start.link`. Re-ran it: the output
  is as shown. I judge this acceptable, consistent with the review of computers_2025_26_g4 Q11(i).

## Syllabus filter

All 31 items kept, 0 excluded. I confirmed each against the syllabus:

- **1(ix) "What is an exception?"** is in. Class XII item 5(c) reads "Basic input/output using Scanner and Printer
  classes from JDK; input/output exceptions."
- Interfaces and abstract classes: item 12. Encoders, decoders, MUX and XNOR: Section A item 2.
- Propositional logic and validity: Section A item 1(a). K-maps: 1(c).
- Recursion: item 11. Complexity: item 14.
- Linked lists and conceptual binary trees: item 13. The binary-tree items here are conceptual and traversal
  only, not tree programs.
- Infix to prefix: item 13. 2D arrays: item 10.

## Checked and found correct

- **Transcription.** Every item matches the page images word for word, including options, marks (Part I 20,
  Q3–Q5 10 each, Q6–Q8 10, Q9–Q11 5), code, the Q8 example and the Q11 member lists. The Q3(b) expression's eight
  sum terms match the image.
- **1(i) A; 1(ii) C; 1(iii) A; 1(vi) a) O(n); 1(viii) C.** The last level is filled left to right.
- **1(v).** Both comparison tables are correct. The leaves 1, 4, 7, 13 and internal nodes 8, 3, 6, 10, 14 are
  right for the Q10 tree.
- **1(ix).** The definition is correct and examiner-ready.
- **2(i).** Re-derived /+/ABC*D-EF. **2(ii)** correct. **2(iii)** O(1).
- **2(iv).** The blanks are 1, '0', str.charAt(0)-'0', Math.pow(10, str.length()-1), Inte(str). Re-ran Part1.java:
  it prints 1235, and Inte("40096") = 40096.
- **3(a).** Re-solved: F = AB′ + BC + A′BD. Cell 5's only 1-neighbour is 7, so the pair A′BD is essential.
- **3(b).** The maxterms π(0,1,2,3,5,6,8,10) are read correctly. F = (A+B)(B+D)(A+C+D′)(A+C′+D) is minimal
  (kmapsolve agrees).
- **4(a).** All eight AND terms and hex values 2 5 7 8 A C E F are correct.
- **4(c)(i), 4(c)(ii).** XNOR is the biconditional; Y = A′B′ + AB.
- **5(b).** AC, each law step valid. **5(c).** X = AB + A′BD + CD gives rows {3,5,7,11,12,13,14,15}, re-derived
  by hand. The truth table figure agrees row by row, including the criterion column.
- **Q6.** Duplicate.java re-run: programming → progamin; MISSISSIPPI RIVER → MISP RVE. The method is recursive and
  matches the String remvDup(String,String,int) signature.
- **Q7.** Join.java re-run: 65723 / 673; 12030 / 100. The digit-count do-while handles 0.
- **Q8.** Swirl.java re-run: k=7 → 16; 3×4, k=10 → 5 (spiral 1 2 3 4 8 12 11 10 9 5); invalid k is reported.
  The single-row and single-column guards are present.
- **Q10(a).** Correct. **10(b).** Postorder 1 4 7 6 3 13 14 10 8, depth 1, size 9. Re-traced against the printed
  tree, where 14 is the right child of 10 and 13 the left child of 14.
- **Q11.** Staff.java re-run, and the output matches: overtime 12 × 250 = 3000, wages 18000. super() comes first
  and the display methods are public.

## Figures

Rendered with `python3 src/preview.py computers_2024_25_figs`. I read every PNG; the decoder was re-rendered at
1100 px wide.

- **q1iii insert** — correct.
- **q3a kmap** — correct cells and rings.
- **q3a circuit** — every input is wired.
- **q3b kmap** — correct 0 cells, the corner quad and both pairs.
- **q3b circuit** — correct.
- **q4a decoder** — checked gate by gate against the bus x-positions: A/B/C/D true buses and A′/B′/C′/D′
  complement buses each have their own inverter, and all 8 gates take the right lines.
- **q4c xnor and q4c xnor gates** — correct.
- **q5a mux** — matches the printed figure.
- **q5a xor** — correct.
- **q5c truth** — correct.
- **q8 spiral** — the arrows follow 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10.
- **q9 delete** — correct.
- **q10 tree** — matches the printed tree.
- **q10 recursive** — correct.
- **q11 classes** — correct.

## Page

`python3 src/build.py computers_2024_25_g4` runs with no ERROR. I read all 30 preview slices: KaTeX renders and
nothing overflows. The figures sit with their answers and the code blocks fit their boxes.
