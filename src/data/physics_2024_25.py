"""Heritage School Pre-Board 2024-25, Physics Paper 1 (Theory) — digital copy, ISC 2027 filter, solutions.
Source of record: the Word file (PreBoard-PYQ/2024-25/SET-1/Physics.docx); transcribed from its rendered pages
(LibreOffice PDF, 7 pages) with every embedded image checked at full resolution."""
from kit import Q, SEC
import physics_2024_25_figs as F

ES, CE, MAG = "Electrostatics", "Current Electricity", "Magnetic Effects of Current and Magnetism"
EMI, EMW = "Electromagnetic Induction and Alternating Currents", "Electromagnetic Waves"
RAY, WAVE = "Optics — Ray Optics and Optical Instruments", "Optics — Wave Optics"
DUAL, ATOM, NUC, ELEC = ("Dual Nature of Radiation and Matter", "Atoms and Nuclei — Atoms",
                         "Atoms and Nuclei — Nuclei", "Electronic Devices")

AR_OPTS = r"""<p>a) Both assertion and reason are true and reason is the correct explanation for assertion.<br>
b) Both assertion and reason are true and reason is not the correct explanation for assertion.<br>
c) Assertion is true but the reason is false.<br>
d) Assertion is false but the reason is true.</p>"""

PAPER = dict(
    subject="physics", year="2024-25", slug="2024-25", paper="Paper I (Theory)",
    source="PreBoard-PYQ/2024-25/SET-1/Physics.docx", marks=70, time="Three hours",
    intro=r"""<p><i>(Candidates are allowed <b>an additional 15 minutes</b> for <b>only</b> reading the paper. They must
<b>NOT</b> start writing during this time).</i></p>
<p><i>This paper is divided into <b>four</b> sections – <b>A</b>, <b>B</b>, <b>C</b> and <b>D</b>. Answer <b>all</b>
questions. <b>Section A</b> consists of <b>one</b> question <b>having sub-parts</b> of <b>one</b> mark each.
<b>Section B</b> consists of <b>seven</b> questions of <b>two</b> marks each. <b>Section C</b> consists of
<b>nine</b> questions of <b>three</b> marks each, and <b>Section D</b> consists of <b>three</b> questions of
<b>five</b> marks each. <b>Internal choices have been provided in two questions each in Section B, Section C and
Section D.</b> The intended marks for questions are given in brackets [ ]. All working, including rough work, should be
done on the same sheet as and adjacent to the rest of the answer. Answers to sub-parts of the same question must be
given in one place only. A list of useful physical constants is given at the end of this paper. A simple scientific
calculator without a programmable memory may be used for calculations.</i></p>
<p><b>Useful Constants &amp; Relations</b> (as printed): charge of a proton \(e = 1.6\times10^{-19}\) C; Planck's
constant \(h = 6.6\times10^{-34}\) J s; mass of an electron \(m_e = 9.1\times10^{-31}\) kg; permittivity of vacuum
\(\varepsilon_0 = 8.85\times10^{-12}\) F m\(^{-1}\); Coulomb's constant \(\dfrac{1}{4\pi\varepsilon_0} = 9\times10^{9}\)
N m\(^2\) C\(^{-2}\); Rydberg's constant \(R = 1.097\times10^{7}\) m\(^{-1}\); speed of light in vacuum
\(c = 3\times10^{8}\) m s\(^{-1}\); permeability of vacuum \(\mu_0 = 4\pi\times10^{-7}\) H m\(^{-1}\).</p>
<p>[This question paper consists of 6 printed pages]</p>""",
    items=[
        SEC("Section A — 14 marks", "Question 1. A. Choose the correct alternative: [1×7]"),
        Q("1(A)(i)", 1, r"""<p>Three small charged spheres X, Y and Z carrying charges + q, -q and + q respectively are placed equidistant
from each other, as shown in the figure. The spheres Y and Z are held in place. Initially, X was also held in place but
was otherwise free to move. When X is released, the path followed by it will be towards:</p>{{fig:0}}
<p>a) A &nbsp; b) B &nbsp; c) C &nbsp; d) D</p>""",
          qfig=[(F.fig_q1a1_charges, "X, Y and Z at the corners of an equilateral triangle (redrawn; charges from the text)")],
          a=r"""<p><b>b) B</b></p>
<p class="step">X is at the same distance r from Y and from Z, so the two forces on it have the same magnitude
\(F = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q^2}{r^2}\).</p>
<p class="step">Y (−q) <b>attracts</b> X along XY (down and to the left, 60° below the line XA); Z (+q) <b>repels</b> X
along ZX produced (up and to the left, 60° above XA). The vertical components (\(F\sin60^\circ\)) cancel and the
horizontal ones add: the <b>initial</b> force is \(F_{\text{net}} = 2F\cos60^\circ = F\), parallel to YZ, along XA. {{fig:0}}</p>
<p class="step">X starts from rest, so it begins to move along XA — but the force does not stay along XA. As soon as X
has moved to the left it is <b>nearer to Y</b> and <b>farther from Z</b>: the attraction towards Y (which points
downwards) grows, the repulsion from Z (which points upwards) weakens, and a net downward force appears.</p>
<p class="step">So the path starts along XA and curves downwards, towards Y — the curved path <b>B</b>. (Path A, a straight
line, would need the force to stay along XA throughout, which it does not.) {{fig:1}}</p>""",
          afig=[(F.fig_a1a1_forces, "At the start: equal forces F_XY (attraction) and F_XZ (repulsion) give a resultant along XA"),
                (F.fig_a1a1_path, "The path computed numerically: it leaves along XA and bends down towards Y (path B)")],
          topic=ES, recall=r"<ul><li>Coulomb's law: like charges repel, unlike attract; \(F \propto q_1q_2/r^2\).</li><li>Superposition: add the forces as vectors (resolve and add components).</li><li>A charge released from rest starts off along the net force; its path is straight only if the force keeps that direction.</li></ul>"),
        Q("1(A)(ii)", 1, r"""<p>If the ammeter reading in the given circuit is zero, find the value of the resistance R.</p>{{fig:0}}
<p>a) 50 Ω &nbsp; b) 100 Ω &nbsp; c) 150 Ω &nbsp; d) 200 Ω</p>""",
          qfig=[(F.fig_q1a2_bridge, "Circuit as printed (long plate = + terminal)")],
          a=r"""<p><b>c) 150 Ω</b></p>
<p class="step">No current flows in the branch A–ammeter–D–4 V cell–C, so there is no drop across the ammeter and the
4 V cell is on open circuit: \(V_A - V_C = 4\) V (the + terminal of the 4 V cell is at D, which is at the potential
of A).</p>
<p class="step">The 10 V cell then drives a single current I round the loop A → 100 Ω → C → R → B → A:
\(I = \dfrac{10}{100 + R}\). {{fig:0}}</p>
<p class="step">The p.d. across the 100 Ω resistor must equal 4 V: \(I\times100 = 4 \Rightarrow I = 0.04\) A.</p>
<p class="step">\(100 + R = \dfrac{10}{0.04} = 250\ \Omega\) ⇒ <span class="box">\(R = 150\ \Omega\)</span></p>""",
          afig=[(F.fig_a1a2_bridge, "With I = 0 in A–D–C, the 10 V cell drives I through 100 Ω and R in series")],
          topic=CE, recall=r"<ul><li>Zero current through a cell ⇒ p.d. across it = its emf.</li><li>Kirchhoff's loop law: sum of emfs = sum of IR drops round a loop.</li></ul>"),
        Q("1(A)(iii)", 1, r"""<p>Four cells E<sub>1</sub>, E<sub>2</sub>, E<sub>3</sub> and E<sub>4</sub> are connected as shown in the figure.
E.M.F of the battery so formed is</p>{{fig:0}}
<p>a) 6 V &nbsp; b) 12 V &nbsp; c) 4V &nbsp; d) zero</p>""",
          qfig=[(F.fig_q1a3_cells, "Cells as printed (long plate = + terminal, all facing the + end)")],
          a=r"""<p><b>a) 6 V</b></p>
<p class="step">Upper branch: E<sub>1</sub>, E<sub>2</sub>, E<sub>3</sub> in series, all with the + terminal towards
the left, so their emfs add: 2 + 2 + 2 = 6 V.</p>
<p class="step">Lower branch: E<sub>4</sub> = 6 V, also with + towards the left. Two sources of equal emf (6 V) in
parallel, + to +, give a combination of emf <span class="box">6 V</span> (no current circulates between them when no
external current is drawn).</p>""",
          topic=CE, recall=r"<ul><li>Cells in series (same sense): emfs add.</li><li>Equal emfs in parallel: emf of the combination = that emf (only the internal resistance changes).</li></ul>"),
        Q("1(A)(iv)", 1, r"""<p>Two statements are given below. One is <b>Assertion (A)</b> and the other is <b>Reason (R)</b>. Read the
statements carefully and choose the option that correctly describes statements A and R.</p>
<p><b>Assertion (A):</b> The kinetic energy of a charged particle describing a circular path in a uniform magnetic field
does NOT remain constant with time.</p>
<p><b>Reason (R):</b> The velocity of a charged particle moving in a circular path in a uniform magnetic field changes
with time.</p>""" + AR_OPTS,
          a=r"""<p><b>d) Assertion is false but the reason is true.</b></p>
<p class="step">The magnetic force \(\vec F = q(\vec v\times\vec B)\) is always perpendicular to \(\vec v\), so it does
no work: the speed, and hence the kinetic energy, stays <b>constant</b> — the Assertion is false.</p>
<p class="step">The force continually changes the <b>direction</b> of motion, so the velocity (a vector) does change
with time — the Reason is true.</p>""",
          topic=MAG, recall=r"<ul><li>\(\vec F = q\vec v\times\vec B\) ⊥ \(\vec v\) ⇒ work done = 0, speed constant.</li><li>Radius \(r = mv/qB\).</li></ul>"),
        Q("1(A)(v)", 1, r"""<p>Lorenz's force is</p>
<p>a) the vector sum of electrostatic and magnetic force acting on a moving charged particle.<br>
b) the sum of electrostatic and magnetic force acting on a moving charged particle.<br>
c) electrostatic force acting only on a charged particle.<br>
d) the magnetic force acts only on a moving charged particle.</p>""",
          a=r"""<p><b>a) the vector sum of electrostatic and magnetic force acting on a moving charged particle.</b></p>
<p class="step">\(\vec F = q\vec E + q(\vec v\times\vec B)\): the electric and magnetic forces are in general in
different directions, so they add as vectors.</p>""",
          topic=MAG, recall=r"<ul><li>Lorentz force \(\vec F = q(\vec E + \vec v\times\vec B)\).</li></ul>"),
        Q("1(A)(vi)", 1, r"""<p>An alternating current (a.c.) voltage source at 50 Hz is applied to a series combination of resistor A of
resistance ‘P’ and component B of reactance ‘Y’. The phase angle is + π/4. Which of the following is true?</p>
<p>a) B is a capacitor and Y = 2P. &nbsp; b) B is an inductor and Y = 2P.<br>
c) B is a capacitor and Y = P. &nbsp; d) B is an inductor and Y = P.</p>""",
          a=r"""<p><b>d) B is an inductor and Y = P.</b></p>
<p class="step">For a series R–X circuit \(\tan\varphi = \dfrac{X}{R}\); \(\varphi = \pi/4\) ⇒ \(\tan\varphi = 1\) ⇒
\(Y = P\).</p>
<p class="step">The phase angle φ (of the voltage relative to the current) is <b>positive</b>, i.e. the voltage leads
the current — the behaviour of an <b>inductive</b> circuit (\(\tan\varphi = (X_L - X_C)/R \gt 0\)). So B is an
inductor.</p>
<p class="note">[The phase angle of a circuit is, by the ISC convention, the angle by which the applied voltage leads the
current (\(V = V_0\sin\omega t\), \(I = I_0\sin(\omega t - \varphi)\)). Read the other way round — current leading by
π/4 — the answer would be (c).]</p>""",
          topic=EMI, recall=r"<ul><li>\(\tan\varphi = (X_L - X_C)/R\); φ &gt; 0: voltage leads (inductive), φ &lt; 0: current leads (capacitive).</li></ul>"),
        Q("1(A)(vii)", 1, r"""<p><b>ASSERTION:</b> A photon is different from a normal particle.<br>
<b>REASON 1:</b> The energy of the photon in motion is purely kinetic as it has no rest energy.<br>
<b>REASON 2:</b> A photon travels with the speed of light in a vacuum.<br>
<b>REASON 3:</b> The energy of the photon at rest becomes purely potential as its rest mass is zero.</p>
<p>Select the correct option.</p>
<p>a) Assertion is correct. Only reason 3 is correct.<br>
b) Assertion is incorrect. Only Reason 2 is correct.<br>
c) Assertion is correct. Only reasons 1 and 2 are correct.<br>
d) Assertion is incorrect. Only Reasons 1 &amp; 3 are correct.</p>""",
          a=r"""<p><b>c) Assertion is correct. Only reasons 1 and 2 are correct.</b></p>
<p class="step">A photon has zero rest mass, so it has no rest energy (\(m_0c^2 = 0\)); all its energy
\(E = h\nu = pc\) is energy of motion — Reason 1 is correct. It always moves at c in vacuum — Reason 2 is correct.
These make it unlike a material particle — the Assertion is correct.</p>
<p class="step">A photon is never at rest, so it cannot have "energy at rest" of any kind — Reason 3 is wrong.</p>""",
          topic=DUAL, recall=r"<ul><li>Photon: rest mass 0, speed c, \(E = h\nu\), \(p = h/\lambda = E/c\).</li></ul>"),

        SEC("Question 1 B — Answer the following question in brief. [1×7]"),
        Q("1(B)(i)", 1, r"""<p>A blue-coloured alternate band of diffraction pattern appears on a screen due to the blue light of wavelength
λ passing through a single slit of width ω. If the blue light is replaced with a green light of wavelength 1.5 λ, to
what width should you change the slit to get the original pattern back?</p>""",
          a=r"""<p class="step">The pattern is fixed by the positions of the minima: \(\omega\sin\theta_n = n\lambda\), i.e.
\(\sin\theta_n = n\lambda/\omega\). To keep \(\theta_n\) unchanged with \(\lambda' = 1.5\lambda\), \(\lambda/\omega\) must
stay constant.</p>
<p class="step">\(\omega' = \omega\times\dfrac{1.5\lambda}{\lambda}\) ⇒ <span class="box">\(\omega' = 1.5\,\omega\)</span>
(the slit must be widened 1.5 times).</p>""",
          topic=WAVE, recall=r"<ul><li>Single slit minima: \(a\sin\theta = n\lambda\).</li><li>Angular width of central maximum \(2\lambda/a\).</li></ul>"),
        Q("1(B)(ii)", 1, r"""<p>How is the refractive index of a prism's material dependent on the angle of deviation and angle of prism in
minimum deviation conditions?</p>""",
          a=r"""<p class="step">At minimum deviation \(\delta_m\) the ray passes symmetrically (\(r_1 = r_2 = A/2\),
\(i = e = (A + \delta_m)/2\)), and</p>
<p class="step"><span class="box">\(\mu = \dfrac{\sin\left(\dfrac{A + \delta_m}{2}\right)}{\sin\left(\dfrac{A}{2}\right)}\)</span>
where A is the angle of the prism and \(\delta_m\) the angle of minimum deviation.</p>""",
          topic=RAY, recall=r"<ul><li>Prism: \(r_1 + r_2 = A\), \(\delta = i + e - A\).</li><li>At \(\delta_m\): \(i = e\), \(r_1 = r_2 = A/2\).</li></ul>"),
        Q("1(B)(iii)", 1, r"""<p>An electron is revolving around the nucleus of a hydrogen atom. If the radius of the first orbit is
\(0.53\times10^{-10}\) m, calculate the de Broglie wavelength of the moving electron in the orbit.</p>""",
          a=r"""<p class="step">Bohr's condition \(mvr = \dfrac{nh}{2\pi}\) with \(\lambda = \dfrac{h}{mv}\) gives
\(2\pi r = n\lambda\): the orbit holds a whole number of de Broglie wavelengths. For n = 1:</p>
<p class="step">\(\lambda = 2\pi r_1 = 2\times3.14\times0.53\times10^{-10}\)
⇒ <span class="box">\(\lambda = 3.33\times10^{-10}\) m</span></p>""",
          topic=ATOM, recall=r"<ul><li>\(mvr = nh/2\pi\) ⇔ \(2\pi r = n\lambda\) (standing wave round the orbit).</li><li>\(\lambda = h/mv\).</li></ul>"),
        Q("1(B)(iv)", 1, r"""<p>Ultra-violet light is incident on a zinc surface and photoelectrons are emitted. The graph shows how the
stopping potential \(V_S\) varies with frequency \(f\). How to determine Plank's constant from the graph?</p>{{fig:0}}""",
          qfig=[(F.fig_q1b4_vsf, "Graph as printed")],
          a=r"""<p class="step">Einstein's equation: \(eV_S = hf - \phi_0\) ⇒ \(V_S = \left(\dfrac{h}{e}\right)f - \dfrac{\phi_0}{e}\),
a straight line of slope \(h/e\).</p>
<p class="step">So find the <b>slope</b> of the line (\(\Delta V_S/\Delta f\)) and multiply by the electronic charge:
<span class="box">\(h = e\times\text{slope} = e\,\dfrac{\Delta V_S}{\Delta f}\)</span> {{fig:0}}</p>""",
          afig=[(F.fig_a1b4_vsf, "Slope = h/e; intercepts f₀ (threshold) and −φ₀/e")],
          topic=DUAL, recall=r"<ul><li>\(eV_S = hf - \phi_0\); \(\phi_0 = hf_0\).</li><li>Slope of \(V_S\)–\(f\) graph is \(h/e\) for every metal.</li></ul>"),
        Q("1(B)(v)", 1, r"""<p>What type of impurity is added to obtain an n-type semiconductor?</p>""",
          a=r"""<p class="step">A <b>pentavalent</b> (donor) impurity — an element of group 15 such as phosphorus, arsenic or
antimony — added to pure Si or Ge.</p>""",
          topic=ELEC, recall=r"<ul><li>n-type: pentavalent donor; majority carriers electrons.</li><li>p-type: trivalent acceptor (B, Al, In); majority carriers holes.</li></ul>"),
        Q("1(B)(vi)", 1, r"""<p>Define depletion region.</p>""",
          a=r"""<p class="step">The <b>depletion region</b> is the thin layer on either side of a p-n junction which is
<b>depleted of free charge carriers</b> (electrons and holes), containing only the immobile ions — positive donor ions on
the n-side and negative acceptor ions on the p-side — formed by diffusion of carriers across the junction and
recombination. The electric field of these ions sets up the potential barrier.</p>""",
          topic=ELEC, recall=r"<ul><li>Diffusion of majority carriers → recombination → uncovered immobile ions.</li><li>Forward bias narrows it; reverse bias widens it.</li></ul>"),
        Q("1(B)(vii)", 1, r"""<p>A parallel plate capacitor of capacitance C is charged to a potential V by a battery. Q is the charge stored in
the capacitor. The battery is then disconnected and the distance between the plates of the capacitor is increased by a
small amount. What changes will occur in its capacitance? Will it increase, decrease or remain the same? Explain.</p>""",
          a=r"""<p class="step">The capacitance <b>decreases</b>: \(C = \dfrac{\varepsilon_0A}{d}\), so a larger plate
separation d gives a smaller C.</p>
<p class="step">(With the battery disconnected the charge Q stays the same, so \(V = Q/C\) increases.)</p>""",
          topic=ES, recall=r"<ul><li>\(C = \varepsilon_0A/d\).</li><li>Battery disconnected ⇒ Q constant; connected ⇒ V constant.</li></ul>"),

        SEC("Section B — 14 marks"),
        Q("2", 2, r"""<p>Young’s double-slit experiment is first performed in air and then in a medium other than air. It is found that
the 8<sup>th</sup> bright fringe in the medium lies with the 5<sup>th</sup> dark fringe in the air. Find the refractive
index of the medium.</p>""",
          a=r"""<p class="step">In a medium of refractive index μ the wavelength becomes \(\lambda/\mu\), so the n-th bright fringe
is at \(y_n = \dfrac{n\lambda D}{\mu d}\).</p>
<p class="step">The n-th dark fringe in air is at \(y = \dfrac{(2n-1)\lambda D}{2d}\); for n = 5:
\(y = \dfrac{9\lambda D}{2d} = 4.5\,\dfrac{\lambda D}{d}\).</p>
<p class="step">Equating: \(\dfrac{8\lambda D}{\mu d} = \dfrac{4.5\lambda D}{d}\) ⇒ \(\mu = \dfrac{8}{4.5} = \dfrac{16}{9}\)</p>
<p class="step"><span class="box">\(\mu \approx 1.78\)</span></p>""",
          topic=WAVE, recall=r"<ul><li>Bright: \(y_n = n\lambda D/d\); dark: \(y_n = (2n-1)\lambda D/2d\).</li><li>In a medium \(\lambda_m = \lambda/\mu\), so fringes shrink by μ.</li></ul>"),
        Q("3(a)", 2, r"""<p>a) A current-carrying solenoid of 50 turns/cm carries a current of 2 A. Find the intensity of magnetic field B at the
centre of the solenoid.</p>""",
          a=r"""<p class="step">\(n = 50\) turns/cm \(= 5000\) turns m\(^{-1}\).</p>
<p class="step">\(B = \mu_0 nI = 4\pi\times10^{-7}\times5000\times2\)</p>
<p class="step"><span class="box">\(B = 1.26\times10^{-2}\) T</span> (along the axis)</p>""",
          topic=MAG, recall=r"<ul><li>Long solenoid: \(B = \mu_0 nI\) inside (n = turns per metre).</li><li>Convert turns/cm to turns/m (×100).</li></ul>"),
        Q("3(b)", 2, r"""<p>(OR) b) Draw a labelled graph showing the variation of X<sub>L</sub> and X<sub>C</sub> with the frequency of the
alternating voltage source.</p>""",
          a=r"""<p class="step">\(X_L = 2\pi fL \propto f\): a straight line through the origin.</p>
<p class="step">\(X_C = \dfrac{1}{2\pi fC} \propto \dfrac1f\): a rectangular hyperbola, very large at low frequency (infinite
for d.c.) and tending to zero at high frequency. {{fig:0}}</p>
<p class="step">The two curves cross at the resonant frequency \(f_0 = \dfrac{1}{2\pi\sqrt{LC}}\), where \(X_L = X_C\).</p>""",
          afig=[(F.fig_a3b_xlxc, "X_L ∝ f (line through origin); X_C ∝ 1/f (hyperbola)")],
          topic=EMI, recall=r"<ul><li>\(X_L = \omega L\), \(X_C = 1/\omega C\), \(\omega = 2\pi f\).</li><li>An inductor blocks high f; a capacitor blocks low f (and d.c.).</li></ul>"),
        Q("4", 2, r"""<p>Name the EM wave which is suitable for radar systems used in aircraft navigation. Write the frequency range of this
wave.</p>""",
          a=r"""<p class="step"><b>Microwaves.</b> (Their short wavelength gives a narrow, well-directed beam that reflects
well from aircraft.)</p>
<p class="step">Frequency range: about <span class="box">\(10^{9}\) Hz to \(3\times10^{11}\) Hz</span> (1 GHz – 300 GHz;
wavelength about 30 cm to 1 mm).</p>""",
          topic=EMW, recall=r"<ul><li>Order of increasing f: radio, microwave, IR, visible, UV, X-rays, γ-rays.</li><li>\(c = f\lambda\).</li></ul>"),
        Q("5(a)", 2, r"""<p>a) A thin convex lens of focal length f is cut into parts and then combined as shown in Fig 1 and Fig 2. Evaluate the
focal length of the combination, in:<br>(i) figure 1<br>(ii) figure 2</p>{{fig:0}}""",
          qfig=[(F.fig_q5_parts, "As printed: the lens is cut along its principal axis (dashed)")],
          a=r"""<p class="step">Cutting a lens <b>along its principal axis</b> into an upper and a lower half does not change the
curvature of either surface, so by the lens maker's formula \(\dfrac1f = (\mu - 1)\left(\dfrac1{R_1} - \dfrac1{R_2}\right)\)
<b>each half still has focal length f</b> (only the aperture, hence the brightness, is halved).</p>
<p class="step">(i) Fig 1: the two halves are placed one behind the other, in contact — two thin lenses of focal length
f in contact: \(\dfrac1F = \dfrac1f + \dfrac1f = \dfrac2f\) ⇒ <span class="box">\(F = f/2\)</span></p>
<p class="step">(ii) Fig 2: an upper half and a lower half, again in contact: \(\dfrac1F = \dfrac1f + \dfrac1f\) ⇒
<span class="box">\(F = f/2\)</span> {{fig:0}}</p>
<p class="step">In Fig 2 the two halves are not coaxial — the flat (axis) edge of one is displaced from that of the other.
This does not change the focal length of thin lenses in contact: for a ray at height y the deviations
\((y - a_1)/f\) and \((y - a_2)/f\) add to \(\left(y - \tfrac{a_1 + a_2}{2}\right)\dfrac{2}{f}\), a single lens of focal
length f/2 whose axis lies midway between the two.</p>""",
          afig=[(F.fig_a5a_parts, "Each half-lens has focal length f; in contact, powers add")],
          topic=RAY, recall=r"<ul><li>Lens maker: f depends only on μ, R₁, R₂ — not on the aperture.</li><li>Thin lenses in contact: \(1/F = 1/f_1 + 1/f_2\), \(P = P_1 + P_2\).</li><li>(Cutting perpendicular to the axis gives two plano-convex lenses of focal length 2f.)</li></ul>"),
        Q("5(b)", 2, r"""<p>(OR) b) An object placed at a distance of x from the first focus of a convex lens forms a real image at a distance of y
from its second focus. Show that the product xy is equal to the square of the focal length f of the lens.</p>""",
          a=r"""<p class="step">Cartesian convention, distances from the optical centre O, light travelling left to right.
The object is at \(u = -(f + x)\) and the real image at \(v = +(f + y)\). {{fig:0}}</p>
<p class="step">Lens formula: \(\dfrac1v - \dfrac1u = \dfrac1f\) ⇒ \(\dfrac{1}{f + y} + \dfrac{1}{f + x} = \dfrac1f\)</p>
<p class="step">\(f(f + x) + f(f + y) = (f + x)(f + y)\)</p>
<p class="step">\(2f^2 + fx + fy = f^2 + fx + fy + xy\)</p>
<p class="step"><span class="box">\(xy = f^2\)</span> (Newton's formula)</p>""",
          afig=[(F.fig_a5b_newton, "Drawn to scale with f = 10, x = 5, y = 20 (xy = 100 = f²)")],
          topic=RAY, recall=r"<ul><li>Lens formula \(1/v - 1/u = 1/f\) with u negative for a real object.</li><li>Measure x from F₁ and y from F₂.</li></ul>"),
        Q("6", 2, r"""<p>A light ray entering a right-angled prism undergoes refraction at the face AC as shown in the figure. What is the
refractive index of the prism in the figure?</p>{{fig:0}}""",
          qfig=[(F.fig_q6_prism, "As printed: ∠B = 90°, ∠C = 45°; the ray leaves along AC")],
          a=r"""<p class="step">The ray strikes AB normally, so it goes straight through, parallel to BC.</p>
<p class="step">∠A = 180° − 90° − 45° = 45°. The ray (parallel to BC) meets AC at 45° to the surface, so the angle of
incidence on AC (from the normal) is \(i = 45^\circ\). {{fig:0}}</p>
<p class="step">The emergent ray grazes along AC: angle of refraction \(e = 90^\circ\). So 45° is the
<b>critical angle</b>: \(\mu\sin45^\circ = \sin90^\circ\).</p>
<p class="step">\(\mu = \dfrac{1}{\sin45^\circ}\) ⇒ <span class="box">\(\mu = \sqrt2 \approx 1.41\)</span></p>""",
          afig=[(F.fig_a6_prism, "At AC: i = 45°, emergent ray at 90° (grazing) ⇒ C = 45°")],
          topic=RAY, recall=r"<ul><li>Normal incidence: no bending.</li><li>Grazing emergence ⇒ angle of incidence = critical angle; \(\mu = 1/\sin C\).</li></ul>"),
        Q("7", 2, r"""<p>A photoelectric emission apparatus with an unknown metal is irradiated with 200 nm light. The photocurrent becomes
zero as the collector plate potential of –0.80 V. Determine the work function of the unknown metal.</p>""",
          a=r"""<p class="step">Photon energy \(E = \dfrac{hc}{\lambda} = \dfrac{6.6\times10^{-34}\times3\times10^{8}}{200\times10^{-9}}
= 9.9\times10^{-19}\) J \(= \dfrac{9.9\times10^{-19}}{1.6\times10^{-19}} = 6.19\) eV</p>
<p class="step">Stopping potential \(V_0 = 0.80\) V ⇒ \(K_{\max} = eV_0 = 0.80\) eV.</p>
<p class="step">\(\phi_0 = E - eV_0 = 6.19 - 0.80\) ⇒ <span class="box">\(\phi_0 \approx 5.39\) eV \((= 8.6\times10^{-19}\) J)</span></p>""",
          topic=DUAL, recall=r"<ul><li>\(hc/\lambda = \phi_0 + eV_0\).</li><li>1 eV = \(1.6\times10^{-19}\) J; \(hc \approx 1240\) eV nm.</li></ul>"),
        Q("8", 2, r"""<p>State two necessary conditions for nuclear fusion.</p>""",
          a=r"""<ul><li><b>Very high temperature</b> (of the order of \(10^{7}\) K): the light nuclei must have enough kinetic energy
to overcome their electrostatic (Coulomb) repulsion and come within the short range (~fm) of the nuclear force.</li>
<li><b>Very high pressure / density</b> of the fuel, held (confined) for long enough, so that collisions between nuclei
are frequent and the reaction is self-sustaining.</li></ul>""",
          topic=NUC, recall=r"<ul><li>Fusion: light nuclei combine (e.g. \(4\,{}^{1}_{1}\mathrm{H}\rightarrow{}^{4}_{2}\mathrm{He}\)), releasing energy because BE/A increases.</li><li>Thermonuclear: needs ~\(10^7\) K (as in the sun).</li></ul>"),

        SEC("Section C — 27 marks"),
        Q("9", 3, r"""<p>Derive an expression for a combined capacitance of two capacitors C<sub>1</sub> and C<sub>2</sub> connected in
parallel. Draw the diagram necessary for the derivation.</p>""",
          a=r"""<p class="step">C<sub>1</sub> and C<sub>2</sub> are connected between the same two points A and B, across a source
of p.d. V. {{fig:0}}</p>
<p class="step">The p.d. across <b>each</b> capacitor is the same, V. Their charges are
\(Q_1 = C_1V\) and \(Q_2 = C_2V\).</p>
<p class="step">The total charge drawn from the source is \(Q = Q_1 + Q_2 = C_1V + C_2V = (C_1 + C_2)V\).</p>
<p class="step">If a single capacitor C stores the same charge Q at the same p.d. V, \(Q = CV\). Hence
\(CV = (C_1 + C_2)V\) ⇒ <span class="box">\(C = C_1 + C_2\)</span></p>""",
          afig=[(F.fig_a9_parallel, "Two capacitors in parallel across a p.d. V")],
          topic=ES, recall=r"<ul><li>Parallel: same V, charges add ⇒ \(C = C_1 + C_2\).</li><li>Series: same Q, p.d.s add ⇒ \(1/C = 1/C_1 + 1/C_2\).</li></ul>"),
        Q("10", 3, r"""<p>A student starts working on a problem on Gauss' theorem to calculate the flux and hence the electric field at a
given point due to a system of discreet charges. The teacher gives him certain instructions and the student responds to
each instruction as per her understanding of the concept. State whether the student's response is correct or incorrect.
Give a reason for your answer.</p>
<p>(a) <b>Examiner:</b> Draw a Gaussian surface for the given system of charges.<br>
<b>Student:</b> Draws a symmetric surface passing through the point at which the electric field is to be calculated.</p>
<p>(b) <b>Examiner:</b> Suggest a way to double the flux through the given surface.<br>
<b>Student:</b> Doubles the surface area of the Gaussian surface.</p>
<p>(c) <b>Examiner:</b> Calculate the electric flux of a point charge of 2 μC, placed 5 cm above the centre of a square
plate of side 10 cm, through the given plate.<br>
<b>Student:</b> As the charge is not enclosed by the surface, the flux through the surface is zero.</p>""",
          a=r"""<p class="step">(a) <b>Correct.</b> A Gaussian surface is an imaginary <b>closed</b> surface around the charges,
chosen through the point where E is wanted, and symmetric so that E has the same magnitude over it and
\(\oint\vec E\cdot d\vec A\) becomes \(E\times\text{area}\).</p>
<p class="step">(b) <b>Incorrect.</b> By Gauss's theorem \(\phi = q_{\text{enc}}/\varepsilon_0\): the flux depends only
on the charge enclosed, not on the size or area of the surface. To double the flux, the enclosed charge must be doubled.</p>
<p class="step">(c) <b>Incorrect.</b> The plate is an open surface, and field lines from the charge do pass through it.
Imagine a cube of side 10 cm with the charge at its centre (5 cm from each face); the plate is one of its six identical
faces, so it receives one-sixth of the total flux. {{fig:0}}</p>
<p class="step">\(\phi = \dfrac{1}{6}\dfrac{q}{\varepsilon_0} = \dfrac{2\times10^{-6}}{6\times8.85\times10^{-12}}\)
⇒ <span class="box">\(\phi \approx 3.77\times10^{4}\) N m\(^2\) C\(^{-1}\)</span></p>
<p class="note">[CISCE's competency booklet (Q68) prints this question; its key gives (a) correct, (b) incorrect,
(c) incorrect with \(\phi = \tfrac16\times2\times10^{-6}/\varepsilon_0 = 3.77\times10^4\) N m² C⁻¹, and notes that a
reason is needed for both correct and incorrect responses.]</p>""",
          afig=[(F.fig_a10_cube, "The plate as one face of a cube of side 10 cm centred on the charge")],
          topic=ES, recall=r"<ul><li>Gauss: \(\oint\vec E\cdot d\vec A = q_{\text{enc}}/\varepsilon_0\) for a closed surface.</li><li>Charge at the centre of a cube: each face gets \(q/6\varepsilon_0\).</li></ul>"),
        Q("11", 3, r"""<p>For the given electrical circuit, calculate the current through each branch using Kirchhoff's laws</p>{{fig:0}}""",
          qfig=[(F.fig_q11_circuit, "Circuit as printed (long plate = + terminal)")],
          a=r"""<p class="step">Label the junctions P (top) and Q (bottom). Branch currents: \(I_1\) from Q round the left loop
through the 3 V cell to P; \(I_2\) from P to Q through 2 Ω; \(I_3\) from P through 5 Ω, 3.5 Ω and the 2 V cell to Q.
{{fig:0}}</p>
<p class="step">The total resistance of the left branch is \(4 + 2 + 2.5 = 8.5\ \Omega\); of the right branch
\(5 + 3.5 + 0.5 = 9\ \Omega\). In the right branch the 2 V cell has its + terminal towards Q, so it also drives current
from P towards Q.</p>
<p class="step">Junction rule at P: \(I_1 = I_2 + I_3\) … (1)</p>
<p class="step">Loop rule, left mesh (Q → 3 V cell → P → 2 Ω → Q): \(3 = 8.5I_1 + 2I_2\) … (2)</p>
<p class="step">Loop rule, right mesh (P → 5 Ω → 3.5 Ω → 2 V cell → Q → 2 Ω → P): \(2 = 9I_3 - 2I_2\) … (3)</p>
<p class="step">From (1) and (2): \(3 = 8.5I_2 + 8.5I_3 + 2I_2 = 10.5I_2 + 8.5I_3\). From (3):
\(I_3 = \dfrac{2 + 2I_2}{9}\). Substituting: \(27 = 94.5I_2 + 17 + 17I_2\) ⇒ \(I_2 = \dfrac{10}{111.5} = 0.0897\) A.</p>
<p class="step">\(I_3 = \dfrac{2 + 0.179}{9} = 0.242\) A; \(I_1 = I_2 + I_3 = 0.332\) A.</p>
<p class="step"><span class="box">3 V branch (2.5 Ω, 4 Ω): 0.33 A; 2 Ω branch: 0.090 A (P to Q); 2 V branch (5 Ω, 3.5 Ω):
0.24 A (P to Q)</span></p>
<p class="step">Check (left mesh): \(8.5\times0.332 + 2\times0.0897 = 2.82 + 0.18 = 3.00\) V ✓</p>
<p class="note">[The polarities are read from the printed figure: the long plate of the 3 V cell is at the top, and the
long plate of the 2 V cell is at the lower (Q) end. If the 2 V cell were the other way round the currents would be
0.26 A, 0.39 A and 0.13 A.]</p>""",
          afig=[(F.fig_a11_circuit, "Branch currents I₁, I₂, I₃ and junctions P, Q")],
          topic=CE, recall=r"<ul><li>Junction rule: ΣI in = ΣI out (charge conservation).</li><li>Loop rule: Σε = ΣIR round any closed loop (energy conservation); include internal resistances.</li></ul>"),
        Q("12", 3, r"""<p>Using Ampere’s Circuital Law deduce the expression for the magnetic field at the centre of a circular coil.</p>""",
          a=r"""<p class="note">[Ampère's circuital law cannot give the field at the centre of a circular coil: there is no closed
path through the centre on which B is constant in magnitude and along the path, so \(\oint\vec B\cdot d\vec l\) cannot be
evaluated as \(B\times\) length. The ISC syllabus derives this result from the <b>Biot–Savart law</b>, which is what
an examiner will accept; it is done below.]</p>
<p class="step"><b>Biot–Savart law:</b> \(dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl\sin\theta}{r^2}\), where θ is the angle
between \(d\vec l\) and the line joining it to the point.</p>
<p class="step">Consider a circular coil of radius r carrying current I, and a small element \(d\vec l\) on it. The line
from \(d\vec l\) to the centre O is a radius, which is perpendicular to \(d\vec l\): \(\theta = 90^\circ\). {{fig:0}}</p>
<p class="step">\(dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl}{r^2}\), and by the right-hand rule every element gives dB in the
<b>same</b> direction — perpendicular to the plane of the coil — so the contributions add directly:</p>
<p class="step">\(B = \displaystyle\oint dB = \dfrac{\mu_0 I}{4\pi r^2}\oint dl = \dfrac{\mu_0I}{4\pi r^2}\times2\pi r\)
⇒ <span class="box">\(B = \dfrac{\mu_0I}{2r}\)</span>; for N turns \(B = \dfrac{\mu_0NI}{2r}\), along the axis.</p>""",
          afig=[(F.fig_a12_loop, "Element dl on the coil, r to the centre O; dB ⊥ plane of the coil")],
          topic=MAG, recall=r"<ul><li>Biot–Savart: \(d\vec B = \dfrac{\mu_0}{4\pi}\dfrac{I\,d\vec l\times\hat r}{r^2}\).</li><li>Ampère's law \(\oint\vec B\cdot d\vec l = \mu_0I\) is useful only with symmetry (long wire, solenoid).</li></ul>"),
        Q("13(a)", 3, r"""<p>(a) In a given LCR series AC circuit, the inductive and capacitive reactance are given as 400 Ω and 600 Ω
respectively. If resistance R in the circuit is 100 Ω and the maximum voltage of the supply is 100 V, then determine the
following</p>
<p>(a) the net impedance of the circuit.<br>(b) the maximum current in the circuit.<br>(c) the sum of the maximum
voltages across the three elements.</p>""",
          a=r"""<p class="step">(a) \(Z = \sqrt{R^2 + (X_L - X_C)^2} = \sqrt{100^2 + (400 - 600)^2} = \sqrt{50000}\)
⇒ <span class="box">\(Z = 223.6\ \Omega\)</span></p>
<p class="step">(b) \(I_0 = \dfrac{V_0}{Z} = \dfrac{100}{223.6}\) ⇒ <span class="box">\(I_0 = 0.447\) A</span></p>
<p class="step">(c) \(V_{R0} = I_0R = 44.7\) V; \(V_{L0} = I_0X_L = 178.9\) V; \(V_{C0} = I_0X_C = 268.3\) V.</p>
<p class="step">Sum \(= 44.7 + 178.9 + 268.3\) ⇒ <span class="box">\(\approx 492\) V</span></p>
<p class="step">The sum exceeds the 100 V supply because the three maxima occur at different instants: the voltages are
out of phase and add as phasors, \(V_0 = \sqrt{V_{R0}^2 + (V_{C0} - V_{L0})^2} = \sqrt{44.7^2 + 89.4^2} = 100\) V. {{fig:0}}</p>""",
          afig=[(F.fig_a13a_phasor, "Phasor diagram to scale (X_C > X_L: current leads by 63.4°)")],
          topic=EMI, recall=r"<ul><li>\(Z = \sqrt{R^2 + (X_L - X_C)^2}\), \(I_0 = V_0/Z\).</li><li>Element voltages are out of phase: they add as phasors, not arithmetically.</li></ul>"),
        Q("13(b)", 3, r"""<p>(OR) (b) Match the following:</p>
<table><tr><td>1.</td><td>\(\omega L \gt \dfrac{1}{\omega C}\)</td><td>(i)</td><td>The current is in phase with voltage V.</td></tr>
<tr><td>2.</td><td>\(\omega L \lt \dfrac{1}{\omega C}\)</td><td>(ii)</td><td>The current lags in phase with voltage V.</td></tr>
<tr><td>3.</td><td>\(\omega L = \dfrac{1}{\omega C}\)</td><td>(iii)</td><td>The current leads in phase with voltage V.</td></tr></table>""",
          a=r"""<p class="step"><b>1 → (ii)</b>: \(X_L \gt X_C\): the circuit is inductive, \(\tan\varphi = (X_L - X_C)/R \gt 0\);
the current lags the voltage.</p>
<p class="step"><b>2 → (iii)</b>: \(X_C \gt X_L\): the circuit is capacitive; the current leads the voltage.</p>
<p class="step"><b>3 → (i)</b>: \(X_L = X_C\) (resonance): \(Z = R\), φ = 0; the current is in phase with the voltage.</p>""",
          topic=EMI, recall=r"<ul><li>\(\tan\varphi = (X_L - X_C)/R\).</li><li>Resonance: \(\omega_0 = 1/\sqrt{LC}\), Z = R, current maximum.</li></ul>"),
        Q("14", 3, r"""<p>In Young's double-slit experiment, using monochromatic light, fringes are obtained on a screen placed at some
distance from the slits. If the screen is moved by \(5\times10^{-2}\) m towards the slits, the change in the fringe
width is \(3\times10^{-5}\) m. If the distance between the two slits is \(10^{-3}\) m, calculate the wavelength of the
light used.</p>""",
          a=r"""<p class="step">Fringe width \(\beta = \dfrac{\lambda D}{d}\). With λ and d fixed, \(\Delta\beta = \dfrac{\lambda\,\Delta D}{d}\).</p>
<p class="step">\(\lambda = \dfrac{d\,\Delta\beta}{\Delta D} = \dfrac{10^{-3}\times3\times10^{-5}}{5\times10^{-2}}\)</p>
<p class="step"><span class="box">\(\lambda = 6\times10^{-7}\) m \(= 600\) nm</span></p>""",
          topic=WAVE, recall=r"<ul><li>\(\beta = \lambda D/d\), so β ∝ D.</li><li>Change in β depends only on the change in D.</li></ul>"),
        Q("15(a)", 3, r"""<p>(a) With the help of Huygens wave principle show that for the refraction of light \(\mu_1\sin i = \mu_2\sin r\)</p>""",
          a=r"""<p class="step"><b>Huygens' principle:</b> every point of a wavefront is a source of secondary wavelets which
spread out with the speed of light in that medium; the new wavefront is the forward envelope (common tangent) of these
wavelets.</p>
<p class="step">A plane wavefront AB in medium 1 (speed \(v_1\)) strikes the surface XY at A. In the time t that the
disturbance at B takes to reach C (\(BC = v_1t\)), the wavelet from A spreads into medium 2 to a radius
\(AE = v_2t\). The tangent CE from C to this wavelet is the refracted wavefront. {{fig:0}}</p>
<p class="step">The angle between the incident wavefront and the surface equals the angle of incidence i, and that
between the refracted wavefront and the surface equals the angle of refraction r. In right-angled triangles ABC and AEC
(right angles at B and E):</p>
<p class="step">\(\sin i = \dfrac{BC}{AC} = \dfrac{v_1t}{AC}\), &nbsp; \(\sin r = \dfrac{AE}{AC} = \dfrac{v_2t}{AC}\)
⇒ \(\dfrac{\sin i}{\sin r} = \dfrac{v_1}{v_2}\)</p>
<p class="step">With \(\mu_1 = c/v_1\) and \(\mu_2 = c/v_2\): \(\dfrac{v_1}{v_2} = \dfrac{\mu_2}{\mu_1}\), so
\(\dfrac{\sin i}{\sin r} = \dfrac{\mu_2}{\mu_1}\) ⇒ <span class="box">\(\mu_1\sin i = \mu_2\sin r\)</span> (Snell's law).
The incident ray, refracted ray and normal lie in one plane — the plane of the figure.</p>""",
          afig=[(F.fig_a15a_huygens, "Refraction of a plane wavefront at XY (BC = v₁t, AE = v₂t)")],
          topic=WAVE, recall=r"<ul><li>Huygens: secondary wavelets, envelope = new wavefront.</li><li>Refractive index \(\mu = c/v\).</li><li>Wavefront ⊥ ray, so wavefront–surface angle = ray–normal angle.</li></ul>"),
        Q("15(b)", 3, r"""<p>(OR) (b) (i) What do you mean by coherent source of light?<br>
(ii) State one difference between diffraction and interference.<br>
(iii) Draw the intensity distribution graph for the diffraction pattern formed by a single slit.</p>""",
          a=r"""<p class="step">(i) Two sources are <b>coherent</b> if they emit light waves of the same frequency (wavelength) with a
<b>constant phase difference</b> (zero or fixed) between them, so that the interference pattern stays steady. They are
obtained from a single source (e.g. the two slits of Young's experiment illuminated by one slit).</p>
<p class="step">(ii) Any one: interference is the superposition of waves from <b>two coherent sources</b>, diffraction of
secondary wavelets from <b>different parts of the same wavefront</b>; in interference all bright fringes have (nearly)
the same intensity, in diffraction the intensity of successive maxima falls off rapidly; interference fringes are of
equal width, while the central diffraction maximum is twice as wide as the others.</p>
<p class="step">(iii) Central maximum of intensity \(I_0\) at θ = 0, minima at \(\sin\theta = \pm\lambda/a, \pm2\lambda/a, \dots\),
secondary maxima near \(\sin\theta = \pm\tfrac{3}{2}\lambda/a, \pm\tfrac52\lambda/a\) of rapidly decreasing intensity
(about \(I_0/22\), \(I_0/62\)). {{fig:0}}</p>""",
          afig=[(F.fig_a15b_single_slit, "Single-slit diffraction: intensity against sin θ")],
          topic=WAVE, recall=r"<ul><li>Single slit: minima \(a\sin\theta = n\lambda\); secondary maxima \(a\sin\theta \approx (n + \tfrac12)\lambda\).</li><li>Central maximum width \(2\lambda/a\) (angular).</li></ul>"),
        Q("16", 3, r"""<p>This question is about atomic spectra.</p>
<p>Diagram 1 shows some of the energy levels of the hydrogen atom. Diagram 2 represents part of the emission spectrum of
atomic hydrogen. The lines shown represent transitions involving the –3.40 eV level.</p>
<p>(i) Deduce the energy of a photon of wavelength 658 nm.<br>
(ii) Copy the diagram hence on the <b>diagram</b>, draw an arrow to show the electron transition between energy levels
that gives rise to the emission of a photon of wavelength 658 nm.</p>{{fig:0}}""",
          qfig=[(F.fig_q16_diagrams, "Diagrams 1 and 2 as printed (energies in eV)")],
          a=r"""<p class="step">(i) \(E = \dfrac{hc}{\lambda} = \dfrac{6.6\times10^{-34}\times3\times10^{8}}{658\times10^{-9}}\)
⇒ <span class="box">\(E = 3.01\times10^{-19}\) J \(= 1.88\) eV</span></p>
<p class="step">(ii) The emitted photon carries the difference of two levels, one of which is −3.40 eV. The level
1.88 eV above −3.40 eV is at \(-3.40 + 1.88 = -1.52 \approx -1.51\) eV. So the transition is from
<b>−1.51 eV to −3.40 eV</b> (n = 3 → n = 2, the first Balmer line, H<sub>α</sub>, red). Check:
\(-1.51 - (-3.40) = 1.89\) eV. {{fig:0}}</p>""",
          afig=[(F.fig_a16_levels, "The 658 nm line: −1.51 eV → −3.40 eV (arrow pointing down: emission)")],
          topic=ATOM, recall=r"<ul><li>\(h\nu = E_i - E_f\); \(E = hc/\lambda\).</li><li>\(E_n = -13.6/n^2\) eV: −3.40 (n = 2), −1.51 (n = 3), −0.85 (n = 4).</li><li>Emission: arrow downwards.</li></ul>"),
        Q("17", 3, r"""<p>(i) Deduce the expression for the de Broglie wavelength of moving electron.<br>
(ii) An electron beam has kinetic energy equal to 100 eV. Find the wavelength associated with the beam.</p>""",
          a=r"""<p class="step">(i) de Broglie: a particle of momentum p has a wave of wavelength \(\lambda = \dfrac{h}{p} = \dfrac{h}{mv}\).</p>
<p class="step">An electron (mass m, charge e) accelerated from rest through a p.d. V gains kinetic energy
\(K = \dfrac12mv^2 = eV\), so \(p = mv = \sqrt{2mK} = \sqrt{2meV}\).</p>
<p class="step"><span class="box">\(\lambda = \dfrac{h}{\sqrt{2mK}} = \dfrac{h}{\sqrt{2meV}}\)</span>
\(\left(\approx \dfrac{12.27}{\sqrt V}\ \text{Å}\right)\)</p>
<p class="step">(ii) \(K = 100\) eV \(= 100\times1.6\times10^{-19} = 1.6\times10^{-17}\) J.</p>
<p class="step">\(\lambda = \dfrac{6.6\times10^{-34}}{\sqrt{2\times9.1\times10^{-31}\times1.6\times10^{-17}}} =
\dfrac{6.6\times10^{-34}}{5.40\times10^{-24}}\) ⇒ <span class="box">\(\lambda = 1.22\times10^{-10}\) m \(= 1.22\) Å</span></p>""",
          topic=DUAL, recall=r"<ul><li>\(\lambda = h/p\); \(p = \sqrt{2mK}\).</li><li>For an electron \(\lambda \approx 12.27/\sqrt V\) Å.</li></ul>"),

        SEC("Section D — 15 marks"),
        Q("18(a)", 5, r"""<p>a) Draw a neat, labelled diagram of image formation by a telescope with the image at least a distance of distinct vision
hence stating the formula for angular magnification.</p>""",
          a=r"""<p class="step"><b>Astronomical (refracting) telescope, final image at the least distance of distinct vision D.</b>
The objective (large focal length \(f_o\), large aperture) forms a real, inverted, diminished image I′ of a distant object
at its focus F₀. The eyepiece (short focal length \(f_e\)) is moved so that I′ lies within its focal length, at
\(u_e\) from it; it acts as a magnifier and forms the final virtual, magnified image I at distance D from the eye. {{fig:0}}</p>
<p class="step"><b>Angular magnification</b> \(M = \dfrac{\beta}{\alpha}\), where α is the angle the object subtends at the
objective (≈ at the eye) and β the angle the final image subtends at the eye.</p>
<p class="step">If h is the size of I′: \(\alpha \approx \tan\alpha = \dfrac{h}{f_o}\), \(\beta \approx \tan\beta = \dfrac{h}{u_e}\)
⇒ \(M = \dfrac{f_o}{u_e}\).</p>
<p class="step">Eyepiece (lens formula, \(v = -D\), \(u = -u_e\)): \(-\dfrac1D + \dfrac{1}{u_e} = \dfrac{1}{f_e}\) ⇒
\(\dfrac{1}{u_e} = \dfrac{1}{f_e}\left(1 + \dfrac{f_e}{D}\right)\).</p>
<p class="step"><span class="box">\(M = \dfrac{f_o}{f_e}\left(1 + \dfrac{f_e}{D}\right)\)</span> (in magnitude; the final
image is inverted). Length of the tube \(L = f_o + u_e\). (For the final image at infinity, \(M = f_o/f_e\) and
\(L = f_o + f_e\).)</p>""",
          afig=[(F.fig_a18a_telescope, "Drawn to scale: f₀ = 24, fₑ = 6, D = 25 ⇒ uₑ = 4.84, final image 25 in front of the eyepiece")],
          topic=RAY, recall=r"<ul><li>Telescope: \(M = \beta/\alpha\).</li><li>Image at D: \(M = \dfrac{f_o}{f_e}(1 + f_e/D)\); at infinity \(M = f_o/f_e\).</li><li>Large \(f_o\), small \(f_e\) for high M.</li></ul>"),
        Q("18(b)", 5, r"""<p>(OR) b) i) With the help of a diagram, derive the condition for maxima and minima produced in YDSE [ Youngs Double
Slit Experiment.]</p>
<p>(i) A slit of width <i><b>a</b></i> is illuminated by red light of wavelength 6500 Å. For what value of <i><b>a</b></i>
will the first minima fall at an angle of diffraction of 30<sup>0</sup>?</p>
<p class="note">[The paper numbers both parts "(i)"; the second is answered as (ii).]</p>""",
          a=r"""<p><b>(i)</b> Two narrow slits S₁ and S₂, a distance d apart, are illuminated by the same monochromatic source, so
they are coherent. Consider a point P on a screen at distance D (\(D \gg d\)), at height y above the centre O, in the
direction θ. {{fig:0}}</p>
<p class="step">Draw S₁N ⊥ S₂P. Path difference \(\Delta x = S_2P - S_1P = S_2N = d\sin\theta\).</p>
<p class="step">For small θ, \(\sin\theta \approx \tan\theta = \dfrac{y}{D}\), so \(\Delta x = \dfrac{yd}{D}\).</p>
<p class="step"><b>Maxima</b> (constructive interference): \(\Delta x = n\lambda\) ⇒
<span class="box">\(y_n = \dfrac{n\lambda D}{d}\), n = 0, 1, 2, …</span></p>
<p class="step"><b>Minima</b> (destructive): \(\Delta x = (2n - 1)\dfrac\lambda2\) ⇒
<span class="box">\(y_n = \dfrac{(2n - 1)\lambda D}{2d}\), n = 1, 2, …</span></p>
<p class="step">Fringe width (distance between successive bright or dark fringes) \(\beta = \dfrac{\lambda D}{d}\).</p>
<p><b>(ii)</b> First minimum of a single slit: \(a\sin\theta = \lambda\).</p>
<p class="step">\(a = \dfrac{\lambda}{\sin30^\circ} = \dfrac{6500\times10^{-10}}{0.5}\) ⇒
<span class="box">\(a = 1.3\times10^{-6}\) m \(= 1.3\ \mu\)m</span></p>""",
          afig=[(F.fig_a18b_ydse, "Young's double slit: path difference S₂N = d sin θ")],
          topic=WAVE, recall=r"<ul><li>Path difference \(d\sin\theta \approx yd/D\).</li><li>Bright: \(n\lambda\); dark: \((2n-1)\lambda/2\); \(\beta = \lambda D/d\).</li><li>Single slit minima: \(a\sin\theta = n\lambda\).</li></ul>"),
        Q("19(a)", 5, r"""<p>a) I) Deduce an expression for<br>i) induced current<br>ii) force necessary to pull the conductor and<br>
iii) power delivered by the external source</p>
<p>For a conductor carrying free charge carriers moving in a perpendicular magnetic field. [Draw the necessary diagram for
the derivation].</p>
<p>II) What is eddy current? Write one use of it.</p>""",
          a=r"""<p><b>I)</b> A straight conductor PQ of length l slides with constant velocity v on two parallel rails joined through a
resistance R, in a uniform magnetic field B perpendicular to the plane of the rails (into the page). The rails and rod
have negligible resistance. {{fig:0}}</p>
<p class="step">If x is the length of the circuit from R to PQ, the flux through it is \(\phi = Blx\), so the induced
emf is \(\varepsilon = \left|\dfrac{d\phi}{dt}\right| = Bl\dfrac{dx}{dt} = Blv\). (Equivalently, each free charge in PQ
feels \(q\vec v\times\vec B\) along the rod.)</p>
<p class="step">(i) <b>Induced current</b>: <span class="box">\(I = \dfrac{\varepsilon}{R} = \dfrac{Blv}{R}\)</span>; by
\(q\vec v\times\vec B\) it flows from Q to P in the rod (Lenz's law).</p>
<p class="step">(ii) The current-carrying rod in the field feels \(F_B = BIl = \dfrac{B^2l^2v}{R}\), directed opposite to v.
To keep v constant the external force must balance it:
<span class="box">\(F = \dfrac{B^2l^2v}{R}\)</span>, in the direction of v.</p>
<p class="step">(iii) <b>Power</b> delivered by the external agent: <span class="box">\(P = Fv = \dfrac{B^2l^2v^2}{R}\)</span>,
which equals \(I^2R\) — the mechanical work done appears as Joule heat in R (energy conservation).</p>
<p><b>II)</b> <b>Eddy currents</b> are the closed loops of induced current set up inside the body of a bulk conductor when
the magnetic flux through it changes (or when it moves in a magnetic field); they oppose the change (Lenz) and heat the
conductor.</p>
<p class="step">One use (any one): electromagnetic (eddy current) braking in trains; induction furnace / induction
cooking; damping of a moving-coil galvanometer (dead-beat); speedometers; energy meters.</p>""",
          afig=[(F.fig_a19a_rails, "Rod PQ on rails in B (into page): induced I from Q to P, F_B opposes v")],
          topic=EMI, recall=r"<ul><li>Motional emf \(\varepsilon = Blv\).</li><li>Force on current \(F = BIl\); Lenz: it opposes the motion.</li><li>\(P = Fv = I^2R\).</li></ul>"),
        Q("19(b)", 5, r"""<p>(OR) b) I) An alternating emf is applied to a series combination of a resistor of resistance R, a capacitor of
capacitance C and an inductor of inductance L. Derive the phase relationship between current and emf. Find the impedance
of the circuit. Draw the necessary phasor diagram.</p>
<p>II) In a galvanometer there is a deflection of 10 divisions per mA. The internal resistance of the galvanometer is
60 Ω. If a shunt of 2.5 Ω is connected to the galvanometer and there are 50 divisions in all on the scale of the
galvanometer, what maximum current can this galvanometer read?</p>""",
          a=r"""<p><b>I)</b> An emf \(V = V_0\sin\omega t\) is applied to R, L and C in series. {{fig:0}}</p>
<p class="step">The same current \(I = I_0\sin(\omega t - \varphi)\) flows through all three. Taking I as the reference
phasor: \(V_R = I_0R\) is in phase with I; \(V_L = I_0X_L\) leads I by 90°; \(V_C = I_0X_C\) lags I by 90°
(\(X_L = \omega L\), \(X_C = 1/\omega C\)).</p>
<p class="step">\(V_L\) and \(V_C\) are opposite, so their resultant is \(V_L - V_C\) (taking \(V_L \gt V_C\)), at 90° to
\(V_R\). The applied emf is the phasor sum: {{fig:1}}</p>
<p class="step">\(V_0^2 = V_R^2 + (V_L - V_C)^2 = I_0^2\left[R^2 + (X_L - X_C)^2\right]\)</p>
<p class="step"><b>Impedance</b>: <span class="box">\(Z = \dfrac{V_0}{I_0} = \sqrt{R^2 + (X_L - X_C)^2} =
\sqrt{R^2 + \left(\omega L - \dfrac{1}{\omega C}\right)^2}\)</span></p>
<p class="step"><b>Phase</b>: <span class="box">\(\tan\varphi = \dfrac{V_L - V_C}{V_R} = \dfrac{X_L - X_C}{R}\)</span>.
If \(X_L \gt X_C\) the emf leads the current by φ; if \(X_L \lt X_C\) the current leads; if \(X_L = X_C\) they are in
phase (resonance, Z = R).</p>
<p><b>II)</b> Full-scale current of the galvanometer: \(I_g = \dfrac{50\ \text{div}}{10\ \text{div/mA}} = 5\) mA.</p>
<p class="step">With the shunt, \(I_gG = (I - I_g)S\) ⇒ \(I = I_g\left(1 + \dfrac GS\right) = 5\times10^{-3}\left(1 + \dfrac{60}{2.5}\right)
= 5\times10^{-3}\times25\)</p>
<p class="step"><span class="box">\(I_{\max} = 0.125\) A \(= 125\) mA</span></p>""",
          afig=[(F.fig_a19b_lcr, "Series LCR circuit"), (F.fig_a19b_phasor, "Phasor diagram (current I₀ as reference)")],
          topic=EMI, recall=r"<ul><li>R: V in phase with I; L: V leads by 90°; C: V lags by 90°.</li><li>\(Z = \sqrt{R^2 + (X_L - X_C)^2}\), \(\tan\varphi = (X_L - X_C)/R\).</li><li>Shunt: \(I_gG = (I - I_g)S\).</li></ul>"),
        Q("20", 5, r"""<p>(i) With the help of a suitable circuit diagram (block diagram), sketch the characteristic curves of a junction
diode.<br>
(ii) With the help of a circuit diagram, explain full-wave rectification using a junction diode. Draw the waveforms of
input and output voltages.</p>""",
          a=r"""<p><b>(i)</b> The p-n junction diode is connected through a milliammeter to a battery via a rheostat used as a
potential divider, with a voltmeter across the diode. The p-side is joined to the + side (forward bias). For reverse
bias the battery connections are reversed and a microammeter replaces the milliammeter. The voltage is varied in steps
and the current noted. {{fig:0}}</p>
<p class="step"><b>Forward bias:</b> the current is negligible until the voltage exceeds the barrier potential (the knee
or threshold voltage, ≈ 0.7 V for Si, 0.3 V for Ge); beyond it the current rises steeply (non-linearly) — a few mA.</p>
<p class="step"><b>Reverse bias:</b> a very small, almost constant current (μA) due to minority carriers, until at the
breakdown voltage the reverse current rises suddenly. {{fig:1}}</p>
<p><b>(ii) Full-wave (centre-tap) rectifier.</b> The a.c. input is applied to the primary of a transformer whose secondary
is centre-tapped at T. The ends S₁ and S₂ feed two diodes D₁ and D₂, whose cathodes are joined at P; the load
\(R_L\) is connected between P and T. {{fig:2}}</p>
<p class="step">During the half-cycle when S₁ is positive with respect to T, D₁ is forward biased and conducts while D₂
is reverse biased; current flows S₁ → D₁ → P → \(R_L\) → T.</p>
<p class="step">In the next half-cycle S₂ is positive; D₂ conducts and D₁ is off; current flows S₂ → D₂ → P → \(R_L\) → T
— <b>in the same direction</b> through the load.</p>
<p class="step">So both halves of every input cycle give output: a unidirectional, pulsating d.c. voltage across
\(R_L\) (frequency twice the input frequency), which a capacitor filter can smooth. {{fig:3}}</p>""",
          afig=[(F.fig_a20_bias, "Circuit for the diode characteristics (forward bias shown)"),
                (F.fig_a20_iv, "I–V characteristics of a p-n junction diode (forward in mA, reverse in μA; not to the same scale)"),
                (F.fig_a20_fwr, "Centre-tap full-wave rectifier"),
                (F.fig_a20_waves, "Input and output waveforms")],
          topic=ELEC, recall=r"<ul><li>Forward bias: p to +; current after the knee voltage.</li><li>Reverse bias: tiny minority-carrier current; breakdown at high reverse voltage.</li><li>Full-wave: two diodes conduct alternately; load current in one direction.</li></ul>"),
    ])
