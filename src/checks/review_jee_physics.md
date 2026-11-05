# Independent review — JEE Main mock tests, Physics (src/jee/physics_t{1,2,3}.py)

Method: each question re-solved before reading the given answer; every distractor's stated slip
recomputed; source item opened in `src/data/` (all 75 are kept items, on the stated topic, ISC 2027
syllabus); figures rendered with `src/preview.py` and read (physics_figs: zener, rails, lens-mirror;
reused: physics_2016_17 fig_q5a_wire, physics_2013_14 fig_q2b_caps). No question depends on
physics_2024_25 1(A)(i). Options are rotated by `_mcq(..., k)`, so a positional reference in a
solution points at the wrong displayed option. Fixes are pinned in `jee_physics_check.py`
(`review_checks()`).

## Test 1
- Q1 OK (20 V; Q conserved, 6C).
- Q2 OK (5e-4 N).
- Q3 OK (C halves, V doubles, U doubles).
- Q4 OK (0.50 A; slips 0.80/0.48/0.11 verified).
- Q5 OK (8v).
- Q6 OK (1:1 at equal KE; equal-p, equal-v, equal-V rationales verified).
- Q7 OK (μ0I(π+1)/4πr). Figure: vertical lead lies on the line through O (0), semicircle anticlockwise (out), lower wire rightward below O (out) — consistent.
- Q8 OK (20 mH).
- Q9 OK (440 V).
- Q10 OK (10^10 Hz, microwaves).
- Q11 OK (40 cm).
- Q12 OK (30 cm).
- Q13 OK (√2; all three slip values verified).
- Q14 OK (4:1).
- Q15 OK (1.8 V).
- Q16 OK (Paschen, IR; λ = 1.88 μm).
- Q17 OK (7.07 MeV).
- Q18 OK (10 mA). Figure: Zener cathode to + rail via 200 Ω (reverse biased), values match.
- Q19 OK (both decrease).
- Q20 OK (0.02 N; 0.04/0.2/0.08 slips verified).
- Q21 OK (9 J).
- Q22 OK (25 Ω).
- Q23 OK (1960 Ω).
- Q24 OK (540 nm).
- Q25 OK (6 eV, rounding stated).

## Test 2
- Q1 OK (√3 qa).
- Q2 OK (0.06 J).
- Q3 OK (3.77e4).
- Q4 OK (2.2 V).
- Q5 OK (1 Ω in series; 9 Ω ∥ 4.5 Ω = 3 Ω rationale verified).
- Q6 Rationale wrong: "B/2 has the radius change the wrong way" — N = 2 with R doubled gives B, the same as the other distractor's rationale. Fixed: B/2 = radius doubled with the extra turn forgotten.
- Q7 OK (0.025 T into page; v×B direction re-derived for an electron).
- Q8 OK (12.6 mT).
- Q9 OK (2.2 A).
- Q10 OK (inductor, Y = P).
- Q11 Solution named options by position ("the second sequence… the third… the fourth"); with k = 3 the displayed order differs, so all three references pointed at the wrong option. Fixed: options named by content.
- Q12 OK (−30 cm).
- Q13 OK (100 cm, 9).
- Q14 OK (7I).
- Q15 OK (1.2 μm).
- Q16 OK (600 nm, 2.06 eV). The 500 nm/2.48 eV rationale is contrived but the option is wrong and harmless.
- Q17 Solution referred to "the third option". Fixed: named by content.
- Q18 OK (4πa0).
- Q19 OK (n-type, electrons).
- Q20 OK (100 Hz).
- Q21 OK (10 μJ).
- Q22 OK (5 min).
- Q23 OK (968 W).
- Q24 OK (6 cm).
- Q25 OK (18).

## Test 3
- Q1 OK (n²).
- Q2 OK (120 V).
- Q3 OK (1.5e-4 J).
- Q4 OK (2 A).
- Q5 OK (number density).
- Q6 OK (√(me/mp)).
- Q7 Rationale wrong: "4 uses an inverse-square law" — inverse-square with the factor 2 gives 8 (another distractor). Fixed: 4 = inverse-square and the axial factor 2 dropped.
- Q8 Stem misused "figure of merit" (that is current per division, not divisions per mA) and the 150 mA rationale inherited the error. Fixed: "deflects 5 divisions per mA (figure of merit 0.2 mA per division)"; 150 mA = 30 × 5 instead of 30 ÷ 5.
- Q9 OK (lags 45°).
- Q10 OK (500 W).
- Q11 OK (ultraviolet; matches source answer for Fig-2).
- Q12 OK (2/5).
- Q13 OK (+60 cm converging).
- Q14 OK (0.15°).
- Q15 OK (60°).
- Q16 Rationale wrong: "λ/√2 takes the speed as doubling" — doubled speed gives λ/2, the correct answer. Fixed: λ/√2 is the result for height 2H.
- Q17 OK (3.7 eV).
- Q18 OK (2.43 pm).
- Q19 OK (indium).
- Q20 OK (alternate half-cycles, 100 Hz).
- Q21 OK (20 V). Reused figure shows 8, 16, 24 μF and 110 V, matching the stem.
- Q22 OK (23 A).
- Q23 OK (250 mA; N→M direction checked against figure). Figure: field label "B (into page)" sat beside rail end "B". Fixed: relabelled "field 0.2 T into page" and moved clear of M.
- Q24 OK (5 cm). Figure to scale (12 px/cm): lens image at 30 cm = mirror's C, rays meet mirror normally.
- Q25 OK (9).

## Summary
75 questions: 0 wrong answers, 0 wrong keys, 0 defensible second options, 0 source problems.
Defects fixed: 2 positional option references (T2 Q11, Q17), 3 wrong distractor rationales
(T2 Q6, T3 Q7, T3 Q16), 1 misused term in a stem (T3 Q8), 1 figure label clash (T3 Q23 rails).
