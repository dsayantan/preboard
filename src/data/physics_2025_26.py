"""Heritage School Pre-Board 2025-26, Physics Paper I (Theory) — digital copy, ISC 2027 filter, solutions.
Source of record: the Word file (SET-1/PHYSICS (1).docx); transcribed from its rendered pages."""
from kit import Q, SEC
import physics_2025_26_figs as F

ES, CE, MAG = "Electrostatics", "Current Electricity", "Magnetic Effects of Current and Magnetism"
EMI, EMW = "Electromagnetic Induction and Alternating Currents", "Electromagnetic Waves"
RAY, WAVE = "Optics — Ray Optics and Optical Instruments", "Optics — Wave Optics"
DUAL, ATOM, NUC, ELEC = ("Dual Nature of Radiation and Matter", "Atoms and Nuclei — Atoms",
                         "Atoms and Nuclei — Nuclei", "Electronic Devices")

PAPER = dict(
    subject="physics", year="2025-26", slug="2025-26", paper="Paper I (Theory)",
    source="PreBoard-PYQ/2025-26/SET-1/PHYSICS (1).docx", marks=70, time="Three hours",
    intro=r"""<p><i>(Candidates are allowed additional 15 minutes for <b>only</b> reading the paper. They must NOT start
writing during this time.)</i></p>
<p><b><i>All questions are compulsory. This question paper is divided in 4 Sections A, B, C and D as follows.</i></b></p>
<p><b>Section A</b> — Question number 1 is of 14 marks. All parts of this question are compulsory.<br>
<b>Section B</b> — Question numbers 2 to 8 carry 2 marks each with two questions having internal choice.<br>
<b>Section C</b> — Question numbers 9 to 17 carry 3 marks each with two questions having internal choice.<br>
<b>Section D</b> — Question numbers 18 to 20 are long-answer type questions and carry 5 marks each. Each question has
an internal choice.</p>
<p>The intended marks for questions are given in brackets [ ]. All working, including rough work, should be done on
the same sheet as and adjacent to the rest of the answer. Answers to sub parts of the same question must be given in
one place only. A list of useful physical constants is given at the end of this paper. A simple scientific
calculator without a programmable memory may be used for calculations.</p>
<p><b>Useful Constants &amp; Relations</b> (as printed): charge of a proton \(e = 1.6\times10^{-19}\) C; Planck's
constant \(h = 6.6\times10^{-34}\) J s; mass of an electron \(m_e = 9.1\times10^{-31}\) kg; permittivity of vacuum
\(\varepsilon_0 = 8.85\times10^{-12}\) F m\(^{-1}\); Rydberg's constant \(R = 1.097\times10^{7}\) m\(^{-1}\); speed of
light in vacuum \(c = 3\times10^{8}\) m s\(^{-1}\); permeability of vacuum \(\mu_0 = 4\pi\times10^{-7}\) H m\(^{-1}\);
Coulomb's constant \(\dfrac{1}{4\pi\varepsilon_0} = 9\times10^{9}\) N m\(^2\) C\(^{-2}\).</p>""",
    items=[
        SEC("Section A — 14 marks", "Question 1. (A) In questions (i) to (vii) choose the correct alternative (a), (b), "
            "(c) or (d) for each of the questions given below. [1×7]"),
        Q("1(A)(i)", 1, r"""<p>In an N-type semiconductor, there is</p>
<p>(a) a majority of free electrons &nbsp; (b) a majority of holes &nbsp; (c) an equal number of holes and free
electrons &nbsp; (d) a trivalent element as an impurity</p>""",
          a=r"""<p><b>(a) a majority of free electrons.</b></p>
<p class="step">N-type silicon/germanium is doped with a pentavalent (donor) impurity such as P or As; four of its
valence electrons form covalent bonds and the fifth becomes a free electron. Electrons are the majority carriers, holes
the minority carriers. (A trivalent impurity would make it p-type.)</p>""",
          topic=ELEC, recall=r"<ul><li>n-type: pentavalent donor (P, As, Sb) ⇒ \(n_e \gg n_h\).</li><li>p-type: trivalent acceptor (B, Al, In) ⇒ \(n_h \gg n_e\).</li></ul>"),
        Q("1(A)(ii)", 1, r"""<p>Zener diode is used as:</p>
<p>(a) Half wave rectifier &nbsp; (b) full wave rectifier &nbsp; (c) voltage regulator &nbsp; (d) an amplifier</p>""",
          a=r"""<p><b>(c) voltage regulator.</b></p>
<p class="step">In reverse breakdown the voltage across a Zener diode stays practically constant at \(V_Z\) over a
wide range of current, so connected in reverse bias across a load (with a series resistor) it holds the load voltage
steady.</p>""",
          topic=ELEC, recall=r"<ul><li>Zener: heavily doped, used in reverse breakdown; \(V_Z\) constant.</li><li>Series resistor drops the excess input voltage.</li></ul>"),
        Q("1(A)(iii)", 1, r"""<p>A circuit contains an ammeter, a battery of 30 V and a resistance of 40.8 ohm all connected in series. If
the ammeter has a coil of resistance 480 ohm and a shunt of 20 ohm, the reading in the ammeter will be:</p>
<p>(a) 0.25 A &nbsp; (b) 2 A &nbsp; (c) 1 A &nbsp; (d) 0.5 A</p>""",
          a=r"""<p><b>(d) 0.5 A</b></p>
<p class="step">Resistance of the ammeter = coil ∥ shunt \(= \dfrac{480\times20}{480+20} = 19.2\ \Omega\).</p>
<p class="step">Total resistance \(= 40.8 + 19.2 = 60\ \Omega\); \(I = \dfrac{30}{60} = 0.5\) A, which is what the
ammeter reads.</p>""",
          topic=CE, recall=r"<ul><li>Ammeter = galvanometer with a low shunt in parallel: \(R_A = GS/(G+S)\).</li><li>Ohm's law for the whole circuit \(I = E/R_{\text{total}}\).</li></ul>"),
        Q("1(A)(iv)", 1, r"""<p>When the current in a coil change from 8 A to 2 A in \(3\times10^{-2}\) second, the emf induced in the coil
is 2 V. The self-inductance of the coil, in millihenry is:</p>
<p>(a) 1 &nbsp; (b) 5 &nbsp; (c) 20 &nbsp; (d) 10</p>""",
          a=r"""<p><b>(d) 10</b></p>
<p class="step">\(|e| = L\dfrac{|\Delta I|}{\Delta t} \Rightarrow L = \dfrac{e\,\Delta t}{|\Delta I|} =
\dfrac{2\times3\times10^{-2}}{8-2} = 1\times10^{-2}\ \text{H} = 10\ \text{mH}\).</p>""",
          topic=EMI, recall=r"<ul><li>\(e = -L\,dI/dt\).</li><li>1 mH = \(10^{-3}\) H.</li></ul>"),
        Q("1(A)(v)", 1, r"""<p><b>Assertion (A):</b> The graph for 'v' versus 'u' of a concave mirror forming real images, falls within the
second quadrant.</p>
<p><b>Reason (R):</b> For concave mirrors, according to the sign convention for real images, 'u' is negative, and 'v'
is positive.</p>
<p>(a) Both Assertion and Reason are true, and Reason is the correct explanation for Assertion.<br>
(b) Both Assertion and Reason are true, but Reason is not the correct explanation for Assertion.<br>
(c) Assertion is true, and Reason is false.<br>
(d) Both Assertion and Reason are false.</p>""",
          a=r"""<p><b>(d) Both Assertion and Reason are false.</b></p>
<p class="step">In the Cartesian (New Cartesian) convention, distances are measured from the pole and the incident
light travels in the +x direction. For a concave mirror forming a real image, the object and the image are both in
front of the mirror, so <b>u and v are both negative</b>. The \(v\)–\(u\) graph is a rectangular hyperbola lying in
the <b>third quadrant</b>, with asymptotes \(u = f\) and \(v = f\) and passing through \((2f, 2f)\). {{fig:0}}</p>
<p class="step">So the Assertion (second quadrant) is false and the Reason (v positive) is false.</p>""",
          afig=[(F.fig_q1a5_vu, "v against u for a concave mirror, real images (f = −10 cm, Cartesian signs)")],
          topic=RAY, recall=r"<ul><li>Mirror formula \(\dfrac1v + \dfrac1u = \dfrac1f\); concave \(f\lt 0\).</li><li>Real image of a real object: both on the incident side ⇒ same sign as \(u\).</li></ul>"),
        Q("1(A)(vi)", 1, r"""<p>Variation of photoelectric current with intensity of light is best represented by:</p>{{fig:0}}""",
          qfig=[(F.fig_q1a6_photo, "The four options, redrawn")],
          a=r"""<p><b>(d)</b> — a straight line through the origin.</p>
<p class="step">For a given frequency above threshold, the number of photoelectrons emitted per second is proportional
to the number of photons falling per second, i.e. to the intensity. So the (saturation) photocurrent \(\propto\)
intensity: a straight line through the origin, with no saturation in intensity.</p>""",
          topic=DUAL, recall=r"<ul><li>Photocurrent ∝ intensity (ν fixed, ν &gt; ν₀).</li><li>Maximum KE depends on ν, not on intensity.</li></ul>"),
        Q("1(A)(vii)", 1, r"""<p>The de-Broglie wavelength \(\lambda\) associated with a moving electron having kinetic energy (E) is given
by:</p>
<p>(a) \(\dfrac{2h}{\sqrt{2mE}}\) &nbsp; (b) \(\dfrac{2\sqrt{2mE}}{h}\) &nbsp; (c) \(\dfrac{h}{\sqrt{2mE}}\) &nbsp;
(d) \(\sqrt{2mhE}\)</p>""",
          a=r"""<p><b>(c) \(\dfrac{h}{\sqrt{2mE}}\)</b></p>
<p class="step">\(E = \dfrac{p^2}{2m} \Rightarrow p = \sqrt{2mE}\), and \(\lambda = \dfrac{h}{p} = \dfrac{h}{\sqrt{2mE}}\).</p>""",
          topic=DUAL, recall=r"<ul><li>\(\lambda = h/p\).</li><li>\(K = p^2/2m\); for an accelerating p.d. V, \(K = eV\).</li></ul>"),

        SEC("Question 1 (B) — Answer the following questions briefly. [1×7]"),
        Q("1(B)(i)", 1, r"""<p>State one limitation of Bohr's atomic model.</p>""",
          a=r"""<p class="step">Any one of:</p><ul>
<li>It applies only to hydrogen and hydrogen-like (one-electron) ions such as He\(^+\), Li\(^{2+}\); it fails for
many-electron atoms.</li>
<li>It cannot explain the relative intensities of spectral lines, or their fine structure (each line is really a group
of close lines).</li>
<li>It does not explain the splitting of lines in a magnetic field (Zeeman effect) or an electric field (Stark
effect).</li></ul>""",
          topic=ATOM, recall=r"<ul><li>Bohr's postulates: stationary orbits, \(mvr = nh/2\pi\), \(h\nu = E_i - E_f\).</li></ul>"),
        Q("1(B)(ii)", 1, r"""<p>In an experiment of photoelectric effect, the slope of cutoff voltage versus frequency of incident light is
found to be \(4.12\times10^{-15}\) V s. Calculate the value of Planck's constant.</p>""",
          a=r"""<p class="step">\(eV_0 = h\nu - \phi_0 \Rightarrow V_0 = \dfrac{h}{e}\nu - \dfrac{\phi_0}{e}\), so slope \(= h/e\).</p>
<p class="step">\(h = e\times\text{slope} = 1.6\times10^{-19}\times4.12\times10^{-15}\)</p>
<p class="step"><span class="box">\(h = 6.59\times10^{-34}\) J s</span></p>""",
          topic=DUAL, recall=r"<ul><li>Einstein: \(eV_0 = h\nu - \phi_0\).</li><li>\(V_0\)–\(\nu\) graph: slope \(h/e\), intercept \(\nu_0\) on the ν-axis.</li></ul>"),
        Q("1(B)(iii)", 1, r"""<p>Give an advantage of reflecting telescopes over refracting telescopes.</p>""",
          a=r"""<p class="step">Any one: a mirror objective has <b>no chromatic aberration</b> (reflection does not depend on
wavelength); a parabolic mirror is free from spherical aberration; a large-aperture mirror is easier and cheaper to
make and support than a large lens, so it gathers more light and has greater <b>resolving power</b>.</p>""",
          topic=RAY, recall=r"<ul><li>Resolving power of a telescope ∝ aperture D / λ.</li><li>Lenses disperse light (chromatic aberration); mirrors do not.</li></ul>"),
        Q("1(B)(iv)", 1, r"""<p>Find the angular momentum of an electron when it is in the second Bohr's orbit of a hydrogen atom.</p>""",
          a=r"""<p class="step">\(L = \dfrac{nh}{2\pi} = \dfrac{2\times6.6\times10^{-34}}{2\times3.14}\)</p>
<p class="step"><span class="box">\(L = 2.1\times10^{-34}\) J s</span> \((= h/\pi)\)</p>""",
          topic=ATOM, recall=r"<ul><li>Bohr's quantisation: \(mvr = nh/2\pi\).</li></ul>"),
        Q("1(B)(v)", 1, r"""<p>If a hydrogen atom goes from the 3rd excited state to 2nd excited state, what kind of radiation is emitted?</p>""",
          a=r"""<p class="step">3rd excited state is \(n = 4\); 2nd excited state is \(n = 3\). A transition ending on \(n = 3\)
belongs to the <b>Paschen series</b>.</p>
<p class="step">\(\dfrac1\lambda = R\left(\dfrac1{3^2}-\dfrac1{4^2}\right) = \dfrac{7R}{144} \Rightarrow
\lambda = \dfrac{144}{7\times1.097\times10^{7}} = 1.88\times10^{-6}\) m ≈ 1875 nm.</p>
<p class="step"><span class="box">Infrared radiation</span> (Paschen series, λ ≈ 1875 nm).</p>""",
          topic=ATOM, recall=r"<ul><li>Ground state n = 1; k-th excited state n = k + 1.</li><li>Lyman (→1) UV, Balmer (→2) visible, Paschen (→3) IR.</li></ul>"),
        Q("1(B)(vi)", 1, r"""<p>Name the particles and radiation involved in a pair production. Give equation relating them.</p>""",
          a=r"""<p class="step">A <b>γ-ray photon</b> passing close to a nucleus converts into an <b>electron</b> and a
<b>positron</b>:</p>
<p class="step">\(\gamma \;\rightarrow\; {}_{-1}^{\;\;0}e + {}_{+1}^{\;\;0}e\), &nbsp; with \(h\nu = 2m_0c^2 + K_{e^-} + K_{e^+}\),
so \(h\nu \ge 2m_0c^2 = 1.02\) MeV.</p>""",
          topic=NUC, recall=r"<ul><li>\(E = mc^2\); rest energy of an electron = 0.511 MeV.</li><li>Annihilation is the reverse: \(e^- + e^+ \to 2\gamma\).</li></ul>"),
        Q("1(B)(vii)", 1, r"""<p>In a nuclear reactor what are cadmium rods used for?</p>""",
          a=r"""<p class="step">Cadmium rods are the <b>control rods</b>: cadmium absorbs neutrons strongly, so pushing the
rods in or pulling them out controls the number of neutrons available for fission and keeps the chain reaction steady
(multiplication factor \(k = 1\)); fully inserted they shut the reactor down.</p>""",
          topic=NUC, recall=r"<ul><li>Reactor parts: fuel, moderator (slows neutrons), control rods (absorb), coolant, shielding.</li></ul>"),

        SEC("Section B — 14 marks"),
        Q("2", 2, r"""<p>The electric potential as a function of distance x as shown in the figure. Construct a graph of electric
field strength E as a function of distance x.</p>{{fig:0}}""",
          qfig=[(F.fig_q2_vx, "V against x, as printed (no values on the V-axis)")],
          a=r"""<p class="step">\(E = -\dfrac{dV}{dx}\), i.e. minus the slope of the V–x graph. Let the maximum potential be
\(V_0\) and x be in metres.</p>
<p class="step">0 &lt; x &lt; 1: V rises uniformly from 0 to \(V_0\), slope \(= +V_0\) ⇒ \(E = -V_0\) (constant).<br>
1 &lt; x &lt; 2: V constant ⇒ \(E = 0\).<br>
2 &lt; x &lt; 3: V falls uniformly from \(V_0\) to 0, slope \(= -V_0\) ⇒ \(E = +V_0\) (constant).</p>
{{fig:0}}
<p class="note">[The paper gives no value on the V-axis, so the field is expressed in terms of the maximum potential
\(V_0\); E has the unit V m\(^{-1}\).]</p>""",
          afig=[(F.fig_q2_ex, "E against x: three constant steps")],
          topic=ES, recall=r"<ul><li>\(E = -dV/dx\): field points towards decreasing potential.</li><li>Uniform slope ⇒ uniform field; constant V ⇒ E = 0.</li></ul>"),
        Q("3", 2, r"""<p>If there are identical capacitors all connected in parallel connected to V volt source, then find the energy
stored in the system.</p>
<p class="note">[The number of capacitors and their capacitance are missing from the printed question; taken as
\(n\) capacitors, each of capacitance \(C\).]</p>""",
          a=r"""<p class="step">In parallel, \(C_{\text{eq}} = C + C + \dots\) (n terms) \(= nC\), and each capacitor has the full
p.d. V.</p>
<p class="step">\(U = \tfrac12 C_{\text{eq}}V^2\) ⇒ <span class="box">\(U = \tfrac12\,nCV^2\)</span></p>
<p class="step">(Equivalently, n times the energy \(\tfrac12CV^2\) of one capacitor.)</p>""",
          topic=ES, recall=r"<ul><li>Parallel: \(C_p = \sum C_i\), same V.</li><li>\(U = \tfrac12CV^2 = \tfrac12QV = Q^2/2C\).</li></ul>"),
        Q("4(a)", 2, r"""<p>A heater takes 20 minutes to boil a given amount of water. Its coil is cut and (¼)th of its length is used in
the heater now. How much time will it take now to boil the same amount of water using the same source beginning with
the same initial temperature?</p>""",
          a=r"""<p class="step">The heat needed, \(H\), is the same. With the same source voltage V,
\(H = \dfrac{V^2}{R}\,t\) ⇒ \(t \propto R\).</p>
<p class="step">\(R \propto l\): using \(\tfrac14\) of the length, \(R' = R/4\).</p>
<p class="step">\(t' = t\,\dfrac{R'}{R} = 20\times\dfrac14\) ⇒ <span class="box">\(t' = 5\) minutes</span></p>""",
          topic=CE, recall=r"<ul><li>\(P = V^2/R\) at constant V; \(H = Pt\).</li><li>\(R = \rho l/A\).</li></ul>"),
        Q("4(b)", 2, r"""<p>(OR) Name a material which has very low temperature coefficient of resistance and give an example of a non
Ohmic conductor.</p>""",
          a=r"""<p class="step">Low temperature coefficient of resistance: <b>manganin</b> (or constantan, nichrome) — used in
standard resistors and resistance boxes.</p>
<p class="step">Non-ohmic conductor: a <b>semiconductor diode</b> (p-n junction) — or a filament lamp, an electrolyte, a
thermistor; its V–I graph is not a straight line through the origin.</p>""",
          topic=CE, recall=r"<ul><li>\(R_t = R_0(1+\alpha t)\); alloys have very small α.</li><li>Ohmic: V ∝ I at constant temperature.</li></ul>"),
        Q("5", 2, r"""<p>What is the SI unit of magnetic dipole moment? State its direction as well.</p>""",
          a=r"""<p class="step">SI unit: <span class="box">A m\(^2\)</span> (ampere metre², equivalently J T\(^{-1}\)).</p>
<p class="step">Direction: for a current loop \(\vec m = NI\vec A\), along the normal to the plane of the loop given by the
right-hand thumb rule (fingers curled along the current, thumb gives \(\vec m\)). For a bar magnet it points from its
<b>S-pole to its N-pole</b>.</p>""",
          topic=MAG, recall=r"<ul><li>\(\vec m = NI\vec A\); torque \(\vec\tau = \vec m\times\vec B\).</li></ul>"),
        Q("6(a)", 2, r"""<p>The angle of an equilateral glass prism is 59.5 degrees. The angle of minimum deviation is 38.5 degrees.
Without using the value of refractive index of the glass, calculate the angle of incidence for ray of light suffering
minimum deviation.</p>""",
          a=r"""<p class="step">At minimum deviation \(i = e\) and \(r_1 = r_2 = A/2\). Since \(\delta = i + e - A\),
\(\delta_m = 2i - A\).</p>
<p class="step">\(i = \dfrac{A + \delta_m}{2} = \dfrac{59.5^\circ + 38.5^\circ}{2}\) ⇒ <span class="box">\(i = 49^\circ\)</span></p>
<p class="note">[An "equilateral" prism would have A = 60°; the value 59.5° printed is used.]</p>""",
          topic=RAY, recall=r"<ul><li>\(\delta = i + e - A\), \(r_1 + r_2 = A\).</li><li>At \(\delta_m\): \(i = e\), ray inside parallel to the base.</li></ul>"),
        Q("6(b)", 2, r"""<p>(OR) The far point of a myopic eye is 10 cm from the eyes. What must be the focal length of lens reading at
least distance of distinct vision (25 cm)?</p>""",
          excluded="Defects of vision (myopia and its correction) — not in the ISC 2027 Class XII syllabus, whose Optics unit "
                   "lists mirrors, refraction, lenses, prisms and optical instruments but not the human eye."),
        Q("7", 2, r"""<p>Show that the shortest wavelengths in Lyman, Balmer and Paschen series have their wavelengths in the ratio of
1 : 4 : 9.</p>""",
          a=r"""<p class="step">\(\dfrac1\lambda = R\left(\dfrac1{n_f^2} - \dfrac1{n_i^2}\right)\). The shortest wavelength (series
limit) is for \(n_i \to \infty\): \(\dfrac1{\lambda_{\min}} = \dfrac{R}{n_f^2}\) ⇒ \(\lambda_{\min} = \dfrac{n_f^2}{R}\).</p>
<p class="step">Lyman \(n_f = 1\): \(\lambda_L = 1/R\); Balmer \(n_f = 2\): \(\lambda_B = 4/R\); Paschen \(n_f = 3\):
\(\lambda_P = 9/R\).</p>
<p class="step"><span class="box">\(\lambda_L : \lambda_B : \lambda_P = 1 : 4 : 9\)</span></p>{{fig:0}}""",
          afig=[(F.fig_q7_levels, "Series limits: transitions from n = ∞")],
          topic=ATOM, recall=r"<ul><li>Rydberg formula \(1/\lambda = R(1/n_f^2 - 1/n_i^2)\).</li><li>Series limit ⇒ \(n_i = \infty\).</li></ul>"),
        Q("8", 2, r"""<p>Analyse the figures given below and mention the significance of electromagnetic waves in each case.</p>{{fig:0}}""",
          qfig=[(F.fig_q8_em, "Fig-1 a greenhouse in sunlight; fig-2 a welder at work (redrawn schematically from the photographs)")],
          a=r"""<p class="step"><b>Fig-1 (greenhouse) — infrared waves.</b> Visible and short infrared radiation from the Sun passes
through the glass and warms the plants and soil. These re-emit long-wavelength <b>infrared</b> (heat) radiation, which
glass does not transmit, so it is trapped and keeps the greenhouse warm (greenhouse effect).</p>
<p class="step"><b>Fig-2 (welding) — ultraviolet waves.</b> The welding arc is very hot and emits intense
<b>ultraviolet</b> radiation (and glare), which damages the eyes and skin. The welder wears a special dark glass
goggle/face shield that absorbs UV.</p>""",
          topic=EMW, recall=r"<ul><li>IR: heat radiation, greenhouse effect, physiotherapy.</li><li>UV: from very hot sources (arc, Sun); absorbed by glass/ozone; harmful to eyes.</li></ul>"),

        SEC("Section C — 27 marks"),
        Q("9", 3, r"""<p>(a) A monochromatic light source emits light of wavelength 198 nm. Calculate the energy of each photon and
momentum of photons.</p>
<p>(b) Plot labelled graph of stopping potential versus frequency of incident radiation.</p>""",
          a=r"""<p><b>(a)</b></p>
<p class="step">\(E = \dfrac{hc}{\lambda} = \dfrac{6.6\times10^{-34}\times3\times10^{8}}{198\times10^{-9}}\)
⇒ <span class="box">\(E = 1.0\times10^{-18}\) J \(= 6.25\) eV</span></p>
<p class="step">\(p = \dfrac{h}{\lambda} = \dfrac{6.6\times10^{-34}}{198\times10^{-9}}\)
⇒ <span class="box">\(p = 3.33\times10^{-27}\) kg m s\(^{-1}\)</span></p>
<p><b>(b)</b> \(eV_s = h\nu - \phi_0\), so \(V_s = \dfrac{h}{e}\nu - \dfrac{\phi_0}{e}\): a straight line cutting
the frequency axis at the threshold frequency \(\nu_0\), slope \(h/e\) (the same for every metal), and extrapolated
intercept \(-\phi_0/e\) on the \(V_s\)-axis. No emission below \(\nu_0\).</p>{{fig:0}}""",
          afig=[(F.fig_q9_vs_nu, "Stopping potential against frequency")],
          topic=DUAL, recall=r"<ul><li>\(E = h\nu = hc/\lambda\); \(p = h/\lambda = E/c\).</li><li>1 eV = \(1.6\times10^{-19}\) J.</li></ul>"),
        Q("10", 3, r"""<p>Calculate the: i) equivalent capacitance of the circuit between points A and B. ii) The charge on
C<sub>1</sub>.</p>{{fig:0}}""",
          qfig=[(F.fig_q10_caps, "")],
          a=r"""<p class="step">(i) C<sub>1</sub> and C<sub>2</sub> are in series:
\(C_{12} = \dfrac{C_1C_2}{C_1+C_2} = \dfrac{3\times6}{3+6} = 2\ \mu\)F.</p>
<p class="step">This branch is in parallel with C<sub>3</sub>: \(C_{AB} = 2 + 10\) ⇒ <span class="box">\(C_{AB} = 12\ \mu\)F</span></p>
<p class="step">(ii) The series branch has the full 50 V across it, and C<sub>1</sub>, C<sub>2</sub> in series carry
the same charge: \(Q_1 = C_{12}V = 2\ \mu\text{F}\times50\ \text{V}\) ⇒ <span class="box">\(Q_1 = 100\ \mu\)C</span>
\(= 1\times10^{-4}\) C.</p>
<p class="step">(Check: \(V_1 = 100/3 = 33.3\) V, \(V_2 = 100/6 = 16.7\) V, total 50 V.)</p>""",
          topic=ES, recall=r"<ul><li>Series: same Q, \(1/C_s = \sum 1/C_i\).</li><li>Parallel: same V, \(C_p = \sum C_i\).</li></ul>"),
        Q("11(a)", 3, r"""<p>In a meter bridge circuit, resistance in the left hand gap is 2 ohm and an unknown resistance X is in the
right hand gap as shown in the figure below. The null point is found to be 40 cm from left end of the wire. What
resistance should be connected to X so that the new null point is 50 cm from the left end of the wire?</p>{{fig:0}}""",
          qfig=[(F.fig_q11_bridge, "")],
          a=r"""<p class="step">Balance condition: \(\dfrac{P}{Q} = \dfrac{l}{100-l}\).</p>
<p class="step">\(\dfrac{2}{X} = \dfrac{40}{60}\) ⇒ \(X = 3\ \Omega\).</p>
<p class="step">For the null point at 50 cm the right gap must equal the left: \(R_{\text{right}} = 2\ \Omega\). It must
fall from 3 Ω to 2 Ω, so a resistance S is joined <b>in parallel</b> with X:</p>
<p class="step">\(\dfrac{3S}{3+S} = 2 \Rightarrow 3S = 6 + 2S\) ⇒ <span class="box">\(S = 6\ \Omega\) in parallel with X</span></p>{{fig:0}}""",
          afig=[(F.fig_q11a_new, "Right-hand gap after adding S")],
          topic=CE, recall=r"<ul><li>Metre bridge: \(R/S = l/(100-l)\).</li><li>To reduce a resistance add one in parallel; to increase, in series.</li></ul>"),
        Q("11(b)", 3, r"""<p>(OR) Using Ampere's circuital law, obtain an expression for the magnetic flux density 'B' at a point 'X' at a
perpendicular distance 'r' from a long current carrying conductor.</p>""",
          a=r"""<p class="step"><b>Ampere's circuital law:</b> \(\oint \vec B\cdot d\vec l = \mu_0 I\), where I is the net current
threading the closed loop.</p>
<p class="step">Take as the Amperian loop a circle of radius r through X, in a plane perpendicular to the wire, centred on
it. {{fig:0}}</p>
<p class="step">By symmetry B has the same magnitude at every point of the loop and is tangential to it, so
\(\vec B \parallel d\vec l\) and \(\vec B\cdot d\vec l = B\,dl\).</p>
<p class="step">\(\oint \vec B\cdot d\vec l = B\oint dl = B(2\pi r) = \mu_0 I\)</p>
<p class="step"><span class="box">\(B = \dfrac{\mu_0 I}{2\pi r}\)</span>, along the tangent to the circle; direction by the
right-hand grip rule.</p>""",
          afig=[(F.fig_q11b_ampere, "End-on view: current out of the page, B anticlockwise")],
          topic=MAG, recall=r"<ul><li>\(\oint\vec B\cdot d\vec l = \mu_0 I_{\text{enc}}\).</li><li>Choose a loop on which B is constant and parallel to dl.</li></ul>"),
        Q("12(a)", 3, r"""<p>In series LCR circuit using phasor diagram, derive an expression for impedance.</p>""",
          a=r"""<p class="step">Let \(I = I_0\sin\omega t\) flow through R, L and C in series (same current in all). Peak voltages:
\(V_R = I_0R\) in phase with I; \(V_L = I_0X_L\) leading I by 90°; \(V_C = I_0X_C\) lagging I by 90°, where
\(X_L = \omega L\), \(X_C = 1/\omega C\).</p>
<p class="step">Draw I along the x-axis. \(V_L\) and \(V_C\) are opposite, so their resultant is \(V_L - V_C\) (taking
\(X_L \gt X_C\)) along +y; the applied voltage \(V_0\) is the phasor sum of \(V_R\) and \(V_L - V_C\). {{fig:0}}</p>
<p class="step">\(V_0^2 = V_R^2 + (V_L - V_C)^2 = I_0^2\left[R^2 + (X_L - X_C)^2\right]\)</p>
<p class="step">Impedance \(Z = \dfrac{V_0}{I_0}\) ⇒ <span class="box">\(Z = \sqrt{R^2 + \left(\omega L - \dfrac{1}{\omega C}\right)^2}\)</span></p>
<p class="step">Phase angle: \(\tan\phi = \dfrac{V_L - V_C}{V_R} = \dfrac{X_L - X_C}{R}\), voltage leading the current
by φ.</p>""",
          afig=[(F.fig_q12a_phasor, "Phasor diagram, series LCR (X_L > X_C)")],
          topic=EMI, recall=r"<ul><li>\(X_L = \omega L\) (V leads I by 90°), \(X_C = 1/\omega C\) (V lags by 90°).</li><li>Phasors add as vectors.</li></ul>"),
        Q("12(b)", 3, r"""<p>(OR) In series LCR circuit draw I vs ω graph and label the bandwidth, resonant frequency and current
amplitude.</p>""",
          a=r"""<p class="step">\(I_0 = \dfrac{V_0}{\sqrt{R^2 + (\omega L - 1/\omega C)^2}}\): the current is maximum
(\(= V_0/R\)) at the resonant frequency \(\omega_0 = 1/\sqrt{LC}\), where \(X_L = X_C\), and falls on either side.</p>
{{fig:0}}
<p class="step"><b>Current amplitude</b> at resonance: \(I_0 = V_0/R\) (the peak). <b>Resonant frequency</b>:
\(\omega_0 = 1/\sqrt{LC}\). <b>Bandwidth</b>: \(\Delta\omega = \omega_2 - \omega_1\), where \(\omega_1, \omega_2\) are the
frequencies at which the current falls to \(I_0/\sqrt2\) (half-power points); \(\Delta\omega = R/L\). A smaller R
gives a sharper peak (higher Q = \(\omega_0/\Delta\omega\)).</p>""",
          afig=[(F.fig_q12b_resonance, "Resonance curve of a series LCR circuit")],
          topic=EMI, recall=r"<ul><li>Resonance: \(X_L = X_C\), Z = R, \(\omega_0 = 1/\sqrt{LC}\).</li><li>Half-power points at \(I_0/\sqrt2\); Q = \(\omega_0/\Delta\omega\).</li></ul>"),
        Q("13", 3, r"""<p>Student 1 and Student 2 conducted experiments using coherent sources of light, with Student 1 using a single
slit and Student 2 using a double slit.</p>{{fig:0}}
<p>Answer the following questions.</p>
<p>(a) Identify the patterns resulting from Student 1 and Student 2 experiments.</p>
<p>(b) Give <i>two</i> reasons that assisted you in recognizing the patterns.</p>""",
          qfig=[(F.fig_q13_patterns, "Patterns A, B and C (redrawn)")],
          a=r"""<p class="step"><b>(a)</b> Student 1 (single slit) — <b>pattern C</b>, a diffraction pattern.
Student 2 (double slit) — <b>pattern B</b>, an interference pattern.</p>
<p class="step"><b>(b)</b> 1. Pattern C has a <b>much wider, very bright central maximum</b> with secondary maxima that
are narrower and far fainter (intensity falls off rapidly) — the signature of single-slit diffraction (central
maximum is twice as wide as the others).<br>
2. Pattern B has <b>equally spaced fringes of equal width and nearly equal brightness</b> — the signature of
two-source interference, where fringe width \(\beta = \lambda D/d\) is constant.</p>
<p class="step">(Pattern A, whose rings crowd closer together outward, is neither.)</p>
<p class="note">This is CISCE Competency-Focused Practice Question 92 (parts (a) and (b)). Its published key: "Student 1 –
Pattern C; Student 2 – Pattern B", the reasons being the wider central maximum with fringe widths diminishing outward
(diffraction, C) and the uniform fringe widths (interference, B).</p>""",
          topic=WAVE, recall=r"<ul><li>Interference: equal fringe width \(\beta = \lambda D/d\), equal intensity.</li><li>Single-slit diffraction: central maximum width \(2\lambda D/a\), intensity falls rapidly.</li></ul>"),
        Q("14", 3, r"""<p><b>Match the following:</b></p>
<table class="plain"><tr><td>1.</td><td>\(\omega L \gt \dfrac{1}{\omega C}\)</td><td>(i)</td><td>The current is in phase with voltage V.</td></tr>
<tr><td>2.</td><td>\(\omega L \lt \dfrac{1}{\omega C}\)</td><td>(ii)</td><td>The current lags in phase with voltage V.</td></tr>
<tr><td>3.</td><td>\(\omega L = \dfrac{1}{\omega C}\)</td><td>(iii)</td><td>The current leads in phase with voltage V.</td></tr></table>""",
          a=r"""<p class="step"><span class="box">1 → (ii), 2 → (iii), 3 → (i)</span></p>
<p class="step">\(\tan\phi = \dfrac{X_L - X_C}{R}\).<br>
1. \(X_L \gt X_C\): φ positive, circuit inductive — <b>current lags</b> the voltage.<br>
2. \(X_L \lt X_C\): φ negative, circuit capacitive — <b>current leads</b> the voltage.<br>
3. \(X_L = X_C\): φ = 0, resonance, Z = R — <b>current in phase</b> with the voltage.</p>""",
          topic=EMI, recall=r"<ul><li>Inductive: I lags V; capacitive: I leads V (mnemonic CIVIL).</li><li>\(\tan\phi = (X_L - X_C)/R\).</li></ul>"),
        Q("15", 3, r"""<p>AB and CD are two parallel conductors kept 1 m apart and connected by a resistance R of 6 ohm, as shown in the
figure below. They are placed in a magnetic field \(B = 3\times10^{-2}\) T which is perpendicular to the plane of the
conductors and directed into the paper. A wire MN is placed over AB and CD and then made to slide with velocity 2 m/s.
(Neglect the resistance of AB, CD and MN.) Calculate the induced current flowing through the resistor R.</p>{{fig:0}}""",
          qfig=[(F.fig_q15_rails, "")],
          a=r"""<p class="step">Motional emf: \(e = Blv = 3\times10^{-2}\times1\times2 = 0.06\) V.</p>
<p class="step">\(I = \dfrac{e}{R} = \dfrac{0.06}{6}\) ⇒ <span class="box">\(I = 0.01\) A \(= 10\) mA</span></p>
<p class="step">Direction (taking MN moving to the right, away from R): the area of loop AMNC and the inward flux
increase, so by Lenz's law the induced current makes an outward field — anticlockwise as seen: from N to M in the rod,
and <b>from A to C through R</b> (Fleming's right-hand rule gives the same). {{fig:0}}</p>""",
          afig=[(F.fig_q15_ans, "Induced current when MN moves to the right")],
          topic=EMI, recall=r"<ul><li>\(e = Blv\) (B ⊥ l ⊥ v).</li><li>Lenz's law / Fleming's right-hand rule for direction.</li></ul>"),
        Q("16", 3, r"""<p>In Young's double slit experiment using monochromatic light of wavelength 600 nm, 5th bright fringe is at a
distance of 0.48 mm from the centre of the pattern. If the screen is at a distance of 80 cm from the plane of the two
slits, calculate:</p>
<p>i) Distance between the two slits.<br>ii) Fringe width.</p>
<p class="note">[The paper prints the clause "If the screen is at a distance of 0.48 mm from the centre of the pattern"
twice; the duplicate is a typing slip and is dropped here.]</p>""",
          a=r"""<p class="step">Position of the n-th bright fringe: \(y_n = \dfrac{n\lambda D}{d}\).</p>
<p class="step">(i) \(d = \dfrac{n\lambda D}{y_5} = \dfrac{5\times600\times10^{-9}\times0.80}{0.48\times10^{-3}}\)
⇒ <span class="box">\(d = 5.0\times10^{-3}\) m \(= 5\) mm</span></p>
<p class="step">(ii) \(\beta = \dfrac{\lambda D}{d} = \dfrac{y_5}{5} = \dfrac{0.48}{5}\) mm ⇒
<span class="box">\(\beta = 0.096\) mm \(= 9.6\times10^{-5}\) m</span></p>""",
          topic=WAVE, recall=r"<ul><li>Bright fringes \(y_n = n\lambda D/d\); fringe width \(\beta = \lambda D/d\).</li></ul>"),
        Q("17", 3, r"""<p>In an optics experiment, an optics student is using a compound microscope. The examiner gives the requisite
instructions and asks the student some questions. State whether the responses of the student, in each case, is correct
or incorrect. Give a reason for your answer.</p>
<p>i) <b>Examiner:</b> increase the magnification produced by the objective lens.<br>
<b>Student:</b> Decrease the distance between object and objective lens, keeping in mind that this distance must be
greater than the focal length of the objective lens.</p>
<p>ii) <b>Examiner:</b> Increase the resolving power of the instrument.<br>
<b>Student:</b> Illuminates the object with the light of longer wavelength.</p>
<p>iii) <b>Examiner:</b> Which of the two lenses among f<sub>1</sub>, f<sub>2</sub> and f<sub>3</sub> will you prefer to
take as an objective and eyepiece of compound microscope? (f<sub>1</sub> = 2 cm, f<sub>2</sub> = 100 cm and
f<sub>3</sub> = 6 cm)<br>
<b>Student:</b> f<sub>1</sub> = 2 cm as an objective and f<sub>2</sub> = 100 cm as an eyepiece.</p>""",
          a=r"""<p class="step">(i) <b>Correct.</b> \(m_o = \dfrac{v_o}{u_o} = \dfrac{f_o}{u_o - f_o}\) (magnitudes): as the object
is brought closer to \(F_o\) (still outside it, so the image stays real), \(v_o\) increases and \(u_o\) decreases, so
the magnification increases.</p>
<p class="step">(ii) <b>Incorrect.</b> Resolving power of a microscope \(= \dfrac{2n\sin\theta}{1.22\lambda}\propto
\dfrac1\lambda\); it is increased by using light of <b>shorter</b> wavelength (e.g. blue/UV).</p>
<p class="step">(iii) <b>Incorrect</b> (partly). The objective f<sub>1</sub> = 2 cm is right, but the eyepiece should also
have a short focal length — <b>f<sub>3</sub> = 6 cm</b> — since \(M = \dfrac{v_o}{u_o}\left(1 + \dfrac{D}{f_e}\right)\)
is larger for a smaller \(f_e\). A 100 cm lens would give almost no eyepiece magnification (it suits a telescope
objective).</p>""",
          topic=RAY, recall=r"<ul><li>Compound microscope: \(M = m_o m_e\), \(m_e = 1 + D/f_e\); both \(f_o\), \(f_e\) small, \(f_o \lt f_e\).</li><li>Resolving power ∝ 1/λ.</li></ul>"),

        SEC("Section D — 15 marks"),
        Q("18(a)", 5, r"""<p>I) For 2 thin lenses kept in contact with each other show that \(\dfrac1F = \dfrac1{f_1} + \dfrac1{f_2}\).</p>
<p>II) Calculate the critical angle for glass-air interface, if a ray of light incident on the interface is deviated
through 15 degree when its angle of incidence is 40 degree.</p>""",
          a=r"""<p><b>I)</b> Let thin lenses L<sub>1</sub> (focal length \(f_1\)) and L<sub>2</sub> (\(f_2\)) be in contact on a
common axis, and O a point object at distance u. {{fig:0}}</p>
<p class="step">L<sub>1</sub> alone would form the image I<sub>1</sub> at \(v_1\): \(\dfrac1{v_1} - \dfrac1u = \dfrac1{f_1}\) … (1)</p>
<p class="step">I<sub>1</sub> acts as the (virtual) object for L<sub>2</sub>, which forms the final image I at v. The lenses
are thin and in contact, so distances are measured from the same point:
\(\dfrac1v - \dfrac1{v_1} = \dfrac1{f_2}\) … (2)</p>
<p class="step">Adding (1) and (2): \(\dfrac1v - \dfrac1u = \dfrac1{f_1} + \dfrac1{f_2}\).</p>
<p class="step">If the combination is a single lens of focal length F, \(\dfrac1v - \dfrac1u = \dfrac1F\), so
<span class="box">\(\dfrac1F = \dfrac1{f_1} + \dfrac1{f_2}\)</span> (and \(P = P_1 + P_2\)).</p>
<p><b>II)</b> The ray is incident <b>from air on the glass</b> at \(i = 40^\circ\). Entering the denser medium it
bends <b>towards</b> the normal, so the angle of refraction is \(r = i - \delta = 40^\circ - 15^\circ = 25^\circ\). {{fig:1}}</p>
<p class="step">Snell's law: \(n_g = \dfrac{\sin i}{\sin r} = \dfrac{\sin40^\circ}{\sin25^\circ} = \dfrac{0.6428}{0.4226} = 1.521\)</p>
<p class="step">The critical angle C (for light going from glass to air, at the same interface):
\(\sin C = \dfrac1{n_g} = \dfrac{1}{1.521} = 0.6575\) ⇒ <span class="box">\(C \approx 41.1^\circ\)</span></p>
<p class="note">[The question does not say on which side the ray starts. The data decide it: taking the ray inside the
glass (bending away, r = 55°) would give \(n = \sin55^\circ/\sin40^\circ = 1.27\), far below any glass, whereas the
air-to-glass reading gives n = 1.52, the refractive index of ordinary glass. (A glass of n = 1.52 could not even give a
15° deviation from inside at 40°: the ray would emerge at 77.9°.) The critical angle is a property of the interface,
so it is found either way from \(\sin C = 1/n\).]</p>""",
          afig=[(F.fig_q18_lenses, "Two thin lenses in contact (drawn to scale: f₁ = 40, f₂ = 60, u = −60 ⇒ v₁ = 120, v = 40)"),
                (F.fig_q18_refraction, "Air to glass: i = 40°, r = 25°, deviation 15°")],
          topic=RAY, recall=r"<ul><li>Lens formula \(1/v - 1/u = 1/f\) (Cartesian).</li><li>Image by the first lens = object for the second.</li><li>Snell: \(n = \sin i/\sin r\); entering a denser medium the ray bends towards the normal, \(\delta = i - r\).</li><li>\(\sin C = 1/n\) (denser → rarer).</li></ul>"),
        Q("18(b)", 5, r"""<p>(OR) i) Derive laws of reflection using Huygen's principle.</p>
<p>ii) If you had to construct an optical fibre using the two materials, which would you prefer for the core and the
cladding? X: with a refractive index of 1.4905 or Y: with a refractive index of 1.337? Give reason in support of your
answer.</p>""",
          a=r"""<p><b>(i)</b> <b>Huygens' principle:</b> every point on a wavefront is a source of secondary wavelets spreading
with the speed of the wave; the new wavefront is the forward envelope (common tangent) of these wavelets.</p>
<p class="step">A plane wavefront AB strikes the reflecting surface XY, A touching it first, at angle of incidence i.
While the disturbance at B travels to C (BC = ct), the secondary wavelet from A spreads to a hemisphere of radius
AD = ct. The tangent CD from C to this wavelet is the reflected wavefront. {{fig:0}}</p>
<p class="step">In right-angled triangles ABC and CDA (right angles at B and D): AC is common and BC = AD = ct, so
the triangles are congruent ⇒ ∠BAC = ∠DCA.</p>
<p class="step">∠BAC is the angle between the incident wavefront and the surface = angle of incidence i;
∠DCA = angle between the reflected wavefront and the surface = angle of reflection r. Hence
<span class="box">\(i = r\)</span>. Also the incident ray, the reflected ray and the normal all lie in the plane of the
figure — the second law.</p>
<p><b>(ii)</b> <b>Core: X (n = 1.4905); cladding: Y (n = 1.337).</b> Light is guided by total internal reflection
at the core–cladding boundary, which needs light travelling in the <b>optically denser</b> medium, so the core must
have the higher refractive index. Critical angle \(\sin C = \dfrac{1.337}{1.4905} = 0.897\), C ≈ 63.8°: rays striking
the boundary at more than 63.8° are totally reflected and travel along the fibre. {{fig:1}}</p>""",
          afig=[(F.fig_q18_huygens, "Reflection of a plane wavefront (BC = AD = ct)"), (F.fig_q18_fibre, "Optical fibre")],
          topic=WAVE, recall=r"<ul><li>Huygens: secondary wavelets; new wavefront = envelope.</li><li>TIR needs denser → rarer and angle &gt; C; \(\sin C = n_2/n_1\).</li></ul>"),
        Q("19(a)", 5, r"""<p>Using Bohr's postulates derive an expression for velocity of electrons in the hydrogen atom and prove that it
is 1/137 times the speed of light.</p>""",
          a=r"""<p class="step"><b>Postulates used:</b> (1) the electron moves in a circular orbit, the Coulomb attraction of the
nucleus providing the centripetal force; (2) only those orbits are allowed in which the angular momentum is an
integral multiple of \(h/2\pi\): \(mvr = \dfrac{nh}{2\pi}\). {{fig:0}}</p>
<p class="step">(1): \(\dfrac{mv^2}{r} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{e^2}{r^2}\) ⇒ \(mv^2r = \dfrac{e^2}{4\pi\varepsilon_0}\) … (i)</p>
<p class="step">(2): \(mvr = \dfrac{nh}{2\pi}\) … (ii)</p>
<p class="step">Dividing (i) by (ii): <span class="box">\(v_n = \dfrac{e^2}{2\varepsilon_0 nh}\)</span></p>
<p class="step">For the first orbit (n = 1): \(\dfrac{v_1}{c} = \dfrac{e^2}{2\varepsilon_0hc} =
\dfrac{(1.6\times10^{-19})^2}{2\times8.85\times10^{-12}\times6.6\times10^{-34}\times3\times10^{8}} =
\dfrac{2.56\times10^{-38}}{3.505\times10^{-36}} = 7.30\times10^{-3}\)</p>
<p class="step">\(\dfrac{v_1}{c} = \dfrac{1}{137}\) ⇒ <span class="box">\(v_1 = \dfrac{c}{137} \approx 2.19\times10^{6}\) m s\(^{-1}\)</span></p>
<p class="step">(The ratio \(e^2/2\varepsilon_0hc\) is the fine-structure constant; in general \(v_n = \dfrac{c}{137\,n}\).)</p>""",
          afig=[(F.fig_q19_bohr, "Electron in a Bohr orbit")],
          topic=ATOM, recall=r"<ul><li>Centripetal force = Coulomb force.</li><li>\(mvr = nh/2\pi\).</li><li>\(v_n \propto 1/n\), \(r_n \propto n^2\).</li></ul>"),
        Q("19(b)(i)", 3, r"""<p>(OR) Sketch a graph showing the variation of binding energy per nucleon of a nucleus with mass number.
Indicate which regions of this graph shows stable, nuclear fission prone and nuclear fusion prone nuclei.</p>""",
          a=r"""{{fig:0}}
<p class="step">BE/A rises steeply for light nuclei (with peaks at \(^4\)He, \(^{12}\)C, \(^{16}\)O), reaches a broad
maximum of about 8.8 MeV near A ≈ 56 (Fe), then falls slowly to about 7.6 MeV for A ≈ 238.</p>
<p class="step"><b>Stable:</b> the flat top, A ≈ 40 to 120 (highest BE/A, most tightly bound).<br>
<b>Fusion-prone:</b> light nuclei, A ≲ 20–30 — joining two of them gives a nucleus of higher BE/A, releasing energy.<br>
<b>Fission-prone:</b> heavy nuclei, A ≳ 170 (e.g. U-235) — splitting into two middle nuclei raises BE/A, releasing
energy.</p>""",
          afig=[(F.fig_q19_bea, "Binding energy per nucleon against mass number")],
          topic=NUC, recall=r"<ul><li>BE = Δm c²; BE/A measures stability.</li><li>Energy released whenever products have higher BE/A.</li></ul>"),
        Q("19(b)(ii)", 2, r"""<p>Calculate the energy released in the following nuclear reaction.</p>
<p>\({}_1^2\mathrm H + {}_1^2\mathrm H \rightarrow {}_2^4\mathrm{He} + \text{energy}\)</p>
<p>Mass of \({}_1^2\mathrm H = 2.014102\) u<br>Mass of \({}_2^4\mathrm{He} = 4.002604\) u</p>
<p class="note">[The paper labels the helium mass "\(^4\)He\(_1\)"; the atomic number of helium is 2.]</p>""",
          a=r"""<p class="step">Mass defect \(\Delta m = 2\times2.014102 - 4.002604 = 4.028204 - 4.002604 = 0.025600\) u</p>
<p class="step">\(Q = \Delta m\times931.5\ \text{MeV/u} = 0.0256\times931.5\)</p>
<p class="step"><span class="box">\(Q \approx 23.8\) MeV</span> \((\approx 3.8\times10^{-12}\) J)</p>""",
          topic=NUC, recall=r"<ul><li>\(Q = (\sum m_{\text{reactants}} - \sum m_{\text{products}})c^2\).</li><li>1 u ≡ 931.5 MeV.</li></ul>"),
        Q("20", 5, r"""<p>A rectifier is an electronic circuit that converts alternating current (AC) into direct current (DC). There
are two main types of rectifiers — half-wave and full-wave.</p>
<p>In a half-wave rectifier, only one half of the input AC signal (either positive or negative) is allowed to pass
through the circuit, while the other half is blocked. It uses a single diode and produces an output that is pulsating
DC. However, since only half of the input wave is utilized, its efficiency is low, and the output is not smooth.</p>
<p>In a full-wave rectifier, both halves of the AC input are used to produce DC. This can be done using either two
diodes with a center-tapped transformer or four diodes in a bridge arrangement. The output of a full-wave rectifier is
smoother and has higher efficiency compared to a half-wave rectifier. Therefore, full-wave rectifiers are more commonly
used in power supply circuits.</p>
<p>a) State how the thickness of depletion region changes forward and reverse biasing a p-n junction.</p>
<p>b) Draw a neat, labelled diagram of a full wave rectifier.</p>
<p>c) Show the input and output signals in it.</p>""",
          a=r"""<p><b>(a)</b> <b>Forward bias:</b> the applied field opposes the barrier field; majority carriers are pushed
towards the junction, so the depletion region becomes <b>thinner</b> (barrier lowered).
<b>Reverse bias:</b> the applied field adds to the barrier field; carriers are drawn away from the junction, so the
depletion region becomes <b>wider</b> (barrier raised).</p>
<p><b>(b)</b> Centre-tap full-wave rectifier (the form in the ISC syllabus; the bridge is not required): {{fig:0}}</p>
<p class="step">During the half-cycle when S<sub>1</sub> is positive with respect to the centre tap T, D<sub>1</sub>
is forward biased and conducts, D<sub>2</sub> is reverse biased; current flows S<sub>1</sub> → D<sub>1</sub> → P →
R<sub>L</sub> → T. In the next half-cycle S<sub>2</sub> is positive, D<sub>2</sub> conducts and D<sub>1</sub> is off;
current again flows P → R<sub>L</sub> → T. So the current through R<sub>L</sub> is in the same direction in both
halves.</p>
<p><b>(c)</b> {{fig:1}}</p>
<p class="step">The output is unidirectional (pulsating DC) with one positive pulse for every half-cycle of the input:
its frequency is twice the input frequency.</p>""",
          afig=[(F.fig_q20_fwr, "Full-wave rectifier with a centre-tapped transformer"),
                (F.fig_q20_waves, "Input and output waveforms")],
          topic=ELEC, recall=r"<ul><li>Forward bias narrows, reverse bias widens the depletion layer.</li><li>Centre-tap FWR: two diodes conduct on alternate half-cycles; output ripple frequency = 2f.</li></ul>"),
    ])
