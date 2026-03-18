# Qwen (qwen-code) — Harness Reference

**Docs:** https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/
**Repo:** https://github.com/QwenLM/qwen-code

## Skill placement (Linux)

| Scope | Path |
|---|---|
| Project | `.qwen/skills/<name>/SKILL.md` |
| Personal (global) | `~/.qwen/skills/<name>/SKILL.md` |
| Extension-provided | `skills/` within an installed extension package |

## Frontmatter fields

Only `name` and `description` are documented. Base spec fields are safe to include.

| Field | Required | Constraints |
|---|---|---|
| `name` | Yes | Lowercase letters, numbers, hyphens; non-empty |
| `description` | Yes | Non-empty; should describe both *what* and *when* |

**Fields not supported:** `model`, `allowed-tools`, `disable-model-invocation`, `user-invocable`, `context`, `agent`, `hooks`.

## Slash command setup

Qwen uses a **prefix syntax** unique among all harnesses:

```
/skills <skill-name>
```

Not `/skill-name` — the literal word `skills` precedes the name.

The model can also invoke skills autonomously when requests match the description, without the `/skills` prefix.

## Multi-file skill structure

Qwen explicitly documents supporting files within a skill directory:

```text
my-skill/
├── SKILL.md
├── scripts/
│   └── helper.py       ← utility scripts
└── templates/
    └── template.txt    ← reusable templates
```

Files in these subdirectories are referenced from `SKILL.md` via relative paths and loaded on demand.

## Questions to ask the user

When targeting Qwen specifically, ask:

1. **Invocation:** Users invoke via `/skills <name>` (not `/<name>`). Is the user aware of this syntax difference?
2. **Supporting files:** Will this skill include helper scripts or templates? (Use `scripts/` and `templates/` subdirectories.)
3. **Scope:** Personal global (`~/.qwen/skills/`) or project-specific (`.qwen/skills/`)?

## Notable constraints and quirks

- The `/skills <name>` invocation syntax is unique — users coming from other harnesses may attempt `/<name>` and find it doesn't work.
- Extension skills (provided by installable extensions) are a distinct third category alongside global and project-local. If distributing a skill as part of a qwen extension, the packaging differs from a standalone skill directory.
- Only `.qwen/skills/` is scanned — unlike Warp or OpenCode, Qwen does not scan other tools' directories (`.claude/`, `.agents/`, etc.).
