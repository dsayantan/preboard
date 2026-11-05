"""Heritage School Pre-Board 2013-14, Physics Paper 1 (Theory) — digital copy, ISC 2027 filter, solutions.
Transcribed from the page images.  The scan has 6 pages; the page(s) carrying Q2(c) after its first line,
Q3, Q4, Q5 and Q6(a)-(b) are missing from the PDF, so those questions cannot be reproduced."""
from kit import Q, SEC
import physics_2013_14_figs as F

ES, CE, MAG = "Electrostatics", "Current Electricity", "Magnetic Effects of Current and Magnetism"
EMI, RAY, WAVE = "Electromagnetic Induction and Alternating Currents", "Optics — Ray Optics", "Optics — Wave Optics"
DUAL, ATOM, NUC, ELEC = ("Dual Nature of Radiation and Matter", "Atoms and Nuclei — Atoms",
                         "Atoms and Nuclei — Nuclei", "Electronic Devices")

MISSING = ('<p class="note">[The scanned paper is incomplete: the page after this one is missing, '
           'so the rest of Q2(c), Questions 3, 4 and 5, and Q6(a)–(b) are not available.]</p>')

PAPER = dict(
    subject="physics", year="2013-14", slug="2013-14", paper="Paper 1 (Theory)",
    source="PreBoard-PYQ/2013-14/Physics.pdf", marks=70, time="3 hours",
    intro=r"""<p><i>Candidates are allowed additional 15 minutes only for reading the paper. They must NOT start
writing during this time.</i></p>
<p>Answer all questions in Part I and eight questions in Part II, choosing two questions from Section A and two
questions from each of the section B and C.</p>
<p>All work including rough work, should be done on the same sheet as, and adjacent to, the rest of the answer.
The intended marks for questions or parts of a question are given in brackets [ ]. Calculator of capacity FX-82
may be used. A list of useful physical constants is given at the end of this paper.</p>
<p><b>Useful constants and relations</b> (as printed): electron charge \(e = 1.6\times10^{-19}\) C; Planck's
constant \(h = 6.6\times10^{-34}\) J s; speed of light \(c = 3\times10^{8}\) m/s;
\(\varepsilon_0 = 8.85\times10^{-12}\) F/m; \(\mu_0 = 4\pi\times10^{-7}\) T m A\(^{-1}\); mass of an electron
\(= 9\times10^{-31}\) kg.</p>
<p class="note">[The paper's instructions disagree with each other: the cover says "eight questions in Part II",
Part II itself says "six questions … two from each Section A, B and C". Six (2 + 2 + 2) matches the 50 marks.
The scan is missing a page: Q2(c) after its first line, Questions 3–5 and Q6(a)–(b) are not available.]</p>""",
    items=[
        SEC("Part I (20 marks) — Question 1 A) Choose the correct answer [5]", "Answer all questions."),
        Q("1(A)(i)", 1, r"""<p>When a charged particle is projected perpendicular to a uniform magnetic field, it describes
a circular path in which:</p><p>(a) Its speed remains constant &nbsp; (b) Its velocity remains constant &nbsp;
(c) Its momentum remains constant &nbsp; (d) Its kinetic energy increases.</p>""",
          a=r"""<p><b>(a) Its speed remains constant.</b></p>
<p class="step">The magnetic force \(\vec F = q\,\vec v\times\vec B\) is always perpendicular to \(\vec v\), so it does
no work: kinetic energy and hence speed stay constant. The direction of \(\vec v\) (and of \(\vec p\)) keeps
changing, so velocity and momentum are not constant.</p>""",
          topic=MAG, recall=r"<ul><li>\(\vec F=q\vec v\times\vec B\perp\vec v\) ⇒ work done = 0.</li><li>Radius \(r = mv/qB\).</li></ul>"),
        Q("1(A)(ii)", 1, r"""<p>The dimensions of Planck's constant are:</p>
<p>(a) \(\mathrm{ML^2T^{-3}}\) &nbsp; (b) \(\mathrm{ML^2T^{-2}}\) &nbsp; (c) \(\mathrm{ML^2T^{-1}}\) &nbsp; (d) \(\mathrm{MLT^{-3}}\)</p>""",
          a=r"""<p><b>(c) \(\mathrm{ML^2T^{-1}}\)</b></p>
<p class="step">\(E = h\nu \Rightarrow [h] = [E]/[\nu] = \mathrm{ML^2T^{-2}}/\mathrm{T^{-1}} = \mathrm{ML^2T^{-1}}\)
(same as angular momentum).</p>""",
          topic=DUAL, recall=r"<ul><li>\(E=h\nu\); \([E]=\mathrm{ML^2T^{-2}}\).</li><li>h has the dimensions of angular momentum (J s).</li></ul>"),
        Q("1(A)(iii)", 1, r"""<p>The self inductance of a straight conductor is:</p>
<p>(a) 0 &nbsp; (b) Infinite &nbsp; (c) Very large &nbsp; (d) Very small</p>""",
          a=r"""<p><b>(d) Very small.</b></p>
<p class="step">A straight wire has no turns, so the magnetic flux it links with itself per unit current is very
small; its self-inductance is tiny (of the order of \(10^{-6}\) H per metre) but not exactly zero. Coiling the
wire into many turns is what makes \(L\) large (\(L = \mu_0 N^2A/l\)).</p>
<p class="note">Some question banks give (a) 0 for this item, treating a straight wire as linking no flux. That is an
idealisation: a current in a straight wire does set up circular field lines round it, so its self-inductance is
small but not zero. (d) is the physically correct choice.</p>""",
          topic=EMI, recall=r"<ul><li>\(\phi = LI\); \(L\) depends on geometry (turns, area, length) and core.</li><li>Solenoid: \(L=\mu_0N^2A/l\).</li></ul>"),
        Q("1(A)(iv)", 1, r"""<p>In which state a substance emits a line spectra?</p>
<p>(a) Molecular State &nbsp; (b) Atomic State &nbsp; (c) Solid State &nbsp; (d) Liquid state</p>""",
          a=r"""<p><b>(b) Atomic state.</b></p>
<p class="step">Isolated atoms (e.g. a gas at low pressure) have discrete energy levels, so the photons emitted
in transitions have definite wavelengths — a line spectrum. Molecules give band spectra; solids and liquids give
continuous spectra.</p>""",
          topic=ATOM, recall=r"<ul><li>Line spectrum ← discrete atomic energy levels, \(h\nu = E_i - E_f\).</li><li>Molecules → bands; hot solids → continuous.</li></ul>"),
        Q("1(A)(v)", 1, r"""<p>A wire of resistance R is cut into ten equal parts which are then joined in parallel. The new
resistance is:</p><p>(a) 0.01R &nbsp; (b) 0.1R &nbsp; (c) 10R &nbsp; (d) 100R</p>""",
          a=r"""<p><b>(a) 0.01R</b></p>
<p class="step">Each piece has resistance \(R/10\). Ten equal resistances in parallel:
\(R_p = \dfrac{R/10}{10} = \dfrac{R}{100} = 0.01R\).</p>""",
          topic=CE, recall=r"<ul><li>\(R\propto l\) for a uniform wire.</li><li>n equal resistors r in parallel: \(r/n\).</li></ul>"),

        SEC("Question 1 — B) Answer all questions briefly and to the point [15]"),
        Q("1(B)(i)", 1, r"""<p>A point charge of \(5\times10^{-6}\) C experiences a force of \(2\times10^{-3}\) N when kept in a
uniform electric field of intensity E. Find E.</p>""",
          a=r"""<p class="step">\(E = \dfrac{F}{q} = \dfrac{2\times10^{-3}}{5\times10^{-6}}\)</p>
<p class="step"><span class="box">\(E = 400\ \mathrm{N\,C^{-1}}\)</span></p>""",
          topic=ES, recall=r"<ul><li>\(\vec E = \vec F/q_0\); unit N C\(^{-1}\) = V m\(^{-1}\).</li></ul>"),
        Q("1(B)(ii)", 1, r"""<p>Write an expression of magnetic flux density 'B' at a point in end-on position or an axial position
of a magnetic dipole. (Derivation <b>not</b> required.)</p>""",
          a=r"""<p class="step">At distance \(r\) from the centre of a short magnetic dipole of moment \(m\), on its axis
(\(r \gg l\)):</p>
<p class="step"><span class="box">\(B_{\text{axial}} = \dfrac{\mu_0}{4\pi}\,\dfrac{2m}{r^3}\)</span>, directed along \(\vec m\).</p>
<p class="step">(For a magnet of length \(2l\): \(B = \dfrac{\mu_0}{4\pi}\dfrac{2mr}{(r^2-l^2)^2}\).)</p>""",
          topic=MAG, recall=r"<ul><li>Axial: \(\frac{\mu_0}{4\pi}\frac{2m}{r^3}\); equatorial: \(\frac{\mu_0}{4\pi}\frac{m}{r^3}\) (opposite to \(\vec m\)).</li><li>Same form as the electric dipole with \(\frac{1}{4\pi\varepsilon_0}\to\frac{\mu_0}{4\pi}\).</li></ul>"),
        Q("1(B)(iii)", 1, r"""<p>In a moving coil galvanometer, what is meant by a radial magnetic field?</p>""",
          a=r"""<p class="step">A field whose lines are along the radii of the cylindrical soft-iron core, produced by
concave (cylindrical) pole pieces with the core at their centre. The plane of the coil therefore always lies
<b>along</b> the field in every position, so the angle between \(\vec m\) and \(\vec B\) is always 90° and the
deflecting torque is \(\tau = NIAB\) (maximum, independent of deflection) — giving \(I\propto\theta\), a linear
scale.</p>{{fig:0}}""",
          afig=[(F.fig_a1b3_radial, "Concave pole pieces and a soft-iron core make the field radial in the gap.")],
          topic=MAG, recall=r"<ul><li>\(\tau = NIAB\sin\phi\), φ between normal and B.</li><li>Radial field ⇒ φ = 90° always ⇒ \(NIAB = k\theta\).</li></ul>"),
        Q("1(B)(iv)", 1, r"""<p>Variation of alternating current 'I' with time t is shown in the graph below:</p>{{fig:0}}
<p>What is the rms value of this current?</p>""",
          qfig=[F.fig_q1b4_ac],
          a=r"""<p class="step">Peak value from the graph: \(I_0 = 5\sqrt2\) A (sinusoidal).</p>
<p class="step">\(I_{\text{rms}} = \dfrac{I_0}{\sqrt2} = \dfrac{5\sqrt2}{\sqrt2}\) ⇒ <span class="box">\(I_{\text{rms}} = 5\ \mathrm{A}\)</span></p>""",
          topic=EMI, recall=r"<ul><li>Sinusoidal: \(I_{\rm rms}=I_0/\sqrt2\approx0.707\,I_0\).</li><li>Mean over a half cycle: \(2I_0/\pi\).</li></ul>"),
        Q("1(B)(v)", 1, r"""<p>Threshold frequency of a certain metal for photo-electric emission is \(5\times10^{14}\) Hz.
Calculate its work function.</p>""",
          a=r"""<p class="step">\(W_0 = h\nu_0 = 6.6\times10^{-34}\times5\times10^{14} = 3.3\times10^{-19}\ \mathrm{J}\)</p>
<p class="step">In eV: \(3.3\times10^{-19}/1.6\times10^{-19}\) ⇒ <span class="box">\(W_0 = 3.3\times10^{-19}\ \mathrm J \approx 2.06\ \mathrm{eV}\)</span></p>""",
          topic=DUAL, recall=r"<ul><li>\(W_0 = h\nu_0 = hc/\lambda_0\).</li><li>1 eV = \(1.6\times10^{-19}\) J.</li></ul>"),
        Q("1(B)(vi)", 1, r"""<p>What conclusion was drawn by <b>Rutherford</b> based on <b>Geiger-Marsden's</b> experiment on
scattering of alpha particles?</p>""",
          a=r"""<p class="step">Most α-particles passed undeflected, so most of the atom is empty space; a very few were
deflected through large angles (some > 90°), so the entire positive charge and almost all the mass of the atom is
concentrated in a tiny central <b>nucleus</b> (radius \(\sim10^{-15}\) m, about \(10^{-5}\) of the atomic size),
with the electrons revolving around it.</p>""",
          topic=ATOM, recall=r"<ul><li>Large-angle scattering needs a massive, tiny, positive centre.</li><li>Distance of closest approach: \(r_0 = \frac{2Ze^2}{4\pi\varepsilon_0 K}\).</li></ul>"),
        Q("1(B)(vii)", 1, r"""<p>Write a balanced nuclear reaction showing emission of \(\beta^-\) particle by \(^{234}\mathrm{Th}_{90}\).
(Symbol of daughter nucleus formed in the process is Pa)</p>""",
          a=r"""<p class="step">In β⁻ emission a neutron in the nucleus changes into a proton, an electron (the β⁻ particle) and an
antineutrino: \(n \rightarrow p + e^- + \bar\nu\). So the mass number A is unchanged and the atomic number Z rises by 1.</p>
<p class="step"><span class="box">\({}^{234}_{\ 90}\mathrm{Th} \;\rightarrow\; {}^{234}_{\ 91}\mathrm{Pa} + {}^{\ \ 0}_{-1}e + \bar\nu\)</span></p>
<p class="step">Check: A: 234 = 234 + 0; Z: 90 = 91 + (−1). Both are conserved, so the equation is balanced.</p>
<p class="note">ISC 2027 dropped radioactivity as a topic (no decay law, half-life or activity). Balancing a nuclear
reaction equation by conserving A and Z is still examinable under "Nuclear reactions" in the Nuclei unit, which is why
this item is kept.</p>""",
          topic=NUC, recall=r"<ul><li>In any nuclear reaction the total mass number A and the total charge (atomic number) Z are conserved.</li><li>Electron: \({}^{\ \ 0}_{-1}e\); α: \({}^4_2\mathrm{He}\); neutron: \({}^1_0n\); proton: \({}^1_1p\).</li><li>β⁻: A same, Z + 1.</li></ul>"),
        Q("1(B)(viii)", 1, r"""<p>What is the essential difference between the working of a nuclear reactor and that of a fission
bomb?</p>""",
          a=r"""<p class="step">Both use a fission chain reaction. In a <b>reactor</b> the chain reaction is
<b>controlled</b>: control rods (Cd/B) absorb surplus neutrons so that on average exactly one neutron from each
fission causes a further fission (multiplication factor \(k = 1\)); energy is released steadily.</p>
<p class="step">In a <b>fission bomb</b> the chain reaction is <b>uncontrolled</b> (\(k > 1\)): the number of
fissions multiplies in each generation and an enormous energy is released in a fraction of a second —
an explosion.</p>""",
          topic=NUC, recall=r"<ul><li>Multiplication factor k: = 1 critical (reactor), > 1 supercritical (bomb).</li><li>Moderator slows neutrons; control rods absorb them.</li></ul>"),
        Q("1(B)(ix)", 1, r"""<p>State one important use of <b>Zener</b> diode.</p>""",
          a=r"""<p class="step">As a <b>voltage regulator</b>: operated in reverse breakdown, the voltage across a Zener diode
stays constant (= \(V_Z\)) over a wide range of current, so the load connected across it gets a steady d.c. voltage
even when the input voltage or the load current varies.</p>""",
          topic=ELEC, recall=r"<ul><li>Zener: heavily doped, used in reverse bias at breakdown.</li><li>Series resistor drops the excess input voltage.</li></ul>"),
        Q("1(B)(x)", 1, r"""<p>In a Young's double slit experiment, the angular width of a fringe formed on a distant screen is 0.1°.
The wavelength of light used is 6000 Å. Find the spacing between the slits.</p>""",
          a=r"""<p class="step">Angular fringe width \(\theta = \beta/D = \lambda/d\) ⇒ \(d = \lambda/\theta\).</p>
<p class="step">\(\theta = 0.1° = 0.1\times\dfrac{\pi}{180} = 1.745\times10^{-3}\) rad; \(\lambda = 6000\) Å \(= 6\times10^{-7}\) m.</p>
<p class="step">\(d = \dfrac{6\times10^{-7}}{1.745\times10^{-3}}\) ⇒ <span class="box">\(d \approx 3.44\times10^{-4}\ \mathrm m = 0.344\ \mathrm{mm}\)</span></p>""",
          topic=WAVE, recall=r"<ul><li>Fringe width \(\beta = \lambda D/d\); angular width \(\lambda/d\).</li><li>Convert degrees to radians.</li></ul>"),
        Q("1(B)(xi)", 1, r"""<p>How many lines per metre are there in a grating which gives an angle of diffraction equal to 30° in
the first order of light of wavelength \(6\times10^{-7}\) m?</p>""",
          excluded="Diffraction grating — not in ISC 2027: Wave Optics lists only 'Fraunhofer diffraction due to a single slit' (a sin θ = nλ); a grating appears nowhere in the syllabus."),
        Q("1(B)(xii)", 1, r"""<p>On what factors does the angular dispersion of a prism depend?</p>""",
          a=r"""<p class="step">For a thin prism, angular dispersion \(\delta_V-\delta_R = (\mu_V-\mu_R)A\). It depends on</p>
<p class="step">(1) the <b>angle of the prism</b> A, and (2) the <b>material</b> of the prism, through the
difference \(\mu_V-\mu_R\) of its refractive indices for the extreme colours (i.e. on the wavelengths considered).</p>""",
          topic=RAY, recall=r"<ul><li>Thin prism: \(\delta = (\mu-1)A\).</li><li>Dispersive power \(\omega = \frac{\mu_V-\mu_R}{\mu_Y-1}\) — independent of A.</li></ul>"),
        Q("1(B)(xiii)", 1, r"""<p>For an achromatic combination of two lenses in contact, why should the lenses be of opposite
nature?</p>""",
          excluded="Achromatic combination of lenses — not in ISC 2027: Optics 6(c) lists only 'Dispersion; Angular dispersion; dispersive power, rainbow'; achromatism (ω₁/f₁ + ω₂/f₂ = 0) is not listed."),
        Q("1(B)(xiv)", 1, r"""<p>In a compound microscope consisting of two convex lenses of focal lengths 1.5 cm and 10 cm, the object
is 2 cm from the objective and the final image is formed at the least distance of distinct vision (D = 25 cm).
Find the distance of separation of the two lenses.</p>""",
          a=r"""<p class="step">Objective (\(f_o = 1.5\) cm, \(u = -2\) cm): \(\dfrac1v-\dfrac1u=\dfrac1f\Rightarrow\dfrac1{v_o}=\dfrac1{1.5}-\dfrac12=\dfrac16\Rightarrow v_o = 6\) cm.</p>
<p class="step">Eyepiece (\(f_e=10\) cm, image at \(v_e=-25\) cm): \(\dfrac1{u_e}=\dfrac1{v_e}-\dfrac1{f_e}=-\dfrac1{25}-\dfrac1{10}=-\dfrac{7}{50}\Rightarrow u_e=-7.14\) cm.</p>
<p class="step">Separation \(L = v_o + |u_e| = 6 + 7.14\) ⇒ <span class="box">\(L \approx 13.1\ \mathrm{cm}\)</span></p>""",
          topic=RAY, recall=r"<ul><li>Lens formula \(\frac1v-\frac1u=\frac1f\) (Cartesian signs).</li><li>Tube length = image distance of objective + object distance of eyepiece.</li></ul>"),
        Q("1(B)(xv)", 1, r"""<p>The size of the moon is much smaller than stars, still it appears bigger. Why?</p>""",
          a=r"""<p class="step">The apparent size of an object depends on the <b>visual angle</b> it subtends at the eye,
not on its actual size. The moon is very near (\(\approx3.8\times10^{5}\) km) and subtends about 0.5°, while a
star, though enormously larger, is so far away that it subtends a vanishingly small angle. Hence the moon looks
bigger.</p>{{fig:0}}""",
          afig=[F.fig_a1b15_visual_angle],
          topic=RAY, recall=r"<ul><li>Visual angle ≈ size/distance (radians).</li><li>Optical instruments work by increasing the visual angle.</li></ul>"),

        SEC("Part II (50 marks) — Section A", "Answer six questions in this part, choosing two questions from each Section A, B and C. Section A: answer any two questions."),
        Q("2(a)", 4, r"""<p>With the help of a labelled diagram, obtain an expression for the electric field intensity 'E' at a
point P in broad side position (i.e. equatorial plane) of an electric dipole.</p>""",
          a=r"""<p class="step">Dipole: charges \(-q\) at A and \(+q\) at B, \(AB = 2l\), dipole moment \(p = q\cdot2l\)
directed from \(-q\) to \(+q\). P is on the perpendicular bisector at distance \(r\) from the centre O.</p>{{fig:0}}
<p class="step">Distance of P from each charge \(= \sqrt{r^2+l^2}\), so the magnitudes are equal:</p>
\[E_+ = E_- = \frac{1}{4\pi\varepsilon_0}\,\frac{q}{r^2+l^2}\]
<p class="step">\(\vec E_+\) points along BP (away from +q); \(\vec E_-\) points along PA (towards −q).
Resolve each along and perpendicular to the axis. The components perpendicular to AB (\(E\sin\theta\)) are equal
and opposite and cancel. The components parallel to AB (\(E\cos\theta\)) are both directed from +q towards −q and add:</p>
\[E = E_+\cos\theta + E_-\cos\theta = 2\,\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2+l^2}\cdot\frac{l}{\sqrt{r^2+l^2}}\qquad\left(\cos\theta=\frac{l}{\sqrt{r^2+l^2}}\right)\]
\[E = \frac{1}{4\pi\varepsilon_0}\,\frac{q\,(2l)}{(r^2+l^2)^{3/2}} = \frac{1}{4\pi\varepsilon_0}\,\frac{p}{(r^2+l^2)^{3/2}}\]
<p class="step">Direction: parallel to the axis, from +q towards −q, i.e. <b>opposite to \(\vec p\)</b>.</p>
<p class="step">For a short dipole (\(r\gg l\)): <span class="box">\(\vec E = -\dfrac{1}{4\pi\varepsilon_0}\dfrac{\vec p}{r^3}\)</span></p>""",
          afig=[(F.fig_a2a_dipole_equatorial, "E₊ points away from +q, E₋ towards −q; the components ⟂ to the axis cancel.")],
          topic=ES, recall=r"<ul><li>Field of a point charge \(kq/r^2\); add vectorially.</li><li>Equatorial field is half the axial field (\(2kp/r^3\)) and antiparallel to \(\vec p\).</li></ul>"),
        Q("2(b)", 2, r"""<p>Find the electric charge \(Q_1\) on plates of capacitor \(C_1\) shown in the figure below:</p>{{fig:0}}""",
          qfig=[F.fig_q2b_caps],
          a=r"""<p class="step">The three capacitors are in series, so each carries the same charge as the equivalent capacitor.</p>
\[\frac1C=\frac18+\frac1{16}+\frac1{24}=\frac{6+3+2}{48}=\frac{11}{48}\ \mu\mathrm F^{-1}\ \Rightarrow\ C=\frac{48}{11}\ \mu\mathrm F\]
<p class="step">\(Q = CV = \dfrac{48}{11}\times110\ \mu\mathrm C\) ⇒ <span class="box">\(Q_1 = 480\ \mu\mathrm C = 4.8\times10^{-4}\ \mathrm C\)</span></p>""",
          topic=ES, recall=r"<ul><li>Series: same Q, \(1/C=\sum1/C_i\).</li><li>Parallel: same V, \(C=\sum C_i\).</li></ul>"),
        Q("2(c)(i)(1)", 1, r"""<p>(c) (i) What is meant by: (1) Drift velocity and … <i>[the rest of Q2(c), carrying 3 marks in all,
is on the missing page]</i></p>""" + MISSING,
          a=r"""<p class="step"><b>Drift velocity</b> is the average velocity with which the free electrons in a conductor
drift (opposite to the field) when an electric field is applied across it. Superposed on their random thermal
motion, the electrons acquire a small net velocity
\(\vec v_d = -\dfrac{e\vec E}{m}\tau\) (τ = relaxation time). It is related to the current by
<span class="box">\(I = neAv_d\)</span>; typically \(v_d\sim10^{-4}\ \mathrm{m\,s^{-1}}\).</p>
<p class="note">Only this part of Q2(c) survives in the scan; its mark share is not known.</p>""",
          topic=CE, recall=r"<ul><li>\(v_d = eE\tau/m\); mobility \(\mu = v_d/E\).</li><li>\(I = neAv_d\); \(\rho = m/ne^2\tau\).</li></ul>"),

        SEC("Section B", "[Heading lost with the missing page. Q6(c) is the first question that survives in this section.]"),
        Q("6(c)", 3, r"""<p>A thin biconvex lens of refractive index 3/2 is placed on a horizontal plane mirror as shown below. The
space between the lens and the mirror is then filled with water of refractive index 4/3. It is found that when a
point object is placed 15 cm above the lens on its principal axis, the object coincides with its own image. On
repeating with another liquid, the object and the image again coincide at a distance 25 cm from the lens.
Calculate the refractive index of the liquid.</p>{{fig:0}}""",
          qfig=[F.fig_q6c_lens_mirror],
          a=r"""<p class="step"><b>Principle.</b> The object coincides with its own image when the rays, after passing
through the lens system, fall <b>normally</b> on the plane mirror and retrace their path — i.e. when the object is
at the focus of the combined system. So the object distance equals the focal length of the combination of the
glass lens and the liquid between lens and mirror.</p>{{fig:0}}
<p class="step">The liquid forms a <b>plano-concave lens</b> whose curved face has the radius R of the lower face
of the glass lens (taken as an equiconvex lens of radii R).</p>
<p class="step">Glass lens: \(\dfrac1{f_1}=(\mu_g-1)\left(\dfrac1R+\dfrac1R\right)=\left(\tfrac32-1\right)\dfrac2R=\dfrac1R\)</p>
<p class="step">Water lens: \(\dfrac1{f_2}=(\mu_w-1)\left(-\dfrac1R+\dfrac1\infty\right)=-\dfrac{1}{3R}\)</p>
<p class="step">Combination: \(\dfrac1{15}=\dfrac1R-\dfrac1{3R}=\dfrac{2}{3R}\Rightarrow R = 10\) cm (so \(f_1 = 10\) cm).</p>
<p class="step">With the liquid of index μ: \(\dfrac1{25}=\dfrac1{10}-\dfrac{\mu-1}{10}\Rightarrow\mu-1 = 10\left(\dfrac1{10}-\dfrac1{25}\right)=0.6\)</p>
<p class="step"><span class="box">\(\mu_{\text{liquid}} = 1.6\)</span></p>""",
          afig=[(F.fig_a6c_liquid_lens, "Rays leave the system parallel to the axis, hit the mirror normally and return: O ≡ I.")],
          topic=RAY, recall=r"<ul><li>Lens maker: \(\frac1f=(\mu-1)\left(\frac1{R_1}-\frac1{R_2}\right)\).</li><li>Lenses in contact: \(\frac1F=\frac1{f_1}+\frac1{f_2}\).</li><li>Object = own image on a plane mirror ⇒ object at the focus.</li></ul>"),
        Q("7(a)", 2, r"""<p>Two students are separated by a 7 m partition wall in a room 10 m high. If both light and sound
waves can bend around obstacles, how is it that the students are unable to see each other even though they can
converse easily?</p>""",
          a=r"""<p class="step">Bending (diffraction) is appreciable only when the size of the obstacle/opening is
comparable to the wavelength.</p>
<p class="step">Sound waves of speech have wavelengths of about 0.3 m to a few metres, comparable with the 3 m gap
above the 7 m wall, so sound diffracts round the wall and is heard.</p>
<p class="step">Light has \(\lambda\approx5\times10^{-7}\) m, about \(10^{-7}\) times the size of the wall; its
diffraction is negligible and it travels in practically straight lines, so the wall casts a sharp shadow and the
students cannot see each other.</p>""",
          topic=WAVE, recall=r"<ul><li>Diffraction significant when \(a\sim\lambda\); angular spread \(\sim\lambda/a\).</li></ul>"),
        Q("7(b)", 3, r"""<p>Consider interference between waves from the two sources of intensities I and 4I. Find intensities
at points where the phase difference is (a) π/2 (b) π</p>""",
          a=r"""<p class="step">For two coherent waves, \(I_R = I_1 + I_2 + 2\sqrt{I_1I_2}\cos\phi\), with
\(I_1 = I,\ I_2 = 4I,\ 2\sqrt{I_1I_2} = 4I\).</p>
<p class="step">(a) \(\phi = \pi/2\): \(\cos\phi = 0\) ⇒ <span class="box">\(I_R = I + 4I = 5I\)</span></p>
<p class="step">(b) \(\phi = \pi\): \(\cos\phi = -1\) ⇒ \(I_R = 5I - 4I\) ⇒ <span class="box">\(I_R = I\)</span></p>""",
          topic=WAVE, recall=r"<ul><li>\(I\propto a^2\); \(I_R = I_1+I_2+2\sqrt{I_1I_2}\cos\phi\).</li><li>\(I_{\max}=(\sqrt{I_1}+\sqrt{I_2})^2\), \(I_{\min}=(\sqrt{I_1}-\sqrt{I_2})^2\).</li></ul>"),
        Q("7(c)", 3, r"""<p>Briefly describe how a given beam of light can be analysed and determined if it is linearly polarised
or unpolarised. What is double refraction?</p>""",
          excluded="Polarisation and double refraction — not in ISC 2027: Wave Optics covers Huygens' principle, interference (YDSE) and single-slit diffraction; polarisation occurs only as a word in Unit 7 ('wave nature … exhibited in interference, diffraction and polarisation'), with no Polaroid, Malus, Brewster or double refraction."),

        SEC("Section C", "(Answer any two questions)"),
        Q("8(a)", 2, r"""<p>Electrons having a velocity v of \(2\times10^{-6}\ \mathrm{ms^{-1}}\) pass undeviated through a uniform
electric field E of intensity \(5\times10^{4}\ \mathrm{Vm^{-1}}\) and a uniform magnetic field B.</p>
<p>i) Find the magnitude of magnetic flux density B of the magnetic fields.</p>
<p>ii) What is the direction of B, if v is towards right and E is vertically downwards in the plane of this paper?</p>
<p class="note">[The paper prints \(2\times10^{-6}\) m s\(^{-1}\); this is evidently a misprint for
\(2\times10^{6}\) m s\(^{-1}\) — the given value would need B ≈ \(2.5\times10^{10}\) T. Solved with \(2\times10^{6}\) m s\(^{-1}\).]</p>""",
          a=r"""<p class="step">(i) Undeviated ⇒ electric and magnetic forces are equal and opposite: \(eE = evB\).</p>
<p class="step">\(B = \dfrac Ev = \dfrac{5\times10^4}{2\times10^6}\) ⇒ <span class="box">\(B = 2.5\times10^{-2}\ \mathrm T\)</span></p>
<p class="step">(ii) The electron is negative, so the electric force on it is opposite to \(\vec E\): <b>upwards</b>.
The magnetic force \(-e(\vec v\times\vec B)\) must therefore be downwards, i.e. \(\vec v\times\vec B\) upwards.
With \(\vec v\) to the right this requires <span class="box">\(\vec B\) perpendicular to the paper, into the page</span>.</p>{{fig:0}}""",
          afig=[F.fig_a8a_selector],
          topic=MAG, recall=r"<ul><li>Velocity selector: \(qE = qvB\Rightarrow v = E/B\).</li><li>\(\vec F = q(\vec E+\vec v\times\vec B)\); reverse the direction for an electron.</li></ul>"),
        Q("8(b)", 3, r"""<p>Monochromatic light of wavelength 198 nm is incident on the surface of a metal, whose work function is
2.5 eV. Calculate the <b>stopping potential</b>.</p>""",
          a=r"""<p class="step">Photon energy \(E = \dfrac{hc}{\lambda} = \dfrac{6.6\times10^{-34}\times3\times10^{8}}{198\times10^{-9}} = 1.0\times10^{-18}\ \mathrm J = \dfrac{1.0\times10^{-18}}{1.6\times10^{-19}} = 6.25\ \mathrm{eV}\)</p>
<p class="step">Einstein: \(eV_0 = K_{\max} = h\nu - W_0 = 6.25 - 2.5 = 3.75\ \mathrm{eV}\)</p>
<p class="step"><span class="box">\(V_0 = 3.75\ \mathrm V\)</span></p>""",
          topic=DUAL, recall=r"<ul><li>\(eV_0 = h\nu - W_0\).</li><li>\(E(\mathrm{eV}) \approx 1240/\lambda(\mathrm{nm})\).</li></ul>"),
        Q("8(c)", 3, r"""<p>Energy levels of H atom are given by: \(E_n = -13.6/n^2\) eV, where n is Principal Quantum number.
Calculate the wavelength of electromagnetic radiation by hydrogen atom resulting from the transition: n = 2 to n = 1.</p>""",
          a=r"""<p class="step">\(\Delta E = E_2 - E_1 = -\dfrac{13.6}{4} - \left(-13.6\right) = 10.2\ \mathrm{eV} = 10.2\times1.6\times10^{-19} = 1.632\times10^{-18}\ \mathrm J\)</p>
<p class="step">\(\lambda = \dfrac{hc}{\Delta E} = \dfrac{6.6\times10^{-34}\times3\times10^{8}}{1.632\times10^{-18}}\)</p>
<p class="step"><span class="box">\(\lambda \approx 1.21\times10^{-7}\ \mathrm m = 121\ \mathrm{nm}\)</span> (ultraviolet; first line of the Lyman series)</p>{{fig:0}}""",
          afig=[F.fig_a8c_levels],
          topic=ATOM, recall=r"<ul><li>\(h\nu = E_i - E_f\), \(\lambda = hc/\Delta E\).</li><li>Transitions to n = 1: Lyman (UV); to n = 2: Balmer (visible).</li></ul>"),
        Q("9(a)", 3, r"""<p>(i) What is <b>Compton</b> effect?</p><p>(ii) In Coolidge X-Ray tube (Modern X-Ray tube) how will you vary:
(1) Intensity of emitted X-Rays? (2) Penetrating power of emitted X-Rays?</p>""",
          excluded="Compton effect and the Coolidge X-ray tube — not in ISC 2027: Unit 7 covers only the photoelectric effect and matter waves; X-rays appear only as a band of the EM spectrum (Unit 5, 'elementary facts' of source, detection and uses), not the X-ray tube and the control of intensity and hardness, which belonged to the deleted X-rays section."),
        Q("9(b)", 3, r"""<p>Complete the following table for a radioactive element whose half life is 5 minutes. Assume that you
have 32 g of this element at start, i.e. at t = 0.</p>
<div class="tbl"><table><tr><th>Time 't' in minutes</th><td>0</td><td>5</td><td>10</td><td>15</td><td>20</td><td>25</td></tr>
<tr><th>Amount of radioactive element left in grams</th><td>32</td><td></td><td></td><td></td><td></td><td></td></tr></table></div>
<p>Now, using this data. Plot the "decay curve".</p>""",
          excluded="Radioactive decay law, half-life and decay curve — not in ISC 2027: the Nuclei unit lists composition and size, mass defect and binding energy, nuclear reactions, fission and fusion; 'decay', 'half-life' and 'activity' occur nowhere in the syllabus."),
        Q("9(c)", 2, r"""<p>Calculate the energy released when an electron <b>annihilates</b> a positron.</p>""",
          a=r"""<p class="step">\(e^- + e^+ \rightarrow 2\gamma\); the whole rest mass \(2m_e\) is converted into energy.</p>
<p class="step">\(E = 2m_ec^2 = 2\times9\times10^{-31}\times(3\times10^{8})^2 = 1.62\times10^{-13}\ \mathrm J\)</p>
<p class="step">\(= \dfrac{1.62\times10^{-13}}{1.6\times10^{-19}}\ \mathrm{eV}\) ⇒ <span class="box">\(E \approx 1.62\times10^{-13}\ \mathrm J \approx 1.01\ \mathrm{MeV}\)</span></p>
<p class="note">With the accurate mass \(9.11\times10^{-31}\) kg the value is 1.02 MeV (0.511 MeV per particle).</p>""",
          topic=NUC, recall=r"<ul><li>\(E = mc^2\); \(m_ec^2 = 0.511\) MeV.</li><li>Annihilation gives two γ-photons (momentum conservation).</li></ul>"),
        Q("10(a)", 3, r"""<p>Draw a labelled <b>energy band diagram</b> for a solid which is an <b>insulator</b>. What is the main
difference between the diagram and that of a semi-conductor?</p>""",
          a=r"""{{fig:0}}<p class="step">In an insulator the valence band is completely filled, the conduction band is empty
and they are separated by a <b>wide forbidden gap</b> \(E_g > 3\) eV (≈ 6 eV for diamond). No electron can gain
enough energy at room temperature to cross it, so there is no conduction.</p>
<p class="step"><b>Difference:</b> in a semiconductor the forbidden gap is <b>small</b> (≈ 1 eV: Si 1.1 eV, Ge 0.7 eV),
so at room temperature some electrons are thermally excited into the conduction band, leaving holes in the valence
band, and the material conducts slightly.</p>""",
          afig=[F.fig_a10a_bands],
          topic=ELEC, recall=r"<ul><li>Conductor: bands overlap; semiconductor: \(E_g\lesssim3\) eV; insulator: \(E_g>3\) eV.</li><li>Typical gaps: C 5.4–6 eV, Si 1.1 eV, Ge 0.7 eV.</li></ul>"),
        Q("10(b)", 3, r"""<p>Figure below shows the circuit of an electronic device:</p>{{fig:0}}
<p>(i) Which electronic device: a rectifier, an amplifier or an oscillator does the above circuit represent?</p>
<p>(ii) State where the input voltage is applied and where the output voltage is available.</p>
<p>(iii) Compare the output voltage of this circuit with its input voltage.</p>""",
          qfig=[F.fig_q10b_transistor],
          excluded="Transistor (common-emitter amplifier) — not in ISC 2027: Unit 9 covers energy bands, the p-n junction diode, rectifiers, LED, photodiode, solar cell and Zener diode; transistors appear only in the demonstration practicals (identifying one with a multimeter)."),
        Q("10(c)", 2, r"""<p>Prepare a truth table for the combination of gates shown in the figure below:</p>{{fig:0}}""",
          qfig=[F.fig_q10c_gates],
          excluded="Logic gates — not in ISC 2027: Unit 9 has no digital electronics (the word 'gate' does not occur in the syllabus)."),
    ])
