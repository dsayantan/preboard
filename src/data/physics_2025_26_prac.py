"""Heritage School Pre-Board 2025-26, Physics Paper 2 (Practical) — digital copy, ISC 2027 filter, solutions.
Source of record: SET-1/PHYSICS PRACTICALS.docx; transcribed from its rendered pages.
Sample readings and every derived value are generated and checked in src/checks/physics_2025_26_prac_check.py."""
from kit import Q, SEC
import physics_2025_26_figs as F

RAY = "Practical — Ray Optics (convex lens by u–v / no-parallax method)"
CE = "Practical — Current Electricity (resistance of a wire from V and I)"

SAMPLE = '<p class="note">The readings below are <b>sample readings</b>, generated for a convex lens of focal length ' \
         'about 15 cm and rounded to the least count; your own readings will differ.</p>'

PAPER = dict(
    subject="physics", year="2025-26", slug="2025-26-practical", paper="Paper 2 (Practical)", practical=True,
    source="PreBoard-PYQ/2025-26/SET-1/PHYSICS PRACTICALS.docx", marks=30, time="Three hours",
    intro=r"""<p><i>(Candidates are allowed additional 15 minutes for <b>only</b> reading the paper. They must NOT start
writing during this time.)</i></p>
<p>Subject Code 861/2.</p>
<p><b>ALL ANSWERS MUST BE WRITTEN IN THE ANSWER BOOKLET PROVIDED SEPARATELY.</b></p>
<p><i>If squared paper is used, it must be attached to the answer booklet. Marks are given for a clear record of
observations actually made, for their suitability and accuracy, and for the use made of them. Statement of the theory,
<b>procedure of the experiment, apparatus, circuit diagrams, precautions are not required to be written unless
specifically asked for.</b> Candidates are advised to record their observations as soon as they have been made. All
working, including rough work, should be done on the same sheet as, and adjacent to, the rest of the answer.
Mathematical tables and squared paper are provided. The intended marks for questions or parts of questions are given in
brackets [ ].</i></p>
<p>Answer <b>all</b> questions. <b><i>You should not spend more than one and a half hours on each question.</i></b></p>
<p><i>In addition to the Practical Paper, candidates will also be evaluated in the following: Project Work — 10 marks;
Practical File — 5 marks.</i></p>""",
    items=[
        SEC("Question 1"),
        Q("1", 9, r"""<p>This experiment determines the <b>focal length</b> of the given Convex lens by <b>no parallax method</b>.</p>
<p>You are provided with: (a) A lens holder (b) A Convex lens (c) Two optical pins (d) An optical bench</p>
<ol type="i">
<li>Arrange the object pin <b>O</b>, the image pin <b>I</b> and the lens <b>L</b> on an optical bench or a tabletop as
shown in <b><i>Figure 1</i></b> below. Adjust the height of the object pin <b>O</b> and that of the image pin <b>I</b> so
that their tips lie on the principal axis of the lens. {{fig:0}}</li>
<li>Place the object pin <b>O</b> at the 0·0 cm mark and the lens <b>L</b> at the ___ cm mark so that the object
distance <b><i>u</i> = 20 cm</b> (i.e. the distance between the lens and the object pin).</li>
<li>Look at the tip of the object pin <b>O</b> through the lens from a distance so that you see an inverted image (I′)
of the object pin.</li>
<li>Now, adjust the position of the image pin I in such a way, that there is <b>no parallax</b> between I and I′.
Ensure that <b>tip to tip</b> parallax is removed.</li>
<li>At no parallax, note the position of the image pin <b>I</b> and record the image distance <i>v</i> = LI (i.e. the
distance between the lens and the image pin) in cm, correct up to <b>one decimal place</b>.</li>
<li>Repeat the experiment for <b>five</b> more values of <b><i>u</i></b>, i.e. <b><i>u</i> = 25 cm, 30 cm, 35 cm,
40 cm, and 45 cm.</b> Each time, remove the parallax and find the value of <b><i>v</i></b>.</li>
<li>For <b>each</b> value of <i>u</i>, calculate \(x = u\cdot v\) &amp; \(y = u + v\) and record their values up to
<b>two decimal places</b>.</li>
<li>Tabulate all <b>Six</b> sets of <b><i>u</i></b>, <b><i>v</i></b>, <b><i>x</i></b>, and <b><i>y</i></b> with their
<b>units.</b></li>
<li>Now plot a graph of y vs x.</li>
<li>Draw the <b>best fit line</b>. (<i>It must be thin and uniform.</i>)</li>
<li>Find its slope <i>S</i>, using \(S = \dfrac{\text{change in } y}{\text{change in } x} = \dfrac{y_2 - y_1}{x_2 - x_1}\)</li>
<li>Record the value of <b><i>S</i></b>, rounded up to <b>three significant figures</b>.</li>
<li>Determine: \(F = \dfrac{1}{S}\) for <b>each</b> set and record its value correct up to <b>one decimal place with
Unit</b>.</li></ol>
<p><b>Show the image position when the parallax has been removed, in any one of the readings in (vi) above, to the
Visiting Examiner.</b></p>
<p class="note">[The printed slope formula reads "change∈y / change∈x" — an equation-editor slip for "change in y /
change in x". Step (xiii) says "for each set", but F = 1/S comes from the single slope of the graph, so there is one
value of F.]</p>""",
          qfig=[(F.fig_p1_bench, "Figure 1 (redrawn)")],
          a=SAMPLE + r"""<p><b>Theory (for the practical file; not required in the answer booklet).</b> With all distances taken
as positive magnitudes for a real image, \(\dfrac1u + \dfrac1v = \dfrac1f\) ⇒ \(f = \dfrac{uv}{u+v}\) ⇒
\(u + v = \dfrac{1}{f}\,(uv)\), i.e. \(y = \dfrac{1}{f}\,x\). So the graph of y against x is a straight line of slope
\(S = 1/f\), and \(F = 1/S\) is the focal length.</p>
<p class="step">(ii) Object pin at 0.0 cm, so the lens is placed at the <b>20.0 cm</b> mark for \(u = 20.0\) cm.</p>
<p class="step"><b>Observations</b> (bench scale least count 0.1 cm):</p>
<table><tr><th>S. No.</th><th><i>u</i> (cm)</th><th>image pin at (cm)</th><th><i>v</i> (cm)</th><th>\(x = uv\) (cm²)</th><th>\(y = u + v\) (cm)</th></tr>
<tr><td>1</td><td>20.0</td><td>80.4</td><td>60.4</td><td>1208.00</td><td>80.40</td></tr>
<tr><td>2</td><td>25.0</td><td>62.3</td><td>37.3</td><td>932.50</td><td>62.30</td></tr>
<tr><td>3</td><td>30.0</td><td>60.2</td><td>30.2</td><td>906.00</td><td>60.20</td></tr>
<tr><td>4</td><td>35.0</td><td>61.1</td><td>26.1</td><td>913.50</td><td>61.10</td></tr>
<tr><td>5</td><td>40.0</td><td>64.1</td><td>24.1</td><td>964.00</td><td>64.10</td></tr>
<tr><td>6</td><td>45.0</td><td>67.4</td><td>22.4</td><td>1008.00</td><td>67.40</td></tr></table>
<p class="step"><b>Graph</b> of y against x: origin shifted to (880, 58) so that the points spread over more than 60% of
the paper; scale x: 1 small division = 10 cm², y: 1 small division = 0.25 cm. The best-fit line is drawn with the points
evenly on either side. {{fig:0}}</p>
<p class="step"><b>Slope</b> from two points on the line that are not plotted points, P(920, 61.37) and
Q(1200, 79.91):</p>
<p class="step">\(S = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{79.91 - 61.37}{1200 - 920} = \dfrac{18.54}{280}\)
⇒ <span class="box">\(S = 0.0662\ \text{cm}^{-1}\)</span> (3 s.f.)</p>
<p class="step">\(F = \dfrac{1}{S} = \dfrac{1}{0.0662}\) ⇒ <span class="box">\(F = 15.1\) cm</span></p>
<p class="step"><b>Result:</b> the focal length of the given convex lens is 15.1 cm.</p>
<p class="step"><b>Precautions</b> (for the file): tips of O, I and the lens centre at one height on the principal
axis; parallax removed tip to tip, keeping the eye at least 25 cm from the image pin; distances measured between the
index marks of the stands (index correction if any).</p>""",
          afig=[(F.fig_p1_graph, "Sample graph: y = u + v against x = uv, with the slope triangle")],
          topic=RAY, recall=r"<ul><li>\(1/u + 1/v = 1/f\) (magnitudes, real image) ⇒ \(u+v = uv/f\).</li><li>Slope from two non-plotted points far apart on the line; S to 3 s.f., F to 1 d.p. with unit.</li><li>Real image exists only for \(u \gt f\); at \(u = 2f\), \(v = 2f\).</li></ul>"),

        SEC("Question 2"),
        Q("2", 6, r"""<p>This experiment determines the <b>resistance of</b> the given wire.</p>
<p>You are provided with: a) A 100 cm long uniform metallic wire <b>AB</b> stretched along a metre scale and provided with
terminals at both ends. b) A resistance box <b>R.B.</b>, c) A voltmeter of range 0–3 V d) An ammeter of range 0–1 A
e) <b>DC source E</b> f) A plug key 'K', g) A jockey '<b>J</b>' and h) A few connecting wires.</p>
<ol type="i">
<li>Determine and record the <b>least count</b> of the given with proper <b>units</b> in your answer booklet.
I. voltmeter II. ammeter with proper <b>units</b> in your answer booklet.</li>
<li>Set up a circuit as shown in <b><i>Figure 2</i></b> below. Make sure that all connections are tight. {{fig:0}}</li>
<li>Take out 1 Ω plug from the resistance box R.B. so that R = 1 Ω. Ensure that all other plugs are tightly closed.
Place the jockey <b>J</b> at a point <b>C</b> on the wire AB, such that AC = x = 80 <b>cm.</b> The reading of the
voltmeter as well as the ammeter must be <b>within its range</b>. Read and record the readings of the voltmeter and the
ammeter, i.e. <b>V</b> and <b>I,</b> with proper units.</li>
<li>Repeat the experiment to obtain <b>five more</b> sets of readings of <b>R</b>, <b>V</b> and <b>I</b> by taking
resistance R = 2 Ω, 3 Ω, 4 Ω, 5 Ω and 6 Ω. Ensure that the jockey is <b>always</b> kept at the <b>same position C</b>
such that AC = x cm in <b>all six sets</b> of readings.</li>
<li><b>Show any one of the readings in (iv) above, to the Visiting Examiner.</b></li>
<li>Determine the value of resistance r using: \(r = V/I\) for each set, correct <b>up to one decimal place.</b></li>
<li>Now, tabulate all the <b>six sets</b> of values of <b>R</b>, <b>V,</b> I and <b>r</b> with proper units.</li>
<li>Find <b>r<sub>0</sub></b>, the mean of all the six values of r and record its value in your answer booklet.</li></ol>""",
          qfig=[(F.fig_p2_circuit, "Figure 2 (redrawn)")],
          a=r"""<p class="note">The readings below are <b>sample readings</b>, generated for a wire of about 0.04 Ω cm\(^{-1}\)
(4 Ω for the whole 100 cm) driven by a 3 V source, and rounded to the meters' least counts; your own readings will
differ.</p>
<p class="step"><b>(i) Least counts</b> (each meter has its range divided into equal small divisions;
least count = range ÷ number of divisions; the values below are those of the school's meters, as given in the Lab Manual):<br>
I. Voltmeter (0–3 V, 60 divisions): \(\text{LC} = 3/60 =\) <span class="box">0.05 V</span><br>
II. Ammeter (0–1 A, 50 divisions): \(\text{LC} = 1/50 =\) <span class="box">0.02 A</span></p>
<p class="step"><b>Theory</b> (for the file): the ammeter measures the current I through the wire; the voltmeter, joined
between A and the jockey at C, measures the p.d. V across the length AC = 80 cm. By Ohm's law the resistance of that
80 cm is \(r = V/I\). Changing R in the resistance box changes I (and V in proportion), so each set gives an
independent value of the same r.</p>
<p class="step"><b>Observations</b> (AC = x = 80.0 cm in every set):</p>
<table><tr><th>S. No.</th><th>R (Ω)</th><th>V (V)</th><th>I (A)</th><th>\(r = V/I\) (Ω)</th></tr>
<tr><td>1</td><td>1</td><td>1.85</td><td>0.58</td><td>3.2</td></tr>
<tr><td>2</td><td>2</td><td>1.55</td><td>0.48</td><td>3.2</td></tr>
<tr><td>3</td><td>3</td><td>1.35</td><td>0.42</td><td>3.2</td></tr>
<tr><td>4</td><td>4</td><td>1.15</td><td>0.36</td><td>3.2</td></tr>
<tr><td>5</td><td>5</td><td>1.05</td><td>0.32</td><td>3.3</td></tr>
<tr><td>6</td><td>6</td><td>0.95</td><td>0.30</td><td>3.2</td></tr></table>
<p class="step">e.g. set 1: \(r = \dfrac{1.85}{0.58} = 3.19 \approx 3.2\ \Omega\); set 5: \(\dfrac{1.05}{0.32} = 3.28
\approx 3.3\ \Omega\).</p>
<p class="step"><b>(viii)</b> \(r_0 = \dfrac{3.2 + 3.2 + 3.2 + 3.2 + 3.3 + 3.2}{6} = \dfrac{19.3}{6} = 3.22\)
⇒ <span class="box">\(r_0 = 3.2\ \Omega\)</span></p>
<p class="step"><b>Result:</b> resistance of 80 cm of the wire = 3.2 Ω (≈ 0.04 Ω per cm).</p>
<p class="step"><b>Precautions</b> (for the file): meters connected with + to the higher-potential side (current enters
the wire at A); key closed only while reading, so the wire does not heat up; jockey pressed gently and always at the
same point C; readings within range and recorded to the least count.</p>""",
          topic=CE, recall=r"<ul><li>Least count = range ÷ number of divisions (school meters: 0.05 V, 0.02 A).</li><li>Ohm's law \(r = V/I\); a series R only changes the current, not r.</li><li>Every reading must be a whole number of least counts.</li></ul>"),
    ])
