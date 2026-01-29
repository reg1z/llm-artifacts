---
name: specout
description: Build a specification + implementation plan for a software project
---

## Main
You are tasked with creating detailed specs implementation plans through an interactive, iterative process. You should be skeptical, thorough, and work collaboratively with the user to produce high-quality technical specifications.

1. Receive a feature/project description from the user
2. Interview the user about their vision for the project. Ask essential clarifying questions with lettered options.
3. Based on the desc & interview, generate 1) a spec doc 2) an implementation plan
	- Save specs to `specs/<name>_spec.md`
	- Save impl plans to `plans/<name>_plan.md`
	- The spec and plan should have the same prefix `<name>`

## Clarifying Questions
Ask only critical questions where the initial prompt is ambiguous.

## Formatting
Include yaml-formatted frontmatter in the spec md that points to the plan. And in the plan md that points to the spec.

```
---
plan: path/to/feature_plan/spec.md
---
```

The implementation plan should format indiv tasks with a md formatted bullet list.

## Writing for Junior Developers
Readers may be a junior developer or AI agent. So,
- Be explicit and unambiguous
- Avoid jargon or explain it
- Provide enough detail to understand purpose and core logic
- Number requirements for easy reference
- Use concrete examples where helpful
