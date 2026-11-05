"""JEE Main mock test 3 — Chemistry (Q26–50).  Every item is adapted from a kept pre-board item."""
from jee_kit import MCQ, NUM
import chemistry_figs as JF
from chemistry_2015_16_figs import fig_ag_conc_cell, fig_co_en2cl2_optical
from chemistry_2024_25_s2_figs import fig_b_trans_cocl2en2
from chemistry_2016_17_figs import fig_fecl4_cft

SUBJECT = "chemistry"
TEST = 3

QUESTIONS = [
    # ------------------------------------------------------------------ Solutions
    MCQ(src=("chemistry_2025_26_s2", "20"), topic="Solutions",
        q=r"""<p>6.21 g of a non-volatile solute dissolved in 24.0 g of chloroform raises its boiling
        point from 61.70 °C to 68.04 °C. If \(K_b\) for chloroform is 3.63 K kg mol\(^{-1}\), the molar
        mass of the solute is about</p>""",
        options=[r"\(148\) g mol\(^{-1}\)", r"\(74\) g mol\(^{-1}\)", r"\(296\) g mol\(^{-1}\)",
                 r"\(13.8\) g mol\(^{-1}\)"],
        answer=0,
        sol=r"""<p>\(\Delta T_b = 68.04 - 61.70 = 6.34\) K.
        \[M = \frac{1000\,K_b\,w_B}{\Delta T_b\,w_A} = \frac{1000\times3.63\times6.21}{6.34\times24.0} = 148\ \text{g mol}^{-1}\]</p>
        <p>13.8 uses the boiling point 68.04 in place of the elevation; 74 and 296 are the answer
        halved and doubled.</p>
        <p><b>Answer: (1) 148 g mol\(^{-1}\)</b></p>"""),

    MCQ(src=("chemistry_2025_26_s2", "1(B)(vi)"), topic="Solutions",
        q=r"""<p>For a solution of chloroform and acetone, which shows negative deviation from
        Raoult's law,</p>""",
        options=[r"\(\Delta_\text{mix}H > 0\) and \(\Delta_\text{mix}V > 0\)",
                 r"\(\Delta_\text{mix}H \lt 0\) and \(\Delta_\text{mix}V \lt 0\)",
                 r"\(\Delta_\text{mix}H = 0\) and \(\Delta_\text{mix}V = 0\)",
                 r"\(\Delta_\text{mix}H \lt 0\) and \(\Delta_\text{mix}V > 0\)"],
        answer=1,
        sol=r"""<p>Chloroform's H forms a hydrogen bond with the C=O oxygen of acetone, so A–B
        attraction is stronger than A–A and B–B. Mixing releases heat (\(\Delta_\text{mix}H &lt; 0\))
        and the molecules pack more closely (\(\Delta_\text{mix}V &lt; 0\)); the vapour pressure is
        lower than Raoult's law predicts.</p>
        <p>Both positive is positive deviation (e.g. ethanol + water); both zero is an ideal
        solution; stronger attraction cannot be accompanied by expansion.</p>
        <p><b>Answer: (2)</b></p>"""),

    # ------------------------------------------------------------------ Electrochemistry
    MCQ(src=("chemistry_2015_16", "4(b)"), topic="Electrochemistry",
        q=r"""<p>For the concentration cell
        \(\ce{Ag | AgNO3 (0.001 M) || AgNO3 (0.1 M) | Ag}\) at 298 K, the emf and the direction of
        electron flow in the external circuit are (\(2.303RT/F = 0.059\) V)</p>""",
        options=[r"\(0.059\) V; from the 0.001 M side to the 0.1 M side",
                 r"\(0.118\) V; from the 0.1 M side to the 0.001 M side",
                 r"\(0.118\) V; from the 0.001 M side to the 0.1 M side",
                 r"\(0.236\) V; from the 0.001 M side to the 0.1 M side"],
        answer=2,
        sol=r"""<p>Both electrodes are \(\ce{Ag+/Ag}\), so \(E^\circ_\text{cell} = 0\) and \(n = 1\).
        \[E = \frac{0.059}{1}\log\frac{[\ce{Ag+}]_\text{cathode}}{[\ce{Ag+}]_\text{anode}} = 0.059\log\frac{0.1}{0.001} = 0.118\ \text{V}\]</p>
        <p>The dilute electrode is the anode (Ag dissolves, raising its \(\ce{Ag+}\)); silver deposits
        from the concentrated side. Electrons therefore travel from the 0.001 M electrode to the
        0.1 M electrode.</p>
        {{fig:0}}
        <p>0.059 V takes \(\log 100 = 1\); 0.236 V uses \(n = 1/2\) or squares the ratio; the
        reversed electron flow would make the cell drive the concentrations further apart.</p>
        <p><b>Answer: (3)</b></p>""",
        sfig=fig_ag_conc_cell),

    MCQ(src=("chemistry_2014_15", "4(c)"), topic="Electrochemistry",
        q=r"""<p>A current of 4.0 A passed for 45 min through a molten salt deposits 2.977 g of a metal
        of atomic mass 106.4. The charge on the metal ion is</p>""",
        options=[r"\(+1\)", r"\(+2\)", r"\(+3\)", r"\(+4\)"],
        answer=3,
        sol=r"""<p>\(Q = 4.0\times45\times60 = 10\,800\) C; moles of electrons \(= 10\,800/96\,500 = 0.1119\).
        Moles of metal \(= 2.977/106.4 = 0.02798\).
        \[z = \frac{0.1119}{0.02798} = 4.0\]</p>
        <p><b>Answer: (4) +4</b></p>"""),

    # ------------------------------------------------------------------ Chemical Kinetics
    MCQ(src=("chemistry_2015_16", "4(c)"), topic="Chemical Kinetics",
        q=r"""<p>For \(\ce{A + B -> products}\), first order in each reactant:</p>
        <table class="tbl"><tr><th>rate / mol L\(^{-1}\) s\(^{-1}\)</th><th>[A] / M</th><th>[B] / M</th></tr>
        <tr><td>0.10</td><td>0.20</td><td>0.05</td></tr>
        <tr><td>0.40</td><td>X</td><td>0.05</td></tr>
        <tr><td>0.80</td><td>0.40</td><td>Y</td></tr></table>
        <p>X and Y are</p>""",
        options=[r"X = 0.80 M, Y = 0.20 M", r"X = 0.20 M, Y = 0.80 M",
                 r"X = 0.40 M, Y = 0.10 M", r"X = 1.60 M, Y = 0.40 M"],
        answer=0,
        sol=r"""<p>rate \(= k[A][B]\); row 1: \(k = 0.10/(0.20\times0.05) = 10\) L mol\(^{-1}\) s\(^{-1}\).</p>
        <p>Row 2: \(0.40 = 10\times X\times0.05\Rightarrow X = 0.80\) M.
        Row 3: \(0.80 = 10\times0.40\times Y\Rightarrow Y = 0.20\) M.</p>
        <p>Option (2) swaps the two values; option (3) (X = 0.40 M) would only double the rate in
        row 2; option (4) doubles both correct values, which would give rates of 0.80 and
        1.60 mol L\(^{-1}\) s\(^{-1}\).</p>
        <p><b>Answer: (1)</b></p>"""),

    MCQ(src=("chemistry_2025_26_s2", "17"), topic="Chemical Kinetics",
        q=r"""<p>The rate constant of a reaction is \(3\times10^{-3}\) mol\(^{-2}\) L\(^2\) s\(^{-1}\).
        If the concentration of every reactant is doubled, the rate becomes</p>""",
        options=[r"\(2\) times", r"\(4\) times", r"\(8\) times", r"\(16\) times"],
        answer=2,
        sol=r"""<p>Units of \(k\) are (mol L\(^{-1}\))\(^{1-n}\) s\(^{-1}\). Here
        (mol L\(^{-1}\))\(^{-2}\) s\(^{-1}\) ⇒ \(1 - n = -2\) ⇒ \(n = 3\): third order overall.</p>
        <p>Doubling all concentrations multiplies the rate by \(2^n = 2^3 = 8\).</p>
        <p>2 and 4 are the first- and second-order results; 16 would need \(n = 4\).</p>
        <p><b>Answer: (3) 8 times</b></p>"""),

    # ------------------------------------------------------------------ d- and f-Block
    MCQ(src=("chemistry_2024_25_s2", "1(B)(vii)"), topic="d- and f-Block Elements",
        q=r"""<p><b>Assertion (A):</b> Actinoids form complexes more readily than lanthanoids.<br>
        <b>Reason (R):</b> The 5f orbitals extend further from the nucleus than the 4f orbitals and
        can take part in bonding.</p>""",
        options=[r"Both A and R are true and R is the correct explanation of A",
                 r"Both A and R are true but R is not the correct explanation of A",
                 r"A is true but R is false",
                 r"A is false but R is true"],
        answer=0,
        sol=r"""<p>The 5f orbitals are less deeply buried than the 4f (less shielded by the filled
        outer shells), so actinoid ions can use them, together with 6d, 7s and 7p, in covalent
        bonding to ligands; actinoids also show higher oxidation states (+4 to +6), giving ions of
        higher charge density. Hence actinoids
        form complexes more readily: both true, and R explains A.</p>
        <p><b>Answer: (1)</b></p>"""),

    MCQ(src=("chemistry_2015_16", "7(a)(iii)"), topic="d- and f-Block Elements",
        q=r"""<p>Acidified potassium permanganate oxidises potassium iodide to iodine. The number of
        moles of \(\ce{I2}\) liberated by one mole of \(\ce{KMnO4}\) is</p>""",
        options=[r"\(0.5\)", r"\(1\)", r"\(2.5\)", r"\(5\)"],
        answer=2,
        sol=r"""<p>In acid, Mn(+7) → \(\ce{Mn^2+}\): 5 electrons per \(\ce{MnO4-}\). Each \(\ce{I2}\) needs
        2 electrons removed from \(2\ce{I-}\).
        \[\ce{2MnO4- + 10I- + 16H+ -> 2Mn^2+ + 5I2 + 8H2O}\]
        So 2 mol \(\ce{MnO4-}\) give 5 mol \(\ce{I2}\): 2.5 mol per mole.</p>
        <p>5 counts moles of \(\ce{I-}\) oxidised, not \(\ce{I2}\); 0.5 inverts the ratio; 1 assumes a
        one-to-one reaction.</p>
        <p><b>Answer: (3) 2.5</b></p>"""),

    # ------------------------------------------------------------------ Coordination
    MCQ(src=("chemistry_2015_16", "5(b)"), topic="Coordination Compounds",
        q=r"""<p>Which of the following complex ions is optically active?</p>""",
        options=[r"trans-\(\ce{[Co(en)2Cl2]+}\)", r"cis-\(\ce{[Co(en)2Cl2]+}\)",
                 r"cis-\(\ce{[Co(NH3)4Cl2]+}\)", r"\(\ce{[Pt(en)Cl2]}\)"],
        answer=1,
        sol=r"""<p>cis-\(\ce{[Co(en)2Cl2]+}\) has no plane or centre of symmetry: its mirror image cannot
        be superimposed on it, so it exists as a pair of enantiomers.</p>
        {{fig:0}}
        <p>The trans isomer has a mirror plane through Co and the four N atoms (and a centre of
        symmetry), so it is optically inactive.</p>
        {{fig:1}}
        <p>cis-\(\ce{[Co(NH3)4Cl2]+}\) has a mirror plane containing both Cl and Co (monodentate
        ligands, no chelate rings); square-planar \(\ce{[Pt(en)Cl2]}\) lies in a plane of symmetry.</p>
        <p><b>Answer: (2)</b></p>""",
        sfig=[fig_co_en2cl2_optical, fig_b_trans_cocl2en2]),

    MCQ(src=("chemistry_2024_25_s1", "15"), topic="Coordination Compounds",
        q=r"""<p>A complex of composition \(\ce{Cr(NH3)4Cl2Br}\) is isolated in two forms. Form A gives
        with \(\ce{AgNO3}\) a white precipitate soluble in dilute aqueous ammonia; form B gives a pale
        yellow precipitate soluble only in concentrated ammonia. A and B are</p>""",
        options=[r"A = \(\ce{[Cr(NH3)4ClBr]Cl}\), B = \(\ce{[Cr(NH3)4Cl2]Br}\); ionisation isomers",
                 r"A = \(\ce{[Cr(NH3)4Cl2]Br}\), B = \(\ce{[Cr(NH3)4ClBr]Cl}\); ionisation isomers",
                 r"A = \(\ce{[Cr(NH3)4ClBr]Cl}\), B = \(\ce{[Cr(NH3)4Cl2]Br}\); linkage isomers",
                 r"A = cis-, B = trans-\(\ce{[Cr(NH3)4Cl2]Br}\); geometrical isomers"],
        answer=0,
        sol=r"""<p>White precipitate soluble in dilute \(\ce{NH3}\) is AgCl, so A has \(\ce{Cl-}\) outside the
        sphere: \(\ce{[Cr(NH3)4ClBr]Cl}\). Pale yellow AgBr, soluble only in concentrated
        \(\ce{NH3}\), shows \(\ce{Br-}\) outside in B: \(\ce{[Cr(NH3)4Cl2]Br}\).</p>
        <p>The two differ only in which anion is inside the coordination sphere and which is
        ionisable — <b>ionisation isomerism</b>. Linkage isomerism needs an ambidentate ligand; the
        cis/trans pair of option 4 would both give AgBr.</p>
        <p><b>Answer: (1)</b></p>"""),

    # ------------------------------------------------------------------ Haloalkanes
    MCQ(src=("chemistry_2024_25_s2", "1(B)(iii)"), topic="Haloalkanes and Haloarenes",
        q=r"""<p>The best reagent for converting ethanol into pure chloroethane is</p>""",
        options=[r"conc. HCl alone", r"\(\ce{PCl5}\)", r"\(\ce{SOCl2}\) in pyridine", r"\(\ce{PCl3}\)"],
        answer=2,
        sol=r"""<p>\[\ce{C2H5OH + SOCl2 ->[pyridine] C2H5Cl + SO2 ^ + HCl ^}\]
        Both by-products are gases and escape, leaving the alkyl chloride pure; pyridine takes up
        the HCl.</p>
        <p>\(\ce{PCl5}\) and \(\ce{PCl3}\) leave \(\ce{POCl3}\) / \(\ce{H3PO3}\) to be separated; conc. HCl
        alone reacts with a primary alcohol only slowly (it needs \(\ce{ZnCl2}\)).</p>
        <p><b>Answer: (3)</b></p>"""),

    MCQ(src=("chemistry_2025_26_s1", "14"), topic="Haloalkanes and Haloarenes",
        q=r"""<p>In the sequence
        \[\ce{C6H5NH2 ->[NaNO2/HCl][\text{0–5 °C}] A ->[CuCl/HCl] B ->[Na,\ CH3Cl][\text{dry ether}] C}\]
        the cross-coupled product C is</p>""",
        options=[r"biphenyl", r"ethylbenzene", r"chlorotoluene", r"toluene"],
        answer=3,
        sol=r"""<p>A = \(\ce{C6H5N2+Cl-}\); Sandmeyer: B = \(\ce{C6H5Cl}\); Wurtz–Fittig:
        \[\ce{C6H5Cl + 2Na + CH3Cl ->[\text{dry ether}] C6H5CH3 + 2NaCl}\]</p>
        <p>Biphenyl (Fittig, aryl + aryl) and ethane (Wurtz, alkyl + alkyl) are the by-products, not
        the cross product. No C–Cl survives the sodium, and no extra carbon is added to give
        ethylbenzene.</p>
        <p><b>Answer: (4) toluene</b></p>"""),

    # ------------------------------------------------------------------ Alcohols, Phenols, Ethers
    MCQ(src=("chemistry_2013_14", "1(b)(iii)"), topic="Alcohols, Phenols and Ethers",
        q=r"""<p>Phenol is heated with carbon tetrachloride and aqueous NaOH and the product is
        acidified. The major product is</p>""",
        options=[r"salicylaldehyde", r"salicylic acid", r"4-hydroxybenzoic acid", r"chlorobenzene"],
        answer=1,
        sol=r"""<p>This is the Reimer–Tiemann reaction with \(\ce{CCl4}\) in place of \(\ce{CHCl3}\). The
        phenoxide ion is attacked mainly at the ortho position; the \(\ce{-CCl3}\) group is hydrolysed
        to \(\ce{-COOH}\):
        \[\ce{C6H5OH + CCl4 + 6NaOH -> C6H4(ONa)COONa + 4NaCl + 4H2O}\ \text{(ortho)}\]
        Acidification gives 2-hydroxybenzoic (salicylic) acid.</p>
        <p>Salicylaldehyde is the product with chloroform; the para acid is the minor product;
        chlorobenzene is never formed from phenol this way.</p>
        <p><b>Answer: (2)</b></p>"""),

    MCQ(src=("chemistry_2025_26_s2", "14"), topic="Alcohols, Phenols and Ethers",
        q=r"""<p>Methyl tert-butyl ether, \(\ce{CH3-O-C(CH3)3}\), is heated with one equivalent of
        concentrated HI. The products are</p>""",
        options=[r"\(\ce{CH3I}\) and \(\ce{(CH3)3COH}\)", r"\(\ce{CH3OH}\) and \(\ce{(CH3)3CI}\)",
                 r"\(\ce{CH3I}\) and \(\ce{(CH3)3CI}\) only", r"\(\ce{CH4}\) and \(\ce{(CH3)3COI}\)"],
        answer=1,
        sol=r"""<p>The ether is protonated; the C–O bond to the <b>tertiary</b> carbon breaks because it
        gives a stable 3° carbocation (\(\mathrm{S_N1}\)), which then takes up \(\ce{I-}\).</p>
        {{fig:0}}
        <p>With a primary or methyl group on both sides (e.g. \(\ce{CH3OC2H5}\)) the cleavage would
        be \(\mathrm{S_N2}\) and \(\ce{I-}\) would attack the smaller methyl group, giving
        \(\ce{CH3I}\) — that is the slip behind option 1. Two iodides need excess HI.</p>
        <p><b>Answer: (2)</b></p>""",
        sfig=JF.fig_jc_mtbe_hi),

    # ------------------------------------------------------------------ Aldehydes, Ketones, Acids
    MCQ(src=("chemistry_2014_15", "8(a)"), topic="Aldehydes, Ketones and Carboxylic Acids",
        q=r"""<p>Which of the following gives a yellow precipitate with iodine and sodium hydroxide?</p>""",
        options=[r"pentan-3-one", r"propanal", r"methanol", r"butan-2-one"],
        answer=3,
        sol=r"""<p>The iodoform test needs a \(\ce{CH3CO-}\) group (or \(\ce{CH3CH(OH)-}\), which is
        oxidised to it). Butan-2-one, \(\ce{CH3COCH2CH3}\), has one:
        \[\ce{CH3COCH2CH3 + 3I2 + 4NaOH -> CHI3 v + CH3CH2COONa + 3NaI + 3H2O}\]</p>
        <p>Pentan-3-one has ethyl groups on both sides; propanal is \(\ce{CH3CH2CHO}\) (no
        \(\ce{CH3CO}\)); methanol is oxidised to HCHO, which has no methyl group.</p>
        <p><b>Answer: (4)</b></p>"""),

    MCQ(src=("chemistry_2025_26_s1", "6"), topic="Aldehydes, Ketones and Carboxylic Acids",
        q=r"""<p>Acetaldehyde heated with HI and red phosphorus gives</p>""",
        options=[r"ethanol", r"ethane", r"iodoethane", r"ethanoic acid"],
        answer=1,
        sol=r"""<p>HI/red P is a powerful reducing agent and reduces the carbonyl group completely to
        \(\ce{CH2}\):
        \[\ce{CH3CHO + 4HI ->[\text{red P}][\Delta] CH3CH3 + H2O + 2I2}\]
        (red P recycles the iodine to HI).</p>
        <p>Ethanol is the product of mild reduction (\(\ce{NaBH4}\), \(\ce{H2/Ni}\)); iodoethane would
        need HI on ethanol; ethanoic acid is an oxidation product.</p>
        <p><b>Answer: (2) ethane</b></p>"""),

    MCQ(src=("chemistry_2025_26_s2", "1(B)(v)"), topic="Aldehydes, Ketones and Carboxylic Acids",
        q=r"""<p>A mixture of calcium acetate and calcium formate is distilled dry. The cross product
        formed is</p>""",
        options=[r"acetaldehyde", r"acetone", r"formaldehyde", r"acetic anhydride"],
        answer=0,
        sol=r"""<p>\[\ce{(CH3COO)2Ca + (HCOO)2Ca ->[\Delta] 2CH3CHO + 2CaCO3}\]
        One acyl group from acetate (\(\ce{CH3CO-}\)) and an H from formate give ethanal.</p>
        <p>Acetone is from calcium acetate alone and formaldehyde from calcium formate alone (the
        self-products); anhydrides are not formed by dry distillation of calcium salts.</p>
        <p><b>Answer: (1) acetaldehyde</b></p>"""),

    # ------------------------------------------------------------------ Nitrogen compounds
    MCQ(src=("chemistry_2024_25_s1", "1(B)(i)"), topic="Organic Compounds containing Nitrogen",
        q=r"""<p>An amine \(\ce{C3H9N}\) (A) liberates \(\ce{N2}\) with nitrous acid, giving an alcohol.
        A warmed with \(\ce{CHCl3}\) and alcoholic KOH gives B, and reduction of B gives
        N-methylpropan-1-amine. A is</p>""",
        options=[r"\(\ce{(CH3)2CHNH2}\)", r"\(\ce{CH3CH2NHCH3}\)", r"\(\ce{(CH3)3N}\)",
                 r"\(\ce{CH3CH2CH2NH2}\)"],
        answer=3,
        sol=r"""<p>Both tests (\(\ce{N2}\) with \(\ce{HNO2}\); carbylamine reaction) show a primary amine.
        Carbylamine: \(\ce{R-NH2 -> R-N#C}\); reduction gives \(\ce{R-NH-CH3}\). Since the product is
        \(\ce{CH3CH2CH2-NH-CH3}\), R is n-propyl:
        \[\ce{CH3CH2CH2NH2 + CHCl3 + 3KOH -> CH3CH2CH2NC + 3KCl + 3H2O}\]
        \[\ce{CH3CH2CH2NC + 4[H] -> CH3CH2CH2NHCH3}\]</p>
        <p>Isopropylamine would give N-methylpropan-2-amine; the secondary and tertiary amines give
        no carbylamine reaction.</p>
        <p><b>Answer: (4)</b></p>"""),

    MCQ(src=("chemistry_2016_17", "8(a)(iii)"), topic="Organic Compounds containing Nitrogen",
        q=r"""<p>Aniline is best converted into fluorobenzene by</p>""",
        options=[r"\(\ce{NaNO2}\)/HCl at 0–5 °C, then CuCl/HCl",
                 r"\(\ce{NaNO2}\)/HCl at 0–5 °C, then KI",
                 r"direct reaction with \(\ce{F2}\) in the dark",
                 r"\(\ce{NaNO2}\)/HCl at 0–5 °C, then \(\ce{HBF4}\), then heating the dry salt"],
        answer=3,
        sol=r"""<p>Balz–Schiemann reaction:
        \[\ce{C6H5NH2 + NaNO2 + 2HCl ->[\text{273–278 K}] C6H5N2+Cl- + NaCl + 2H2O}\]
        \[\ce{C6H5N2+Cl- + HBF4 -> C6H5N2+BF4- v + HCl}\qquad \ce{C6H5N2+BF4- ->[\Delta] C6H5F + BF3 + N2 ^}\]</p>
        <p>CuCl/HCl gives chlorobenzene (Sandmeyer) and KI gives iodobenzene; fluorine reacts
        explosively and unselectively with aromatic amines.</p>
        <p><b>Answer: (4)</b></p>"""),

    # ------------------------------------------------------------------ Biomolecules
    MCQ(src=("chemistry_2024_25_s2", "17"), topic="Biomolecules",
        q=r"""<p>Fructose is a ketose, yet it reduces Tollens' reagent because</p>""",
        options=[r"its open-chain form contains a free –CHO group",
                 r"it is a non-reducing sugar that is hydrolysed by Tollens' reagent",
                 r"in the alkaline reagent it isomerises through an enediol to aldoses (glucose and mannose)",
                 r"Tollens' reagent oxidises the C=O of ketones to –COOH"],
        answer=2,
        sol=r"""<p>Tollens' reagent is alkaline. Base removes an α-H next to the C-2 carbonyl, giving an
        enediol that tautomerises to glucose and mannose (Lobry de Bruyn–van Ekenstein
        rearrangement); these aldoses reduce \(\ce{Ag+}\) to a silver mirror. (The α-hydroxy ketone
        group itself is also easily oxidised.)</p>
        <p>Fructose has a C=O at C-2, not a –CHO; it is a reducing sugar (its hemiketal opens);
        Tollens' reagent does not oxidise simple ketones.</p>
        <p><b>Answer: (3)</b></p>"""),

    # ================================================================== Section B (numerical)
    NUM(src=("chemistry_2024_25_s2", "21(ii) OR"), topic="Solutions",
        q=r"""<p>A 0.0711 molal aqueous solution of \(\ce{Na2SO4}\) freezes at −0.320 °C
        (\(K_f = 1.86\) K kg mol\(^{-1}\)). The apparent degree of dissociation of \(\ce{Na2SO4}\),
        in percent, is ______ (nearest integer).</p>""",
        answer=71,
        sol=r"""<p>\[i = \frac{\Delta T_f}{K_f m} = \frac{0.320}{1.86\times0.0711} = \frac{0.320}{0.1322} = 2.42\]
        \(\ce{Na2SO4 -> 2Na+ + SO4^2-}\): \(i = 1 + 2\alpha\Rightarrow\alpha = (2.42 - 1)/2 = 0.710\).</p>
        <p>(Using \(i = 1 + \alpha\) would give 142%, impossible.)</p>
        <p><b>Answer: 71</b></p>"""),

    NUM(src=("chemistry_2025_26_s1", "16(ii) OR"), topic="Electrochemistry",
        q=r"""<p>The conductivity of 0.01 M acetic acid at 298 K is \(1.65\times10^{-4}\) S cm\(^{-1}\).
        The limiting ionic conductivities of \(\ce{H+}\) and \(\ce{CH3COO-}\) are 349.1 and 40.9
        S cm\(^2\) mol\(^{-1}\). The degree of dissociation of the acid, in percent, is ______
        (nearest integer).</p>""",
        answer=4,
        sol=r"""<p>\[\Lambda_m = \frac{1000\times1.65\times10^{-4}}{0.01} = 16.5\ \text{S cm}^2\text{ mol}^{-1};\qquad
        \Lambda_m^\circ = 349.1 + 40.9 = 390.0\]
        \[\alpha = \frac{16.5}{390.0} = 0.0423 = 4.23\%\]</p>
        <p><b>Answer: 4</b></p>"""),

    NUM(src=("chemistry_2016_17", "3(a)(ii)"), topic="Chemical Kinetics",
        q=r"""<p>The temperature coefficient (ratio of rate constants for a 10 K rise, 298 K → 308 K)
        of the alkaline hydrolysis of ethyl acetate is 1.75. The activation energy is ______
        kJ mol\(^{-1}\) (nearest integer). (\(R = 8.314\) J K\(^{-1}\) mol\(^{-1}\),
        \(\log 1.75 = 0.243\))</p>""",
        answer=43,
        sol=r"""<p>\[E_a = \frac{2.303\,R\,T_1T_2}{T_2 - T_1}\log\frac{k_2}{k_1}
        = \frac{2.303\times8.314\times298\times308}{10}\times0.243 = 4.27\times10^4\ \text{J mol}^{-1}\]</p>
        <p>\(E_a = 42.7\) kJ mol\(^{-1}\).</p>
        <p><b>Answer: 43</b></p>"""),

    NUM(src=("chemistry_2024_25_s1", "20"), topic="d- and f-Block Elements",
        q=r"""<p>The volume of 0.05 M \(\ce{K2Cr2O7}\) required to oxidise 25 mL of 0.12 M
        \(\ce{FeSO4}\) in dilute \(\ce{H2SO4}\) is ______ mL.</p>""",
        answer=10,
        sol=r"""<p>\[\ce{K2Cr2O7 + 6FeSO4 + 7H2SO4 -> K2SO4 + Cr2(SO4)3 + 3Fe2(SO4)3 + 7H2O}\]
        (Cr: +6 → +3, 3 e\(^-\) each, 6 per dichromate; Fe: +2 → +3.)</p>
        <p>\(\ce{Fe^2+} = 25\times0.12 = 3.0\) mmol; dichromate \(= 3.0/6 = 0.50\) mmol;
        \(V = 0.50/0.05 = 10\) mL.</p>
        <p><b>Answer: 10</b></p>"""),

    NUM(src=("chemistry_2016_17", "5(b)"), topic="Coordination Compounds",
        q=r"""<p>If \(\mu\) is the spin-only magnetic moment of \(\ce{[FeCl4]-}\) in Bohr magnetons, the
        value of \(\mu^2\) is ______.</p>""",
        answer=35,
        sol=r"""<p>Fe is +3 (\(x - 4 = -1\)): \(3d^5\). Tetrahedral, and \(\ce{Cl-}\) is weak field with a
        small \(\Delta_t\): high spin \(e^2t_2^3\), 5 unpaired electrons.</p>
        {{fig:0}}
        <p>\(\mu^2 = n(n + 2) = 5\times7 = 35\) (\(\mu = 5.92\) BM).</p>
        <p><b>Answer: 35</b></p>""",
        sfig=fig_fecl4_cft),
]
