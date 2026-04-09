# Vibe Academic PPT

Vibe Academic PPT is a workflow-oriented repository for building academic paper presentation slides with TeX/Beamer.  
It combines planning templates, agent rules, figure-handling guidance, and build notes to produce consistent, presentation-ready outputs.

## What This Repository Provides
- A structured workflow from requirement refinement to final slide build
- Generic skills for page planning and narrative organization
- Guidance for figure placement, caption quality, and script generation
- XeLaTeX build commands and troubleshooting notes for Windows + MiKTeX
- A personalization file to keep evolving presentation preferences

## Core Files
- [AGENTS.md](AGENTS.md): agent-facing workflow and quality gate
- `skills/`: directory containing generic skills for PPT planning, TeX building, structuring, and personalization.

## Recommended Workflow
1. **Preparation**: Create a `reference/` folder and place your target paper, course requirements, and existing outlines inside. Create an `output/` folder for the generated files.
2. Use the `academic-ppt-planner` skill to fill in project context and confirm audience, duration, and constraints.
3. Build a macro storyline: Motivation -> Method -> Evaluation -> Conclusion.
4. Map key paper figures to slide pages and speaking goals.
5. Draft `pre.tex` and `pre.bib` inside the `output/` folder, then compile with XeLaTeX.
6. Generate a directly deliverable speech script.

## Build Commands
Run these inside the `output/` directory:
```powershell
xelatex -interaction=nonstopmode pre
bibtex pre
xelatex -interaction=nonstopmode pre
xelatex -interaction=nonstopmode pre
```

## Personalization Rule
If presentation requirements change (duration, focus, figure strategy, output format), append updates to the `presentation-personalizer` skill before regenerating outline and script.