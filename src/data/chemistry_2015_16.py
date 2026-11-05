"""Heritage School Pre-Board 2015-16, Chemistry (Class XII) -- transcribed from the page images."""
from kit import Q, SEC
import chemistry_2015_16_figs as fg

FILL = (r"<p><b>Fill in the blanks with appropriate words given below:</b> [Number, nature, lime, "
        r"monohydric, unity, trihydric, decreases, does not change, dihydric, zero, sweets, four, "
        r"primary amine, methyl cyanide, nitric acid, nitrous acid, solutions, slow, overall, order, "
        r"molecularity]</p>")
MATCH = (r"<p><b>Match the following:</b></p><table class='tbl'><tr><th colspan='2'>A</th>"
         r"<th colspan='2'>B</th></tr>"
         r"<tr><td>i)</td><td>Werner's theory</td><td>a)</td><td>Isoelectric point</td></tr>"
         r"<tr><td>ii)</td><td>Wohler's synthesis</td><td>b)</td><td>Formal dehyde</td></tr>"
         r"<tr><td>iii)</td><td>Urotropine</td><td>c)</td><td>Amine</td></tr>"
         r"<tr><td>iv)</td><td>Amino acid</td><td>d)</td><td>Coordination compound</td></tr>"
         r"<tr><td>v)</td><td>Hinsberg's reagent</td><td>e)</td><td>Urea</td></tr></table>")
BRIEF = r"<p><b>Another [<i>sic</i>: Answer] the following in brief:</b></p>"
MCQ = r"<p><b>Choose the correct answer from the alternatives given:</b></p>"

PAPER = dict(
    subject="chemistry",
    year="2015-16",
    slug="2015-16",
    paper="Chemistry (Theory)",
    source="PreBoard-PYQ/2015-16/Chemistry.pdf",
    marks=70, time="3 hours",
    intro=r"""<p>(Candidates are allowed additional 15 minutes for only reading the paper. They must NOT
start writing during this time.)</p>
<p>Answer all questions in <b>Part I</b> and six from <b>Part II</b>.</p>
<p>All working, including rough work, should be done on the same sheet as and adjacent to, the rest of
the answer.</p>
<p>The intended marks for questions or parts of questions are given in brackets [ ].</p>
<p>Balanced equations must be given wherever possible and diagrams where they are helpful.</p>
<p>When solving numerical problems, all essential working must be shown. In working out problems, use
the following data: Gas constant R = 1.987 cal deg<sup>&minus;1</sup> mol<sup>&minus;1</sup> = 0.0821
dm<sup>3</sup> atm K<sup>&minus;1</sup> mol<sup>&minus;1</sup>. 1 L atm = 1 dm<sup>3</sup> atm.</p>""",
    items=[
        SEC("Part I", "(Answer all questions)"),
        # ------------------------------------------------------------ 1(a)
        Q("1(a)(i)", 1, FILL + r"<p>i) When a ________ is treated with ________ nitrogen gas is evolved.</p>",
          a=r"""<p>When a <b>primary amine</b> (aliphatic) is treated with <b>nitrous acid</b>, nitrogen gas is
evolved.</p>
<p>\(\ce{CH3CH2NH2 + HNO2 ->[NaNO2/HCl][273-278 K] CH3CH2OH + N2 ^ + H2O}\)</p>
<p><span class="box">primary amine; nitrous acid</span></p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>\(\ce{HNO2}\) is made in situ from \(\ce{NaNO2 + HCl}\).</li>
<li>Aliphatic 1&deg; amine + \(\ce{HNO2}\) &rarr; alcohol + \(\ce{N2}\) (brisk effervescence);
aniline at 273&ndash;278 K gives a diazonium salt instead.</li></ul>"""),
        Q("1(a)(ii)", 1, FILL + r"<p>ii) A reaction at equilibrium in which significant quantities of both "
          r"products and reactants are present has an equilibrium constant with value near ________.</p>",
          excluded="Chemical equilibrium (magnitude of K) &mdash; a Class XI topic; not in the ISC 2027 Class XII unit list."),
        Q("1(a)(iii)", 1, FILL + r"<p>iii) ________ of a reaction is sum of number of molecules of reactant "
          r"taking part in ________ step of the reaction.</p>",
          a=r"""<p><b>Molecularity</b> of a reaction is the sum of the number of molecules of reactants taking
part in the <b>slow</b> (rate-determining) step of the reaction.</p>
<p><span class="box">Molecularity; slow</span></p>
<p>For an elementary reaction molecularity is the number of reacting species in that single step; for a
complex reaction it is defined for the slowest step, which governs the rate.</p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>Molecularity: theoretical, always a whole number (1, 2, rarely 3), never zero.</li>
<li>Order: experimental, sum of powers in the rate law; may be zero or fractional.</li></ul>"""),
        Q("1(a)(iv)", 1, FILL + r"<p>iv) Glycerol is a ________ alchohol used in making ________.</p>",
          a=r"""<p>Glycerol is a <b>trihydric</b> alcohol used in making <b>sweets</b>.</p>
<p>Glycerol, \(\ce{CH2OH-CHOH-CH2OH}\) (propane-1,2,3-triol), has three &ndash;OH groups. It is sweet,
non-toxic and hygroscopic, so it is used in confectionery (sweets) and as a sweetening and moistening
agent; it is also used for nitroglycerine, cosmetics and inks.</p>
<p><span class="box">trihydric; sweets</span></p>""",
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Mono-, di-, tri-hydric = one, two, three &ndash;OH groups (ethanol, ethylene glycol,
glycerol).</li></ul>"""),
        Q("1(a)(v)", 1, FILL + r"<p>v) Properties of ________ which depend upon ________ of solute particles "
          r"are called colligative properties.</p>",
          a=r"""<p>Properties of <b>solutions</b> which depend upon the <b>number</b> of solute particles (and not on
their nature) are called colligative properties.</p>
<p><span class="box">solutions; number</span></p>""",
          topic="Solutions",
          recall=r"""<ul><li>The four colligative properties: relative lowering of vapour pressure, elevation of
boiling point, depression of freezing point, osmotic pressure.</li></ul>"""),
        # ------------------------------------------------------------ 1(b)
        Q("1(b)(i)", 1, MATCH + r"<p>Match (i) Werner's theory.</p>",
          a=r"""<p>(i) Werner's theory &rarr; <b>(d) Coordination compound</b>.</p>
<p>Werner's theory (1893) explained the bonding in coordination compounds through primary (ionisable)
and secondary (non-ionisable, directional) valencies.</p>
<p><span class="box">(i) &ndash; (d)</span></p>""",
          topic="Coordination Compounds",
          recall=r"""<ul><li>Primary valency = oxidation state (satisfied by anions); secondary valency =
coordination number (satisfied by ligands, fixed geometry).</li></ul>"""),
        Q("1(b)(ii)", 1, MATCH + r"<p>Match (ii) Wohler's synthesis.</p>",
          excluded="Wöhler's synthesis of urea (history of organic chemistry) &mdash; not in the ISC 2027 Class XII syllabus."),
        Q("1(b)(iii)", 1, MATCH + r"<p>Match (iii) Urotropine.</p>",
          a=r"""<p>(iii) Urotropine &rarr; <b>(b) Formaldehyde</b>.</p>
<p>Formaldehyde condenses with ammonia to give urotropine (hexamethylenetetramine):</p>
<p>\(\ce{6HCHO + 4NH3 -> (CH2)6N4 + 6H2O}\)</p>
<p><span class="box">(iii) &ndash; (b)</span></p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Reaction with ammonia distinguishes HCHO (urotropine) from \(\ce{CH3CHO}\)
(acetaldehyde ammonia, an addition product).</li></ul>"""),
        Q("1(b)(iv)", 1, MATCH + r"<p>Match (iv) Amino acid.</p>",
          a=r"""<p>(iv) Amino acid &rarr; <b>(a) Isoelectric point</b>.</p>
<p>The isoelectric point is the pH at which an amino acid exists as the neutral zwitter ion and does not
migrate in an electric field.</p>
<p><span class="box">(iv) &ndash; (a)</span></p>""",
          topic="Biomolecules",
          recall=r"""<ul><li>Zwitter ion \(\ce{H3N+-CHR-COO-}\); at the isoelectric point net charge is zero.</li></ul>"""),
        Q("1(b)(v)", 1, MATCH + r"<p>Match (v) Hinsberg's reagent.</p>",
          a=r"""<p>(v) Hinsberg's reagent &rarr; <b>(c) Amine</b>.</p>
<p>Benzenesulphonyl chloride, \(\ce{C6H5SO2Cl}\), distinguishes primary, secondary and tertiary amines.</p>
<p><span class="box">(v) &ndash; (c)</span></p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>1&deg; amine: sulphonamide soluble in KOH; 2&deg;: sulphonamide insoluble in KOH;
3&deg;: no reaction.</li></ul>"""),
        # ------------------------------------------------------------ 1(c)
        Q("1(c)(i)", 1, BRIEF + r"<p>(i) What is the PH of a solution whose hydroxyl ion concentration is "
          r"10<sup>&minus;2</sup> M?</p>",
          excluded="pH from [OH⁻] and the ionic product of water (ionic equilibrium) &mdash; Class XI; the ISC 2027 Class XII syllabus has pH only as a pH-paper practical, with no calculation."),
        Q("1(c)(ii)", 1, BRIEF + r"<p>(ii) Ethanol gives positive iodoform test &ndash; why?</p>",
          a=r"""<p>Iodine in NaOH (sodium hypoiodite) first <b>oxidises ethanol to acetaldehyde</b>, which contains
the \(\ce{CH3CO\bond{-}}\) group; this is then tri-iodinated and cleaved, giving yellow iodoform.</p>
<p>\(\ce{CH3CH2OH + I2 + 2NaOH -> CH3CHO + 2NaI + 2H2O}\)</p>
<p>\(\ce{CH3CHO + 3I2 + 4NaOH -> CHI3 v + HCOONa + 3NaI + 3H2O}\)</p>
<p><span class="box">Ethanol has the \(\ce{CH3CH(OH)\bond{-}}\) group, which is oxidised to \(\ce{CH3CO\bond{-}}\)</span></p>""",
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Iodoform test is given by \(\ce{CH3CO\bond{-}}\) compounds and by alcohols with
\(\ce{CH3CH(OH)\bond{-}}\) (ethanol, propan-2-ol), never by methanol.</li>
<li>Iodoform: yellow solid with an antiseptic smell.</li></ul>"""),
        Q("1(c)(iii)", 1, BRIEF + r"<p>(iii) Give equations for the preparation of acetic acid using Grignard "
          r"reagent.</p>",
          a=r"""<p>Methylmagnesium bromide is added to dry ice (solid \(\ce{CO2}\)) in dry ether and the adduct is
hydrolysed with dilute acid:</p>
<p>\(\ce{CH3MgBr + CO2 ->[dry ether] CH3COOMgBr}\)</p>
<p>\(\ce{CH3COOMgBr + H2O ->[H+] CH3COOH + Mg(OH)Br}\)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>RMgX + \(\ce{CO2}\) &rarr; RCOOH with one carbon more than RX.</li>
<li>Grignard reactions need dry ether; water destroys RMgX.</li></ul>"""),
        Q("1(c)(iv)", 1, BRIEF + r"<p>(iv) What are the conditions for an effective collision?</p>",
          a=r"""<p>A collision is effective (leads to reaction) only if</p>
<ol><li>the colliding molecules possess energy equal to or greater than the <b>threshold energy</b>
(i.e. kinetic energy at least equal to the activation energy), and</li>
<li>they collide with the <b>proper orientation</b>, so that the bonds to be broken and formed are
suitably placed.</li></ol>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>Rate = \(Z_{AB}\,e^{-E_a/RT}\times P\) (collision frequency &times; energy factor &times;
orientation/steric factor) &mdash; qualitative idea only.</li></ul>"""),
        Q("1(c)(v)", 1, BRIEF + r"<p>(v) For a given cell, cell constant is 0.5 cm<sup>&minus;1</sup> and "
          r"resistance of solution is 384 ohm at 25&deg;C. Calculate specific conductance.</p>",
          a=r"""<p>\[\kappa = \frac{\text{cell constant}}{R} = \frac{0.5\ \text{cm}^{-1}}{384\ \Omega}
= 1.30\times10^{-3}\ \Omega^{-1}\,\text{cm}^{-1}\]</p>
<p><span class="box">\(\kappa = 1.30\times10^{-3}\ \text{S cm}^{-1}\)</span></p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>\(\kappa = \dfrac{1}{R}\cdot\dfrac{l}{A}\); cell constant \(G^* = l/A\) (cm\(^{-1}\)).</li>
<li>1 S = 1 &Omega;\(^{-1}\).</li></ul>"""),
        # ------------------------------------------------------------ 1(d)
        Q("1(d)(i)", 1, MCQ + r"""<p>(i) When 96500 c of electricity is passed through barium chloride solution,
the amount of barium deposited will be:</p><p>(a) 0.5 mol &nbsp; (b) 1 mol &nbsp; (c) 1.5 mol &nbsp; (d) 2 mol</p>""",
          a=r"""<p>\(\ce{Ba^2+ + 2e- -> Ba}\): 2 F (2 &times; 96500 C) deposit 1 mol Ba, so 96500 C = 1 F deposits
\(\tfrac12\) mol.</p>
<p><span class="box">(a) 0.5 mol</span></p>
<p class="note">The question intends Faraday's law. In an <i>aqueous</i> solution barium is not actually
deposited (hydrogen is evolved at the cathode); barium is obtained from molten \(\ce{BaCl2}\).</p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>Moles deposited = \(Q/(zF)\), z = charge on the ion.</li></ul>"""),
        Q("1(d)(ii)", 1, MCQ + r"""<p>(ii) Of the following compounds, the one which is a Lewis acid is:</p>
<p>(a) PCl<sub>3</sub> &nbsp; (b) AlCl<sub>3</sub> &nbsp; (c) NCl<sub>3</sub> &nbsp; (d) AsCl<sub>3</sub></p>""",
          excluded="Lewis acids and bases (ionic equilibrium / acid–base theories) &mdash; Class XI; not in the ISC 2027 Class XII syllabus."),
        Q("1(d)(iii)", 1, MCQ + r"""<p>(iii) Among the following compounds, the one showing geometric isomerism is:</p>
<p>(a) [Cu(NH<sub>3</sub>)<sub>4</sub>]<sup>2+</sup> &nbsp; (b) [Pt(NH<sub>3</sub>)<sub>2</sub>Cl<sub>2</sub>]
&nbsp; (c) [FeNO(CN)<sub>5</sub>]<sup>3&minus;</sup> &nbsp; (d) [CO(en)3]<sup>3+</sup></p>
<p class="note">[(d) is printed "[CO (en)3]"; read as [Co(en)<sub>3</sub>]<sup>3+</sup>.]</p>""",
          a=r"""<p>Square planar \(\ce{[Pt(NH3)2Cl2]}\) (type \(\ce{MA2B2}\)) exists as cis and trans isomers.
{{fig:0}}
(a) \(\ce{MA4}\) and (c) \(\ce{MA5B}\) have only one arrangement; (d) \(\ce{[Co(en)3]^3+}\) shows only optical
isomerism.</p>
<p><span class="box">(b) [Pt(NH<sub>3</sub>)<sub>2</sub>Cl<sub>2</sub>]</span></p>""",
          afig=[fg.fig_pt_cis_trans],
          topic="Coordination Compounds",
          recall=r"""<ul><li>Geometrical isomerism: square planar \(\ce{MA2B2}\), \(\ce{MA2BC}\); octahedral
\(\ce{MA4B2}\), \(\ce{MA3B3}\), \(\ce{M(AA)2B2}\).</li>
<li>Tetrahedral complexes never show geometrical isomerism.</li></ul>"""),
        Q("1(d)(iv)", 1, MCQ + r"""<p>(iv) It is not affected by temperature:</p>
<p>(a) Normality &nbsp; (b) Molarity &nbsp; (c) Molality &nbsp; (d) Formality</p>""",
          a=r"""<p>Molality = moles of solute per kg of <i>solvent</i>: it involves only masses, which do not change
with temperature. Normality, molarity and formality are per litre of solution, and volume changes with
temperature.</p>
<p><span class="box">(c) Molality</span></p>""",
          topic="Solutions",
          recall=r"""<ul><li>Mass-based units (molality, mole fraction, mass %, ppm by mass) are temperature
independent.</li></ul>"""),
        Q("1(d)(vi)", 1, MCQ + r"""<p>(vi) Dehydration of amide with P<sub>2</sub>O<sub>5</sub> yields:</p>
<p>(a) NH<sub>3</sub> &nbsp; (b) RCN &nbsp; (c) RNC &nbsp; (d) RNH<sub>2</sub></p>
<p class="note">[The paper numbers this sub-part (vi); there is no sub-part (v).]</p>""",
          a=r"""<p>\(\ce{RCONH2 ->[P2O5][\Delta] RC#N + H2O}\) &mdash; an alkyl cyanide (nitrile) is formed.</p>
<p><span class="box">(b) RCN</span></p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Cyanides are prepared from alkyl halides (KCN) and from amides (\(\ce{P2O5}\)).</li>
<li>Isocyanides RNC: from RX + AgCN, or the carbylamine reaction.</li></ul>"""),
        # ============================================================ PART II
        SEC("Part II", "Answer six questions choosing two from Section-A, two from Section-B and two from Section-C"),
        SEC("Section A", "(Answer any two questions)"),
        Q("2(a)(i)", 2, r"<p>9.65C of electicity is required to deposit all the aluminium from 100 ml of "
          r"solution of aluminium nitrate. What is the normality of the solution?</p>",
          a=r"""<p>By Faraday's laws, 1 F (96500 C) deposits 1 gram-equivalent of any substance.</p>
<p>\[\text{g-equivalents of Al}^{3+} = \frac{Q}{F} = \frac{9.65}{96500} = 1.0\times10^{-4}\]</p>
<p>These are present in 100 mL = 0.100 L of solution:</p>
<p>\[N = \frac{\text{g-equivalents}}{\text{volume in L}} = \frac{1.0\times10^{-4}}{0.100} = 1.0\times10^{-3}\ \text{N}\]</p>
<p><span class="box">Normality = 1.0 &times; 10<sup>&minus;3</sup> N</span> (molarity = N/3 = 3.33 &times; 10<sup>&minus;4</sup> M)</p>
<p class="note">As in 1(d)(i), aluminium is not really deposited from aqueous solution; the data are meant
for Faraday's law.</p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>Faraday's 1st law \(m = ZQ\); 1 F = 96500 C deposits 1 g-equivalent.</li>
<li>Normality = g-equivalents per litre; for \(\ce{Al^3+}\), N = 3 &times; M.</li></ul>"""),
        Q("2(a)(ii)", 1, r"<p>1M acetic acid has higher PH than 1M nitric acid. Explain.</p>",
          a=r"""<p>Nitric acid is a strong acid and is almost completely ionised, so in 1 M \(\ce{HNO3}\),
[H<sup>+</sup>] &asymp; 1 M (pH &asymp; 0). Acetic acid is a weak acid, only slightly ionised
(\(\ce{CH3COOH <=> CH3COO- + H+}\), about 0.4% at 1 M), so [H<sup>+</sup>] is far smaller and its pH is
higher (&asymp; 2.4).</p>
<p><span class="box">Lower [H<sup>+</sup>] from the weak, partly ionised acid &rArr; higher pH</span></p>""",
          topic="Practical: experiments related to pH change",
          recall=r"""<ul><li>pH = &minus;log[H<sup>+</sup>]: the lower [H<sup>+</sup>], the higher the pH.</li>
<li>2027 practical: compare the pH of strong and weak acids of the same concentration with pH paper /
universal indicator.</li></ul>"""),
        Q("2(a)(iii)", 1, r"<p>What are Lewis acid?</p>",
          excluded="Lewis acid–base concept (ionic equilibrium) &mdash; Class XI; not in the ISC 2027 Class XII syllabus."),
        Q("2(b)", 3, r"<p>A current of 4 amp is passed through a molten solution for 45 mins. 2.977 gm of metal "
          r"is deposited. Calculate the charge carried by the metal cation if its atomic mass is 106.4 gm.</p>",
          a=r"""<p>Quantity of electricity: \(Q = It = 4\ \text{A} \times 45\times60\ \text{s} = 10800\ \text{C}\)</p>
<p>Moles of electrons: \(\dfrac{10800}{96500} = 0.1119\ \text{mol}\)</p>
<p>Moles of metal deposited: \(\dfrac{2.977}{106.4} = 0.02798\ \text{mol}\)</p>
<p>For \(\ce{M^{z+} + z e- -> M}\): \[z = \frac{\text{mol } e^-}{\text{mol M}} = \frac{0.1119}{0.02798} = 4.0\]</p>
<p><span class="box">The cation carries a charge of +4 (M<sup>4+</sup>)</span></p>
<p>(Atomic mass 106.4 is palladium, so the ion is \(\ce{Pd^4+}\).)</p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>\(Q = It\) (t in seconds).</li>
<li>\(m = \dfrac{M\,I\,t}{zF}\) &rArr; \(z = \dfrac{M\,I\,t}{mF}\).</li></ul>"""),
        Q("2(c)", 2, r"<p>State and explain the law of mass action.</p>",
          a=r"""<p><b>Law of mass action</b> (Guldberg and Waage): at constant temperature, the rate of a chemical
reaction is directly proportional to the product of the active masses of the reacting substances, each
raised to a power equal to its stoichiometric coefficient in the balanced equation.</p>
<p><b>Active mass</b> = molar concentration, mol L<sup>&minus;1</sup> (shown by [ ]); for a pure solid or
liquid it is constant and taken as unity.</p>
<p>For \(\ce{aA + bB -> products}\): \[\text{rate} \propto [A]^a[B]^b \quad\Rightarrow\quad \text{rate} = k[A]^a[B]^b\]</p>
<p>where k is the rate constant (rate when every concentration is 1 mol L<sup>&minus;1</sup>).</p>
<p>Example: \(\ce{H2(g) + I2(g) -> 2HI(g)}\), rate = k[H<sub>2</sub>][I<sub>2</sub>].</p>
<p>It holds exactly for an elementary step; for a complex reaction the actual rate law (order) must be
found experimentally.</p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>Active mass = molar concentration.</li>
<li>Rate law: rate = k[A]<sup>m</sup>[B]<sup>n</sup>; order = m + n (experimental).</li></ul>"""),
        Q("2(d)", 1, r"<p>What is the geometry of sodium ions around chloride ions in sodium chloride crystal?</p>",
          excluded="Solid state (ionic crystal structures) &mdash; removed; not in the ISC 2027 Class XII unit list."),
        # ------------------------------------------------------------ Q3
        Q("3(a)", 2, r"""<p>Find out the value of Kc for the following reaction from the given value of Kp at 500K.</p>
<p>2NOCl(g) &#8652; 2NO(g) + Cl<sub>2</sub>(g); Kp = 1.8 &times; 10<sup>&minus;2</sup></p>""",
          excluded="Chemical equilibrium (K<sub>p</sub>–K<sub>c</sub> relation) &mdash; Class XI; not in the ISC 2027 Class XII syllabus."),
        Q("3(b)", 3, r"""<p>A mixture contains 0.550 gm of camphor and 0.045 gm of an organic solute freezes at
157&deg;C. The solute contains 93.46% of C and 6.54% of H by weight. What is the molecular formula of the
compound?</p><p>(F.P of camphor = 178.4&deg;C K<sub>f</sub> = 37.70)</p>""",
          a=r"""<p><b>Molar mass from the depression of freezing point</b></p>
<p>\(\Delta T_f = 178.4 - 157.0 = 21.4\ \text{K}\)</p>
<p>\[M_2 = \frac{1000\,K_f\,w_2}{w_1\,\Delta T_f} = \frac{1000\times37.70\times0.045}{0.550\times21.4}
= 144\ \text{g mol}^{-1}\]</p>
<p><b>Empirical formula</b></p>
<table class="tbl"><tr><th>Element</th><th>%</th><th>% &divide; at. mass</th><th>ratio</th></tr>
<tr><td>C</td><td>93.46</td><td>93.46/12 = 7.788</td><td>7.788/6.488 = 1.2 &rarr; 6</td></tr>
<tr><td>H</td><td>6.54</td><td>6.54/1.008 = 6.488</td><td>1 &rarr; 5</td></tr></table>
<p>Empirical formula \(\ce{C6H5}\), empirical formula mass = 72 + 5 = 77.</p>
<p>\[n = \frac{M}{77} = \frac{144}{77} = 1.87 \approx 2\]</p>
<p><span class="box">Molecular formula = C<sub>12</sub>H<sub>10</sub></span> (M = 154; biphenyl)</p>
<p class="note">The freezing-point data give 144, about 7% below 154; n must be a whole number, so n = 2.</p>""",
          topic="Solutions",
          recall=r"""<ul><li>\(\Delta T_f = K_f m\); \(M_2 = \dfrac{1000K_f w_2}{w_1\Delta T_f}\) (w in g, K<sub>f</sub> in K kg mol<sup>&minus;1</sup>).</li>
<li>Molecular formula = n &times; empirical formula, n = M / (empirical formula mass).</li>
<li>Camphor has a very large K<sub>f</sub> (Rast's method).</li></ul>"""),
        Q("3(c)", 3, r"<p>What are azeotropic mixtures? Explain their types with examples.</p>",
          a=r"""<p><b>Azeotropes</b> are liquid mixtures which boil at a constant temperature and distil without
any change in composition (the vapour has the same composition as the liquid). They cannot be separated
by fractional distillation.</p>
{{fig:0}}
<p><b>1. Minimum-boiling azeotropes</b> &mdash; formed by solutions showing a large <b>positive</b>
deviation from Raoult's law (A&ndash;B attractions weaker than A&ndash;A and B&ndash;B). The total vapour
pressure passes through a maximum, so the boiling point passes through a minimum; the azeotrope boils
below either component. Example: ethanol (95.6% by mass) + water, b.p. 351 K.</p>
<p><b>2. Maximum-boiling azeotropes</b> &mdash; formed by solutions showing a large <b>negative</b>
deviation (A&ndash;B attractions stronger). The vapour pressure passes through a minimum and the boiling
point through a maximum; the azeotrope boils above either component. Examples: nitric acid (68%) + water,
b.p. 393.5 K; HCl (20.2%) + water, b.p. 383 K.</p>""",
          afig=[(fg.fig_azeotropes, "Boiling point&ndash;composition curves (schematic). At the azeotrope the liquid and vapour curves touch.")],
          topic="Solutions",
          recall=r"""<ul><li>Ideal solution: obeys Raoult's law, \(\Delta H_{mix} = 0\), \(\Delta V_{mix} = 0\).</li>
<li>+ve deviation &rarr; max. vapour pressure &rarr; min. b.p. azeotrope; &minus;ve deviation &rarr; min.
vapour pressure &rarr; max. b.p. azeotrope.</li></ul>"""),
        Q("3(d)", 2, r"<p>A small quantity of sparingly soluble calcium oxalate is suspended in pure water "
          r"dissolves on adding dilute hydrochloric acid to it. Explain why?</p>",
          a=r"""<p>The little calcium oxalate that dissolves is in equilibrium with its ions:</p>
<p>\(\ce{CaC2O4(s) <=> Ca^2+(aq) + C2O4^2-(aq)}\)</p>
<p>Oxalic acid is a weak acid, so the \(\ce{H+}\) ions of HCl combine with the oxalate ions to form
feebly ionised oxalic acid:</p>
<p>\(\ce{C2O4^2- + 2H+ -> H2C2O4}\)</p>
<p>This removes \(\ce{C2O4^2-}\) from the solution, so the ionic product
[\(\ce{Ca^2+}\)][\(\ce{C2O4^2-}\)] falls below the solubility product. The equilibrium shifts to the right
and more solid dissolves until it has all gone:</p>
<p>\(\ce{CaC2O4 + 2HCl -> CaCl2 + H2C2O4}\)</p>
<p>(This is the observation used in salt analysis: the white precipitate of calcium oxalate from the
oxalate test is insoluble in acetic acid, which supplies too few \(\ce{H+}\), but dissolves in dilute HCl
or \(\ce{HNO3}\).)</p>""",
          topic="Practical: qualitative analysis (oxalate)",
          recall=r"""<ul><li>A salt of a weak acid dissolves in a strong acid: the anion is removed as the weak acid.</li>
<li>Precipitation needs ionic product &gt; \(K_{sp}\); dissolution when it falls below.</li>
<li>Oxalate test: \(\ce{CaCl2}\) &rarr; white \(\ce{CaC2O4}\), insoluble in \(\ce{CH3COOH}\), soluble in dil. HCl.</li></ul>"""),
        # ------------------------------------------------------------ Q4
        Q("4(a)", 1, r"<p>What are point defects? Explain</p>",
          excluded="Solid state (point defects in crystals) &mdash; removed; not in the ISC 2027 Class XII unit list."),
        Q("4(b)", 3, r"""<p>Determine the emf of the galvanic cell.</p>
<p>Ag | AgNO<sub>3</sub> (0.001M) || AgNO<sub>3</sub> (0.1M) | Ag. In what direction will electrons travel
in the external circuit when the cell operates, E&deg;<sub>Ag<sup>+</sup>|Ag</sub> = 0.80V</p>""",
          a=r"""<p>This is a <b>concentration cell</b>; both electrodes are \(\ce{Ag+ | Ag}\).</p>
<p>Electrode potentials (Nernst, 298 K, n = 1):</p>
<p>\(E_{\text{right}} = 0.80 + 0.0591\log(0.1) = 0.80 - 0.0591 = 0.7409\ \text{V}\)</p>
<p>\(E_{\text{left}} = 0.80 + 0.0591\log(0.001) = 0.80 - 0.1773 = 0.6227\ \text{V}\)</p>
<p>\[E_{\text{cell}} = E_{\text{right}} - E_{\text{left}} = 0.0591\log\frac{0.1}{0.001} = 0.0591\times2 = 0.118\ \text{V}\]</p>
<p><span class="box">E<sub>cell</sub> = 0.118 V</span></p>
<p>Since \(E_{\text{cell}} &gt; 0\), the cell works as written: the left electrode (in 0.001 M) is the anode,
\(\ce{Ag -> Ag+ + e-}\); the right electrode (in 0.1 M) is the cathode, \(\ce{Ag+ + e- -> Ag}\).</p>
{{fig:0}}
<p><span class="box">Electrons flow in the external circuit from the Ag electrode in 0.001 M AgNO<sub>3</sub> to the
Ag electrode in 0.1 M AgNO<sub>3</sub> (left &rarr; right)</span></p>""",
          afig=[fg.fig_ag_conc_cell],
          topic="Electrochemistry",
          recall=r"""<ul><li>Nernst: \(E = E^\circ - \dfrac{0.0591}{n}\log\dfrac{1}{[\ce{M^{n+}}]}\) for \(\ce{M^{n+} + ne- -> M}\).</li>
<li>Concentration cell: \(E^\circ_{cell} = 0\); \(E_{cell} = \dfrac{0.0591}{n}\log\dfrac{c_{\text{cathode}}}{c_{\text{anode}}}\).</li>
<li>Electrons leave the anode (oxidation, &minus;) through the wire.</li></ul>"""),
        Q("4(c)", 2, r"""<p>For a chemical reaction A + B &rarr; product, the order is 1 with respect to each of A
and B. find X and Y from the given data.</p>
<table class="tbl"><tr><th>Rate (moles l<sup>&minus;1</sup> sec<sup>&minus;1</sup>)</th><th>[A]</th><th>[B]</th></tr>
<tr><td>0.10</td><td>0.20 M</td><td>0.05 M</td></tr>
<tr><td>0.40</td><td>X</td><td>0.05 M</td></tr>
<tr><td>0.80</td><td>0.40 M</td><td>Y</td></tr></table>""",
          a=r"""<p>Rate law: rate = k[A][B].</p>
<p>From row 1: \(k = \dfrac{0.10}{0.20\times0.05} = 10\ \text{L mol}^{-1}\text{s}^{-1}\)</p>
<p>Row 2: \(0.40 = 10\times X\times0.05 \Rightarrow X = \dfrac{0.40}{0.50} = 0.80\ \text{M}\)</p>
<p>Row 3: \(0.80 = 10\times0.40\times Y \Rightarrow Y = \dfrac{0.80}{4.0} = 0.20\ \text{M}\)</p>
<p><span class="box">X = 0.80 M, Y = 0.20 M</span></p>""",
          topic="Chemical Kinetics",
          recall=r"""<ul><li>Rate = k[A]<sup>m</sup>[B]<sup>n</sup>; for a second-order reaction k has units
L mol<sup>&minus;1</sup> s<sup>&minus;1</sup>.</li>
<li>First order in A: doubling [A] doubles the rate.</li></ul>"""),
        Q("4(d)(i)", 1, r"<p>What happens to the PH of a buffer solution when it is diluted?</p>",
          excluded="Buffer solutions (ionic equilibrium) &mdash; Class XI; not in the ISC 2027 Class XII syllabus."),
        Q("4(d)(ii)", 2, r"<p>Define specific conductance of an electrolytic solution. What is the relationship "
          r"with molar conductance?</p>",
          a=r"""<p><b>Specific conductance (conductivity), &kappa;</b>, is the conductance of a solution of unit
length and unit area of cross-section, i.e. of 1 cm<sup>3</sup> of solution placed between two electrodes
1 cm<sup>2</sup> in area and 1 cm apart. It is the reciprocal of resistivity:</p>
<p>\[\kappa = \frac{1}{\rho} = \frac{1}{R}\cdot\frac{l}{A}\qquad\text{unit: S cm}^{-1}\ (\Omega^{-1}\text{cm}^{-1})\]</p>
<p><b>Molar conductance</b>, \(\Lambda_m\), is the conductance of the volume of solution containing 1 mole of
electrolyte. Relation:</p>
<p>\[\Lambda_m = \kappa\times V = \frac{\kappa\times1000}{M}\]</p>
<p>with \(\kappa\) in S cm<sup>&minus;1</sup>, M the molarity (mol L<sup>&minus;1</sup>) and \(\Lambda_m\) in
S cm<sup>2</sup> mol<sup>&minus;1</sup>.</p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>V = volume (cm<sup>3</sup>) containing 1 mol = 1000/M.</li>
<li>On dilution \(\kappa\) decreases but \(\Lambda_m\) increases.</li></ul>"""),
        Q("4(d)(iii)", 1, r"<p>AgNO<sub>3</sub> solution cannot be stored in a copper vessel. Explain why?</p>",
          a=r"""<p>Copper lies above silver in the electrochemical series
(\(E^\circ_{\ce{Cu^2+/Cu}} = +0.34\) V &lt; \(E^\circ_{\ce{Ag+/Ag}} = +0.80\) V), so copper is the stronger
reducing agent and displaces silver from solution:</p>
<p>\(\ce{Cu(s) + 2Ag+(aq) -> Cu^2+(aq) + 2Ag(s)}\); \(E^\circ_{cell} = 0.80 - 0.34 = +0.46\) V &gt; 0
(spontaneous).</p>
<p>The vessel would dissolve (corrode) and the solution would turn blue.</p>""",
          topic="Electrochemistry",
          recall=r"""<ul><li>A metal with lower (more negative) \(E^\circ\) displaces a metal of higher \(E^\circ\)
from its salt solution.</li>
<li>\(E^\circ_{cell} &gt; 0\) &rArr; \(\Delta G^\circ = -nFE^\circ &lt; 0\), spontaneous.</li></ul>"""),
        # ============================================================ Section B
        SEC("Section B", "(Answer any two questions)"),
        Q("5(a)", 2, r"<p>Write IUPAC names for: (i) K[Ag(CN)<sub>2</sub>] &nbsp; (ii) [Ag(NH<sub>3</sub>)<sub>2</sub>]Cl</p>",
          a=r"""<p>(i) <span class="box">Potassium dicyanidoargentate(I)</span> (older name: potassium dicyanoargentate(I))</p>
<p>(ii) <span class="box">Diamminesilver(I) chloride</span></p>
<p>Ag is +1 in both: in (i) \(x + 2(-1) = -1\); in (ii) \(x + 0 = +1\).</p>""",
          topic="Coordination Compounds",
          recall=r"""<ul><li>Cation named first; ligands in alphabetical order before the metal.</li>
<li>Anionic complex: metal name ends in -ate, Latin root for Ag (argentate).</li>
<li>\(\ce{NH3}\) = ammine, \(\ce{CN-}\) = cyanido.</li></ul>"""),
        Q("5(b)", 1.5, r"<p>Write the structures of optical isomers of the complex ion [Co(en)<sub>2</sub>Cl<sub>2</sub>]<sup>+</sup></p>",
          a=r"""<p>Only the <b>cis</b> isomer is optically active; it exists as a pair of enantiomers (d and l)
which are non-superimposable mirror images:</p>
{{fig:0}}
<p>The trans isomer (the two Cl opposite) has a plane of symmetry and is optically inactive.</p>""",
          afig=[fg.fig_co_en2cl2_optical],
          topic="Coordination Compounds",
          recall=r"""<ul><li>Optical isomers: non-superimposable mirror images, no plane of symmetry.</li>
<li>Octahedral \(\ce{[M(AA)2B2]}\): cis is chiral, trans is not; \(\ce{[M(AA)3]}\) always chiral.</li></ul>"""),
        Q("5(c)", 1.5, r"<p>Explain the geometry, magnetic nature and hybridization of central metal atom in "
          r"[Fe(CN)<sub>6</sub>]<sup>3&minus;</sup> using VBT</p>",
          a=r"""<p>Oxidation state of Fe: \(x + 6(-1) = -3 \Rightarrow x = +3\); \(\ce{Fe^3+}\) is 3d<sup>5</sup>.</p>
<p>\(\ce{CN-}\) is a strong-field ligand, so the 3d electrons are forced to pair, leaving two 3d orbitals
empty. These combine with the 4s and three 4p orbitals:</p>
{{fig:0}}
<p><span class="box">d<sup>2</sup>sp<sup>3</sup> (inner-orbital, low-spin); octahedral; one unpaired electron &rArr;
paramagnetic (&mu; &asymp; 1.73 BM)</span></p>""",
          afig=[fg.fig_fecn6_vbt],
          topic="Coordination Compounds",
          recall=r"""<ul><li>d<sup>2</sup>sp<sup>3</sup> / sp<sup>3</sup>d<sup>2</sup> &rarr; octahedral; dsp<sup>2</sup> &rarr; square
planar; sp<sup>3</sup> &rarr; tetrahedral.</li>
<li>Spin-only \(\mu = \sqrt{n(n+2)}\) BM.</li></ul>"""),
        Q("6(a)", 1, r"<p>State the common oxidation state of (i) Lanthanides (ii) Actinides.</p>",
          a=r"""<p>(i) Lanthanides: <span class="box">+3</span> (a few also show +2, e.g. Eu<sup>2+</sup>, and +4, e.g. Ce<sup>4+</sup>).</p>
<p>(ii) Actinides: <span class="box">+3</span> is common, but they show a wider range, +3 to +7 (e.g. U +6, Np and Pu up to +7),
because the 5f, 6d and 7s levels are close in energy.</p>""",
          topic="d- and f-Block Elements",
          recall=r"""<ul><li>Lanthanoids: 4f series, mainly +3. Actinoids: 5f series, variable states.</li></ul>"""),
        Q("6(b)", 2, r"<p>In a given transition series, there is no significant change in the atomic radii of "
          r"elements with increase in atomic number. Explain.</p>",
          a=r"""<ul><li>Along a transition series the nuclear charge increases by one unit at each step, and the extra
electron enters the inner <b>(n&minus;1)d</b> subshell, not the outer ns shell.</li>
<li>The d electrons <b>shield</b> the outer ns electrons from the increasing nuclear charge. The increase in
nuclear attraction is therefore nearly cancelled by the increased screening, and the effective nuclear charge
felt by the outer electrons changes very little.</li>
<li>Hence the atomic radii stay almost constant in the middle of the series (after a small initial decrease);
towards the end they rise slightly because of repulsion between the paired d electrons.</li></ul>""",
          topic="d- and f-Block Elements",
          recall=r"""<ul><li>Effective nuclear charge = Z &minus; screening.</li>
<li>Electron enters (n&minus;1)d: poor change in Z<sub>eff</sub> for ns electrons.</li></ul>"""),
        Q("6(c)(i)", 1, r"<p>To which class of compounds does IF<sub>7</sub> belongs.</p>",
          excluded="Interhalogen compounds (p-block, group 17) &mdash; not in the ISC 2027 Class XII syllabus."),
        Q("6(c)(ii)", 1, r"<p>Give a balanced chemical equation for the preparation of silver nitrate in the laboratory.</p>",
          excluded="Preparation of silver nitrate (compounds of silver) &mdash; not in the ISC 2027 syllabus, which treats only K<sub>2</sub>Cr<sub>2</sub>O<sub>7</sub> and KMnO<sub>4</sub> among d-block compounds."),
        Q("7(a)(i)", 1, r"<p>Give balanced equations for the following reactions. (i) Ozone and mercury.</p>",
          excluded="Ozone (p-block, group 16) &mdash; not in the ISC 2027 Class XII syllabus."),
        Q("7(a)(ii)", 1, r"<p>Give balanced equations for the following reactions. (ii) Action of hydrogen "
          r"peroxide with acidified ferrous sulphate.</p>",
          excluded="Hydrogen peroxide (chemistry of hydrogen) &mdash; Class XI; not in the ISC 2027 Class XII syllabus."),
        Q("7(a)(iii)", 1, r"<p>Give balanced equations for the following reactions. (iii) Action of potassium "
          r"iodide with acidified potassium permanganate.</p>",
          a=r"""<p>In acid, permanganate is reduced to \(\ce{Mn^2+}\) and iodide is oxidised to iodine:</p>
<p>\(\ce{2KMnO4 + 10KI + 8H2SO4 -> 6K2SO4 + 2MnSO4 + 5I2 + 8H2O}\)</p>
<p>Ionic: \(\ce{2MnO4- + 10I- + 16H+ -> 2Mn^2+ + 5I2 + 8H2O}\)</p>""",
          topic="d- and f-Block Elements",
          recall=r"""<ul><li>Acidic \(\ce{MnO4-}\) (Mn +7 &rarr; +2):<br>\(\ce{MnO4- + 8H+ + 5e-}\)<br>\(\ce{-> Mn^2+ + 4H2O}\)</li>
<li>\(\ce{2I- -> I2 + 2e-}\); balance electrons 2 &times; 5 = 10.</li></ul>"""),
        Q("7(b)", 2, r"<p>What is the hybridisation state of chlorine in ClF<sub>3</sub> molecule? Draw the "
          r"structure and state its geometry.</p>",
          excluded="Interhalogen compounds / VSEPR shape of ClF<sub>3</sub> (p-block) &mdash; not in the ISC 2027 Class XII syllabus."),
        # ============================================================ Section C
        SEC("Section C", "(Answer any two questions)"),
        Q("8(a)(i)", 1, r"<p>How will you perform the following conversions: (i) Nitrobenzene to acetaldanilide</p>"
          r"<p class='note'>[Printed &ldquo;acetaldanilide&rdquo;; read as acetanilide.]</p>",
          a=r"""<p>Reduce nitrobenzene to aniline, then acetylate:</p>
<p>\(\ce{C6H5NO2 + 6[H] ->[Sn/HCl] C6H5NH2 + 2H2O}\)</p>
<p>\(\ce{C6H5NH2 + CH3COCl ->[pyridine] C6H5NHCOCH3 + HCl}\)</p>""",
          topic="Organic Compounds containing Nitrogen",
          recall=r"""<ul><li>Nitrobenzene &rarr; aniline: Sn/HCl or Fe/HCl.</li>
<li>Acetylation (\(\ce{CH3COCl}\) or \(\ce{(CH3CO)2O}\)) replaces an N&ndash;H by N&ndash;COCH<sub>3</sub>.</li></ul>"""),
        Q("8(a)(ii)", 2, r"<p>How will you perform the following conversions: (ii) Acetyl chloride to acetone</p>",
          a=r"""<p>Treat acetyl chloride with dimethylcadmium (prepared from a Grignard reagent and \(\ce{CdCl2}\)):</p>
<p>\(\ce{2CH3MgBr + CdCl2 -> (CH3)2Cd + 2MgBrCl}\)</p>
<p>\(\ce{2CH3COCl + (CH3)2Cd -> 2CH3COCH3 + CdCl2}\)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Acid chloride + dialkylcadmium &rarr; ketone (stops at the ketone, unlike RMgX).</li>
<li>Acid chloride + \(\ce{H2}\)/Pd&ndash;\(\ce{BaSO4}\) &rarr; aldehyde (Rosenmund).</li></ul>"""),
        Q("8(a)(iii)", 1, r"<p>How will you perform the following conversions: (iii) Acetaldehyde to lactic acid</p>",
          a=r"""<p>Add HCN to form the cyanohydrin, then hydrolyse the &ndash;CN group:</p>
<p>\(\ce{CH3CHO + HCN -> CH3CH(OH)CN}\)</p>
<p>\(\ce{CH3CH(OH)CN + 2H2O + HCl -> CH3CH(OH)COOH + NH4Cl}\)</p>
<p>(2-hydroxypropanoic acid = lactic acid)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Nucleophilic addition of \(\ce{CN-}\) to C=O gives a cyanohydrin (one C more).</li>
<li>Acid hydrolysis: \(\ce{-CN -> -COOH}\).</li></ul>"""),
        Q("8(b)", 4, r"""<p>Give balanced equations for the following reactions:</p>
<p>(i) Benzaldehyde and hydroxylamine. (ii) 1-butanol and hydrogen chloride. (iii) Aniline and aqueous
bromine. (iv) Methyl isocyanide and warm dilute hydrochloric acid.</p>""",
          a=r"""<p>(i) Benzaldoxime is formed:</p>
<p>\(\ce{C6H5CHO + NH2OH ->[H+] C6H5CH=NOH + H2O}\)</p>
<p>(ii) 1-Chlorobutane (anhydrous \(\ce{ZnCl2}\), Groves' process):</p>
<p>\(\ce{CH3CH2CH2CH2OH + HCl ->[ZnCl2] CH3CH2CH2CH2Cl + H2O}\)</p>
<p>(iii) White precipitate of 2,4,6-tribromoaniline:</p>
<p>\(\ce{C6H5NH2 + 3Br2 -> C6H2Br3NH2 v + 3HBr}\)</p>
<p>(iv) Methylamine and formic acid (isocyanides are hydrolysed by dilute acid):</p>
<p>\(\ce{CH3NC + 2H2O ->[H+] CH3NH2 + HCOOH}\)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Carbonyl + \(\ce{NH2-Z}\) &rarr; \(\ce{C=N-Z}\) + \(\ce{H2O}\) (oxime, hydrazone&hellip;).</li>
<li>&ndash;NH<sub>2</sub> strongly activates the ring: bromine water substitutes all o/p positions.</li>
<li>RNC + H<sub>2</sub>O (H<sup>+</sup>) &rarr; RNH<sub>2</sub> + HCOOH; RCN &rarr; RCOOH + NH<sub>3</sub>.</li></ul>"""),
        Q("8(c)", 2, r"""<p>(i) Give one example of fibrous and one globular protein each.</p>
<p>(ii) Glycine exists as zwitter ion but o- and p- amino benzoic acids do not, explain.</p>""",
          a=r"""<p>(i) Fibrous: <b>keratin</b> (hair, wool) or myosin; globular: <b>insulin</b> or albumin.</p>
<p>(ii) In glycine the &ndash;NH<sub>2</sub> group is aliphatic and fairly basic, so it accepts the proton of
its own &ndash;COOH group: \(\ce{H2N-CH2-COOH -> H3N+-CH2-COO-}\) (zwitter ion).</p>
<p>In o- and p-aminobenzoic acids the lone pair of N is delocalised into the benzene ring (and further
towards the electron-withdrawing &ndash;COOH group at the o/p position), so the &ndash;NH<sub>2</sub> is only
very weakly basic. It cannot take the proton from &ndash;COOH, so no zwitter ion forms.</p>""",
          topic="Biomolecules",
          recall=r"""<ul><li>Fibrous proteins: long, thread-like, insoluble; globular: folded, water soluble.</li>
<li>Aryl amines are much weaker bases than alkyl amines (lone pair in resonance with the ring).</li></ul>"""),
        Q("9(a)", 2, r"""<p>Identify A to D</p>
<p>\(\ce{A + CCl4 + KOH ->[Heat] [B] ->[Zn-dust] [C] ->[NaOH + CaO] [D]}\)</p>""",
          a=r"""<p>A reacts with \(\ce{CCl4}\)/KOH (Reimer&ndash;Tiemann with \(\ce{CCl4}\)) to give a phenolic acid, so A is
phenol.</p>
<p>\(\ce{C6H5OH + CCl4 + 6KOH -> C6H4(OK)COOK + 4KCl + 4H2O}\); acidification gives salicylic acid.</p>
<p>\(\ce{C6H4(OH)COOH + Zn -> C6H5COOH + ZnO}\) (zinc dust removes the phenolic &ndash;OH)</p>
<p>\(\ce{C6H5COOH + 2NaOH ->[CaO][\Delta] C6H6 + Na2CO3 + H2O}\) (decarboxylation)</p>
<table class="tbl"><tr><td>A</td><td>Phenol, \(\ce{C6H5OH}\)</td></tr>
<tr><td>B</td><td>Salicylic acid (2-hydroxybenzoic acid), \(\ce{o-HOC6H4COOH}\)</td></tr>
<tr><td>C</td><td>Benzoic acid, \(\ce{C6H5COOH}\)</td></tr>
<tr><td>D</td><td>Benzene, \(\ce{C6H6}\)</td></tr></table>""",
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Reimer&ndash;Tiemann: \(\ce{CHCl3}\)/NaOH &rarr; salicylaldehyde; \(\ce{CCl4}\)/NaOH &rarr; salicylic acid.</li>
<li>Zn dust: Ar&ndash;OH &rarr; Ar&ndash;H. Soda lime: RCOOH &rarr; RH (one C less).</li></ul>"""),
        Q("9(b)", 3, r"""<p>Give one chemical test to distinguish between the following pairs:</p>
<p>(i) Acetic acid and benzoic acid. (ii) Glucose and fructose.</p>""",
          a=r"""<p>(i) <b>Neutral ferric chloride test</b> (on the neutralised acid): acetate gives a
<b>deep red colour</b> (red-brown precipitate on boiling); benzoate gives a <b>buff (pale brown)
precipitate</b>.</p>
<p>\(\ce{3CH3COONa + FeCl3 -> (CH3COO)3Fe + 3NaCl}\) (red)</p>
<p>\(\ce{3C6H5COONa + FeCl3 -> (C6H5COO)3Fe v + 3NaCl}\) (buff ppt)</p>
<p>(ii) <b>Bromine water</b>: glucose (an aldose) decolourises it, being oxidised to gluconic acid;
fructose (a ketose) does not.</p>
<p>\(\ce{CH2OH(CHOH)4CHO + Br2 + H2O -> CH2OH(CHOH)4COOH + 2HBr}\)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Neutral \(\ce{FeCl3}\): acetate &rarr; red; benzoate &rarr; buff ppt; formate &rarr; red.</li>
<li>Bromine water is a mild oxidant: oxidises &ndash;CHO only, so distinguishes aldoses from ketoses
(Tollens' and Fehling's do not, since fructose also reduces them in alkali).</li></ul>"""),
        Q("9(c)(i)", 2, r"<p>Explain the esterification reaction with mechanism.</p>",
          a=r"""<p><b>Esterification</b>: a carboxylic acid reacts with an alcohol in the presence of a little
concentrated \(\ce{H2SO4}\) to give an ester and water; the reaction is reversible.</p>
<p>\(\ce{CH3COOH + C2H5OH <=>[conc. H2SO4] CH3COOC2H5 + H2O}\)</p>
<p><b>Mechanism</b> (acid-catalysed nucleophilic acyl substitution):</p>
{{fig:0}}
<ol><li>\(\ce{H+}\) protonates the carbonyl oxygen, making the carbonyl carbon more electrophilic.</li>
<li>The lone pair of the alcohol oxygen attacks this carbon, giving a tetrahedral intermediate.</li>
<li>A proton is transferred to one of the &ndash;OH groups, turning it into \(\ce{-OH2+}\), a good leaving group.</li>
<li>Water is lost and the C=O is re-formed.</li>
<li>Loss of \(\ce{H+}\) gives the ester and regenerates the catalyst.</li></ol>""",
          afig=[fg.fig_ester_mech],
          topic="Alcohols, Phenols and Ethers",
          recall=r"""<ul><li>Conc. \(\ce{H2SO4}\) acts as catalyst and dehydrating agent (shifts the equilibrium right).</li>
<li>Acyl&ndash;oxygen fission: the OH of water comes from the acid.</li></ul>"""),
        Q("9(c)(ii)", 1, r"<p>Acetamide is amphoteric in nature. Give two equations to support this statement.</p>",
          a=r"""<p>As a weak <b>base</b> it forms a salt with a strong acid:</p>
<p>\(\ce{CH3CONH2 + HCl -> CH3CONH3+Cl-}\) (acetamide hydrochloride)</p>
<p>As a weak <b>acid</b> it forms a salt with a metal oxide (or with sodium):</p>
<p>\(\ce{2CH3CONH2 + HgO -> (CH3CONH)2Hg + H2O}\) (mercury acetamide)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>The C=O withdraws the N lone pair, so amides are very weak bases but their N&ndash;H is
weakly acidic.</li></ul>"""),
        Q("9(c)(iii)", 2, r"""<p>At 110<sup>0</sup>C, oxalic acid reacts with an organic compound A with molecular
formula C<sub>3</sub>H<sub>8</sub>O<sub>3</sub> to yield a monocarboxylic acid B. B gives silver mirror with
Tollen's reagent and reduces acidified KMnO<sub>4</sub> solution. Identify A and B also give reaction of B
with acidified KMnO<sub>4</sub> solution.</p>""",
          a=r"""<p>\(\ce{C3H8O3}\) that reacts with oxalic acid at 383 K is <b>glycerol</b>; it forms glyceryl
monoxalate, which loses \(\ce{CO2}\) to give glyceryl monoformate; hydrolysis then releases formic acid
and regenerates glycerol:</p>
<p>\(\ce{C3H5(OH)3 + HOOC-COOH -> C3H5(OH)2OOC-COOH + H2O}\)</p>
<p>\(\ce{C3H5(OH)2OOC-COOH -> C3H5(OH)2OOCH + CO2}\)</p>
<p>\(\ce{C3H5(OH)2OOCH + H2O -> C3H5(OH)3 + HCOOH}\)</p>
<p><span class="box">A = glycerol (propane-1,2,3-triol); B = formic acid (methanoic acid), HCOOH</span></p>
<p>B contains an aldehyde-like H&ndash;C=O, so it reduces Tollens' reagent and is oxidised by acidified
permanganate to \(\ce{CO2}\):</p>
<p>\(\ce{2KMnO4 + 3H2SO4 + 5HCOOH -> K2SO4 + 2MnSO4 + 5CO2 + 8H2O}\)</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>Formic acid is the only carboxylic acid that is also a reducing agent (Tollens' +ve).</li>
<li>Glycerol + oxalic acid at 383 K &rarr; formic acid; at 503 K &rarr; allyl alcohol.</li></ul>"""),
        Q("10(a)", 3, r"""<p>An organic compound A (C<sub>7</sub>H<sub>8</sub>) on oxidation by chromyl chloride in
presence of CCl<sub>4</sub> gives a compound B which gives a positive Tollen's test. The compound B gives two
products, C and D. when treated with NaOH followed by hydrolysis. C on oxidation gives B which on further
oxidation gives D. The compound D on heating with sodalime gives hydrocarbon E. The compound E when treated
with conc. HNO<sub>3</sub>, in the presence of conc. H<sub>2</sub>SO<sub>4</sub> below 60<sup>0</sup>C gives
compound F. Identify A,B,C,D, E and F.</p>""",
          a=r"""<p>\(\ce{C7H8}\) is toluene; chromyl chloride oxidises its &ndash;CH<sub>3</sub> to &ndash;CHO (&Eacute;tard
reaction):</p>
<p>\(\ce{C6H5CH3 + 2[O] ->[CrO2Cl2/CCl4][then H3O+] C6H5CHO + H2O}\) (via the brown &Eacute;tard complex \(\ce{C6H5CH(OCrOHCl2)2}\))</p>
<p>Benzaldehyde has no &alpha;-H, so with conc. NaOH it undergoes the Cannizzaro reaction:</p>
<p>\(\ce{2C6H5CHO + NaOH -> C6H5CH2OH + C6H5COONa}\); \(\ce{C6H5COONa + HCl -> C6H5COOH + NaCl}\)</p>
<p>Benzyl alcohol \(\xrightarrow{[O]}\) benzaldehyde \(\xrightarrow{[O]}\) benzoic acid, as stated.</p>
<p>\(\ce{C6H5COOH + 2NaOH ->[CaO][\Delta] C6H6 + Na2CO3 + H2O}\)</p>
<p>\(\ce{C6H6 + HNO3 ->[conc. H2SO4] C6H5NO2 + H2O}\) (below 333 K)</p>
<table class="tbl"><tr><td>A</td><td>Toluene, \(\ce{C6H5CH3}\)</td><td>B</td><td>Benzaldehyde, \(\ce{C6H5CHO}\)</td></tr>
<tr><td>C</td><td>Benzyl alcohol, \(\ce{C6H5CH2OH}\)</td><td>D</td><td>Benzoic acid, \(\ce{C6H5COOH}\)</td></tr>
<tr><td>E</td><td>Benzene, \(\ce{C6H6}\)</td><td>F</td><td>Nitrobenzene, \(\ce{C6H5NO2}\)</td></tr></table>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>&Eacute;tard reaction: toluene + \(\ce{CrO2Cl2}\) &rarr; benzaldehyde (lab preparation).</li>
<li>Cannizzaro: aldehydes without &alpha;-H disproportionate into alcohol + carboxylate.</li>
<li>Soda-lime decarboxylation; nitration below 60 &deg;C stops at mononitration.</li></ul>"""),
        Q("10(b)", 4, r"""<p>Account for the following giving reasons:</p>
<p>(i) Acetic acid can be halogenated in the presence of red phosphorous and chlorine but formic acid cannot
be halogenated in the same way.</p><p>(ii) Tertiary amines do not undergo acetylation.</p>
<p>(iii) The boiling points of amides are higher than those of corresponding acids.</p>
<p>(iv) Unlike phenols, alcohols are easily protonated.</p>""",
          a=r"""<p>(i) The Hell&ndash;Volhard&ndash;Zelinsky reaction replaces an <b>&alpha;-hydrogen</b>. Acetic acid
has three &alpha;-H atoms: \(\ce{CH3COOH + Cl2 ->[red P] ClCH2COOH + HCl}\). Formic acid, HCOOH, has no
&alpha;-carbon and so no &alpha;-hydrogen.</p>
<p>(ii) Acetylation replaces a hydrogen on nitrogen by \(\ce{CH3CO\bond{-}}\)
(\(\ce{RNH2 + CH3COCl -> RNHCOCH3 + HCl}\)). A tertiary amine \(\ce{R3N}\) has no N&ndash;H, so it cannot be
acetylated.</p>
<p>(iii) Amides have two N&ndash;H bonds and a highly polar C=O (resonance
\(\ce{R-C(=O)-NH2 <-> R-C(-O^-)=NH2+}\)), so they form a more extensive network of intermolecular hydrogen
bonds than acids, which mostly exist as dimers. More energy is needed to separate the molecules (acetamide
b.p. 494 K, acetic acid 391 K).</p>
<p>(iv) In an alcohol the lone pairs on oxygen are localised (and the alkyl group's +I effect increases their
availability), so the oxygen readily accepts \(\ce{H+}\): \(\ce{ROH + H+ -> ROH2+}\). In phenol a lone pair
is delocalised into the benzene ring by resonance; it is less available, and protonation would destroy this
resonance stabilisation.</p>""",
          topic="Aldehydes, Ketones and Carboxylic Acids",
          recall=r"""<ul><li>HVZ needs &alpha;-H; product is the &alpha;-halo acid.</li>
<li>Acylation needs N&ndash;H (1&deg; and 2&deg; amines only).</li>
<li>H-bonding raises b.p.; resonance delocalisation lowers basicity.</li></ul>"""),
        Q("10(c)(i)", 1, r"<p>Deficiency of which vitamin will cause the disease Beri-Beri.</p>",
          a=r"""<p><span class="box">Vitamin B<sub>1</sub> (thiamine)</span> &mdash; a water-soluble vitamin.</p>""",
          topic="Biomolecules",
          recall=r"""<ul><li>A &ndash; night blindness; B<sub>1</sub> &ndash; beri-beri; C &ndash; scurvy; D &ndash; rickets;
E &ndash; sterility/muscle weakness; K &ndash; delayed blood clotting.</li>
<li>Fat soluble: A, D, E, K; water soluble: B, C.</li></ul>"""),
        Q("10(c)(ii)", 1, r"<p>Give one example of polyester and its monomers.</p>",
          excluded="Polymers &mdash; removed; not in the ISC 2027 Class XII unit list (now only a suggested project topic)."),
        Q("10(c)(iii)", 1, r"<p>Draw the open chain and pyranose structure of glucose.</p>",
          a=r"""{{fig:0}}
<p>The open chain has a free &ndash;CHO at C1 and &ndash;OH groups on C2&ndash;C6. In the pyranose form the
C5&ndash;OH has added to the aldehyde group, giving a six-membered ring of five carbons and one oxygen; the
new C1&ndash;OH is &alpha; (down) or &beta; (up).</p>""",
          afig=[fg.fig_glucose_structures],
          topic="Biomolecules",
          recall=r"""<ul><li>Glucose: aldohexose, \(\ce{C6H12O6}\); D-series because C5&ndash;OH is on the right.</li>
<li>Pyranose = six-membered ring (like pyran); &alpha; and &beta; are anomers.</li></ul>"""),
    ])
