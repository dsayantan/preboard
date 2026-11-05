# Independent review — JEE Main mock tests, Mathematics (Q51–75 × 3)

Reviewer re-solved every item by hand (sympy where useful) before reading the writer's working;
checked the source item in `src/data/` (kept, in ISC 2027 syllabus), the option set (exactly one
defensible), option references (none use A–D letters), and rendered all six figures.
`python3 src/checks/jee_maths_check.py` → 75/75; `python3 src/jee_kit.py` → pass.

## Test 1
- Q51 onto 5→2 = 30 — OK (src 2024-25 S1 1(ix), surjection count).
- Q52 perpendicular lines: symmetric only — OK.
- Q53 tan⁻¹2x+tan⁻¹3x=π/4 → {1/6}; x=−1 gives −3π/4 — OK.
- Q54 skew part [[0,3],[−3,0]] — OK.
- Q55 |A adjA| = |A|² = 4 — OK.
- Q56 det = pxy — OK.
- Q57 d/dx(|x−2|+|x−5|) at 6 = 2 — OK.
- Q58 **AMBIGUITY fixed** (writer's doubt). 1/(x−[x]) is undefined at integers; under the NCERT domain-only convention the count would be 0, under the usual JEE convention 4. Stem now states that an undefined point counts as a discontinuity; distractor "6" replaced by "0" (the other convention) and solution explains it. Check asserts the clause.
- Q59 **WORDING fixed**: option "(−∞,−3)∪(3,∞)" — f is not strictly increasing on the union (f(−4)=49 > f(4)=−39). Option now reads "(−∞,−3) and (3,∞)", stem "increasing in", solution notes the point; check asserts it.
- Q60 √x+√y=6, slope −1 → (9,9) — OK.
- Q61 ∫eˣ(1+sin x)/(1+cos x) = eˣtan(x/2) — OK.
- Q62 ∫_{π/6}^{π/3} 1/(1+√tan x) = π/12 — OK.
- Q63 ∫₀^{3π/2}|cos x| = 3 — OK.
- Q64 area y²=x, y=x−2 = 9/2 — OK; figure correct (intersections (1,−1),(4,2)).
- Q65 linear DE, y(√3/2)=3 — OK.
- Q66 d/dx[(y′)⁴]=0 → order 2, degree 1, sum 3 — OK (consistent with source key).
- Q67 sinθ=√3/2 → π/3 or 2π/3 — OK.
- Q68 Σcos2α = −1 — OK.
- Q69 λ=−2 — OK.
- Q70 Bayes 16/31 — OK.
- Q71 NUM cone in sphere r=9 → h=12 — OK.
- Q72 NUM LPP max 270 at (40,30) — OK; figure sides correct. **Figure label fix**: "(40, 30)" label crossed the 2x+y=120 line; moved inside the region.
- Q73 NUM 16·Var = 12 — OK.
- Q74 NUM system → (1,2,−1), 6 — OK (adj checked).
- Q75 NUM K=3 — OK.

## Test 2
- Q51 R={(c,a)}: transitive (vacuously) only — OK.
- Q52 inverse (2x+5)/3 — OK.
- Q53 cot(π/2+tan⁻¹⅓) = −⅓ — OK.
- Q54 cos⁻¹(sin 9π/7) = 11π/14 — OK.
- Q55 A⁻¹ = (4I−A)/11 — OK.
- Q56 |C²| = 16 — OK.
- Q57 Vandermonde roots 2,5; sum 7 — OK.
- Q58 d/dx log√tan x at π/6 = 2/√3 — OK.
- Q59 k=−2 — OK.
- Q60 LPP max 80 at (20,10) — OK; figure correct.
- Q61 **TWO DEFENSIBLE OPTIONS fixed**: stem "strictly increasing on" made (−∞,0) also true (f′>0 there). Stem now asks for the *largest* interval; solution explains; check asserts (−∞,0) ⊂ answer and the wording.
- Q62 (writer's doubt) f=ax+3cos x+b increasing on ℝ ⇔ a≥3. At a=3 f′=3−3sin x vanishes only at isolated points, so a≥3 is right under both the "non-decreasing" and "strictly increasing" readings; no a>3 option exists to compete. OK, no change.
- Q63 ∫x²sin x — option (3) correct, others one sign slip each — OK.
- Q64 ∫eˣ(x²+1)/(x+1)² = eˣ(x−1)/(x+1) — OK.
- Q65 = π/(3√3) — OK (numerical).
- Q66 area 32/3 — OK; figure correct.
- Q67 homogeneous DE → cot(y/x)=log|x|+1 — OK.
- Q68 |b|=3 — OK.
- Q69 SD 9/√14 — OK.
- Q70 0.324 — OK.
- Q71 NUM 100Var = 54 — OK.
- Q72 NUM S/π = 96 — OK.
- Q73 NUM 4Δ² = 21 — OK.
- Q74 NUM 1/a = 6 — OK.
- Q75 NUM y(5)=5 — OK.

## Test 3
- Q51 R={(b,b)}: symmetric & transitive, not reflexive — OK.
- Q52 Statement I false (ℤ→ℤ not onto), II true — OK.
- Q53 sin[cot⁻¹{tan(cos⁻¹x)}] = x — OK.
- Q54 cos(2tan⁻¹x)=½ → ±1/√3 — OK.
- Q55 x=4 or −2 — OK.
- Q56 (a+b+c)³ — OK.
- Q57 |2A⁻¹| = −8/3 — OK.
- Q58 y″(0)=4 — OK.
- Q59 m²y — OK.
- Q60 (writer's doubt) max of −5t²+4t+1 = 1.8 m at t=0.4 s — correct, single right option. **Distractor fixed**: "1.4 m" corresponded to no slip; replaced by "0.4 m" (the time of the maximum, the classic slip) and explained. Check updated.
- Q61 max volume 8/π m³ — OK.
- Q62 ∫(1+log x)tan²(x log x) — OK.
- Q63 √2 sin⁻¹(sin x−cos x) — OK.
- Q64 π²/4 — OK.
- Q65 area 19/3 — OK; figure correct (9/2 above, 11/6 below).
- Q66 y e^{√x} = √x + C — OK.
- Q67 degree 3 — OK (consistent with source assertion).
- Q68 parallelogram from diagonals 5√3 — OK.
- Q69 plane 3x+5y−z=3; each distractor fails at A(0,1,2) — OK.
- Q70 9/17 — OK.
- Q71 NUM x=13 — OK.
- Q72 NUM p+q=47 — OK.
- Q73 NUM k=15,−9, sum 6 — OK.
- Q74 NUM max profit 27 at (3,3) — OK; figure correct.
- Q75 NUM (3,1,4) → 8 — OK (adj checked).

## Sources / syllabus
All 75 `src` items are kept items in `src/data/maths_*.py` and each question is recognisably built
on its source (numbers changed). All topics are in the ISC 2027 syllabus; no regression, no
commerce application. Solutions never cite options by letter.
