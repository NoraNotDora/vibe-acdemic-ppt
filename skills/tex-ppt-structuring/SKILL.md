---
name: "tex-ppt-structuring"
description: "Structures TeX academic slides and generates speech scripts. Invoke when handling figure integration, structuring presentations, or writing speech scripts."
---

# TeX Academic PPT Structuring and Speech Script Skill (English Version)

## 1. Scope
- Build or refine TeX-based academic slides (for example, `slides.tex`) with stable layout and clear narrative.
- Handle common issues such as misaligned figures, duplicated caption numbering, unclear figure meaning, and crowded slide text.
- Generate speech-ready scripts with strong logic, not rehearsal scripts.

## 2. Folder and Naming Conventions
- Figure folder: `fig/<topic>/`
- Figure naming: `fig/<topic>/<fig-id>-<short-name>.pdf`
- Prefer vector assets (PDF, or SVG converted to PDF); use PNG only when needed.
- Keep legend files near their main figures, for example `*-legend.pdf`.

## 3. Figure Integration Workflow (Execution Order)
1. Build a mapping table: `source figure id -> slide page -> speaking purpose`
2. Choose layout first: single figure / side-by-side / figure + short takeaway
3. Ensure alignment first, then tune size
4. Write caption and speaking sentence
5. Compile and check overflow, overlap, and numbering
6. Normalize caption style across the deck

## 4. Presentation Structuring Principles (Macro First)
- Use the default storyline: **Motivation -> Method -> Evaluation -> Conclusion**.
- Group strongly related pages before writing page-level scripts.
- Typical grouped blocks:
  - Motivation + problem definition
  - System overview + module details
  - Variable definition + objective + constraints
  - Experiment setup + main results + ablation/robustness
- Output macro outline first, then generate page-level speech script.

## 5. Chapter Coverage Check (Section-by-Section)
- Build a coverage table: `section title -> mapped slide pages -> covered? -> evidence(page/figure)`.
- For each section, check at least:
  - Core question is explained
  - Key method/formula is present
  - Key experimental finding is cited
  - Transition to neighboring sections is clear
- If something is missing, add evidence-first content before adding detail pages.

## 6. Figure Usage Strategy (Maximize Source Figure Coverage)
- Goal: include as many source figures as reasonably possible.
- Build a figure map: `figure id -> meaning -> related section -> recommended placement`.
- Arrangement rules:
  - Organize by figure-content relationship, not rigid source order
  - Keep figures for one argument adjacent when possible
  - Keep legends on the same or neighboring page as the main figure
- Every key figure must have one explicit takeaway sentence.

## 7. Reusable TeX Templates

### 7.1 Single-Figure Slide
```tex
\begin{frame}{Topic Overview}
  \begin{figure}
    \centering
    \includegraphics[width=0.82\linewidth]{fig/topic/fig-main.pdf}
    \caption{Comparison under different settings}
  \end{figure}
\end{frame}
```

### 7.2 Side-by-Side Figures
```tex
\begin{frame}{Comparative View}
  \begin{columns}[T]
    \column{0.49\textwidth}
      \centering
      \includegraphics[width=\linewidth]{fig/topic/fig-a.pdf}
      \vspace{2mm}
      {\scriptsize (a) Condition A}
    \column{0.49\textwidth}
      \centering
      \includegraphics[width=\linewidth]{fig/topic/fig-b.pdf}
      \vspace{2mm}
      {\scriptsize (b) Condition B}
  \end{columns}
\end{frame}
```

### 7.3 Wide Figure That Looks Off-Center
```tex
\begin{frame}{Process Overview}
  \centering
  \makebox[\linewidth][c]{\includegraphics[width=0.82\linewidth,height=0.48\textheight,keepaspectratio]{fig/topic/fig-wide.pdf}}\par
  \vspace{0.05cm}
  {\scriptsize Wide figure showing the key trend}
\end{frame}
```

## 8. Caption and Figure-Speaking Rules

### 8.1 Caption Numbering Rule
- If your template auto-generates “Figure X”, do not manually write “Figure X:” in `\caption{...}`.
- Recommended: `\caption{Timeline gain in key stages}`
- Not recommended: `\caption{Figure 3: Timeline gain in key stages}`

### 8.2 Caption Information Structure
- Pattern: **object + metric/dimension + usage**
- Example: `Latency breakdown and sample proportion under different input scales (used for evaluation workload construction)`

### 8.3 Figure-speaking Sentence Pattern
- State conclusion first, then mechanism:
  - `Conclusion: this figure shows XX. Mechanism: YY leads to ZZ.`

## 9. Frequent Issues and Fixes
- Not centered: use `\centering`; if still visually off, wrap with `\makebox[\linewidth][c]{...}`.
- Distorted ratio: set only `width` or only `height`; if both are set, add `keepaspectratio`.
- Duplicated numbering: remove manual “Figure X” from caption.
- Unclear meaning: add variables and usage context in caption.
- Overlap or crowding: reduce image width, add `\vspace`, shorten caption text.
- Slow compile or memory pressure: compress oversized PNG files, prefer PDF.
- Output PDF locked: compile to a temporary jobname first (for example `-jobname=slides_tmp`).

## 10. Source TeX to Slide TeX (Figure Extraction by Appearance Order)
- Inputs:
  - Main file: `source.tex`
  - Section files: `sections/*.tex`
  - Figure directory: `fig/*.pdf`
- Extraction:
  - Read `\input{sections/...}` order from `source.tex`
  - Extract `\includegraphics{fig/...}` line-by-line in each section file
  - Deduplicate to get the figure appearance list
- Landing:
  - Copy source figures into `fig/topic`
  - Place figures in `slides.tex` by speaking logic, not rigid source order
  - Add one takeaway sentence per slide

## 11. Duration and Personalization Handling
- If talk duration is unknown, always ask first: `How many minutes is the presentation?`
- Then adapt planning:
  - Short: keep storyline and key figures only
  - Medium: storyline + key methods + main experiments
  - Long: full coverage + extended discussion + Q&A prep
- Store custom requirements using the `presentation-personalizer` skill.
- Invoke the `presentation-personalizer` skill to append new special requirements before regenerating outline and script.

## 12. Output Requirements
- Do not produce rehearsal scripts.
- Produce a directly deliverable speech script.
- Always provide macro structure first, then page-level script.

## 13. Final Delivery Checklist
- All figures compile and paths are valid
- All figures are visually centered and not stretched
- Caption style is consistent and has no duplicated numbering
- Every key figure has one takeaway sentence
- Side-by-side pages have balanced spacing and font size
- Storyline follows Motivation -> Method -> Evaluation -> Conclusion
- Section-by-section coverage check is completed
- Duration has been confirmed and script length matches it