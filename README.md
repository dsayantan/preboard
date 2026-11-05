# ISC Pre-Board Revision

Heritage School Class XII pre-board papers (2013-14 to 2016-17 and 2025-26) for Physics, Chemistry,
Mathematics and Computer Science, transcribed, filtered to the **ISC 2027 syllabus** and solved
question by question, with diagrams.

Open `index.html`, or publish with GitHub Pages (Settings → Pages → Deploy from branch → `/ (root)`).
The site is fully static and self-contained: maths is rendered by a vendored copy of KaTeX in
`assets/katex/`, so it needs no CDN and works offline.

## Layout

```
index.html                 landing page
<subject>/index.html       papers for that subject
<subject>/<year>.html      one paper: questions, hidden answers, concepts to recall,
                           and the out-of-syllabus questions listed (unanswered) at the end
assets/                    site.css, site.js, KaTeX
src/                       generators (Python 3) — not needed to view the site
```

## Rebuilding

```
python3 src/build.py                 # all papers + index pages
python3 src/build.py physics_2013_14 # one paper
python3 src/preview.py <figs_module> # render figures to PNG for checking
```

Each paper is one data module in `src/data/`, its figures in `src/figs/`, and the scripts that
recompute its numerical answers / run its Java programs in `src/checks/`.
