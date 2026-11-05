# physics_2024_25 — figure checks (rendered with preview.py and looked at; page rendered with --page, all 29 slices read)

Source images checked at full resolution from `word/media/` of the .docx (image1–9 PNG, image3 EMF via a 500 dpi page render).
Cell symbols: long plate = + terminal throughout.

## Question figures (redrawn)
- fig_q1a1_charges — X at the top, Y bottom-left, Z bottom-right; dashed paths A (left), B (curving down-left), C (right), D (curving down-right) as printed. Charges (+q, −q, +q) added from the question text.
- fig_q1a2_bridge — A–B 10 V cell with long plate at A, B–C resistor R, A–C 100 Ω, A–ammeter–D, D–C 4 V cell with long plate at D: matches image2. Polarity is self-consistent with the zero-reading condition (V_A − V_C = +4 V, and the 10 V cell drives A→C) — the other polarity has no solution.
- fig_q1a3_cells — E1, E2, E3 (2 V each) in the upper branch, E4 (6 V) lower branch; every long plate faces the left (+) terminal, as on the 500 dpi render of the EMF.
- fig_q1b4_vsf — V_S–f: solid line from the threshold on the f-axis, dashed extension meeting the negative V_S axis; axes 0, V_S, f as printed (no values on the paper).
- fig_q5_parts — lens with dashed principal axis labelled f; Fig 1 two upper halves side by side; Fig 2 upper half beside a lower half raised so its flat edge is higher, as printed.
- fig_q6_prism — ∠B = 90° (box), ∠C = 45°, horizontal ray entering AB normally, emergent ray (bold arrow) along AC towards C. Geometry: ray height y meets AC where x − x_A = y − y_A (45° face).
- fig_q11_circuit — 3 V, 2 Ω cell left (long plate top); 2.5 Ω top, 4 Ω bottom, 2 Ω middle vertical; 5 Ω top right; diagonal from the top-right corner down to the bottom junction carrying 3.5 Ω then the 2 V, 0.5 Ω cell with long plate at the bottom junction — matches the zoomed image7.
- fig_q16_diagrams — levels −0.378, −0.544, −0.850, −1.51, −3.40 eV (positions proportional to energy; the close top pair labelled with an offset); spectrum lines 411, 435, 488, 658 nm on a linear λ scale.

## Answer figures
- fig_a1a1_forces — equal arrows towards Y (60° below XA) and away from Z (60° above XA); parallelogram dashed; resultant along XA (labelled as the INITIAL force). Check script: unit-vector sum = (−1, 0).
- fig_a1a1_path — (review) trajectory integrated numerically by `_a1a1_trajectory()` (side 1, kq²/m = 1): leaves X along XA, bends down towards Y; ends labelled B. Check script asserts the initial direction and the downward bend.
- fig_a1a2_bridge — I arrows A→C through 100 Ω and C→B through R (out of + of the 10 V cell at A); "I = 0" on the ammeter branch.
- fig_a1b4_vsf — slope triangle ΔV_S/Δf, intercepts f₀ and −φ₀/e, dashed extension.
- fig_a3b_xlxc — X_L line through origin; X_C = A/f hyperbola; crossing at f₀ = √(A/k) marked with dashed drop line.
- fig_a5a_parts — the two arrangements, each piece labelled f, F = f/2.
- fig_a5b_newton — to scale, f = 10, u = −15, v = +30, h = 4 → h′ = −8 (check script); three rays: parallel→F₂, through O, through F₁→parallel (meets the lens at −8 = image height, passes x = −10 at y = 0). x between object and F₁, y between F₂ and image.
- fig_a6_prism — normal to AC at the point of incidence (perpendicular to the 45° face); i = 45° between incident ray and normal inside; e = 90° between outward normal and emergent ray along AC.
- fig_a9_parallel — C₁, C₂ between A and B; cell long plate on the A side so left plates +Q.
- fig_a10_cube — cube of side 10 cm, charge at the centre, 5 cm below the shaded top face (the plate).
- fig_a11_circuit — I₁ along the top wire towards P and along the bottom wire away from Q, I₂ down through 2 Ω, I₃ rightwards through 5 Ω; matches the solved signs (all positive), check script nodal solution.
- fig_a12_loop — current arrows anticlockwise at 20° (up) and 260° (right), dl at 140° tangent pointing down-left (anticlockwise), r to O perpendicular to dl, field out of page (⊙) — right-hand grip consistent.
- fig_a13a_phasor — to scale (0.55 px/V): V_R0 44.7 along I, V_L0 178.9 up, V_C0 268.3 down, V₀ in the fourth quadrant at 63.4° below I (current leads). Check: √(44.7² + 89.4²) = 100.
- fig_a15a_huygens — i = 50°, μ₂/μ₁ = 1.5 ⇒ r = 30.7°; BC = AC sin i, AE = AC sin r; AB ⊥ incident rays, CE tangent to the wavelet (AE ⊥ CE); refracted rays bend towards the normal.
- fig_a15b_single_slit — (sin β/β)²: zeros at ±λ/a, ±2λ/a, ±3λ/a; secondary maxima 0.047 I₀ and 0.016 I₀ (≈ I₀/22, I₀/62, check script).
- fig_a16_levels — as Diagram 1, red arrow downward from −1.51 to −3.40 eV, labelled 658 nm (1.89 eV).
- fig_a18a_telescope — to scale f₀ = 24, fₑ = 6, D = 25: three parallel incident rays all pass through the tip of I′ (at F₀, height −4); uₑ = 150/31 = 4.84; emergent rays lie on lines from the final image tip (25 in front of the eyepiece, height −20.67), dashed back-extensions meet there. Fₑ lies 1.16 to the left of F₀ (I′ inside fₑ). Labels F₀/Fₑ placed either side.
- fig_a18b_ydse — S₁N perpendicular to S₂P (foot computed), θ at the slit midpoint, y, d, D marked.
- fig_a19a_rails — B into page (×), v to the right; q v×B = +y so I runs Q→P in the rod and back through R (arrow on top rail leftwards); F_B = I l×B to the left (opposes v). Check script computes both cross products.
- fig_a19b_lcr / fig_a19b_phasor — series R, L, C with a.c. source; V_R along I₀, V_L up, V_C down, V₀ leading by φ (X_L > X_C).
- fig_a20_bias — battery long plate on the left feeds the rheostat; the left (+) end goes via mA to the p side of the diode, the n side to the slider: forward bias. Voltmeter across the diode.
- fig_a20_iv — forward current negligible until ~0.7 V knee then steep; reverse small constant μA current then breakdown; axes labelled with the mA/μA scale change.
- fig_a20_fwr — centre-tapped secondary, D₁ and D₂ cathodes to P, load from P to T; load current P→T in both half-cycles (+ at P).
- fig_a20_waves — input sine, output |sin| with D₁/D₂ alternating each half-cycle.
