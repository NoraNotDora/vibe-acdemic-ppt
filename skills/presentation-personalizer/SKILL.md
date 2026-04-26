---
name: "presentation-personalizer"
description: "Maintain persistent presentation requirements before generating or regenerating an academic PPT or speech script. Use whenever duration, audience, output format, figure strategy, or style constraints change, or when a prior deck needs to be updated with new preferences. Trigger this skill before drafting so the next step can use the current requirements without guessing."
---

# Presentation Personalizer

Use this skill to keep presentation preferences in one place so future outlines and scripts stay consistent.

## When to Trigger
- The user is about to generate a new PPT or speech script.
- The deck is being revised and requirements changed.
- The talk duration is missing or changed.
- The audience, focus, figure strategy, or output format changed.
- The user wants a persistent record of presentation preferences.

## Source of Truth
- `skills/presentation_personalization_requirements.md`

## Workflow
1. Read the active requirements first.
2. If duration is unknown, ask for it before any outline or script work.
3. Confirm each changed requirement separately when the user is updating several things at once.
4. Preserve unspecified requirements; update only what changed.
5. Append new requirements under Requirement History with a date and a short reason.
6. If requirements conflict, keep the newest entry and record the override note.
7. Return a concise summary of the active requirements so the next skill can use them immediately.

## Confirmation Habit
- Treat requirement updates as a sequence, not a single bulk edit.
- Ask one focused question when the answer changes the next slide or script decision.
- Confirm audience, duration, figure strategy, and delivery style in that order when they are all still open.
- If the user gives a partial answer, keep the unanswered items open instead of inferring them.

## Keep These Active Checks in Mind
- Presentation perspective should stay aligned with problem -> method -> evaluation -> conclusion unless the user overrides it.
- Uncommon core concepts should be explained in plain language for the audience.
- Figure strategy should prioritize source figures, visual anchors, and logical placement.
- The user experience should feel checked step by step, not assumed.
- The output should remain a direct speech script, not a rehearsal script.

## Output
- An updated requirement block or summary
- A note about any overrides or open questions
