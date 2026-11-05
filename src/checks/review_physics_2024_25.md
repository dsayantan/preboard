# Independent review — physics_2024_25 (Heritage Pre-Board 2024-25, Physics Paper I)

Source: `SchoolNotes/PreBoard-PYQ/2024-25/SET-1/Physics.docx`, converted with LibreOffice (7 pp) and rendered;
every embedded image in `word/media/` inspected at full resolution and zoomed (image1 charges, image2 bridge,
image3.emf four cells (converted to PNG), image4 Vs–f, image5 lens parts, image6 prism, image7 Kirchhoff circuit,
image8 match table, image9 energy levels). Syllabus: `Physics/Syllabus/ISC-2027.pdf`.

## Findings (fixed)

| Item | Kind | What was wrong | Change |
|---|---|---|---|
| 1(A)(i) | answer | Answer given as **a) A** on the strength of the *initial* force alone. The initial resultant is along XA, but the force does not stay there: once X moves left it is nearer Y (attraction, downward component) and farther from Z, so the path bends down towards Y. Numerical integration (side 1, kq²/m = 1) shows X leaves horizontally (dy/dx ≈ 2×10⁻⁴ over the first step) and reaches y = 0.45 at x = −0.85 — the curved path **B** of the printed figure. (Same reasoning as the mirror-image textbook version of this question, whose key is the curved path.) | Answer → **b) B** with the initial-force step kept and the bending argued; new figure `fig_a1a1_path` (trajectory integrated by `_a1a1_trajectory()`); `fig_a1a1_forces` red label now "initial F (along XA)"; recall item added; check script integrates the motion and asserts start direction and downward bend. |
| 1(A)(vi) | answer (completeness) | (d) is right under the ISC convention (φ = angle by which V leads I), but the convention was not stated and the question is ambiguous. | Note added stating the convention and that the other reading gives (c). |
| 5(a) | answer (completeness) | Fig 2 halves are drawn with their axes (flat edges) displaced; the answer asserted f/2 without justifying it for non-coaxial halves. | Step added: deviations (y − a₁)/f + (y − a₂)/f = (y − ā)·2/f, i.e. one lens of focal length f/2 with axis midway. |
| fig_a15a_huygens | layout | "medium 1 … μ₁" label was crossed by the incident ray from B. | Label moved to the top right (anchor end). |
| fig_a18a_telescope | layout | β label sat on the emergent-ray arrowheads; f₀ label sat among the dashed back-extensions. | β moved below the eye; f₀ centred on its dimension line. |

## Re-judged as asked (correct, no change)

- **Q11 polarities** — zoomed image7: 3 V cell long plate on top (+ towards the 2.5 Ω / P side); 2 V cell: the lower-left plate (towards the bottom junction Q) is the long one. Writer's reading is right. Kirchhoff solved independently (numpy): I₁ = 0.3318, I₂ = 0.0897 (P→Q), I₃ = 0.2422 A (P→Q); alternative polarity 0.260/0.395/−0.135 matches the note. Redrawn qfig verified at zoom: cell long plate towards Q.
- **1(A)(ii)** — image2 zoomed: 10 V long plate at the A end, 4 V long plate at the D end. V_A − V_C = 4, I = 0.04 A, R = 150 Ω ✓. qfig/afig polarities match.
- **1(A)(iii)** — EMF image: all four long plates on the left (+ end); 6 V ∥ 6 V → 6 V ✓; qfig matches.
- **Q10** — competency booklet Q68 quote checked against `Competency/Competency-Focused-Questions.pdf` text: (a) correct, (b) incorrect, (c) incorrect, (1/6)(2×10⁻⁶/ε₀) = 3.77×10⁴ N m² C⁻¹, "Reason is to be given for both correct as well as incorrect responses" ✓.
- **Q12** — Ampère's law cannot yield B at the centre of a coil (no symmetric path); the syllabus (Unit 3 (a)) derives it by Biot–Savart. The note + Biot–Savart derivation is the right treatment ✓. Figure circulation (CCW) consistent with dl arrow (tangent checked) and B out of the page ✓.
- **5(a)** — image5 zoomed: Fig 1 = two halves cut along the axis, flat edges collinear, in contact → f/2 ✓.

## Syllabus filter (all 39 kept — confirmed)

Fusion: Unit 8 lists "Fusion, simple example 4 ¹H → ⁴He … requires very high temperature" ✓ (Q8). Full-wave rectifier and V–I characteristics: Unit 9 "half wave and a full wave rectifier … [Bridge rectifier not included]" ✓ (Q20; answer uses centre-tap, not bridge). Microwaves/radar: Unit 5 "uses; approximate range of λ or f" ✓ (Q4). n-type doping, depletion region ✓ (1B(v),(vi)). Galvanometer → ammeter ✓ (19b II). Eddy currents ✓. Huygens, YDSE, single slit, telescope at D, prism δm, Newton's xy = f² (lens formula) ✓. Nothing in the paper falls under the settled-OUT list.

## Items checked and found correct

Transcription of every item against the rendered pages (wording, numbers, options, marks, OR structure, constants table, "(i)" misnumbering in 18(b) noted) ✓. Answers recomputed: 1A(iv) d, 1A(v) a, 1A(vii) c, 1B(i) 1.5ω, 1B(ii), 1B(iii) 3.33×10⁻¹⁰ m, 1B(iv), 1B(v)–(vii), Q2 16/9, 3(a) 1.26×10⁻² T, 3(b), Q4, 5(b), Q6 √2, Q7 5.39 eV, Q9, Q13(a) 223.6 Ω / 0.447 A / 492 V, 13(b) 1-ii 2-iii 3-i, Q14 600 nm, 15(a), 15(b), Q16 1.88 eV and −1.51→−3.40, Q17 1.22 Å, 18(a) M = (f₀/fₑ)(1 + fₑ/D), 18(b) 1.3 µm, 19(a) Blv/R, B²l²v/R, B²l²v²/R, 19(b) Z, tan φ, 125 mA, Q20 ✓.

## Figures (all 33 rendered and read)

fig_q1a1_charges ✓; fig_a1a1_forces ✓ (relabelled); fig_a1a1_path new ✓; fig_q1a2/a1a2_bridge ✓ polarity; fig_q1a3_cells ✓; fig_q1b4_vsf, fig_a1b4_vsf ✓ (slope triangle, f₀, −φ₀/e); fig_a3b_xlxc ✓; fig_q5_parts, fig_a5a_parts ✓ (schematic; Fig 2 halves drawn adjacent rather than overlapping as in the low-res original — acceptable); fig_a5b_newton recomputed to scale (f = 10, x = 5, v = 30, image −8; both construction rays hit A′) ✓; fig_q6/a6_prism ✓ (i = 45° from normal, grazing emergence); fig_a9_parallel ✓; fig_a10_cube ✓; fig_q11/a11_circuit ✓; fig_a12_loop ✓; fig_a13a_phasor to scale (0.55 px/V; V_L up = leads I, V₀ lags by 63.4°) ✓; fig_a15a_huygens geometry (i = 50°, r = 30.7°, BC = AC sin i, AE = AC sin r) ✓ (label moved); fig_a15b_single_slit ✓; fig_q16/a16 levels proportional (68.8 px/eV), arrow downward ✓; fig_a18a_telescope recomputed (f₀ 24, fₑ 6, uₑ 4.84, final image 20.67 at 25; scale 8.95 px/unit in render) — all three rays meet at the tip of I′ and emerge on lines from the final image ✓ (labels moved); fig_a18b_ydse ✓; fig_a19a_rails: qv×B = +y → I from Q to P, F_B = Il×B = −x opposes v ✓; fig_a19b_lcr, fig_a19b_phasor ✓; fig_a20_bias (p-side to + end of divider) ✓; fig_a20_iv ✓; fig_a20_fwr (diodes anode at S₁/S₂, cathodes at P; load P→T) ✓; fig_a20_waves ✓.

## Build / page

`python3 src/checks/physics_2024_25_check.py` → ALL OK (two new 1A(i) trajectory checks). `python3 src/build.py physics_2024_25` → kept 39, excluded 0, figures 33, no ERROR. All 29 page slices read: math renders, no overflow, figures in place.

## Summary

39 items checked (39 kept, 0 excluded; filter confirmed). Errors: transcription 0, filter 0, answer 1 (1(A)(i) A → B) plus 2 completeness notes (1(A)(vi), 5(a)), figure 0 physics errors (1 new figure added), layout 2 (label collisions in fig_a15a_huygens, fig_a18a_telescope). Unresolved: none. Minor kit-independent nit: the 18(a) recall renders a stray "." on its own line after `M = f_o/f_e` — cosmetic.
