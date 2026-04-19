# TeX Setup and Build Notes

> Quick build and troubleshooting notes for `skills/tex-builder/SKILL.md`.

## 1. Environment Setup
- Install MiKTeX.
- Install Perl (required by `latexmk`).

## 2. Required Executable Paths (Windows + MiKTeX)
- Typical path: `C:\Users\<username>\AppData\Local\Programs\MiKTeX\miktex\bin\x64`
- Must include at least:
  - `xelatex.exe`
  - `bibtex.exe`
  - `latexmk.exe` (optional but recommended)
  - `initexmf.exe`

## 3. First-Time Verification Commands
```powershell
where xelatex
where bibtex
where latexmk
perl -v
```

If `where xelatex` returns nothing, temporarily prepend PATH:
```powershell
$env:Path="C:\Users\<username>\AppData\Local\Programs\MiKTeX\miktex\bin\x64;$env:Path"
```

## 4. Recommended Build Flow (XeLaTeX)
Run inside `output/`:
```powershell
xelatex -interaction=nonstopmode pre
bibtex pre
xelatex -interaction=nonstopmode pre
xelatex -interaction=nonstopmode pre
```

Target output: `pre.pdf`

### 4.1 Quick Layout Audit
After the first successful compile, run:
```powershell
python tools/ppt_layout_audit.py --tex pre.tex --log pre.log
```

Use the audit to quickly judge:
- whether a frame has too many bullets or too many major blocks
- whether a figure is too wide, too small, or visually unbalanced
- whether the log contains `Overfull \hbox` or `Overfull \vbox`
- whether a slide lacks a clear dominant visual element

Treat audit warnings as fix-before-final issues, especially when a page mixes dense text and large figures.

## 5. Single-Command Build (Optional)
```powershell
latexmk -xelatex -synctex=1 -interaction=nonstopmode pre.tex
```

## 6. Common Troubleshooting
### 6.1 No output from `where xelatex`
- Cause: PATH not refreshed or not set in user environment variables.
- Fix:
  1. Reopen terminal.
  2. Temporarily prepend PATH (as above).
  3. Add MiKTeX `bin` path in system/user environment settings if needed.

### 6.2 MiKTeX update check warning
- You can ignore it temporarily for basic builds.
- Update packages later in MiKTeX Console.

### 6.3 Log directory error (`log4cxx`)
- Create the log directory, then retry:
```powershell
New-Item -ItemType Directory -Force -Path "$env:LOCALAPPDATA\MiKTeX\miktex\log"
```

### 6.4 Bibliography not showing
- Ensure `.bib` keys match `\cite{}` keys.
- Run the full chain: `xelatex -> bibtex -> xelatex -> xelatex`.

## 7. Minimum Acceptance Criteria
- `pre.pdf` is generated successfully.
- Agenda, content, and reference pages render correctly.
- Fonts, figures, and formulas show no obvious errors.
