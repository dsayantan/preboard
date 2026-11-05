"""Heritage School Pre-Board 2016-17, Physics Paper 1 (Theory) — digital copy, ISC 2027 filter, solutions.
The PDF is a scan with no text layer; transcribed from the page images."""
from kit import Q, SEC
import physics_2016_17_figs as F

ES, CE, MAG = "Electrostatics", "Current Electricity", "Magnetic Effects of Current and Magnetism"
EMI, EMW = "Electromagnetic Induction and Alternating Currents", "Electromagnetic Waves"
RAY, WAVE = "Optics — Ray Optics", "Optics — Wave Optics"
DUAL, ATOM, NUC, ELEC = ("Dual Nature of Radiation and Matter", "Atoms and Nuclei — Atoms",
                         "Atoms and Nuclei — Nuclei", "Electronic Devices")

DIPOLE_A = r"""<p class="step"><span class="box">\(\vec\tau = \vec p\times\vec E\)</span>, magnitude
\(\tau = pE\sin\theta\), \(\theta\) = angle between \(\vec p\) and \(\vec E\).</p>
<p class="step">(i) Maximum, \(\tau = pE\), when \(\theta = 90^\circ\): dipole axis perpendicular to the field.</p>
<p class="step">(ii) Zero when \(\theta = 0^\circ\) (stable) or \(180^\circ\) (unstable): axis along the field.</p>
{{fig:0}}"""

PAPER = dict(
    subject="physics", year="2016-17", slug="2016-17", paper="Paper 1 (Theory)",
    source="PreBoard-PYQ/2016-17/PHYSICS PAPER I.pdf", marks=70, time="3 hours",
    intro=r"""<p><i>Candidates are allowed additional 15 minutes for only reading the paper. They must NOT start
writing during this time.</i></p>
<p>Answer all questions in <b>Part I</b> and <b>ten</b> questions from <b>Part II</b>, choosing <b>four</b>
questions from <b>Section A</b>, <b>three</b> questions from <b>Section B</b> and <b>three</b> questions from
<b>Section C</b>. All working, including rough work, should be done on the same sheet as, and adjacent to, the rest
of the answer. The intended marks for questions or part of questions are given in brackets [ ]. (Materials to be
supplied: Log tables including Trigonometric functions.) A list of useful physical constants is given at the end
of this paper.</p>
<p><b>Useful constants and relations</b> (as printed): charge of a proton \(e = 1.6\times10^{-19}\) C; Planck's
constant \(h = 6.6\times10^{-34}\) J s; mass of an electron \(m_e = 9.1\times10^{-31}\) kg; permittivity of vacuum
\(\varepsilon_0 = 8.85\times10^{-12}\) F m\(^{-1}\); Coulomb's constant \(1/4\pi\varepsilon_0 = 9\times10^{9}\) m F\(^{-1}\);
permeability of vacuum \(\mu_0 = 4\pi\times10^{-7}\) H m\(^{-1}\); Rydberg's constant \(R = 1.097\times10^{7}\) m\(^{-1}\);
speed of light in vacuum \(c = 3\times10^{8}\) m s\(^{-1}\).</p>""",
    items=[
        SEC("Part I (20 marks) — Question 1 A. Choose the correct alternative [5]", "Answer all questions."),
        Q("1(A)(i)", 1, r"""<p>Three equal charges are placed on the three corners of a square. If the force between
\(q_1\) and \(q_2\) is \(F_{12}\) and that between \(q_1\) and \(q_3\) is \(F_{13}\), then the ratio of magnitudes
\((F_{12}/F_{13})\) is</p><p>(a) \(\tfrac12\) &nbsp; (b) 2 &nbsp; (c) \(\tfrac{1}{\sqrt2}\) &nbsp; (d) \(\sqrt2\)</p>""",
          afig=F.fig_a1a1_square,
          a=r"""<p><b>(b) 2.</b></p>
<p class="step">The intended arrangement: \(q_2\) at a corner adjacent to \(q_1\) (distance \(a\)), \(q_3\) at the
diagonally opposite corner (distance \(\sqrt2a\)).</p>{{fig:0}}
<p class="step">\(F\propto 1/r^2\): \(\dfrac{F_{12}}{F_{13}} = \dfrac{(\sqrt2a)^2}{a^2} = 2\).</p>
<p class="note">[The question does not say which corners; if \(q_2\) and \(q_3\) were both adjacent to \(q_1\) the
ratio would be 1, which is not an option.]</p>""",
          topic=ES, recall=r"""<ul><li>Coulomb: \(F = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1q_2}{r^2}\).</li><li>Diagonal of a square = \(\sqrt2a\).</li></ul>"""),
        Q("1(A)(ii)", 1, r"""<p>Which of the following quantities does not change when a resistor connected to a battery
is heated due to current?</p><p>(a) Drift speed &nbsp; (b) Resistivity &nbsp; (c) Resistance &nbsp; (d) Number of
free electrons</p>""",
          a=r"""<p><b>(d) Number of free electrons.</b></p>
<p class="step">Heating increases the collision frequency (smaller relaxation time \(\tau\)), so resistivity and
resistance rise and the current and drift speed fall. The number of free electrons in a metal is fixed by the
material and does not change.</p>""",
          topic=CE, recall=r"""<ul><li>\(\rho = m/ne^2\tau\); in metals \(\tau\) decreases with temperature, \(n\) is constant.</li></ul>"""),
        Q("1(A)(iii)", 1, r"""<p>If two waves represented by \(y_1 = 4\sin\omega t\) and \(y_2 = 3\sin(\omega t+\pi/3)\)
interfere at a point, the amplitude of the resultant wave will be about</p>
<p>(a) 7 &nbsp; (b) 5 &nbsp; (c) 6 &nbsp; (d) 3.5</p>""",
          a=r"""<p><b>(c) 6.</b></p>
<p class="step">\(A = \sqrt{a_1^2 + a_2^2 + 2a_1a_2\cos\phi} = \sqrt{16 + 9 + 2(4)(3)\cos60^\circ} = \sqrt{37} \approx 6.1\).</p>""",
          topic=WAVE, recall=r"""<ul><li>Superposition of two SHMs of the same frequency: \(A^2 = a_1^2+a_2^2+2a_1a_2\cos\phi\).</li></ul>"""),
        Q("1(A)(iv)", 1, r"""<p>If the work function of potassium is 2 eV, then its photoelectric threshold wavelength
is</p><p>(a) 310 nm &nbsp; (b) 620 nm &nbsp; (c) 6200 nm &nbsp; (d) 3100 nm</p>""",
          a=r"""<p><b>(b) 620 nm.</b></p>
<p class="step">\(\lambda_0 = \dfrac{hc}{\phi_0} = \dfrac{6.6\times10^{-34}\times3\times10^{8}}{2\times1.6\times10^{-19}}
= 6.19\times10^{-7}\) m ≈ 620 nm (or \(1240/2\) nm).</p>""",
          topic=DUAL, recall=r"""<ul><li>\(\phi_0 = hc/\lambda_0\); shortcut \(\lambda(\text{nm}) \approx 1240/E(\text{eV})\).</li></ul>"""),
        Q("1(A)(v)", 1, r"""<p>In a n-type semiconductor, which of the following statement is true?</p>
<p>(a) Electrons are majority carriers and trivalent atoms are dopants.<br>(b) Electrons are minority carriers and
pentavalent atoms are dopants.<br>(c) Holes are minority carriers and pentavalent atoms are dopants.<br>(d) Holes are
majority carriers and trivalent atoms are dopants.</p>""",
          a=r"""<p><b>(c) Holes are minority carriers and pentavalent atoms are dopants.</b> A pentavalent donor
gives free electrons (majority carriers); holes, produced only thermally, are the minority.</p>""",
          topic=ELEC, recall=r"""<ul><li>n-type: pentavalent donor, electrons majority. p-type: trivalent acceptor, holes majority.</li></ul>"""),

        SEC("Part I — Question 1 B. Answer all questions given below briefly and to the point [15]"),
        Q("1(B)(i)", 1, r"""<p>A parallel plate condenser with air between the plates possesses the capacitance of
\(10^{-12}\) F. Now the plates are removed apart so that the separation is twice the original value. The space
between the plates is filled with a material of dielectric constant 4.0. Find the value of the capacitance.</p>""",
          a=r"""<p class="step">\(C = \dfrac{K\varepsilon_0A}{d}\): \(C' = \dfrac{4\,\varepsilon_0A}{2d} = 2C\) =
<span class="box">\(2\times10^{-12}\) F</span> (2 pF)</p>""",
          topic=ES, recall=r"""<ul><li>\(C = K\varepsilon_0A/d\).</li></ul>"""),
        Q("1(B)(ii)", 1, r"""<p>A charge of magnitude \(3e\) and mass \(2m\) is moving in an electric field \(\vec E\). Find the
acceleration imparted to the charge.</p>""",
          a=r"""<p class="step">\(F = qE = 3eE\); \(a = F/M\) = <span class="box">\(\vec a = \dfrac{3e\vec E}{2m}\)</span>
(along \(\vec E\) for a positive charge).</p>""",
          topic=ES, recall=r"""<ul><li>\(\vec F = q\vec E\), \(\vec a = q\vec E/m\).</li></ul>"""),
        Q("1(B)(iii)", 1, r"""<p>In the given figure find the current through the 20 V battery.</p>{{fig:0}}""",
          qfig=F.fig_q1b3_cells, afig=F.fig_a1b3_cells,
          a=r"""<p class="step">The ideal 20 V cell is connected directly between the top junction T and the bottom
junction M, with + at T: \(V_T - V_M = 20\) V.</p>
<p class="step">Left branch (16 V, + at top, with 2 Ω): \(V_T - V_M = 16 - 2I_1\) for current \(I_1\) upward
⇒ \(I_1 = (16 - 20)/2 = -2\) A, i.e. 2 A <b>downward</b>.</p>
<p class="step">Middle branch (16 V with + at the <em>bottom</em>, and 4 Ω): \(V_T - V_M = -16 - 4I_2\)
⇒ \(I_2 = (-16-20)/4 = -9\) A, i.e. 9 A downward.</p>
<p class="step">Kirchhoff's junction rule at T: current through the 20 V cell (upward) \(= 2 + 9\) =
<span class="box">11 A</span></p>{{fig:0}}""",
          topic=CE, recall=r"""<ul><li>Long plate = positive terminal; crossing a cell − → + raises potential by ε.</li>
<li>Parallel branches share the same p.d.; junction rule: currents in = currents out.</li></ul>"""),
        Q("1(B)(iv)", 1, r"""<p>An electron and a proton, having equal momentum, enter a uniform magnetic field at right
angles to the field lines. What will be the ratio of their radius of trajectories?</p>""",
          a=r"""<p class="step">\(r = \dfrac{p}{qB}\); equal \(p\), equal \(|q| = e\) ⇒ <span class="box">\(r_e : r_p = 1 : 1\)</span>
(they curve in opposite senses).</p>""",
          topic=MAG, recall=r"""<ul><li>\(r = mv/qB = p/qB\).</li></ul>"""),
        Q("1(B)(v)", 1, r"""<p>What is the ratio of the magnetic field intensity at a distance \(d\) from a short bar magnet
in longitudinal and transverse position?</p>""",
          a=r"""<p class="step">\(B_{\text{axial}} = \dfrac{\mu_0}{4\pi}\dfrac{2m}{d^3}\), \(B_{\text{equatorial}} = \dfrac{\mu_0}{4\pi}\dfrac{m}{d^3}\)
⇒ <span class="box">2 : 1</span></p>""",
          topic=MAG, recall=r"""<ul><li>End-on (longitudinal) field is twice the broadside-on (transverse) field at the same distance.</li></ul>"""),
        Q("1(B)(vi)", 1, r"""<p>A metallic square loop \(ABCD\) is moving in its own plane with velocity \(v\) in a uniform
magnetic field perpendicular to its plane as shown in the figure. Mention the arms in which an electric field is
induced.</p>{{fig:0}}""",
          qfig=F.fig_q1b6_loop, afig=F.fig_a1b6_loop,
          a=r"""<p class="step">A motional electric field (emf \(Blv\)) appears in a conductor only when \(\vec v\times\vec B\) has a
component along it. For AB and DC, \(\vec v\) is along their length, so \(\vec v\times\vec B\) is perpendicular to them:
no emf.</p>
<p class="step">An electric field is induced in the arms <span class="box">AD and BC</span> (perpendicular to
\(\vec v\)). The two emfs are equal and oppose each other round the loop (flux is constant), so no current flows.</p>{{fig:0}}""",
          topic=EMI, recall=r"""<ul><li>Motional emf \(\varepsilon = Blv\), along \(\vec v\times\vec B\) (on + charges).</li>
<li>Net induced current needs a change of flux through the loop.</li></ul>"""),
        Q("1(B)(vii)", 1, r"""<p>Find the value of reactance of a \(25\,\mu\)F capacitor at the A.C frequency of 4000 Hz.</p>""",
          a=r"""<p class="step">\(X_C = \dfrac{1}{2\pi fC} = \dfrac{1}{2\pi\times4000\times25\times10^{-6}}\) = <span class="box">1.59 Ω</span></p>""",
          topic=EMI, recall=r"""<ul><li>\(X_C = 1/(2\pi fC)\).</li></ul>"""),
        Q("1(B)(viii)", 1, r"""<p>In the figure, an air lens of radii of curvature 10 cm \((R_1 = R_2 = 10\) cm.) is cut in a
cylinder of glass \((\mu = \tfrac32)\). Find the focal length of the lens.</p>{{fig:0}}""",
          qfig=F.fig_q1b8_airlens,
          a=r"""<p class="step">Lens maker's formula for a lens of index \(\mu_l\) in a medium \(\mu_m\):
\(\dfrac1f = \left(\dfrac{\mu_l}{\mu_m}-1\right)\left(\dfrac1{R_1}-\dfrac1{R_2}\right)\).</p>
<p class="step">Biconvex air lens: \(R_1 = +10\), \(R_2 = -10\) cm; \(\mu_l/\mu_m = 1/1.5 = 2/3\).</p>
<p class="step">\(\dfrac1f = \left(\tfrac23 - 1\right)\left(\tfrac1{10}+\tfrac1{10}\right) = -\tfrac1{15}\) ⇒
<span class="box">\(f = -15\) cm</span> — the convex air lens is <b>diverging</b>.</p>""",
          topic=RAY, recall=r"""<ul><li>Use the <em>relative</em> refractive index \(\mu_l/\mu_m\) for a lens in a medium.</li>
<li>If \(\mu_l &lt; \mu_m\) a convex lens diverges.</li></ul>"""),
        Q("1(B)(ix)", 1, r"""<p>In order to operate RADAR which part of the electromagnetic spectrum is used?</p>""",
          a=r"""<p><span class="box">Microwaves</span> (wavelength about 1 mm to 30 cm).</p>""",
          topic=EMW, recall=r"""<ul><li>Microwaves: RADAR, microwave ovens, satellite links.</li></ul>"""),
        Q("1(B)(x)", 1, r"""<p>In Young's double slit experiment, the angular width of the fringe is \(0.2^0\) for the
sodium light \((\lambda = 5890\) Å\()\). Find the necessary change in wavelength in order to increase the angular
width of the fringes by 10%.</p>""",
          a=r"""<p class="step">Angular fringe width \(\theta = \lambda/d\) ∝ \(\lambda\) (same \(d\)).</p>
<p class="step">10% increase in \(\theta\) needs 10% increase in \(\lambda\): \(\Delta\lambda = 0.1\times5890\) =
<span class="box">589 Å increase</span> (new \(\lambda = 6479\) Å).</p>""",
          topic=WAVE, recall=r"""<ul><li>Fringe width \(\beta = \lambda D/d\); angular width \(\beta/D = \lambda/d\).</li></ul>"""),
        Q("1(B)(xi)", 1, r"""<p>Find the angle of incidence at which reflected light is totally polarized for reflection from
air to glass medium. (Refractive index of glass \(\mu = 1.5\)).</p>""",
          excluded="Polarisation by reflection (Brewster's law) — not in the ISC 2027 Wave Optics unit."),
        Q("1(B)(xii)", 1, r"""<p>In a hydrogen atom, if the difference in the energy of the electron in \(n = 2\) and
\(n = 3\) orbits is \(E\), find the ionization energy of hydrogen atom in terms of \(E\).</p>""",
          a=r"""<p class="step">\(E_n = -\dfrac{E_0}{n^2}\) (\(E_0\) = ionisation energy).
\(E = E_0\left(\tfrac14 - \tfrac19\right) = \tfrac{5}{36}E_0\).</p>
<p class="step"><span class="box">\(E_0 = \dfrac{36}{5}E = 7.2\,E\)</span></p>""",
          topic=ATOM, recall=r"""<ul><li>\(E_n = -13.6/n^2\) eV; ionisation energy = \(13.6\) eV = energy to take \(n=1\) to \(\infty\).</li></ul>"""),
        Q("1(B)(xiii)", 1, r"""<p>If decay constant of a radioactive element is \(1.5\times10^{-9}\) s\(^{-1}\) then what will be
the value of its mean-life in second?</p>""",
          excluded="Radioactivity (decay constant, mean life) — not in the ISC 2027 'Nuclei' unit."),
        Q("1(B)(xiv)", 1, r"""<p>What is the current through 300 Ω resistor in the circuit shown below?</p>{{fig:0}}
<p class="note">[The printed value in the question text was corrected by hand: a 0 is struck out of "3000",
leaving 300 Ω — which is also the value printed in the circuit diagram.]</p>""",
          qfig=F.fig_q1b14_diode,
          a=r"""<p class="step">The p side is at +4 V and the n side (through 300 Ω) at +1 V, so the diode is
<b>forward biased</b>.</p>
<p class="step">Ideal diode (no drop): \(I = \dfrac{4-1}{300}\) = <span class="box">0.01 A = 10 mA</span></p>
<p class="note">If a silicon diode's 0.7 V drop is taken into account: \(I = 2.3/300 = 7.7\) mA.</p>""",
          topic=ELEC, recall=r"""<ul><li>Forward bias: p at higher potential than n; an ideal diode then acts as a closed switch.</li></ul>"""),
        Q("1(B)(xv)", 1, r"""<p>Why \(n-p-n\) transistors are preferred over \(p-n-p\)?</p>""",
          excluded="Transistors — not in the ISC 2027 theory syllabus (only identified in a demonstration experiment)."),

        SEC("Part II (50 marks) — Section A", "Answer any four questions."),
        Q("2(a)", 2, r"""<p>A pendulum of mass 80 mg and carrying a charge of 20 nC is at rest in a horizontal uniform
electric field of \(2\times10^4\) N/C. Find the tension in the thread of the pendulum</p>""",
          afig=F.fig_a2a_pendulum,
          a=r"""<p class="step">At rest the bob is in equilibrium under \(mg\) (down), \(qE\) (horizontal) and \(T\) along the thread.</p>{{fig:0}}
<p class="step">\(mg = 80\times10^{-6}\times9.8 = 7.84\times10^{-4}\) N; \(qE = 20\times10^{-9}\times2\times10^{4} = 4.0\times10^{-4}\) N.</p>
<p class="step">\(T = \sqrt{(mg)^2 + (qE)^2} = 10^{-4}\sqrt{7.84^2 + 4^2}\) = <span class="box">\(8.8\times10^{-4}\) N</span>,
the thread making \(\theta = \tan^{-1}(qE/mg) = 27^\circ\) with the vertical.</p>""",
          topic=ES, recall=r"""<ul><li>Three forces in equilibrium: \(T\) balances the resultant of \(mg\) and \(qE\).</li>
<li>80 mg \(= 80\times10^{-6}\) kg.</li></ul>"""),
        Q("2(b)", 3, r"""<p>An electric dipole of dipole moment \(\vec p\) is placed in a uniform electric field \(\vec E\) with
its axis inclined to the field. Write an expression for the torque \(\vec\tau\) experienced by the dipole in vector
form. Show diagrammatically how the dipole should be kept in the electric field so that the torque acting on it
is (i) Maximum (ii) Zero</p>""",
          afig=F.fig_a2b_dipole, a=DIPOLE_A, topic=ES,
          recall=r"""<ul><li>The forces \(+q\vec E\), \(-q\vec E\) form a couple of arm \(2l\sin\theta\).</li>
<li>\(\tau = pE\sin\theta\); \(U = -pE\cos\theta\).</li></ul>"""),
        Q("3(a)", 2, r"""<p>With a potentiometer, null points were obtained at 140 cm and 180 cm, with cells of emf
1.1 V and an unknown emf of X volt respectively. Find the value of the unknown emf.</p>""",
          a=r"""<p class="step">\(\dfrac{\varepsilon_1}{\varepsilon_2} = \dfrac{l_1}{l_2}\Rightarrow X = 1.1\times\dfrac{180}{140}\) =
<span class="box">1.41 V</span></p>""",
          topic=CE, recall=r"""<ul><li>Potentiometer: \(\varepsilon = Kl\) at balance, so emfs compare as balancing lengths.</li></ul>"""),
        Q("3(b)", 3, r"""<p>Derive an expression for the energy stored in a charged capacitor.</p>""",
          afig=F.fig_a3b_qv,
          a=r"""<p class="step">Charge a capacitor \(C\) gradually. When its charge is \(q\), its p.d. is \(v = q/C\). The work
needed to bring a further charge \(dq\) from the negative plate to the positive plate is \(dW = v\,dq = \dfrac{q}{C}dq\).</p>
<p class="step">Total work in charging from 0 to \(Q\): \(W = \displaystyle\int_0^Q \frac{q}{C}\,dq = \frac{Q^2}{2C}\).</p>
<p class="step">This work is stored as electric potential energy. Using \(Q = CV\):</p>
<p><span class="box">\(U = \dfrac{Q^2}{2C} = \dfrac12CV^2 = \dfrac12QV\)</span> — the area under the \(v\)–\(q\) graph.</p>{{fig:0}}""",
          topic=ES, recall=r"""<ul><li>\(dW = v\,dq\); p.d. grows linearly with charge, so average p.d. is \(V/2\).</li>
<li>Energy density \(u = \tfrac12\varepsilon_0E^2\).</li></ul>"""),
        Q("4(a)", 2, r"""<p>The figure shows a network of circuit of currents. Find the value of current \(i\).</p>{{fig:0}}""",
          qfig=F.fig_q4a_junction,
          a=r"""<p class="step">Kirchhoff's junction rule at each corner (top-left TL, top-right TR, bottom-right BR,
bottom-left BL):</p>
<p class="step">TL: in 15 A + 8 A ⇒ 23 A along the top side. TR: 23 + 3 = 26 A down the right side.</p>
<p class="step">BL: the bottom side brings \(x\), plus 5 A in, and 8 A leaves upward ⇒ \(x = 3\) A (flowing right to left).</p>
<p class="step">BR: 26 A in = \(i\) + 3 A ⇒ <span class="box">\(i = 23\) A</span>
(check: total in \(15+3+5 = 23\) A = total out).</p>""",
          topic=CE, recall=r"""<ul><li>Junction rule (charge conservation): \(\sum I_{\text{in}} = \sum I_{\text{out}}\).</li>
<li>The whole network is itself a "junction": total in = total out.</li></ul>"""),
        Q("4(b)", 3, r"""<p>Draw a neat labeled diagram of meter bridge circuit use to determine the unknown
resistance \(X\).</p>""",
          afig=F.fig_a4b_metrebridge,
          a=r"""<p class="step">A uniform wire AC, 1 m long, is stretched along a metre scale between thick copper strips.
The unknown resistance \(X\) is put in the left gap and a resistance box \(R\) in the right gap. A galvanometer G is
connected between the middle strip B and a jockey J sliding on the wire; a cell with key K is joined across A and C.</p>{{fig:0}}
<p class="step">The jockey is moved to the null point D (no deflection), at distance \(l\) from A. Then the bridge
is balanced: \(\dfrac{X}{R} = \dfrac{R_{AD}}{R_{DC}} = \dfrac{l}{100-l}\)</p>
<p><span class="box">\(X = R\,\dfrac{l}{100-l}\)</span></p>""",
          topic=CE, recall=r"""<ul><li>Metre bridge = Wheatstone bridge with two arms formed by the wire (\(R\propto l\)).</li>
<li>Best accuracy when the null point is near the middle.</li></ul>"""),
        Q("5(a)", 2, r"""<p>Find the magnetic field induction at the point \(O\) due to current flowing in an infinite wire
shaped as shown in the figure.</p>{{fig:0}}""",
          qfig=F.fig_q5a_wire, afig=F.fig_a5a_wire,
          a=r"""<p class="step">Vertical straight part: O lies on its line, so \(d\vec l\times\hat r = 0\) ⇒ \(B_1 = 0\).</p>
<p class="step">Semicircle of radius \(r\) centred at O: \(B_2 = \dfrac12\cdot\dfrac{\mu_0I}{2r} = \dfrac{\mu_0I}{4r}\);
current anticlockwise (as seen) ⇒ out of the page.</p>
<p class="step">Horizontal semi-infinite wire starting at the foot of the perpendicular from O, distance \(r\):
\(B_3 = \dfrac{\mu_0I}{4\pi r}\); current to the right, O above it ⇒ out of the page.</p>
<p><span class="box">\(B = \dfrac{\mu_0I}{4r}\left(1 + \dfrac1\pi\right) = \dfrac{\mu_0I(\pi+1)}{4\pi r}\)</span>, perpendicular
to the page, outward.</p>{{fig:0}}""",
          topic=MAG, recall=r"""<ul><li>Centre of a circular arc of angle θ: \(B = \dfrac{\mu_0I\theta}{4\pi r}\) (semicircle: \(\mu_0I/4r\)).</li>
<li>Semi-infinite wire, point opposite its end: \(\mu_0I/4\pi r\); point on its line: 0.</li></ul>"""),
        Q("5(b)", 3, r"""<p>Plot a labelled graph showing variation in impedance Z of a L-C-R circuit with frequency f
of alternating emf applied to it. What is the minimum value of this impedance? Define 'power factor' of an L-C-R
circuit.</p>""",
          afig=F.fig_a5b_zf,
          a=r"""<p class="step">\(Z = \sqrt{R^2 + (2\pi fL - 1/2\pi fC)^2}\): large at low \(f\) (capacitive), falls to a minimum at
the resonant frequency \(f_0 = \dfrac{1}{2\pi\sqrt{LC}}\), then rises at high \(f\) (inductive).</p>{{fig:0}}
<p class="step">Minimum impedance (at resonance, \(X_L = X_C\)): <span class="box">\(Z_{\min} = R\)</span></p>
<p class="step"><b>Power factor</b> is the ratio of the true (average) power to the apparent power \(V_{\text{rms}}I_{\text{rms}}\):
\(\cos\varphi = \dfrac{P}{V_{\text{rms}}I_{\text{rms}}} = \dfrac{R}{Z}\), where \(\varphi\) is the phase difference between
voltage and current.</p>""",
          topic=EMI, recall=r"""<ul><li>Resonance: \(X_L = X_C\), \(f_0 = 1/2\pi\sqrt{LC}\), \(Z = R\), \(\cos\varphi = 1\).</li></ul>"""),
        Q("6(a)", 2, r"""<p>What are eddy currents? Write a practical application of eddy current.</p>""",
          a=r"""<p class="step"><b>Eddy currents</b> are the circulating currents induced in the body of a bulk conductor when
the magnetic flux through it changes (or it moves in a magnetic field). They flow in closed loops and, by Lenz's
law, oppose the change producing them.</p>
<p class="step">Applications (any one): electromagnetic (eddy-current) brakes in trains; induction furnace;
dead-beat moving-coil galvanometer (damping); speedometers; induction cooktops.</p>""",
          topic=EMI, recall=r"""<ul><li>Reduced in transformer cores by lamination (insulated thin sheets).</li></ul>"""),
        Q("6(b)", 3, r"""<p>A moving coil galvanometer of resistance 50 Ω gives full-scale deflection when 10 mA current
is passed through it. How will you convert it into a voltmeter of range 0 to 20 V? Explain with a diagram.</p>""",
          afig=F.fig_a6b_voltmeter,
          a=r"""<p class="step">A large resistance \(R\) is connected in <b>series</b> with the galvanometer so that a
p.d. of 20 V across the combination drives exactly the full-scale current \(I_g = 10\) mA.</p>
<p class="step">\(V = I_g(G + R)\Rightarrow R = \dfrac{V}{I_g} - G = \dfrac{20}{0.01} - 50\) = <span class="box">1950 Ω in series</span></p>{{fig:0}}""",
          topic=MAG, recall=r"""<ul><li>Voltmeter: high series resistance; ammeter: low shunt in parallel \(S = I_gG/(I-I_g)\).</li></ul>"""),
        Q("7(a)", 2, r"""<p>Derive an expression for torque on a rectangular current loop having a steady current \(i\)
and placed in a uniform magnetic field \(B\).</p>""",
          afig=F.fig_a7a_torque,
          a=r"""<p class="step">Let the rectangular loop PQRS (sides \(l\) and \(b\), \(N\) turns) carry current \(i\) and be
free to turn about an axis perpendicular to \(\vec B\); let the normal \(\hat n\) to its plane make angle \(\theta\)
with \(\vec B\).</p>{{fig:0}}
<p class="step">Sides of length \(b\): the forces on them are equal, opposite and collinear — they cancel.</p>
<p class="step">Sides PS and QR (length \(l\), perpendicular to \(\vec B\)): \(F = ilB\) each, equal and opposite
but along different lines ⇒ a couple. The perpendicular distance between their lines of action is \(b\sin\theta\).</p>
<p class="step">\(\tau = F\times b\sin\theta = ilB\,b\sin\theta = iAB\sin\theta\) (\(A = lb\)). For \(N\) turns:</p>
<p><span class="box">\(\tau = NiAB\sin\theta\), i.e. \(\vec\tau = \vec m\times\vec B\) with \(\vec m = Ni\vec A\)</span></p>
<p class="step">Maximum (\(NiAB\)) when the plane of the loop is parallel to \(\vec B\) (\(\theta = 90^\circ\)); zero when
the plane is perpendicular to \(\vec B\).</p>""",
          topic=MAG, recall=r"""<ul><li>\(\vec F = i\,\vec l\times\vec B\); net force on a closed loop in a uniform field is zero.</li>
<li>θ is between the <em>normal</em> (\(\vec m\)) and \(\vec B\).</li></ul>"""),
        Q("7(b)", 3, r"""<p>(i) In the circuit shown in figure, calculate the peak current \((I_0)\).<br>(ii) For what
value of capacitance \(C\) the power delivered by the battery in the above circuit will be maximum?</p>{{fig:0}}""",
          qfig=F.fig_q7b_lcr,
          a=r"""<p class="step">From \(\varepsilon = 300\sin(500t)\): \(\varepsilon_0 = 300\) V, \(\omega = 500\) rad/s.</p>
<p class="step">\(X_L = \omega L = 500\times2 = 1000\) Ω; \(X_C = \dfrac1{\omega C} = \dfrac{1}{500\times4\times10^{-6}} = 500\) Ω.</p>
<p class="step">\(Z = \sqrt{R^2 + (X_L - X_C)^2} = \sqrt{500^2+500^2} = 707.1\) Ω.</p>
<p class="step">(i) \(I_0 = \dfrac{\varepsilon_0}{Z} = \dfrac{300}{707.1}\) = <span class="box">0.424 A</span></p>
<p class="step">(ii) Power is maximum at resonance, \(\omega L = \dfrac{1}{\omega C}\):
\(C = \dfrac{1}{\omega^2L} = \dfrac{1}{(500)^2\times2}\) = <span class="box">\(2\times10^{-6}\) F = 2 μF</span></p>
<p class="note">The paper says "battery"; the source is an a.c. source.</p>""",
          topic=EMI, recall=r"""<ul><li>\(\varepsilon = \varepsilon_0\sin\omega t\): read \(\varepsilon_0\) and \(\omega\) directly.</li>
<li>\(I_0 = \varepsilon_0/Z\); max power at resonance.</li></ul>"""),

        SEC("Section B", "Answer any three questions."),
        Q("8(a)", 3, r"""<p>Starting with an expression for refraction at a single spherical surface, obtain an expression
for lens maker's formula for a bi-convex lens.</p>""",
          afig=F.fig_a8a_lensmaker,
          a=r"""<p class="step">For refraction at a spherical surface from medium \(\mu_1\) to \(\mu_2\):
\(\dfrac{\mu_2}{v} - \dfrac{\mu_1}{u} = \dfrac{\mu_2-\mu_1}{R}\).</p>
<p class="step">Thin biconvex lens of index \(\mu_2\) in a medium \(\mu_1\); radii \(R_1\) (first surface) and \(R_2\)
(second). A point object O on the axis.</p>{{fig:0}}
<p class="step">First surface alone forms image \(I_1\) at \(v_1\): \(\dfrac{\mu_2}{v_1} - \dfrac{\mu_1}{u} = \dfrac{\mu_2-\mu_1}{R_1}\) … (1)</p>
<p class="step">\(I_1\) is the (virtual) object for the second surface (lens thin, so distance \(v_1\) from it); light
goes from \(\mu_2\) to \(\mu_1\), giving the final image I at \(v\):
\(\dfrac{\mu_1}{v} - \dfrac{\mu_2}{v_1} = \dfrac{\mu_1-\mu_2}{R_2}\) … (2)</p>
<p class="step">Add (1) and (2): \(\mu_1\left(\dfrac1v - \dfrac1u\right) = (\mu_2-\mu_1)\left(\dfrac1{R_1}-\dfrac1{R_2}\right)\).</p>
<p class="step">For an object at infinity \(v = f\): with \(\mu = \mu_2/\mu_1\),</p>
<p><span class="box">\(\dfrac1f = (\mu - 1)\left(\dfrac1{R_1} - \dfrac1{R_2}\right)\)</span> and hence \(\dfrac1v - \dfrac1u = \dfrac1f\).</p>
<p class="step">For a biconvex lens \(R_1 &gt; 0\), \(R_2 &lt; 0\), so \(\dfrac1f = (\mu-1)\left(\dfrac1{|R_1|}+\dfrac1{|R_2|}\right) &gt; 0\).</p>""",
          topic=RAY, recall=r"""<ul><li>Image of the first surface acts as the object of the second.</li>
<li>Cartesian signs: \(R_1 = +\), \(R_2 = -\) for a biconvex lens.</li></ul>"""),
        Q("8(b)", 2, r"""<p>A narrow beam of light is incident normally on one face of an equilateral glass prism of
refractive index 1.45. When the prism is immersed in a suitable liquid, the ray makes a grazing emergence along
the other face. Find the refractive index of this liquid.</p>""",
          afig=F.fig_a8b_prism,
          a=r"""<p class="step">Normal incidence on the first face ⇒ \(r_1 = 0\), so \(r_2 = A - r_1 = 60^\circ\).</p>
<p class="step">Grazing emergence ⇒ 60° is the critical angle for glass→liquid:
\(\sin C = \dfrac{\mu_l}{\mu_g}\).</p>
<p class="step">\(\mu_l = 1.45\sin60^\circ = 1.45\times0.866\) = <span class="box">1.26</span></p>{{fig:0}}""",
          topic=RAY, recall=r"""<ul><li>Prism: \(r_1 + r_2 = A\).</li><li>Critical angle (denser → rarer): \(\sin C = \mu_{\text{rarer}}/\mu_{\text{denser}}\).</li></ul>"""),
        Q("9(a)", 3, r"""<p>Draw a neat labeled diagram showing the formation of image by a compound microscope for
normal adjustment condition.</p>""",
          afig=F.fig_a9a_micro,
          a=r"""<p class="step">Object AB is placed just beyond \(F_o\) of the objective (short focal length). The objective
forms a real, inverted, magnified image A′B′ inside the focal length of the eyepiece. The eyepiece acts as a
simple magnifier and forms the final virtual, inverted (w.r.t. AB), highly magnified image A″B″ at the least
distance of distinct vision \(D = 25\) cm.</p>{{fig:0}}
<p class="step">\(M = \dfrac{v_o}{u_o}\left(1 + \dfrac{D}{f_e}\right)\).</p>
<p class="note">Figure drawn to scale for \(f_o = 2\) cm, \(f_e = 5\) cm, \(u_o = 2.4\) cm (heights not to scale).
For a <em>telescope</em>, normal adjustment always means the final image at infinity. For the compound microscope
the ISC 2027 syllabus asks for the ray diagram with the final image at \(D\) (only the expression for the image at
infinity), and this school's 2015-16 paper calls the image-at-\(D\) set-up "normal use", so that is the diagram
drawn. If the examiner means the image at infinity, A′B′ is placed at \(F_e\) instead, the emergent rays are
parallel and \(M = \dfrac{v_o}{u_o}\cdot\dfrac{D}{f_e}\).</p>""",
          topic=RAY, recall=r"""<ul><li>Objective: real magnified image; eyepiece: magnifier.</li>
<li>Rays: one parallel to the axis (through the focus after the lens), one through the optical centre (undeviated).</li></ul>"""),
        Q("9(b)", 2, r"""<p>A pin is placed 10 cm in front of a convex lens of focal length 20 cm. The surface of the lens
further away from the pin is silvered and has a radius of curvature 22 cm. Determine the position of the final
image.</p>""",
          excluded="Silvered lens — explicitly excluded in the ISC 2027 syllabus ('Combination of lenses and mirrors "
                   "(silvering of lens excluded)')."),
        Q("10(a)", 3, r"""<p>i) What is the shape of the wave front diverging from a point source of light?<br>
ii) In Young's double slit experiment, red light of wavelength 6000 Å is used and the n<sup>th</sup> bright fringe is
obtained at a point \(P\) on the screen. Keeping the same setting, the source is replaced by the green light of
5000 Å and now \((n+1)^{th}\) bright fringe is obtained at the same point \(P\). Calculate the value of \(n\).</p>""",
          a=r"""<p class="step">(i) <span class="box">Spherical</span> (diverging).</p>
<p class="step">(ii) Position of the \(n\)th bright fringe: \(y_n = \dfrac{n\lambda D}{d}\). Same point P, same \(D, d\):
\(n\lambda_1 = (n+1)\lambda_2\).</p>
<p class="step">\(6000n = 5000(n+1)\Rightarrow 1000n = 5000\) ⇒ <span class="box">\(n = 5\)</span></p>""",
          topic=WAVE, recall=r"""<ul><li>Bright fringe: path difference \(d\sin\theta = n\lambda\), \(y_n = n\lambda D/d\).</li></ul>"""),
        Q("10(b)", 2, r"""<p>Can two sodium vapour lamps act as coherent sources? Explain in brief.</p>""",
          a=r"""<p class="step"><b>No.</b> Each lamp's light comes from many atoms emitting independently in short wave
trains (~\(10^{-8}\) s) with random phases. The phase difference between two independent lamps changes randomly
millions of times a second, so it is not constant: they are not coherent and no sustained interference pattern is
seen.</p>""",
          topic=WAVE, recall=r"""<ul><li>Coherent sources: same frequency and a constant phase difference.</li></ul>"""),
        Q("11(a)", 3, r"""<p>A point source of monochromatic light S is kept at the centre of the bottom of a cylinder.
Radius of the circular base of the cylinder is 15 cm. The cylinder contains water (Refractive Index = 4/3) to a
height of 7 cm. Find the area of the water surface through which the light emerges in the air.</p>""",
          afig=F.fig_a11a_cylinder,
          a=r"""<p class="step">Light escapes only where it meets the surface at less than the critical angle \(C\):
\(\sin C = \dfrac1\mu = \dfrac34\), \(\tan C = \dfrac{3}{\sqrt{16-9}} = \dfrac{3}{\sqrt7}\).</p>{{fig:0}}
<p class="step">Radius of the circle of escape: \(r = h\tan C = 7\times\dfrac{3}{\sqrt7} = 3\sqrt7 = 7.94\) cm
(less than 15 cm, so the whole circle lies on the water surface).</p>
<p class="step">Area \(= \pi r^2 = \pi\times63\) = <span class="box">198 cm²</span> (\(1.98\times10^{-2}\) m²).</p>""",
          topic=RAY, recall=r"""<ul><li>Total internal reflection beyond \(C\), \(\sin C = 1/\mu\).</li>
<li>Radius of the bright circle \(= h\tan C = h/\sqrt{\mu^2-1}\).</li></ul>"""),
        Q("11(b)", 2, r"""<p>A ray of light strikes a glass plate at an angle of \(60^0\). If the reflected and the refracted
rays are perpendicular to each other, find the refractive index of the glass.</p>""",
          afig=F.fig_a11b_angles,
          a=r"""<p class="step">Angle of reflection = 60°. Reflected and refracted rays perpendicular:
\(60^\circ + 90^\circ + r = 180^\circ\Rightarrow r = 30^\circ\).</p>{{fig:0}}
<p class="step">Snell's law: \(\mu = \dfrac{\sin 60^\circ}{\sin 30^\circ} = \sqrt3\) = <span class="box">1.73</span></p>
<p class="note">Equivalently \(\mu = \tan i\) — this is the polarising (Brewster) angle, but Snell's law alone answers the
question.</p>""",
          topic=RAY, recall=r"""<ul><li>Angles on a straight line at the point of incidence sum to 180°.</li><li>\(\mu = \sin i/\sin r\).</li></ul>"""),

        SEC("Section C", "Answer any three questions."),
        Q("12(a)", 3, r"""<p>Obtain an expression for the kinetic energy of the electron in Bohr model of the hydrogen atom
\((Z = 1)\). Start from equating the electrostatic force with the centripetal force required and then use the
quantization condition for angular momentum.</p>""",
          afig=F.fig_a12a_bohr,
          a=r"""<p class="step">Coulomb force = centripetal force: \(\dfrac{mv^2}{r} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{e^2}{r^2}\)
⇒ \(mv^2 = \dfrac{e^2}{4\pi\varepsilon_0 r}\), so \(K = \tfrac12mv^2 = \dfrac{e^2}{8\pi\varepsilon_0 r}\) … (i)</p>{{fig:0}}
<p class="step">Quantisation: \(mvr = \dfrac{nh}{2\pi}\). Dividing \(mv^2 r = \dfrac{e^2}{4\pi\varepsilon_0}\) by it:
\(v = \dfrac{e^2}{2\varepsilon_0 nh}\) … (ii); then \(r = \dfrac{nh}{2\pi m v} = \dfrac{\varepsilon_0n^2h^2}{\pi me^2}\).</p>
<p class="step">Put \(r\) in (i):</p>
<p><span class="box">\(K_n = \dfrac{me^4}{8\varepsilon_0^2n^2h^2}\)</span> \(= \dfrac{13.6}{n^2}\) eV
(and \(U = -2K\), \(E = -K\)).</p>""",
          topic=ATOM, recall=r"""<ul><li>\(mvr = nh/2\pi\); \(r_n\propto n^2\), \(v_n\propto 1/n\).</li><li>\(K = -E = -U/2\).</li></ul>"""),
        Q("12(b)", 2, r"""<p>An electron is accelerated through a potential difference of 300 V. What is its de Broglie
wavelength associated with the electron in Å unit?</p>""",
          a=r"""<p class="step">\(\lambda = \dfrac{h}{\sqrt{2meV}} = \dfrac{6.6\times10^{-34}}{\sqrt{2\times9.1\times10^{-31}\times1.6\times10^{-19}\times300}}\)</p>
<p class="step">\(= \dfrac{6.6\times10^{-34}}{9.35\times10^{-24}} = 7.06\times10^{-11}\) m = <span class="box">0.71 Å</span>
(shortcut \(12.27/\sqrt{300}\) Å = 0.708 Å).</p>""",
          topic=DUAL, recall=r"""<ul><li>\(eV = p^2/2m\) ⇒ \(\lambda = h/\sqrt{2meV}\).</li></ul>"""),
        Q("13(a)", 3, r"""<p>Derive the expression \(N = N_0e^{-\lambda t}\), from radioactive decay law, where t is the time and
\(\lambda\) is the decay constant of the radioactive substance.</p>""",
          excluded="Radioactive decay law — not in the ISC 2027 'Nuclei' unit."),
        Q("13(b)", 2, r"""<p>Calculate the energy released in the nuclear reaction
\({}_1\mathrm{H}^2 + {}_1\mathrm{H}^2\to{}_2\mathrm{He}^4 + \text{energy}\). (Mass of \({}_1\mathrm{H}^2 = 2.014102\) u, mass of
\({}_2\mathrm{He}^4 = 4.002604\) u)</p>""",
          a=r"""<p class="step">\(\Delta m = 2(2.014102) - 4.002604 = 4.028204 - 4.002604 = 0.025600\) u.</p>
<p class="step">\(Q = 0.0256\times931\) MeV = <span class="box">23.8 MeV</span> (\(\approx3.8\times10^{-12}\) J).</p>""",
          topic=NUC, recall=r"""<ul><li>Q-value = mass defect × 931 MeV/u (1 u = 931.5 MeV).</li></ul>"""),
        Q("14(a)", 3, r"""<p>Explain with the help of a circuit diagram how a Zener diode works as a voltage regulator.
Draw its \(I-V\) characteristics.</p>""",
          afig=[F.fig_a14a_zener, F.fig_a14a_zener_iv],
          a=r"""<p class="step"><b>Circuit:</b> the Zener diode is connected in <b>reverse bias</b> across the load \(R_L\);
the unregulated d.c. input is applied through a series resistor \(R_s\).</p>{{fig:0}}
<p class="step"><b>Working:</b> once the input exceeds the breakdown voltage \(V_Z\), the Zener conducts in
breakdown, where its voltage stays almost constant at \(V_Z\) over a wide range of current. If the input voltage
rises, the current through \(R_s\) increases; the extra current flows through the Zener, the extra voltage drops
across \(R_s\), and the output stays at \(V_Z\). If the input falls (or the load current changes) the Zener current
adjusts the other way. So \(V_0 = V_Z\) is regulated.</p>
<p class="step"><b>I–V characteristic:</b> forward bias as an ordinary diode; in reverse bias a tiny current until
\(V_Z\), then a sharp rise of current at almost constant voltage.</p>{{fig:1}}""",
          topic=ELEC, recall=r"""<ul><li>Zener: heavily doped, sharp reverse breakdown, used in reverse bias.</li>
<li>\(V_{\text{in}} = IR_s + V_Z\); \(I = I_Z + I_L\).</li></ul>"""),
        Q("14(b)", 2, r"""<p>Draw a neat labeled diagram of a \(n-p-n\) transistor in a common emitter configuration to
study its characteristics.</p>""",
          excluded="Transistors (CE characteristics) — not in the ISC 2027 theory syllabus."),
        Q("15(a)", 3, r"""<p>Identify the logic gates marked \(P\) and \(Q\) in the logic circuit. Write down the truth table
for this combinational logic circuit.</p>{{fig:0}}""",
          qfig=F.fig_q15a_logic,
          excluded="Logic gates — not in the ISC 2027 Electronic Devices unit."),
        Q("15(b)", 2, r"""<p>Define the following terms i) Attenuation ii) Bandwidth</p>""",
          excluded="Communication systems (attenuation, bandwidth of a channel) — removed from the ISC syllabus; not in "
                   "the ISC 2027 unit list."),
    ])
