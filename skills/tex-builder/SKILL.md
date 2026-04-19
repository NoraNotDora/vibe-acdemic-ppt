---
name: "tex-builder"
description: "Build and troubleshoot XeLaTeX academic PPTs in `output/`. Use when compilation fails, citations or fonts break, PATH or MiKTeX setup is missing, or you need the reliable build chain and layout-audit checklist."
---

# TeX Build and Troubleshooting Skill

Use this skill when the slide TeX should compile, but the build is failing or needs a clean final pass.

## When to Trigger
- `xelatex` or `bibtex` is missing or not on PATH.
- The PDF does not build, or citations and cross-references do not resolve.
- Fonts, figures, or math look wrong in the compiled deck.
- You need a reliable build checklist for `output/pre.tex`.

## Build Assumptions
- Work inside `output/`.
- Use MiKTeX on Windows unless the repo says otherwise.
- Keep the standard build chain unless the log tells you to stop earlier.

## Recommended Build Flow
1. `xelatex -interaction=nonstopmode pre`
2. `bibtex pre`
3. `xelatex -interaction=nonstopmode pre`
4. `xelatex -interaction=nonstopmode pre`

Target output: `pre.pdf`

## After the First Successful Compile
- Inspect `pre.log` for `Overfull \hbox`, `Overfull \vbox`, unresolved references, and font warnings.
- Run `python ..\tools\ppt_layout_audit.py --tex pre.tex --log pre.log`.
- Treat layout warnings as fix-before-final issues.

## Common Fixes
- `where xelatex` returns nothing: refresh PATH or reopen the terminal.
- MiKTeX log directory error: create `"$env:LOCALAPPDATA\MiKTeX\miktex\log"`.
- Bibliography missing: verify `.bib` keys and rerun the full chain.
- Output PDF locked: close the viewer or compile with a temporary job name.

## Optional One-Command Build
```powershell
latexmk -xelatex -synctex=1 -interaction=nonstopmode pre.tex
```

## Minimum Acceptance Criteria
- `pre.pdf` is generated successfully.
- Agenda, content, and reference pages render correctly.
- Fonts, figures, and formulas show no obvious errors.
