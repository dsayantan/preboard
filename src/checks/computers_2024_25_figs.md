# Figures — computers_2024_25_g4 (src/figs/computers_2024_25_figs.py); computers_2024_25_p2 has none

All rendered with `python3 src/preview.py computers_2024_25_figs` and looked at, then seen again in the built page.

- fig_q1iii_insert: new node 5 (temp) with temp.link → old first node 10; start re-pointed to temp; old start reference dashed. Two assignments labelled (1), (2).
- fig_q3a_kmap: Gray-code headings, cell numbers in corners match; 1s exactly in 5,6,7,8,9,10,11,14,15 (= the check); rings = kmapsolve cover: quad 8–11 (AB′), quad 6,7,14,15 (BC, dashed), pair 5,7 (A′BD).
- fig_q3a_circuit: AND(A′,B,D), AND(B,C), AND(A,B′) into one 3-input OR → F; every input wired.
- fig_q3b_kmap: 0s exactly in 0,1,2,3,5,6,8,10 (maxterms read from the printed sum terms, verified in the check); rings: quad 0–3 (A+B), corner quad 0,2,8,10 (B+D, open at all four edges), pair 1,5 (A+C+D′), pair 2,6 (A+C′+D).
- fig_q3b_circuit: OR(A,B), OR(B,D), OR(A,C,D′), OR(A,C′,D) into one 4-input AND → F.
- fig_q4a_decoder: zoomed and checked gate by gate — 0010 → A′B′CD′, 0101 → A′BC′D, 0111 → A′BCD, 1000 → AB′C′D′, 1010 → AB′CD′, 1100 → ABC′D′, 1110 → ABCD′, 1111 → ABCD; every complement has its own NOT gate and bus; hex labels 2 5 7 8 A C E F.
- fig_q4c_xnor (question): matches page 4 — XNOR (double back curve, output bubble), inputs A, B, output Y.
- fig_q4c_xnor_gates: AND(A′,B′), AND(A,B) into OR → Y = A′B′ + AB.
- fig_q5a_mux (question): matches page 4 (zoomed at 300 dpi) — C̄ tied to I3 and I2, C tied to I1 and I0 (junction dots), select S1 = A, S2 = B at the bottom, output Z.
- fig_q5a_xor: XOR gate, inputs A and C, output Z (Z = A ⊕ C verified over all 8 rows in the check).
- fig_q5c_truth: 16 rows in binary order A B C D; X = 1 exactly in rows 3,5,7,11,12,13,14,15 (= truth(X) in the check); criterion column spot-checked (row 7 = 0111: A′BD and CD → "2nd, 3rd").
- fig_q8_spiral: 4 × 4 example; arrows follow 1,2,3,4,8,12,16 (red, numbered 1–7) then 15,14,13,9,5,6,7,11,10 (blue); 16 ringed as the 7th.
- fig_q9_delete: list Red → Green → Blue → Pink; (1) Green copied into the first node (Red struck out), (2) first.link bypasses the second node to Blue; first/start arrow on the first node; matches the Java run (Red… → Green → Blue → Pink).
- fig_q10_tree (question): matches page 8 — 8 (3 (1, 6 (4, 7)), 10 (–, 14 (13, –))); 14 is the RIGHT child of 10 and 13 the LEFT child of 14, as printed.
- fig_q10_recursive: root with two triangles labelled left/right subtree (a binary tree); edges meet the triangle apexes.
- fig_q11_classes: «interface» Staff ← (dashed, implements) Worker ← (solid, extends) Wages; members as in the program; no text touching borders.
