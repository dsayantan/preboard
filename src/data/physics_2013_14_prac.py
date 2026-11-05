"""Heritage School Pre-Board 2013-14, Physics Paper 2 (Practical) — digital copy and worked solutions with
sample readings.  Transcribed from the page images."""
from kit import Q, SEC
import physics_2013_14_figs as F

RAY = "Optics — Ray Optics (Practical 1: f of a convex lens, no-parallax method)"
MB = "Current Electricity (Practical 8: metre bridge, resistance of a wire)"

SAMPLE = '<p class="note">The readings below are <b>sample readings</b> generated from plausible apparatus values ' \
         '(rounded to the least count) to show how the answer is set out — in the examination you record your own.</p>'

PAPER = dict(
    subject="physics", year="2013-14", slug="2013-14-practical", paper="Paper 2 (Practical)", practical=True,
    source="PreBoard-PYQ/2013-14/Physics Practical Paper 2.pdf", marks=20, time="3 hours",
    intro=r"""<p><i>(Candidates are allowed additional 15 minutes for only reading the paper. They must NOT start writing
during this time.)</i></p>
<p>ALL ANSWERS MUST BE WRITTEN IN THE ANSWER BOOKLET PROVIDED SEPARATELY.</p>
<p><i>If squared paper is used, it must be attached to the answer booklet.</i></p>
<p><i>Marks are given for a clear record of observations actually made, for their suitability and accuracy, and for
the use made of them.</i></p>
<p><i>A brief statement of the method may be given if necessary. The theory of the experiment is not required unless
specifically asked for.</i></p>
<p><i>Candidates are advised to record their observations as soon as they have been made.</i></p>
<p><i>All working, including rough work, should be done on the same sheet as, and adjacent to, the rest of the
answer.</i></p>
<p><i>Mathematical tables and squared paper are provided. The intended marks for questions or parts of questions are
given in brackets [ ].</i></p>
<p>Answer <b>all</b> questions.</p>
<p><i>You should not spend more than one and a half hours on Question 1.</i></p>
<p class="note">[This paper is for 20 marks; the current ISC practical paper is 15 marks, with 15 more for project and file.]</p>""",
    items=[
        SEC("Answer all questions"),
        Q("1", 10, r"""<p>This experiment determines the focal length of the given convex lens by no parallax method.
You are provided with: (i) an optical bench (ii) a lens holder (iii) a convex lens (iv) two optical pins.</p>
<p>Determine approximate focal length F of the given convex lens by projecting the image of a distant object formed by
the lens on a wall or a screen. Record the value of F in cm up to one decimal place. Mount the given convex lens on the
lens holder. Adjust the heights of object pin 'O' and image pin 'I' so that their tips lie on the principal axis of the
lens. Keep the object pin 'O' to the left of the convex lens L and image pin 'I' to the right of the lens, as shown in
Figure 1.</p>{{fig:0}}
<p>Keep the object pin at zero cm mark and the convex lens at 70 cm mark; so that the object distance u = OL = 70 cm.
Look at the object pin through the lens, from a distance. You would see an inverted image (say I') of the object pin.
Adjust the position of the image pin I in such a way, that there is no parallax between I' and I. Ensure that it is a
'tip to tip' parallax. At no parallax, note the position of the image pin. Measure the image distance v = LI, i.e.
distance of the image pin from the lens in cm correct up to one decimal place. Record this value of v in your answer
book.</p>
<p>Calculate \(x = u - F\) and \(y = \dfrac{100}{v-F}\), both up to one decimal place.</p>
<p>Now, repeat the experiment for u = 60 cm, 50 cm, 40 cm, 30 cm and 20 cm. Each time, find v, x and y. Now, tabulate
all <i>six</i> sets of values of u, v, x and y with their units. Plot a graph of y vs. x. Draw the line of best fit.</p>
<p>Determine its slope m using the equation: \(m = \dfrac{\Delta y}{\Delta x}\). Record the value of m in your answer
book, correct up to <i>three</i> significant figures.</p>
<p>Calculate f using: \(f = \dfrac{10}{\sqrt m}\) and record its value in your answer book, correct up to <i>one</i>
decimal place.</p>""",
          qfig=[(F.fig_pr_bench, "Figure 1")],
          a=SAMPLE + r"""
<p class="step"><b>Approximate focal length</b> (image of a distant window on the wall): <b>F = 15.0 cm</b>.</p>
<p class="step"><b>Observations</b> (object pin at 0.0 cm; v read at no parallax, tip to tip):</p>
<div class="tbl"><table>
<tr><th>S. No.</th><th>u (cm)</th><th>v (cm)</th><th>x = u − F (cm)</th><th>y = 100/(v − F) (cm\(^{-1}\))</th></tr>
<tr><td>1</td><td>70.0</td><td>19.1</td><td>55.0</td><td>24.4</td></tr>
<tr><td>2</td><td>60.0</td><td>20.1</td><td>45.0</td><td>19.6</td></tr>
<tr><td>3</td><td>50.0</td><td>21.5</td><td>35.0</td><td>15.4</td></tr>
<tr><td>4</td><td>40.0</td><td>24.1</td><td>25.0</td><td>11.0</td></tr>
<tr><td>5</td><td>30.0</td><td>30.1</td><td>15.0</td><td>6.6</td></tr>
<tr><td>6</td><td>20.0</td><td>60.1</td><td>5.0</td><td>2.2</td></tr></table></div>
<p class="step"><b>Graph</b> of y against x (origin at (0, 0), uniform scales using most of the sheet):</p>
{{fig:0}}
<p class="step"><b>Slope</b> from two points on the line (not plotted points), far apart:
\(m = \dfrac{\Delta y}{\Delta x} = \dfrac{24.67 - 1.73}{56.0 - 4.0} = \dfrac{22.94}{52.0}\)
⇒ <span class="box">\(m = 0.441\ \mathrm{cm^{-2}}\)</span></p>
<p class="step"><b>Focal length</b>: \(f = \dfrac{10}{\sqrt m} = \dfrac{10}{\sqrt{0.441}} = \dfrac{10}{0.6641}\)
⇒ <span class="box">\(f = 15.1\ \mathrm{cm}\)</span></p>
<p class="step"><b>Why the method works</b> (not required in the answer): from \(\frac1v+\frac1u=\frac1f\) with
real distances positive one gets Newton's form \((u-f)(v-f)=f^2\). With \(F\approx f\),
\(y = \dfrac{100}{v-f} = \dfrac{100}{f^2}(u-f) = \dfrac{100}{f^2}\,x\), a straight line through the origin of slope
\(m = 100/f^2\), hence \(f = 10/\sqrt m\).</p>
<p class="step"><b>Precautions:</b> tips of O, I and the optical centre of L on one horizontal line; parallax removed
tip to tip with the eye at least 25 cm behind I; index correction (bench error) applied if the pins are not at the
marked positions.</p>""",
          afig=[(F.fig_pr_graph1, "Sample graph: y = 100/(v − F) against x = u − F, best-fit line and slope triangle.")],
          topic=RAY, recall=r"<ul><li>Lens formula \(\frac1v+\frac1u=\frac1f\) (real distances positive) ⇔ \((u-f)(v-f)=f^2\).</li><li>No parallax: image and pin move together when the eye moves sideways.</li><li>Slope: two far-apart points on the line, covering more than half of it.</li></ul>"),
        Q("2", 7, r"""<p>This experiment determines the resistance of a metallic wire. You are provided with:
(i) a 100 cm long and uniform wire AB attached to a meter scale on a wooden board. (ii) a 50 cm long and uniform
wire R on a wooden frame. (iii) a 10 cm long specimen wire W on a piece of card board. (iv) a Resistance Box.
(v) a dc source E (vi) a central zero galvanometer G (vii) a plug key K. (viii) a jockey J. (ix) a few connecting
wires. (x) a micrometer Screw Gauge.</p>
<p>Arrange the given apparatus as shown in <i>Figure 2</i> below. Connect various components as shown in Figure 2.
Ensure that all connections are tight.</p>{{fig:0}}
<p>Close the key K. Introduce a resistance x = 1 Ω in the branch MD by removing a 1 Ω plug from the resistance box.
All other plugs must be kept tightly closed. Press the jockey J lightly at different points on the wire AB till at a
certain point C, the galvanometer G shows no deflection. Note and record the length \(l\) = AC, correct up to 0.1 cm.</p>
<p>Repeat the experiment for x = 2 Ω, 3 Ω, 4 Ω, 5 Ω and 6 Ω. (x should be in the range of 1–10 Ω). Find the null point
each and every time and record the different values of \(l\).</p>
<p>For each value of x, calculate \(y = \dfrac{l}{(100-l)}\) correct up to second decimal place.</p>
<p>Now tabulate all six sets of values of x, \(l\) and y. Plot a graph of y versus x. Draw the line of best fit.
Determine its slope S using: \(S = \dfrac{\Delta y}{\Delta x}\)</p>
<p>Record its value in your answer book, correct up to three significant figures.</p>
<p>Calculate resistance R of the wire using: \(R = \dfrac1S\) and record its value up to one decimal place, with its
unit.</p>""",
          qfig=[(F.fig_pr_bridge, "Figure 2")],
          a=SAMPLE + r"""
<p class="step"><b>Observations</b> (null point C measured from end A; jockey pressed lightly):</p>
<div class="tbl"><table>
<tr><th>S. No.</th><th>x (Ω)</th><th>\(l\) = AC (cm)</th><th>100 − \(l\) (cm)</th><th>y = \(l\)/(100 − \(l\))</th></tr>
<tr><td>1</td><td>1</td><td>28.6</td><td>71.4</td><td>0.40</td></tr>
<tr><td>2</td><td>2</td><td>44.3</td><td>55.7</td><td>0.80</td></tr>
<tr><td>3</td><td>3</td><td>54.7</td><td>45.3</td><td>1.21</td></tr>
<tr><td>4</td><td>4</td><td>61.5</td><td>38.5</td><td>1.60</td></tr>
<tr><td>5</td><td>5</td><td>66.8</td><td>33.2</td><td>2.01</td></tr>
<tr><td>6</td><td>6</td><td>70.5</td><td>29.5</td><td>2.39</td></tr></table></div>
<p class="step"><b>Graph</b> of y against x (origin at (0, 0), uniform scales using most of the sheet):</p>{{fig:0}}
<p class="step"><b>Slope:</b> \(S = \dfrac{\Delta y}{\Delta x} = \dfrac{2.60 - 0.20}{6.50 - 0.50} = \dfrac{2.40}{6.00}\)
⇒ <span class="box">\(S = 0.400\ \Omega^{-1}\)</span></p>
<p class="step"><b>Resistance of the wire:</b> \(R = \dfrac1S = \dfrac{1}{0.400}\) ⇒ <span class="box">\(R = 2.5\ \Omega\)</span></p>
<p class="step"><b>Theory</b> (not required): at balance
\(\dfrac{x}{R} = \dfrac{\text{resistance of }AC}{\text{resistance of }CB} = \dfrac{l}{100-l} = y\), so y is
proportional to x with slope \(1/R\).</p>
<p class="step"><b>Precautions:</b> null point kept near the middle of the wire; jockey pressed gently (not slid);
current passed only while taking a reading; plugs of the box tight.</p>""",
          afig=[(F.fig_pr_graph2, "Sample graph: y = l/(100 − l) against x, best-fit line through the origin.")],
          topic=MB, recall=r"<ul><li>Balanced metre bridge: \(\frac PQ=\frac{l}{100-l}\).</li><li>Here P = x (box, left gap), Q = R (wire, right gap) ⇒ \(y = x/R\).</li><li>Best accuracy when l is near 50 cm.</li></ul>"),
        Q("3", 3, r"""<p>You are provided with a specimen wire W and a micrometer screw gauge. Determine and record its least count
in mm. Now determine the diameter d of the specimen wire, using the screw gauge and record its value in mm.</p>
<p>Calculate K using: \(K = \dfrac{\pi R d^2}{200}\) where R is the resistance of the wire obtained in Question 2.</p>
<p>(Note: R is not the radius of the wire and K is not the specific resistance.)</p>""",
          a=SAMPLE + r"""
<p class="step"><b>Least count</b> = pitch / number of circular-scale divisions = \(\dfrac{0.5\ \mathrm{mm}}{50}\)
⇒ <span class="box">LC = 0.01 mm</span> (zero error: nil).</p>
<div class="tbl"><table>
<tr><th>S. No.</th><th>Main scale (mm)</th><th>Circular scale div.</th><th>d = MS + CSD × LC (mm)</th></tr>
<tr><td>1</td><td>0.0</td><td>36</td><td>0.36</td></tr>
<tr><td>2 (⟂ to 1)</td><td>0.0</td><td>35</td><td>0.35</td></tr>
<tr><td>3 (another place)</td><td>0.0</td><td>37</td><td>0.37</td></tr></table></div>
<p class="step">Mean diameter <span class="box">d = 0.36 mm</span></p>
<p class="step">\(K = \dfrac{\pi R d^2}{200} = \dfrac{3.142\times2.5\times(0.36)^2}{200} = \dfrac{3.142\times2.5\times0.1296}{200}\)
⇒ <span class="box">\(K = 5.09\times10^{-3}\)</span> (with d in mm, R in Ω)</p>
<p class="step">What K means: the resistivity of the 50 cm wire is \(\rho = \dfrac{R\,\pi d^2}{4L}\). With d in mm and
L = 500 mm, \(\rho = \dfrac{\pi R d^2}{2000}\ \Omega\,\mathrm{mm} = K\times10^{-4}\ \Omega\,\mathrm m
\approx 5.1\times10^{-7}\ \Omega\,\mathrm m\) (a constantan-like alloy).</p>""",
          topic="Current Electricity (Practical 8: specific resistance — diameter by screw gauge)",
          recall=r"<ul><li>LC = pitch / no. of circular divisions.</li><li>Take readings in two perpendicular directions at several places; subtract zero error.</li><li>\(\rho = RA/L = R\pi d^2/4L\).</li></ul>"),
    ])
