# Vibe Academic PPT

Vibe Academic PPT is a workspace for building academic paper presentation slides with TeX/Beamer.

## Repository Layout
- `reference/`: source paper PDFs, course requirements, notes, and extracted figures
- `template/`: the SYSU-PRE base template to copy into `output/` before drafting slides
- `output/`: generated TeX, figures, logs, PDF, and speech script
- `skills/`: local planning, personalization, and TeX workflow skills plus supporting notes
- `tools/`: helper scripts, including the layout audit utility
- `AGENTS.md`: agent-facing workflow and quality gate for this repository

## Recommended Workflow
1. Put the paper PDF, course brief, and any supporting notes in `reference/`.
2. Copy the template from `template/` into `output/` before writing slides.
3. Run `academic-ppt-planner` to refine the requirements and build the page outline.
4. Run `presentation-personalizer` whenever duration, audience, or figure strategy changes.
5. Draft `pre.tex` and `pre.bib` in `output/`, then use `tex-ppt-structuring` to place figures and prepare the speech script.
6. Build in `output/` with `tex-builder`, then run the layout audit before finalizing the PDF.

## Skills and Notes
- [`skills/academic-ppt-planner/SKILL.md`](skills/academic-ppt-planner/SKILL.md): requirement refinement and page planning
- [`skills/presentation-personalizer/SKILL.md`](skills/presentation-personalizer/SKILL.md): persistent presentation preferences
- [`skills/tex-ppt-structuring/SKILL.md`](skills/tex-ppt-structuring/SKILL.md): slide structuring, figure placement, and speech scripts
- [`skills/tex-builder/SKILL.md`](skills/tex-builder/SKILL.md): XeLaTeX build and troubleshooting
- [`skills/README.md`](skills/README.md): index of the supporting markdown templates and notes

## Build Commands
Run these inside the `output/` directory:

```powershell
xelatex -interaction=nonstopmode pre
bibtex pre
xelatex -interaction=nonstopmode pre
xelatex -interaction=nonstopmode pre
python ..\tools\ppt_layout_audit.py --tex pre.tex --log pre.log
```

## Personalization Rule
If presentation requirements change, update `skills/presentation_personalization_requirements.md` through the `presentation-personalizer` workflow before regenerating the outline or script.

## Acknowledgements
Special thanks to [SYSU-PRE](https://github.com/Lovely-XPP/SYSU-PRE) for the LaTeX Beamer template used for Sun Yat-Sen University academic presentations.
