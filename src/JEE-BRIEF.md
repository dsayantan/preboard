# Brief: JEE Main–style mock tests built from the pre-board questions

Three full mock tests, `jee/test-1.html` … `jee/test-3.html`, plus `jee/index.html`, added to the
site at `/home/sayantan/Ujaan/class12/PreBoard-Revision/`. **Every question is adapted from a
question in the pre-board papers already on this site** (`src/data/*.py`, kept items only — never
an item with `excluded=`), and says which one.

## The pattern (JEE Main, current NTA pattern)

- Three subjects in this order: **Physics, Chemistry, Mathematics**. (No Computer Science — JEE
  has none.)
- Each subject: **Section A — 20 multiple-choice questions**, four options, exactly one correct;
  **Section B — 5 numerical-value questions**, all compulsory, answer an **integer** (the
  candidate types it; state any rounding in the question: "nearest integer").
- Numbering runs through the paper: Physics 1–25, Chemistry 26–50, Mathematics 51–75.
- Marking, both sections: **+4 correct, −1 wrong, 0 unattempted**. 75 questions, **300 marks,
  3 hours (180 minutes)**.
- Style: JEE single-concept-plus-calculation questions — crisp stem, options that are the values a
  student gets from the standard slips (sign error, missing factor of 2, wrong formula), not
  absurd values. Numerical answers are integers, chosen so the data give a clean integer or one
  that rounds unambiguously.

## Data contract — `src/jee/<subject>_t<N>.py` (subject ∈ physics, chemistry, maths; N ∈ 1,2,3)

```python
from jee_kit import MCQ, NUM
SUBJECT = "physics"; TEST = 1
QUESTIONS = [
    MCQ(src=("physics_2016_17", "3(b)"),          # (data module, printed question number)
        topic="Current Electricity",                # ISC 2027 chapter name
        q=r"<p>…stem… \(R = 4\,\Omega\) …</p>",
        options=[r"\(2\) A", r"\(4\) A", r"\(1\) A", r"\(0.5\) A"],
        answer=1,                                   # index 0–3 of the correct option
        sol=r"<p>…worked solution, steps, then the answer…</p>",
        qfig=None, sfig=None),                      # optional fig_* functions (SVG), as in kit
    ...  # 20 MCQ first
    NUM(src=("maths_2025_26", "14"), topic="Integrals",
        q=r"<p>…</p>", answer=12, sol=r"<p>…</p>"),
    ...  # then 5 NUM
]
```

`src/jee_kit.py` defines `MCQ` / `NUM` and `check()`. Same HTML/KaTeX rules as `src/BRIEF.md`
(raw strings, `\( \)` / `\[ \]`, `\ce{}`, escape `<`), same SVG rules (unique ids, no HTML inside
`<text>`). A figure printed in the source question can be reused by importing that paper's
`fig_*` function; new figures go in `src/jee/<subject>_figs.py`.

**`check()` enforces:** `src` names an existing data module and a **kept** item in it; 20 MCQ then
5 NUM; 4 distinct options; `answer` in range (MCQ) or an `int` (NUM); non-empty `sol` and
`topic`; no single correct letter used for more than 7 of a subject's 20 MCQs in a test; no
`src` used twice in the same test-subject; no question text identical across the three tests.

## Coverage

Spread each subject-test across the Class XII chapters in roughly JEE proportion (no chapter more
than 4 questions in one subject-test), draw from as many different pre-board papers/years as
possible, and over the three tests use as much of the bank as is sensible. Adapt freely —
change numbers, turn a "derive/explain" item into a conceptual MCQ, a 4-mark numerical into a
single-answer one — but the question must be recognisably built on its source item and in the
ISC 2027 syllabus (which is why only kept items are allowed).

## Correctness

`src/checks/jee_<subject>_check.py` recomputes **every** numerical result: the value of the
correct option and each NUM answer (sympy for maths), and confirms no distractor equals the
correct value. Conceptual MCQs: the check asserts the chosen index; the solution must say why each
wrong option is wrong. Render and look at every figure (`python3 src/preview.py <figs module>`).
An independent reviewer will re-solve every question afterwards.

## Build and page (shell agent)

`python3 src/build_jee.py` → `jee/test-1.html`, `jee/test-2.html`, `jee/test-3.html`,
`jee/index.html`; the landing page (`src/build.py` `build_index`) gets a "JEE Main mock tests"
card when `jee/index.html` exists. Same assets (`../assets/site.css`, KaTeX) and light palette.
