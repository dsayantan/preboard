"""Heritage School Pre-Board 2024-25, Chemistry (Paper 1), Set 1 -- transcribed from the page images."""
from kit import Q, SEC
import chemistry_2024_25_figs as fg

AR = r"""<p>(a) Both assertion and reason are true and the reason is the correct explanation of assertion.<br>
(b) Both assertion and reason are true but reason is not the correct explanation for assertion.<br>
(c) Assertion is true but reason is false.<br>
(d) Assertion is false but reason is true.</p>"""

WORDS = (r"[specific, acetaldehyde, formaldehyde, acetic acid, methyl isocyanide, tetrahedral, octahedral, "
         r"square planar, calcium bicarbonate, para, iodoform, equivalent, acetone, dia, one, two, three]")

PAPER = dict(
    subject="chemistry",
    year="2024-25",
    slug="2024-25-set-1",
    paper="Set 1",
    source="PreBoard-PYQ/2024-25/SET-1/Chemistry.pdf",
    marks=70, time="3 hours",
    intro=r"""<p><b>The Heritage School &mdash; Pre-Board Examinations, 2024-2025. Subject: Chemistry (Paper 1),
Class XII.</b> Full Marks = 70. Time &mdash; 3 hrs.</p>
<p><i>(Candidates are allowed additional 15 minutes for only reading the paper. They must NOT start writing during
this time).</i></p>
<p>This paper is divided into four sections &ndash; A, B, C and D. Answer all questions.
Section A consists of one question having sub-parts of one mark each. Section B consists of ten questions of two
marks each. Section C consists of seven questions of three marks each, and Section D consists of three questions of
five marks each.</p>
<p><b>Internal choices have been provided in one question each in Section B, Section C and Section D.</b></p>
<p>All working, including rough work, should be done on the same sheet as, and adjacent to the rest of the answer.
The intended marks for questions or parts of questions are given in brackets [ ]. Balanced equations must be given
wherever possible and diagrams where they are helpful. When solving numerical problems, all essential working must
be shown. In working out problems, use the following data:</p>
<p>Gas constant R = 1&middot;987 cal deg<sup>&minus;1</sup> mol<sup>&minus;1</sup> = 8&middot;314 J K<sup>&minus;1</sup>
mol<sup>&minus;1</sup> = 0&middot;0821 dm<sup>3</sup> atm K<sup>&minus;1</sup> mol<sup>&minus;1</sup>.
1 l atm = 1 dm<sup>3</sup> atm = 101&middot;3 J. 1 Faraday = 96500 coulombs. Avogadro's number =
6&middot;023 &times; 10<sup>23</sup>.</p>
<p>This question paper consists of ten printed pages.</p>""",
    items=[
        SEC("Section A &ndash; 14 Marks", "Question 1"),
        # ------------------------------------------------------------------ 1(A)
        Q("1(A)(i)", 1, r"<p><b>(A) Fill in the blanks by choosing the appropriate word(s) from those given in the "
          r"bracket:</b> " + WORDS + r" [4&times;1=4]</p>"
          r"<p>(i) As the concentration of an electrolytic solution increases its ________ conductance increases "
          r"but _________ conductance decreases.</p>",
          a=r"""<p>As the concentration of an electrolytic solution increases its <b>specific</b> conductance increases
but <b>equivalent</b> conductance decreases.</p>
<p>Specific conductance \(\kappa\) is the conductance of 1 cm<sup>3</sup> of solution: more concentrated &rArr; more
ions per cm<sup>3</sup> &rArr; \(\kappa\) rises. Equivalent (and molar) conductance
\(\Lambda_{eq} = \dfrac{1000\,\kappa}{N}\) refers to the ions from one gram-equivalent; at higher concentration
interionic attraction (strong electrolytes) or a smaller degree of dissociation (weak electrolytes) lowers it.</p>
<p><span class="box">specific; equivalent</span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>\(\kappa = \dfrac{1}{R}\cdot\dfrac{l}{A}\) (S cm<sup>&minus;1</sup>);
\(\Lambda_m = \dfrac{1000\,\kappa}{M}\), \(\Lambda_{eq} = \dfrac{1000\,\kappa}{N}\).</li>
<li>On dilution: \(\kappa\) decreases, \(\Lambda_m\) and \(\Lambda_{eq}\) increase.</li></ul>"""),
        Q("1(A)(ii)", 1, r"<p>(ii) Ferricyanide ion is ____ magnetic while ferrocyanide ion is ______ magnetic in "
          r"nature.</p>",
          a=r"""<p>Ferricyanide ion is <b>para</b>magnetic while ferrocyanide ion is <b>dia</b>magnetic in nature.</p>
<p>\(\ce{[Fe(CN)6]^3-}\): \(\ce{Fe^3+}\), 3d<sup>5</sup>; \(\ce{CN-}\) is strong field, so the electrons pair into
\(t_{2g}^5\) &mdash; one unpaired electron (paramagnetic, d<sup>2</sup>sp<sup>3</sup>).
\(\ce{[Fe(CN)6]^4-}\): \(\ce{Fe^2+}\), 3d<sup>6</sup> &rarr; \(t_{2g}^6\), no unpaired electron (diamagnetic).</p>
<p><span class="box">para; dia</span></p>""",
          topic="Coordination Compounds",
          recall=r"""<ul><li>\(\ce{CN-}\) is a strong-field ligand: \(\Delta_o > P\), low-spin complexes.</li>
<li>Any unpaired electron &rArr; paramagnetic; all paired &rArr; diamagnetic.</li></ul>"""),
        Q("1(A)(iii)", 1, r"<p>(iii) Calcium acetate on heating gives _____ which gives _____ on heating with iodine "
          r"and sodium hydroxide solution.</p>",
          a=r"""<p>Calcium acetate on heating gives <b>acetone</b> which gives <b>iodoform</b> on heating with iodine and
sodium hydroxide solution.</p>
<p>\(\ce{(CH3COO)2Ca ->[\Delta] CH3COCH3 + CaCO3}\)</p>
<p>\(\ce{CH3COCH3 + 3I2 + 4NaOH -> CHI3 v + CH3COONa + 3NaI + 3H2O}\)</p>
<p><span class="box">acetone; iodoform</span></p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Dry distillation of calcium salts:<br>\(\ce{(RCOO)2Ca -> RCOR}\) \(\ce{+ CaCO3}\); calcium formate
gives HCHO.</li><li>Iodoform test: positive for \(\ce{CH3CO-}\) and \(\ce{CH3CH(OH)-}\) compounds (yellow
\(\ce{CHI3}\)).</li></ul>"""),
        Q("1(A)(iv)", 1, r"<p>(iv) The number of unpaired electrons in [CuCl<sub>4</sub>]<sup>&minus;2</sup> is ______ "
          r"and is ______ in shape.</p>",
          a=r"""<p>The number of unpaired electrons in \(\ce{[CuCl4]^2-}\) is <b>one</b> and is <b>tetrahedral</b> in
shape.</p>
<p>\(\ce{Cu^2+}\) is 3d<sup>9</sup>: whatever the arrangement, one electron stays unpaired (\(\mu \approx 1.73\) BM).
\(\ce{Cl-}\) is a weak-field ligand and four bulky \(\ce{Cl-}\) ions are arranged tetrahedrally (sp<sup>3</sup>);
in crystals the tetrahedron is somewhat flattened.</p>
<p><span class="box">one; tetrahedral</span></p>
<p class="note">Some school keys give "square planar" (dsp<sup>2</sup>) for Cu(II). The isolated
\(\ce{[CuCl4]^2-}\) ion, as in \(\ce{Cs2CuCl4}\), is a (flattened) tetrahedron; the number of unpaired electrons
is one in either case.</p>""",
          topic="Coordination Compounds",
          recall=r"""<ul><li>3d<sup>9</sup> always has one unpaired electron.</li>
<li>Four weak-field halide ligands &rArr; usually tetrahedral (sp<sup>3</sup>), e.g. \(\ce{[NiCl4]^2-}\),
\(\ce{[CoCl4]^2-}\).</li></ul>"""),
        # ------------------------------------------------------------------ 1(B)
        Q("1(B)(i)", 1, r"<p><b>(B) Select the correct alternative from the choices given below:</b> [7&times;1=7]</p>"
          r"<p>(i) An organic compound <b>A</b>[C<sub>3</sub>H<sub>9</sub>N], when treated with nitrous acid, gave an "
          r"alcohol and N<sub>2</sub> gas. Compound <b>A</b> on warming with CHCl<sub>3</sub> and caustic potash gave "
          r"<b>C</b> which on reduction gave isopropyl methyl amine. Predict the structure of <b>A</b>.</p>"
          r"<p>(a) (CH<sub>3</sub>)<sub>2</sub>CHNH<sub>2</sub> &nbsp; (b) CH<sub>3</sub>CH<sub>2</sub>NHCH<sub>3</sub>"
          r" &nbsp; (c) (CH<sub>3</sub>)<sub>3</sub>N &nbsp; (d) CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>NH<sub>2</sub></p>",
          a=r"""<p>Alcohol + \(\ce{N2}\) with \(\ce{HNO2}\) and the carbylamine reaction both show a <b>primary</b> amine.
Carbylamine: \(\ce{R-NH2 -> R-N#C}\); reduction gives \(\ce{R-NH-CH3}\). Since the product is isopropyl methyl
amine, \(\ce{R}\) = isopropyl:</p>
<p>\(\ce{(CH3)2CHNH2 + CHCl3 + 3KOH -> (CH3)2CH-NC + 3KCl + 3H2O}\)<br>
\(\ce{(CH3)2CH-NC + 4[H] -> (CH3)2CH-NH-CH3}\)</p>
<p><span class="box">(a) (CH<sub>3</sub>)<sub>2</sub>CHNH<sub>2</sub></span></p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>1&deg; aliphatic amine + \(\ce{HNO2}\) &rarr; alcohol + \(\ce{N2}\)&uarr;.</li>
<li>Only 1&deg; amines give the carbylamine (isocyanide) test; \(\ce{R-NC}\) reduces to the secondary amine
\(\ce{R-NHCH3}\).</li></ul>"""),
        Q("1(B)(ii)", 1, r"<p>(ii) Three samples of aqueous solution of KCl are labelled as 10<sup>&minus;1</sup> M[A], "
          r"10<sup>&minus;2</sup> M[B] and 10<sup>&minus;3</sup> M[C] respectively. Which of the following represents the "
          r"correct order of van't Hoff factor for these solutions.</p>"
          r"<p>(a) i<sub>A</sub> &lt; i<sub>B</sub> &lt; i<sub>C</sub> &nbsp; (b) i<sub>A</sub> &gt; i<sub>B</sub> &gt; "
          r"i<sub>C</sub> &nbsp; (c) i<sub>A</sub> = i<sub>B</sub> = i<sub>C</sub> &nbsp; (d) i<sub>A</sub> &lt; "
          r"i<sub>C</sub> &lt; i<sub>B</sub></p>",
          a=r"""<p>KCl is a strong electrolyte, \(\ce{KCl -> K+ + Cl-}\), so the ideal value of \(i\) is 2. In a real
solution interionic attraction makes the ions behave as if fewer particles were present, so \(i\) is a little less
than 2; the effect weakens on dilution and \(i\) approaches 2. Hence the most dilute sample (C) has the largest
\(i\).</p>
<p><span class="box">(a) i<sub>A</sub> &lt; i<sub>B</sub> &lt; i<sub>C</sub></span></p>""",
          topic="Solutions",
          recall=r"""<ul><li>\(i\) = observed colligative property &divide; calculated (normal) value.</li>
<li>For dissociation \(i = 1 + (n-1)\alpha\); \(\alpha\) (or the effective value for strong electrolytes) rises
on dilution, so \(i \to n\).</li></ul>"""),
        Q("1(B)(iii)", 1, r"<p>(iii) The reaction of toluene with chlorine in the presence of light yields &mdash;</p>"
          r"<p>(a) Benzyl chloride &nbsp; (b) o-chlorobenzene &nbsp; (c) p-chlorobenzene &nbsp; (d) m-chlorobenzene</p>",
          a=r"""<p>In light (or heat) and without a Lewis acid, chlorination is a free-radical substitution in the
<b>side chain</b>:</p>
<p>\(\ce{C6H5CH3 + Cl2 ->[h\nu] C6H5CH2Cl + HCl}\)</p>
<p>(Ring substitution, giving o- and p-chlorotoluene, needs \(\ce{FeCl3}\) in the dark.)</p>
<p><span class="box">(a) Benzyl chloride</span></p>""",
          topic="Haloalkanes and Haloarenes",
          recall=r"""<ul><li>"Side chain in Sunlight, nucleus in Cold with Carrier (\(\ce{FeCl3}\))".</li>
<li>Excess \(\ce{Cl2}\)/light gives \(\ce{C6H5CHCl2}\) and \(\ce{C6H5CCl3}\).</li></ul>"""),
        Q("1(B)(iv)", 1, r"<p>(iv) Which of the statements about <b><u>denaturation</u></b> given below are correct?</p>"
          r"<p>1. Denaturation causes loss of secondary and tertiary structures of the protein<br>"
          r"2. Denaturation leads to conversion of double strand of DNA into single strand.<br>"
          r"3. Denaturation affects primary structure which gets distorted.</p>"
          r"<p>(a) 1, 2 and 3 &nbsp; (b) 1 and 3 &nbsp; (c) 2 and 3 &nbsp; (d) 1 and 2</p>",
          a=r"""<p>Denaturation (heat, pH change, etc.) breaks hydrogen bonds and other weak interactions: a protein loses
its secondary and tertiary structure (statement 1), and the two strands of DNA, held by hydrogen bonds between bases,
separate (statement 2). Peptide bonds are not broken, so the <b>primary structure is unaffected</b> &mdash; statement
3 is wrong.</p>
<p><span class="box">(d) 1 and 2</span></p>""",
          topic="Biomolecules",
          recall=r"""<ul><li>Denaturation: loss of 2&deg;/3&deg; structure and biological activity; 1&deg;
(amino-acid sequence) intact. e.g. coagulation of egg white.</li></ul>"""),
        Q("1(B)(v)", 1, r"<p>(v) In which of the following species does the transition metal ion have d<sup>3</sup> "
          r"electronic configuration?</p>"
          r"<p>(a) [Cr(NH<sub>3</sub>)<sub>6</sub>]<sup>+3</sup> &nbsp; (b) [CoF<sub>6</sub>]<sup>&minus;3</sup> &nbsp; "
          r"(c) [Fe(CN)<sub>6</sub>]<sup>&minus;3</sup> &nbsp; (d) [Ni(CO)<sub>4</sub>]</p>",
          a=r"""<table class="tbl"><tr><th>Species</th><th>metal ion</th><th>configuration</th></tr>
<tr><td>\(\ce{[Cr(NH3)6]^3+}\)</td><td>\(\ce{Cr^3+}\) (Z = 24)</td><td>3d<sup>3</sup></td></tr>
<tr><td>\(\ce{[CoF6]^3-}\)</td><td>\(\ce{Co^3+}\)</td><td>3d<sup>6</sup></td></tr>
<tr><td>\(\ce{[Fe(CN)6]^3-}\)</td><td>\(\ce{Fe^3+}\)</td><td>3d<sup>5</sup></td></tr>
<tr><td>\(\ce{[Ni(CO)4]}\)</td><td>Ni(0)</td><td>3d<sup>8</sup>4s<sup>2</sup></td></tr></table>
<p><span class="box">(a) [Cr(NH<sub>3</sub>)<sub>6</sub>]<sup>3+</sup></span></p>""",
          topic="Coordination Compounds",
          recall=r"""<ul><li>Oxidation state of the metal = charge of complex &minus; sum of ligand charges
(\(\ce{NH3}\), CO neutral; \(\ce{F-}\), \(\ce{CN-}\) &minus;1).</li>
<li>Remove 4s electrons first: Cr 3d<sup>5</sup>4s<sup>1</sup> &rarr; \(\ce{Cr^3+}\) 3d<sup>3</sup>.</li></ul>"""),
        Q("1(B)(vi)", 1, r"<p>(vi) <b>Assertion</b>: C-X bond in aryl halides is less polar than the C-X bond in alkyl "
          r"halides.<br><b>Reason</b>: In aryl halides, the electron withdrawing inductive effect is opposed by electron "
          r"releasing resonance effect.</p>" + AR,
          a=r"""<p>In an aryl halide a lone pair of the halogen is delocalised into the ring (+R effect), which partly
cancels the &minus;I pull of the halogen, and the C&ndash;X bond acquires some double-bond character. So the bond is
less polar &mdash; e.g. dipole moment of chlorobenzene 1.69 D against about 2.0 D for chloroalkanes. The reason is
true and is the explanation (the sp<sup>2</sup> carbon, being more electronegative, adds to the effect).</p>
<p><span class="box">(a) Both true; reason is the correct explanation</span></p>""",
          topic="Haloalkanes and Haloarenes",
          recall=r"""<ul><li>Haloarenes: C&ndash;X shorter, stronger, less polar (resonance + sp<sup>2</sup> carbon) &rArr;
inert to nucleophilic substitution.</li></ul>"""),
        Q("1(B)(vii)", 1, r"<p>(vii) <b>Assertion</b>: Separation of Zr and Hf is difficult.<br>"
          r"<b>Reason</b>: Zr and Hf have almost equal atomic radii.</p>" + AR,
          a=r"""<p>Because of the <b>lanthanoid contraction</b>, Hf (5d series, after the 14 lanthanoids) has almost the
same radius as Zr (4d) &mdash; 160 pm and 159 pm. With the same valence configuration and nearly the same size, their
chemical properties are almost identical, so they occur together and are very hard to separate. The reason explains
the assertion.</p>
<p><span class="box">(a) Both true; reason is the correct explanation</span></p>""",
          topic="d- and f-Block Elements",
          recall=r"""<ul><li>Lanthanoid contraction: poor shielding by 4f electrons &rArr; steady decrease in size
from La to Lu; 4d and 5d members of a group (Zr/Hf, Nb/Ta, Mo/W) have nearly equal radii.</li></ul>"""),
        # ------------------------------------------------------------------ 1(C)
        Q("1(C)", 3, r"<p><b>(C) Read the passage given below carefully and answer the questions that follow:</b> [3]</p>"
          r"<p>The rate of the reaction is proportional to the concentration of the reactant. Hydrogenation of ethene "
          r"results in the formation of ethane. The rate constant k for the reaction was found to be "
          r"2.5 &times; 10<sup>&minus;15</sup> s<sup>&minus;1</sup>. The concentration of the reactant reduces to "
          r"one-third of the initial concentration in 5 minutes.</p>"
          r"<p>(i) State the order of the reaction.</p>"
          r"<p>(ii) The rate law equation is:<br>(a) Rate = k [C<sub>2</sub>H<sub>6</sub>] &nbsp; (b) Rate = k "
          r"[C<sub>2</sub>H<sub>4</sub>]<sup>2</sup> &nbsp; (c) Rate = k [C<sub>2</sub>H<sub>4</sub>] &nbsp; (d) Rate = k "
          r"[C<sub>2</sub>H<sub>4</sub>]<sup>2</sup></p>"
          r"<p>(iii) What is the half life for the reaction?</p>"
          r"<p>(iv) What is the rate constant of the reaction after 5 minutes?</p>"
          r"<p class='note'>[Options (b) and (d) are printed identically in the original.]</p>",
          a=r"""<p><b>(i)</b> Rate &prop; [reactant] (first power), and k has the unit s<sup>&minus;1</sup>:
<span class="box">first order</span></p>
<p><b>(ii)</b> The reactant is ethene: <span class="box">(c) Rate = k[C<sub>2</sub>H<sub>4</sub>]</span></p>
<p><b>(iii)</b> For a first-order reaction</p>
\[t_{1/2} = \frac{0.693}{k} = \frac{0.693}{2.5\times10^{-15}\ \text{s}^{-1}} = 2.77\times10^{14}\ \text{s}\]
<p><span class="box">\(t_{1/2} = 2.77\times10^{14}\) s</span></p>
<p><b>(iv)</b> The rate constant does not depend on time or concentration (only on temperature), so after 5 minutes
it is still <span class="box">\(k = 2.5\times10^{-15}\ \text{s}^{-1}\)</span></p>
<p class="note">The passage's data are not consistent with each other. If the concentration really fell to one-third
in 5 min, then \(k = \dfrac{2.303}{300}\log 3 = 3.66\times10^{-3}\ \text{s}^{-1}\) and \(t_{1/2} = 189\) s. The
answers above use the k the passage states, as the questions ask.</p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>First order: \(k = \dfrac{2.303}{t}\log\dfrac{[A]_0}{[A]}\); unit of k = s<sup>&minus;1</sup>.</li>
<li>\(t_{1/2} = 0.693/k\), independent of concentration.</li>
<li>k changes only with temperature (and catalyst), not with time.</li></ul>"""),
        # ------------------------------------------------------------------ Section B
        SEC("Section B &ndash; 20 Marks"),
        Q("2", 2, r"<p>(i) Conductivity of two electrolytic solutions A and B each one having a concentration of 0.1 M "
          r"are 8.5 &times; 10<sup>&minus;2</sup> S cm<sup>&minus;1</sup> and 4.1 &times; 10<sup>&minus;4</sup> S "
          r"cm<sup>&minus;1</sup> respectively. Which of the two offers less resistance to the flow of current? "
          r"Explain.</p>"
          r"<p>(ii) In each of the following pair which will allow better conduction of electricity. Justify</p>"
          r"<p>a. Copper wire at 25&deg;C and copper wire at 40&deg;C</p><p>b. 0.1 M acetic acid and 1 M acetic acid.</p>",
          a=r"""<p><b>(i)</b> Resistivity \(\rho = 1/\kappa\). A has the larger conductivity (8.5 &times; 10<sup>&minus;2</sup>
&gt; 4.1 &times; 10<sup>&minus;4</sup> S cm<sup>&minus;1</sup>), so for the same cell
\(R = \dfrac{1}{\kappa}\cdot\dfrac{l}{A}\) is smaller. <span class="box">A offers less resistance</span> &mdash; at
equal concentration it furnishes far more ions, i.e. A is a strong electrolyte and B a weak one.</p>
<p><b>(ii) a.</b> <span class="box">Copper wire at 25 &deg;C</span> &mdash; metallic (electronic) conduction
falls as temperature rises, because the vibrating kernels scatter the moving electrons more, so resistance increases
with temperature.</p>
<p><b>b.</b> <span class="box">1 M acetic acid</span> conducts better (higher conductivity): although its degree of
ionisation is lower, 1 L of it contains more ions in all (\([\ce{H+}] \approx \sqrt{K_ac}\): about
\(4.2\times10^{-3}\) M against \(1.3\times10^{-3}\) M for 0.1 M).</p>
<p class="note">The <i>molar</i> conductivity (conducting power per mole) is greater for 0.1 M acetic acid, because
it is more ionised (\(\alpha \approx 1.3\%\) against 0.42% for 1 M). The NCERT Exemplar-style key for this pair
answers "0.1 M acetic acid" on exactly that basis, so in the examination say which quantity you are comparing:
<b>per mole (\(\Lambda_m\), degree of ionisation) &mdash; 0.1 M; per unit volume (\(\kappa\), what a pair of
electrodes sees) &mdash; 1 M</b>. Stating both, with the reason, earns the marks whichever reading the examiner
intends.</p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>\(R = \rho\dfrac{l}{A}\), \(\kappa = 1/\rho\).</li>
<li>Metallic conductance decreases with rise in temperature; electrolytic conductance increases.</li>
<li>Weak electrolyte: \(\alpha \approx \sqrt{K_a/c}\); \([\ce{H+}] = c\alpha \approx \sqrt{K_ac}\).</li></ul>"""),
        Q("3", 2, r"<p>An aromatic compound (A) with molecular formula C<sub>8</sub>H<sub>8</sub>O gives positive 2,4-DNP "
          r"test. It gives a yellow ppt of compound (B) on treatment with iodine and sodium hydroxide solution. "
          r"Compound (A) doesn't give Tollen's or Fehling's test. On drastic oxidation with potassium permanganate it "
          r"forms a carboxylic acid (C) with molecular formula C<sub>7</sub>H<sub>6</sub>O<sub>2</sub>, which is also "
          r"formed along with the yellow compound in the above reaction. When (B) is heated with Ag, a compound D is "
          r"formed which decolourises bromine in CCl<sub>4</sub>. Identify A, B, C, D.</p>",
          a=r"""<p>2,4-DNP positive &rArr; carbonyl; no Tollens'/Fehling's &rArr; ketone; iodoform positive &rArr;
\(\ce{CH3CO-}\); oxidation to \(\ce{C6H5COOH}\) &rArr; one side chain on a benzene ring. Hence A is acetophenone.</p>
{{fig:0}}
<p>\(\ce{C6H5COCH3 + 3I2 + 4NaOH -> C6H5COONa + CHI3 v + 3NaI + 3H2O}\)</p>
<p>\(\ce{2CHI3 + 6Ag ->[\Delta] HC#CH + 6AgI}\) (ethyne, unsaturated, decolourises \(\ce{Br2/CCl4}\))</p>
<p><span class="box">A = acetophenone \(\ce{C6H5COCH3}\); B = iodoform \(\ce{CHI3}\); C = benzoic acid
\(\ce{C6H5COOH}\); D = ethyne (acetylene) \(\ce{C2H2}\)</span></p>""",
          afig=fg.fig_s1_q3_answer,
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>2,4-DNP: all aldehydes and ketones; Tollens'/Fehling's: aldehydes only.</li>
<li>Haloform: \(\ce{RCOCH3 -> RCOO-}\) \(\ce{+ CHX3}\).</li>
<li>Any alkyl side chain on benzene is oxidised by hot alkaline \(\ce{KMnO4}\) to &ndash;COOH.</li>
<li>Iodoform/chloroform + Ag powder, heat &rarr; acetylene.</li></ul>"""),
        Q("4", 2, r"<p>(i) Haloalkanes react with KCN to give alkyl cyanide as the main product while with AgCN they form "
          r"isocyanide as main product. Give reason.</p>"
          r"<p>(ii) Give balanced chemical equation: C<sub>6</sub>H<sub>5</sub>N<sub>2</sub><sup>+</sup>Cl<sup>&minus;</sup> "
          r"treated with Cu/HCl</p>",
          a=r"""<p><b>(i)</b> The cyanide ion is <b>ambident</b>, \(\ce{[:C#N:]-}\), able to bond through C or N. KCN is
ionic, so free \(\ce{CN-}\) ions are available; attack takes place through the carbon atom, which forms the stronger
C&ndash;C bond &rarr; \(\ce{R-C#N}\) (alkyl cyanide). AgCN is mainly <b>covalent</b> (Ag&ndash;C bond), so the carbon
lone pair is tied up; only the nitrogen lone pair is free to attack &rarr; \(\ce{R-N#C}\) (isocyanide).</p>
<p>\(\ce{R-X + KCN -> R-CN + KX}\) &nbsp;&nbsp; \(\ce{R-X + AgCN -> R-NC + AgX}\)</p>
<p><b>(ii)</b> Gattermann reaction:</p>
<p>\(\ce{C6H5N2+Cl- ->[Cu/HCl] C6H5Cl + N2 ^}\)</p>
<p><span class="box">\(\ce{C6H5N2Cl ->[Cu/HCl] C6H5Cl + N2}\) (chlorobenzene)</span></p>""",
          topic="Haloalkanes and Haloarenes",
          recall=r"""<ul><li>Ambident nucleophiles: \(\ce{CN-}\), \(\ce{NO2-}\). Ionic salt &rarr; C (or O) attack;
covalent silver salt &rarr; N attack (isocyanide, nitroalkane).</li>
<li>Sandmeyer: CuCl/HCl; Gattermann: Cu powder/HCl.</li></ul>"""),
        Q("5", 2, r"<p>A hydrogenation reaction is carried out at 500 K. If the same reaction is carried out in presence "
          r"of a catalyst at the same rate, the temperature required is 400 K. Calculate the activation energy of the "
          r"reaction if the catalyst lowers the activation barrier by 20 kJ mol<sup>&minus;1</sup>.</p>",
          a=r"""<p>Arrhenius equation \(k = Ae^{-E_a/RT}\). Same rate &rArr; same k; the catalyst does not change A:</p>
\[Ae^{-E_a/R(500)} = Ae^{-(E_a-20)/R(400)} \;\Rightarrow\; \frac{E_a}{500} = \frac{E_a - 20}{400}\]
\[400\,E_a = 500\,E_a - 10000 \;\Rightarrow\; E_a = 100\ \text{kJ mol}^{-1}\]
<p><span class="box">\(E_a\) (uncatalysed) = 100 kJ mol<sup>&minus;1</sup></span> (catalysed: 80 kJ mol<sup>&minus;1</sup>)</p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>\(k = Ae^{-E_a/RT}\); equal rates &rArr; \(E_a/T\) equal.</li>
<li>A catalyst lowers \(E_a\) by providing an alternative path; A unchanged (assumed).</li></ul>"""),
        Q("6", 2, r"<p>(i) How can the following conversion be brought about &mdash; Ethylamine to Methylamine.</p>"
          r"<p>(ii) Dimethylamine is more basic than trimethylamine in an aqueous solution. Explain.</p>",
          a=r"""<p><b>(i)</b> Step down by one carbon through the amide (Hofmann bromamide):</p>
\[\ce{C2H5NH2 ->[HNO2][(NaNO2+HCl)] C2H5OH ->[K2Cr2O7/H+][\text{oxidation}] CH3COOH}\]
\[\ce{CH3COOH ->[NH3] CH3COONH4 ->[\Delta][-H2O] CH3CONH2 ->[Br2/KOH] CH3NH2}\]
<p>\(\ce{CH3CONH2 + Br2 + 4KOH -> CH3NH2 + K2CO3 + 2KBr + 2H2O}\)</p>
<p><b>(ii)</b> Basicity in water depends on (1) +I effect of alkyl groups, which raises electron density on N;
(2) <b>solvation</b> of the conjugate acid by hydrogen bonding with water; (3) steric hindrance.
\(\ce{(CH3)2NH2+}\) has two N&ndash;H bonds to H-bond with water, \(\ce{(CH3)3NH+}\) only one, so the trimethylammonium
ion is less stabilised; three methyl groups also crowd the nitrogen and hinder approach of \(\ce{H+}\) and of water.
These outweigh the extra +I effect, so dimethylamine is the stronger base
(p<i>K</i><sub>b</sub> 3.27 against 4.22).</p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Hofmann bromamide degradation: \(\ce{RCONH2 -> RNH2}\) (one C less).</li>
<li>Order in water (methyl): 2&deg; &gt; 1&deg; &gt; 3&deg; &gt; \(\ce{NH3}\) &mdash; +I, solvation and steric effects
together.</li></ul>"""),
        Q("7", 2, r"<p>An aqueous solution of cobalt(III) chloride is mixed with liquid ammonia and stirred for 24 hours. "
          r"A violet coloured solid is formed. It is washed with dry ether and the following observations were made.</p>"
          r"<table class='tbl'><tr><td>OBSERVATIONS:</td></tr><tr><td>a. The violet solid has an octahedral geometry "
          r"and produces white ppt with AgNO<sub>3</sub> equivalent to one ionic chlorine.</td></tr><tr><td>b. When "
          r"stirred with excess ammonia an orange solid is formed.</td></tr></table>"
          r"<p><b>Answer the following questions:</b></p>"
          r"<p>(i) State the formula of the violet coloured solid.<br>(ii) The hybridisation of the violet coloured solid "
          r"complex<br>(iii) State the formula of the orange coloured solid<br>(iv) The orange coloured compound is "
          r"&mdash; [choose the correct option]<br>a. homoleptic &nbsp; b. heteroleptic &nbsp; c. inner metallic complex "
          r"&nbsp; d. polynuclear complex</p>",
          a=r"""<p><b>(i)</b> Octahedral (CN 6) with only one ionisable \(\ce{Cl-}\): two \(\ce{Cl-}\) and four
\(\ce{NH3}\) are inside the coordination sphere &mdash;
<span class="box">\(\ce{[Co(NH3)4Cl2]Cl}\)</span> (the violet form is the cis isomer).</p>
<p><b>(ii)</b> \(\ce{Co^3+}\) is 3d<sup>6</sup>; with \(\ce{NH3}\) the six electrons pair in three 3d orbitals,
leaving two 3d orbitals free: <span class="box">d<sup>2</sup>sp<sup>3</sup></span> (inner orbital, diamagnetic).</p>
<p><b>(iii)</b> Excess \(\ce{NH3}\) replaces the two coordinated \(\ce{Cl-}\):
<span class="box">\(\ce{[Co(NH3)6]Cl3}\)</span></p>
<p><b>(iv)</b> All six ligands are the same (\(\ce{NH3}\)): <span class="box">a. homoleptic</span></p>""",
          topic="Coordination Compounds",
          recall=r"""<ul><li>Ions outside [ ] are precipitated by \(\ce{AgNO3}\); coordinated \(\ce{Cl-}\) is not.</li>
<li>Co(III) + \(\ce{NH3}\): low spin, d<sup>2</sup>sp<sup>3</sup>.</li>
<li>Homoleptic: one kind of ligand; heteroleptic: more than one kind.</li></ul>"""),
        Q("8", 2, r"<p>Identify A, B, C, D</p>",
          qfig=fg.fig_s1_q8_scheme,
          a=r"""<p>The starting compound is 2-chloropropane, \(\ce{CH3CHClCH3}\).</p>
<p>\(\ce{CH3CHClCH3 + KOH(alc) ->[\Delta] CH3CH=CH2 + KCl + H2O}\) (dehydrohalogenation)</p>
<p>\(\ce{CH3CH=CH2 + HBr -> CH3CHBrCH3}\) (Markovnikov addition)</p>
<p>\(\ce{CH3CHBrCH3 + NaI -> CH3CHICH3 + NaBr}\) (Finkelstein)</p>
<p>\(\ce{CH3CHICH3 + Mg ->[\text{dry ether}] (CH3)2CHMgI}\) (Grignard reagent)</p>
{{fig:0}}
<p><span class="box">A = propene; B = 2-bromopropane; C = 2-iodopropane; D = isopropylmagnesium iodide</span></p>
<p class="note">The paper writes "dry ether" under NaI; the Finkelstein reaction is normally run in dry acetone, in
which NaI dissolves and the NaBr formed precipitates, driving the reaction forward. The product is the same.</p>""",
          afig=fg.fig_s1_q8_answer,
          topic="Haloalkanes and Haloarenes",
          recall=r"""<ul><li>Alcoholic KOH: elimination (Saytzeff); aqueous KOH: substitution.</li>
<li>Markovnikov: H adds to the carbon with more H.</li>
<li>Finkelstein: R&ndash;Cl/Br + NaI (dry acetone) &rarr; R&ndash;I.</li>
<li>R&ndash;X + Mg (dry ether) &rarr; RMgX.</li></ul>"""),
        Q("9(i)", 2, r"<p>(i) Identify A, B, C, D</p>"
          r"\[\ce{C6H5COOH ->[SOCl2] A ->[NH3] B ->[Br2/KOH] C ->[NaNO2 + HCl][\text{0–5 °C}] D}\]",
          a=r"""<p>\(\ce{C6H5COOH + SOCl2 -> C6H5COCl + SO2 + HCl}\)</p>
<p>\(\ce{C6H5COCl + 2NH3 -> C6H5CONH2 + NH4Cl}\)</p>
<p>\(\ce{C6H5CONH2 + Br2 + 4KOH -> C6H5NH2 + K2CO3 + 2KBr + 2H2O}\) (Hofmann bromamide)</p>
<p>\(\ce{C6H5NH2 + NaNO2 + 2HCl ->[\text{0–5 °C}] C6H5N2+Cl- + NaCl + 2H2O}\) (diazotisation)</p>
<p><span class="box">A = benzoyl chloride; B = benzamide; C = aniline; D = benzenediazonium chloride</span></p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>\(\ce{SOCl2}\) converts &ndash;COOH to &ndash;COCl (by-products gaseous).</li>
<li>Amide + \(\ce{Br2}\)/KOH &rarr; amine with one C less.</li>
<li>Aromatic 1&deg; amine + \(\ce{HNO2}\) at 0&ndash;5 &deg;C &rarr; diazonium salt.</li></ul>"""),
        Q("9(ii) (OR)", 2, r"<p>OR</p><p>(ii) An aromatic carboxylic acid [A] which readily sublimes on heating, "
          r"produces compound [B] on treatment with PCl<sub>5</sub>. Compound [B], when reduced in the presence of Pd "
          r"catalyst over BaSO<sub>4</sub> poisoned by sulphur in xylene solution gives compound [C]. When the compound "
          r"[C] is condensed in the presence of alcoholic KCN, it gives compound [D]. (Molecular formula of compound "
          r"[D] is C<sub>14</sub>H<sub>12</sub>O<sub>2</sub>.) Identify the compounds [A], [B], [C], [D].</p>",
          a=r"""<p>Benzoic acid sublimes; the rest follows:</p>
<p>\(\ce{C6H5COOH + PCl5 -> C6H5COCl + POCl3 + HCl}\)</p>
<p>\(\ce{C6H5COCl + H2 ->[Pd/BaSO4,\ S][\text{xylene}] C6H5CHO + HCl}\) (Rosenmund reduction)</p>
<p>\(\ce{2C6H5CHO ->[\text{alc. KCN}] C6H5CH(OH)COC6H5}\) (benzoin condensation, \(\ce{C14H12O2}\))</p>
<p><span class="box">A = benzoic acid; B = benzoyl chloride; C = benzaldehyde; D = benzoin</span></p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Rosenmund: \(\ce{RCOCl + H2}\) \(\ce{->[Pd/BaSO4] RCHO}\); the poison stops reduction at the
aldehyde.</li><li>Benzoin condensation: two \(\ce{ArCHO}\), \(\ce{CN-}\) catalyst &rarr; \(\ce{ArCH(OH)COAr}\).</li></ul>"""),
        Q("10", 2, r"<p>Calculate the emf of the following cell at 298 K.</p>"
          r"<p>Al/Al<sup>+3</sup>(0.01 M)//Sn<sup>+2</sup>(0.015 M)/Sn</p>"
          r"<p>E<sup>0</sup><sub>Al<sup>+3</sup>/Al</sub> = &minus;1.66 V and E<sup>0</sup><sub>Sn<sup>+2</sup>/Sn</sub> "
          r"= &minus;0.14 V</p>",
          a=r"""<p>Cell reaction (n = 6): \(\ce{2Al + 3Sn^2+ -> 2Al^3+ + 3Sn}\)</p>
\[E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode} = -0.14 - (-1.66) = 1.52\ \text{V}\]
\[E_{cell} = E^\circ_{cell} - \frac{0.0591}{n}\log\frac{[\ce{Al^3+}]^2}{[\ce{Sn^2+}]^3}
= 1.52 - \frac{0.0591}{6}\log\frac{(0.01)^2}{(0.015)^3}\]
\[\frac{(0.01)^2}{(0.015)^3} = \frac{1\times10^{-4}}{3.375\times10^{-6}} = 29.63,\quad \log 29.63 = 1.472\]
\[E_{cell} = 1.52 - 0.00985\times1.472 = 1.52 - 0.0145 = 1.5055\ \text{V}\]
<p><span class="box">\(E_{cell} \approx 1.51\) V</span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>Nernst (298 K): \(E = E^\circ - \dfrac{0.0591}{n}\log Q\), Q = [products]/[reactants]
with powers; solids omitted.</li><li>n = LCM of electrons in the two half-reactions (3 and 2 &rArr; 6).</li></ul>"""),
        Q("11", 2, r"<p>Write the chemical test to distinguish between the following pairs of compounds:</p>"
          r"<p>(i) Phenol and cyclohexanol<br>(ii) Ethanol and isopropanol</p>",
          a=r"""<p><b>(i) Neutral ferric chloride test:</b> phenol gives a <b>violet</b> colour; cyclohexanol gives no
colour.</p>
<p>\(\ce{6C6H5OH + FeCl3 -> [Fe(OC6H5)6]^3- + 3H+ + 3HCl}\) (violet complex)</p>
<p>(Also: phenol gives a white ppt of 2,4,6-tribromophenol with bromine water; cyclohexanol does not.)</p>
<p><b>(ii) Lucas test</b> (conc. HCl + anhydrous \(\ce{ZnCl2}\), room temperature): isopropanol (2&deg;) turns
<b>turbid in about 5 minutes</b> (insoluble 2-chloropropane separates); ethanol (1&deg;) shows no turbidity at room
temperature.</p>
<p>\(\ce{(CH3)2CHOH + HCl ->[ZnCl2] (CH3)2CHCl + H2O}\)</p>
<p class="note">The iodoform test does <b>not</b> distinguish this pair: ethanol (\(\ce{CH3CH2OH}\)) and isopropanol
(\(\ce{CH3CH(OH)CH3}\)) both contain \(\ce{CH3CH(OH)-}\) and both give yellow \(\ce{CHI3}\).</p>""",
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Phenols: violet/purple colour with neutral \(\ce{FeCl3}\); alcohols do not.</li>
<li>Lucas: 3&deg; immediate, 2&deg; ~5 min, 1&deg; no turbidity at room temperature.</li></ul>"""),
        # ------------------------------------------------------------------ Section C
        SEC("Section C &ndash; 21 Marks"),
        Q("12", 3, r"<p>Identify A, B in each of the following:</p>"
          r"<p>i. \(\ce{C6H5N2+Cl- ->[CuCN][\Delta] A ->[H2O/H+] B}\)</p>"
          r"<p>ii. \(\ce{C6H5NO2 ->[Sn/HCl] A ->[Br2/H2O] B}\)</p>"
          r"<p>iii.</p>",
          qfig=fg.fig_s1_q12_scheme,
          a=r"""<p><b>i.</b> \(\ce{C6H5N2Cl + CuCN ->[\Delta] C6H5CN + N2 + CuCl}\) (Sandmeyer)<br>
\(\ce{C6H5CN + 2H2O ->[H+] C6H5COOH + NH4+}\)<br>
<span class="box">A = benzonitrile (phenyl cyanide); B = benzoic acid</span></p>
<p><b>ii.</b> \(\ce{C6H5NO2 + 6[H] ->[Sn/HCl] C6H5NH2 + 2H2O}\)<br>
\(\ce{C6H5NH2 + 3Br2(aq) -> C6H2Br3NH2 v + 3HBr}\) (white ppt)<br>
<span class="box">A = aniline; B = 2,4,6-tribromoaniline</span></p>
<p><b>iii.</b> Aniline forms a salt with conc. \(\ce{H2SO4}\); on heating at 453&ndash;473 K the salt loses water and
rearranges to the para sulphonic acid:</p>
<p>\(\ce{C6H5NH2 + H2SO4 -> C6H5NH3+HSO4-}\) &nbsp; \(\ce{C6H5NH3+HSO4- ->[453–473 K] H2NC6H4SO3H + H2O}\)</p>
{{fig:0}}
<p><span class="box">A = anilinium hydrogensulphate; B = sulphanilic acid (p-aminobenzenesulphonic acid), which exists
as a zwitterion</span></p>""",
          afig=fg.fig_s1_q12_answer,
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Sandmeyer: \(\ce{ArN2+}\) &rarr; ArCl, ArBr, ArCN with CuCl/CuBr/CuCN.</li>
<li>Nitriles hydrolyse to acids.</li><li>&ndash;NH<sub>2</sub> strongly activates: bromine water gives the
tribromo compound directly.</li><li>Sulphonation of aniline: para product, sulphanilic acid
(\(\ce{H3N+C6H4SO3-}\)).</li></ul>"""),
        Q("13", 3, r"""<p>Henna is investigating the melting point of different salt solutions.
She makes a salt solution using 10 mL of water with a known mass of NaCl salt. She puts the salt solution into a
freezer and leaves it to freeze. She takes the frozen salt solution out of the freezer and measures the temperature
when the frozen salt solution melts. She repeats each experiment.</p>
<div class="tbl"><table><tr><th rowspan="2">S.No</th><th rowspan="2">Mass of the salt used in g</th>
<th colspan="2">Melting point in &deg;C</th></tr><tr><th>Readings Set 1</th><th>Reading Set 2</th></tr>
<tr><td>1</td><td>0.3</td><td>&minus;1.9</td><td>&minus;1.9</td></tr>
<tr><td>2</td><td>0.4</td><td>&minus;2.5</td><td>&minus;2.6</td></tr>
<tr><td>3</td><td>0.5</td><td>&minus;3.0</td><td>&minus;5.5</td></tr>
<tr><td>4</td><td>0.6</td><td>&minus;3.8</td><td>&minus;3.8</td></tr>
<tr><td>5</td><td>0.8</td><td>&minus;5.1</td><td>&minus;5.0</td></tr>
<tr><td>6</td><td>1.0</td><td>&minus;6.4</td><td>&minus;6.3</td></tr></table></div>
<p>Assuming the melting point of pure water as 0&deg; C, answer the following questions:</p>
<p>(i) One temperature in the second set of results does not fit the pattern. Which temperature is that?<br>
(ii) Why did Henna collect two sets of results?<br>
(iii) In place of NaCl, if Henna had used glucose, what would have been the melting point of the solution with 0.6 g
glucose in it?</p>""",
          a=r"""<p><b>(i)</b> The depression rises steadily with the mass of salt (about 6.3 &deg;C per gram). For 0.5 g Set 1
gives &minus;3.0 &deg;C, between &minus;2.6 and &minus;3.8; Set 2's <span class="box">&minus;5.5 &deg;C</span> (for
0.5 g) is far off the line &mdash; an anomalous reading.</p>
{{fig:0}}
<p><b>(ii)</b> To check that the results are <b>repeatable/reliable</b>: repeating each measurement lets anomalous
readings (like &minus;5.5 &deg;C) be spotted and discarded, and the two concordant values can be averaged to reduce
random error.</p>
<p><b>(iii)</b> Glucose is a non-electrolyte (\(i = 1\)); NaCl gives two ions (\(i \approx 2\)). From Henna's own
data for 0.6 g NaCl:</p>
\[K_f = \frac{\Delta T_f}{i\,m} = \frac{3.8}{2\times\dfrac{0.6/58.5}{0.010}} = \frac{3.8}{2\times1.026} = 1.85\ \text{K kg mol}^{-1}\]
<p>(the accepted value for water, 1.86 K kg mol<sup>&minus;1</sup>). For 0.6 g glucose (M = 180) in 10 g water:</p>
\[m = \frac{0.6/180}{0.010} = 0.333\ \text{mol kg}^{-1},\qquad \Delta T_f = K_f\,m = 1.86\times0.333 = 0.62\ \text{K}\]
<p><span class="box">Melting point \(\approx -0.62\) &deg;C</span></p>""",
          afig=fg.fig_s1_q13_graph,
          topic="Solutions",
          recall=r"""<ul><li>\(\Delta T_f = i K_f m\); \(m\) = moles of solute per kg of solvent.</li>
<li>NaCl \(i \approx 2\); glucose \(i = 1\).</li>
<li>Repeat readings to check reliability and identify anomalies.</li></ul>"""),
        Q("14", 3, r"<p>Give balanced chemical equations with conditions where necessary for the following name "
          r"reactions:</p><p>(i) Wolff-Kishner reduction<br>(ii) Perkin reaction.<br>(iii) Etard reaction.</p>",
          a=r"""<p><b>(i) Wolff&ndash;Kishner reduction</b> &mdash; C=O to \(\ce{CH2}\) with hydrazine and KOH in ethylene
glycol, heated (453&ndash;473 K):</p>
<p>\(\ce{(CH3)2C=O + NH2NH2 ->[-H2O] (CH3)2C=NNH2}\) (hydrazone)<br>
\(\ce{(CH3)2C=NNH2 ->[KOH/\text{ethylene glycol}][\Delta] CH3CH2CH3 + N2 ^}\)</p>
<p><b>(ii) Perkin reaction</b> &mdash; aromatic aldehyde + acid anhydride with the sodium salt of the same acid,
heated (~453 K):</p>
<p>\(\ce{C6H5CHO + (CH3CO)2O ->[CH3COONa][453 K] C6H5CH=CHCOOH + CH3COOH}\) (cinnamic acid)</p>
<p><b>(iii) Etard reaction</b> &mdash; toluene oxidised by chromyl chloride in \(\ce{CS2}\) (or \(\ce{CCl4}\)) to a
brown chromium complex, which is hydrolysed:</p>
<p>\(\ce{C6H5CH3 + 2CrO2Cl2 ->[CS2] C6H5CH(OCrOHCl2)2 ->[H3O+] C6H5CHO}\) (benzaldehyde)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Wolff&ndash;Kishner (basic) and Clemmensen (Zn&ndash;Hg/HCl, acidic): C=O &rarr; \(\ce{CH2}\).</li>
<li>Perkin: \(\ce{ArCHO}\) &rarr; \(\ce{ArCH=CHCOOH}\).</li><li>Etard: \(\ce{ArCH3}\) &rarr; \(\ce{ArCHO}\) by
\(\ce{CrO2Cl2}\).</li></ul>"""),
        Q("15", 3, r"<p>A metal complex having composition <b>Cr(NH<sub>3</sub>)<sub>4</sub>Cl<sub>2</sub>Br</b> has been "
          r"isolated in two forms A and B. The form A reacts with AgNO<sub>3</sub> to give a white precipitate readily "
          r"soluble in dilute aqueous ammonia whereas B gives a pale yellow precipitate soluble in concentrated "
          r"ammonia.</p><p>(i) State the hybridisation of Chromium in each of them.<br>(ii) State the formula of A and B "
          r"respectively.<br>(iii) Calculate the magnetic moment (spin only value) of the isomer A<br>(iv) State the IUPAC "
          r"name of isomer B and the geometry of the complex.</p>",
          a=r"""<p>White ppt soluble in dilute \(\ce{NH3}\) = AgCl &rArr; in A the counter-ion is \(\ce{Cl-}\). Pale yellow
ppt soluble only in conc. \(\ce{NH3}\) = AgBr &rArr; in B the counter-ion is \(\ce{Br-}\). A and B are
<b>ionisation isomers</b>.</p>
<p><b>(i)</b> Cr is +3 in both (3d<sup>3</sup>); the three electrons occupy three 3d orbitals, two 3d orbitals are
empty: <span class="box">d<sup>2</sup>sp<sup>3</sup> in both</span></p>
{{fig:0}}
<p><b>(ii)</b> <span class="box">A = \(\ce{[Cr(NH3)4ClBr]Cl}\); B = \(\ce{[Cr(NH3)4Cl2]Br}\)</span></p>
<p><b>(iii)</b> n = 3 unpaired electrons:
\(\mu = \sqrt{n(n+2)} = \sqrt{15} = 3.87\) BM. <span class="box">3.87 BM</span></p>
<p><b>(iv)</b> <span class="box">Tetraamminedichloridochromium(III) bromide; octahedral</span></p>
{{fig:1}}""",
          afig=[fg.fig_s1_q15_vbt, (fg.fig_s1_q15_isomers, "The two cations, drawn with the halides trans; cis forms also exist (geometrical isomers).")],
          topic="Coordination Compounds",
          recall=r"""<ul><li>AgCl white, soluble in dil. \(\ce{NH3}\); AgBr pale yellow, sparingly soluble (conc.
\(\ce{NH3}\)); AgI yellow, insoluble.</li><li>Ionisation isomers exchange a ligand and a counter-ion.</li>
<li>\(\mu = \sqrt{n(n+2)}\) BM.</li><li>IUPAC: ligands alphabetical (ammine before chlorido), then metal with
oxidation state.</li></ul>"""),
        Q("16(i)", 3, r"<p>(i) a. What type of cell is a lead storage battery?<br>b. Write the anode and cathode "
          r"reactions occurring during the use of a lead storage battery.<br>c. Two metallic elements A and B have the "
          r"following oxidation potentials: A = 0.40 V, B = &minus;0.80 V. What would you expect if the element A was "
          r"added to an aqueous salt solution of element B?</p>",
          a=r"""<p><b>a.</b> A <span class="box">secondary (rechargeable) cell</span> &mdash; the cell reaction can be reversed
by passing current from an external source.</p>
<p><b>b.</b> During use (discharge), electrolyte 38% \(\ce{H2SO4}\):</p>
<p>Anode (Pb): \(\ce{Pb(s) + SO4^2-(aq) -> PbSO4(s) + 2e-}\)</p>
<p>Cathode (\(\ce{PbO2}\) on a lead grid): \(\ce{PbO2(s) + SO4^2-(aq) + 4H+(aq) + 2e- -> PbSO4(s) + 2H2O(l)}\)</p>
<p>Overall: \(\ce{Pb + PbO2 + 2H2SO4 -> 2PbSO4 + 2H2O}\)</p>
<p><b>c.</b> A has the higher oxidation potential (+0.40 V &gt; &minus;0.80 V), so A is the stronger reducing agent:
it is oxidised and <b>displaces B</b> from the solution &mdash; A dissolves and metal B is deposited
(\(E^\circ_{cell} = 0.40 - (-0.80) = +1.20\) V &gt; 0, spontaneous).</p>
<p><span class="box">A + B<sup>n+</sup> &rarr; A<sup>n+</sup> + B: A displaces B</span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>Primary cells (dry cell, mercury cell) cannot be recharged; secondary (lead storage,
Ni&ndash;Cd) can.</li><li>Higher oxidation potential (lower reduction potential) &rArr; stronger reducing agent,
displaces the other metal.</li></ul>"""),
        Q("16(ii) (OR)", 3, r"<p>OR</p><p>(ii) Conductivity of 0.00241 M acetic acid is 7.896 &times; 10<sup>&minus;5</sup> "
          r"S cm<sup>&minus;1</sup>. Calculate the molar conductivity and if \(\lambda^0\) for acetic acid is 390.5 S "
          r"cm<sup>2</sup> mol<sup>&minus;1</sup>, what is its dissociation constant?</p>",
          a=r"""\[\Lambda_m = \frac{1000\,\kappa}{c} = \frac{1000\times7.896\times10^{-5}}{0.00241} = 32.76\ \text{S cm}^2\,\text{mol}^{-1}\]
\[\alpha = \frac{\Lambda_m}{\Lambda_m^\circ} = \frac{32.76}{390.5} = 0.0839\]
\[K_a = \frac{c\alpha^2}{1-\alpha} = \frac{0.00241\times(0.0839)^2}{1 - 0.0839} = 1.85\times10^{-5}\ \text{mol L}^{-1}\]
<p><span class="box">\(\Lambda_m = 32.76\) S cm<sup>2</sup> mol<sup>&minus;1</sup>; \(K_a = 1.85\times10^{-5}\)</span>
(using \(K_a \approx c\alpha^2\) gives \(1.70\times10^{-5}\))</p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>\(\Lambda_m = 1000\kappa/c\) (c in mol L<sup>&minus;1</sup>).</li>
<li>Weak electrolyte: \(\alpha = \Lambda_m/\Lambda_m^\circ\); Ostwald: \(K_a = c\alpha^2/(1-\alpha)\).</li></ul>"""),
        Q("17", 3, r"<p>(i) A non-reducing disaccharide [A] on hydrolysis with dilute acid gives an equimolar mixture of "
          r"D(+) glucose and D(&minus;) Fructose.</p>"
          r"<div class='tbl'><table><tr><td>A</td><td>+ H<sub>2</sub>O</td><td>&rarr;</td>"
          r"<td>C<sub>6</sub>H<sub>12</sub>O<sub>6</sub></td><td>+</td><td>C<sub>6</sub>H<sub>12</sub>O<sub>6</sub></td></tr>"
          r"<tr><td>[&alpha;]<sub>D</sub> = +66.5&deg;</td><td></td><td></td><td>= +52.5&deg;</td><td></td>"
          r"<td>= &minus;92.4&deg;</td></tr></table></div>"
          r"<p>a. Identify A.<br>b. What is the mixture of D(+) glucose and D(&minus;) Fructose known as?<br>c. Name the "
          r"linkage that holds the two units in the disaccharide.</p>"
          r"<p>(ii) What is isoelectric point?</p><p>(iii) Name the product formed when Glucose is heated with HI</p>",
          a=r"""<p><b>(i) a.</b> <span class="box">A = sucrose (cane sugar), \(\ce{C12H22O11}\)</span></p>
<p>\(\ce{C12H22O11 + H2O ->[H+] C6H12O6 (glucose) + C6H12O6 (fructose)}\)</p>
<p><b>b.</b> <span class="box">Invert sugar</span> &mdash; the sign of rotation changes from dextro (+66.5&deg;) to
laevo, because fructose (&minus;92.4&deg;) rotates more strongly than glucose (+52.5&deg;): net
\((52.5 - 92.4)/2 \approx -20\)&deg;.</p>
<p><b>c.</b> <span class="box">Glycosidic linkage</span> &mdash; between C1 of \(\alpha\)-D-glucose and C2 of
\(\beta\)-D-fructose (\(\alpha 1\to\beta 2\)); both reducing groups are used up, so sucrose is non-reducing.</p>
<p><b>(ii)</b> The <b>isoelectric point</b> is the pH at which an amino acid exists mainly as the dipolar ion
(zwitterion, \(\ce{H3N+-CHR-COO-}\)) with no net charge, so it does not migrate in an electric field.</p>
<p><b>(iii)</b> <span class="box">n-hexane</span>:
\(\ce{CHO-(CHOH)4-CH2OH ->[HI][\Delta] CH3-CH2-CH2-CH2-CH2-CH3}\) &mdash; evidence that the six carbons of glucose are
in a straight chain.</p>""",
          topic="Biomolecules",
          recall=r"""<ul><li>Sucrose: glucose + fructose, \(\alpha 1\to\beta 2\) glycosidic bond; non-reducing.</li>
<li>Inversion: dextro sucrose &rarr; laevo invert sugar.</li>
<li>Glucose + HI/heat &rarr; n-hexane (straight chain).</li></ul>"""),
        Q("18", 3, r"""<p>For the equation, A + B &rarr; C + D. The following results were obtained to determine the initial
rate of the reaction.</p>
<div class="tbl"><table><tr><th>Experiment</th><th>[A] mol L<sup>&minus;1</sup></th><th>[B] mol L<sup>&minus;1</sup></th>
<th>Initial rate [mol L<sup>&minus;1</sup> sec<sup>&minus;1</sup>]</th></tr>
<tr><td>1</td><td>1.0</td><td>1.0</td><td>2 &times; 10<sup>&minus;3</sup></td></tr>
<tr><td>2</td><td>2.0</td><td>1.0</td><td>4 &times; 10<sup>&minus;3</sup></td></tr>
<tr><td>3</td><td>4.0</td><td>1.0</td><td>8 &times; 10<sup>&minus;3</sup></td></tr>
<tr><td>4</td><td>1.0</td><td>2.0</td><td>2 &times; 10<sup>&minus;3</sup></td></tr>
<tr><td>5</td><td>1.0</td><td>4.0</td><td>2 &times; 10<sup>&minus;3</sup></td></tr></table></div>
<p>i) What is the order of reaction with respect to A and B? Justify.<br>ii) State the overall order. Write down the
rate law equation.<br>iii) What is the value of rate constant?</p>""",
          a=r"""<p>Let rate = \(k[A]^x[B]^y\).</p>
<p><b>(i)</b> Experiments 1 &rarr; 2 &rarr; 3 ([B] fixed): doubling [A] doubles the rate,
\(\dfrac{4\times10^{-3}}{2\times10^{-3}} = 2 = 2^x\) &rArr; <span class="box">x = 1 (first order in A)</span>.<br>
Experiments 1 &rarr; 4 &rarr; 5 ([A] fixed): doubling or quadrupling [B] leaves the rate unchanged, \(1 = 2^y\)
&rArr; <span class="box">y = 0 (zero order in B)</span>.</p>
<p><b>(ii)</b> Overall order = 1 + 0 = <span class="box">1; Rate = k[A]</span></p>
<p><b>(iii)</b> From experiment 1: \(k = \dfrac{\text{rate}}{[A]} = \dfrac{2\times10^{-3}\ \text{mol L}^{-1}\text{s}^{-1}}{1.0\ \text{mol L}^{-1}}\)
= <span class="box">\(2\times10^{-3}\ \text{s}^{-1}\)</span> (the same from every experiment).</p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>Initial-rate method: change one concentration, keep the others fixed;
\(\text{rate ratio} = (\text{conc. ratio})^{\text{order}}\).</li><li>Unit of k for first order: s<sup>&minus;1</sup>.</li></ul>"""),
        # ------------------------------------------------------------------ Section D
        SEC("Section D &ndash; 15 Marks"),
        Q("19", 5, r"""<p>An exciting direction in amine research is their application in artificial photosynthesis. A 2024
study published in Science demonstrated the use of amine-based catalysts for CO<sub>2</sub> reduction, which is a key
step in the development of artificial photosynthesis systems that mimic the natural process plants use to convert
sunlight into energy. Researchers found that amine-modified catalysts could efficiently reduce CO<sub>2</sub> into
useful chemical fuels, such as methanol and ethanol, under mild conditions using sunlight. The amines acted as proton
donors, facilitating the necessary chemical reactions for the conversion of CO<sub>2</sub> into fuel.</p>
<p>(i) Answer the following questions:<br>i. Give balanced equation in each case:<br>a. Benzene diazonium chloride is
treated with alkaline solution of Phenol at 0&deg;C<br>b. Aniline is treated with Chloroform and alc KOH and heated.</p>
<p>(ii) Arrange the following in order of their increasing basic strength:<br>a. NH<sub>3</sub>,
C<sub>6</sub>H<sub>5</sub>NH<sub>2</sub>, CH<sub>3</sub>NH<sub>2</sub>, (CH<sub>3</sub>)<sub>2</sub>NH [in aqueous
solution]<br>b. aniline, p-nitroaniline, p-methylaniline</p>
<p>(iii) Distinguish using chemical test in each case: Aniline and Diethylaniline</p>""",
          a=r"""<p><b>(i) a.</b> Coupling reaction (para position of phenol, alkaline medium, 0 &deg;C):</p>
<p>\(\ce{C6H5N2+Cl- + C6H5OH + NaOH ->[0 °C] C6H5-N=N-C6H4OH + NaCl + H2O}\)</p>
{{fig:0}}
<p>p-hydroxyazobenzene, an orange dye.</p>
<p><b>b.</b> Carbylamine reaction:</p>
<p>\(\ce{C6H5NH2 + CHCl3 + 3KOH(alc) ->[\Delta] C6H5NC + 3KCl + 3H2O}\) (phenyl isocyanide, offensive smell)</p>
<p><b>(ii) a.</b> <span class="box">\(\ce{C6H5NH2 < NH3 < CH3NH2 < (CH3)2NH}\)</span> &mdash; in aniline the lone pair
is delocalised into the ring; alkyl groups (+I) and solvation raise basicity, 2&deg; &gt; 1&deg; in water.</p>
<p><b>b.</b> <span class="box">p-nitroaniline &lt; aniline &lt; p-methylaniline</span> &mdash; &ndash;NO<sub>2</sub>
(&minus;R, &minus;I) withdraws electron density from N; &ndash;CH<sub>3</sub> (+I, hyperconjugation) releases it.</p>
<p><b>(iii)</b> <b>Carbylamine test:</b> warm each with \(\ce{CHCl3}\) and alcoholic KOH. Aniline (1&deg;) gives the
offensive smell of phenyl isocyanide; N,N-diethylaniline (3&deg;, no N&ndash;H) gives no such smell.</p>
<p>(Alternatively, <b>Hinsberg's test</b>: aniline gives a sulphonamide soluble in KOH; N,N-diethylaniline does not
react with benzenesulphonyl chloride.)</p>""",
          afig=fg.fig_s1_q19_azo,
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Coupling: \(\ce{ArN2+}\) attacks the para position of phenol (mildly alkaline) or aniline
(mildly acidic).</li><li>Carbylamine: only 1&deg; amines.</li>
<li>Basic strength: electron-donating groups increase, electron-withdrawing groups decrease;
aryl amines &lt; \(\ce{NH3}\) &lt; alkyl amines.</li></ul>"""),
        Q("20", 5, r"""<p>(i) Explain why:<br>a. transition elements form alloys?<br>b. Zn<sup>+2</sup> salts are white
whereas Cu<sup>+2</sup> salts are coloured?<br>c. transition metals and their compounds act as catalyst?</p>
<p>(ii) Complete and balance the following equations:<br>a. KMnO<sub>4</sub> + H<sub>2</sub>SO<sub>4</sub> +
H<sub>2</sub>C<sub>2</sub>O<sub>4</sub> &rarr;<br>b. K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> + H<sub>2</sub>SO<sub>4</sub> +
FeSO<sub>4</sub> &rarr;</p>""",
          a=r"""<p><b>(i) a.</b> Transition metals have <b>similar atomic radii</b> (within about 15%) and similar
metallic lattice/bonding characteristics, so atoms of one metal can readily take the place of atoms of another in the
crystal lattice, forming substitutional solid solutions (alloys), e.g. brass, bronze, steels.</p>
<p><b>b.</b> Colour arises from <b>d&ndash;d transitions</b>: in the ligand field the d orbitals split and an electron
absorbs visible light in jumping to the higher level; the complementary colour is seen. \(\ce{Zn^2+}\) is
3d<sup>10</sup> &mdash; d orbitals full, no d&ndash;d transition, so white. \(\ce{Cu^2+}\) is 3d<sup>9</sup> with a
vacancy &mdash; d&ndash;d transition possible; it absorbs in the red/orange region and appears blue.</p>
<p><b>c.</b> Transition metals show <b>variable oxidation states</b>, so they can form unstable intermediates and
change oxidation state in a redox cycle; they also provide a <b>large surface</b> with free valencies (vacant d
orbitals) to adsorb reactants, weakening their bonds and lowering the activation energy (e.g. Fe in Haber process,
\(\ce{V2O5}\) in contact process, Ni in hydrogenation).</p>
<p><b>(ii) a.</b> \(\ce{2KMnO4 + 3H2SO4 + 5H2C2O4 -> K2SO4 + 2MnSO4 + 10CO2 + 8H2O}\)</p>
<p>(ionic: \(\ce{2MnO4- + 5C2O4^2- + 16H+ -> 2Mn^2+ + 10CO2 + 8H2O}\))</p>
<p><b>b.</b> \(\ce{K2Cr2O7 + 7H2SO4 + 6FeSO4 -> K2SO4 + Cr2(SO4)3 + 3Fe2(SO4)3 + 7H2O}\)</p>
<p>(ionic: \(\ce{Cr2O7^2- + 6Fe^2+ + 14H+ -> 2Cr^3+ + 6Fe^3+ + 7H2O}\))</p>""",
          topic="d- and f-Block Elements",
          recall=r"""<ul><li>Colour needs an incompletely filled d subshell (d<sup>1</sup>&ndash;d<sup>9</sup>).</li>
<li>Catalysis: variable oxidation states + adsorption on surface.</li>
<li>Acidic \(\ce{MnO4-}\) gains 5e<sup>&minus;</sup>; \(\ce{Cr2O7^2-}\) gains 6e<sup>&minus;</sup>; \(\ce{C2O4^2-}\)
loses 2e<sup>&minus;</sup>, \(\ce{Fe^2+}\) loses 1e<sup>&minus;</sup>.</li></ul>"""),
        Q("21 I", 5, r"""<p>Colligative properties, traditionally defined as those that depend on the number of solute
particles rather than their identity (such as boiling point elevation, freezing point depression, osmotic pressure,
and vapor pressure lowering), can be explored in new ways when applied to smart nanomaterials. These materials could
change their behavior in response to environmental conditions, allowing for adaptive responses based on external
stimuli like temperature, pressure, or pH. In this idea, the traditional colligative properties could be used to
design next-generation, self-regulating nanomaterials that can respond dynamically to changes in their
surroundings.</p>
<p><b>Based on colligative properties answer the following questions:</b></p>
<p><b>I.</b> (i) The vapour pressure vs. composition diagram of an ideal binary solution of A and B is given below&mdash;</p>
{{fig:0}}
<p>The vapour pressure of pure liquids A and B are 450 and 700 mm Hg respectively, at 350 K.<br>
a. Find out the composition of the liquid mixture if total vapour pressure is 600 mm Hg.<br>
b. What is the composition of the vapour phase?</p>
<p>(ii) The osmotic pressure of a 50 g of 500 ml polymer solution linearly varies with temperature as</p>
{{fig:1}}
<p>If the slope of the plot is 1.23 &times; 10<sup>&minus;4</sup> atm K<sup>&minus;1</sup>,<br>a. what is the molar
mass of the polymer?<br>b. If the temperature of this solution is doubled, by how much factor the osmotic pressure will
change?</p>
<p>(iii) Assume three samples of juices A, B and C have glucose as the only sugar present in them. The concentration of
sample A, B and C are 0.1 M, 0.5 M and 0.2 M respectively. Freezing point will be highest for the fruit juice:<br>
(a) A &nbsp; (b) B &nbsp; (c) C &nbsp; (d) All have same freezing point</p>""",
          qfig=[(fg.fig_s1_q21_vp_printed, ""), (fg.fig_s1_q21_osmotic, "The paper labels the horizontal axis C; the text and the slope's unit (atm K<sup>&minus;1</sup>) show it is temperature.")],
          a=r"""<p><b>(i) a.</b> Raoult's law: \(P = p_A^\circ x_A + p_B^\circ(1 - x_A)\)</p>
\[600 = 450\,x_A + 700(1 - x_A) \;\Rightarrow\; 250\,x_A = 100 \;\Rightarrow\; x_A = 0.40,\ x_B = 0.60\]
<p><b>b.</b> Dalton's law: \(y_A = \dfrac{p_A}{P} = \dfrac{450\times0.40}{600} = \dfrac{180}{600} = 0.30\),
\(y_B = \dfrac{700\times0.60}{600} = \dfrac{420}{600} = 0.70\)</p>
<p><span class="box">Liquid: \(x_A = 0.4,\ x_B = 0.6\); vapour: \(y_A = 0.3,\ y_B = 0.7\)</span> (the vapour is
richer in the more volatile B)</p>
{{fig:0}}
<p><b>(ii) a.</b> \(\pi = CRT = \dfrac{w}{MV}RT\), so a plot of \(\pi\) against T is a straight line through the
origin with slope \(\dfrac{wR}{MV}\):</p>
\[M = \frac{wR}{V\times\text{slope}} = \frac{50\ \text{g}\times0.0821\ \text{L atm K}^{-1}\text{mol}^{-1}}{0.500\ \text{L}\times1.23\times10^{-4}\ \text{atm K}^{-1}}
= 6.67\times10^{4}\ \text{g mol}^{-1}\]
<p><span class="box">M \(\approx 6.67\times10^4\) g mol<sup>&minus;1</sup></span></p>
<p><b>b.</b> \(\pi \propto T\) (absolute temperature) at fixed concentration: doubling T (in kelvin) doubles
\(\pi\). <span class="box">Factor 2</span></p>
<p><b>(iii)</b> \(\Delta T_f = K_f m\) is least for the most dilute juice, so its freezing point is highest:
<span class="box">(a) A</span></p>""",
          afig=(fg.fig_s1_q21_vp_answer, "To scale: total pressure 600 mm Hg at x<sub>B</sub> = 0.6."),
          topic="Solutions",
          recall=r"""<ul><li>Raoult: \(p_i = p_i^\circ x_i\); Dalton: \(y_i = p_i/P\).</li>
<li>van't Hoff: \(\pi = CRT = \dfrac{wRT}{MV}\).</li>
<li>Higher concentration &rArr; larger \(\Delta T_f\) &rArr; lower freezing point.</li></ul>"""),
        Q("21 II (OR)", 5, r"""<p>OR</p>
<p><b>II.</b> (i) Henry's law and Henry's law constant are widely used in determining the solubility of different gas
under different conditions.</p>
<div class="tbl"><table><tr><th>Gas</th><th>K<sub>H</sub> (atm)</th></tr>
<tr><td>He</td><td>1.514 &times; 10<sup>5</sup></td></tr><tr><td>O<sub>2</sub></td><td>5.32 &times; 10<sup>4</sup></td></tr>
<tr><td>N<sub>2</sub></td><td>2.66 &times; 10<sup>5</sup></td></tr></table></div>
<p>a) Arrange the gases in increasing order of solubility<br>b) At what partial pressure would the O<sub>2</sub> gas have
solubility (in water) of 2 &times; 10<sup>&minus;5</sup> M?</p>
<p>(ii) Ramesh took 10 g of glucose to prepare 500 ml aqueous solution of it and observed the boiling point of the
solution as 100.05 &deg;C. Now, he prepared two more solutions:<br>a. 10 g sucrose dissolved in 500 ml water<br>
b. 10 g glucose in 500 ml acetic acid<br>Does the boiling point will remain same in each case? Justify your answer</p>
<p>(iii) Measurement of colligative property of a solution is frequently used to determine the molar mass of an unknown
solute. The common methods are elevation of boiling point, depression of freezing point and osmotic pressure. If we
would like to determine the molar mass of a polymer, which method is most suitable among them? Justify your answer.</p>""",
          a=r"""<p><b>(i) a.</b> Henry's law \(p = K_H x\): at a given pressure the mole fraction dissolved
\(x = p/K_H\), so the <b>larger</b> \(K_H\), the <b>lower</b> the solubility.
\(K_H\): \(\ce{N2}\) (2.66 &times; 10<sup>5</sup>) &gt; He (1.514 &times; 10<sup>5</sup>) &gt; \(\ce{O2}\)
(5.32 &times; 10<sup>4</sup>).</p>
<p><span class="box">Solubility: \(\ce{N2}\) &lt; He &lt; \(\ce{O2}\)</span></p>
<p><b>b.</b> 2 &times; 10<sup>&minus;5</sup> M: in 1 L (&asymp; 1000 g) water, \(n(\ce{H2O}) = 1000/18 = 55.56\)
mol, so</p>
\[x_{\ce{O2}} = \frac{2\times10^{-5}}{55.56 + 2\times10^{-5}} \approx 3.6\times10^{-7}\]
\[p_{\ce{O2}} = K_H\,x = 5.32\times10^{4}\ \text{atm}\times3.6\times10^{-7} = 1.92\times10^{-2}\ \text{atm}\]
<p><span class="box">\(p_{\ce{O2}} \approx 0.019\) atm</span></p>
<p><b>(ii)</b> No. \(\Delta T_b = K_b\,m = K_b\dfrac{w_2\times1000}{M_2\,w_1}\).</p>
<p>a. Sucrose (M = 342) in the same water: the same 10 g gives fewer moles than glucose (M = 180), so
\(\Delta T_b = 0.05\times\dfrac{180}{342} \approx 0.026\) K. Boiling point \(\approx\) 100.03 &deg;C &mdash;
<b>lower</b> than 100.05 &deg;C.</p>
<p>b. In acetic acid the solvent itself is different: its normal boiling point is 118.1 &deg;C and
\(K_b \approx 3.07\) K kg mol<sup>&minus;1</sup> (water 0.52). With 500 mL &asymp; 525 g of acetic acid,
\(\Delta T_b = 3.07\times\dfrac{10/180}{0.525} \approx 0.33\) K, so the solution boils at about
118.4 &deg;C &mdash; very different.</p>
<p><span class="box">The boiling point is not the same in either case</span></p>
<p><b>(iii)</b> <span class="box">Osmotic pressure</span>. For a polymer (large M) a reasonable mass gives a very low
molality, so \(\Delta T_b\) and \(\Delta T_f\) are too small to measure accurately, whereas \(\pi\) is measurable
(e.g. a few mm of liquid column). It is measured at room temperature, so polymers/biomolecules that are unstable at
high temperature are not decomposed, and molarity rather than molality is used.</p>""",
          topic="Solutions",
          recall=r"""<ul><li>Henry: \(p = K_H x\); higher \(K_H\) &rArr; less soluble.</li>
<li>\(\Delta T_b = K_b m\): depends on the solvent (\(K_b\)) and on the number of solute moles.</li>
<li>Osmotic pressure is the method of choice for macromolecules.</li></ul>"""),
    ])
