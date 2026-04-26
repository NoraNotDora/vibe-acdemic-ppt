---
name: "natural-academic-language"
description: "Rewrite academic slide text, speaker notes, captions, and translations in natural, concise language while preserving standard technical terms. Use when the user wants to reduce AI-like wording, remove stiff phrasing, or decide whether a domain term should stay in English or be translated based on common usage."
---

# Natural Academic Language

Use this skill when slide text, speaker notes, or translations need to sound more natural without losing technical accuracy.

## When to Trigger
- The user wants to remove AI-like wording from a PPT, script, abstract, or caption.
- The user asks whether a technical term should be translated, kept in English, or rewritten more naturally.
- The user wants slide text to sound concise, human, and presentation-ready.
- The user is polishing wording after the content and layout are already set.

## Workflow
1. Identify the audience and the purpose of the text before rewriting it.
2. Check the terminology first.
   - If a term is a proper noun, dataset name, model name, method name, or standard abbreviation, preserve the established form.
   - If the term appears frequently in the field, prefer the dominant published usage over a literal rewrite.
   - If the field uses mixed wording, choose the version that is most natural for the intended audience and keep it consistent.
   - When the usage is uncertain, check recent papers, official docs, or other reliable field sources before deciding whether to keep, translate, or transliterate the term.
3. Rewrite the sentence with plain, direct academic language.
   - Prefer short sentences over stacked clauses.
   - Avoid overusing hyphens, quotation marks, and parentheses as a style crutch.
   - Keep punctuation simple unless the meaning truly depends on the extra mark.
   - Remove template-like phrases that do not add meaning.
4. Choose translation style by usage.
   - Use direct translation when the target language has a stable technical equivalent.
   - Use semantic translation when literal translation sounds awkward or unnatural.
   - Keep the original term when it is the recognized field standard.
   - Prefer the translation that matches common field usage, not the one that only looks closest word-for-word.
5. Check the rewritten text from a reader's point of view.
   - If it still sounds machine-made, make it more specific and less generic.
   - If the wording feels heavy, simplify it again before changing the meaning.

## Output Expectations
- Provide a polished version of the text.
- Briefly note any terms that were preserved in the original language.
- Briefly note any translation choices that depended on field usage.
