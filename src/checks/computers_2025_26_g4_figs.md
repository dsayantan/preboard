# Figures — computers_2025_26_g4 (src/figs/computers_2025_26_figs.py)

- fig_q3_truth: 16 rows in binary order M L T S; X = 1 exactly in rows 1,3,4,5,6,7,12,13 (= truth(X) in the check); shaded rows carry maxterms with 0→plain, 1→complement (rows 0 and 15 spot-checked).
- fig_q3_kmap: Gray-code rows/cols (cell numbers in corners match), 0s in 0,2,8,9,10,11,14,15; rings = kmapsolve groups: corners 0,2,8,10 (L+S), row 8–11 (M'+L), 10,11,14,15 (M'+T').
- fig_q3_circuit: three 2-input ORs (L,S)(M',L)(M',T') into one 3-input AND, output X; every input wired.
- fig_q4i_kmap: 0s in 0,1,2,3,5,7,8,10; rings corners (B+D) and 1,3,5,7 (A+D'); redundant 0–3 quad deliberately not drawn.
- fig_q4i_circuit: OR(B,D), OR(A,D') into AND → F.
- fig_q4ii_circuit (question): compared with page 4 image — gate (1) OR of X and NOT Y, (2) AND of X (branch, dot) and Z, (3) AND of (1),(2), final OR of (3) and NOT Z (Z branch, dot); Y′ wire crosses the X branch without a dot, as printed.
- fig_q5i_decoder: true and inverted bus for A–D; each AND checked: 0001 → A′B′C′D … 1111 → ABCD, labels give hex 1 5 7 8 A C E F; height cap lifted so it renders full size.
- fig_q5ii_circuit (question): A′ to NOR; A and B′ to AND; AND output to NOR second input; output F4 — matches page 4.
- fig_q9_queue: cap 5, after 3 pushes and 1 pop: f = 1, r = 2, cell 0 greyed; insert at rear (right), delete at front (left).
- fig_q11i_delete: 10→20→30→40, prev at 20, ptr at 30, red bypass arrow from 20's link to 40, old links dashed.
- fig_q11_tree (question): A(B,C), B(D,E), D(H,I), E(–,J) [J is E's right child, read off the page image at 200 dpi], C(F,G); layout is in-order x-position so left/right is unambiguous.

Review (independent): fig_q4ii_circuit — Y′ label moved off the X branch line; gates re-checked at 300 dpi.
fig_q5i_decoder — inline max-height/max-width override removed (kit class "tall"), scale 1.6 (428 px);
all 8 AND gates' inputs traced against their codes. fig_q11_tree — J confirmed as E's right child.
