# Brief: Heritage School pre-board papers → solved revision site

Site root: `/home/sayantan/Ujaan/class12/PreBoard-Revision/` (a static site to be pushed to GitHub
Pages as-is). Read `src/kit.py` (its docstring is the data contract), `src/figs/svg.py`,
`src/build.py`, `src/preview.py`.

Source papers: `/home/sayantan/Ujaan/class12/SchoolNotes/PreBoard-PYQ/<year>/*.pdf` — Heritage
School Class XII pre-board papers, 2013-14 to 2016-17.

**Practical papers** (Physics/Chemistry practical, CS Paper II) set `practical=True` in PAPER;
the subject index lists them under a separate "Practical papers" heading.

## What you produce, per paper

1. **A digital copy.** Every question of the paper, in printed order, as `Q(...)` items in
   `src/data/<subject>_<yyyy>_<yy>[_prac|_p1|_p2].py` (e.g. `physics_2013_14.py`,
   `physics_2013_14_prac.py`, `computers_2015_16_p2.py`), with section headings (`SEC`) and the
   printed instructions in `intro`. Keep the paper's own numbering (`1(a)(iii)`, `7 (OR)`, …),
   its marks and its wording. Transcribe from the **page images**, not from `pdftotext`:
   `pdftoppm -r 200 -png -f N -l N file.pdf /var/tmp/<you>/pN` and Read the PNG (crop with PIL to
   zoom on a dense area). Formulas, Greek letters, primes and subscripts are lost or garbled in
   extracted text, and the 2016-17 papers have no text layer at all. Existing OCR of the 2016-17
   papers may help as a starting point: `class12/Chemistry/OCR/heritage-2016-17-preboard.txt`,
   `class12/Computers/OCR/heritage-2016-17-preboard.txt`, `class12/Maths/OCR/`,
   `class12/Physics/src/paper-text/`. Always confirm against the image.
   **Every diagram printed in a question is redrawn** as SVG and attached as `qfig`.
   Choose the granularity of `Q` items as the smallest sub-part that carries its own marks
   (e.g. each of 1(a)…1(o) is its own item).

2. **The ISC 2027 filter.** The authority is the CISCE syllabus
   `class12/<Subject>/Syllabus/ISC-2027.pdf` (Maths dir is `Maths`, CS dir is `Computers`) —
   read the Class XII theory section **and** the practical section. A question (or sub-part)
   whose topic is not in the ISC 2027 Class XII syllabus gets
   `excluded="<one-line reason naming the topic and why, e.g. 'Communication systems — removed
   from ISC syllabus; not in ISC 2027 Unit list'>"` and no answer. Be decisive, judge each
   sub-part on its own, and don't exclude a question just because it is phrased in an old style.
   Examples of known removals worth checking: Maths — linear regression, and Section C
   commerce/economics applications; check what the 2027 syllabus actually lists. Practical
   papers: keep an experiment only if it (or the same measurement) is in the 2027 practical list.

3. **The solution**, for every kept item, written as an ISC candidate should write it:
   - the working in steps, each line justified; formula first, then substitution, then the
     result **with unit** and to sensible significant figures; final result in
     `<span class="box">…</span>`;
   - definitions/laws stated precisely; derivations complete with a labelled diagram;
   - "explain/why" questions answered in the points an examiner marks;
   - **diagrams in the answer wherever the answer needs one** (ray diagrams, circuit diagrams,
     field patterns, graphs, apparatus, structures of molecules/mechanisms, logic circuits,
     K-maps, trees, linked lists, area-under-curve sketches, LPP feasible regions…). Put them in
     `afig` and place them with `{{fig:N}}`;
   - a short `recall` panel (`<ul>` of 2–5 items): the formulae, definitions or ideas a student
     needs to recall to solve this question. Not a repeat of the answer.
   - `topic` = the ISC 2027 syllabus chapter/unit name.
   - Physics/Chemistry practical: give the method, a table of **realistic sample readings**
     (clearly labelled as sample readings, generated from plausible apparatus values and rounded
     to the instrument least count), the calculation, the graph (as a figure, with best-fit line
     and slope triangle where used) and the result. Chemistry salt/organic analysis: tests,
     observations and inferences table, ending in the ions/compound identified, with ionic
     equations. Titration: the full calculation from the given data.
   - Computer Science: Java only (as ISC). Programs complete and compilable, with comments,
     algorithm where the question asks for one, and sample input/output. Output-prediction /
     dry-run questions show the trace.

## Correctness — this is the point of the exercise

- **Every number is checked by computation.** Write `src/checks/<module>_check.py` that
  recomputes each numerical answer from the question data (sympy for Maths: integrals,
  derivatives, determinants, matrix inverses, probabilities, LPP vertices). Run it; it must pass.
- **Every Java program is compiled and run** (`java File.java`, JDK 11 single-file launcher; put
  them in `src/checks/java/<module>/`). Paste only code that ran. Check dry-run answers by running.
- **Every figure is rendered and looked at**: `python3 src/preview.py <figs_module>` writes one PNG
  per `fig_*` to `/var/tmp/pbrev-preview/<module>/`; Read each PNG. Check the physics/chemistry/
  maths of it, not just that it draws: rays obey the lens/mirror rule and pass through the right
  focal points with the image where the formula puts it; current/field directions consistent
  (right-hand rules); battery polarity and meter placement correct; logic gates actually wired
  to the inputs (complemented inputs included); molecular structures with correct valencies,
  bond positions and stereochemistry; graphs with labelled axes, correct shape, intercepts and
  asymptotes; feasible regions on the correct side of each line; arrows pointing the right way.
  Labels must not overlap lines or each other. A figure redrawn from the question must match the
  printed one in every labelled value.
- Then build (`python3 src/build.py <module>` — must report no ERROR) and look at the whole page:
  `python3 src/preview.py --page <subject>/<slug>.html` → Read every slice. Check math renders
  (no raw `\(`), nothing overflows, figures sit where they belong.
- Keep `src/checks/<module>_figs.md`: one line per figure stating what you checked.

## Figures

Figure modules: `src/figs/<subject>_<yyyy>_<yy>_figs.py` (one per paper, or per agent), each figure a
`fig_<something>()` returning SVG. Use `svg.Fig` (arrow markers get unique ids) or write SVG by
hand; any id inside an SVG must be unique on the page (prefix with the function name). No HTML
tags inside `<text>` (use `sub=`/`sup=` of `Fig.text`, or `<tspan>`). Fixed colours (light page).
Draw to scale where the answer depends on geometry.

## Rules

- Do not edit `kit.py`, `build.py`, `preview.py`, `svg.py`, `assets/` — if you need a kit change,
  say so in your final report. Do not touch other agents' modules.
- Raw strings `r"..."` for anything containing backslashes. KaTeX delimiters `\( \)` / `\[ \]`
  only (no `$`). Chemistry formulae with `\ce{}`. Escape `<`, `>`, `&` in code and in prose
  (`&lt;`), never a bare `<` in HTML text.
- Do not put the original PDFs in the site.
- If a word or number on the paper is unreadable, give your best reading and add a note in the
  question (`<p class="note">[Unclear in the original: …]</p>`). If the paper itself is wrong
  (misprint, impossible data), solve the evident intended question and say so in a note.
- Final report (your last message): per paper — items kept / excluded with the list of excluded
  topics; figures drawn; checks run and their result; anything unclear or doubtful.
