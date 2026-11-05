# Independent review brief

You are reviewing a paper that another agent transcribed, filtered and solved. You did not write
it; assume it contains errors and find them. Read `src/BRIEF.md` first (the writer's brief) and
`src/kit.py`'s docstring.

For each module you are given (`src/data/<module>.py`, its figures in `src/figs/`, checks in
`src/checks/`):

1. **Transcription.** Render every page of the source PDF
   (`pdftoppm -r 200 -png file.pdf /var/tmp/<you>/p`) and compare each question, word for word
   and number for number, with the module: values, units, signs, exponents, options, marks,
   numbering, nothing missing, nothing invented. Every diagram printed in the paper must be
   redrawn as a `qfig`, matching every labelled value.
2. **Syllabus filter.** Open `class12/<Subject>/Syllabus/ISC-2027.pdf`. For every excluded item,
   confirm the topic really is outside the ISC 2027 Class XII syllabus (theory or practical);
   for every kept item, confirm it is inside. Wrongly excluded → write the answer. Wrongly kept →
   exclude with a reason.
3. **Answers.** Solve every kept question yourself, independently, before reading the given
   answer, then compare. Check the reasoning step by step, not just the final value — an
   invalid step with a right answer is an error. Units, significant figures, sign conventions,
   balanced equations, Java that compiles and runs (re-run it), dry-runs re-traced. Check that
   the answer is what an ISC examiner would award full marks for (definitions stated, laws named,
   diagram labelled), and that the *Concepts to recall* panel is correct and relevant.
4. **Figures.** `python3 src/preview.py <figs_module>` and Read every PNG. Check each figure
   against the physics/chemistry/maths/logic it claims to show (see the BRIEF's list: ray
   geometry, field and current directions, polarity, valencies and stereochemistry, gate wiring,
   K-map order and groups, tree children, feasible-region side, curve shapes and intersections,
   axis labels). Check labels don't collide. A figure that is merely plausible is not enough —
   recompute the geometry it depends on.
5. **Page.** `python3 src/build.py <module>` (no ERROR), then
   `python3 src/preview.py --page <subject>/<slug>.html` and Read every slice: math renders,
   nothing overflows, figures where they belong.

**Fix what you find**, directly in the module / figure / check files (keep the check scripts
passing and extend them to cover what you fixed). Then rebuild.

Log everything in `src/checks/review_<module>.md`: one entry per finding — item, what was wrong,
what you changed — plus a line per item/figure you checked and found correct. End your final
message with a summary: counts of items checked, errors found by kind (transcription / filter /
answer / figure / layout), and anything you could not resolve.

Do not edit `kit.py`, `build.py`, `preview.py`, `svg.py` or `assets/`; report kit problems instead.
Other agents may be working on other modules at the same time — touch only yours.
