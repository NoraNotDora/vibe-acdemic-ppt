---
name: "academic-ppt-planner"
description: "Helps plan and structure academic paper presentations. Invoke when starting a new academic PPT project, outlining slides, or refining presentation requirements."
---

# Academic PPT Plan Template (XeLaTeX)

## 0. Project Info
- Course / context:
- Target paper:
- Presentation duration:
- Template path:
- Target build directory:

## 1. Input Materials
- Paper PDF:
- Course references / textbook chapters:
- Existing outline (if any):
- Figure sources (paper figures, experiment plots, flowcharts):

## 2. Requirement Refinement (Do This First)
### 2.1 Content Goals
- Core problem to explain:
- Key methods:
- Key results:
- Critical analysis:

### 2.2 Style Goals
- Tone: academic, objective, structured
- Layout: visual-first with controlled page density
- Math expression: consistent notation, readable formulas

### 2.3 Delivery Criteria
- Target page count (recommended 14–20):
- Time fit (expected speaking time per page):
- Output files: `pre.tex`, `pre.bib`, `pre.pdf`

## 3. Page Structure Plan (Example)
1. Title
2. Agenda
3. Background and problem definition
4. Paper contributions
5. Method overview
6. Mathematical modeling
7. Optimization formulation and solver
8. Experiment setup
9. Core results
10. Result interpretation
11. Limitations and improvement directions
12. Conclusion
13. References
14. Q&A

## 4. Figure-Text Strategy (Must Be Explicit)
- At least one visual anchor per page (figure / flowchart / table).
- Prioritize key paper figures in matching logical positions.
- Figure naming convention: `fig/<section>/<figure-name>.<ext>`
- Add 1–2 speaking points for each key figure.

## 5. Implementation Steps
### Phase A: Project Initialization
- Copy template into target directory.
- Verify `pre.tex / pre.bib / fig / cls` completeness.

### Phase B: Content Drafting
- Fill `pre.tex` by page structure.
- Update `pre.bib`.
- Insert key paper figures and captions.

### Phase C: Build and Fix
- Run XeLaTeX build chain.
- Fix fonts, figure paths, citations, and overflow issues.

### Phase D: Finalization
- Check page density and transition smoothness.
- Ensure timing fit at script level.
- Freeze deliverable version.

## 6. Build Commands
```powershell
xelatex -interaction=nonstopmode pre
bibtex pre
xelatex -interaction=nonstopmode pre
xelatex -interaction=nonstopmode pre
```

## 7. Execution Checklist
- [ ] Requirement refinement completed
- [ ] Page-level outline completed
- [ ] Figure resources collected
- [ ] `pre.tex` content drafted
- [ ] `pre.bib` updated
- [ ] Build completed and `pre.pdf` generated
- [ ] Final speech script aligned with target duration