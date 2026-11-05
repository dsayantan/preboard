# Review — physics_2025_26 (theory) and physics_2025_26_prac (practical)

Independent review against src/REVIEW.md. Source pages rendered from /var/tmp/pbrev-2025-26/SET-1/PHYSICS (1).pdf
(9 pp) and PHYSICS PRACTICALS.pdf (4 pp) and compared item by item; syllabus ISC-2027.pdf; lab manual; CISCE
competency booklet.

## Findings (fixed)

1. **18(a) II — answer error (critical angle 51.7° → 41.1°).** The writer assumed the ray starts in the glass
   ("a critical angle exists only glass→air"), giving r = 55°, n = sin55/sin40 = 1.27, C = 51.7°. That argument is a
   non-sequitur: C is a property of the interface whichever way this ray travels. The data force the other reading:
   from inside, n = 1.27 is far below any glass; from air, r = 40 − 15 = 25°, n = sin40/sin25 = 1.521 (ordinary
   glass), C = 41.1°. (A glass of n = 1.52 could not even give 15° from inside at i = 40°: it emerges at 77.9°.)
   This is also the standard textbook version of the problem ("incident in air on the glass surface"). Answer rewritten,
   note explains the choice; recall panel adds Snell / bending towards the normal. Check script now checks n = 1.521,
   C = 41.1°, the rejected n = 1.27 and the 77.9°.
2. **fig_q18_refraction — figure redrawn** for air→glass (i = 40°, r = 25°, δ = 15°); caption changed; labels moved
   clear of the rays.
3. **fig_q18_fibre — figure physics error.** The zig-zag met the core–cladding boundary at 53° to the normal, which is
   below C = 63.8° and so would *not* be totally reflected. Now computed at 72° (> C), with one reflection's normal and
   θ marked.
4. **Q13 — note tightened**: the CISCE CFQ 92 key was confirmed in the booklet (Expected Answers p.56): "Student 1 –
   Pattern C; Student 2 – Pattern B", reasons wider central maximum / diminishing fringe widths vs uniform fringe widths.
   Note now quotes it rather than paraphrasing.
5. fig_q18_huygens: docstring said i = 40° (code draws 30°); B label moved off the arrowhead. Cosmetic.

## Items checked and found correct

- Transcription: every item of both papers compared with the page images — wording, numbers, options, marks,
  numbering. Minor printed slips are silently normalised (option "2a" → 2 A; "1/F2" → 1/f2; stray "a)" prefixes on
  Q15/Q17) — acceptable.
- 6(b) excluded: confirmed — the 2027 Optics unit (6(i)(a)–(e), (ii)) and practical list have no human eye /
  defects of vision / myopia (grep "eye", "vision", "myop": only "least distance of distinct vision" in the microscope
  item). Exclusion stands. All other items are inside the syllabus (Zener as regulator, centre-tap FWR with "bridge
  rectifier of 4 diodes not required", pair production, reactor control rods, reflecting telescope, resolving power of
  compound microscope, bandwidth/Q, Huygens reflection, optical fibres, BE/A).
- 1(A)(v): re-derived. Concave mirror, real image: object and image both in front, so u < 0 and v < 0 (Cartesian);
  the v–u hyperbola is in the 3rd quadrant through (2f, 2f) with asymptotes u = f, v = f. No convention gives
  "u negative, v positive" for a real mirror image (real-is-positive puts it in the 1st quadrant). A false, R false ⇒
  (d). Correct; fig_q1a5_vu scale checked ((2f,2f) at exactly 2×58 px).
- 1(A)(i)–(iv),(vi),(vii); 1(B)(i)–(vii): all answers re-solved (0.5 A; 10 mH; h = 6.59e-34; L = 2.1e-34; Paschen
  1875 nm IR; 1.02 MeV threshold) — correct.
- Q2: no V values on the printed axis (ticks 0,1,2,3 only) — expressing E in terms of V0 is the right call; signs of E
  correct.
- Q3: number and capacitance genuinely missing in the print; n × C assumption and ½nCV² correct.
- Q4(a) 5 min; 4(b); Q5; Q6(a) i = 49° (note on "equilateral" with A = 59.5° is right — the paper's own slip; 59.5° used);
  Q7; Q8 (IR greenhouse / UV welding); Q9 (1.0e-18 J = 6.25 eV, 3.33e-27); Q10 (12 µF, 100 µC); Q11(a) X = 3 Ω,
  6 Ω in parallel; 11(b); 12(a)/(b); Q14 1→(ii) 2→(iii) 3→(i); Q15 0.06 V, 0.01 A, direction N→M, A→C through R
  (qv×B and Lenz both checked); Q16 d = 5 mm, β = 0.096 mm (duplicate garbled clause note accurate); Q17 C/I/I;
  18(a) I; 18(b); 19(a) v1 = c/137 (7.30e-3); 19(b)(i); 19(b)(ii) Δm = 0.0256 u, Q = 23.85 → 23.8 MeV, 3.8e-12 J
  (⁴He₁ note accurate — the equation itself prints ⁴He₂); Q20.
- Practical Q1: within syllabus expt 1 (u–v, no parallax); readings within ±0.4 cm of f = 15 cm; x, y to 2 dp;
  slope from non-plotted points, S = 0.0662 cm⁻¹ (3 s.f.), F = 15.1 cm (1 dp); origin shifted, >60% coverage, per the
  lab manual. Notes on "change∈y" and "for each set" are right (one slope ⇒ one F).
- Practical Q2: syllabus expt 9 (resistance of a wire from V and I); least counts 0.05 V / 0.02 A match the lab manual;
  readings are whole least counts, within range; r per set and r0 = 3.2 Ω recomputed.
- Figures looked at (all PNGs): q1a5_vu, q1a6_photo, q2_vx, q2_ex, q7_levels, q8_em, q9_vs_nu, q10_caps (matches
  print: C1 3 µF, C2 6 µF series, C3 10 µF, 50 V), q11_bridge (2 Ω / X / G jockey at 40 cm, as printed), q11a_new,
  q11b_ampere, q12a_phasor, q12b_resonance, q13_patterns, q15_rails, q15_ans, q18_lenses (to scale: v1 = 120, v = 40),
  q18_huygens (BC = AD = ct = 150 px; wavelet radius = AD; AB ⊥ ray), q19_bohr, q19_bea, q20_fwr (cathodes at P,
  + output at P, same current direction), q20_waves, p1_bench, p2_circuit (current enters ammeter + and voltmeter + at A,
  as printed), p1_graph.
- Page: both built with no ERROR; every slice viewed — math renders, figures in place, no overflow.

## Summary
Items checked: theory 40 (39 kept, 1 excluded), practical 2; figures 27.
Errors: transcription 0; filter 0; answer 1 (18(a)II); figure 2 (refraction redraw consequent on 18(a)II; fibre TIR
angle below C); layout 0 (2 cosmetic label fixes). Unresolved: none.
