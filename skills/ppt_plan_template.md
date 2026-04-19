# Academic PPT Plan Template (XeLaTeX)

> Use this template with `skills/academic-ppt-planner/SKILL.md`. Fill it in before any TeX drafting so the outline, figure map, and risk list stay explicit.

## 0. Project Info
- Course / context:
- Target paper:
- Presentation duration:
- Audience background:
- Template path:
- Target build directory:

## 1. Input Materials
- Paper PDF:
- Course references / textbook chapters:
- Existing outline (if any):
- Figure sources (paper figures, experiment plots, flowcharts):
- Notes / glossary / terminology list:

## 2. Requirement Refinement (Do This First)
### 2.1 Content Goals
- Core problem to explain:
- Key methods:
- Key results:
- Critical analysis:
- Key concepts / terms / abbreviations:
- Uncommon core concepts that must be explained:
- First-appearance explanation strategy (definition / analogy / example / figure annotation):
- Which terms must appear in the audience-facing script:

### 2.2 Audience Goals
- Audience type:
- Assumed background:
- What the audience will not know:
- Bridge sentences needed for unfamiliar terms:
- Places where a dedicated concept slide is needed:

### 2.3 Style Goals
- Tone: academic, objective, structured
- Layout: visual-first with controlled density
- Size budget per page: dominant block / secondary block / caption length
- Math expression: consistent notation, readable formulas

### 2.4 Delivery Criteria
- Target page count (recommended 14-20):
- Time fit (expected speaking time per page):
- Output files: `pre.tex`, `pre.bib`, `pre.pdf`
- Layout preflight check: pass/fail criteria

## 3. Page Structure Plan (Example)
1. Title
2. Agenda
3. Background and problem definition
4. Core concepts / notation bridge
5. Paper contributions
6. Method overview
7. Mathematical modeling
8. Optimization formulation and solver
9. Experiment setup
10. Core results
11. Result interpretation
12. Limitations and improvement directions
13. Conclusion
14. References
15. Q&A

## 4. Figure-Text Strategy (Must Be Explicit)
- At least one visual anchor per page (figure / flowchart / table).
- Prioritize key paper figures in matching logical positions.
- For each page, record:
  - Dominant visual element:
  - Supporting text budget (bullet count / line count):
  - Size ratio target:
  - Split condition:
- Figure naming convention: `fig/<section>/<figure-name>.<ext>`
- Add 1-2 speaking points for each key figure.

## 5. Layout Preflight Check
### 5.1 Quick Rules
- If a page has no visual anchor and more than 4 bullets, split it or add a diagram.
- If a page has more than 2 major blocks, treat it as a split candidate.
- If a single figure occupies less than 35% or more than 85% of the page width without intent, revise the layout.
- For side-by-side layouts, keep the visual weight balanced unless one side is clearly the primary figure.
- Keep captions short enough to remain in one or two lines.

### 5.2 Compile-Time Check
- Run the XeLaTeX build chain.
- Inspect `pre.log` for `Overfull \hbox`, `Overfull \vbox`, and page break warnings.
- Use `tools/ppt_layout_audit.py --tex pre.tex --log pre.log` for a quick pass/fail report.
- If the audit flags a page, resize, simplify, or split before finalizing.

## 6. Implementation Steps
### Phase A: Project Initialization
- Copy the template into the target directory.
- Verify `pre.tex`, `pre.bib`, `fig`, and class files are present.

### Phase B: Content Drafting
- Fill `pre.tex` by page structure.
- Update `pre.bib`.
- Insert key paper figures and captions.
- Add plain-language explanations for uncommon core concepts.

### Phase C: Build and Fix
- Run the XeLaTeX build chain.
- Fix fonts, figure paths, citations, size balance, and overflow issues.
- Re-run the layout audit after each non-trivial layout change.

### Phase D: Finalization
- Check page density and transition smoothness.
- Ensure timing fit at script level.
- Freeze the deliverable version.

## 7. Execution Checklist
- [ ] Requirement refinement completed
- [ ] Key concepts and uncommon terms identified
- [ ] Page-level outline completed
- [ ] Figure resources collected
- [ ] Layout budgets assigned to every page
- [ ] `pre.tex` content drafted
- [ ] `pre.bib` updated
- [ ] Build completed and `pre.pdf` generated
- [ ] Layout audit passed or all issues resolved
- [ ] Final speech script aligned with target duration
