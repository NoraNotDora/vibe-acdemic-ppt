---
name: "academic-ppt-planner"
description: "Plan academic paper presentation slides from a paper PDF and course requirements. Use when starting a new academic PPT, refining slide requirements, mapping figures to pages, or turning a paper into a page-level outline before TeX drafting."
---

# Academic PPT Planner

Use this skill to turn a paper and its constraints into a page-level presentation plan before anyone starts writing TeX.

## When to Trigger
- The user is starting a new academic PPT.
- The user wants slide pages outlined from a paper PDF or draft notes.
- The user needs duration, audience, or page-budget decisions before slide writing.
- The user asks how to map paper figures, sections, or claims into a presentation.

## Mandatory First Step
Before you outline slides, always output:
- Presentation goal in one sentence
- Target audience
- Duration and page constraints
- Core paper contributions (3-5 items)
- Must-cover figure list
- Risk list (formula density, unreadable figures, page overflow)

If duration or audience is missing, ask for it directly instead of guessing. The page budget and figure strategy depend on those constraints.

## Inputs to Inspect
- Paper PDF
- Course requirements or instructor notes
- Existing outline, if any
- Extracted figure files
- `skills/presentation_personalization_requirements.md`
- `skills/ppt_plan_template.md`

## Planning Workflow
1. Read the paper structure, section titles, key claims, and figure IDs.
2. Refine the requirements before drafting slides.
3. Build the storyline as problem -> method -> result -> conclusion.
4. Write a page-level outline with a page title, speaking goal, and one visual anchor for every page.
5. Map each key figure to a page and write one sentence explaining why it belongs there.
6. Identify unfamiliar terms early and mark where a concept-bridge slide or plain-language annotation is needed.
7. Record the slide-level risks: formula density, unreadable figures, page overflow, or missing evidence.
8. Draft the TeX skeleton and bibliography only after the outline is stable.
9. Hand off to `tex-ppt-structuring` for figure placement and to `tex-builder` for compile troubleshooting.

## Output Expectations
- A requirement-refinement summary
- A page-by-page outline
- A figure-to-page map
- A short risk list
- A draft-ready TeX plan, not a final speech script
