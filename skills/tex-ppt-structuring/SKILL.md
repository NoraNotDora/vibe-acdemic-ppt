---
name: "tex-ppt-structuring"
description: "Structure TeX academic slides, map paper figures to pages, and generate a directly deliverable speech script. Use when arranging figures, balancing slide density, revising a page from the audience's point of view, or turning a drafted outline into Beamer slides."
---

# TeX Academic PPT Structuring and Speech Script Skill

Use this skill after planning. It turns a paper outline into TeX slides that read clearly and compile cleanly.

## Scope
- Build or refine TeX-based academic slides
- Integrate figures, tables, and the minimum necessary math
- Generate a speech-ready script
- Fix layout imbalance, duplicate captions, and unreadable pages

## When to Trigger
- The outline is ready and TeX drafting should start.
- Figures need to be positioned by narrative logic.
- A slide feels too dense, too empty, or visually unbalanced.
- A direct speech script is needed from the approved slide order.

## Macro Workflow
1. Extract the section structure, key claims, and figure IDs from the paper or outline.
2. Build a coverage table: `section title -> mapped slide pages -> covered? -> evidence(page/figure) -> concept explained?`.
3. Build a figure map: `figure id -> meaning -> related section -> recommended placement -> takeaway sentence`.
4. Decide the layout before editing text.
   - Read each page from the audience's point of view and ask whether the main message is clear on first pass.
   - Prefer one visual anchor per page.
   - Keep 3-6 bullet points per page.
   - Avoid more than 2 major figures on a page.
   - Add a concept bridge slide or annotation when a term is likely unfamiliar.
5. Assign a size budget before placing figures.
   - Record the dominant visual, supporting text budget, and approximate width share.
6. Write one plain-language explanation for each key formula or definition.
7. Place figures in narrative order: background -> method -> evaluation -> conclusion.
8. Compile, inspect the log, and simplify any page with overflow, unreadable figures, or dense text.
9. Generate the final speech script from the approved page outline.

## Concept Bridge
- If a core term is central but unfamiliar, explain it before heavy use.
- Prefer one short definition or bridge sentence over a long paragraph.
- If the concept is important to the argument, make it visible in the outline instead of hiding it in a dense page.

## Figure Rules
- Use source figures whenever they support the argument directly.
- If the original figure is unavailable, draw an equivalent diagram instead of forcing a weak substitution.
- Put a short takeaway sentence immediately after each key figure.
- Keep captions short and avoid manually repeating figure numbers if the template already numbers them.
- Keep grouped figures together on the same page when they support one argument.
- Place figures in the section where the related claim is introduced, not where they merely fit visually.
- Match layout to aspect ratio and grouping:
  - Use top-bottom layout for wide figures when that keeps the slide readable.
  - Use left-right layout for tall figures when that keeps the slide readable.
  - Keep paired or comparative figures adjacent so the audience can compare them without hunting across pages.

## Layout Audit
After the first successful compile, run:

```powershell
python ..\tools\ppt_layout_audit.py --tex pre.tex --log pre.log
```

Treat warnings as a cue to simplify, resize, or split the page before finalizing.

## Useful TeX Patterns

### Single-Figure Slide
```tex
\begin{frame}{Topic Overview}
  \begin{figure}
    \centering
    \includegraphics[width=0.82\linewidth]{fig/topic/fig-main.pdf}
    \caption{Comparison under different settings}
  \end{figure}
\end{frame}
```

### Side-by-Side Figures
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

### Wide Figure That Looks Off-Center
```tex
\begin{frame}{Process Overview}
  \centering
  \makebox[\linewidth][c]{\includegraphics[width=0.82\linewidth,height=0.48\textheight,keepaspectratio]{fig/topic/fig-wide.pdf}}\par
  \vspace{0.05cm}
  {\scriptsize Wide figure showing the key trend}
\end{frame}
```

## Duration and Personalization Handling
- If talk duration is unknown, ask before you finalize page count.
- Short talk: keep storyline and key figures only.
- Medium talk: storyline + key methods + main experiments.
- Long talk: full coverage + extended discussion + Q&A prep.
- Use `presentation-personalizer` when requirements change midstream.
- If the wording feels too dense for a live talk, simplify it before adjusting the layout again.

## Output Requirements
- Do not produce rehearsal scripts.
- Produce a directly deliverable speech script.
- Always provide macro structure first, then page-level script.
- Keep each page to 3-6 points, one sentence per point.

## Final Delivery Checklist
- All figures compile and paths are valid
- All figures are visually centered and not stretched
- Caption style is consistent and has no duplicated numbering
- Every key figure has one takeaway sentence
- Side-by-side pages have balanced spacing and font size
- Uncommon core concepts are explained once in plain language
- Storyline follows Motivation -> Method -> Evaluation -> Conclusion
- Section-by-section coverage check is completed
- Duration has been confirmed and script length matches it
- Layout audit shows no critical overflow or imbalance warnings
