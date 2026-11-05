"""JEE Main mock test 1 — Physics (Q1-25).  Every item adapted from a kept pre-board question.

Options are written correct-first and placed by `_mcq(..., k=…)` so that the correct one lands at
index k; solutions never refer to an option by letter.
"""
from jee_kit import MCQ, NUM
import physics_figs as F
from physics_2016_17_figs import fig_q5a_wire

SUBJECT = "physics"
TEST = 1

ES = "Electrostatics"
CE = "Current Electricity"
MAG = "Magnetic Effects of Current and Magnetism"
EMI = "Electromagnetic Induction and Alternating Currents"
EMW = "Electromagnetic Waves"
RAY = "Optics — Ray Optics and Optical Instruments"
WAVE = "Optics — Wave Optics"
DUAL = "Dual Nature of Radiation and Matter"
ATOM = "Atoms and Nuclei — Atoms"
NUC = "Atoms and Nuclei — Nuclei"
SEMI = "Electronic Devices"


def _mcq(src, topic, q, opts, k, sol, **kw):
    """opts[0] is the correct option; it is placed at index k."""
    rest = list(opts[1:])
    rest.insert(k, opts[0])
    return MCQ(src=src, topic=topic, q=q, options=rest, answer=k, sol=sol, **kw)


QUESTIONS = [
    # 1 ------------------------------------------------------------------ Electrostatics
    _mcq(("physics_2014_15", "1(B)(iii)"), ES,
         r"""<p>Two identical parallel-plate capacitors are connected in parallel across a 60 V battery.
The battery is then disconnected and the space between the plates of <i>one</i> capacitor is
completely filled with a dielectric of dielectric constant \(K = 5\). The potential difference
across the other capacitor now is</p>""",
         [r"\(20\) V", r"\(60\) V", r"\(12\) V", r"\(10\) V"], 0,
         r"""<p>Before: total charge \(Q = (C + C)\times 60 = 120C\). The battery is removed, so this
charge is conserved.</p>
<p>After: the two capacitors are still in parallel, \(C_{\text{eq}} = C + 5C = 6C\).</p>
<p>Common potential \(V = \dfrac{Q}{C_{\text{eq}}} = \dfrac{120C}{6C} = 20\) V (the same across both).</p>
<p>\(60\) V assumes the battery is still connected; \(12\) V divides 60 V by \(K\) as if the
dielectric acted alone; \(10\) V forgets that the charge was stored on <i>two</i> capacitors.</p>
<p><b>Answer: \(20\) V.</b></p>"""),

    # 2 ------------------------------------------------------------------ Electrostatics
    _mcq(("physics_2016_17", "2(a)"), ES,
         r"""<p>A pendulum bob of mass 40 mg carrying a charge of 15 nC hangs at rest in a uniform
<i>horizontal</i> electric field of \(2\times10^{4}\) N C\(^{-1}\). Taking \(g = 10\) m s\(^{-2}\), the
tension in the thread is</p>""",
         [r"\(5\times10^{-4}\) N", r"\(7\times10^{-4}\) N", r"\(1\times10^{-4}\) N", r"\(4\times10^{-4}\) N"], 1,
         r"""<p>Weight \(mg = 40\times10^{-6}\times10 = 4\times10^{-4}\) N, vertically down.</p>
<p>Electric force \(qE = 15\times10^{-9}\times2\times10^{4} = 3\times10^{-4}\) N, horizontal.</p>
<p>In equilibrium the tension balances the resultant of these two perpendicular forces:
\(T = \sqrt{(mg)^2 + (qE)^2} = 10^{-4}\sqrt{4^2+3^2} = 5\times10^{-4}\) N
(thread at \(\tan^{-1}(3/4) = 37^\circ\) to the vertical).</p>
<p>Adding the forces as scalars gives \(7\times10^{-4}\) N, subtracting gives \(1\times10^{-4}\) N, and
\(4\times10^{-4}\) N ignores the electric force.</p>
<p><b>Answer: \(5\times10^{-4}\) N.</b></p>"""),

    # 3 ------------------------------------------------------------------ Electrostatics
    _mcq(("physics_2024_25", "1(B)(vii)"), ES,
         r"""<p>A parallel-plate capacitor is charged by a battery, which is then disconnected. The
separation between the plates is now doubled. Which statement is correct?</p>""",
         [r"Capacitance halves, potential difference doubles, stored energy doubles",
          r"Capacitance halves, potential difference is unchanged, stored energy halves",
          r"Capacitance halves, potential difference doubles, stored energy is unchanged",
          r"Capacitance doubles, potential difference halves, stored energy halves"], 2,
         r"""<p>\(C = \varepsilon_0A/d\): doubling \(d\) halves \(C\).</p>
<p>The battery is disconnected, so \(Q\) is constant. \(V = Q/C\) doubles.</p>
<p>\(U = \dfrac{Q^2}{2C}\): with \(Q\) fixed and \(C\) halved, \(U\) doubles (the extra energy is
the work done in pulling the plates apart against their attraction).</p>
<p>Why the others are wrong: "\(V\) unchanged, \(U\) halves" is the result when the battery stays
connected (\(V\) fixed, \(U = \tfrac12CV^2\)); "\(U\) unchanged" ignores that \(U\) depends on \(C\);
"capacitance doubles" has \(C\propto d\) instead of \(1/d\).</p>
<p><b>Answer: capacitance halves, potential difference doubles, stored energy doubles.</b></p>"""),

    # 4 ------------------------------------------------------------------ Current Electricity
    _mcq(("physics_2025_26", "1(A)(iii)"), CE,
         r"""<p>An ammeter is made from a galvanometer of coil resistance 90 Ω with a shunt of
10 Ω. It is connected in series with a 15 Ω resistor across an ideal 12 V battery. The ammeter
reads</p>""",
         [r"\(0.50\) A", r"\(0.80\) A", r"\(0.48\) A", r"\(0.11\) A"], 3,
         r"""<p>Resistance of the ammeter = coil ∥ shunt \(= \dfrac{90\times10}{90+10} = 9\) Ω.</p>
<p>Total resistance \(= 15 + 9 = 24\) Ω, so \(I = \dfrac{12}{24} = 0.50\) A. The ammeter reads the
whole current (coil + shunt together).</p>
<p>\(0.80\) A treats the ammeter as ideal (12/15); \(0.48\) A uses the shunt alone (12/25);
\(0.11\) A uses the coil alone (12/105).</p>
<p><b>Answer: \(0.50\) A.</b></p>"""),

    # 5 ------------------------------------------------------------------ Current Electricity
    _mcq(("physics_2015_16", "1(B)(iv)"), CE,
         r"""<p>Free electrons drift with speed \(v\) in a metal wire carrying current \(I\). In a
second wire of the same material but of half the radius, carrying current \(2I\), the drift speed
is</p>""",
         [r"\(8v\)", r"\(4v\)", r"\(2v\)", r"\(v/2\)"], 1,
         r"""<p>\(I = neAv_d = ne\pi r^2 v_d\Rightarrow v_d = \dfrac{I}{ne\pi r^2}\); \(n\) is the same
(same material).</p>
<p>\(\dfrac{v_d'}{v} = \dfrac{2I}{I}\times\dfrac{r^2}{(r/2)^2} = 2\times4 = 8\).</p>
<p>\(4v\) forgets the doubled current, \(2v\) forgets the smaller area, and \(v/2\) uses
\(v_d\propto r^2\).</p>
<p><b>Answer: \(8v\).</b></p>"""),

    # 6 ------------------------------------------------------------------ Magnetism
    _mcq(("physics_2015_16", "6(a)"), MAG,
         r"""<p>An \(\alpha\)-particle and a proton, having the <i>same kinetic energy</i>, move at
right angles to a uniform magnetic field. The ratio of the radii of their circular paths,
\(r_\alpha : r_p\), is</p>""",
         [r"\(1:1\)", r"\(1:2\)", r"\(2:1\)", r"\(\sqrt2:1\)"], 0,
         r"""<p>\(qvB = \dfrac{mv^2}{r}\Rightarrow r = \dfrac{mv}{qB} = \dfrac{\sqrt{2mK}}{qB}\).</p>
<p>With \(m_\alpha = 4m_p\), \(q_\alpha = 2e\), same \(K\):
\(\dfrac{r_\alpha}{r_p} = \dfrac{\sqrt{4m_p}}{\sqrt{m_p}}\cdot\dfrac{e}{2e} = \dfrac{2}{2} = 1\).</p>
<p>\(1:2\) is the answer for equal <i>momenta</i> (\(r\propto1/q\)); \(2:1\) is for equal speeds
(\(r\propto m/q\)); \(\sqrt2:1\) is for acceleration through the same potential difference
(\(r\propto\sqrt{m/q}\)).</p>
<p><b>Answer: \(1:1\).</b></p>"""),

    # 7 ------------------------------------------------------------------ Magnetism
    _mcq(("physics_2016_17", "5(a)"), MAG,
         r"""<p>A very long wire carrying current \(I\) is bent as shown: a straight part along a line
through O, a semicircle of radius \(r\) centred at O, and a straight part running off to infinity
from the foot of the perpendicular from O. The magnitude of the magnetic field at O is</p>""",
         [r"\(\dfrac{\mu_0 I}{4\pi r}(\pi+1)\)", r"\(\dfrac{\mu_0 I}{4\pi r}(\pi-1)\)",
          r"\(\dfrac{\mu_0 I}{4r}\)", r"\(\dfrac{\mu_0 I}{4\pi r}(\pi+2)\)"], 3,
         r"""<p>Straight part whose line passes through O: \(d\vec l\parallel\hat r\), so it gives
\(B_1 = 0\).</p>
<p>Semicircle: half of a full loop's field, \(B_2 = \dfrac12\cdot\dfrac{\mu_0I}{2r} = \dfrac{\mu_0I}{4r}\),
out of the page.</p>
<p>Semi-infinite wire starting at the foot of the perpendicular (distance \(r\)):
\(B_3 = \dfrac{\mu_0I}{4\pi r}\), also out of the page (current to the right, O above it).</p>
<p>\(B = \dfrac{\mu_0I}{4r} + \dfrac{\mu_0I}{4\pi r} = \dfrac{\mu_0I}{4\pi r}(\pi+1)\).</p>
<p>Why not the others: \((\pi-1)\) takes the two contributions as opposite, but both are out of
the page; \(\mu_0I/4r\) leaves out the straight wire; \((\pi+2)\) treats the semi-infinite wire as
an infinite one (\(\mu_0I/2\pi r\)).</p>
<p><b>Answer: \(\dfrac{\mu_0 I}{4\pi r}(\pi+1)\).</b></p>""",
         qfig=fig_q5a_wire),

    # 8 ------------------------------------------------------------------ EMI
    _mcq(("physics_2025_26", "1(A)(iv)"), EMI,
         r"""<p>When the current in a coil falls steadily from 5 A to 1 A in 0.02 s, an emf of 4 V is
induced in it. The self-inductance of the coil is</p>""",
         [r"\(20\) mH", r"\(16\) mH", r"\(13.3\) mH", r"\(80\) mH"], 2,
         r"""<p>\(|e| = L\dfrac{|\Delta I|}{\Delta t}\Rightarrow L = \dfrac{|e|\,\Delta t}{|\Delta I|}
= \dfrac{4\times0.02}{5-1} = 0.02\) H \(= 20\) mH.</p>
<p>\(16\) mH uses \(\Delta I = 5\) A (the initial current), \(13.3\) mH adds the currents
(\(\Delta I = 6\) A), \(80\) mH uses the final current 1 A.</p>
<p><b>Answer: \(20\) mH.</b></p>"""),

    # 9 ------------------------------------------------------------------ AC
    _mcq(("physics_2024_25", "13(a)"), EMI,
         r"""<p>A series LCR circuit has \(R = 80\ \Omega\), \(X_L = 100\ \Omega\) and \(X_C = 40\ \Omega\),
and is connected to an a.c. supply of peak voltage 200 V. The sum of the peak voltages across the
resistor, the inductor and the capacitor is</p>""",
         [r"\(440\) V", r"\(200\) V", r"\(280\) V", r"\(360\) V"], 3,
         r"""<p>\(Z = \sqrt{R^2 + (X_L - X_C)^2} = \sqrt{80^2 + 60^2} = 100\ \Omega\);
\(I_0 = \dfrac{200}{100} = 2\) A.</p>
<p>Peak voltages: \(V_R = 160\) V, \(V_L = 200\) V, \(V_C = 80\) V; their sum is \(440\) V.</p>
<p>This exceeds the supply because the three peaks occur at different instants; only the phasor sum
\(\sqrt{160^2 + (200-80)^2} = 200\) V equals the supply. \(200\) V is that phasor sum,
\(280\) V subtracts \(V_C\), \(360\) V leaves \(V_C\) out.</p>
<p><b>Answer: \(440\) V.</b></p>"""),

    # 10 ----------------------------------------------------------------- EM waves
    _mcq(("physics_2016_17", "1(B)(ix)"), EMW,
         r"""<p>An aircraft radar operates at a wavelength of 3 cm. Its frequency and the part of the
electromagnetic spectrum it belongs to are</p>""",
         [r"\(10^{10}\) Hz, microwaves", r"\(10^{9}\) Hz, microwaves",
          r"\(10^{12}\) Hz, infrared", r"\(10^{8}\) Hz, radio waves"], 0,
         r"""<p>\(\nu = \dfrac{c}{\lambda} = \dfrac{3\times10^{8}}{3\times10^{-2}} = 10^{10}\) Hz (10 GHz),
which lies in the microwave band (about 1 mm to 30 cm).</p>
<p>\(10^9\) Hz comes from taking 3 cm as 0.3 m; \(10^{12}\) Hz (0.3 mm) and \(10^8\) Hz (3 m) are
the wrong wavelengths and the wrong bands.</p>
<p><b>Answer: \(10^{10}\) Hz, microwaves.</b></p>"""),

    # 11 ----------------------------------------------------------------- Ray optics
    _mcq(("physics_2015_16", "1(A)(iii)"), RAY,
         r"""<p>A bird is flying 30 cm above the surface of still water \((\mu = 4/3)\). To a fish just
below the surface, looking vertically up, the bird appears to be at a height of</p>""",
         [r"\(40\) cm", r"\(22.5\) cm", r"\(30\) cm", r"\(45\) cm"], 1,
         r"""<p>The object (bird) is in the rarer medium and is seen from the denser one, so it appears
<i>farther</i>: apparent height \(= \mu\times\) real height \(= \tfrac43\times30 = 40\) cm.</p>
<p>\(22.5\) cm divides by \(\mu\) (the rule for an object in water seen from air); \(30\) cm ignores
refraction; \(45\) cm uses \(\mu = 1.5\).</p>
<p><b>Answer: \(40\) cm.</b></p>"""),

    # 12 ----------------------------------------------------------------- Ray optics
    _mcq(("physics_2014_15", "9(b)"), RAY,
         r"""<p>Where must an object be placed in front of a convex lens of focal length 20 cm to obtain
a <i>real</i> image twice the size of the object?</p>""",
         [r"\(30\) cm from the lens", r"\(10\) cm from the lens", r"\(40\) cm from the lens",
          r"\(60\) cm from the lens"], 2,
         r"""<p>Real image, magnified twice: \(m = \dfrac{v}{u} = -2\Rightarrow v = -2u\).</p>
<p>\(\dfrac1v - \dfrac1u = \dfrac1f\Rightarrow -\dfrac{1}{2u} - \dfrac1u = \dfrac1{20}
\Rightarrow -\dfrac{3}{2u} = \dfrac1{20}\Rightarrow u = -30\) cm (image at \(v = +60\) cm).</p>
<p>\(10\) cm gives the <i>virtual</i> image with \(m = +2\); \(40\) cm (at \(2f\)) gives \(m = -1\);
\(60\) cm is the image distance, not the object distance.</p>
<p><b>Answer: \(30\) cm from the lens.</b></p>"""),

    # 13 ----------------------------------------------------------------- Ray optics
    _mcq(("physics_2025_26", "6(a)"), RAY,
         r"""<p>For a prism of angle \(60^\circ\) the angle of minimum deviation is \(30^\circ\). The
refractive index of the prism material is</p>""",
         [r"\(\sqrt2\)", r"\(\sqrt3\)", r"\(2\)", r"\(\sqrt{3/2}\)"], 3,
         r"""<p>At minimum deviation \(r_1 = r_2 = A/2 = 30^\circ\) and
\(i = \dfrac{A+\delta_m}{2} = \dfrac{60^\circ + 30^\circ}{2} = 45^\circ\).</p>
<p>\(\mu = \dfrac{\sin i}{\sin r} = \dfrac{\sin45^\circ}{\sin30^\circ} = \dfrac{1/\sqrt2}{1/2} = \sqrt2\).</p>
<p>\(\sqrt3\) takes \(i = A = 60^\circ\); \(2\) takes \(i = A + \delta_m = 90^\circ\);
\(\sqrt{3/2}\) is \(\sin A/\sin i\), the formula upside-down in the wrong angles.</p>
<p><b>Answer: \(\sqrt2\).</b></p>"""),

    # 14 ----------------------------------------------------------------- Wave optics
    _mcq(("physics_2015_16", "8(b)"), WAVE,
         r"""<p>In a Young's double-slit experiment the ratio of the intensities at the maxima and the
minima is 9 : 1. Taking the intensity from each slit to be proportional to its width, the ratio of
the slit widths is</p>""",
         [r"\(4:1\)", r"\(2:1\)", r"\(3:1\)", r"\(9:1\)"], 0,
         r"""<p>\(\dfrac{I_{\max}}{I_{\min}} = \left(\dfrac{a_1 + a_2}{a_1 - a_2}\right)^2 = 9
\Rightarrow \dfrac{a_1 + a_2}{a_1 - a_2} = 3\Rightarrow a_1 = 2a_2\).</p>
<p>Width \(\propto\) intensity \(\propto a^2\): \(\dfrac{w_1}{w_2} = \left(\dfrac{a_1}{a_2}\right)^2 = 4\).</p>
<p>\(2:1\) is the amplitude ratio, \(3:1\) is \(\sqrt{9}\), and \(9:1\) is the intensity ratio
of the fringes themselves.</p>
<p><b>Answer: \(4:1\).</b></p>"""),

    # 15 ----------------------------------------------------------------- Dual nature
    _mcq(("physics_2013_14", "8(b)"), DUAL,
         r"""<p>Light of wavelength 310 nm falls on a metal of work function 2.2 eV. The stopping
potential is (take \(hc = 1240\) eV nm)</p>""",
         [r"\(1.8\) V", r"\(4.0\) V", r"\(6.2\) V", r"\(2.2\) V"], 1,
         r"""<p>Photon energy \(E = \dfrac{hc}{\lambda} = \dfrac{1240}{310} = 4.0\) eV.</p>
<p>\(eV_0 = E - \phi_0 = 4.0 - 2.2 = 1.8\) eV, so \(V_0 = 1.8\) V.</p>
<p>\(4.0\) V forgets the work function, \(6.2\) V adds it, \(2.2\) V is the work function itself.</p>
<p><b>Answer: \(1.8\) V.</b></p>"""),

    # 16 ----------------------------------------------------------------- Atoms
    _mcq(("physics_2025_26", "1(B)(v)"), ATOM,
         r"""<p>The electron in a hydrogen atom jumps from the third excited state to the second excited
state. The emitted photon belongs to the</p>""",
         [r"Paschen series, in the infrared", r"Balmer series, in the visible",
          r"Lyman series, in the ultraviolet", r"Brackett series, in the infrared"], 3,
         r"""<p>Third excited state is \(n = 4\); second excited state is \(n = 3\) (the ground state is
\(n = 1\)). A transition ending on \(n = 3\) is a Paschen line.</p>
<p>\(\dfrac1\lambda = R\left(\dfrac1{9} - \dfrac1{16}\right) = \dfrac{7R}{144}\Rightarrow
\lambda = \dfrac{144}{7\times1.097\times10^{7}} \approx 1.88\times10^{-6}\) m — infrared.</p>
<p>Balmer/visible results from reading the states as \(n = 3\to2\); Lyman needs the electron to end in
\(n = 1\); Brackett lines end in \(n = 4\), not start there.</p>
<p><b>Answer: Paschen series, in the infrared.</b></p>"""),

    # 17 ----------------------------------------------------------------- Nuclei
    _mcq(("physics_2014_15", "13(b)"), NUC,
         r"""<p>Mass of proton = 1.007276 u, mass of neutron = 1.008665 u, mass of the
\({}^{4}_{2}\mathrm{He}\) nucleus = 4.001506 u. Taking 1 u = 931 MeV/\(c^2\), the binding energy
<i>per nucleon</i> of \({}^{4}_{2}\mathrm{He}\) is about</p>""",
         [r"\(7.07\) MeV", r"\(28.3\) MeV", r"\(14.1\) MeV", r"\(3.54\) MeV"], 2,
         r"""<p>Mass defect \(\Delta m = 2(1.007276) + 2(1.008665) - 4.001506 = 4.031882 - 4.001506
= 0.030376\) u.</p>
<p>\(BE = 0.030376\times931 = 28.3\) MeV; per nucleon \(28.3/4 = 7.07\) MeV.</p>
<p>\(28.3\) MeV is the total binding energy; \(14.1\) MeV divides by the number of protons only;
\(3.54\) MeV divides by 8.</p>
<p><b>Answer: \(7.07\) MeV.</b></p>"""),

    # 18 ----------------------------------------------------------------- Semiconductors
    _mcq(("physics_2013_14", "1(B)(ix)"), SEMI,
         r"""<p>In the voltage-regulator circuit shown, the Zener diode has a breakdown voltage of 6 V.
The current through the Zener diode is</p>""",
         [r"\(10\) mA", r"\(20\) mA", r"\(30\) mA", r"\(12.5\) mA"], 0,
         r"""<p>Check that the Zener is in breakdown: without it the load would get
\(10\times\dfrac{600}{800} = 7.5\) V \(\gt 6\) V, so it does break down and holds 6 V.</p>
<p>Current through the 200 Ω resistor: \(I_s = \dfrac{10 - 6}{200} = 20\) mA.</p>
<p>Load current: \(I_L = \dfrac{6}{600} = 10\) mA. Zener current \(I_Z = I_s - I_L = 10\) mA.</p>
<p>\(20\) mA is the series current, \(30\) mA adds instead of subtracting, and \(12.5\) mA is the
current with the Zener removed.</p>
<p><b>Answer: \(10\) mA.</b></p>""",
         qfig=F.fig_jp_t1_zener),

    # 19 ----------------------------------------------------------------- Semiconductors
    _mcq(("physics_2024_25", "1(B)(vi)"), SEMI,
         r"""<p>When a p-n junction is forward biased, the width of the depletion region and the height
of the potential barrier respectively</p>""",
         [r"both decrease", r"increase, decrease", r"both increase", r"decrease, remain unchanged"], 1,
         r"""<p>The applied forward voltage opposes the built-in field. Majority carriers are pushed
towards the junction and neutralise some of the immobile ions, so the depletion layer narrows and
the barrier falls from \(V_0\) to \(V_0 - V\).</p>
<p>"Both increase" is the reverse-bias behaviour. The barrier height cannot stay unchanged while the
width shrinks — it is the potential across that layer of ions, so the two fall together. Width
increasing with barrier decreasing is inconsistent for the same reason.</p>
<p><b>Answer: both decrease.</b></p>"""),

    # 20 ----------------------------------------------------------------- EMI
    _mcq(("physics_2014_15", "6(b)"), EMI,
         r"""<p>A metal rod of length 0.5 m slides on two parallel conducting rails in a uniform field
of 0.2 T perpendicular to the plane of the rails. The total resistance of the circuit is 2 Ω. The
force needed to move the rod at a constant speed of 4 m s\(^{-1}\) is</p>""",
         [r"\(0.02\) N", r"\(0.04\) N", r"\(0.2\) N", r"\(0.08\) N"], 3,
         r"""<p>Motional emf \(\varepsilon = Blv = 0.2\times0.5\times4 = 0.4\) V;
\(I = \varepsilon/R = 0.2\) A.</p>
<p>Magnetic force on the rod \(F = BIl = 0.2\times0.2\times0.5 = 0.02\) N, opposing the motion (Lenz).
At constant speed the applied force equals it: \(F = \dfrac{B^2l^2v}{R} = 0.02\) N.</p>
<p>\(0.04\) N leaves \(l\) unsquared, \(0.2\) N is \(Blv/R\) (that is the current, not a force), and
\(0.08\) N is the power \(Fv\) in watts.</p>
<p><b>Answer: \(0.02\) N.</b></p>"""),

    # ===================================================================== Section B (integer)
    # 21 ----------------------------------------------------------------- Electrostatics
    NUM(src=("physics_2015_16", "3(b)"), topic=ES,
        q=r"""<p>Two point charges of \(+10\ \mu\)C each are 10 cm apart. They are brought 5 cm closer
to each other. Find the increase in the electrostatic potential energy of the system, in joule.
(\(\tfrac{1}{4\pi\varepsilon_0} = 9\times10^{9}\) N m\(^2\) C\(^{-2}\))</p>""",
        answer=9,
        sol=r"""<p>\(kq_1q_2 = 9\times10^{9}\times(10\times10^{-6})^2 = 0.9\) J m.</p>
<p>\(U_1 = 0.9/0.10 = 9\) J; \(U_2 = 0.9/0.05 = 18\) J.</p>
<p>Increase \(\Delta U = 18 - 9 = 9\) J (work done against the repulsion).</p>
<p><b>Answer: 9</b></p>"""),

    # 22 ----------------------------------------------------------------- Current Electricity
    NUM(src=("physics_2013_14", "1(A)(v)"), topic=CE,
        q=r"""<p>A uniform wire of resistance 100 Ω is stretched uniformly to twice its length. It is
then cut into four equal parts, which are joined in parallel. Find the resistance of the
combination, in ohm.</p>""",
        answer=25,
        sol=r"""<p>Stretching keeps the volume fixed: length ×2, area ÷2, so \(R = \rho l/A\) becomes
\(4\times100 = 400\) Ω.</p>
<p>Each quarter: \(400/4 = 100\) Ω. Four equal resistors in parallel: \(100/4 = 25\) Ω.</p>
<p><b>Answer: 25</b></p>"""),

    # 23 ----------------------------------------------------------------- Magnetism
    NUM(src=("physics_2016_17", "6(b)"), topic=MAG,
        q=r"""<p>A galvanometer of resistance 40 Ω gives full-scale deflection for a current of 5 mA.
Find the resistance, in ohm, that must be connected in series with it to convert it into a
voltmeter of range 0–10 V.</p>""",
        answer=1960,
        sol=r"""<p>At full scale the whole 10 V drives \(I_g = 5\) mA through \(G + R\):
\(V = I_g(G + R)\).</p>
<p>\(R = \dfrac{V}{I_g} - G = \dfrac{10}{0.005} - 40 = 2000 - 40 = 1960\) Ω.</p>
<p><b>Answer: 1960</b></p>"""),

    # 24 ----------------------------------------------------------------- Wave optics
    NUM(src=("physics_2024_25", "14"), topic=WAVE,
        q=r"""<p>In a Young's double-slit experiment the slits are 1 mm apart. When the screen is moved
25 cm towards the slits, the fringe width changes by 0.135 mm. Find the wavelength of the light, in
nanometre.</p>""",
        answer=540,
        sol=r"""<p>\(\beta = \dfrac{\lambda D}{d}\); with \(\lambda\) and \(d\) fixed,
\(\Delta\beta = \dfrac{\lambda\,\Delta D}{d}\).</p>
<p>\(\lambda = \dfrac{d\,\Delta\beta}{\Delta D} = \dfrac{10^{-3}\times1.35\times10^{-4}}{0.25}
= 5.4\times10^{-7}\) m \(= 540\) nm.</p>
<p><b>Answer: 540</b></p>"""),

    # 25 ----------------------------------------------------------------- Dual nature
    NUM(src=("physics_2014_15", "1(B)(xiii)"), topic=DUAL,
        q=r"""<p>Ultraviolet light has a frequency of \(1.45\times10^{15}\) Hz. Find the energy of one
photon of this light, in eV, to the nearest integer. (\(h = 4.14\times10^{-15}\) eV s)</p>""",
        answer=6,
        sol=r"""<p>\(E = h\nu = 4.14\times10^{-15}\times1.45\times10^{15} = 6.00\) eV
(\(\approx9.6\times10^{-19}\) J).</p>
<p><b>Answer: 6</b></p>"""),
]
