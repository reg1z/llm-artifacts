---
name: lang-explain
description: Concisely describe the core fundamentals of a specific coding/programming language
---

## Important
- Take this step by step
- Use [[template]] for output structure. Use the context within this template to determine relevant info.
- Provide a markdown file with your output once finished.

### Scope
- Focus on syntax and semantics, not tutorials
- Target: developers familiar with at least one other language
- Length: ~1000-1500 words. Keep things as brief as is possible to fit necessary information. Optimized for skimming. Almost like a cheat sheet.

### Conventions
If a common convention of the lang is encountered while explaining, be sure to BRIEFLY let the user know about it. A common convention is one that is likely to be encountered frequently in other codebases.

### Fit the template
- If a lang doesn't fit well into the template, categorize the concepts of the language in a similar format that maintains logical consistency with it.

### Code Examples
Include snippets SPARINGLY. Use minimal (1-5 lines), illustrative examples for:
- All code snippets use triple tickmarked blocks for syntax highlighting
- Basic syntax demonstration
- Unique language features
- Common gotchas/pitfalls

### Handling Edge Cases
- If language lacks a feature (e.g., no classes), note this briefly
- For multi-paradigm languages, cover all supported paradigms
- For languages with major version differences, specify version


## To consider
- Syntax for implementing interfaces
- Multiple assignment (e.g. python's mult. assignment `a, b = b, a+b`)
- 