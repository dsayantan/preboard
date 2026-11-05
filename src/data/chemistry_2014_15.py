"""Chemistry pre-board 2014-15, Paper 1 (Theory).  Transcribed from the page images (6 printed pages)."""
from kit import Q, SEC
import chemistry_2014_15_figs as F

SOL, EL, KIN = "Solutions", "Electrochemistry", "Chemical Kinetics"
DF, COORD = "d- and f-Block Elements", "Coordination Compounds"
HALO, ALC = "Haloalkanes and Haloarenes", "Alcohols, Phenols and Ethers"
CARB, NIT, BIO = "Aldehydes, Ketones and Carboxylic Acids", "Organic Compounds containing Nitrogen", "Biomolecules"

ION = "Ionic equilibrium (acid–base ionisation, salt hydrolysis, buffers, solubility product) — Class XI; not in the ISC 2027 Class XII units."
EQM = "Chemical equilibrium (Kp, Kc, Le Chatelier's principle) — Class XI; not in the ISC 2027 Class XII units."
SOLID = "Solid state (defects, voids, packing) — removed; not among the ten ISC 2027 Class XII units."
PBLK = "p-Block elements — not in the ISC 2027 Class XII syllabus, whose inorganic units are only d- and f-block and coordination compounds."
MET = "Metallurgy (extraction of silver) — removed; not in the ISC 2027 Class XII syllabus."
POLY = "Polymers — removed from the ISC Class XII theory syllabus; not in the ISC 2027 unit list (now only a suggested project)."
GLY = ("Reactions of glycerol (with oxalic acid, giving formic acid) — the ISC 2027 Alcohols unit covers chemical "
       "properties of primary (monohydric) alcohols only; this reaction is no longer listed.")

PAPER = dict(
    subject="chemistry",
    year="2014-15",
    slug="2014-15",
    paper="Paper 1 (Theory)",
    source="PreBoard-PYQ/2014-15/Chemistry.pdf",
    marks=70, time="3 hours",
    intro=r"""<p>(Candidates are allowed additional 15 minutes for only reading the paper. They must NOT start writing
during this time)</p>
<p>Answer all questions in <b>Part I</b> and six from <b>Part II</b>.</p>
<p>All working, including rough work, should be done on the same sheet as and adjacent to, the rest of the answer.</p>
<p>The intended marks for questions or parts of questions are given in brackets [ ].</p>
<p>Balanced equations must be given wherever possible and diagrams where they are helpful.</p>
<p>When solving numerical problems, all essential working must be shown. In working out problems, use the following
data. Gas Constant R = 1.987 cal deg<sup>−1</sup> mol<sup>−1</sup> = 0.0821 dm<sup>3</sup> atm K<sup>−1</sup> mol<sup>−1</sup>.
1 L atm = 1 dm<sup>3</sup></p>
<p>This Paper Consists Of 6 Printed Pages</p>""",
    items=[
        SEC("PART – I", "(Answer all questions)"),
        # ------------------------------------------------------------------ 1(a)
        Q("1(a)(i)", 1, r"""<p><b>Fill in the blanks</b> by choosing the appropriate word / words from given in brackets:
[Sandmayer, 6, 4, 12, +1, +2, +3, +4, HCl, HClO, \(\ce{H2S}\), more, Gattermann, \(\ce{H2SO4}\), nitrobenzene, phenyl
isocyanide, phenyl cyanide, less, scurvy, rickets, sterility, pernicious anaemia]</p>
<p>(i) The dissociation of \(\ce{H2S}\) is ______ in HCl while ______ in \(\ce{NH4OH}\).</p>""", excluded=ION),
        Q("1(a)(ii)", 1, r"""<p><b>Fill in the blanks</b> by choosing the appropriate word / words from given in brackets:
[Sandmayer, 6, 4, 12, +1, +2, +3, +4, HCl, HClO, \(\ce{H2S}\), more, Gattermann, \(\ce{H2SO4}\), nitrobenzene, phenyl
isocyanide, phenyl cyanide, less, scurvy, rickets, sterility, pernicious anaemia]</p>
<p>(ii) The cordination number and the oxidation state of the element E in the complex
\(\ce{[E(en)2(C2O4)]NO2}\) are respectively ______ and ______.</p>""",
          a=r"""<p class="step">Coordination number: each en and \(\ce{C2O4^2-}\) is bidentate ⇒ \(2\times2 + 1\times2 = 6\).</p>
<p class="step">Oxidation state: the complex ion is \(\ce{[E(en)2(C2O4)]+}\) (balanced by \(\ce{NO2-}\)).
\(x + 2(0) + (-2) = +1 \Rightarrow x = +3\).</p>
<p><span class="box">6 and +3</span></p>""",
          topic=COORD,
          recall=r"""<ul><li>CN = number of donor atoms bonded (count bidentate ligands twice).</li>
<li>en is neutral; oxalate is \(\ce{C2O4^2-}\); sum of charges = charge on the complex ion.</li></ul>"""),
        Q("1(a)(iii)", 1, r"""<p>(iii) Sulphur dioxide reacts with chlorine in the presence of moisture to form ______ and ______.</p>""",
          excluded=PBLK),
        Q("1(a)(iv)", 1, r"""<p>(iv) Reaction of benzene diazonium chloride with potassium cyanide in presence of copper powder
produces ______ and is known as ______ reaction.</p>""",
          a=r"""<p><span class="box">phenyl cyanide (benzonitrile); Gattermann reaction</span></p>
\[\ce{C6H5N2+Cl- + KCN ->[Cu] C6H5CN + N2 ^ + KCl}\]
<p>With copper powder as catalyst the replacement is the <b>Gattermann</b> reaction; the same product with
\(\ce{CuCN/KCN}\) is the Sandmeyer reaction.</p>""",
          topic=NIT,
          recall=r"""<ul><li>Sandmeyer: \(\ce{ArN2+}\) + CuCl/CuBr/CuCN → ArCl/ArBr/ArCN.</li>
<li>Gattermann: same replacements using Cu powder with the halogen acid (or KCN).</li></ul>"""),
        Q("1(a)(v)", 1, r"""<p>(v) Deficiency of vitamin C leads to ______ and that of vitamin \(\ce{B12}\) leads to ______.</p>""",
          a=r"""<p><span class="box">scurvy; pernicious anaemia</span></p>""",
          topic=BIO,
          recall=r"""<ul><li>A — night blindness; B₁ — beri-beri; B₁₂ — pernicious anaemia; C — scurvy; D — rickets; E — sterility;
K — delayed clotting.</li><li>Water-soluble: B, C. Fat-soluble: A, D, E, K.</li></ul>"""),
        # ------------------------------------------------------------------ 1(b)
        Q("1(b)(i)", 1, r"""<p><b>Complete the following statements by selecting the correct alternative from the choices given:</b></p>
<p>(i) When potassium cyanide is added to water, then: (a) pH will increase (b) pH will decrease (c) pH will remain
the same (d) electrical conductivity will not change.</p>""", excluded=ION),
        Q("1(b)(ii)", 1, r"""<p><b>Complete the following statements by selecting the correct alternative from the choices given:</b></p>
<p>(ii) In the following sequence of reactions,</p>
\[\ce{CH3CH2OH ->[P + I2] A ->[Mg/Ether] B ->[HCHO] C ->[H2O/H+] D}\]
<p>The compound D is: (a) Butanal (b) N-methyl propanamine (b) Propanol (d) Propanal.</p>""",
          a=r"""\[\ce{CH3CH2OH ->[P/I2] CH3CH2I (A) ->[Mg][dry ether] CH3CH2MgI (B)}\]
\[\ce{CH3CH2MgI + HCHO -> CH3CH2CH2OMgI (C) ->[H2O/H+] CH3CH2CH2OH (D) + Mg(OH)I}\]
<p>A Grignard reagent adds to methanal to give, after hydrolysis, a primary alcohol with one more carbon.</p>
<p><span class="box">D = propan-1-ol (Propanol) — the option printed as the second "(b)", i.e. (c)</span></p>
<p class="note">[Misprint in the original: the options are lettered (a), (b), (b), (d).]</p>""",
          topic=ALC,
          recall=r"""<ul><li>RMgX + HCHO → 1° alcohol; + RCHO → 2°; + ketone → 3° (after hydrolysis).</li>
<li>P/I₂ (\(\ce{PI3}\)) converts R–OH to R–I.</li></ul>"""),
        Q("1(b)(iii)", 1, r"""<p>(iii) The standard reduction potentials for \(\ce{Zn^2+/Zn}\), \(\ce{Ni^2+/Ni}\) and \(\ce{Fe^2+/Fe}\) are
−0.76, −0.23 and −0.44 V respectively. The reaction \(\ce{X + Y^2+ -> X^2+ + Y}\) will be spontaneous when:</p>
<p>(a) X = Ni, Y = Zn (b) X = Fe, Y = Zn (c) X = Zn, Y = Ni (d) X = Ni, Y = Fe.</p>""",
          a=r"""<p>X is oxidised (anode), \(\ce{Y^2+}\) is reduced (cathode); spontaneous if
\(E^\circ_\text{cell} = E^\circ_{\ce{Y}} - E^\circ_{\ce{X}} &gt; 0\).</p>
<p>(a) −0.76 − (−0.23) = −0.53 V; (b) −0.76 − (−0.44) = −0.32 V; (c) −0.23 − (−0.76) = <b>+0.53 V</b>;
(d) −0.44 − (−0.23) = −0.21 V.</p>
<p><span class="box">(c) X = Zn, Y = Ni</span> (\(E^\circ = +0.53\) V, \(\Delta G^\circ = -nFE^\circ &lt; 0\))</p>""",
          topic=EL,
          recall=r"""<ul><li>\(E^\circ_\text{cell} = E^\circ_\text{cathode} - E^\circ_\text{anode}\); spontaneous when positive.</li>
<li>A metal lower in the electrochemical series (more negative \(E^\circ\)) displaces one above it.</li></ul>"""),
        Q("1(b)(iv)", 1, r"""<p>(iv) Kp / Kc for the reaction, \(\ce{CO(g) + 1/2O2(g) <=> CO2(g)}\) is:
(a) 1 (b) \(1/\sqrt{RT}\) (b) RT (d) \(RT^{1/2}\)</p>""", excluded=EQM),
        Q("1(b)(v)", 1, r"""<p>(v) Lanthanide Contraction is due to increase in (a) Shielding effect (b) Atomic No. (c) Size of 4f Orbital
(d) Effective nuclear charge</p>""",
          a=r"""<p><span class="box">(d) Effective nuclear charge</span></p>
<p>Across the lanthanoids each added proton is matched by an electron entering the 4f subshell; 4f electrons shield
one another poorly (diffuse shape), so the effective nuclear charge felt by the outer electrons rises steadily and
the atomic/ionic radii decrease from La to Lu.</p>""",
          topic=DF,
          recall=r"""<ul><li>Lanthanoid contraction: steady decrease in size La → Lu due to imperfect shielding by 4f electrons.</li>
<li>Consequences: Zr/Hf nearly equal size; basicity of \(\ce{Ln(OH)3}\) decreases La → Lu.</li></ul>"""),
        # ------------------------------------------------------------------ 1(c)
        Q("1(c)(i)", 1, r"""<p><b>Answer the following questions:</b></p>
<p>(i) A reaction is 50% complete in 2 hours and 75% complete in 4 hours. What is the order of the reaction?</p>""",
          a=r"""<p>50% → 2 h: first half-life = 2 h. 75% means half of the remaining 50% has also reacted in the next 2 h:
the second half-life is also 2 h. The half-life does not depend on the concentration left, which is true only
for a first-order reaction (\(t_{1/2} = 0.693/k\)).</p>
<p>Check: \(k = \frac{2.303}{2}\log\frac{100}{50} = 0.3466\ \text{h}^{-1}\) and \(k = \frac{2.303}{4}\log\frac{100}{25} = 0.3466\ \text{h}^{-1}\) — equal.</p>
<p><span class="box">First order</span></p>""",
          topic=KIN,
          recall=r"""<ul><li>First order: \(t_{1/2} = 0.693/k\), independent of \([A]_0\); \(t_{75\%} = 2t_{1/2}\), \(t_{87.5\%} = 3t_{1/2}\).</li>
<li>Zero order: \(t_{1/2} \propto [A]_0\).</li></ul>"""),
        Q("1(c)(ii)", 1, r"""<p>(ii) A coordination compound is found to contain Pt, \(\ce{NH3}\) and Cl in the molar ratio 1 : 4 : 4.
Platinum is found to be in terapositive state. On treatment with silver nitrate, only 50% of the chlorine gets
precipitated as AgCl. Determine the structure of the coordination compound.</p>""",
          a=r"""<p class="step">Pt(IV) has coordination number 6. Of the 4 Cl, only 2 are precipitated by \(\ce{AgNO3}\) ⇒ 2 Cl are
ionisable (outside the sphere) and 2 are coordinated. The sphere is \(\ce{Pt(NH3)4Cl2}\) (CN = 6) carrying
\(+4 - 2 = +2\).</p>
<p><span class="box">\(\ce{[Pt(NH3)4Cl2]Cl2}\) — tetraamminedichloridoplatinum(IV) chloride</span></p>
\[\ce{[Pt(NH3)4Cl2]Cl2 + 2AgNO3 -> [Pt(NH3)4Cl2](NO3)2 + 2AgCl v}\]
<p>The complex ion is octahedral (\(d^2sp^3\)) and exists as cis and trans isomers:</p>
{{fig:0}}""",
          afig=[(F.fig_q1c2_pt, "Octahedral [Pt(NH₃)₄Cl₂]²⁺: trans (Cl opposite) and cis (Cl adjacent).")],
          topic=COORD,
          recall=r"""<ul><li>Only ions outside the coordination sphere are precipitated (Werner's primary valency).</li>
<li>Pt(IV): CN 6, octahedral; \(\ce{MA4B2}\) shows cis–trans isomerism.</li></ul>"""),
        Q("1(c)(iii)", 1, r"""<p>(iii) Why is \(\ce{KMnO4}\) capable of exhibiting oxidizing properties in neutral, alkaline as well as acidic
solutions?</p>""",
          a=r"""<p>In \(\ce{KMnO4}\) manganese is in its highest oxidation state, +7, so it can only gain electrons; it is reduced
in every medium, to a product that depends on the medium:</p>
\[\text{acidic:}\quad \ce{MnO4- + 8H+ + 5e- -> Mn^2+ + 4H2O}\]
\[\text{neutral / faintly alkaline:}\quad \ce{MnO4- + 2H2O + 3e- -> MnO2 + 4OH-}\]
\[\text{strongly alkaline:}\quad \ce{MnO4- + e- -> MnO4^2-}\]""",
          topic=DF,
          recall=r"""<ul><li>Mn(+7) in \(\ce{MnO4-}\): highest state ⇒ strong oxidant.</li>
<li>Acid → \(\ce{Mn^2+}\) (5 e⁻); neutral → \(\ce{MnO2}\) (3 e⁻); strong alkali → \(\ce{MnO4^2-}\) (1 e⁻).</li></ul>"""),
        Q("1(c)(iv)", 1, r"""<p>(iv) What is the dissociation constant of 0.1M solution of a weak acid HA which is 4.5% ionized at 20°C?</p>""",
          excluded=ION),
        Q("1(c)(v)", 1, r"""<p>(v) Give a balanced equation to show the reaction of glycerol with oxalic acid at 383K.</p>""", excluded=GLY),
        # ------------------------------------------------------------------ 1(d)
        Q("1(d)(i)", 1, r"""<p><b>Match the items of Column A with those of Column B:</b></p>
<div class="tbl"><table><tr><th colspan="2">Column A</th><th colspan="2">Column B</th></tr>
<tr><td>(i)</td><td>Acetone</td><td>(a)</td><td>Saponification</td></tr>
<tr><td>(ii)</td><td>Acetic acid</td><td>(b)</td><td>Bidentate ligand</td></tr>
<tr><td>(iii)</td><td>Propane-1, 2, 3-triol</td><td>(c)</td><td>Lewis base</td></tr>
<tr><td>(iv)</td><td>Ethylene diamine</td><td>(d)</td><td>Iodoform</td></tr>
<tr><td>(v)</td><td>Ethyl amine</td><td>(e)</td><td>Ostwald's dilution law</td></tr></table></div>
<p>(i) Acetone</p>""",
          a=r"""<p><span class="box">(i) Acetone — (d) Iodoform</span></p>
\[\ce{CH3COCH3 + 3I2 + 4NaOH -> CHI3 v + CH3COONa + 3NaI + 3H2O}\]""",
          topic=CARB,
          recall=r"""<ul><li>Iodoform test: positive for CH₃CO– compounds and CH₃CH(OH)– alcohols (yellow \(\ce{CHI3}\)).</li></ul>"""),
        Q("1(d)(ii)", 1, r"""<p>(ii) Acetic acid</p>""",
          a=r"""<p><span class="box">(ii) Acetic acid — (e) Ostwald's dilution law</span></p>
<p>Acetic acid is a weak electrolyte; its degree of dissociation (from \(\alpha = \Lambda_m/\Lambda_m^\circ\)) obeys
\(K_a = C\alpha^2/(1-\alpha)\).</p>""",
          topic=EL,
          recall=r"""<ul><li>Weak electrolytes: \(\alpha\) increases on dilution; \(\Lambda^\circ_m\) found from Kohlrausch's law.</li></ul>"""),
        Q("1(d)(iii)", 1, r"""<p>(iii) Propane-1, 2, 3-triol</p>""",
          a=r"""<p><span class="box">(iii) Propane-1,2,3-triol (glycerol) — (a) Saponification</span></p>
<p>Alkaline hydrolysis of fats (glyceryl esters) gives soap and glycerol.</p>""",
          topic=ALC,
          recall=r"""<ul><li>Fat + 3NaOH → 3 RCOONa (soap) + \(\ce{C3H5(OH)3}\).</li></ul>"""),
        Q("1(d)(iv)", 1, r"""<p>(iv) Ethylene diamine</p>""",
          a=r"""<p><span class="box">(iv) Ethylene diamine — (b) Bidentate ligand</span></p>
<p>\(\ce{H2N-CH2-CH2-NH2}\) binds through both N atoms, forming a five-membered chelate ring.</p>""",
          topic=COORD,
          recall=r"""<ul><li>Bidentate ligands: en, \(\ce{C2O4^2-}\), glycinate; EDTA is hexadentate.</li></ul>"""),
        Q("1(d)(v)", 1, r"""<p>(v) Ethyl amine</p>""",
          a=r"""<p><span class="box">(v) Ethyl amine — (c) Lewis base</span></p>
<p>The lone pair on nitrogen of \(\ce{C2H5NH2}\) can be donated to an electron-pair acceptor.</p>""",
          topic=NIT,
          recall=r"""<ul><li>Amines are bases because of the lone pair on N; \(\ce{C2H5NH2}\) is more basic than \(\ce{NH3}\) (+I effect).</li></ul>"""),
        SEC("PART – II", "Answer six questions choosing two from Section-A, two from Section-B and two from Section-C"),
        SEC("Section – A", "(Answer any two questions)"),
        # ------------------------------------------------------------------ Q2
        Q("2(a)", 3, r"""<p>75.2 gm of phenol (\(\ce{C6H5OH}\)) is dissolved in a solvent of \(K_f = 14\). If the depression in freezing
point is 7 K. Find the % of phenol that dimerises.</p>""",
          a=r"""<p class="note">[Not printed in the original: the mass of solvent. This is the standard problem with 1 kg of
solvent, which is assumed here.]</p>
<p class="step">\(M(\ce{C6H5OH}) = 94\) g mol⁻¹: \(m = \dfrac{75.2/94}{1\ \text{kg}} = 0.8\ \text{mol kg}^{-1}\)</p>
<p class="step">Normal depression: \(\Delta T_f(\text{calc}) = K_f m = 14 \times 0.8 = 11.2\ \text{K}\)</p>
\[i = \frac{\Delta T_f(\text{obs})}{\Delta T_f(\text{calc})} = \frac{7}{11.2} = 0.625\]
<p class="step">Dimerisation \(\ce{2C6H5OH <=> (C6H5OH)2}\): if \(\alpha\) is the fraction dimerised, particles
\(= 1 - \alpha + \alpha/2 = 1 - \alpha/2\).</p>
\[1 - \frac{\alpha}{2} = 0.625 \;\Rightarrow\; \alpha = 0.75\]
<p><span class="box">75% of the phenol dimerises</span></p>""",
          topic=SOL,
          recall=r"""<ul><li>\(i = \Delta T(\text{obs})/\Delta T(\text{calc})\).</li>
<li>Association \(n\mathrm{A} \rightleftharpoons \mathrm{A}_n\): \(i = 1 - \alpha(1 - 1/n)\); for dimers \(i = 1 - \alpha/2\).</li></ul>"""),
        Q("2(b)", 2, r"""<p>If the molality of an aqueous solution of cane sugar is 0.4445, what is the mole fraction of cane sugar?</p>""",
          a=r"""<p class="step">0.4445 mol of sugar in 1000 g water; \(n_{\ce{H2O}} = 1000/18 = 55.56\) mol.</p>
\[x_\text{sugar} = \frac{0.4445}{0.4445 + 55.56} = \frac{0.4445}{56.00} = 7.94\times10^{-3}\]
<p><span class="box">\(x_\text{cane sugar} \approx 0.0079\)</span></p>""",
          topic=SOL,
          recall=r"""<ul><li>Molality = mol solute per kg solvent ⇒ take 1 kg solvent.</li>
<li>\(x_B = n_B/(n_A + n_B)\); \(x_B \approx m M_A/1000\) for dilute solutions.</li></ul>"""),
        Q("2(c)", 1, r"""<p>Common salt or calcium chloride is used to clear snow on the roads. Why?</p>""",
          a=r"""<p>Dissolved salt <b>lowers the freezing point</b> of water (depression of freezing point, a colligative property),
so the ice/snow melts at temperatures below 0 °C and does not re-freeze. \(\ce{CaCl2}\) (\(i \approx 3\)) gives more
particles per mole than NaCl (\(i \approx 2\)) and is more effective.</p>""",
          topic=SOL,
          recall=r"""<ul><li>\(\Delta T_f = iK_f m\): more particles ⇒ larger depression.</li></ul>"""),
        Q("2(d)", 1, r"""<p>Why is potassium chloride violet instead of pure white?</p>""", excluded=SOLID),
        Q("2(e)", 2, r"""<p>A compound formed by two elements M and N. The element N forms ccp and atoms of M occupy 1/3 rd of
tetrahedral voids. What is the formula of the compound?</p>""", excluded=SOLID),
        Q("2(f)", 1, r"""<p>Give an example (equation) of a homogeneously catalysed reaction and name the catalyst.</p>""",
          excluded="Homogeneous and heterogeneous catalysis — part of Surface Chemistry, removed; ISC 2027 Chemical Kinetics covers only the effect of a catalyst on activation energy and rate."),
        # ------------------------------------------------------------------ Q3
        Q("3(a)", 3, r"""<p>5 ml of ethyl acetate was added to a flask containing 100 ml of 0.1 N HCl placed in a thermostate at 23°C.
5ml of the reaction mixture was withdrawn at different intervals of time and after chilling, titrated against a
standard alkali. The following data were obtained.</p>
<div class="tbl"><table><tr><td>Time (min)</td><td>0</td><td>75</td><td>119</td><td>193</td><td>∞</td></tr>
<tr><td>Vol of alkali (ml)</td><td>9.62</td><td>12.10</td><td>13.10</td><td>14.75</td><td>21.05</td></tr></table></div>
<p>show that the above reaction is a first order reaction</p>""",
          a=r"""<p class="step">\(\ce{CH3COOC2H5 + H2O ->[H+] CH3COOH + C2H5OH}\). The alkali titre rises as acetic acid forms.
\(V_\infty - V_0\) ∝ initial ester \([A]_0\) and \(V_\infty - V_t\) ∝ ester left \([A]_t\). If first order:</p>
\[k = \frac{2.303}{t}\log\frac{V_\infty - V_0}{V_\infty - V_t},\qquad V_\infty - V_0 = 21.05 - 9.62 = 11.43\ \text{mL}\]
<div class="tbl"><table><tr><th>t / min</th><th>\(V_\infty - V_t\) / mL</th><th>\(k = \frac{2.303}{t}\log\frac{11.43}{V_\infty-V_t}\) / min⁻¹</th></tr>
<tr><td>75</td><td>8.95</td><td>\(\frac{2.303}{75}\log 1.2771 = 3.26\times10^{-3}\)</td></tr>
<tr><td>119</td><td>7.95</td><td>\(\frac{2.303}{119}\log 1.4377 = 3.05\times10^{-3}\)</td></tr>
<tr><td>193</td><td>6.30</td><td>\(\frac{2.303}{193}\log 1.8143 = 3.09\times10^{-3}\)</td></tr></table></div>
<p>The values of \(k\) are (nearly) constant, so the reaction is first order (pseudo-first-order: water is in large
excess). Equivalently, a plot of \(\log(V_\infty - V_t)\) against \(t\) is a straight line:</p>
{{fig:0}}
<p>Slope \(= -0.200/150 = -1.33\times10^{-3}\ \text{min}^{-1}\Rightarrow k = -2.303\times\text{slope} = 3.07\times10^{-3}\ \text{min}^{-1}\).</p>
<p><span class="box">k ≈ 3.1 × 10⁻³ min⁻¹ (constant) ⇒ first order</span></p>""",
          afig=[(F.fig_q3a_graph, "log₁₀(V∞ − Vt) against t: the four points lie on a straight line.")],
          topic=KIN,
          recall=r"""<ul><li>First order: \(k = \dfrac{2.303}{t}\log\dfrac{[A]_0}{[A]_t}\); \(\log[A]_t\) vs \(t\) is linear, slope \(-k/2.303\).</li>
<li>Acid hydrolysis of ester: \([A]_0 \propto V_\infty - V_0\), \([A]_t \propto V_\infty - V_t\).</li>
<li>Pseudo-first-order: \(\ce{H2O}\) in large excess, its concentration is effectively constant.</li></ul>"""),
        Q("3(b)", 2, r"""<p>Define molecularity of a reaction. Give one difference between the order of a reaction and its molecularity.</p>""",
          a=r"""<p><b>Molecularity</b> is the number of reacting species (atoms, ions or molecules) that must collide simultaneously
in an <b>elementary</b> step for the reaction to occur.</p>
<div class="tbl"><table><tr><th>Order</th><th>Molecularity</th></tr>
<tr><td>Sum of the powers of the concentration terms in the experimentally determined rate law.</td>
<td>Number of species colliding in an elementary step — a theoretical concept.</td></tr>
<tr><td>Can be zero or fractional; determined by experiment.</td><td>Always a small whole number (1, 2, rarely 3); never zero.</td></tr>
<tr><td>Applies to the overall reaction.</td><td>Applies only to an elementary step (for a complex reaction, to the slowest step).</td></tr></table></div>""",
          topic=KIN,
          recall=r"""<ul><li>Rate = \(k[A]^x[B]^y\): order = \(x + y\) (experimental).</li>
<li>Molecularity: elementary steps only; integer ≥ 1.</li></ul>"""),
        Q("3(c)", 3, r"""<p>At 540k, 0.10 mole of \(\ce{PCl5}\) are heated in a 8 litre flast. The pressure of the equilibrium mixture is
found to be 1.0 atm. Calculate Kp and Kc for the reaction.</p>""", excluded=EQM),
        Q("3(d)", 2, r"""<p>What is a buffer solution? Explain the buffer action of a basic buffer with a suitable example.</p>
<p class="note">[No mark is printed against 3(d); 2 marks completes the 10 for Question 3.]</p>""", excluded=ION),
        # ------------------------------------------------------------------ Q4
        Q("4(a)", 3, r"""<p>The solubility product of silver chloride is \(1\times10^{-10}\) at 25°C. Calculate the solubility of silver
chloride in (i) pure water (ii) 0.2 M sodium chloride.</p>""", excluded=ION),
        Q("4(b)", 1, r"""<p>Why is it necessary to use a salt bridge in a galvanic cell?</p>""",
          a=r"""<p>A salt bridge (inert electrolyte such as KCl or \(\ce{KNO3}\) in agar–agar):</p>
<p class="step">1. <b>completes the internal circuit</b> by allowing ions to move between the two half-cells, and</p>
<p class="step">2. <b>keeps each solution electrically neutral</b> — anions drift towards the anode compartment (where
\(\ce{Zn^2+}\) builds up) and cations towards the cathode compartment (where \(\ce{Cu^2+}\) is removed). Without it charge
builds up and the current stops at once. It also minimises the liquid-junction potential.</p>
{{fig:0}}""",
          afig=[(F.fig_q4b_cell, "Daniell cell: through the salt bridge anions (NO₃⁻) drift towards the Zn (anode) side and cations (K⁺) towards the Cu (cathode) side.")],
          topic=EL,
          recall=r"""<ul><li>Galvanic cell: anode (−) oxidation, cathode (+) reduction; electrons flow anode → cathode in the wire.</li>
<li>Salt-bridge electrolyte: ions of similar mobility (\(\ce{K+}\), \(\ce{Cl-}\)/\(\ce{NO3-}\)), inert to both half-cells.</li></ul>"""),
        Q("4(c)", 2, r"""<p>A current of 4 amperes is passed through a molten solution for 45 minutes. 2.977 gm of metal is deposited.
Calculate the charge carried by the metal cation if its atomic mass is 106.4 gm mol⁻¹.</p>""",
          a=r"""<p class="step">\(Q = It = 4\ \text{A}\times(45\times60)\ \text{s} = 10\,800\ \text{C}\)</p>
<p class="step">Moles of electrons \(= \dfrac{10\,800}{96\,500} = 0.1119\ \text{mol}\)</p>
<p class="step">Moles of metal deposited \(= \dfrac{2.977}{106.4} = 0.02798\ \text{mol}\)</p>
\[z = \frac{\text{mol } e^-}{\text{mol metal}} = \frac{0.1119}{0.02798} = 4.0\]
<p><span class="box">The cation carries a charge of +4 (\(\ce{M^4+}\))</span></p>""",
          topic=EL,
          recall=r"""<ul><li>\(\ce{M^{z+} + ze- -> M}\): \(m = \dfrac{M\,It}{zF}\Rightarrow z = \dfrac{M\,It}{mF}\).</li>
<li>1 F = 96 500 C = charge on 1 mol of electrons.</li></ul>"""),
        Q("4(d)", 2, r"""<p>For the cell \(\ce{Zn | Zn^2+ (a = 1) || Cu^2+ (a = 1) | Cu}\)</p>
<p>Given that \(E_{\ce{Zn/Zn^2+}} = 0.761\) V, \(E_{\ce{Cu^2+/Cu}} = 0.339\) v</p>
<p>(i) Write the cell reaction. (ii) Calculate the emf and free energy change at 298k involved in the cell.
(F = 96500 C eq⁻¹)</p>""",
          a=r"""<p class="step"><b>(i)</b> Anode: \(\ce{Zn -> Zn^2+ + 2e-}\); cathode: \(\ce{Cu^2+ + 2e- -> Cu}\)</p>
\[\ce{Zn(s) + Cu^2+(aq) -> Zn^2+(aq) + Cu(s)}\]
<p class="step"><b>(ii)</b> \(E_{\ce{Zn/Zn^2+}} = +0.761\) V is an <i>oxidation</i> potential, i.e. \(E^\circ_{\ce{Zn^2+/Zn}} = -0.761\) V.
Both ions are at unit activity, so \(E = E^\circ\):</p>
\[E^\circ_\text{cell} = E^\circ_\text{cathode} - E^\circ_\text{anode} = 0.339 - (-0.761) = 1.100\ \text{V}\]
\[\Delta G^\circ = -nFE^\circ = -2\times96\,500\times1.100 = -2.123\times10^{5}\ \text{J} = -212.3\ \text{kJ mol}^{-1}\]
<p><span class="box">emf = 1.100 V; ΔG° = −212.3 kJ mol⁻¹ (spontaneous)</span></p>""",
          topic=EL,
          recall=r"""<ul><li>Oxidation potential = − reduction potential.</li>
<li>\(\Delta G^\circ = -nFE^\circ_\text{cell}\); \(n\) = electrons transferred in the balanced cell reaction.</li></ul>"""),
        Q("4(e)", 2, r"""<p>Why does ice melt slowly at higher altitudes?</p>""",
          excluded="Effect of pressure on the ice ⇌ water equilibrium (Le Chatelier's principle / phase equilibrium) — Class XI chemical equilibrium; not in the ISC 2027 Class XII units."),
        SEC("Section – B", "(Answer any two questions)"),
        # ------------------------------------------------------------------ Q5-7
        Q("5(a)(i)", 2, r"""<p>(i) Give the equations for the conversion of argentite (\(\ce{Ag2S}\)) to metallic silver</p>""", excluded=MET),
        Q("5(a)(ii)", 1, r"""<p>(ii) State the type of hybridization and shape of \(\ce{IF7}\).</p>""", excluded=PBLK),
        Q("5(b)", 2, r"""<p>How would you account for the following</p>
<p>(i) \(\ce{SF6}\) exists but \(\ce{OF6}\) does not though both oxygen and sulphur belong to the same group in the periodic table.</p>
<p>(ii) Xenon does not form fluorides such as \(\ce{XeF3}\) and \(\ce{XeF5}\)</p>""", excluded=PBLK),
        Q("6(a)(i)", 1, r"""<p>What do you observe when [2 marks for (i) and (ii) together]</p>
<p>(i) Silver nitrate solution is added to dil HCl followed by \(\ce{NH4OH}\) in excess.</p>""",
          a=r"""<p>A <b>curdy white precipitate</b> of AgCl forms, which <b>dissolves</b> in excess \(\ce{NH4OH}\) to give a
colourless solution of the soluble complex diamminesilver(I) chloride:</p>
\[\ce{AgNO3 + HCl -> AgCl v + HNO3}\]
\[\ce{AgCl + 2NH4OH -> [Ag(NH3)2]Cl + 2H2O}\]""",
          topic=COORD,
          recall=r"""<ul><li>Complex formation used in qualitative analysis: AgCl dissolves in \(\ce{NH3}\) as \(\ce{[Ag(NH3)2]+}\) (linear, sp).</li>
<li>Confirms \(\ce{Cl-}\); AgBr is only sparingly soluble, AgI insoluble in \(\ce{NH3}\).</li></ul>"""),
        Q("6(a)(ii)", 1, r"""<p>(ii) Lead sulphide is heated with ozone</p>""", excluded=PBLK + " (ozone as an oxidant)"),
        Q("6(b)", 3, r"""<p>Write balanced equations for the following</p>
<p>(i) Ozone with moist iodine (ii) Silver nitrate is added to sodium thiosulphate. (iii) Potassium iodide is heated with
conc. \(\ce{H2SO4}\)</p>""",
          excluded="p-Block chemistry (ozone, thiosulphate, halides with conc. H₂SO₄) — not in the ISC 2027 Class XII syllabus."),
        Q("7(a)", 2, r"""<p>Write the IUPAC name of the following:</p>
<p>(i) \(\ce{[Co(CN)(H2O)(en)2]^2+}\) (ii) \(\ce{[Co(NH3)6][Cr(CN)6]}\)</p>""",
          a=r"""<p class="step">(i) Co: \(x + (-1) + 0 + 0 = +2 \Rightarrow x = +3\). Ligands in alphabetical order (aqua, cyanido,
ethane-1,2-diamine — "bis" is ignored):</p>
<p><span class="box">aquacyanidobis(ethane-1,2-diamine)cobalt(III) ion</span></p>
<p class="step">(ii) \(\ce{[Co(NH3)6]^3+}\) cation and \(\ce{[Cr(CN)6]^3-}\) anion (Co +3, Cr +3); the anion takes the ending -ate:</p>
<p><span class="box">hexaamminecobalt(III) hexacyanidochromate(III)</span></p>""",
          topic=COORD,
          recall=r"""<ul><li>Cation first; ligands alphabetical (ignore di/tri/bis); metal with oxidation state in Roman numerals.</li>
<li>Anionic complex: metal name ends in -ate (chromate, ferrate, cuprate…).</li>
<li>Names: aqua (H₂O), ammine (NH₃), cyanido (CN⁻), chlorido (Cl⁻), en = ethane-1,2-diamine.</li></ul>"""),
        Q("7(b)", 2, r"""<p>Using valence bond approach, predict the shape and magnetic behaviour of \(\ce{[Fe(CN)6]^3-}\)</p>""",
          a=r"""<p class="step">Fe: [Ar]3d⁶4s²; in \(\ce{[Fe(CN)6]^3-}\) iron is \(\ce{Fe^3+}\): 3d⁵ (5 unpaired electrons in the free ion).</p>
<p class="step">\(\ce{CN-}\) is a strong-field ligand: it forces the 3d electrons to pair, leaving two 3d orbitals empty. These
combine with 4s and three 4p orbitals — <b>d²sp³</b> (inner-orbital, low-spin) hybridisation — and accept six
electron pairs from six \(\ce{CN-}\).</p>
{{fig:0}}
<p><span class="box">Octahedral; paramagnetic with 1 unpaired electron (μ = √(1×3) = 1.73 BM)</span></p>""",
          afig=[(F.fig_q7b_vbt, "VBT box diagram for [Fe(CN)₆]³⁻: d²sp³, one unpaired electron.")],
          topic=COORD,
          recall=r"""<ul><li>Strong-field ligands (\(\ce{CN-}\), CO, en) cause pairing → inner-orbital d²sp³ (low spin).</li>
<li>Spin-only \(\mu = \sqrt{n(n+2)}\) BM.</li><li>d²sp³ / sp³d² → octahedral; sp³ → tetrahedral; dsp² → square planar.</li></ul>"""),
        Q("7(c)", 1, r"""<p>Draw the structural isomer of \(\ce{[Co(NH3)5NO2]Cl2}\) and name the type of isomerism</p>""",
          a=r"""<p>\(\ce{NO2-}\) is an ambidentate ligand: it can bind through N (nitro) or through O (nitrito). The isomer is
\(\ce{[Co(NH3)5(ONO)]Cl2}\).</p>
{{fig:0}}
<p><span class="box">Linkage isomerism</span></p>
<p>(The ionisation isomer \(\ce{[Co(NH3)5Cl]Cl(NO2)}\) is another structural isomer.)</p>""",
          afig=[(F.fig_q7c_linkage, "Linkage isomers: Co–NO₂ (nitro, yellow) and Co–ONO (nitrito, red).")],
          topic=COORD,
          recall=r"""<ul><li>Structural isomerism: linkage (ambidentate ligand — \(\ce{NO2-}\), \(\ce{SCN-}\)), ionisation, coordination, hydrate.</li>
<li>Stereoisomerism: geometrical and optical.</li></ul>"""),
        SEC("Section – C", "(Answer any two questions)"),
        # ------------------------------------------------------------------ Q8
        Q("8(a)", 3, r"""<p>Write equations for the following reactions and name the reaction.</p>
<p>(i) Acetaldehyde with iodine and NaOH solution. (ii) Benzene with acetyl chloride in presence of anhydrous \(\ce{AlCl3}\)
(iii) Aniline and chloroform with alcoholic potash.</p>""",
          a=r"""<p class="step">(i) <b>Iodoform (haloform) reaction</b> — yellow precipitate of iodoform:</p>
\[\ce{CH3CHO + 3I2 + 4NaOH -> CHI3 v + HCOONa + 3NaI + 3H2O}\]
<p class="step">(ii) <b>Friedel–Crafts acylation</b> — acetophenone:</p>
\[\ce{C6H6 + CH3COCl ->[anhydrous AlCl3] C6H5COCH3 + HCl}\]
<p class="step">(iii) <b>Carbylamine (isocyanide) reaction</b> — phenyl isocyanide, offensive smell:</p>
\[\ce{C6H5NH2 + CHCl3 + 3KOH(alc) ->[\Delta] C6H5NC + 3KCl + 3H2O}\]""",
          topic=CARB,
          recall=r"""<ul><li>Iodoform: CH₃CO– group + \(\ce{I2}\)/NaOH → \(\ce{CHI3}\); acetaldehyde is the only aldehyde that gives it.</li>
<li>Friedel–Crafts acylation: ArH + RCOCl / \(\ce{AlCl3}\) → ArCOR.</li>
<li>Carbylamine: 1° amines only.</li></ul>"""),
        Q("8(b)(i)", 1, r"""<p>(i) How will you prepare (i) phenol from cumene [2 marks for (i) and (ii) together]</p>""",
          a=r"""<p>Cumene (isopropylbenzene) is air-oxidised to cumene hydroperoxide, which is cleaved by dilute acid:</p>
\[\ce{C6H5CH(CH3)2 + O2 ->[air] C6H5C(CH3)2-O-OH}\]
\[\ce{C6H5C(CH3)2-O-OH ->[H+ / H2O] C6H5OH + CH3COCH3}\]
<p>Acetone is obtained as a by-product.</p>""",
          topic=ALC,
          recall=r"""<ul><li>Cumene process: cumene → hydroperoxide → phenol + acetone.</li>
<li>Other routes: from diazonium salt, chlorobenzene (Dow), benzenesulphonic acid.</li></ul>"""),
        Q("8(b)(ii)", 1, r"""<p>(ii) formic acid from glycerol</p>""", excluded=GLY),
        Q("8(c)", 3, r"""<p>Give one good chemical test to distinguish between the following pairs of compounds:</p>
<p>(i) Glycerol and 2- propanol. (ii) Glucose and fructose.</p>""",
          a=r"""<p class="step"><b>(i) Iodoform test.</b> Warm each with iodine and NaOH: <b>propan-2-ol</b> gives a yellow precipitate of
iodoform (it contains CH₃CH(OH)–); glycerol does not.</p>
\[\ce{CH3CH(OH)CH3 + 4I2 + 6NaOH -> CHI3 v + CH3COONa + 5NaI + 5H2O}\]
<p class="step"><b>(ii) Bromine water test.</b> <b>Glucose</b> (an aldose) decolourises bromine water, being oxidised to
gluconic acid; fructose (a ketose) does not.</p>
\[\ce{CH2OH(CHOH)4CHO + Br2 + H2O -> CH2OH(CHOH)4COOH + 2HBr}\]""",
          topic=BIO,
          recall=r"""<ul><li>Iodoform positive: ethanol, propan-2-ol, ethanal, methyl ketones.</li>
<li>Bromine water (mild oxidant) oxidises only the aldehyde group: glucose yes, fructose no.</li>
<li>Both glucose and fructose reduce Tollens' and Fehling's (fructose via enolisation in alkali).</li></ul>"""),
        Q("8(d)", 2, r"""<p>Differentiate between copolymer and homopolymer by giving one example of each with their monomeric units..</p>""",
          excluded=POLY),
        # ------------------------------------------------------------------ Q9
        Q("9(a)", 3, r"""<p>Identify the compounds A, B, C, D, E and F in the given reactions.</p>
{{fig:0}}""",
          qfig=[F.fig_q9a_scheme],
          a=r"""<div class="tbl"><table><tr><th></th><th>Compound</th><th>Formula</th></tr>
<tr><td>A</td><td>methanol</td><td>\(\ce{CH3OH}\)</td></tr>
<tr><td>B</td><td>iodomethane</td><td>\(\ce{CH3I}\)</td></tr>
<tr><td>C</td><td>ethanenitrile (methyl cyanide)</td><td>\(\ce{CH3CN}\)</td></tr>
<tr><td>D</td><td>ethanoic acid</td><td>\(\ce{CH3COOH}\)</td></tr>
<tr><td>E</td><td>ethanamide</td><td>\(\ce{CH3CONH2}\)</td></tr>
<tr><td>F</td><td>ethanamine</td><td>\(\ce{CH3CH2NH2}\)</td></tr></table></div>
\[\ce{HCOOH ->[LiAlH4] CH3OH}\]
\[\ce{2P + 3I2 -> 2PI3};\quad \ce{3CH3OH + PI3 -> 3CH3I + H3PO3}\]
\[\ce{CH3I + KCN -> CH3CN + KI}\]
\[\ce{CH3CN + 2H2O + H+ -> CH3COOH + NH4+}\]
\[\ce{CH3COOH + NH3 -> CH3COONH4 ->[\Delta] CH3CONH2 + H2O}\]
\[\ce{CH3CONH2 + 4[H] ->[Ni/H2] CH3CH2NH2 + H2O}\]
<p class="note">Amides are usually reduced with \(\ce{LiAlH4}\); if strong heating dehydrates E to \(\ce{CH3CN}\), Ni/H₂ reduces
that to the same F, ethanamine.</p>""",
          topic=CARB,
          recall=r"""<ul><li>KCN on an alkyl halide adds one carbon (step-up); hydrolysis of RCN → RCOOH.</li>
<li>RCOOH + \(\ce{NH3}\), heat → \(\ce{RCONH2}\); reduction of amides/nitriles → amines.</li></ul>"""),
        Q("9(b)(i)", 2, r"""<p>How can the following conversions be brought about:</p><p>(i) Benzaldehyde to aniline.</p>""",
          a=r"""<p>Oxidise to benzoic acid, convert to benzamide, then Hofmann bromamide degradation:</p>
\[\ce{C6H5CHO ->[KMnO4/H+] C6H5COOH ->[NH3] C6H5COONH4 ->[\Delta] C6H5CONH2}\]
\[\ce{C6H5CONH2 + Br2 + 4KOH -> C6H5NH2 + K2CO3 + 2KBr + 2H2O}\]""",
          topic=NIT,
          recall=r"""<ul><li>Hofmann bromamide: RCONH₂ + Br₂ + 4KOH → RNH₂ — one carbon fewer.</li>
<li>Aldehyde → acid with \(\ce{KMnO4}\) / \(\ce{K2Cr2O7}\) / Tollens'.</li></ul>"""),
        Q("9(b)(ii)", 3, r"""<p>(ii) Acetic acid to formic acid.</p>""",
          a=r"""<p>Step down by one carbon via methane (soda-lime decarboxylation):</p>
\[\ce{CH3COOH + NaOH -> CH3COONa + H2O}\]
\[\ce{CH3COONa + NaOH ->[CaO][\Delta] CH4 + Na2CO3}\]
\[\ce{CH4 + Cl2 ->[h\nu] CH3Cl + HCl}\]
\[\ce{CH3Cl + KOH(aq) -> CH3OH + KCl}\]
\[\ce{CH3OH ->[K2Cr2O7/H+] HCHO ->[\text{oxidation}] HCOOH}\]
<p>(Alternative: \(\ce{CH3COOH -> CH3CONH2 ->[Br2/KOH] CH3NH2 ->[HNO2] CH3OH ->[\text{oxidation}] HCHO -> HCOOH}\).)</p>""",
          topic=CARB,
          recall=r"""<ul><li>Decarboxylation with soda lime: \(\ce{RCOONa -> RH}\) (one C fewer).</li>
<li>1° alcohol → aldehyde → acid on oxidation.</li><li>Hofmann bromamide also removes one carbon.</li></ul>"""),
        Q("9(c)", 2, r"""<p>Methyl magnesium iodide is treated with \(\ce{CO2}\) and the product is hydrolysed in acidic medium. Write
balanced equation for the reaction.</p>""",
          a=r"""\[\ce{CH3MgI + CO2 ->[dry ether] CH3COOMgI}\]
\[\ce{CH3COOMgI + H2O ->[H+] CH3COOH + Mg(OH)I}\]
<p><span class="box">Product: ethanoic (acetic) acid</span></p>""",
          topic=CARB,
          recall=r"""<ul><li>RMgX + \(\ce{CO2}\) (dry ice), then \(\ce{H3O+}\) → RCOOH (one carbon more).</li></ul>"""),
        # ------------------------------------------------------------------ Q10
        Q("10(a)", 4, r"""<p>An organic compound A has molecular formula \(\ce{C7H6O}\). When A is treated with NaOH followed by acid
hydrolysis, it gives two products B and C. When B is oxidized it gives A. When A and C are each treated with
\(\ce{PCl5}\) separately, they give two different products D and E.</p>
<p>(i) Identify A, B, C, D and E (ii) Give the chemical reaction when A is treated with NaOH and name the reaction.</p>""",
          a=r"""<p class="step">\(\ce{C7H6O}\) that reacts with alkali to give two products and has no α-H ⇒ A is <b>benzaldehyde</b>; with
conc. NaOH it undergoes the Cannizzaro reaction.</p>
<div class="tbl"><table><tr><th></th><th>Compound</th><th>Formula</th></tr>
<tr><td>A</td><td>benzaldehyde</td><td>\(\ce{C6H5CHO}\)</td></tr>
<tr><td>B</td><td>benzyl alcohol</td><td>\(\ce{C6H5CH2OH}\)</td></tr>
<tr><td>C</td><td>benzoic acid</td><td>\(\ce{C6H5COOH}\)</td></tr>
<tr><td>D</td><td>benzal chloride (dichloromethylbenzene)</td><td>\(\ce{C6H5CHCl2}\)</td></tr>
<tr><td>E</td><td>benzoyl chloride</td><td>\(\ce{C6H5COCl}\)</td></tr></table></div>
<p class="step"><b>(ii) Cannizzaro reaction:</b></p>
\[\ce{2C6H5CHO + NaOH(conc) -> C6H5CH2OH + C6H5COONa}\]
\[\ce{C6H5COONa + HCl -> C6H5COOH + NaCl}\]
<p class="step">Other reactions: \(\ce{C6H5CH2OH ->[\text{mild oxidation}] C6H5CHO}\);
\(\ce{C6H5CHO + PCl5 -> C6H5CHCl2 + POCl3}\); \(\ce{C6H5COOH + PCl5 -> C6H5COCl + POCl3 + HCl}\).</p>
{{fig:0}}""",
          afig=[(F.fig_q10a_scheme, "A = benzaldehyde and its products B–E.")],
          topic=CARB,
          recall=r"""<ul><li>Cannizzaro: aldehyde without α-H + conc. alkali → alcohol + carboxylate (disproportionation).</li>
<li>\(\ce{PCl5}\): &gt;C=O of aldehydes → &gt;CCl₂; –COOH → –COCl.</li></ul>"""),
        Q("10(b)", 2, r"""<p>What are polyamides? Name the monomers of Nylon-66.</p>""", excluded=POLY),
        Q("10(c)", 2, r"""<p>(i) Name the functional group common to both glucose and fructose.</p>
<p>(ii) Deficiency of what vitamins will cause the following diseases 1. Night blindness 2. Scurvy</p>""",
          a=r"""<p class="step">(i) Both are polyhydroxy carbonyl compounds: the common groups are the <b>carbonyl group</b> (\(\ce{&gt;C=O}\) —
aldehydic in glucose, ketonic in fructose) and <b>alcoholic hydroxyl groups</b> (–OH; five in each).</p>
<p class="step">(ii) 1. Night blindness — <b>vitamin A</b>; 2. Scurvy — <b>vitamin C</b>.</p>""",
          topic=BIO,
          recall=r"""<ul><li>Glucose: \(\ce{CH2OH(CHOH)4CHO}\) (aldohexose); fructose: \(\ce{CH2OH(CHOH)3COCH2OH}\) (ketohexose).</li>
<li>Vitamin A — night blindness; C — scurvy.</li></ul>"""),
        Q("10(d)(i)", 1, r"""<p>Give balanced equations for the following [2 marks for (i) and (ii) together]</p><p>(i) Urea is heated</p>""",
          excluded="Urea (carbamide) — not in the ISC 2027 'Organic Compounds containing Nitrogen' unit, which covers amines, cyanides, isocyanides and diazonium salts."),
        Q("10(d)(ii)", 1, r"""<p>Give balanced equations for the following:</p><p>(ii) Chlorine is passed through diethyl ether</p>""",
          a=r"""<p>In the dark, substitution occurs at the α-carbon; in light with excess chlorine all hydrogens are replaced:</p>
\[\ce{CH3CH2-O-CH2CH3 + Cl2 ->[dark] CH3CHCl-O-CH2CH3 + HCl}\]
\[\ce{(C2H5)2O + 10Cl2 ->[h\nu] (C2Cl5)2O + 10HCl}\]
<p>(α-chlorodiethyl ether; perchlorodiethyl ether)</p>""",
          topic=ALC,
          recall=r"""<ul><li>Ethers: halogenation at the α-C (next to O); light + excess \(\ce{Cl2}\) → perchloro ether.</li></ul>"""),
    ])
