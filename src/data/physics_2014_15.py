"""Heritage School Pre-Board 2014-15, Physics Paper 1 (Theory) — digital copy, ISC 2027 filter, solutions.
Transcribed from the page images (6 pages, complete)."""
from kit import Q, SEC
import physics_2014_15_figs as F

ES, CE, MAG = "Electrostatics", "Current Electricity", "Magnetic Effects of Current and Magnetism"
EMI, EMW = "Electromagnetic Induction and Alternating Currents", "Electromagnetic Waves"
RAY, WAVE = "Optics — Ray Optics", "Optics — Wave Optics"
DUAL, ATOM, NUC, ELEC = ("Dual Nature of Radiation and Matter", "Atoms and Nuclei — Atoms",
                         "Atoms and Nuclei — Nuclei", "Electronic Devices")

PAPER = dict(
    subject="physics", year="2014-15", slug="2014-15", paper="Paper 1 (Theory)",
    source="PreBoard-PYQ/2014-15/Physics.pdf", marks=70, time="3 hours",
    intro=r"""<p><i>[Candidates are allowed additional 15 minutes for only reading this paper. They must not start writing
during this time]</i></p>
<p><i>Answer all questions in Part I. Part II consists of three Sections A, B &amp; C. Answer 10 questions choosing four
questions from Section-A and three from each of the Sections B and C. All working including rough work should be
done on the same sheet as and adjacent to, the rest of the answer. The intended marks for questions or parts of
questions are given in brackets. [ ]</i></p>
<p><b>Useful Constants and relations</b> (as printed): electron charge \(e = 1.6\times10^{-19}\) C; Planck's constant
\(h = 6.6\times10^{-34}\) J s; speed of light \(c = 3\times10^{8}\) m/s; \(\varepsilon_0 = 8.85\times10^{-12}\) F/m;
\(\mu_0 = 4\pi\times10^{-7}\) T m A\(^{-1}\); mass of an electron \(= 9\times10^{-31}\) kg; Avogadro number
\(6.023\times10^{23}\) mol\(^{-1}\); 1 u = 931 MeV; \(\pi = 3.14\).</p>""",
    items=[
        SEC("Part I (20 marks) — Question 1 A) Choose the correct answer [5]", "Answer all questions."),
        Q("1(A)(i)", 1, r"""<p>Two point charges \(17.7\ \mu C\) and \(-17.7\ \mu C\), separated by a small distance, are kept inside a
large hollow metallic sphere of radius 15 cm. Electric flux emanating through the sphere is:</p>
<p>(a) \(2\times10^{6}\) V m &nbsp; (b) \(-2\times10^{6}\) V m &nbsp; (c) Zero &nbsp; (d) \(4\times10^{6}\) V m</p>""",
          a=r"""<p><b>(c) Zero.</b></p><p class="step">By Gauss's theorem \(\phi = q_{\text{enclosed}}/\varepsilon_0\), and
the net charge enclosed is \(17.7 - 17.7 = 0\ \mu\)C, so the flux is zero (the radius is irrelevant).</p>""",
          topic=ES, recall=r"<ul><li>Gauss: \(\oint\vec E\cdot d\vec A = q_{\rm enc}/\varepsilon_0\).</li><li>Flux depends only on the net enclosed charge.</li></ul>"),
        Q("1(A)(ii)", 1, r"""<p>Current (I) is flowing through a circular coil. If its radius (R) and number of turns (N) in it are each
doubled, magnetic flux density at its center becomes:</p>
<p>(a) Two times &nbsp; (b) Four times &nbsp; (c) Eight times &nbsp; (d) Six times</p>""",
          a=r"""<p class="step">\(B = \dfrac{\mu_0 N I}{2R}\). Doubling both N and R: \(B' = \dfrac{\mu_0(2N)I}{2(2R)} = B\).</p>
<p class="step"><span class="box">B remains the same (unchanged)</span></p>
<p class="note">[None of the printed options is correct — the paper's options are in error. If only N were doubled
the answer would be (a) two times.]</p>""",
          topic=MAG, recall=r"<ul><li>Centre of a coil: \(B=\mu_0NI/2R\).</li><li>\(B\propto N\), \(B\propto1/R\).</li></ul>"),
        Q("1(A)(iii)", 1, r"""<p>Ohm's law in vector form is:</p>
<p>(a) \(\vec J=\rho\vec E\) &nbsp; (b) \(\vec J=\sigma\vec E\) &nbsp; (c) \(V = IR\) &nbsp; (d) \(\vec E=\sigma\vec J\)</p>""",
          a=r"""<p><b>(b) \(\vec J=\sigma\vec E\)</b></p><p class="step">Current density is proportional to the field, the constant
being the conductivity \(\sigma = 1/\rho = ne^2\tau/m\). (Equivalently \(\vec E=\rho\vec J\).)</p>""",
          topic=CE, recall=r"<ul><li>\(J = I/A = nev_d\); \(\sigma = ne^2\tau/m\).</li></ul>"),
        Q("1(A)(iv)", 1, r"""<p>The slit of a spectrometer is illuminated by light of a neon discharge lamp. What type of spectrum will be
seen?</p><p>(a) Solar &nbsp; (b) Band &nbsp; (c) continuous &nbsp; (d) line</p>""",
          a=r"""<p><b>(d) Line spectrum.</b></p><p class="step">Neon in a discharge tube is a monatomic gas at low pressure; its
excited atoms emit only the definite wavelengths fixed by their energy levels — bright lines (strong red-orange
lines for neon).</p>""",
          topic=ATOM, recall=r"<ul><li>Atomic gas → line spectrum; molecules → band; incandescent solid → continuous.</li></ul>"),
        Q("1(A)(v)", 1, r"""<p>Two convex lenses of focal lengths 0.27 m and 0.15 m are used to make a telescope. The distance between them
is equal to:</p><p>(a) 0.25 m &nbsp; (b) 0.12 m &nbsp; (c) 0.42 m &nbsp; (d) 0.15 m</p>""",
          a=r"""<p><b>(c) 0.42 m</b></p><p class="step">In normal adjustment (final image at infinity) the separation is
\(f_o + f_e = 0.27 + 0.15 = 0.42\) m (the larger focal length is the objective).</p>""",
          topic=RAY, recall=r"<ul><li>Astronomical telescope, normal adjustment: \(L = f_o+f_e\), \(M = f_o/f_e\).</li></ul>"),

        SEC("Question 1 — B) Answer all questions given below briefly and to the point [15]"),
        Q("1(B)(i)", 1, r"""<p>How long will an electron take to fall through a distance of 2 m in a uniform electric field of 250 N/C?</p>""",
          a=r"""<p class="step">\(a = \dfrac{eE}{m} = \dfrac{1.6\times10^{-19}\times250}{9\times10^{-31}} = 4.44\times10^{13}\ \mathrm{m\,s^{-2}}\)
(gravity is negligible).</p>
<p class="step">Starting from rest: \(s = \tfrac12at^2\Rightarrow t = \sqrt{\dfrac{2s}{a}} = \sqrt{\dfrac{2\times2}{4.44\times10^{13}}}\)</p>
<p class="step"><span class="box">\(t = 3.0\times10^{-7}\ \mathrm s\)</span></p>""",
          topic=ES, recall=r"<ul><li>\(F = qE\), \(a = qE/m\).</li><li>From rest: \(s=\frac12at^2\).</li></ul>"),
        Q("1(B)(ii)", 1, r"""<p>Five point charges, each of value +q, are placed at five vertices of a regular hexagon of side L m. What is the
magnitude of the force on a point charge −q placed at the center of the hexagon?</p>""",
          a=r"""<p class="step">With +q at all six vertices the forces on the centre charge would cancel by symmetry.
So the resultant of the five equals minus the force the missing sixth charge would exert. The centre is a
distance L from every vertex (regular hexagon), so</p>
<p class="step"><span class="box">\(F = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q^2}{L^2}\)</span>, directed from the centre
towards the vertex opposite the empty one.</p>""",
          topic=ES, recall=r"<ul><li>Superposition; symmetric arrangements cancel.</li><li>Regular hexagon: centre-to-vertex distance = side.</li></ul>"),
        Q("1(B)(iii)", 1, r"""<p>Two identical capacitors are connected in parallel across a battery of potential 50 V. The battery is then
disconnected and the space between the plates of one capacitor is completely filled with material of dielectric
constant 4. Find the potential across the second capacitor.</p>""",
          a=r"""<p class="step">Charge stored: \(Q = 2C\times50 = 100C\) (stays constant after disconnection).</p>
<p class="step">New total capacitance (still in parallel): \(C + 4C = 5C\). Common potential \(V = \dfrac{100C}{5C}\)</p>
<p class="step"><span class="box">\(V = 20\ \mathrm V\)</span> (across both capacitors)</p>""",
          topic=ES, recall=r"<ul><li>Isolated system: total charge conserved.</li><li>Dielectric: \(C' = KC\); parallel ⇒ same V.</li></ul>"),
        Q("1(B)(iv)", 1, r"""<p>Find the potential difference between A and B in the following circuit diagram.</p>{{fig:0}}""",
          qfig=[F.fig_q1b4_cd],
          a=r"""<p class="step">Each branch C–D has \(1+3 = 4\ \Omega\); two in parallel give \(2\ \Omega\). Total
\(R = 2 + 0.5 = 2.5\ \Omega\), \(I = 10/2.5 = 4\) A, i.e. 2 A in each branch.</p>
<p class="step">\(V_C - V_A = 2\times1 = 2\) V; \(V_C - V_B = 2\times3 = 6\) V.</p>
<p class="step">\(V_A - V_B = 6 - 2\) ⇒ <span class="box">\(V_{AB} = 4\ \mathrm V\)</span> (A at the higher potential, the
cell's positive plate being on the C side).</p>""",
          topic=CE, recall=r"<ul><li>\(I = E/(R+r)\).</li><li>Potential falls by IR along the current in each resistor.</li></ul>"),
        Q("1(B)(v)", 1, r"""<p>The quantity of charge flowing through a certain cross-section varies with time and is given by
\(q = 3t^2 + 15t + 2\), where t is in seconds. Find the current through the surface at t = 2.0 s.</p>""",
          a=r"""<p class="step">\(I = \dfrac{dq}{dt} = 6t + 15\); at \(t = 2.0\) s: \(I = 12 + 15\) ⇒ <span class="box">\(I = 27\ \mathrm A\)</span></p>""",
          topic=CE, recall=r"<ul><li>Instantaneous current \(I = dq/dt\).</li></ul>"),
        Q("1(B)(vi)", 1, r"""<p>A very long straight wire carries a current I. At the instant, a charge +Q at a point P at a distance a has
velocity \(\vec v\) as shown in figure. Find the magnitude and direction of force on the charge.</p>{{fig:0}}""",
          qfig=[F.fig_q1b6_wire],
          a=r"""<p class="step">Field of the wire at P: \(B = \dfrac{\mu_0 I}{2\pi a}\); by the right-hand grip rule (I upwards,
P to the right) \(\vec B\) at P is <b>into the page</b>, perpendicular to \(\vec v\).</p>
<p class="step">\(F = QvB\sin90^\circ\) ⇒ <span class="box">\(F = \dfrac{\mu_0 I Q v}{2\pi a}\)</span></p>
<p class="step">Direction of \(\vec v\times\vec B\) (right × into page) = upwards, i.e. <b>parallel to the current I</b>,
in the plane of the paper.</p>{{fig:0}}""",
          afig=[F.fig_a1b6_force],
          topic=MAG, recall=r"<ul><li>Long wire: \(B=\mu_0I/2\pi r\), circles round the wire (right-hand grip).</li><li>\(\vec F = q\vec v\times\vec B\).</li></ul>"),
        Q("1(B)(vii)", 1, r"""<p>Name a substance whose temperature coefficient of resistance is nearly zero.</p>""",
          a=r"""<p class="step"><span class="box">Manganin</span> (or constantan / nichrome — alloys whose resistance hardly
changes with temperature; used for standard resistances).</p>""",
          topic=CE, recall=r"<ul><li>\(R_t = R_0(1+\alpha t)\); α small for alloys.</li></ul>"),
        Q("1(B)(viii)", 1, r"""<p>Which one of the transistor p-n-p or n-p-n is more useful and why?</p>""",
          excluded="Transistors — not in ISC 2027: Unit 9 covers the p-n junction diode, rectifiers and special diodes only; transistors appear only in the demonstration practicals."),
        Q("1(B)(ix)", 1, r"""<p>In AND gate, the output signal Y is high (1), then what should be the possible inputs?</p>""",
          excluded="Logic gates — not in ISC 2027: Unit 9 has no digital electronics (the word 'gate' does not occur in the syllabus)."),
        Q("1(B)(x)", 1, r"""<p>What is modulation factor or modulation index?</p>""",
          excluded="Communication systems (modulation) — not in ISC 2027: the nine units end with Electronic Devices; 'modulation' occurs nowhere in the syllabus."),
        Q("1(B)(xi)", 1, r"""<p>When sunlight is incident on water at an angle of 53°, the reflected light is found to be completely plane
polarized. Determine: (i) angle of refraction of light (ii) refractive index of water</p>""",
          excluded="Polarisation (Brewster's law) — not in ISC 2027: Wave Optics covers Huygens' principle, interference and single-slit diffraction; polarisation occurs only as a word in Unit 7, with no Brewster's or Malus's law."),
        Q("1(B)(xii)", 1, r"""<p>What is the main difference between Huygen's wave theory of light and Maxwell's electromagnetic theory?</p>""",
          a=r"""<p class="step"><b>Huygens</b> treated light as a <b>mechanical</b> wave needing a material medium — a
hypothetical all-pervading "ether".</p>
<p class="step"><b>Maxwell</b> showed light is an <b>electromagnetic</b> wave: mutually perpendicular oscillating
\(\vec E\) and \(\vec B\), transverse to the direction of travel, needing <b>no medium</b> and travelling in vacuum at
\(c = 1/\sqrt{\mu_0\varepsilon_0}\).</p>""",
          topic=EMW, recall=r"<ul><li>EM wave: \(\vec E\perp\vec B\perp\) direction of propagation; \(c=1/\sqrt{\mu_0\varepsilon_0}\).</li><li>Huygens' principle still used for wavefront construction.</li></ul>"),
        Q("1(B)(xiii)", 1, r"""<p>The frequency of a beam of UV light is \(1.0\times10^{-15}\) Hz. What is the energy in one quantum of this light?
Express it in eV.</p><p class="note">[The exponent is misprinted: UV light has \(\nu\sim10^{15}\) Hz. Solved with
\(\nu = 1.0\times10^{15}\) Hz.]</p>""",
          a=r"""<p class="step">\(E = h\nu = 6.6\times10^{-34}\times1.0\times10^{15} = 6.6\times10^{-19}\ \mathrm J\)</p>
<p class="step">\(E = \dfrac{6.6\times10^{-19}}{1.6\times10^{-19}}\) eV ⇒ <span class="box">\(E \approx 4.1\ \mathrm{eV}\)</span> (4.125 eV)</p>""",
          topic=DUAL, recall=r"<ul><li>Photon energy \(E = h\nu\).</li><li>1 eV = \(1.6\times10^{-19}\) J.</li></ul>"),
        Q("1(B)(xiv)", 1, r"""<p>Find angular momentum of an electron when it is in the second Bohr orbit of hydrogen atom.</p>""",
          a=r"""<p class="step">Bohr's quantisation: \(L = \dfrac{nh}{2\pi}\); for n = 2, \(L = \dfrac{h}{\pi} = \dfrac{6.6\times10^{-34}}{3.14}\)</p>
<p class="step"><span class="box">\(L \approx 2.1\times10^{-34}\ \mathrm{J\,s}\)</span></p>""",
          topic=ATOM, recall=r"<ul><li>\(mvr = nh/2\pi\).</li></ul>"),
        Q("1(B)(xv)", 1, r"""<p>What is the essential difference between the working of a nuclear reactor and that of a fission bomb?</p>""",
          a=r"""<p class="step">Reactor: <b>controlled</b> chain reaction — control rods absorb excess neutrons so that the
multiplication factor k = 1 and energy is released at a steady rate.</p>
<p class="step">Bomb: <b>uncontrolled</b> chain reaction (k &gt; 1) — the number of fissions grows in each generation
and a huge energy is released explosively in a very short time.</p>""",
          topic=NUC, recall=r"<ul><li>k = 1 critical (reactor); k &gt; 1 supercritical (bomb).</li></ul>"),

        SEC("Part II — Section A", "Answer any four questions from this section."),
        Q("2(a)", 2, r"""<p>Obtain an expression of the work done in rotating the dipole through an angle θ from its equilibrium
position.</p>""",
          a=r"""{{fig:0}}<p class="step">In a uniform field \(\vec E\) a dipole \(\vec p\) at angle θ feels a torque
\(\tau = pE\sin\theta\) (the couple \(qE\times2l\sin\theta\)), tending to restore it to θ = 0.</p>
<p class="step">Work done against this torque in turning it through dθ: \(dW = \tau\,d\theta = pE\sin\theta\,d\theta\).</p>
\[W = \int_0^{\theta} pE\sin\theta\,d\theta = pE\big[-\cos\theta\big]_0^{\theta}\]
<p class="step"><span class="box">\(W = pE(1-\cos\theta)\)</span> (stored as potential energy; e.g. \(W = 2pE\) for θ = 180°).</p>""",
          afig=[F.fig_a2a_dipole_torque],
          topic=ES, recall=r"<ul><li>\(\vec\tau = \vec p\times\vec E\).</li><li>\(U = -\vec p\cdot\vec E\); \(W = U(\theta)-U(0)\).</li></ul>"),
        Q("2(b)", 3, r"""<p>The plates of a parallel plate capacitor have an area of 90 cm\(^2\) each and are separated by 2.5 mm. The
capacitor is charged to 800 V. How much electrostatic energy is stored in it? What will be the energy when the gap
between the plates of the capacitor is filled with a dielectric material of K = 3.</p>""",
          a=r"""<p class="step">\(C = \dfrac{\varepsilon_0A}{d} = \dfrac{8.85\times10^{-12}\times90\times10^{-4}}{2.5\times10^{-3}} = 3.19\times10^{-11}\ \mathrm F\)</p>
<p class="step">\(U = \tfrac12CV^2 = \tfrac12\times3.19\times10^{-11}\times(800)^2\) ⇒ <span class="box">\(U = 1.02\times10^{-5}\ \mathrm J\)</span></p>
<p class="step"><b>With dielectric</b> (the capacitor, once charged, is taken as disconnected, so Q is constant):
\(C' = KC\), \(U' = \dfrac{Q^2}{2KC} = \dfrac{U}{K}\) ⇒ <span class="box">\(U' = 3.4\times10^{-6}\ \mathrm J\)</span></p>
<p class="step">(If the battery were kept connected, V stays 800 V and \(U' = KU = 3.06\times10^{-5}\) J.)</p>""",
          topic=ES, recall=r"<ul><li>\(C=\varepsilon_0A/d\); \(U=\frac12CV^2=Q^2/2C\).</li><li>Isolated: Q fixed ⇒ U/K; connected: V fixed ⇒ KU.</li></ul>"),
        Q("3(a)", 2, r"""<p>Three charges q, −2q, q are arranged on the vertices of an equilateral triangle of side a. What is the
equivalent dipole moment?</p>""",
          a=r"""<p class="step">Split −2q into two charges −q. The system is then two dipoles, each of moment
\(p_1 = p_2 = qa\), directed from the −2q vertex to each +q vertex, with 60° between them.</p>{{fig:0}}
<p class="step">\(p = \sqrt{p_1^2+p_2^2+2p_1p_2\cos60^\circ} = \sqrt{3}\,qa\)</p>
<p class="step"><span class="box">\(p = \sqrt3\,qa\)</span>, along the bisector from the −2q vertex towards the
midpoint of the opposite side.</p>""",
          afig=[F.fig_a3a_triangle],
          topic=ES, recall=r"<ul><li>Dipole moment points from −q to +q, magnitude q × separation.</li><li>Dipole moments add as vectors.</li></ul>"),
        Q("3(b)", 3, r"""<p>Obtain an expression for self-induction of a solenoid having N-number of turns.</p>""",
          a=r"""{{fig:0}}<p class="step">Long air-cored solenoid: N turns, length l, cross-section A, current I. Field inside
(Ampère's law): \(B = \mu_0 nI = \dfrac{\mu_0NI}{l}\).</p>
<p class="step">Flux through each turn \(= BA\); total flux linkage \(\phi = NBA = \dfrac{\mu_0N^2AI}{l}\).</p>
<p class="step">By definition \(\phi = LI\), so <span class="box">\(L = \dfrac{\mu_0N^2A}{l}\)</span>
(\(= \mu_0n^2Al\); with a core of relative permeability \(\mu_r\), \(L = \mu_0\mu_rN^2A/l\)).</p>""",
          afig=[F.fig_a3b_solenoid],
          topic=EMI, recall=r"<ul><li>Solenoid \(B=\mu_0nI\).</li><li>\(\phi = LI\), \(\varepsilon = -L\,dI/dt\).</li></ul>"),
        Q("4(a)", 2, r"""<p>Find the effective resistance between the points A and B in the following diagram.</p>{{fig:0}}""",
          qfig=[F.fig_q4a_net],
          a=r"""{{fig:0}}<p class="step">Name the junctions C, T, M, D. In the upper part, C–T–B and C–M–B with T–M across them
form a Wheatstone bridge with all arms R: \(\frac{R_{CT}}{R_{TB}} = \frac{R_{CM}}{R_{MB}}\), so it is balanced and
<b>TM carries no current</b> — remove it.</p>
<p class="step">Upper part: two paths of 2R in parallel = R. Lower path C–D–B = 2R.</p>
<p class="step">Between C and B: \(R\parallel2R = \dfrac{2R}{3}\). Adding the R from A to C:</p>
<p class="step"><span class="box">\(R_{AB} = R + \dfrac{2R}{3} = \dfrac{5R}{3}\)</span></p>""",
          afig=[F.fig_a4a_net_labelled],
          topic=CE, recall=r"<ul><li>Balanced bridge: P/Q = R/S ⇒ no current in the galvanometer arm.</li><li>Series add; parallel \(\frac{R_1R_2}{R_1+R_2}\).</li></ul>"),
        Q("4(b)", 3, r"""<p>Draw a current (I) versus time (t) graph in the following three circuits.</p>{{fig:0}}""",
          qfig=[F.fig_q4b_circuits],
          a=r"""{{fig:0}}<p class="step">(a) Steady d.c. through a resistor: \(I = E/R\), constant — a horizontal line.</p>
<p class="step">(b) A capacitor blocks steady d.c.: a charging current flows only for a moment when the circuit is
made (decaying exponentially, very rapidly since the resistance is only that of the wires), after which
\(I = 0\).</p>
<p class="step">(c) A.c. through a pure resistor: \(I = \dfrac{E_0}{R}\sin\omega t = I_0\sin\omega t\), a sine curve in
phase with the e.m.f.</p>""",
          afig=[F.fig_a4b_graphs],
          topic=EMI, recall=r"<ul><li>Capacitor: charging current \(I = I_0e^{-t/RC}\), zero in steady d.c.</li><li>Pure R in a.c.: I in phase with V.</li></ul>"),
        Q("5(a)", 2, r"""<p>What is eddy current? How it is disadvantageous to us?</p>""",
          a=r"""<p class="step"><b>Eddy currents</b> are the closed loops of current induced in the body of a bulk conductor
when the magnetic flux through it changes (it moves in a field or the field varies). By Lenz's law they oppose the
change that produces them.</p>
<p class="step"><b>Disadvantages:</b> they heat the cores of transformers, motors and generators, wasting electrical
energy (I²R loss) and lowering efficiency, and may damage insulation. They are reduced by using <b>laminated</b>
cores (thin insulated sheets) or slotted/ferrite cores.</p>""",
          topic=EMI, recall=r"<ul><li>Faraday + Lenz in a bulk conductor ⇒ eddy currents.</li><li>Laminations raise the resistance of the eddy paths.</li></ul>"),
        Q("5(b)", 3, r"""<p>A solenoid of length 1.5 m and radius 2 cm has 5 layers of windings, each having 150 turns. Find magnetic flux
coming out through one of its ends of cross-section. The current through the solenoid is 10 A.</p>""",
          a=r"""<p class="step">Total turns \(N = 5\times150 = 750\); \(n = N/l = 750/1.5 = 500\ \mathrm{m^{-1}}\).</p>
<p class="step">At an <b>end</b> of a long solenoid the field is half that inside:
\(B_{\text{end}} = \tfrac12\mu_0nI = \tfrac12\times4\times3.14\times10^{-7}\times500\times10 = 3.14\times10^{-3}\ \mathrm T\).</p>
<p class="step">\(A = \pi r^2 = 3.14\times(0.02)^2 = 1.256\times10^{-3}\ \mathrm{m^2}\)</p>
<p class="step">\(\phi = BA = 3.14\times10^{-3}\times1.256\times10^{-3}\) ⇒ <span class="box">\(\phi \approx 3.9\times10^{-6}\ \mathrm{Wb}\)</span></p>
<p class="step"><b>Why exactly half at the end face.</b> Place a second identical solenoid against this end: the pair is one
long solenoid with field \(\mu_0nI\) at the joining plane. By symmetry each half contributes equally to the axial
component there, so at the end face of one solenoid \(B_{\text{axial}} = \tfrac12\mu_0nI\) over the whole
cross-section. Only half the flux inside reaches the end face; the rest leaks out through the sides near the end.</p>
<p class="note">The question says "coming out through one of its ends", so the end-face reading is the one intended.
Using the field deep inside (\(\mu_0nI\)) gives \(7.9\times10^{-6}\) Wb, which is the flux through a cross-section
near the middle, not through the end.</p>""",
          topic=MAG, recall=r"<ul><li>Long solenoid: \(B=\mu_0nI\) inside, \(\frac12\mu_0nI\) at the ends.</li><li>\(\phi = BA\) for uniform B ⟂ A.</li></ul>"),
        Q("6(a)", 2, r"""<p>State two factors on which motional e.m.f induced in a conductor depends.</p>""",
          a=r"""<p class="step">\(\varepsilon = Blv\) (conductor, field and velocity mutually perpendicular). It depends on</p>
<p class="step">(1) the magnetic flux density B, (2) the length l of the conductor in the field, (3) its speed v
(and on the angle between \(\vec v\) and \(\vec B\): \(\varepsilon = Blv\sin\theta\)). Any two.</p>""",
          topic=EMI, recall=r"<ul><li>\(\varepsilon = Blv\); induced current \(Blv/R\).</li></ul>"),
        Q("6(b)", 3, r"""<p>A 0.5 m long metal rod PQ completes the circuit, as shown in the figure. The area of the circuit is perpendicular
to the magnetic field of flux density 0.15 T. If the resistance of the total circuit is 3 Ω, calculate the force
needed to move the rod in the direction as indicated in figure, with a constant speed 2 m/s.</p>{{fig:0}}""",
          qfig=[F.fig_q6b_rod],
          a=r"""<p class="step">Induced e.m.f. \(\varepsilon = Blv = 0.15\times0.5\times2 = 0.15\ \mathrm V\)</p>
<p class="step">Current \(I = \varepsilon/R = 0.15/3 = 0.05\ \mathrm A\) (from Q to P in the rod, by \(\vec v\times\vec B\)).</p>
<p class="step">Magnetic force on the rod \(F = BIl = 0.15\times0.05\times0.5\), directed opposite to \(\vec v\) (Lenz).
At constant speed the applied force must balance it:</p>
<p class="step"><span class="box">\(F = 3.75\times10^{-3}\ \mathrm N\)</span>, in the direction of motion.</p>{{fig:0}}""",
          afig=[F.fig_a6b_rod],
          topic=EMI, recall=r"<ul><li>\(\varepsilon=Blv\), \(I=\varepsilon/R\), \(F=BIl = B^2l^2v/R\).</li><li>Power \(Fv = \varepsilon^2/R\).</li></ul>"),
        Q("7(a)", 2, r"""<p>A 110 V D.C heater is connected to an A.C source such that the heat produced is the same. What is the r.m.s value
of the alternating voltage?</p>""",
          a=r"""<p class="step">The r.m.s. value of an a.c. is, by definition, the d.c. value that produces the same heat in the
same resistor in the same time.</p><p class="step"><span class="box">\(V_{\text{rms}} = 110\ \mathrm V\)</span>
(peak value \(110\sqrt2\approx156\) V).</p>""",
          topic=EMI, recall=r"<ul><li>Heat \(\propto V_{\rm rms}^2/R\).</li><li>\(V_{\rm rms} = V_0/\sqrt2\).</li></ul>"),
        Q("7(b)", 3, r"""<p>An alternating e.m.f of frequency 50 Hz is applied to a circuit with a resistor of 20 Ω, an inductor of 100 mH
and a capacitor 30 μF connected in series.</p>
<p>i. What is the angle by which the current leads or lags the applied e.m.f?</p>
<p>ii. Represent the voltage and the current in a vector diagram showing the phase angle.</p>""",
          a=r"""<p class="step">\(X_L = 2\pi fL = 2\pi\times50\times0.1 = 31.4\ \Omega\);
\(X_C = \dfrac{1}{2\pi fC} = \dfrac{1}{2\pi\times50\times30\times10^{-6}} = 106.1\ \Omega\)</p>
<p class="step">\(\tan\phi = \dfrac{X_C - X_L}{R} = \dfrac{106.1-31.4}{20} = 3.73\Rightarrow\phi = 75.0^\circ\)</p>
<p class="step">(i) Since \(X_C > X_L\) the circuit is capacitive: <span class="box">the current <b>leads</b> the e.m.f. by about 75°</span>
(\(Z = \sqrt{20^2+74.7^2} = 77.3\ \Omega\)).</p>
<p class="step">(ii) Phasor diagram (current as reference):</p>{{fig:0}}""",
          afig=[F.fig_a7b_phasor],
          topic=EMI, recall=r"<ul><li>\(X_L=\omega L\), \(X_C=1/\omega C\), \(Z=\sqrt{R^2+(X_L-X_C)^2}\).</li><li>\(\tan\phi = (X_L-X_C)/R\); \(V_L\) leads I by 90°, \(V_C\) lags by 90°.</li></ul>"),

        SEC("Section B", "Answer any three questions from this section."),
        Q("8(a)", 3, r"""<p>Show that the deviation produced by a thin glass prism placed in air is reduced to one-fourth when the prism is
immersed in water. Given: \({}_a\mu_g = 3/2\) and \({}_a\mu_w = 4/3\)</p>""",
          a=r"""<p class="step">Thin prism of angle A: \(\delta = (\mu-1)A\), μ being the index of the prism relative to the
surrounding medium.</p>
<p class="step">In air: \(\delta_a = \left(\tfrac32-1\right)A = \dfrac A2\).</p>
<p class="step">In water: \({}_w\mu_g = \dfrac{{}_a\mu_g}{{}_a\mu_w} = \dfrac{3/2}{4/3} = \dfrac98\), so
\(\delta_w = \left(\tfrac98-1\right)A = \dfrac A8\).</p>
<p class="step"><span class="box">\(\dfrac{\delta_w}{\delta_a} = \dfrac{A/8}{A/2} = \dfrac14\)</span> — reduced to one-fourth.</p>""",
          topic=RAY, recall=r"<ul><li>Thin prism \(\delta=(\mu-1)A\).</li><li>Relative index \({}_1\mu_2 = \mu_2/\mu_1\).</li></ul>"),
        Q("8(b)", 2, r"""<p>State any one condition for sustained interference of light.</p>
<p>State one dissimilarity between the two electromagnetic waves: X-rays and Microwaves</p>""",
          a=r"""<p class="step"><b>Sustained interference:</b> the two sources must be <b>coherent</b> — emit waves of the same
frequency with a constant phase difference (in practice derived from a single source). (Also acceptable: nearly
equal amplitudes; narrow sources close together.)</p>
<p class="step"><b>X-rays vs microwaves:</b> wavelength — X-rays \(\sim10^{-10}\) m (very short, highly penetrating,
ionising), microwaves \(\sim10^{-3}\)–\(10^{-1}\) m. (Or production: X-rays from fast electrons striking a metal
target; microwaves from klystrons/magnetrons.)</p>""",
          topic="Optics — Wave Optics; Electromagnetic Waves",
          recall=r"<ul><li>Coherent = constant phase difference.</li><li>EM spectrum order: radio, micro, IR, visible, UV, X, γ (decreasing λ).</li></ul>"),
        Q("9(a)", 3, r"""<p>Obtain an expression for refraction at a single convex spherical surface, i.e. the relation between
\(\mu_1\) (rarer medium), \(\mu_2\) (denser medium), the object distance u, image distance v and radius of curvature R.</p>""",
          a=r"""{{fig:0}}<p class="step">A convex surface (pole P, centre C) separates a rarer medium \(\mu_1\) (object side) from a
denser medium \(\mu_2\). A ray from the point object O meets the surface at A (height h) and after refraction meets
the axis at the real image I. CA (produced to N) is the normal. Let α, β, γ be the angles that AO, AI, AC make with
the axis.</p>
<p class="step">From the triangles: exterior angle of △OAC: \(i = \alpha + \gamma\); of △ACI: \(\gamma = r + \beta\Rightarrow r = \gamma-\beta\).</p>
<p class="step">Snell's law for paraxial rays (small angles): \(\mu_1 i = \mu_2 r \Rightarrow \mu_1(\alpha+\gamma) = \mu_2(\gamma-\beta)\).</p>
<p class="step">For small angles \(\alpha\approx\dfrac{h}{PO},\ \beta\approx\dfrac{h}{PI},\ \gamma\approx\dfrac{h}{PC}\)
(A is very close to P):</p>
\[\frac{\mu_1}{PO}+\frac{\mu_2}{PI} = \frac{\mu_2-\mu_1}{PC}\]
<p class="step">Cartesian signs (distances from P, positive along the incident light): \(PO = -u,\ PI = +v,\ PC = +R\):</p>
<p class="step"><span class="box">\(\dfrac{\mu_2}{v} - \dfrac{\mu_1}{u} = \dfrac{\mu_2-\mu_1}{R}\)</span></p>""",
          afig=[(F.fig_a9a_spherical, "i = α + γ, r = γ − β; schematic, angles opened out.")],
          topic=RAY, recall=r"<ul><li>Exterior angle of a triangle = sum of interior opposite angles.</li><li>Paraxial: \(\sin\theta\approx\tan\theta\approx\theta\).</li><li>Snell \(\mu_1\sin i = \mu_2\sin r\).</li></ul>"),
        Q("9(b)", 2, r"""<p>Where should an object be kept on the principal axis of a convex lens of focal length 20 cm, in order to get an
image, which is double the size of the object?</p>""",
          a=r"""<p class="step">Lens: \(\dfrac1v-\dfrac1u=\dfrac1f\), \(m = v/u\), f = +20 cm.</p>
<p class="step"><b>Real (inverted) image</b>, m = −2: v = −2u ⇒ \(-\dfrac{1}{2u}-\dfrac1u = \dfrac1{20}\Rightarrow u = -30\) cm (v = +60 cm).</p>
<p class="step"><b>Virtual (erect) image</b>, m = +2: v = 2u ⇒ \(\dfrac{1}{2u}-\dfrac1u=\dfrac1{20}\Rightarrow u = -10\) cm (v = −20 cm).</p>
<p class="step"><span class="box">At 30 cm from the lens (real image) or at 10 cm (virtual image, magnifier)</span></p>""",
          topic=RAY, recall=r"<ul><li>\(m = v/u\) for a lens; real image ⇒ m negative.</li><li>Object between F and 2F ⇒ magnified real image; inside F ⇒ virtual.</li></ul>"),
        Q("10(a)", 3, r"""<p>An object is placed at a distance of 20 cm to the left of a convex lens of focal length 10 cm. A concave mirror of
focal length 5 cm is placed at a distance of 30 cm to the right of the lens. Find the position and nature of the
final image. Draw the ray-diagram and locate the position of the final image.</p>""",
          a=r"""<p class="step"><b>Lens</b> (u = −20, f = +10): \(\dfrac1v = \dfrac1{10}-\dfrac1{20}\Rightarrow v = +20\) cm; \(I_1\) is real,
inverted, same size (m = −1), 20 cm right of the lens, i.e. <b>10 cm in front of the mirror</b>.</p>
<p class="step"><b>Mirror</b> (u = −10, f = −5): \(\dfrac1v = \dfrac1f-\dfrac1u = -\dfrac15+\dfrac1{10}\Rightarrow v = -10\) cm.
\(I_1\) is at the mirror's centre of curvature, so \(I_2\) is formed at the same place, real, inverted with respect to
\(I_1\) (m = −1).</p>
<p class="step"><b>Lens again</b> (light now travels right to left; \(I_2\) is 20 cm from the lens = 2f): the image
\(I_3\) is formed 20 cm on the other side, i.e. at the original object position, with m = −1.</p>
<p class="step"><span class="box">Final image: 20 cm to the left of the lens (at the object itself), real, inverted, same size</span>
(overall \(m = (-1)(-1)(-1) = -1\)). If only the reflection is counted, the image formed by the mirror is 10 cm in front
of it (20 cm right of the lens), real and erect relative to the object.</p>{{fig:0}}""",
          afig=[(F.fig_a10a_lens_mirror, "Blue: first refraction; red: reflection at the mirror; green: return through the lens. Scale 8 px = 1 cm.")],
          topic=RAY, recall=r"<ul><li>Image of one element is the object for the next.</li><li>Object at C of a concave mirror ⇒ image at C, inverted, same size.</li><li>Object at 2F of a lens ⇒ image at 2F.</li></ul>"),
        Q("10(b)", 2, r"""<p>What is the use of a Spectrometer? In a Spectrometer, what is the function of the Telescope?</p>""",
          excluded="Spectrometer — not in ISC 2027: the instrument occurs neither in the theory (Optical instruments: microscopes and telescopes only) nor in the practical list."),
        Q("11(a)(i)", 2, r"""<p>What is meant by spherical aberration? How can spherical aberration be reduced? Suggest any method using one or
more lens.</p><p class="note">[Q11(a) carries 3 marks for its three parts together; split here.]</p>""",
          excluded="Spherical aberration and its reduction — not in ISC 2027: no lens defects are listed ('aberration' occurs nowhere in the syllabus)."),
        Q("11(a)(ii)", 1, r"""<p>State one of the advantages of reflecting telescope over refracting type telescope.</p>""",
          a=r"""<p class="step">A reflecting telescope uses a (parabolic) concave mirror as objective, so it has <b>no chromatic
aberration</b> (and no spherical aberration). Also: a large mirror is easier and cheaper to make and support than a
large lens, giving greater light-gathering and resolving power. (Any one.)</p>""",
          topic=RAY, recall=r"<ul><li>Mirrors reflect all colours alike — no dispersion.</li><li>Resolving power ∝ aperture.</li></ul>"),
        Q("11(b)", 2, r"""<p>A compound microscope consists of an objective of focal length 2 cm and an eye piece of focal length 5 cm. When an
object is kept 2.4 cm from the objective, final image formed is virtual and is at 25 cm from the eye piece.
Determine magnifying power of this compound microscope in this set up i.e. in normal use.</p>""",
          a=r"""<p class="step">Objective: \(\dfrac1{v_o} = \dfrac12-\dfrac1{2.4} = \dfrac1{12}\Rightarrow v_o = 12\) cm; \(m_o = \dfrac{v_o}{u_o} = \dfrac{12}{2.4} = 5\).</p>
<p class="step">Eyepiece with final image at D = 25 cm: \(m_e = 1+\dfrac{D}{f_e} = 1+\dfrac{25}{5} = 6\).</p>
<p class="step">\(M = m_o\times m_e = 5\times6\) ⇒ <span class="box">\(M = 30\)</span> (magnitude; the final image is inverted).</p>""",
          topic=RAY, recall=r"<ul><li>Compound microscope (image at D): \(M = \frac{v_o}{u_o}\left(1+\frac{D}{f_e}\right)\).</li></ul>"),

        SEC("Section C", "Answer any three questions from this section."),
        Q("12(a)", 3, r"""<p>Obtain an expression for the total energy of an electron in the Bohr model of Hydrogen atom. Start from equating the
electrostatic force with the centripetal force required and then use the quantization condition for angular
momentum.</p>""",
          a=r"""{{fig:0}}<p class="step">Electron (mass m, charge −e) in a circular orbit of radius r about the proton:</p>
\[\frac{mv^2}{r} = \frac{1}{4\pi\varepsilon_0}\frac{e^2}{r^2}\quad\Rightarrow\quad mv^2 = \frac{e^2}{4\pi\varepsilon_0 r}\qquad(1)\]
<p class="step">Quantisation: \(mvr = \dfrac{nh}{2\pi}\Rightarrow v = \dfrac{nh}{2\pi mr}\). Substituting in (1):
\(r_n = \dfrac{\varepsilon_0n^2h^2}{\pi me^2}\).</p>
<p class="step">Kinetic energy \(K = \tfrac12mv^2 = \dfrac{e^2}{8\pi\varepsilon_0 r}\); potential energy
\(U = -\dfrac{e^2}{4\pi\varepsilon_0 r}\).</p>
<p class="step">Total \(E = K + U = -\dfrac{e^2}{8\pi\varepsilon_0 r}\); putting \(r_n\):</p>
<p class="step"><span class="box">\(E_n = -\dfrac{me^4}{8\varepsilon_0^2n^2h^2} = -\dfrac{13.6}{n^2}\ \mathrm{eV}\)</span>
(negative: the electron is bound; K = −E, U = 2E).</p>""",
          afig=[F.fig_a12a_bohr],
          topic=ATOM, recall=r"<ul><li>Coulomb force = centripetal force.</li><li>\(mvr = nh/2\pi\).</li><li>\(E = -K = U/2\).</li></ul>"),
        Q("12(b)", 2, r"""<p>In Coolidge (modern) X-ray tube, how will you vary (i) The intensity of emitted X-rays (ii) The penetrating power of
emitted X-rays</p>""",
          excluded="Coolidge X-ray tube — not in ISC 2027: X-rays appear only as a band of the EM spectrum (Unit 5, 'elementary facts' of source, detection and uses); the X-ray tube and the control of intensity and penetrating power belonged to the deleted X-rays section."),
        Q("13(a)", 3, r"""<p>A radioactive sample has a half-life of \(1.42\times10^{17}\) seconds and a mass number of 238. Calculate the number of
disintegrations per second in 1 g of this sample.</p>""",
          excluded="Radioactivity (activity and half-life) — not in ISC 2027: the Nuclei unit lists composition, binding energy, nuclear reactions, fission and fusion; 'decay', 'half-life' and 'activity' occur nowhere in the syllabus."),
        Q("13(b)", 2, r"""<p>Calculate the mass defect of Helium [\({}^4\mathrm{He}_2\)] nucleus and ii) its binding energy in MeV. Mass of
proton = 1.007276 u, Mass of neutron = 1.008665 u, mass of \({}^4\mathrm{He}_2\) = 4.001506 u</p>""",
          a=r"""<p class="step">\(\Delta m = 2m_p + 2m_n - M = 2(1.007276) + 2(1.008665) - 4.001506 = 4.031882 - 4.001506\)</p>
<p class="step">(i) <span class="box">\(\Delta m = 0.030376\ \mathrm u\)</span></p>
<p class="step">(ii) \(BE = \Delta m\times931\ \mathrm{MeV} = 0.030376\times931\) ⇒ <span class="box">\(BE \approx 28.3\ \mathrm{MeV}\)</span>
(≈ 7.07 MeV per nucleon)</p>""",
          topic="Atoms and Nuclei — Nuclei", recall=r"<ul><li>\(\Delta m = Zm_p + (A-Z)m_n - M_{\rm nucleus}\).</li><li>1 u ≡ 931 MeV.</li></ul>"),
        Q("14(a)", 3, r"""<p>Draw the circuit diagram of a full-wave rectifier using two junction diodes. Label the diagram showing the direction
of current through the circuit.</p>""",
          a=r"""{{fig:0}}<p class="step">The a.c. input is applied to the primary of a <b>centre-tapped</b> transformer. The ends
S₁, S₂ of the secondary feed diodes D₁, D₂, whose cathodes are joined at X; the load \(R_L\) is connected between X and
the centre tap T.</p>
<p class="step">During the half-cycle when S₁ is positive with respect to T, D₁ is forward biased and conducts
(D₂ reverse biased): current S₁ → D₁ → X → \(R_L\) → T.</p>
<p class="step">In the next half-cycle S₂ is positive: D₂ conducts and D₁ is off: current S₂ → D₂ → X → \(R_L\) → T.</p>
<p class="step">So the current through the load is <b>always from X to T</b> — a unidirectional (pulsating d.c.) output
during both halves of every cycle.</p>""",
          afig=[F.fig_a14a_fwr],
          topic=ELEC, recall=r"<ul><li>Diode conducts only when forward biased (p at higher potential).</li><li>Full-wave: output frequency = twice the input frequency.</li></ul>"),
        Q("14(b)", 2, r"""<p>Using several 'NAND' gates, how can you obtain an 'OR' gate? Draw a label diagram and write down the Boolean
expression for the output.</p>""",
          excluded="Logic gates — not in ISC 2027: Unit 9 has no digital electronics."),
        Q("15(a)", 2, r"""<p>Write down two needs for modulation in satellite communication.</p>""",
          excluded="Communication systems (modulation) — not in ISC 2027: 'modulation' occurs nowhere in the syllabus."),
        Q("15(b)", 3, r"""<p>Draw a labeled circuit diagram of a simple common-emitter amplifier. What is the phase angle between the input and
output voltage?</p>""",
          excluded="Transistor amplifier — not in ISC 2027: Unit 9 covers diodes only; transistors appear only in the demonstration practicals."),
    ])
