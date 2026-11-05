"""Heritage School Pre-Board 2025-26, Chemistry (Paper 1), Set 1 -- transcribed from the page images
of the .docx (rendered to PDF)."""
from kit import Q, SEC
import chemistry_2025_26_figs as fg

AR = r"""<p>(a) Both assertion and reason are true and the reason is the correct explanation of assertion.<br>
(b) Both assertion and reason are true but reason is not the correct explanation for assertion.<br>
(c) Assertion is true but reason is false.<br>
(d) Assertion is false but reason is true.</p>"""

WORDS = (r"[lesser than, six, Benzoin, dia, octahedral, sp<sup>3</sup>d<sup>2</sup>, formaldehyde, phenol, "
         r"mutarotation, greater than, zero, third, ethylisocyanide, Cannizaro, green, ethanenitrile, independent, "
         r"substitution, one, equal to, para, yellow, white, aniline, second, absence, dependent, trigonalplanar, "
         r"high, two, ammonia, tetrahedral, four, presence, aldol, acetaldehyde, first, dehydration, acetone, "
         r"three, hydroxylamine]")

SALT_BRIDGE = r"""<ol>
<li>It <b>completes the internal circuit</b>: ions move through it, so current can flow between the two
solutions without the solutions mixing.</li>
<li>It <b>maintains electrical neutrality</b> of the two half-cells: as the anode solution gains cations
(or the cathode solution loses them), anions of the bridge electrolyte migrate to the anode side and
cations to the cathode side. Without it, charge would build up and the cell would stop within moments.</li>
<li>It minimises the liquid-junction potential (an inert electrolyte such as KCl or \(\ce{KNO3}\) in
agar, whose ions have nearly equal mobilities).</li></ol>"""

CARBYLAMINE_Q = r"<p>(i) Carbylamine reaction</p>"
CARBYLAMINE_A = r"""<p><b>(i) Carbylamine reaction</b> &mdash; a primary amine (aliphatic or aromatic) warmed with
chloroform and alcoholic KOH gives an isocyanide (carbylamine) with an offensive smell:</p>
<p>\[\ce{R-NH2 + CHCl3 + 3KOH(alc) ->[\Delta] R-NC + 3KCl + 3H2O}\]</p>
<p>e.g. \(\ce{C6H5NH2 + CHCl3 + 3KOH -> C6H5NC + 3KCl + 3H2O}\) (phenyl isocyanide).</p>"""

PAPER = dict(
    subject="chemistry",
    year="2025-26",
    slug="2025-26-set-1",
    paper="Set 1",
    source="/home/sayantan/Ujaan/class12/SchoolNotes/PreBoard-PYQ/2025-26/SET-1/CHEMISTRY.docx",
    marks=70, time="3 hours",
    intro=r"""<p><b>The Heritage School &mdash; Pre-Board Examinations, 2025-2026. Subject: Chemistry (Paper 1),
Class XII.</b> Maximum Marks: 70. Time Allotted: Three Hours. Reading Time: Additional Fifteen Minutes.</p>
<p>Instructions to Candidates</p>
<ol>
<li>You are allowed an additional fifteen minutes for only reading the question paper.</li>
<li>You must NOT start writing during the reading time.</li>
<li>This question paper has 9 printed pages. <span class="note">[The page footers say ten printed pages.]</span></li>
<li>It is divided into four sections and has twenty one questions in all.</li>
<li>Answer all questions.</li>
<li>Section A has fourteen subparts. Each question carries 1 mark.</li>
<li>While attempting Multiple Choice Questions in Section A, you are required to write only ONE option as
the answer.</li>
<li>Section B has ten questions. Each question carries 2 marks.</li>
<li>Section C has seven questions. Each question carries 3 marks.</li>
<li>Section D has three questions. Each question carries 5 marks.</li>
<li>Internal choices have been provided in one question each in Sections B, C and D.</li>
<li>The intended marks for questions are given in brackets [ ].</li>
<li>All working, including rough work, should be done on the same sheet as, and adjacent to the rest of
the answer.</li>
<li>Balanced equations must be given wherever possible and diagrams where they are helpful.</li>
<li>When solving numerical problems, all essential workings must be shown.</li>
<li>In working out problems, use the following data: Gas constant R = 1&middot;987 cal deg<sup>&minus;1</sup>
mol<sup>&minus;1</sup> = 8&middot;314 J K<sup>&minus;1</sup> mol<sup>&minus;1</sup> = 0&middot;0821 dm<sup>3</sup>
atm K<sup>&minus;1</sup> mol<sup>&minus;1</sup>, 1 l atm = 1 dm<sup>3</sup> atm = 101&middot;3 J.
1 Faraday = 96500 coulombs. Avogadro's number = 6&middot;023 &times; 10<sup>23</sup>.</li>
</ol>""",
    items=[
        SEC("Section A &ndash; 14 Marks", "Question 1"),
        # ------------------------------------------------------------------ 1(A)
        Q("1(A)(i)", 1, r"<p><b>Fill in the blanks by choosing the appropriate word(s) from those given in the "
          r"bracket:</b> " + WORDS + r" [4&times;1=4]</p>"
          r"<p>i. van't Hoff factor for sucrose is -------- one while that for potassium ferrocyanide is "
          r"--------- one.</p>",
          a=r"""<p>van't Hoff factor for sucrose is <b>equal to</b> one while that for potassium ferrocyanide is
<b>greater than</b> one.</p>
<p>Sucrose is a non-electrolyte (no dissociation, no association), so \(i = 1\).
\(\ce{K4[Fe(CN)6] -> 4K+ + [Fe(CN)6]^4-}\) gives 5 ions per formula unit, so \(i > 1\) (ideally 5).</p>
<p><span class="box">equal to; greater than</span></p>""",
          topic="Solutions",
          recall=r"""<ul><li>van't Hoff factor \(i\) = observed colligative property &divide; calculated value
= normal molar mass &divide; observed molar mass.</li>
<li>Dissociation: \(i > 1\); association: \(i < 1\); non-electrolyte: \(i = 1\).</li></ul>"""),
        Q("1(A)(ii)", 1, r"<p>ii. The half-life period of a ------ order reaction is ------ of the concentration "
          r"of the reactant.</p>",
          a=r"""<p>The half-life period of a <b>first</b> order reaction is <b>independent</b> of the concentration
of the reactant.</p>
<p>\(t_{1/2} = \dfrac{0.693}{k}\) &mdash; no concentration term appears.</p>
<p><span class="box">first; independent</span></p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>First order: \(t_{1/2} = 0.693/k\), independent of \([\mathrm{A}]_0\).</li>
<li>Zero order: \(t_{1/2} = [\mathrm{A}]_0/2k\), directly proportional to \([\mathrm{A}]_0\).</li></ul>"""),
        Q("1(A)(iii)", 1, r"<p>iii. Benzenediazonium chloride on warming with water gives ------ which gives "
          r"----- precipitate on treatment with bromine water.</p>",
          a=r"""<p>Benzenediazonium chloride on warming with water gives <b>phenol</b> which gives <b>white</b>
precipitate on treatment with bromine water.</p>
<p>\(\ce{C6H5N2+Cl- + H2O ->[\Delta] C6H5OH + N2 ^ + HCl}\)</p>
<p>\(\ce{C6H5OH + 3Br2(aq) -> C6H2Br3OH v + 3HBr}\) (2,4,6-tribromophenol, white ppt.)</p>
<p><span class="box">phenol; white</span></p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Diazonium salts: replacement of \(\ce{-N2+}\) by &ndash;OH on warming with water.</li>
<li>&ndash;OH strongly activates the ring: bromine water substitutes all three o/p positions.</li></ul>"""),
        Q("1(A)(iv)", 1, r"<p>iv. Ethanamide on heating with P<sub>2</sub>O<sub>5</sub> gives ------. This is an "
          r"example of -----------</p>",
          a=r"""<p>Ethanamide on heating with \(\ce{P2O5}\) gives <b>ethanenitrile</b>. This is an example of
<b>dehydration</b>.</p>
<p>\(\ce{CH3CONH2 ->[P2O5][\Delta] CH3C#N + H2O}\)</p>
<p><span class="box">ethanenitrile; dehydration</span></p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Cyanides from amides: dehydration with \(\ce{P2O5}\) (or \(\ce{SOCl2}\)).</li>
<li>\(\ce{CH3CN}\) = ethanenitrile (methyl cyanide).</li></ul>"""),
        # ------------------------------------------------------------------ 1(B)
        Q("1(B)(i)", 1, r"<p><b>(B) Select the correct alternative from the choices given below:</b> [7&times;1=7]</p>"
          r"<p>(i) Among the following ions which one has the highest paramagnetism?</p>"
          r"<p>(a) [Cr(H<sub>2</sub>O)<sub>6</sub>]<sup>+3</sup><br>(b) [Fe(H<sub>2</sub>O)<sub>6</sub>]<sup>+2</sup><br>"
          r"(c) [Cu(H<sub>2</sub>O)<sub>6</sub>]<sup>+2</sup><br>(d) [Zn(H<sub>2</sub>O)<sub>6</sub>]<sup>+2</sup></p>",
          a=r"""<p>Count unpaired electrons (water is a weak-field ligand, so the ions stay high spin):</p>
<table class="tbl"><tr><th>Ion</th><th>configuration</th><th>unpaired e<sup>&minus;</sup></th></tr>
<tr><td>\(\ce{Cr^3+}\)</td><td>3d<sup>3</sup></td><td>3</td></tr>
<tr><td>\(\ce{Fe^2+}\)</td><td>3d<sup>6</sup> (\(t_{2g}^4e_g^2\))</td><td>4</td></tr>
<tr><td>\(\ce{Cu^2+}\)</td><td>3d<sup>9</sup></td><td>1</td></tr>
<tr><td>\(\ce{Zn^2+}\)</td><td>3d<sup>10</sup></td><td>0</td></tr></table>
<p>\(\mu = \sqrt{n(n+2)}\) is largest for \(n = 4\) (4.90 BM).</p>
<p><span class="box">(b) [Fe(H<sub>2</sub>O)<sub>6</sub>]<sup>2+</sup></span></p>""",
          topic="Coordination Compounds",
          recall=r"""<ul><li>Spin-only moment \(\mu = \sqrt{n(n+2)}\) BM, \(n\) = unpaired electrons.</li>
<li>\(\ce{H2O}\) is weak field: \(\Delta_o < P\), electrons occupy \(e_g\) before pairing.</li></ul>"""),
        Q("1(B)(ii)", 1, r"<p>(ii) An excess of AgNO<sub>3</sub> is added to 100 ml of a 0.01 M solution of "
          r"dichlorotetra aquachromium(III) chloride. The number of moles of AgCl precipitated would be:</p>"
          r"<p>(a) 0.003 &nbsp; (b) 0.01 &nbsp; (c) 0.001 &nbsp; (d) 0.002</p>",
          a=r"""<p>The compound is \(\ce{[CrCl2(H2O)4]Cl}\): only <b>one</b> \(\ce{Cl-}\) is outside the coordination
sphere and ionisable.</p>
<p>Moles of complex \(= 0.01\ \text{mol L}^{-1} \times 0.100\ \text{L} = 1\times10^{-3}\) mol
&rArr; moles of AgCl \(= 1 \times 10^{-3}\).</p>
<p><span class="box">(c) 0.001</span></p>""",
          topic="Coordination Compounds",
          recall=r"""<ul><li>Only counter-ions (outside [ ]) are precipitated by \(\ce{AgNO3}\); coordinated
\(\ce{Cl-}\) is not.</li><li>moles = molarity &times; volume in litres.</li></ul>"""),
        Q("1(B)(iii)", 1, r"<p>(iii) KCN reacts readily to form cyanide with:</p>"
          r"<p>(a) ethanol &nbsp; (b) ethyl bromide &nbsp; (c) bromobenzene &nbsp; (d) chlorobenzene</p>",
          a=r"""<p>An alkyl halide undergoes S<sub>N</sub>2 substitution by \(\ce{CN-}\):
\(\ce{C2H5Br + KCN(alc) -> C2H5CN + KBr}\).
Ethanol has a poor leaving group (\(\ce{OH-}\)); aryl halides do not undergo nucleophilic substitution
readily (partial double-bond character of C&ndash;X).</p>
<p><span class="box">(b) ethyl bromide</span></p>""",
          topic="Haloalkanes and Haloarenes",
          recall=r"""<ul><li>KCN (ionic) &rarr; nitrile R&ndash;CN; AgCN (covalent) &rarr; isocyanide R&ndash;NC.</li>
<li>Haloarenes resist nucleophilic substitution.</li></ul>"""),
        Q("1(B)(iv)", 1, r"<p>(iv) Which of the following is not a pyrimidine base?</p>"
          r"<p>(a) Uracil &nbsp; (b) Thymine &nbsp; (c) Cytosine &nbsp; (d) Guanine</p>",
          a=r"""<p>Pyrimidines (single six-membered ring): cytosine, thymine, uracil. Purines (fused
two-ring system): adenine and <b>guanine</b>.</p>
<p><span class="box">(d) Guanine</span></p>""",
          topic="Biomolecules",
          recall=r"""<ul><li>Purines: A, G. Pyrimidines: C, T (DNA), U (RNA).</li></ul>"""),
        Q("1(B)(v)", 1, r"<p>(v) The graphs below show the solubility of a primary, a secondary and a tertiary "
          r"aliphatic amine I, J, and K in water, at the same temperature. The number of carbon atoms in each of "
          r"the compounds is three. Amine I is the tertiary amine, amine J is the primary amine, and amine K is "
          r"the secondary amine.</p>",
          qfig=fg.fig_s1_amine_bars,
          a=r"""<p>Solubility in water depends on hydrogen bonding with water through N&ndash;H. For isomeric
amines (\(\ce{C3H9N}\)): the primary amine has two N&ndash;H bonds, the secondary one, the tertiary none,
so solubility: <b>primary (J) &gt; secondary (K) &gt; tertiary (I)</b>.</p>
<p>Only graph S shows J tallest, K next and I lowest.</p>
<p><span class="box">(d) graph S</span></p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Number of N&ndash;H bonds: 1&deg; = 2, 2&deg; = 1, 3&deg; = 0 &rarr; extent of
H-bonding and hence solubility and boiling point fall 1&deg; &gt; 2&deg; &gt; 3&deg; for isomers.</li></ul>"""),
        Q("1(B)(vi)", 1, r"<p>(vi) <b>Assertion</b>: The depression in freezing point of 0.1M aqueous solution of "
          r"MgCl<sub>2</sub> is more than that of 0.1M aqueous solution of KCl.<br><b>Reason</b>: Number of "
          r"particles furnished by MgCl<sub>2</sub> is greater than that of KCl.</p>" + AR,
          a=r"""<p>\(\ce{MgCl2 -> Mg^2+ + 2Cl-}\) (\(i \approx 3\)) while \(\ce{KCl -> K+ + Cl-}\) (\(i \approx 2\)).
\(\Delta T_f = iK_fm\), so at the same molality \(\ce{MgCl2}\) gives the larger depression &mdash; and that is
precisely because it furnishes more particles.</p>
<p><span class="box">(a) Both true; reason is the correct explanation</span></p>""",
          topic="Solutions",
          recall=r"""<ul><li>\(\Delta T_f = iK_f m\): a colligative property depends on the number of solute
particles.</li></ul>"""),
        Q("1(B)(vii)", 1, r"<p>(vii) <b>Assertion</b>: m-Nitrophenol is more acidic than ortho and para "
          r"nitrophenols.<br><b>Reason</b>: &ndash;NO<sub>2</sub> groups at o- and p- position withdraws electrons "
          r"of the O-H bond by stronger &ndash;R effect while the &ndash;NO<sub>2</sub> group at m- position "
          r"withdraws electrons of the O-H bond by weaker &ndash;I effect.</p>" + AR,
          a=r"""<p>At o- and p- positions \(\ce{-NO2}\) withdraws electrons by both &ndash;R and &ndash;I effects
and delocalises the negative charge of the phenoxide ion onto its own oxygens; at the m-position only the
weaker &ndash;I effect acts. Hence o- and p-nitrophenol are <b>more</b> acidic than m-nitrophenol
(pK<sub>a</sub>: p 7.1, o 7.2, m 8.3). The assertion is false; the reason is a true statement.</p>
<p><span class="box">(d) Assertion is false but reason is true</span></p>""",
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Electron-withdrawing groups at o/p stabilise phenoxide by resonance (&ndash;R) &rarr;
stronger acid than the m-isomer, which has only &ndash;I.</li></ul>"""),
        # ------------------------------------------------------------------ 1(C)
        Q("1(C)", 3, r"<p><b>(C) Read the passage given below carefully and answer the questions that "
          r"follow:</b></p><p>{{fig:0}}</p>"
          r"<p>In the chemistry lab, Kabir sets up an electrochemical cell as shown below: At room temperature, "
          r"she found that the initial voltmeter reading was +0.16v.</p>"
          r"<p>(i) The standard electrode potential for the Cu<sup>2+</sup>/Cu electrode is given by</p>"
          r"<p>Cu<sup>2+</sup>(aq) + 2e<sup>&ndash;</sup> &rarr; Cu(s); E<sup>o</sup> = + 0.34 V</p>"
          r"<p>Calculate the electrode potential of the electrode on the left-hand side of the above "
          r"electrochemical cell.</p>"
          r"<p>(ii) Explain the importance of the salt bridge between the two solutions.</p>"
          r"<p>(iii) Give the cell representation.</p>",
          qfig=fg.fig_s1_cu_conc_cell,
          a=r"""<p><b>(i)</b> The right-hand electrode dips in 1.0 mol dm<sup>&minus;3</sup> \(\ce{Cu^2+}\), i.e. it
is under standard conditions: \(E_\text{right} = E^\circ = +0.34\) V. With the voltmeter reading taken as
\(E_\text{cell} = E_\text{right} - E_\text{left}\):</p>
<p>\[E_\text{left} = E_\text{right} - E_\text{cell} = 0.34 - 0.16 = 0.18\ \text{V}\]</p>
<p><span class="box">\(E_\text{left} = +0.18\) V</span></p>
<p class="note">The diagram has copper in both beakers, so this is a Cu | Cu<sup>2+</sup> <b>concentration
cell</b>, not a cell measured against the standard hydrogen electrode: the 0.16 V reading is the difference of the
two copper electrode potentials, not the potential of the left electrode itself. The answer above is the one the
question's data lead to. Note, however, that the data are not self-consistent: the Nernst equation for
0.15 mol dm<sup>&minus;3</sup> \(\ce{Cu^2+}\) gives \(E_\text{left} = 0.34 + \frac{0.0591}{2}\log 0.15 = +0.316\) V,
i.e. an emf of only 0.024 V. A reading of 0.16 V would need \([\ce{Cu^2+}] \approx 4\times10^{-6}\) mol
dm<sup>&minus;3</sup> on the left. The measured reading is used as given.</p>
<p><b>(ii) Importance of the salt bridge:</b></p>""" + SALT_BRIDGE + r"""
<p><b>(iii)</b> Oxidation at the left (dilute) electrode, reduction at the right:</p>
<p><span class="box">\(\ce{Cu(s) | Cu^2+(aq, 0.15 M) || Cu^2+(aq, 1.0 M) | Cu(s)}\)</span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>\(E_\text{cell} = E_\text{cathode} - E_\text{anode}\) (reduction potentials;
cathode written on the right).</li>
<li>Nernst: \(E = E^\circ - \frac{0.0591}{n}\log\frac{1}{[\ce{M^{n+}}]}\) at 298 K.</li>
<li>Cell notation: anode | anode solution || cathode solution | cathode.</li></ul>"""),
        # ------------------------------------------------------------------ Section B
        SEC("Section B &ndash; 20 Marks"),
        Q("2", 2, r"<p>Carbon dating is used by archaeologists to date trees, plants, and animal remains as well as "
          r"human artefacts made from wood and leather. If an archaeologist found that the percentage of carbon-14 "
          r"in the remains of an animal was 10% of what carbon-14 was in the animal's body when the animal died, "
          r"find the age of this sample.</p><p><i>(Given the half-life of carbon-14 = 5730 years)</i></p>",
          a=r"""<p>Radioactive decay is a first-order process.</p>
<p>\[k = \frac{0.693}{t_{1/2}} = \frac{0.693}{5730\ \text{y}} = 1.209\times10^{-4}\ \text{y}^{-1}\]</p>
<p>\[t = \frac{2.303}{k}\log\frac{N_0}{N} = \frac{2.303}{1.209\times10^{-4}}\log\frac{100}{10}
= \frac{2.303\times 5730}{0.693}\times 1\]</p>
<p>\[t = 1.904\times10^{4}\ \text{y}\]</p>
<p><span class="box">Age \(\approx 1.90\times10^{4}\) years (about 19 000 years)</span></p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>First order: \(k = \frac{2.303}{t}\log\frac{[\mathrm{A}]_0}{[\mathrm{A}]}\);
\(t_{1/2} = 0.693/k\).</li><li>10% remaining means \(N_0/N = 10\), \(\log 10 = 1\).</li></ul>"""),
        Q("3", 2, r"<p>Write the chemical equations to convert each of the following:</p>"
          r"<p>i. Nitrobenzene to benzenediazonium chloride</p><p>ii. Aniline to 2,4,6-tribromoaniline.</p>",
          a=r"""<p><b>(i)</b> Reduce to aniline, then diazotise at 273&ndash;278 K:</p>
<p>\[\ce{C6H5NO2 + 6[H] ->[Sn/HCl] C6H5NH2 + 2H2O}\]</p>
<p>\[\ce{C6H5NH2 + NaNO2 + 2HCl ->[273-278 K] C6H5N2+Cl- + NaCl + 2H2O}\]</p>
<p><b>(ii)</b> Aniline with bromine water at room temperature:</p>
<p>\[\ce{C6H5NH2 + 3Br2(aq) -> C6H2Br3NH2 v + 3HBr}\]</p>
<p>2,4,6-tribromoaniline separates as a white precipitate.</p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Diazotisation: \(\ce{NaNO2 + HCl}\) (in situ \(\ce{HNO2}\)) at 0&ndash;5 &deg;C.</li>
<li>&ndash;NH<sub>2</sub> is strongly o/p-activating: bromine water gives the 2,4,6-tribromo product.</li></ul>"""),
        Q("4", 2, r"<p>Discuss the hybridisation, shape and charge on metal in [Ni(CO)<sub>4</sub>] complex. Also "
          r"comment on its magnetic properties.</p>",
          a=r"""<p>Ni (Z = 28): [Ar] 3d<sup>8</sup>4s<sup>2</sup>. CO is neutral, so the oxidation state (charge) of
Ni is <b>0</b>.</p>
<p>CO is a strong-field ligand: the two 4s electrons are paired into 3d, giving 3d<sup>10</sup>; the empty 4s
and three 4p orbitals hybridise to accept four electron pairs from four CO.</p>
{{fig:0}}
<ul><li>Hybridisation: <b>sp<sup>3</sup></b></li><li>Shape: <b>tetrahedral</b></li>
<li>Charge on metal: <b>zero</b> (Ni(0))</li>
<li>Magnetic property: no unpaired electron &rArr; <b>diamagnetic</b></li></ul>
<p><span class="box">sp<sup>3</sup>, tetrahedral, Ni(0), diamagnetic</span></p>""",
          afig=[fg.fig_s1_nico4_vbt],
          topic="Coordination Compounds",
          recall=r"""<ul><li>VBT: number of ligands &rarr; number of hybrid orbitals; 4 &rarr; sp<sup>3</sup>
(tetrahedral) or dsp<sup>2</sup> (square planar).</li><li>Strong-field CO forces pairing.</li></ul>"""),
        Q("5", 2, r"<p>A 2 molal solution of sodium chloride in water causes an elevation in the boiling point by "
          r"1.88K. What is the value of van't Hoff factor? What does it signify? [K<sub>b</sub> = 0.52 K kg "
          r"mol<sup>&minus;1</sup>]</p>",
          a=r"""<p>\[\Delta T_b = iK_bm \;\Rightarrow\; i = \frac{\Delta T_b}{K_b m} = \frac{1.88}{0.52\times2}
= 1.81\]</p>
<p><span class="box">\(i = 1.81\)</span></p>
<p><b>Significance:</b> \(i > 1\) means the solute <b>dissociates</b> in water
(\(\ce{NaCl -> Na+ + Cl-}\)), so there are more particles than formula units. Degree of dissociation
\(\alpha = \frac{i-1}{n-1} = \frac{1.81-1}{2-1} = 0.81\), i.e. about 81% dissociated (not 100%, because of
interionic attraction at this concentration).</p>""",
          topic="Solutions",
          recall=r"""<ul><li>\(\Delta T_b = iK_bm\).</li><li>For dissociation into \(n\) ions:
\(\alpha = (i-1)/(n-1)\).</li></ul>"""),
        Q("6", 2, r"<p>How will you convert the following (write chemical equation):</p>"
          r"<p>i. Acetaldehyde is heated with hydroiodic acid in presence of red phosphorous.</p>"
          r"<p>ii. Formaldehyde is treated with ammonia.</p>",
          a=r"""<p><b>(i)</b> HI/red P reduces the &gt;C=O group completely to &ndash;CH<sub>2</sub>&ndash;: acetaldehyde
gives <b>ethane</b>.</p>
<p>\[\ce{CH3CHO + 4HI ->[red P][\Delta] CH3CH3 + H2O + 2I2}\]</p>
<p><b>(ii)</b> Formaldehyde condenses with ammonia to give <b>hexamethylenetetramine (urotropine)</b>:</p>
<p>\[\ce{6HCHO + 4NH3 -> (CH2)6N4 + 6H2O}\]</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Red P regenerates HI from \(\ce{I2}\); C=O &rarr; CH<sub>2</sub>.</li>
<li>HCHO + NH<sub>3</sub> &rarr; urotropine (a cage compound, used as a urinary antiseptic); other
aldehydes give aldimines.</li></ul>"""),
        Q("7", 2, r"<p>The standard reduction potentials of the following electrodes are given below. Answer the "
          r"questions that follow:</p><p>Electrodes SRP values&ndash;<br>Fe<sup>2+</sup>/Fe &rArr; &minus;0.44V<br>"
          r"Mg<sup>2+</sup>/Mg &rArr; &minus;2.37V<br>I<sub>2</sub>/2I<sup>&minus;</sup> &rArr; +0.54V<br>"
          r"Ag<sup>+</sup>/Ag &rArr; +0.88V</p>"
          r"<p>i. Which substance/s could be used to convert iodide ions to iodine?</p>"
          r"<p>ii. From the given reactions which reaction is spontaneous and why?<br>"
          r"I: Fe<sup>2+</sup> + 2Ag &rarr; 2Ag<sup>+1</sup> + Fe<br>II: Fe<sup>2+</sup> + Mg &rarr; "
          r"Mg<sup>2+</sup> + Fe</p>"
          r"<p class='note'>[The paper prints +0.88 V for Ag<sup>+</sup>/Ag; the tabulated value is +0.80 V. "
          r"The answers do not change.]</p>",
          a=r"""<p><b>(i)</b> To oxidise \(\ce{I-}\) to \(\ce{I2}\) we need a species that is reduced more readily
than \(\ce{I2}\), i.e. the oxidised form of a couple with \(E^\circ > +0.54\) V. Only
\(\ce{Ag+/Ag}\) (+0.88 V) qualifies:</p>
<p>\(\ce{2Ag+ + 2I- -> 2Ag + I2}\), \(E^\circ_\text{cell} = 0.88 - 0.54 = +0.34\) V &gt; 0.</p>
<p><span class="box">\(\ce{Ag+}\) ions</span></p>
<p><b>(ii)</b> \(E^\circ_\text{cell} = E^\circ_\text{cathode} - E^\circ_\text{anode}\) (cathode = species reduced):</p>
<p>I: \(\ce{Fe^2+}\) reduced, Ag oxidised: \(E^\circ = -0.44 - 0.88 = -1.32\) V &lt; 0 &rArr; non-spontaneous.</p>
<p>II: \(\ce{Fe^2+}\) reduced, Mg oxidised: \(E^\circ = -0.44 - (-2.37) = +1.93\) V &gt; 0 &rArr;
\(\Delta G^\circ = -nFE^\circ < 0\).</p>
<p><span class="box">Reaction II is spontaneous (E&deg;<sub>cell</sub> = +1.93 V, &Delta;G&deg; &lt; 0)</span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>A species with a higher reduction potential oxidises one with a lower potential.</li>
<li>\(\Delta G^\circ = -nFE^\circ_\text{cell}\); spontaneous if \(E^\circ_\text{cell} > 0\).</li></ul>"""),
        Q("8(i)", 2, r"<p>i. When FeCr<sub>2</sub>O<sub>4</sub> is fused with Na<sub>2</sub>CO<sub>3</sub> in the "
          r"presence of air, it gives a yellow solution of compound [A]. Compound [A] on acidification gives "
          r"compound [B]. Compound [B] on reaction with KCl forms an orange coloured compound [C]. An acidified "
          r"solution of compound [C] oxidises Na<sub>2</sub>SO<sub>3</sub> to [D]. Identify [A], [B], [C], [D].</p>",
          a=r"""<p>[A] = \(\ce{Na2CrO4}\) (sodium chromate, yellow); [B] = \(\ce{Na2Cr2O7}\) (sodium dichromate);
[C] = \(\ce{K2Cr2O7}\) (potassium dichromate, orange); [D] = \(\ce{Na2SO4}\) (sodium sulphate).</p>
<p>\[\ce{4FeCr2O4 + 8Na2CO3 + 7O2 -> 8Na2CrO4 + 2Fe2O3 + 8CO2}\]</p>
<p>\[\ce{2Na2CrO4 + H2SO4 -> Na2Cr2O7 + Na2SO4 + H2O}\]</p>
<p>\[\ce{Na2Cr2O7 + 2KCl -> K2Cr2O7 + 2NaCl}\]</p>
<p>\[\ce{K2Cr2O7 + 4H2SO4 + 3Na2SO3 -> K2SO4 + Cr2(SO4)3 + 3Na2SO4 + 4H2O}\]</p>""",
          topic="d- and f-Block Elements",
          recall=r"""<ul><li>Chromite &rarr; chromate (fusion with \(\ce{Na2CO3}\), air) &rarr; dichromate (acid)
&rarr; \(\ce{K2Cr2O7}\) (KCl, less soluble).</li>
<li>Acidified dichromate gains 6e<sup>&minus;</sup> per ion (Cr +6 &rarr; +3);
sulphite is oxidised to sulphate.</li></ul>"""),
        Q("8(ii) OR", 2, r"<p style='text-align:center'>OR</p><p>ii. a. Comment on the nature of bonding in "
          r"La<sub>2</sub>O<sub>3</sub> and Lu<sub>2</sub>O<sub>3</sub>.<br>b. Zr and Hf exhibit similar "
          r"properties. Explain [At no of Zr = 40, Hf = 72]</p>",
          a=r"""<p><b>(a)</b> Because of the <b>lanthanoid contraction</b>, \(\ce{Lu^3+}\) is much smaller than
\(\ce{La^3+}\), so it has a greater polarising power. Hence \(\ce{La2O3}\) is the more <b>ionic</b> (and more
basic) oxide, while \(\ce{Lu2O3}\) has greater <b>covalent</b> character (and is less basic).</p>
<p><b>(b)</b> Hf (5d series) follows the lanthanoids. The lanthanoid contraction (poor shielding by the 4f
electrons) cancels the expected increase in size from Zr to Hf, so the two have almost identical atomic radii
(Zr 160 pm, Hf 159 pm) and ionic radii, with the same outer configuration (\(n\)d<sup>2</sup>\((n+1)\)s<sup>2</sup>).
Same size + same valence configuration &rArr; very similar properties (they occur together and are hard to
separate).</p>""",
          topic="d- and f-Block Elements",
          recall=r"""<ul><li>Lanthanoid contraction: steady decrease in size La &rarr; Lu due to poor shielding
by 4f electrons.</li><li>Consequences: basicity of oxides/hydroxides decreases La &rarr; Lu; 4d and 5d
elements of a group have similar radii (Zr/Hf, Nb/Ta, Mo/W).</li></ul>"""),
        Q("9", 2, r"<p>(i) This box gives a list of aldehydes and ketones. Choose the appropriate aldehyde/ketone "
          r"that reacts with CH<sub>3</sub>MgBr to form a 1<sup>0</sup> alcohol and a 3<sup>0</sup> alcohol</p>"
          r"<table class='tbl'><tr><td>CH<sub>2</sub>O</td><td>C<sub>2</sub>H<sub>4</sub>O</td><td>C<sub>3</sub>H<sub>6</sub>O</td></tr>"
          r"<tr><td>C<sub>3</sub>H<sub>8</sub>O</td><td>C<sub>2</sub>H<sub>3</sub>O</td><td>CHO</td></tr></table>"
          r"<p>ii. A scientist while working in the lab accidently removed the labels from the carboxylic acid "
          r"bottles. He had two bottles in which he had kept formic acid, acetic acid. Can you suggest a chemical "
          r"test which he can perform to positively identify the acids so that he can label the bottles "
          r"correctly?</p>",
          a=r"""<p><b>(i)</b> Grignard addition then hydrolysis: HCHO gives a 1&deg; alcohol, other aldehydes
2&deg;, ketones 3&deg;.</p>
<p>1&deg; alcohol from <b>CH<sub>2</sub>O</b> (formaldehyde):
\(\ce{HCHO + CH3MgBr -> CH3CH2OMgBr ->[H2O/H+] CH3CH2OH + Mg(OH)Br}\) (ethanol).</p>
<p>3&deg; alcohol from <b>C<sub>3</sub>H<sub>6</sub>O</b> taken as acetone:
\(\ce{(CH3)2CO + CH3MgBr -> (CH3)3COMgBr ->[H2O/H+] (CH3)3COH + Mg(OH)Br}\) (2-methylpropan-2-ol).</p>
<p><span class="box">CH<sub>2</sub>O &rarr; 1&deg;; C<sub>3</sub>H<sub>6</sub>O (propanone) &rarr; 3&deg;</span></p>
<p><b>(ii)</b> <b>Tollens' test</b>: warm a little of each acid with Tollens' reagent (ammoniacal
\(\ce{AgNO3}\)). Formic acid (which has an &ndash;CHO group, H&ndash;COOH) gives a silver mirror; acetic acid does
not.</p>
<p>\(\ce{HCOOH + 2[Ag(NH3)2]+ + 2OH- -> 2Ag v + CO2 + 2H2O + 4NH3}\)</p>
<p>(Alternatively: formic acid decolourises acidified \(\ce{KMnO4}\) / reduces Fehling's solution; acetic
acid does not.)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>RMgX + HCHO &rarr; 1&deg;; + RCHO &rarr; 2&deg;; + R<sub>2</sub>CO &rarr; 3&deg; alcohol.</li>
<li>Formic acid is the only common carboxylic acid that is also a reducing agent.</li></ul>"""),
        Q("10", 2, r"<p>The rate constant of a first order reaction becomes six times when the temperature is "
          r"increased from 350K to 410 K. Calculate activation energy [E<sub>a</sub>] for the reaction.</p>",
          a=r"""<p>Arrhenius equation in two-temperature form:</p>
<p>\[\log\frac{k_2}{k_1} = \frac{E_a}{2.303R}\left(\frac{T_2-T_1}{T_1T_2}\right)\]</p>
<p>\[\log 6 = \frac{E_a}{2.303\times8.314}\left(\frac{410-350}{350\times410}\right)\]</p>
<p>\[0.7782 = \frac{E_a}{19.147}\times4.181\times10^{-4}\]</p>
<p>\[E_a = \frac{0.7782\times19.147}{4.181\times10^{-4}} = 3.563\times10^{4}\ \text{J mol}^{-1}\]</p>
<p><span class="box">\(E_a \approx 35.6\) kJ mol<sup>&minus;1</sup></span></p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>\(\log\frac{k_2}{k_1} = \frac{E_a}{2.303R}\cdot\frac{T_2-T_1}{T_1T_2}\), R = 8.314 J
K<sup>&minus;1</sup> mol<sup>&minus;1</sup>.</li></ul>"""),
        Q("11", 2, r"<p>Write the chemical equation for each of the following named organic reactions:</p>"
          + CARBYLAMINE_Q + r"<p>(ii) Hofmann's degradation reaction</p>",
          a=CARBYLAMINE_A + r"""<p><b>(ii) Hofmann's bromamide degradation</b> &mdash; an amide with bromine and
aqueous KOH gives a primary amine with one carbon atom fewer:</p>
<p>\[\ce{R-CONH2 + Br2 + 4KOH -> R-NH2 + K2CO3 + 2KBr + 2H2O}\]</p>
<p>e.g. \(\ce{CH3CONH2 + Br2 + 4KOH -> CH3NH2 + K2CO3 + 2KBr + 2H2O}\) (methylamine).</p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Carbylamine: test for 1&deg; amines (2&deg;, 3&deg; do not respond).</li>
<li>Hofmann degradation: amide &rarr; amine, one C less (step down of the chain).</li></ul>"""),
        # ------------------------------------------------------------------ Section C
        SEC("Section C &ndash; 21 Marks"),
        Q("12(i)", 3, r"<p>i. a. An organic compound [A] having molecular formula C<sub>2</sub>H<sub>7</sub>N on "
          r"treatment with nitrous acid gives a compound [B]. Compound [B] on controlled oxidation gives a compound "
          r"[C]. Compound [C] reduces Tollen's reagent to give silver mirror and compound [D]. Compound [B] reacts "
          r"with compound [D] in the presence of concentrated sulphuric acid to give a sweet smelling compound [E]. "
          r"Identify the compound [A], [B], [C], [D], [E].</p>"
          r"<p>b. Complete the following:<br>C<sub>2</sub>H<sub>5</sub>NH<sub>2</sub> + HNO<sub>2</sub> &rarr; "
          r"------ + --------- + ---------</p>",
          a=r"""<p><b>(a)</b> [B] gives on mild oxidation a compound [C] that reduces Tollens' reagent, so [B] is a
primary alcohol and [C] an aldehyde; a 1&deg; amine \(\ce{C2H7N}\) gives such an alcohol with \(\ce{HNO2}\).</p>
<table class="tbl"><tr><th></th><th>compound</th><th>formula</th></tr>
<tr><td>[A]</td><td>ethanamine (ethylamine)</td><td>\(\ce{CH3CH2NH2}\)</td></tr>
<tr><td>[B]</td><td>ethanol</td><td>\(\ce{CH3CH2OH}\)</td></tr>
<tr><td>[C]</td><td>ethanal (acetaldehyde)</td><td>\(\ce{CH3CHO}\)</td></tr>
<tr><td>[D]</td><td>ethanoic acid (acetic acid)</td><td>\(\ce{CH3COOH}\)</td></tr>
<tr><td>[E]</td><td>ethyl ethanoate (ethyl acetate)</td><td>\(\ce{CH3COOC2H5}\)</td></tr></table>
<p>\(\ce{CH3CH2NH2 + HNO2 -> CH3CH2OH + N2 + H2O}\)</p>
<p>\(\ce{CH3CH2OH ->[K2Cr2O7/H+][{[O]}] CH3CHO + H2O}\)</p>
<p>\(\ce{CH3CHO + 2[Ag(NH3)2]+ + 3OH- -> CH3COO- + 2Ag v + 4NH3 + 2H2O}\) (acidified: \(\ce{CH3COOH}\))</p>
<p>\(\ce{CH3COOH + C2H5OH <=>[\text{conc.} H2SO4] CH3COOC2H5 + H2O}\) (fruity, sweet smell)</p>
<p><b>(b)</b> \[\ce{C2H5NH2 + HNO2 -> C2H5OH + N2 ^ + H2O}\]</p>
<p><span class="box">ethanol + nitrogen + water</span></p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Aliphatic 1&deg; amine + \(\ce{HNO2}\) &rarr; alcohol + \(\ce{N2}\) (brisk effervescence).</li>
<li>1&deg; alcohol &rarr; aldehyde &rarr; acid; acid + alcohol &rarr; ester (conc. \(\ce{H2SO4}\)).</li></ul>"""),
        Q("12(ii) OR", 3, r"<p style='text-align:center'>OR</p><p>ii. Identify A, B, C, D, E, F in the following "
          r"sequence of reactions:</p>",
          qfig=fg.fig_s1_q12_scheme,
          a=r"""<table class="tbl"><tr><th></th><th>identity</th></tr>
<tr><td>A</td><td>benzene, \(\ce{C6H6}\)</td></tr>
<tr><td>B</td><td>the reducing agent: Sn/HCl (or Fe/HCl)</td></tr>
<tr><td>C</td><td>acetanilide, \(\ce{C6H5NHCOCH3}\)</td></tr>
<tr><td>D</td><td>4-nitroaniline (via 4-nitroacetanilide, hydrolysed)</td></tr>
<tr><td>E</td><td>4-nitrobenzenediazonium chloride</td></tr>
<tr><td>F</td><td>1,4-dinitrobenzene</td></tr></table>
{{fig:0}}
<p>\(\ce{C6H6 + HNO3 ->[\text{conc.} H2SO4][\Delta] C6H5NO2 + H2O}\)</p>
<p>\(\ce{C6H5NO2 + 6[H] ->[Sn/HCl] C6H5NH2 + 2H2O}\)</p>
<p>\(\ce{C6H5NH2 + (CH3CO)2O -> C6H5NHCOCH3 + CH3COOH}\)</p>
<p>Acetylation moderates the &ndash;NH<sub>2</sub> group (and protects it from oxidation), so nitration gives
mainly the para product, which is hydrolysed to 4-nitroaniline:
\(\ce{C6H5NHCOCH3 ->[HNO3/H2SO4] O2N-C6H4-NHCOCH3 ->[H3O+] O2N-C6H4-NH2}\).</p>
<p>\(\ce{O2N-C6H4-NH2 + NaNO2 + 2HCl ->[273-278 K] O2N-C6H4-N2+Cl- + NaCl + 2H2O}\)</p>
<p>\(\ce{O2N-C6H4-N2+Cl- ->[HBF4] O2N-C6H4-N2+BF4- ->[NaNO2, Cu][\Delta] O2N-C6H4-NO2 + N2 + NaBF4}\)</p>
<p class="note">The printed scheme goes straight from D to diazotisation; the free &ndash;NH<sub>2</sub> needed
for that requires the hydrolysis of 4-nitroacetanilide, so D is taken as 4-nitroaniline.</p>""",
          afig=[fg.fig_s1_q12_answer],
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Acetylation of aniline &rarr; p-nitration without oxidation; hydrolysis restores
&ndash;NH<sub>2</sub>.</li><li>Diazonium \(\ce{BF4-}\) salt + \(\ce{NaNO2}\)/Cu, heat &rarr; &ndash;NO<sub>2</sub>
replaces &ndash;N<sub>2</sub><sup>+</sup>.</li></ul>"""),
        Q("13", 3, r"<p>i. Complete and balance the following equations:</p>"
          r"<p>a. K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> + H<sub>2</sub>S + H<sub>2</sub>SO<sub>4</sub> &rarr; "
          r"------ + ------ + ------ + ------</p>"
          r"<p>b. KMnO<sub>4</sub> + FeSO<sub>4</sub> + H<sub>2</sub>SO<sub>4</sub> &rarr; ------ + ------ + ------ "
          r"+ ------</p>"
          r"<p>ii. Explain: Zn salts are white whereas cupric salts are coloured.</p>",
          a=r"""<p><b>(i)(a)</b> \[\ce{K2Cr2O7 + 3H2S + 4H2SO4 -> K2SO4 + Cr2(SO4)3 + 7H2O + 3S v}\]</p>
<p>(\(\ce{Cr2O7^2- + 8H+ + 3H2S -> 2Cr^3+ + 3S + 7H2O}\): orange to green, yellow sulphur deposited.)</p>
<p><b>(b)</b> \[\ce{2KMnO4 + 10FeSO4 + 8H2SO4 -> K2SO4 + 2MnSO4 + 5Fe2(SO4)3 + 8H2O}\]</p>
<p>(\(\ce{MnO4- + 5Fe^2+ + 8H+ -> Mn^2+ + 5Fe^3+ + 4H2O}\))</p>
<p><b>(ii)</b> Colour of transition-metal ions arises from <b>d&ndash;d transitions</b>: in the presence of
ligands the d orbitals split, and an electron absorbs visible light to jump from a lower to a higher d level;
the complementary colour is seen.</p>
<ul><li>\(\ce{Zn^2+}\): 3d<sup>10</sup> &mdash; d orbitals completely filled, no d&ndash;d transition possible &rArr;
no visible absorption &rArr; white.</li>
<li>\(\ce{Cu^2+}\): 3d<sup>9</sup> &mdash; one vacancy (one unpaired electron), d&ndash;d transition absorbs
red/orange light &rArr; blue (hydrated) colour.</li></ul>""",
          topic="d- and f-Block Elements",
          recall=r"""<ul><li>Acidic \(\ce{Cr2O7^2-}\) gains 6e<sup>&minus;</sup> (Cr +6 &rarr; +3); acidic
\(\ce{MnO4-}\) gains 5e<sup>&minus;</sup> (Mn +7 &rarr; +2).</li>
<li>Coloured ions need partly filled d orbitals (d<sup>1</sup>&ndash;d<sup>9</sup>).</li></ul>"""),
        Q("14", 3, r"<p>i. Identify A, B, C, D in the following:</p><p>{{fig:0}}</p>"
          r"<p>ii. Haloarenes are less reactive than haloalkanes towards nucleophilic substitution reactions. "
          r"Explain.</p>",
          qfig=fg.fig_s1_q14_scheme,
          a=r"""<p><b>(i)</b> C + Na/CH<sub>3</sub>Cl gives toluene (Wurtz&ndash;Fittig), so C is chlorobenzene;
it came from a diazonium salt B by Sandmeyer reaction, so A is aniline.</p>
<p><span class="box">A = aniline; B = benzenediazonium chloride; C = chlorobenzene; D = biphenyl</span></p>
{{fig:0}}
<p>\(\ce{C6H5NH2 + NaNO2 + 2HCl ->[273-278 K] C6H5N2+Cl- + NaCl + 2H2O}\)</p>
<p>\(\ce{C6H5N2+Cl- ->[CuCl/HCl][\Delta] C6H5Cl + N2}\) (Sandmeyer)</p>
<p>\(\ce{C6H5Cl + 2Na + CH3Cl ->[dry ether] C6H5CH3 + 2NaCl}\) (Wurtz&ndash;Fittig)</p>
<p>\(\ce{2C6H5Cl + 2Na ->[dry ether] C6H5-C6H5 + 2NaCl}\) (Fittig) &rArr; D</p>
<p><b>(ii)</b></p><ol>
<li><b>Resonance</b>: a lone pair of the halogen is delocalised into the ring, giving the C&ndash;X bond partial
double-bond character; it is shorter and stronger and harder to break.</li>
<li><b>Hybridisation</b>: the C of C&ndash;X is sp<sup>2</sup> (more s-character, more electronegative) and holds
the bonding pair more tightly than an sp<sup>3</sup> carbon.</li>
<li><b>Instability of the phenyl cation</b>: S<sub>N</sub>1 would need \(\ce{C6H5+}\), which is not stabilised by
resonance; and back-side S<sub>N</sub>2 attack is blocked by the ring and the electron-rich &pi; cloud repels the
nucleophile.</li></ol>""",
          afig=[fg.fig_s1_q14_answer],
          topic="Haloalkanes and Haloarenes",
          recall=r"""<ul><li>Sandmeyer: \(\ce{ArN2+}\) + CuCl/HCl &rarr; ArCl.</li>
<li>Wurtz&ndash;Fittig: ArX + RX + Na; Fittig: 2ArX + Na &rarr; Ar&ndash;Ar.</li></ul>"""),
        Q("15", 3, r"<p>i. The structure of glycine and alanine are given below. Show the peptide bond linkage in "
          r"glycylalanine.</p><p>{{fig:0}}</p><p>ii. Deficiency of which vitamin causes the following diseases:<br>"
          r"a. Beri-beri &nbsp;&nbsp; b. Rickets</p><p>iii. What is isoelectric point?</p>",
          qfig=fg.fig_s1_gly_ala,
          a=r"""<p><b>(i)</b> In glycylalanine (Gly-Ala) the &ndash;COOH of glycine condenses with the &ndash;NH<sub>2</sub>
of alanine, eliminating water; the &ndash;CO&ndash;NH&ndash; link formed is the peptide bond.</p>
{{fig:0}}
<p><b>(ii)</b> (a) Beri-beri: <b>vitamin B<sub>1</sub></b> (thiamine). (b) Rickets: <b>vitamin D</b>.</p>
<p><b>(iii)</b> The <b>isoelectric point</b> is the pH at which an amino acid exists entirely as the
zwitterion (\(\ce{H3N+-CHR-COO-}\)), carrying no net charge, so it does not migrate towards either electrode in
an electric field. (For glycine pI &asymp; 6.0.)</p>""",
          afig=[fg.fig_s1_glyala],
          topic="Biomolecules",
          recall=r"""<ul><li>Peptide bond: amide link &ndash;CO&ndash;NH&ndash; between &alpha;-COOH of one amino acid
and &alpha;-NH<sub>2</sub> of the next; name from the N-terminal residue (-yl) to the C-terminal.</li>
<li>B<sub>1</sub> &ndash; beri-beri; C &ndash; scurvy; D &ndash; rickets; A &ndash; night blindness; K &ndash;
delayed clotting.</li></ul>"""),
        Q("16(i)", 3, r"<p>i. a. 0.3605 g of a metal is deposited on the electrode by passing 1.2 A of current for "
          r"15 min through its salt solution. The atomic weight of metal is 96. What is the valency of the metal?</p>"
          r"<p>b. A copper-silver cell is set up is shown below. Determine the concentration of AgNO<sub>3</sub> in "
          r"the cell.</p>",
          qfig=fg.fig_s1_cu_ag_cell,
          a=r"""<p><b>(a)</b> \(Q = It = 1.2\ \text{A}\times(15\times60)\ \text{s} = 1080\) C.</p>
<p>By Faraday's laws, mass deposited by 96500 C = equivalent mass:</p>
<p>\[E = \frac{w\times96500}{Q} = \frac{0.3605\times96500}{1080} = 32.2\ \text{g}\]</p>
<p>\[\text{valency} = \frac{\text{atomic mass}}{\text{equivalent mass}} = \frac{96}{32.2} = 2.98 \approx 3\]</p>
<p><span class="box">Valency of the metal = 3</span></p>
<p><b>(b)</b> Cu is the anode and Ag the cathode:
\(\ce{Cu(s) + 2Ag+(aq) -> Cu^2+(aq) + 2Ag(s)}\), \(n = 2\).</p>
<p>\(E^\circ_\text{cell} = 0.80 - 0.34 = 0.46\) V. Nernst equation at 298 K:</p>
<p>\[E_\text{cell} = E^\circ_\text{cell} - \frac{0.0591}{2}\log\frac{[\ce{Cu^2+}]}{[\ce{Ag+}]^2}\]</p>
<p>\[0.422 = 0.46 - 0.02955\log\frac{0.10}{[\ce{Ag+}]^2}
\;\Rightarrow\; \log\frac{0.10}{[\ce{Ag+}]^2} = \frac{0.038}{0.02955} = 1.286\]</p>
<p>\[\frac{0.10}{[\ce{Ag+}]^2} = 19.32 \;\Rightarrow\; [\ce{Ag+}]^2 = 5.18\times10^{-3}
\;\Rightarrow\; [\ce{Ag+}] = 0.072\ \text{M}\]</p>
<p><span class="box">[AgNO<sub>3</sub>] &asymp; 0.072 mol L<sup>&minus;1</sup></span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>\(w = \frac{E\,I\,t}{96500}\); valency = atomic mass / equivalent mass.</li>
<li>Nernst: \(E = E^\circ - \frac{0.0591}{n}\log Q\), with \(Q = \frac{[\text{products}]}{[\text{reactants}]}\)
(solids omitted).</li></ul>"""),
        Q("16(ii) OR", 3, r"<p style='text-align:center'>OR</p><p>ii. The specific conductance of 0.01M solution of "
          r"acetic acid at 298K is 1.65 &times; 10<sup>&minus;4</sup> S cm<sup>&minus;1</sup>. The molar conductance "
          r"at infinite dilution for H<sup>+</sup> ion and CH<sub>3</sub>COO<sup>&minus;</sup> ion are 349.1 S cm<sup>2</sup> "
          r"mol<sup>&minus;1</sup> and 40.9 S cm<sup>2</sup> mol<sup>&minus;1</sup> respectively. Calculate &ndash;</p>"
          r"<p>a. molar conductance of the solution<br>b. degree of dissociation of acetic acid<br>"
          r"c. dissociation constant for acetic acid.</p>",
          a=r"""<p><b>(a)</b> \[\Lambda_m = \frac{\kappa\times1000}{C} = \frac{1.65\times10^{-4}\times1000}{0.01}
= 16.5\ \text{S cm}^2\,\text{mol}^{-1}\]</p>
<p><b>(b)</b> Kohlrausch's law: \(\Lambda^\circ_m = \lambda^\circ_{\ce{H+}} + \lambda^\circ_{\ce{CH3COO-}}
= 349.1 + 40.9 = 390.0\) S cm<sup>2</sup> mol<sup>&minus;1</sup>.</p>
<p>\[\alpha = \frac{\Lambda_m}{\Lambda^\circ_m} = \frac{16.5}{390} = 0.0423\]</p>
<p><b>(c)</b> \[K_a = \frac{C\alpha^2}{1-\alpha} = \frac{0.01\times(0.0423)^2}{1-0.0423}
= 1.87\times10^{-5}\]</p>
<p><span class="box">\(\Lambda_m = 16.5\) S cm<sup>2</sup> mol<sup>&minus;1</sup>; \(\alpha = 0.0423\);
\(K_a = 1.87\times10^{-5}\) (\(\approx 1.79\times10^{-5}\) if \(1-\alpha \approx 1\))</span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>\(\Lambda_m = \kappa\times1000/C\) (C in mol L<sup>&minus;1</sup>).</li>
<li>Kohlrausch: \(\Lambda^\circ_m = \nu_+\lambda^\circ_+ + \nu_-\lambda^\circ_-\); \(\alpha = \Lambda_m/\Lambda^\circ_m\).</li>
<li>Ostwald: \(K_a = C\alpha^2/(1-\alpha)\).</li></ul>"""),
        Q("17", 3, r"<p>i. Identify the order of reaction if the following are the units of rate constant (k):<br>"
          r"a. mol L<sup>&minus;1</sup> sec<sup>&minus;1</sup> &nbsp; b. mol<sup>&minus;1</sup> L sec<sup>&minus;1</sup></p>"
          r"<p>ii. For the reaction, 2N<sub>2</sub>O<sub>5</sub>(g) &rarr; 4NO<sub>2</sub>(g) + O<sub>2</sub>(g)</p>"
          r"<table class='tbl'><tr><th>S.No.</th><th>conc. of [N<sub>2</sub>O<sub>5</sub>] mol L<sup>&minus;1</sup></th>"
          r"<th>Rate of disappearance of [N<sub>2</sub>O<sub>5</sub>]; mol L<sup>&minus;1</sup>min<sup>&minus;1</sup></th></tr>"
          r"<tr><td>1.</td><td>1.13 &times; 10<sup>&minus;2</sup></td><td>34 &times; 10<sup>&minus;5</sup></td></tr>"
          r"<tr><td>2.</td><td>0.84 &times; 10<sup>&minus;2</sup></td><td>25 &times; 10<sup>&minus;5</sup></td></tr>"
          r"<tr><td>3.</td><td>0.62 &times; 10<sup>&minus;2</sup></td><td>18 &times; 10<sup>&minus;5</sup></td></tr></table>"
          r"<p>a. Calculate the order of reaction<br>b. Write the rate law<br>c. Calculate the rate constant of the "
          r"reaction.</p>",
          a=r"""<p><b>(i)</b> Units of k = (mol L<sup>&minus;1</sup>)<sup>1&minus;n</sup> s<sup>&minus;1</sup>.</p>
<p>(a) mol L<sup>&minus;1</sup> s<sup>&minus;1</sup> &rArr; \(1-n = 1\) &rArr; <b>zero order</b>.<br>
(b) mol<sup>&minus;1</sup> L s<sup>&minus;1</sup> &rArr; \(1-n = -1\) &rArr; <b>second order</b>.</p>
<p><b>(ii)(a)</b> Let rate \(= k[\ce{N2O5}]^n\). From experiments 1 and 2:</p>
<p>\[\frac{34\times10^{-5}}{25\times10^{-5}} = \left(\frac{1.13}{0.84}\right)^n \Rightarrow 1.36 = (1.345)^n
\Rightarrow n = \frac{\log1.36}{\log1.345} = 1.04 \approx 1\]</p>
<p>(Experiments 2 and 3 give \(n = 1.08 \approx 1\).) The rate is proportional to \([\ce{N2O5}]\): rate/conc
is constant (30.1, 29.8, 29.0 &times; 10<sup>&minus;3</sup> min<sup>&minus;1</sup>).
<span class="box">First order</span></p>
<p><b>(b)</b> <span class="box">Rate \(= -\dfrac{d[\ce{N2O5}]}{dt} = k[\ce{N2O5}]\)</span></p>
<p><b>(c)</b> \(k = \dfrac{\text{rate}}{[\ce{N2O5}]}\): \(\dfrac{34\times10^{-5}}{1.13\times10^{-2}} = 3.01\times10^{-2}\),
\(\dfrac{25\times10^{-5}}{0.84\times10^{-2}} = 2.98\times10^{-2}\),
\(\dfrac{18\times10^{-5}}{0.62\times10^{-2}} = 2.90\times10^{-2}\) min<sup>&minus;1</sup>.</p>
<p><span class="box">\(k \approx 2.96\times10^{-2}\) min<sup>&minus;1</sup> (mean)</span></p>
<p class="note">If the rate is defined per mole of reaction, \(-\frac{1}{2}\frac{d[\ce{N2O5}]}{dt} = k'[\ce{N2O5}]\),
then \(k' = 1.48\times10^{-2}\) min<sup>&minus;1</sup>. The table gives the rate of disappearance, so k above is
the expected answer.</p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>Unit of k for order n: (mol L<sup>&minus;1</sup>)<sup>1&minus;n</sup> time<sup>&minus;1</sup>.</li>
<li>Method of initial rates: ratio of rates = (ratio of concentrations)<sup>n</sup>.</li></ul>"""),
        Q("18", 3, r"<p>i. Arrange the following in the decreasing order of acid strength:<br>o-hydroxybenzoic acid, "
          r"p-hydroxybenzoic acid, m-hydroxybenzoic acid, benzoic acid</p>"
          r"<p>ii. Convert &ndash; Acetophenone to benzoic acid.</p>"
          r"<p>iii. Compound [A] having molecular formula C<sub>5</sub>H<sub>10</sub>O, forms a phenyl hydrazone but "
          r"gives negative Tollen's and iodoform tests. On complete reduction, it gives pentane. Identify the "
          r"compound.</p>",
          a=r"""<p><b>(i)</b> <span class="box">o-hydroxybenzoic acid &gt; m-hydroxybenzoic acid &gt; benzoic acid
&gt; p-hydroxybenzoic acid</span></p>
<p>(pK<sub>a</sub> 2.98, 4.08, 4.20, 4.58.) Ortho: the carboxylate ion is stabilised by intramolecular
H-bonding with the o-OH (ortho effect), so it is by far the strongest. Meta: &ndash;OH acts only by its
electron-withdrawing &ndash;I effect &rArr; slightly stronger than benzoic acid. Para: the +R (electron-releasing)
effect of &ndash;OH outweighs &ndash;I and destabilises the anion &rArr; weaker than benzoic acid.</p>
{{fig:0}}
<p><b>(ii)</b> Haloform (iodoform) reaction, then acidify:</p>
<p>\[\ce{C6H5COCH3 + 3I2 + 4NaOH -> C6H5COONa + CHI3 v + 3NaI + 3H2O}\]</p>
<p>\[\ce{C6H5COONa + HCl -> C6H5COOH + NaCl}\]</p>
<p>(Oxidation with alkaline \(\ce{KMnO4}\) followed by acidification also gives benzoic acid.)</p>
<p><b>(iii)</b> Phenylhydrazone &rArr; carbonyl compound; negative Tollens' &rArr; ketone, not aldehyde; negative
iodoform &rArr; not a methyl ketone (no \(\ce{CH3CO-}\)); reduction to <i>n</i>-pentane &rArr; unbranched chain.
The only C<sub>5</sub> straight-chain ketone without a \(\ce{CH3CO-}\) group is pentan-3-one.</p>
<p><span class="box">A = pentan-3-one, \(\ce{CH3CH2COCH2CH3}\)</span></p>
<p>\(\ce{CH3CH2COCH2CH3 ->[Zn-Hg/\text{conc.} HCl] CH3CH2CH2CH2CH3}\) (Clemmensen)</p>""",
          afig=[fg.fig_s1_salicylate],
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Electron-withdrawing groups increase, electron-releasing groups decrease, the
acidity of benzoic acid; ortho-substituted acids are stronger (ortho effect).</li>
<li>Iodoform test: \(\ce{CH3CO-}\) or \(\ce{CH3CH(OH)-}\). Tollens': aldehydes only.</li></ul>"""),
        # ------------------------------------------------------------------ Section D
        SEC("Section D &ndash; 15 Marks"),
        Q("19", 5, r"<p>The human brain's neurotransmitters like dopamine, serotonin, and adrenaline are all amines "
          r"specifically, aromatic amines or heterocyclic amines. Aniline was the first synthetic organic compound "
          r"used to make a dye (&ldquo;Mauveine&rdquo; discovered by William Perkin in 1856), marking the birth of the "
          r"chemical industry! While many aromatic amines (like aniline derivatives) are toxic or carcinogenic, they "
          r"are also the building blocks for drugs, polymers (like polyurethane), and photographic chemicals.</p>"
          r"<p><b>Answer the following questions:</b></p>"
          r"<p>i. Anu was measuring the pK<sub>b</sub> of of two compounds A and B. She recorded her observations in "
          r"the following table:</p>"
          r"<table class='tbl'><tr><th>A</th><th>B</th></tr><tr><td>pK<sub>b</sub> = 4.70</td>"
          r"<td>pK<sub>b</sub> = 9.38</td></tr></table>"
          r"<p>Which test tube is expected to contain benzylamine and which is expected to contain aniline? Give a "
          r"reason for your choice.</p>"
          r"<p>ii. Primary and secondary amines undergo acylation reaction in the presence of a stronger base than "
          r"the amine.</p><p>{{fig:0}}</p>"
          r"<p>a. What would happen if a stronger base is not used for the acylation reaction?</p>"
          r"<p>b. Can we use anhydrous AlCl<sub>3</sub> in place of a strong base? Justify your answer</p>"
          r"<p>iii. Identify the type of amines M, N, O respectively.</p><p>{{fig:1}}</p>",
          qfig=[fg.fig_s1_acylation, fg.fig_s1_amine_flow],
          a=r"""<p><b>(i)</b> Lower pK<sub>b</sub> = stronger base.
<span class="box">A (pK<sub>b</sub> 4.70) = benzylamine; B (pK<sub>b</sub> 9.38) = aniline</span></p>
<p>In benzylamine \(\ce{C6H5CH2NH2}\) the &ndash;NH<sub>2</sub> is on an sp<sup>3</sup> carbon, so its lone pair is
localised on N and freely available (the CH<sub>2</sub> group also releases electrons). In aniline the lone pair
is delocalised into the benzene ring by resonance (and the sp<sup>2</sup> ring carbon withdraws electrons), so it
is far less available for a proton &rArr; aniline is much the weaker base.</p>
<p><b>(ii)(a)</b> The reaction forms HCl as a by-product. Without a stronger base to remove it, HCl would
protonate the unreacted amine to its ammonium salt (\(\ce{C6H5NH3+Cl-}\)), which has no lone pair and cannot
be acylated. The equilibrium would not be shifted forward and the yield of the amide would be poor (at most
half the amine reacts).</p>
<p><b>(b)</b> No. Anhydrous \(\ce{AlCl3}\) is a <b>Lewis acid</b>, not a base: it cannot neutralise HCl. Instead it
would accept the lone pair of nitrogen, forming a complex (\(\ce{C6H5NH2->AlCl3}\)) and deactivating the amine
so that acylation fails.</p>
<p><b>(iii)</b> N gives no product with \(\ce{CH3COCl}\): no N&ndash;H, so it is a <b>tertiary</b> amine. M and O are
acylated (they have N&ndash;H). O gives a foul-smelling isocyanide with \(\ce{CHCl3}\)/KOH (carbylamine test) so it
is <b>primary</b>; M does not, so it is <b>secondary</b>.</p>
<p><span class="box">M = secondary amine; N = tertiary amine; O = primary amine</span></p>
<p>\(\ce{RNH2 + CHCl3 + 3KOH -> RNC + 3KCl + 3H2O}\)</p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Basicity: alkyl / benzyl amines &gt; NH<sub>3</sub> &gt; aniline (resonance).
pK<sub>b</sub> lower &rArr; base stronger.</li>
<li>Acylation needs a replaceable H on N: 1&deg; and 2&deg; amines only. Pyridine removes HCl.</li>
<li>Carbylamine test only for 1&deg; amines.</li></ul>"""),
        Q("20", 5, r"<p>Coordination compounds often show bright colors and are useful in making of dyes and chemical "
          r"indicators. Answer the following questions:</p>"
          r"<p>i. Give IUPAC name of the following co-ordination compound &ndash; [Co(en)<sub>3</sub>]<sup>+3</sup></p>"
          r"<p>ii. When AgNO<sub>3</sub> solution is added into the solution of a co-ordination compound "
          r"PdCl<sub>2</sub>.4NH<sub>3</sub>, it produces 2 moles of AgCl precipitate. On the basis of the "
          r"information above, designate the following:<br>a. coordination entity<br>b. counter ions<br>"
          r"c. coordination number of central metal ion<br>d. the oxidation number of Pd</p>"
          r"<p>iii. In an experiment Test Tube 'A' contains FeSO<sub>4</sub>(NH<sub>4</sub>)<sub>2</sub>SO<sub>4</sub>.6H<sub>2</sub>O "
          r"solution and test tube 'B' contains K<sub>3</sub>[Fe(C<sub>2</sub>O<sub>4</sub>)<sub>3</sub>] solution. "
          r"On adding few drops of KSCN in the two test tubes, solution of one of the test tubes turns into red.<br>"
          r"a. Identify which out of two solutions in the test tubes 'A' or 'B' turns into red?<br>"
          r"b. Give reason why does one solution give red colour with KSCN but other solution does not show any "
          r"change.</p>"
          r"<p>iv. Write the iupac name of the following:<br>a. [PtCl<sub>2</sub>(NH<sub>3</sub>)<sub>4</sub>][PtCl<sub>4</sub>]<br>"
          r"b. K<sub>2</sub>[Zn(OH)<sub>4</sub>]</p>",
          a=r"""<p><b>(i)</b> <span class="box">tris(ethane-1,2-diamine)cobalt(III) ion</span></p>
<p><b>(ii)</b> 2 mol AgCl per mole &rArr; both Cl are ionisable, outside the coordination sphere: the compound is
\(\ce{[Pd(NH3)4]Cl2}\).</p>
<p>(a) coordination entity: \(\ce{[Pd(NH3)4]^2+}\); (b) counter ions: two \(\ce{Cl-}\); (c) coordination number
of Pd: 4; (d) oxidation number of Pd: \(x + 4(0) = +2\) &rArr; <b>+2</b>.</p>
<p><b>(iii)(a)</b> <span class="box">Test tube A (Mohr's salt) turns red</span></p>
<p><b>(b)</b> Mohr's salt is a <b>double salt</b>: in water it dissociates completely into its simple ions
(\(\ce{Fe^2+}\), \(\ce{NH4+}\), \(\ce{SO4^2-}\)), so free iron ions are present in solution (Fe<sup>2+</sup> solutions
always carry some Fe<sup>3+</sup> from aerial oxidation) and they react with thiocyanate:
\(\ce{Fe^3+ + SCN- -> [Fe(SCN)]^2+}\) (blood red). \(\ce{K3[Fe(C2O4)3]}\) is a <b>complex salt</b>: it ionises only
into \(\ce{K+}\) and the stable complex ion \(\ce{[Fe(C2O4)3]^3-}\), in which Fe<sup>3+</sup> is held by three chelating
oxalate ligands; there is practically no free Fe<sup>3+</sup> to react, so no red colour.</p>
<p><b>(iv)</b> (a) <span class="box">tetraamminedichloridoplatinum(IV) tetrachloridoplatinate(II)</span>
(cation: \(x + 0 - 2 = +2\) &rArr; Pt(IV); anion: \(y - 4 = -2\) &rArr; Pt(II)).</p>
<p>(b) <span class="box">potassium tetrahydroxidozincate(II)</span></p>""",
          topic="Coordination Compounds",
          recall=r"""<ul><li>IUPAC: ligands alphabetical (prefixes ignored), metal with oxidation state in Roman
numerals; anionic complex ends in -ate.</li>
<li>Double salt dissociates fully into simple ions; a complex ion persists in solution.</li>
<li>Ionisable Cl<sup>&minus;</sup> = moles of AgCl precipitated.</li></ul>"""),
        Q("21(i)", 5, r"<p>i. a. The osmotic pressure data of some compounds are given at 298 K</p>"
          r"<table class='tbl'><tr><th>Compound</th><th>Concentration (g/L)</th><th>Osmotic pressure (atm)</th></tr>"
          r"<tr><td>NaCl</td><td>12.5</td><td>10.5</td></tr><tr><td>urea</td><td>28.5</td><td>11.6</td></tr></table>"
          r"<p>1. If the concentration of NaCl is reduced by 2 times, what will be its osmotic pressure at 400 K?<br>"
          r"2. When the same urea solution is heated, its osmotic pressure increases by 1.153 atm. What is final "
          r"temperature of the solution? Given the molar mass of urea is 60 g mol<sup>&minus;1</sup>.</p>"
          r"<p>b. Calculate the amount of ice that will separate out on cooling a solution containing 50 g of "
          r"ethylene glycol [CH<sub>2</sub>OH-CH<sub>2</sub>OH] in 200 g of water to &minus;9.3 <sup>0</sup>C. "
          r"[k<sub>f</sub> of water = 1.86 K kg mol<sup>&minus;1</sup>]</p>",
          a=r"""<p><b>(a)1.</b> \(\pi = iCRT\), so for the same solute \(\pi \propto CT\):</p>
<p>\[\pi_2 = \pi_1\times\frac{C_2}{C_1}\times\frac{T_2}{T_1} = 10.5\times\frac12\times\frac{400}{298}
= 7.05\ \text{atm}\]</p>
<p><span class="box">\(\pi \approx 7.05\) atm</span></p>
<p><b>(a)2.</b> Urea: \(C = 28.5/60 = 0.475\) mol L<sup>&minus;1</sup>
(check: \(\pi = CRT = 0.475\times0.0821\times298 = 11.6\) atm &#10003;). At constant C, \(\pi \propto T\):</p>
<p>\[T_2 = T_1\times\frac{\pi_2}{\pi_1} = 298\times\frac{11.6+1.153}{11.6} = 298\times\frac{12.753}{11.6}
= 327.6\ \text{K}\]</p>
<p><span class="box">Final temperature \(\approx 327.6\) K (54.6 &deg;C)</span></p>
<p><b>(b)</b> Moles of glycol \(= 50/62 = 0.8065\) mol. At \(-9.3\) &deg;C, \(\Delta T_f = 9.3\) K.</p>
<p>\[m = \frac{\Delta T_f}{K_f} = \frac{9.3}{1.86} = 5.0\ \text{mol kg}^{-1}\]</p>
<p>Mass of liquid water left \(= \dfrac{0.8065}{5.0}\) kg \(= 0.1613\) kg \(= 161.3\) g.</p>
<p>Ice separated \(= 200 - 161.3 = 38.7\) g.</p>
<p><span class="box">\(\approx 38.7\) g of ice</span></p>""",
          topic="Solutions",
          recall=r"""<ul><li>\(\pi = iCRT\) (C in mol L<sup>&minus;1</sup>, R = 0.0821 L atm K<sup>&minus;1</sup> mol<sup>&minus;1</sup>).</li>
<li>\(\Delta T_f = K_f\dfrac{w_B\times1000}{M_B\times w_A}\): as ice separates, the solution left becomes
more concentrated.</li></ul>"""),
        Q("21(ii) OR", 5, r"<p style='text-align:center'>OR</p>"
          r"<p>ii. a. 1. The elevation of boiling point of water is generally observed by the addition of solute "
          r"like NaCl or glucose which happens due to lowering of vapour pressure but interestingly by the addition "
          r"of methanol boiling point of water decreases. Give a proper reason for that.<br>"
          r"2. A soft drink bottle when opened, fizz sounds come out. Why?</p>"
          r"<p>b. 1. The vapour pressure of pure liquids A and B are 450 and 700 mm Hg respectively, at 350 K. Find "
          r"out the composition of the liquid mixture if total vapour pressure is 600 mm Hg.<br>"
          r"2. What is the composition of the vapour phase?</p>",
          a=r"""<p><b>(a)1.</b> NaCl and glucose are <b>non-volatile</b>: they contribute nothing to the vapour, so
the vapour pressure of the solution falls and a higher temperature is needed to reach 1 atm. Methanol is
<b>volatile</b> &mdash; more volatile than water (b.p. 338 K): it contributes its own partial pressure, so the
total vapour pressure of the mixture is <i>higher</i> than that of water (the mixture also shows positive
deviation from Raoult's law, because methanol&ndash;water H-bonds are weaker than water&ndash;water). The
vapour pressure reaches atmospheric pressure at a lower temperature, so the boiling point falls.</p>
<p><b>(a)2.</b> Soft drinks are bottled with \(\ce{CO2}\) under high pressure; by <b>Henry's law</b>
(\(p = K_H x\)) the solubility of a gas is proportional to its partial pressure. On opening, the pressure drops
to atmospheric, the solubility of \(\ce{CO2}\) falls and the excess gas escapes as bubbles with a fizz.</p>
<p><b>(b)1.</b> Raoult's law: \(P = p^\circ_Ax_A + p^\circ_B(1-x_A)\)</p>
<p>\[600 = 450x_A + 700(1-x_A) \Rightarrow 250x_A = 100 \Rightarrow x_A = 0.40,\; x_B = 0.60\]</p>
<p><b>(b)2.</b> Dalton's law: \(y_A = \dfrac{p^\circ_Ax_A}{P} = \dfrac{450\times0.40}{600} = 0.30\),
\(y_B = \dfrac{700\times0.60}{600} = 0.70\).</p>
<p><span class="box">Liquid: x<sub>A</sub> = 0.40, x<sub>B</sub> = 0.60; vapour: y<sub>A</sub> = 0.30,
y<sub>B</sub> = 0.70</span></p>
<p>(The vapour is richer in the more volatile component B.)</p>""",
          topic="Solutions",
          recall=r"""<ul><li>Raoult: \(p_A = p^\circ_Ax_A\); total \(P = p_A + p_B\). Dalton: \(y_A = p_A/P\).</li>
<li>Henry: \(p = K_Hx\) &mdash; gas solubility &prop; partial pressure.</li></ul>"""),
    ])
