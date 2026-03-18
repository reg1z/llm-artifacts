# KiloCode — Harness Reference

**Docs:** https://kilo.ai/docs/customize/skills#skills
**Repo:** https://github.com/Kilo-Org/kilocode

## Skill placement (Linux)

| Scope | Path |
|---|---|
| Project (all modes) | `.kilocode/skills/<name>/SKILL.md` |
| Project (mode-specific) | `.kilocode/skills-<mode>/<name>/SKILL.md` |
| Global (all modes) | `~/.kilocode/skills/<name>/SKILL.md` |
| Global (mode-specific) | `~/.kilocode/skills-<mode>/<name>/SKILL.md` |

Mode slugs: `code`, `architect`, `ask`, `debug`.

**Important:** Skills are discovered at VSCode startup. After creating or modifying a skill, the user must reload VSCode (Cmd/Ctrl+Shift+P → "Reload Window").

## Frontmatter fields

| Field | Required | Constraints |
|---|---|---|
| `name` | Yes | Max 64 chars; lowercase, hyphens; must exactly match parent directory name |
| `description` | Yes | Max 1024 chars |
| `license` | No | — |
| `compatibility` | No | — |
| `metadata` | No | Key-value mapping |

**Fields not supported:** `model`, `allowed-tools`, `disable-model-invocation`, `user-invocable`, `context`, `agent`, `hooks`.

## Slash command / invocation

KiloCode does **not** support slash command invocation. Skill activation is driven entirely by LLM evaluation against the skill description — not keyword matching. The better the description, the more reliably the skill activates.

There is no user-facing mechanism to force a specific skill to load.

## Mode-specific placement

KiloCode's `skills-{mode}/` directories are unique: skills placed here only activate when the user is in the matching agent mode.

| Directory | When active |
|---|---|
| `skills-code/` | Code mode (editing, implementation) |
| `skills-architect/` | Architect mode (planning, design) |
| `skills-ask/` | Ask mode (Q&A, explanation) |
| `skills-debug/` | Debug mode (troubleshooting) |

Use mode-specific placement when a skill is only relevant in a particular context (e.g. a deployment skill only in `code` mode).

## Questions to ask the user

When targeting KiloCode specifically, ask:

1. **Mode scope:** Should this skill be available in all KiloCode modes, or only a specific mode (code / architect / ask / debug)?
2. **Description quality:** KiloCode relies entirely on LLM description matching — review the description carefully to ensure it clearly describes when the skill should activate.

## Notable constraints and quirks

- No live reload: the user must reload VSCode after adding or modifying skills.
- `name` must exactly match the parent directory name — symlinks must match the symlink name, not the target.
- KiloCode is a VSCode extension; skills are only active within the VSCode environment.
- No slash commands at all — if the user needs command-style invocation, KiloCode is not the right harness for that use case.
