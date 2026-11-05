# Independent review — computers_2025_26_g4 (CS pre-board 2025-26, Group 4)

Source rendered at 110 dpi (all 9 pages) and at 300 dpi for p4 (both printed circuits) and p9 (the tree).
Syllabus: Computers/Syllabus/ISC-2027.pdf, Class XII theory Sections A–C and practical.

## Findings and fixes

1. **Page layout — "Part II – 50 Marks" heading missing.** Two consecutive `SEC`s; the kit renders only the
   last one before a question (kit behaviour, reported, not edited). Merged into one
   `SEC("Part II – 50 Marks · Section A", …)` carrying both printed instructions.
2. **Answer 11(i) — one-node list.** The Java printed a message and left the algorithm silent on the case
   where the only node is the one to delete. Algorithm step 2 now states it (list becomes empty; the caller
   sets start = null, since `void deleteNode(Node start)` cannot re-point the caller's reference); the
   method's message reworded; a one-node test run added to DeleteNode.java and to the check. Added an
   examiner note that ISC algorithm answers write `start = start.link`, which earns the step but only changes
   the local copy inside this signature — hence the copy-next-node technique. Judged acceptable for ISC: the
   question's own signature returns void and takes start by value, so this is the only way the method itself
   can remove the head.
3. **Answer 2(iii)(b)** — reworded so the mark-earning phrase is boxed: "Binary search (divide and conquer)",
   with the one-third split described as a modified (ternary-split) binary search.
4. **Answer 11(ii)(b)** — depth by edges kept (Depth = 1); now cites the convention of CISCE's own key for this
   same question type in the 2025 specimen (sub-tree root at level 0), with the levels-from-1 alternative (2).
5. **Transcription — instructions.** The writer had filled the truncated line "…on the same sheet as" with
   "[the rest of the answer]"; replaced by a note that the line breaks off in the original.
6. **Figure fig_q4ii_circuit** — label Y′ sat on the vertical X branch line; moved right of it.
7. **Figure fig_q5i_decoder** — removed the inline `max-height:none;max-width:600px` override (the kit now
   classes it `tall`); scale lowered 2.4 → 1.6 so its own inline max-width (428 px) sits inside the 440 px
   `tall` cap instead of overriding it.
8. **Layout — code overflow.** Two Sports.java lines and one comment ran past the code box; wrapped/shortened
   (re-run, outputs unchanged).

## Checked and found correct

- Q1(i)–(x): transcription word for word incl. options; (iii) genuinely absent in the paper → Part I = 19, note
  correct; 1(ii) does print [1] twice (note correct). Answers (d), (a), (b), (c), (b) −32 (re-run), (a)
  true false true (re-run), (a) q′⇒p, O(n), abstraction definition — all correct.
- Q2(i) postfix AB−CDE+*/FGH−^+ and stack trace; Q2(ii) 2925 (rows 20, 6×152 + 2013).
- Q2(iii)(a): re-traced by hand — m = 2, 4, 5; returns 5 → 6 → **7** (re-run: 7). The function is buggy
  (k+1 per right move); the note says so. Correct.
- Q2(iv): 0-based reading matches the printed series 0,1,1,2,4,… with T(0)=0; 1-based alternative noted;
  re-run n=0..7 → 0 1 1 2 4 7 13 24.
- Q3: conditions → X = M′L + MLT′ + M′L′S, 1s at 1,3,4,5,6,7,12,13; POS π(0,2,8,9,10,11,14,15); truth table
  figure rows and maxterms; K-map Gray order, three quads (L+S)(M′+L)(M′+T′), minimal (kmapsolve); circuit
  wired to the expression.
- Q4(i): eight maxterms → π(0,1,2,3,5,7,8,10); quads corners (B+D) and 1,3,5,7 (A+D′); 0–3 redundant; circuit.
- Q4(ii)(a): printed circuit at 300 dpi — gate (1) OR(X, Y′), (2) AND(X, Z) (branch from the X line), (3) AND,
  final OR with Z′. Redrawn figure matches. F = X + Z′, contingency, each algebra step valid.
- Q4(ii)(b) dual (A′·0)+B. Q5(ii): printed NOR(A′, A·B′) matches redrawn figure; F4 = AB → False, truth table
  right. Q5(iii) Σ(2,3,5,6) → canonical and π(0,1,4,7).
- Q5(i): hex 1 5 7 8 A C E F; decoder rendered at full height and every AND gate's four inputs traced against
  its code (true bus for 1, complement bus for 0) — all 8 correct; inverters fed from the true buses.
- Q6 Anagram, Q7 Sports, Q8 Mix_sort, Q9 Repeat, Q10 Volume, Q11(i) DeleteNode: transcription of every
  member table; all compiled and run, outputs as shown. Q8 reading (positions from 1: 1st/3rd rows
  descending) is the only one consistent with the printed sample — kept.
- Q9(b) Queue, (c) FIFO; queue figure f = 1, r = 2 consistent with its caption.
- Q11(ii): tree read at 300 dpi — J is E's **right** child (check added); redrawn tree matches; B / sibling C;
  size 3; in-order H D I B E J A F C G.
- Syllabus filter: all 36 kept items are in ISC 2027 Class XII — static methods (Methods unit), recursion,
  interfaces, complexity/Big O (space complexity is computational complexity; recursion space = stack depth),
  String/Character wrapper methods, propositional logic (contrapositive listed), infix→postfix, address
  calculation, Boolean algebra/K-maps, decoders, sorting (any technique; insertion sort is in the syllabus
  list), 2-D arrays, queue, inheritance, single linked list deletion, binary-tree size/depth/traversal. No file
  or stream item, no out-of-list sort. 0 exclusions is right.
- Build: no ERROR; whole page (~41 700 px) rendered in overlapping 7 800 px windows and every slice read: math
  renders, figures in place, no overflow after fix 8.

## Summary
Items checked 36 (+ 13 figures). Errors: transcription 1 (instruction filler), filter 0, answer 3 (11(i)
one-node case/ISC note, 2(iii)(b) emphasis, 11(ii)(b) convention citation — none changed a final value),
figure 2 (label collision, decoder size override), layout 2 (missing Part II heading, code overflow).
Unresolved / for the kit owner: kit.render_paper drops a SEC immediately followed by another SEC;
preview.py --page loses ~90 px at each 12 000 px window boundary and stops early when a window's last
content ends within 40 px of its bottom (here it stopped at ~12 000 of ~41 700 px).
