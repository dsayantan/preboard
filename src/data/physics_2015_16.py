"""Heritage School Pre-Board 2015-16, Physics Paper 1 (Theory) — digital copy, ISC 2027 filter, solutions.
Transcribed from the page images (the PDF's text layer is unusable OCR)."""
from kit import Q, SEC
import physics_2015_16_figs as F

ES, CE, MAG = "Electrostatics", "Current Electricity", "Magnetic Effects of Current and Magnetism"
EMI, RAY, WAVE = "Electromagnetic Induction and Alternating Currents", "Optics — Ray Optics", "Optics — Wave Optics"
DUAL, ATOM, NUC, ELEC = ("Dual Nature of Radiation and Matter", "Atoms and Nuclei — Atoms",
                         "Atoms and Nuclei — Nuclei", "Electronic Devices")

PAPER = dict(
    subject="physics", year="2015-16", slug="2015-16", paper="Paper 1 (Theory)",
    source="PreBoard-PYQ/2015-16/Physics.pdf", marks=70, time="3 hours",
    intro=r"""<p><i>Candidates are allowed additional 15 minutes for only reading this paper. They must not start
writing during this time.</i></p>
<p>Answer all questions in Part I. Part II consists of three groups A, B &amp; C. Answer 10 questions from this
part choosing four from Section A and three from each of the sections B and C. All working including rough work
should be done on the same sheet as and adjacent to, the rest of the answer. The intended marks for questions or
parts of questions are given in brackets [ ].</p>
<p><b>Useful constants and relations</b> (as printed): electron charge \(e = 1.6\times10^{-19}\) C; Planck's
constant \(h = 6.6\times10^{-34}\) J s; speed of light in vacuum \(c = 3\times10^{8}\) m/s; permittivity of free
space \(\varepsilon_0 = 8.85\times10^{-12}\) F/m; \(\mu_0 = 4\pi\times10^{-7}\) T m A\(^{-1}\); mass of an electron
\(= 9\times10^{-31}\) kg; Avogadro number \(= 6.023\times10^{23}\) mol\(^{-1}\); 1 u = 931 MeV; \(\pi = 3.14\).</p>""",
    items=[
        SEC("Part I — Question 1 A. Select the correct alternative [1×5]", "Answer all questions."),
        Q("1(A)(i)", 1, r"""<p>A short electric dipole consisting of charges \(+q\) &amp; \(-q\) is placed at the center
\(O\) of a large cube of side length \(L\). The electric flux emanating through the cube is:</p>
<p>(a) \(\dfrac{q}{4\pi\varepsilon_0 L}\) &nbsp; (b) \(\dfrac{q}{2\pi\varepsilon_0 L}\) &nbsp; (c) Zero &nbsp;
(d) \(\dfrac{q}{3\pi\varepsilon_0 L}\)</p>""",
          a=r"""<p><b>(c) Zero.</b></p>
<p class="step">Gauss's theorem: \(\phi_E = q_{\text{enclosed}}/\varepsilon_0\). The cube encloses \(+q\) and \(-q\),
net charge zero, so \(\phi_E = 0\) (as many field lines enter the cube as leave it).</p>
<p class="step">Note also that options (a), (b), (d) have the dimensions of potential (V), not flux (V m).</p>""",
          topic=ES, recall=r"""<ul><li>Gauss's theorem: \(\oint \vec E\cdot d\vec A = q_{\text{enc}}/\varepsilon_0\).</li>
<li>Only the <em>net</em> enclosed charge matters; size and shape of the surface do not.</li></ul>"""),
        Q("1(A)(ii)", 1, r"""<p>The equivalent resistance between points \(a\) and \(f\) of the electric network given
below is.</p>{{fig:0}}<p>(a) 24 Ω &nbsp; (b) 110 Ω &nbsp; (c) 140 Ω &nbsp; (d) 200 Ω</p>""",
          qfig=F.fig_q1a2_network,
          a=r"""<p><b>(c) 140 Ω.</b></p>
<p class="step">Points \(c\) and \(d\) are free ends, so no current flows in the 20 Ω and 40 Ω resistors; they
play no part.</p>
<p class="step">The current from \(a\) to \(f\) must go \(a\to b\to e\to f\): 10 Ω, 50 Ω and 80 Ω in series.</p>
<p class="step">\(R_{af} = 10 + 50 + 80 = \) <span class="box">140 Ω</span></p>""",
          topic=CE, recall=r"""<ul><li>A resistor with one end free carries no current.</li>
<li>Series: \(R = R_1 + R_2 + \dots\)</li></ul>"""),
        Q("1(A)(iii)", 1, r"""<p>To a bird in air a fish in water \((\mu = 4/3)\) appears to be at 30 cm from the
surface. The real depth of the fish is:</p><p>(a) 22.5 cm &nbsp; (b) 30 cm &nbsp; (c) 40 cm &nbsp; (d) 45 cm</p>""",
          a=r"""<p><b>(c) 40 cm.</b></p>
<p class="step">Viewing from the rarer medium (air) into the denser medium (water):
\(\mu = \dfrac{\text{real depth}}{\text{apparent depth}}\).</p>
<p class="step">Real depth \(= \mu \times 30 = \tfrac43\times 30 = \) <span class="box">40 cm</span></p>""",
          topic=RAY, recall=r"""<ul><li>\(\mu = \text{real depth}/\text{apparent depth}\) when viewed from air.</li>
<li>An object in a denser medium appears raised (nearer the surface).</li></ul>"""),
        Q("1(A)(iv)", 1, r"""<p>If the radius of second electron orbit in hydrogen atom be r then the radius of the third
orbit will be:</p><p>(a) \(3r\) &nbsp; (b) \(2.25r\) &nbsp; (c) \(9r\) &nbsp; (d) \(\dfrac{r}{3}\)</p>""",
          a=r"""<p><b>(b) 2.25 r.</b></p>
<p class="step">Bohr: \(r_n \propto n^2\). So \(\dfrac{r_3}{r_2} = \dfrac{9}{4}\), \(r_3 = 2.25\,r\).</p>""",
          topic=ATOM, recall=r"""<ul><li>\(r_n = \dfrac{\varepsilon_0 n^2 h^2}{\pi m e^2} = 0.53\,n^2\) Å for hydrogen.</li></ul>"""),
        Q("1(A)(v)", 1, r"""<p>Binding energy of a nucleus is of the order of:</p>
<p>(a) eV &nbsp; (b) keV &nbsp; (c) MeV &nbsp; (d) joule</p>""",
          a=r"""<p><b>(c) MeV.</b> Binding energy per nucleon is about 7–9 MeV, so a nucleus is bound by a few MeV
to about 2000 MeV — the MeV is the natural unit (atomic electrons are bound by eV).</p>""",
          topic=NUC, recall=r"""<ul><li>BE \(= \Delta m\,c^2\); 1 u \(\equiv\) 931 MeV.</li>
<li>BE/A ≈ 8.5 MeV near A ≈ 56 (most stable).</li></ul>"""),

        SEC("Part I — Question 1 B. Answer all questions briefly and to the point [1×15]"),
        Q("1(B)(i)", 1, r"""<p>A point charge of \(5\times10^{-6}\) C experiences a force of \(2\times10^{-3}\) N when kept
in a uniform electric field of intensity \(E\). Find \(E\).</p>
<p class="note">[The exponent of the force is faint in the scan; at 400 dpi it reads \(10^{-3}\).]</p>""",
          a=r"""<p class="step">\(E = \dfrac{F}{q} = \dfrac{2\times10^{-3}}{5\times10^{-6}}\) = <span class="box">400 N C\(^{-1}\)</span></p>""",
          topic=ES, recall=r"""<ul><li>\(\vec F = q\vec E\); unit of \(E\): N/C = V/m.</li></ul>"""),
        Q("1(B)(ii)", 1, r"""<p>Write an expression for magnetic flux density \(B\) at a point on the end-on position or an
axial position of a magnetic dipole. (No derivation is expected)</p>""",
          a=r"""<p class="step">For a short magnet (dipole) of moment \(m\), at distance \(d\) from its centre on the axis:</p>
<p><span class="box">\(B_{\text{axial}} = \dfrac{\mu_0}{4\pi}\,\dfrac{2m}{d^3}\)</span>, directed along \(\vec m\)
(from S to N of the magnet).</p>""",
          topic=MAG, recall=r"""<ul><li>Axial: \(\frac{\mu_0}{4\pi}\frac{2m}{d^3}\); equatorial: \(\frac{\mu_0}{4\pi}\frac{m}{d^3}\), opposite to \(\vec m\).</li>
<li>Same form as the electric dipole with \(1/4\pi\varepsilon_0 \to \mu_0/4\pi\), \(p\to m\).</li></ul>"""),
        Q("1(B)(iii)", 1, r"""<p>When two capacitors, one \(3\,\mu\)F and other of \(6\,\mu\)F are connected in series and
the combination is charged to a potential difference of 120 V then what is the potential difference across the
\(3\,\mu\)F capacitor?</p>""",
          a=r"""<p class="step">\(C_s = \dfrac{3\times6}{3+6} = 2\ \mu\text{F}\); \(Q = C_sV = 2\times120 = 240\ \mu\)C
(same on each in series).</p>
<p class="step">\(V_3 = \dfrac{Q}{C} = \dfrac{240}{3} = \) <span class="box">80 V</span> (and 40 V across the 6 μF).</p>""",
          topic=ES, recall=r"""<ul><li>Series capacitors carry the same charge; \(V \propto 1/C\).</li></ul>"""),
        Q("1(B)(iv)", 1, r"""<p>A current \(I\) flows through a metallic wire of radius \(r\) and free electrons in it drift
with a velocity \(v_d\). Calculate the drift velocity of the free electrons through the wire of the same
material, having doubled its radius, when the same current flows through it.</p>""",
          a=r"""<p class="step">\(I = neAv_d = ne\pi r^2 v_d\). Same \(I\), same \(n\) (same material):
\(v_d \propto 1/r^2\).</p>
<p class="step">Radius doubled → area ×4 → <span class="box">\(v_d' = v_d/4\)</span></p>""",
          topic=CE, recall=r"""<ul><li>\(I = neAv_d\).</li><li>\(n\) depends only on the material.</li></ul>"""),
        Q("1(B)(v)", 1, r"""<p>If the horizontal and vertical components of Earth's magnetic field are equal at a certain
place then what is the angle of dip at that place.</p>""",
          excluded="Earth's magnetic field (elements, angle of dip) — not in the ISC 2027 Class XII syllabus; "
                   "'Magnetism and Matter' lists only the magnetic dipole, bar magnet, dia/para/ferro and the B-H loop."),
        Q("1(B)(vi)", 1, r"""<p>Two resistors 6 Ω and 9 Ω are connected in parallel across a current source. Find the
ratio of electric current flowing through the two resistors.</p>""",
          a=r"""<p class="step">In parallel the p.d. is the same: \(I = V/R\), so \(I \propto 1/R\).</p>
<p class="step">\(I_6 : I_9 = \dfrac{1}{6} : \dfrac{1}{9} = \) <span class="box">3 : 2</span></p>""",
          topic=CE, recall=r"""<ul><li>Parallel: same V; current divides inversely as resistance.</li></ul>"""),
        Q("1(B)(vii)", 1, r"""<p>A very long straight wire carries a current \(I\). At the instant when a charge \(+Q\) at
a point P at a distance \(a\) has velocity \(\vec v\) (shown in figure), find the magnitude and direction of force on
the charge.</p>{{fig:0}}""",
          qfig=F.fig_q1b7_wire, afig=F.fig_a1b7_force,
          a=r"""<p class="step">Field of the wire at P: \(B = \dfrac{\mu_0 I}{2\pi a}\); by the right-hand rule (current
upward, P to its right) \(\vec B\) is <b>into the page</b>.</p>
<p class="step">\(\vec v\) (away from the wire) ⟂ \(\vec B\): \(F = QvB\sin 90^\circ\).</p>
<p><span class="box">\(F = \dfrac{\mu_0 I Q v}{2\pi a}\)</span>, directed <b>parallel to the current</b>
(\(\vec v\times\vec B\): away-from-wire × into-page = along \(I\)).</p>{{fig:0}}""",
          topic=MAG, recall=r"""<ul><li>Long wire: \(B = \mu_0 I/2\pi a\), circles round the wire (right-hand grip rule).</li>
<li>Lorentz force \(\vec F = q\,\vec v\times\vec B\).</li></ul>"""),
        Q("1(B)(viii)", 1, r"""<p>A closed conducting loop moves normal to the electric field between the plates of a large
capacitor. Is there any current induced in the loop when it is: a) wholly inside the capacitor b) partially
outside the plates of the capacitor? The electric field is normal to the plane of the loop.</p>""",
          a=r"""<p class="step"><b>No current in either case.</b> A current is induced only by a change of
<em>magnetic</em> flux through the loop (Faraday). A static electric field between charged plates produces no
magnetic field, so the magnetic flux through the loop stays zero whether the loop is wholly inside (a) or partly
outside (b) the plates.</p>""",
          topic=EMI, recall=r"""<ul><li>Faraday: \(\varepsilon = -d\phi_B/dt\) — magnetic flux only.</li></ul>"""),
        Q("1(B)(ix)", 1, r"""<p>Draw the graph showing the variation of capacitive reactance \(X_C\) of a capacitor with
frequency \(f\) of an a.c circuit.</p>""",
          afig=F.fig_a1b9_xc,
          a=r"""<p class="step">\(X_C = \dfrac{1}{2\pi f C}\), so \(X_C \propto 1/f\): a rectangular hyperbola, very large at
low \(f\) (infinite for d.c.) and tending to zero at high \(f\).</p>{{fig:0}}""",
          topic=EMI, recall=r"""<ul><li>\(X_C = 1/\omega C\), \(X_L = \omega L\).</li><li>A capacitor blocks d.c., passes high-frequency a.c.</li></ul>"""),
        Q("1(B)(x)", 1, r"""<p>State one condition for obtaining sustained interference of light.</p>""",
          a=r"""<p class="step">The two sources must be <b>coherent</b> — they must emit waves of the same frequency with a
constant (time-independent) phase difference (in practice, both derived from a single source).</p>
<p class="note">Other acceptable conditions: equal (or nearly equal) amplitudes; narrow sources close to each
other; monochromatic light.</p>""",
          topic=WAVE, recall=r"""<ul><li>Sustained interference needs a constant phase difference → coherent sources.</li></ul>"""),
        Q("1(B)(xi)", 1, r"""<p>Define angular magnification of an optical instrument.</p>""",
          a=r"""<p class="step">Angular magnification (magnifying power) is the ratio of the angle subtended at the eye by
the final image, \(\beta\), to the angle subtended at the eye by the object seen directly (placed at the least
distance of distinct vision for a microscope, at its actual position for a telescope), \(\alpha\):
<span class="box">\(M = \beta/\alpha\)</span></p>""",
          topic=RAY, recall=r"""<ul><li>Simple microscope: \(M = 1 + D/f\) (image at D), \(D/f\) (image at ∞).</li></ul>"""),
        Q("1(B)(xii)", 1, r"""<p>A particle is dropped from a height \(H\). Write down the expression for the de Broglie
wavelength of the particle as a function of height.</p>""",
          a=r"""<p class="step">After falling through \(H\): \(v = \sqrt{2gH}\), momentum \(p = m\sqrt{2gH}\).</p>
<p><span class="box">\(\lambda = \dfrac{h}{p} = \dfrac{h}{m\sqrt{2gH}}\)</span></p>""",
          topic=DUAL, recall=r"""<ul><li>de Broglie: \(\lambda = h/p = h/mv\).</li></ul>"""),
        Q("1(B)(xiii)", 1, r"""<p>On the basis of Bohr's model find the radius of the \(\mathrm{Li^{++}}\) ion in its ground
state. Consider the Bohr's radius as \(a_0 = 53\) pm.</p>""",
          a=r"""<p class="step">For a one-electron ion: \(r_n = \dfrac{a_0 n^2}{Z}\). \(\mathrm{Li^{++}}\): \(Z = 3\), \(n = 1\).</p>
<p class="step">\(r_1 = \dfrac{53}{3}\) = <span class="box">17.7 pm</span></p>""",
          topic=ATOM, recall=r"""<ul><li>\(r_n \propto n^2/Z\); \(E_n \propto -Z^2/n^2\) for hydrogen-like ions.</li></ul>"""),
        Q("1(B)(xiv)", 1, r"""<p>How much energy will be created if 1 g of matter is destroyed completely?</p>""",
          a=r"""<p class="step">\(E = mc^2 = (1\times10^{-3})(3\times10^{8})^2\) = <span class="box">\(9\times10^{13}\) J</span></p>""",
          topic=NUC, recall=r"""<ul><li>Einstein: \(E = mc^2\) (mass in kg).</li></ul>"""),
        Q("1(B)(xv)", 1, r"""<p>What are extrinsic semiconductors?</p>""",
          a=r"""<p class="step">An extrinsic semiconductor is a pure (intrinsic) semiconductor such as Si or Ge
<b>doped</b> with a small, controlled amount of impurity to increase its conductivity: a pentavalent impurity
(P, As) gives an <b>n-type</b> semiconductor (electrons majority carriers); a trivalent impurity (B, Al, In)
gives a <b>p-type</b> semiconductor (holes majority carriers).</p>""",
          topic=ELEC, recall=r"""<ul><li>Donor (group 15) → n-type; acceptor (group 13) → p-type.</li></ul>"""),

        SEC("Part II — Section A", "Answer any four questions from this section."),
        Q("2(a)", 2, r"""<p>An electric dipole of dipole moment \(\vec p\) is placed in a uniform electric field \(\vec E\)
with its axis inclined to the field. Write an expression for the torque \(\vec\tau\) experienced by the dipole in
vector form. Show diagrammatically how the dipole should be kept in the electric field so that the torque acting
on it is: i) maximum &nbsp; ii) zero</p>""",
          afig=F.fig_a2a_dipole,
          a=r"""<p class="step"><span class="box">\(\vec\tau = \vec p\times\vec E\)</span>, magnitude
\(\tau = pE\sin\theta\), \(\theta\) = angle between \(\vec p\) and \(\vec E\).</p>
<p class="step">(i) Maximum, \(\tau = pE\), when \(\theta = 90^\circ\): dipole axis perpendicular to the field.</p>
<p class="step">(ii) Zero when \(\theta = 0^\circ\) (stable) or \(180^\circ\) (unstable): axis along the field.</p>
{{fig:0}}""",
          topic=ES, recall=r"""<ul><li>Net force on a dipole in a uniform field is zero; the two forces form a couple.</li>
<li>Arm of the couple \(= 2l\sin\theta\) ⇒ \(\tau = qE\cdot2l\sin\theta = pE\sin\theta\).</li></ul>"""),
        Q("2(b)", 3, r"""<p>A capacitor of \(4\,\mu\)F is connected to 400 V supply. It is then disconnected and
connected to an uncharged capacitor of \(2\,\mu\)F. Calculate: i) Common potential after the capacitors are
connected together. ii) Loss of energy in the form of heat and radiation.</p>""",
          a=r"""<p class="step">Charge on the first: \(Q = C_1V_1 = 4\times10^{-6}\times400 = 1.6\times10^{-3}\) C. Charge is
conserved on sharing.</p>
<p class="step">(i) \(V = \dfrac{C_1V_1}{C_1+C_2} = \dfrac{1.6\times10^{-3}}{6\times10^{-6}}\) =
<span class="box">266.7 V</span></p>
<p class="step">(ii) \(U_i = \tfrac12 C_1V_1^2 = \tfrac12(4\times10^{-6})(400)^2 = 0.320\) J</p>
<p class="step">\(U_f = \tfrac12(C_1+C_2)V^2 = \tfrac12(6\times10^{-6})(266.7)^2 = 0.2133\) J</p>
<p class="step">Loss \(= U_i - U_f\) = <span class="box">0.107 J</span>
(check: \(\dfrac{C_1C_2}{2(C_1+C_2)}V_1^2 = \dfrac{8\times10^{-12}}{12\times10^{-6}}\times160000 = 0.107\) J).</p>""",
          topic=ES, recall=r"""<ul><li>Charge is conserved when capacitors share charge; energy is not.</li>
<li>\(U = \tfrac12CV^2 = Q^2/2C\); loss \(= \dfrac{C_1C_2(V_1-V_2)^2}{2(C_1+C_2)}\).</li></ul>"""),
        Q("3(a)", 2, r"""<p>Derive using Gauss' theorem an expression for the electric field intensity at a distance
\(r\) from an infinitely long line of charge having a uniform charge density \(\lambda\) coulomb/m.</p>""",
          afig=F.fig_a3a_gauss,
          a=r"""<p class="step">By symmetry \(\vec E\) is radial (perpendicular to the line) and has the same magnitude at all
points at distance \(r\). Choose a coaxial Gaussian cylinder of radius \(r\) and length \(l\).</p>{{fig:0}}
<p class="step">Flux through the flat caps is zero (\(\vec E \perp d\vec A\)). On the curved surface \(\vec E \parallel d\vec A\)
and \(E\) is constant: \(\phi = E(2\pi r l)\).</p>
<p class="step">Charge enclosed \(= \lambda l\). Gauss: \(E(2\pi r l) = \dfrac{\lambda l}{\varepsilon_0}\)</p>
<p><span class="box">\(E = \dfrac{\lambda}{2\pi\varepsilon_0 r}\)</span>, radially outward for \(\lambda>0\).</p>""",
          topic=ES, recall=r"""<ul><li>Gaussian surface: matches the symmetry; \(E\) constant and ∥ or ⟂ to \(d\vec A\) on each part.</li>
<li>Line: \(E\propto 1/r\); sheet: \(\sigma/2\varepsilon_0\) (constant); shell: \(q/4\pi\varepsilon_0 r^2\) outside, 0 inside.</li></ul>"""),
        Q("3(b)", 3, r"""<p>Two positive charges of \(10\,\mu\)C each are situated 10 cm apart from each other. What is
the increase in the electrostatic potential energy of the system when two charges are brought closer by 7 cm?</p>""",
          a=r"""<p class="step">\(U = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1q_2}{r}\), \(q_1q_2 = (10^{-5})^2 = 10^{-10}\) C².</p>
<p class="step">\(r_1 = 0.10\) m: \(U_1 = 9\times10^{9}\times10^{-10}/0.10 = 9.0\) J.</p>
<p class="step">\(r_2 = 0.10 - 0.07 = 0.03\) m: \(U_2 = 0.9/0.03 = 30.0\) J.</p>
<p class="step">Increase \(\Delta U = U_2 - U_1\) = <span class="box">21 J</span> (work done against the repulsion).</p>""",
          topic=ES, recall=r"""<ul><li>\(U = q_1q_2/4\pi\varepsilon_0 r\); like charges: \(U\) rises as they approach.</li></ul>"""),
        Q("4(a)", 2, r"""<p>Why is a potentiometer preferred to a voltmeter in measuring the emf of a cell?</p>""",
          a=r"""<p class="step">A voltmeter draws a current from the cell, so it reads the terminal p.d.
\(V = \varepsilon - Ir\), which is less than the emf.</p>
<p class="step">A potentiometer uses a null method: at the balance point <b>no current is drawn</b> from the cell,
so there is no drop across its internal resistance and the balancing p.d. equals the emf exactly. (It is also
more sensitive, since a long wire gives a small potential gradient.)</p>""",
          topic=CE, recall=r"""<ul><li>\(V = \varepsilon - Ir\) when current flows; \(V = \varepsilon\) only when \(I = 0\).</li>
<li>Potentiometer principle: \(V = Kl\) for a wire of uniform cross-section and steady current.</li></ul>"""),
        Q("4(b)", 3, r"""<p>For what value of unknown resistance \(x\), the p.d between B and D is zero in the arrangement
shown in figure.</p>{{fig:0}}""",
          qfig=F.fig_q4b_bridge,
          a=r"""<p class="step">Arm AB: 6 Ω + 6 Ω in series = 12 Ω. Arm BC: 1 Ω ∥ 1 Ω = 0.5 Ω.</p>
<p class="step">Arm AD: \((x + 6)\) Ω. Arm DC: 2 Ω ∥ 2 Ω = 1 Ω.</p>
<p class="step">\(V_B = V_D\) means the Wheatstone bridge is balanced:
\(\dfrac{R_{AB}}{R_{BC}} = \dfrac{R_{AD}}{R_{DC}}\Rightarrow \dfrac{12}{0.5} = \dfrac{x+6}{1}\)</p>
<p class="step">\(x + 6 = 24\Rightarrow\) <span class="box">\(x = 18\) Ω</span></p>""",
          topic=CE, recall=r"""<ul><li>Balanced bridge: \(P/Q = R/S\), no current through the cross-link BD.</li>
<li>Two equal resistors \(R\) in parallel give \(R/2\).</li></ul>"""),
        Q("5(a)", 2, r"""<p>Calculate the magnitude of the force on an electron moving with a velocity
\(3\times10^{7}\) m/s at right angle to a magnetic field of 10 T.</p>""",
          a=r"""<p class="step">\(F = evB\sin 90^\circ = (1.6\times10^{-19})(3\times10^{7})(10)\) =
<span class="box">\(4.8\times10^{-11}\) N</span>, perpendicular to both \(\vec v\) and \(\vec B\).</p>""",
          topic=MAG, recall=r"""<ul><li>\(F = qvB\sin\theta\); for an electron use \(\vec F = -e\,\vec v\times\vec B\) for direction.</li></ul>"""),
        Q("5(b)", 3, r"""<p>What is hysteresis loss? How does the magnetic permeability \(\mu\) differ for dia, para and
ferromagnetic materials?</p>""",
          afig=F.fig_a5b_hysteresis,
          a=r"""<p class="step"><b>Hysteresis loss:</b> when a ferromagnetic material is taken through a complete cycle of
magnetisation, the magnetisation lags behind the magnetising field and energy is dissipated as heat in the
material. The energy lost per unit volume per cycle equals the <b>area of the B–H loop</b>.</p>{{fig:0}}
<p class="step"><b>Permeability</b> (\(\mu_r = \mu/\mu_0 = 1+\chi_m\)):</p>
<ul><li>Diamagnetic: \(\mu_r\) slightly <b>less than 1</b> (\(\chi_m\) small, negative), e.g. Bi, Cu.</li>
<li>Paramagnetic: \(\mu_r\) slightly <b>greater than 1</b> (\(\chi_m\) small, positive), e.g. Al, Pt.</li>
<li>Ferromagnetic: \(\mu_r \gg 1\) (hundreds to thousands) and depends on \(H\), e.g. Fe, Ni, Co.</li></ul>""",
          topic=MAG, recall=r"""<ul><li>Retentivity: \(B\) left when \(H = 0\); coercivity: reverse \(H\) needed to make \(B = 0\).</li>
<li>Transformer cores: soft iron — narrow loop (low hysteresis loss).</li></ul>"""),
        Q("6(a)", 2, r"""<p>An \(\alpha\) particle and a proton are moving in the plane of the paper in a region of uniform
magnetic field \((\vec B)\), directed normal to the plane of the paper. If the two particles have equal linear
momenta, what will be the ratio of the radii of their trajectories in the field?</p>""",
          a=r"""<p class="step">\(qvB = \dfrac{mv^2}{r}\Rightarrow r = \dfrac{mv}{qB} = \dfrac{p}{qB}\). Same \(p\) and \(B\):
\(r\propto 1/q\).</p>
<p class="step">\(\dfrac{r_\alpha}{r_p} = \dfrac{q_p}{q_\alpha} = \dfrac{e}{2e}\) ⇒ <span class="box">\(r_\alpha : r_p = 1 : 2\)</span></p>""",
          topic=MAG, recall=r"""<ul><li>Radius in a magnetic field: \(r = p/qB = \sqrt{2mK}/qB\).</li></ul>"""),
        Q("6(b)", 3, r"""<p>A 0.5 m long metal rod PQ completes the circuit, as shown in the figure. The area of the
circuit is perpendicular to the magnetic field of flux density 0.15 T. If the resistance of the total circuit is
3 Ω, calculate the force needed to move the rod in the direction as indicated in figure, with a constant speed
2 m/s.</p>{{fig:0}}""",
          qfig=F.fig_q6b_rod,
          a=r"""<p class="step">Motional emf: \(\varepsilon = Blv = 0.15\times0.5\times2 = 0.15\) V.</p>
<p class="step">Current: \(I = \varepsilon/R = 0.15/3 = 0.05\) A.</p>
<p class="step">Force on the rod: \(F = BIl = 0.15\times0.05\times0.5\) = <span class="box">\(3.75\times10^{-3}\) N</span></p>
<p class="step">By Lenz's law this magnetic force opposes the motion, so to keep the speed constant an equal force
must be applied <b>in the direction of motion</b> (\(F = B^2l^2v/R\)).</p>""",
          topic=EMI, recall=r"""<ul><li>Motional emf \(\varepsilon = Blv\); retarding force \(F = B^2l^2v/R\).</li>
<li>Power supplied \(Fv = \varepsilon^2/R\) appears as Joule heat.</li></ul>"""),
        Q("7(a)", 2, r"""<p>What is the power consumed by an ideal inductor even though both V and I are non-zero?
Explain your answer in brief.</p>""",
          afig=F.fig_a7a_phasor,
          a=r"""<p class="step"><b>Zero.</b> In an ideal (resistanceless) inductor the current lags the voltage by
\(\pi/2\), so the power factor \(\cos\varphi = \cos 90^\circ = 0\) and \(P = V_{\text{rms}}I_{\text{rms}}\cos\varphi = 0\).</p>
<p class="step">Energy stored in the magnetic field during one quarter cycle is returned to the source in the next
quarter, so the average power over a cycle is zero (wattless current).</p>{{fig:0}}""",
          topic=EMI, recall=r"""<ul><li>\(P_{\text{av}} = V_{\text{rms}}I_{\text{rms}}\cos\varphi\), \(\cos\varphi = R/Z\).</li></ul>"""),
        Q("7(b)", 3, r"""<p>An LCR series circuit with 100 Ω resistance is connected to an ac source of 200 V and
angular frequency 300 rad/s. When only the capacitance is removed, the current lags behind the voltage by
\(60^0\). When only the inductance is removed, the current leads the voltage by \(60^0\). Calculate the current
and power dissipated in LCR circuit.</p>""",
          a=r"""<p class="step">LR circuit: \(\tan 60^\circ = X_L/R\Rightarrow X_L = 100\sqrt3\) Ω.</p>
<p class="step">CR circuit: \(\tan 60^\circ = X_C/R\Rightarrow X_C = 100\sqrt3\) Ω.</p>
<p class="step">In LCR: \(X_L = X_C\) — resonance, \(Z = \sqrt{R^2+(X_L-X_C)^2} = R = 100\) Ω.</p>
<p class="step">\(I = V/Z = 200/100\) = <span class="box">2 A</span></p>
<p class="step">\(P = I^2R = 4\times100\) = <span class="box">400 W</span> (power factor 1).</p>""",
          topic=EMI, recall=r"""<ul><li>\(\tan\varphi = (X_L - X_C)/R\); \(Z = \sqrt{R^2 + (X_L-X_C)^2}\).</li>
<li>At resonance \(Z = R\), current and power are maximum.</li></ul>"""),

        SEC("Part II — Section B", "Answer any three questions from this section."),
        Q("8(a)", 2, r"""<p>Can two sodium vapour lamps act as coherent sources? Explain in brief.</p>""",
          a=r"""<p class="step"><b>No.</b> Light from a lamp is emitted by millions of atoms independently, in short wave
trains (about \(10^{-8}\) s long) with random phases. The phase difference between light from two independent
lamps therefore changes randomly and rapidly, so it is not constant: the lamps are incoherent and any
interference pattern shifts too fast to be seen (the screen is uniformly illuminated).</p>""",
          topic=WAVE, recall=r"""<ul><li>Coherent: same frequency, constant phase difference — obtained from one source (YDSE slits).</li></ul>"""),
        Q("8(b)", 3, r"""<p>i) The ratio of the intensities at the maxima and minima in an interference pattern is 25:9.
What will be the ratio of the widths of the two slits in the Young's experiment?<br>ii) What type of wave front
is generated from a line source of light?</p>""",
          a=r"""<p class="step">(i) \(\dfrac{I_{\max}}{I_{\min}} = \dfrac{(a_1+a_2)^2}{(a_1-a_2)^2} = \dfrac{25}{9}\Rightarrow
\dfrac{a_1+a_2}{a_1-a_2} = \dfrac53\Rightarrow a_1 = 4a_2\).</p>
<p class="step">Intensity from a slit ∝ its width ∝ \(a^2\): \(\dfrac{w_1}{w_2} = \dfrac{a_1^2}{a_2^2}\) =
<span class="box">16 : 1</span></p>
<p class="step">(ii) A line source gives a <span class="box">cylindrical</span> wavefront.</p>""",
          topic=WAVE, recall=r"""<ul><li>\(I\propto a^2\); \(I_{\max} = (a_1+a_2)^2\), \(I_{\min} = (a_1-a_2)^2\).</li>
<li>Point source → spherical; line source → cylindrical; distant source → plane wavefront.</li></ul>"""),
        Q("9(a)", 2, r"""<p>What is essential difference between polarized light and unpolarized light? Find Brewster's
angle for water having refractive index \(\mu = 1.33\).</p>""",
          excluded="Polarisation and Brewster's law — not in the ISC 2027 Wave Optics unit (Huygens' principle, "
                   "interference/YDSE and single-slit diffraction only)."),
        Q("9(b)", 3, r"""<p>Fraunhofer's diffraction from a single slit of width \(1.24\times10^{-6}\) m is observed with
light of wavelength 6200 Å. Calculate the angular width of the central maximum.</p>""",
          afig=F.fig_a9b_slit,
          a=r"""<p class="step">First minima at \(a\sin\theta = \lambda\):
\(\sin\theta = \dfrac{6.2\times10^{-7}}{1.24\times10^{-6}} = 0.5\Rightarrow\theta = 30^\circ\).</p>
<p class="step">Angular width of central maximum \(= 2\theta\) = <span class="box">60°</span> (\(\pi/3\) rad).</p>
<p class="note">Here \(\lambda/a = 0.5\) is not small, so use \(\sin\theta\), not the approximation
\(2\lambda/a = 1\) rad (57.3°).</p>{{fig:0}}""",
          topic=WAVE, recall=r"""<ul><li>Single slit minima: \(a\sin\theta_n = n\lambda\); central maximum spans \(-\theta_1\) to \(+\theta_1\).</li>
<li>Small angles: angular width \(2\lambda/a\).</li></ul>"""),
        Q("10(a)", 3, r"""<p>Deduce the relation \(\dfrac{\mu_2}{v} - \dfrac{\mu_1}{u} = \dfrac{\mu_2-\mu_1}{R}\) when
refraction takes place from rarer to denser medium \((\mu_2 > \mu_1)\) in case of a convex spherical surface and the
image formed is real.</p>""",
          afig=F.fig_a10a_refraction,
          a=r"""<p class="step">Let a convex surface (pole P, centre C, radius R) separate media \(\mu_1\) (object side) and
\(\mu_2\). A ray from the point object O meets the surface at N and is refracted to form the real image I. CN is the
normal at N; NM ⟂ axis. \(\alpha,\beta,\gamma\) are the angles made with the axis by ON, IN and CN.</p>{{fig:0}}
<p class="step">Exterior angles: in \(\triangle\)ONC, \(i = \alpha + \gamma\); in \(\triangle\)NCI, \(\gamma = r + \beta\Rightarrow r = \gamma - \beta\).</p>
<p class="step">Snell's law for small (paraxial) angles: \(\mu_1 i = \mu_2 r\Rightarrow \mu_1(\alpha+\gamma) = \mu_2(\gamma-\beta)\).</p>
<p class="step">For paraxial rays M ≈ P: \(\alpha \approx \dfrac{NM}{PO}\), \(\beta\approx\dfrac{NM}{PI}\), \(\gamma\approx\dfrac{NM}{PC}\).
Hence \(\dfrac{\mu_1}{PO} + \dfrac{\mu_2}{PI} = \dfrac{\mu_2-\mu_1}{PC}\).</p>
<p class="step">Sign convention (distances from P, positive in the direction of the incident light):
\(PO = -u\), \(PI = +v\), \(PC = +R\):</p>
<p><span class="box">\(\dfrac{\mu_2}{v} - \dfrac{\mu_1}{u} = \dfrac{\mu_2-\mu_1}{R}\)</span></p>""",
          topic=RAY, recall=r"""<ul><li>Snell's law \(\mu_1\sin i = \mu_2\sin r\); paraxial: \(\sin\theta\approx\tan\theta\approx\theta\).</li>
<li>Exterior angle of a triangle = sum of the interior opposite angles.</li></ul>"""),
        Q("10(b)", 2, r"""<p>A point object is placed at a distance of 12 cm on the axis of a convex lens of focal length
10 cm. On the other side of the lens; a convex mirror is placed at a distance of 10 cm from the lens such that the
image formed by the combination coincides with the object itself. What is the focal length of the convex
mirror?</p>""",
          afig=F.fig_a10b_lensmirror,
          a=r"""<p class="step">Lens: \(\dfrac1v - \dfrac1u = \dfrac1f\) with \(u = -12\), \(f = +10\):
\(\dfrac1v = \dfrac1{10} - \dfrac1{12} = \dfrac1{60}\Rightarrow v = +60\) cm.</p>
<p class="step">The image would form 60 − 10 = 50 cm behind the mirror. For the light to retrace its path (image
coinciding with the object), the rays must strike the mirror normally, i.e. head towards its centre of curvature.
So \(R = 50\) cm.</p>
<p class="step">\(f = R/2\) = <span class="box">25 cm</span></p>{{fig:0}}""",
          topic=RAY, recall=r"""<ul><li>Rays aimed at a mirror's centre of curvature strike it normally and retrace their path.</li>
<li>Thin lens \(\frac1v-\frac1u=\frac1f\); mirror \(f = R/2\).</li></ul>"""),
        Q("11(a)", 2, r"""<p>State two ways to minimize spherical aberration for a lens.</p>""",
          excluded="Spherical aberration (defects of images) — not in the ISC 2027 Optics unit."),
        Q("11(b)", 3, r"""<p>i) State how the resolving power of the astronomical telescope can be increased.<br>
ii) A compound microscope consists of an objective of focal length 2 cm and an eyepiece of focal length 5 cm.
When an object is placed 2.4 cm from the objective, final image is virtual and 25 cm from the eyepiece. Determine
the magnifying power of the compound microscope in this set up, i.e in normal use.</p>""",
          afig=F.fig_a11b_micro,
          a=r"""<p class="step">(i) Resolving power of a telescope \(= \dfrac{D}{1.22\lambda}\): increase the
<b>diameter (aperture) of the objective</b> — which is why large telescopes use big mirrors (reflecting
telescopes). (Using shorter wavelength also increases it.)</p>
<p class="note">ISC 2027 names "resolving power of compound microscope" and the advantages of the reflecting
telescope (large aperture); the telescope's resolving power is the same idea, so this part is kept.</p>
<p class="step">(ii) Objective: \(u_o = -2.4\), \(f_o = 2\): \(\dfrac1{v_o} = \dfrac12 - \dfrac1{2.4} = \dfrac1{12}\Rightarrow v_o = 12\) cm;
\(m_o = \dfrac{v_o}{u_o}\), \(|m_o| = \dfrac{12}{2.4} = 5\).</p>
<p class="step">Eyepiece with final image at \(D = 25\) cm: \(m_e = 1 + \dfrac{D}{f_e} = 1 + \dfrac{25}{5} = 6\)
(the intermediate image is \(u_e = 25\times5/30 = 4.17\) cm from it).</p>
<p class="step">\(M = m_o\,m_e = 5\times6\) = <span class="box">30</span></p>{{fig:0}}""",
          topic=RAY, recall=r"""<ul><li>Compound microscope (image at D): \(M = \dfrac{v_o}{u_o}\left(1+\dfrac{D}{f_e}\right)\).</li>
<li>Telescope resolving power ∝ aperture/λ.</li></ul>"""),

        SEC("Part II — Section C", "Answer any three questions from this section."),
        Q("12(a)", 3, r"""<p>In the experiment of photoelectric effect, the graph of maximum kinetic energy \(E_k\) of the
emitted photoelectrons versus the frequency \(\nu\) of the incident light is a straight line AB as shown in the figure
below, find:</p>{{fig:0}}<p>i) Threshold frequency of the metal. ii) Work function of the metal iii) Stopping
potential for the photoelectrons emitted by the light of frequency \(\nu = 30\times10^{14}\) Hz.</p>""",
          qfig=F.fig_q12a_graph, afig=F.fig_a12a_graph,
          a=r"""<p class="step">Einstein: \(E_k = h\nu - \phi_0\) — a straight line of slope \(h\), \(\nu\)-intercept \(\nu_0\)
and \(E_k\)-intercept \(-\phi_0\).</p>{{fig:0}}
<p class="step">(i) Line cuts the \(\nu\)-axis at A: <span class="box">\(\nu_0 = 10\times10^{14}\) Hz = \(1.0\times10^{15}\) Hz</span></p>
<p class="step">(ii) Extended back, the line meets the \(E_k\) axis at −4 eV: <span class="box">\(\phi_0 = 4\) eV</span>
(check: \(h\nu_0\) with slope \(\dfrac{8-0}{(30-10)\times10^{14}} = 0.4\) eV per \(10^{14}\) Hz gives 4 eV;
the slope is \(h = 6.4\times10^{-34}\) J s).</p>
<p class="step">(iii) At \(\nu = 30\times10^{14}\) Hz, \(E_k = 8\) eV (point B). \(eV_s = E_k\Rightarrow\)
<span class="box">\(V_s = 8\) V</span></p>""",
          topic=DUAL, recall=r"""<ul><li>\(K_{\max} = h\nu - \phi_0 = eV_s\); \(\phi_0 = h\nu_0\).</li>
<li>Slope of \(K_{\max}\)–\(\nu\) graph = \(h\), same for all metals.</li></ul>"""),
        Q("12(b)", 2, r"""<p>de-Broglie wavelength of electron of kinetic energy E is \(\lambda\). What will be its value
if K.E of electrons is made 4E?</p>""",
          a=r"""<p class="step">\(\lambda = \dfrac{h}{p} = \dfrac{h}{\sqrt{2mE}}\Rightarrow\lambda\propto\dfrac{1}{\sqrt E}\).</p>
<p class="step">\(\lambda' = \lambda\sqrt{\dfrac{E}{4E}}\) = <span class="box">\(\lambda/2\)</span></p>""",
          topic=DUAL, recall=r"""<ul><li>\(p = \sqrt{2mK}\); \(\lambda = h/\sqrt{2mK}\); for an electron through V volts \(\lambda = 1.227/\sqrt V\) nm.</li></ul>"""),
        Q("13(a)", 3, r"""<p>On the basis of Bohr's theory, derive an expression for the radius of the
n<sup>th</sup> orbit of an electron of hydrogen atom.</p>""",
          afig=F.fig_a13a_bohr,
          a=r"""<p class="step">Postulates used: (1) the electron moves in a circular orbit, the Coulomb attraction of the
nucleus providing the centripetal force; (2) only those orbits are allowed for which the angular momentum is an
integral multiple of \(h/2\pi\).</p>{{fig:0}}
<p class="step">(1) \(\dfrac{mv^2}{r} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{e^2}{r^2}\Rightarrow mv^2r = \dfrac{e^2}{4\pi\varepsilon_0}\) … (i)</p>
<p class="step">(2) \(mvr = \dfrac{nh}{2\pi}\Rightarrow v = \dfrac{nh}{2\pi mr}\) … (ii)</p>
<p class="step">Substitute (ii) in (i): \(m\dfrac{n^2h^2}{4\pi^2m^2r^2}\,r = \dfrac{e^2}{4\pi\varepsilon_0}\Rightarrow
\dfrac{n^2h^2}{4\pi^2 m r} = \dfrac{e^2}{4\pi\varepsilon_0}\)</p>
<p><span class="box">\(r_n = \dfrac{\varepsilon_0 n^2h^2}{\pi m e^2}\)</span> \(\;\propto n^2\); for \(n = 1\),
\(r_1 = 0.53\) Å (Bohr radius).</p>""",
          topic=ATOM, recall=r"""<ul><li>Bohr quantisation: \(mvr = nh/2\pi\).</li><li>Coulomb force = centripetal force.</li></ul>"""),
        Q("13(b)", 2, r"""<p>Using the constant given at the end of the question paper, find the minimum wavelength of the
emitted X-rays, when an X-ray tube is operated at 50 kV.</p>""",
          excluded="X-ray production / cut-off wavelength (Duane–Hunt) — not in the ISC 2027 syllabus; X-rays appear "
                   "only as a band of the electromagnetic spectrum."),
        Q("14(a)", 2, r"""<p>Using the equation \(N = N_0e^{-\lambda t}\), obtain the relation between half-life (T) and
decay constant \((\lambda)\) of a radioactive substance.</p>""",
          excluded="Radioactivity (decay law, half-life) — not in the ISC 2027 'Nuclei' unit, which covers "
                   "composition, mass defect, binding energy, fission and fusion only."),
        Q("14(b)", 3, r"""<p>In a star, three alpha particle fuse together to form \({}_6\mathrm{C}^{12}\) nucleus. Compute
the energy evolved. The masses of \(\alpha\)-particle and \({}_6\mathrm{C}^{12}\) 4.002604u and 12.000000u
respectively.</p>""",
          a=r"""<p class="step">\(3\,{}^4_2\mathrm{He}\to{}^{12}_6\mathrm{C} + Q\)</p>
<p class="step">Mass defect \(\Delta m = 3(4.002604) - 12.000000 = 12.007812 - 12.000000 = 0.007812\) u.</p>
<p class="step">\(Q = \Delta m\times931\) MeV \(= 0.007812\times931\) = <span class="box">7.27 MeV</span>
(\(\approx 1.16\times10^{-12}\) J).</p>""",
          topic=NUC, recall=r"""<ul><li>Energy released \(= (\text{mass of reactants} - \text{mass of products})\times931\) MeV/u.</li>
<li>Fusion of light nuclei releases energy (BE/A increases).</li></ul>"""),
        Q("15(a)(i)", 2, r"""<p>Draw a labelled diagram of a full wave rectifier. Show how output voltage varies with
time, if input voltage is a sinusoidal voltage.</p>
<p class="note">[The paper prints [3+2] for Q15: 3 marks for (a)(i) and (ii) together, split not printed. Taken here
as 2 for the diagram with waveforms and 1 for "what is modulation".]</p>""",
          afig=F.fig_a15a_fwr,
          a=r"""<p class="step">Centre-tap full-wave rectifier: the a.c. input is applied to the primary of a transformer
whose secondary has a centre tap T. The ends S₁, S₂ feed diodes D₁ and D₂, whose cathodes are joined; the load
\(R_L\) is connected between this junction and T.</p>{{fig:0}}
<p class="step">Positive half cycle: S₁ is positive w.r.t. T, D₁ is forward biased and conducts, D₂ is reverse
biased. Negative half cycle: S₂ is positive, D₂ conducts, D₁ is off.</p>
<p class="step">In both halves the current through \(R_L\) is in the <b>same direction</b>, so the output is a
unidirectional (pulsating d.c.) voltage with a hump in every half cycle — frequency twice the input frequency.</p>""",
          topic=ELEC, recall=r"""<ul><li>Forward-biased diode conducts; reverse-biased does not.</li>
<li>Half-wave: output only in alternate half cycles; full-wave: in both.</li></ul>"""),
        Q("15(a)(ii)", 1, r"""<p>What is modulation? Explain in brief.</p>""",
          excluded="Communication systems (modulation) — removed from the ISC syllabus; not in the ISC 2027 unit list."),
        Q("15(b)", 2, r"""<p>Why are NOR gates called the digital building blocks?</p>""",
          excluded="Logic gates — not in the ISC 2027 Electronic Devices unit (semiconductors, p-n junction, "
                   "rectifiers, LED/photodiode/solar cell, Zener diode only)."),
    ])
