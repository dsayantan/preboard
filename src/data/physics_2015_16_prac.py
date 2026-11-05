"""Heritage School Pre-Board 2015-16, Physics Paper 2 (Practical) — digital copy, ISC 2027 filter, solutions.
Transcribed from the page images.  Readings in the answers are SAMPLE readings generated from plausible apparatus
values (a 15.0 cm lens; a constantan wire of 0.039 ohm/cm, d = 0.040 cm) and rounded to the instrument least counts."""
import math
from kit import Q, SEC
import physics_2015_16_figs as F

RAY, CE = "Practical — Ray Optics (Experiment 1: f of a convex lens, u–v method)", \
          "Practical — Current Electricity (Experiments 8/9: resistance and resistivity of a wire)"

# ------------------------------------------------------------------ sample-reading tables (built from figs constants)
_rows1 = "".join(
    f"<tr><td>{k+1}</td><td>{u:.1f}</td><td>{v:.1f}</td><td>{x:.1f}</td><td>{y:.1f}</td></tr>"
    for k, (u, v, x, y) in enumerate(zip(F.P1_U, F.P1_V, F.P1_X, F.P1_Y)))
_ya = F.P1_C + F.P1_M * F.P1_XA
_yb = F.P1_C + F.P1_M * F.P1_XB
P1_SLOPE = round((_yb - _ya) / (F.P1_XB - F.P1_XA), 3)
P1_FOCAL = 10 / math.sqrt(P1_SLOPE)

_r = [round(v / i, 2) for v, i in zip(F.P2_V, F.P2_I)]
_r3 = [f"{v / i:.2f}" for v, i in zip(F.P2_V, F.P2_I)]
_rows2 = "".join(
    f"<tr><td>{k+1}</td><td>{R}</td><td>{V:.2f}</td><td>{I:.2f}</td><td>{r3}</td></tr>"
    for k, (R, V, I, r3) in enumerate(zip(F.P2_R, F.P2_V, F.P2_I, _r3)))
R0 = round(sum(float(x) for x in _r3) / 5, 2)
D = sum(F.P2_D) / len(F.P2_D)
RHO = math.pi * D ** 2 * R0 / 320          # ohm cm

SAMPLE = '<p class="note">The readings below are <b>sample readings</b> (realistic values for typical apparatus, ' \
         'recorded to the least count) — your own readings will differ.</p>'

PAPER = dict(
    subject="physics", year="2015-16", slug="2015-16-practical", paper="Paper 2 (Practical)", practical=True,
    source="PreBoard-PYQ/2015-16/Physics practical paper 2.pdf", marks=20, time="3 hours",
    intro=r"""<p>Candidates are allowed additional 15 minutes for only reading the paper. They must NOT start writing
during this time. <i>Answer all questions.</i></p>
<p>ALL ANSWER MUST BE WRITTEN ON THE ANSWER SHEETS PROVIDED SEPARETLY. If squared paper is used, it must be attached
to the answer booklet.</p>
<p><i>Marks are given for a clear record of observations actually made, for their suitability and accuracy, and for
the use made of them. A brief statement of the method may be given if necessary. The theory of the experiment is not
required unless specifically asked for.</i> Candidates are advised to record their observations as soon as they
have been made. <i>All working including rough work should be done on the same sheet as the rest of the answer.
Mathematical tables and squared paper are provided. The intended marks for questions or parts of questions are given
in brackets [ ]. You should not spend more than one and a half hours on Question No. 1</i></p>
<p><i>Answer</i> all <i>questions. You should not spend more than one and a half hours on each question.</i></p>
<p class="note">[As printed: "Full Marks: 20", although the question marks add up to 10 + 8 + 7 + 3 = 28. Under the
ISC scheme of the time Paper 2 had 20 marks for the experiments and a further 10 (project 7 + file 3) assessed by
the Visiting Examiner, so Q3 sits outside the 20; but Q1 + Q2 print only 10 + 8 = 18. The paper also says it has
4 printed pages while the PDF has 3 (numbered 1–3, Q2 running on continuously from page 2 to page 3), so a 2-mark
item on a lost fourth page cannot be ruled out. Transcribed as printed.]</p>""",
    items=[
        SEC("Question 1"),
        Q("1", 10, r"""<p>(i) This experiment determines the focal length of a convex lens by no parallax method.</p>
<p>(ii) Determine the approximate focal length \(f\) of the given convex lens by projecting the image of a distant
object formed by the lens on a wall or a screen. Record the value of f in cm upto one decimal place.</p>
<p>(iii) Mount the given convex lens on the lens holder. Adjust the heights of object pin O and image pin \(I\) so that
their tips lie on the principal axis of the lens.</p>{{fig:0}}
<p>(iv) Keep the object pin O to the left of the convex lens L, and image pin I to the right of the lens. Keep the
object pin at zero cm. mark and the convex lens at 70.0 cm. mark of the optical bench; so that the object distance
\(u = OL = 70.0\) cm.</p>
<p>(v) Look at the object pin through the lens, from a distance. You would see an inverted image, \(I'\) of the object
pin. Adjust the position of the image pin in such a way that there is no parallax between \(I\) and \(I'\). At no
parallax position, note the position of image pin. Measure the image distance \(v = LI\), i.e. distance of the image
pin from the lens in cm. correct to <b><i>one decimal place</i></b>. Record the value of \(v\) in your answer book and
<b>show this reading to the Visiting Examiner.</b></p>
<p>(vi) Calculate \(x = u - f\) and \(y = \dfrac{100}{v - f}\), both up to <b><i>one decimal place</i></b>.</p>
<p>(vii) Now repeat the experiment for \(u\) = 60 cm, 50 cm, 40 cm, 30 cm and 20 cm. Each time, find \(u, v\) and \(y\).
Now, tabulate all <b><i>six</i></b> sets of values of \(u, v, x\) and \(y\) with their units. Plot a graph of \(y\) vs.
\(x\). Draw the line of best fit.</p>
<p>(viii) Determine its slope \(m\) using: \(m = \dfrac{\text{change in } y}{\text{change in } x}\)</p>
<p>(ix) Record the value of \(m\) in your answer book, correct up to <b><i>three significant figures</i></b>. Hence
calculate the focal length of the lens using: \(f = \dfrac{10}{\sqrt m}\) cm.</p>""",
          qfig=F.fig_p1_bench, afig=F.fig_p1_graph,
          a=r"""<p class="step"><b>Method (brief).</b> Focus a distant window on the wall to get an approximate \(f\).
Set the object pin at 0 cm and the lens at 70.0 cm; looking from beyond the image pin, move the image pin until its
tip and the tip of the inverted image move together when the eye is moved sideways (no parallax). Read \(v\).
Repeat for the other values of \(u\).</p>""" + SAMPLE + rf"""
<p class="step">(ii) Approximate focal length (distant object): <b>f = {F.P1_F_APPROX:.1f} cm</b>.</p>
<p class="step">(v)–(vii) Observations (least count of the scale 0.1 cm):</p>
<div class="tbl"><table><tr><th>S. No.</th><th>u (cm)</th><th>v (cm)</th><th>x = u − f (cm)</th>
<th>y = 100/(v − f) (cm⁻¹)</th></tr>{_rows1}</table></div>
<p class="step">Graph of \(y\) against \(x\): a straight line through (very nearly) the origin; the best-fit line is
drawn with the points evenly on both sides of it.</p>{{{{fig:0}}}}
<p class="step">(viii) Slope from two points P and Q on the line (not plotted points), more than half the line apart:
\(m = \dfrac{{\Delta y}}{{\Delta x}} = \dfrac{{{_yb:.2f} - {_ya:.2f}}}{{{F.P1_XB:.1f} - {F.P1_XA:.1f}}}\)</p>
<p class="step">(ix) <span class="box">\(m = {P1_SLOPE:.3f}\) cm\(^{{-2}}\)</span> &nbsp;
\(f = \dfrac{{10}}{{\sqrt{{m}}}} = \dfrac{{10}}{{\sqrt{{{P1_SLOPE:.3f}}}}}\) = <span class="box">{P1_FOCAL:.1f} cm</span></p>
<p class="step"><b>Why it works:</b> Newton's form of the lens formula, \((u-f)(v-f) = f^2\), gives
\(y = \dfrac{{100}}{{v-f}} = \dfrac{{100}}{{f^2}}(u-f) = \dfrac{{100}}{{f^2}}\,x\), so the slope is \(m = 100/f^2\) and
\(f = 10/\sqrt m\).</p>
<p class="step"><b>Precautions:</b> tips of the pins and the optical centre on one horizontal line; remove parallax
tip to tip, with the eye at least 25 cm from the image pin; apply index correction if the bench scale requires it.</p>""",
          topic=RAY, recall=r"""<ul><li>Lens formula (real-is-positive distances) \(\frac1u+\frac1v=\frac1f\) ⇔ Newton \((u-f)(v-f)=f^2\).</li>
<li>No parallax: image and pin move together when the eye moves sideways.</li>
<li>Slope from two well-separated points on the line, to 3 s.f.</li></ul>"""),
        SEC("Question 2"),
        Q("2", 8, r"""<p><b>A.</b> This experiment determines resistivity of the material of the given wire.</p>
<p>You are provided with one-meter long wire AB attached to a meter scale with terminals at the two ends. You are also
provided with a resistance box RB, a voltmeter of range 0-3 V, an ammeter of range 0-1A, a 4V dc power supply 'E', a
plug key K, a jockey J and a few connecting wires.</p>
<p>(i) Determine and record the least count of the given voltmeter and ammeter with proper units in the answer
booklet.</p>
<p>(ii) Set up a circuit as shown in <b><i>Figure 2</i></b> below. Ensure that all connections are right and tight.</p>
{{fig:0}}
<p>(iii) Take out 1 ohm plug from the resistance box so that R = 1 ohm. Ensure that all other plugs are tightly closed.
Place the jockey J at a point C on the wire AB, such that AC = 80 cm. The reading of the voltmeter as well as the
ammeter must be within its range. Read and record the readings of the voltmeter and the ammeter, i.e. V and I, with
proper units.</p>
<p>(iv) Repeat the experiment to obtain four more sets of reading R, V and I by increasing the resistance R by 1 ohm
each time. Ensure that the jockey is always kept at the same position C such that AC = 80 cm in all five sets of
readings.</p>
<p>(v) Show any one of the readings in (iv) above to the visiting examiner.</p>
<p>(vi) Determine the value of resistance <b>r</b> using: <b>r = V/I</b> for each set, correct upto <b>three
significant figures.</b></p>
<p>(vii) Now, tabulate all the <b>five sets</b> of values of <b>R, V, I and r</b> with proper units.</p>
<p>(viii) Find \(\mathbf{r_0}\), the mean of all the five values of r and record its value in your answer booklet.</p>
<p><b>B.</b> (i) Determine and record the least count of the given micrometer screw gauge in <b>cm.</b><br>
(ii) Using it, calculate the diameter 'd' of the given specimen wire 'X' and record its value in <b>cm</b> in your
answer booklet.<br>(iii) Calculate the <b>resistivity</b> ρ of the material of the wire, using the formula:
\(\rho = \dfrac{\pi d^2 r_0}{320}\)</p>""",
          qfig=F.fig_p2_circuit,
          a=r"""<p class="step"><b>A (i) Least counts</b> (one division of each meter; the values below are those of the
school's meters): voltmeter (0–3 V) <b>0.05 V</b>; ammeter (0–1 A) <b>0.02 A</b>.</p>
<p class="step"><b>Method.</b> The voltmeter reads the p.d. \(V\) across AC = 80.0 cm of the wire, the ammeter the
current \(I\) through it, so \(r = V/I\) is the resistance of 80.0 cm of wire. Changing \(R\) changes \(I\); the
ratio \(V/I\) should stay constant (Ohm's law).</p>""" + SAMPLE + rf"""
<div class="tbl"><table><tr><th>S. No.</th><th>R (Ω)</th><th>V (V)</th><th>I (A)</th><th>r = V/I (Ω)</th></tr>
{_rows2}</table></div>
<p class="step">(viii) \(r_0 = \dfrac{{{' + '.join(_r3)}}}{{5}}\) = <span class="box">\(r_0 = {R0:.2f}\ \Omega\)</span>
(resistance of 80.0 cm of the wire).</p>
<p class="step"><b>B (i)</b> Micrometer: pitch 0.5 mm, 50 circular-scale divisions ⇒ least count
\(= 0.5/50 = 0.01\) mm = <b>0.001 cm</b> (zero error, if any, to be subtracted).</p>
<p class="step">(ii) Diameter at four places, in two perpendicular directions (sample readings):
{', '.join(f'{x:.3f}' for x in F.P2_D)} cm; mean <span class="box">\(d = {D:.3f}\) cm</span></p>
<p class="step">(iii) \(\rho = \dfrac{{\pi d^2 r_0}}{{320}} = \dfrac{{3.142\times({D:.3f})^2\times{R0:.2f}}}{{320}}\) =
<span class="box">\(\rho = {RHO*1e5:.2f}\times10^{{-5}}\ \Omega\) cm</span> \(= {RHO*1e5:.2f}\times10^{{-7}}\ \Omega\) m — of the order expected
for constantan.</p>
<p class="step"><b>Where 320 comes from:</b> \(\rho = \dfrac{{r_0 A}}{{l}} = \dfrac{{r_0\,\pi d^2/4}}{{80}} = \dfrac{{\pi d^2 r_0}}{{320}}\)
with \(l = AC = 80.0\) cm, so \(d\) in cm gives \(\rho\) in Ω cm.</p>
<p class="step"><b>Precautions:</b> keep the key open between readings so the wire does not heat; press the jockey
gently at the same point C; meter readings within range and read without parallax; measure \(d\) at several places
in perpendicular directions.</p>""".replace("{{fig:0}}", ""),
          topic=CE, recall=r"""<ul><li>Ohm's law \(V = Ir\); resistivity \(\rho = rA/l\), \(A = \pi d^2/4\).</li>
<li>Least count = value of one smallest division; micrometer LC = pitch / number of circular divisions.</li>
<li>Readings recorded to the least count; derived values to the figures asked.</li></ul>"""),
        SEC("Question 3", "Show the following to the Visiting Examiner for assessment:"),
        Q("3(a)", 7, r"""<p>Project Report</p>""",
          a=r"""<p class="step">Not a written answer: the Visiting Examiner assesses the project report. Under ISC 2027
the project carries 10 marks and may be theoretical, a working model, or an investigatory experiment. The report
should contain: title, abstract, theory, experimental set-up / model description, observations with tables, graph
or chart, analysis and discussion of results, conclusion and bibliography, and must be the candidate's own work.</p>""",
          topic="Practical — Project work", recall=r"""<ul><li>ISC 2027: Project work 10 marks, Practical file 5 marks.</li></ul>"""),
        Q("3(b)", 3, r"""<p>Physics Practical File.</p>""",
          a=r"""<p class="step">Not a written answer: the Visiting Examiner assesses the practical file kept through the
year — each experiment with aim, apparatus, circuit/ray diagram, observations in tables with units and least counts,
graph, calculation, result and precautions.</p>""",
          topic="Practical — Practical file", recall=r"""<ul><li>Practical file: record of all experiments in the ISC list, signed by the teacher.</li></ul>"""),
    ])
