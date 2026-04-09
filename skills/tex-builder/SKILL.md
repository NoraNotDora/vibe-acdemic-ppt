---
name: "tex-builder"
description: "Provides guidance and commands for building XeLaTeX projects. Invoke when encountering TeX compilation errors, building a PDF, or setting up the TeX environment."
---

# TeX Setup and Build Notes

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
Run in the PPT project directory:
```powershell
xelatex -interaction=nonstopmode pre
bibtex pre
xelatex -interaction=nonstopmode pre
xelatex -interaction=nonstopmode pre
```

Target output: `pre.pdf`

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