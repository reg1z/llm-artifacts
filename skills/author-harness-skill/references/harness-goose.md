# goose — Harness Reference

**Docs:** https://block.github.io/goose/docs/guides/context-engineering/using-skills
**Repo:** https://github.com/block/goose

## Skill placement (Linux)

Goose documents an explicit six-level priority order:

| Priority | Path |
|---|---|
| 1 (highest) | `~/.claude/skills/<name>/SKILL.md` |
| 2 | `~/.config/agents/skills/<name>/SKILL.md` |
| 3 | `~/.config/goose/skills/<name>/SKILL.md` |
| 4 | `./.claude/skills/<name>/SKILL.md` |
| 5 | `./.goose/skills/<name>/SKILL.md` |
| 6 (lowest) | `./.agents/skills/<name>/SKILL.md` |

**Recommended:** `.agents/skills/<name>/` for portability, `.goose/skills/<name>/` for goose-specific project skills, `~/.config/goose/skills/<name>/` for goose-specific global skills.

## Frontmatter fields

Only `name` and `description` are documented. Base spec fields are safe to include.

| Field | Required |
|---|---|
| `name` | Yes |
| `description` | Yes |

**Fields not supported:** `model`, `allowed-tools`, `disable-model-invocation`, `user-invocable`, `context`, `agent`, `hooks`.

## Slash command / invocation

Goose does **not** document slash command support for skills. Skills activate when:
- A request clearly matches the skill's description
- The user explicitly says "Use the [skill-name] skill"

## Supporting files

Skills can include scripts, templates, and configuration files. However, these are only accessible through goose's **Developer extension's file tools**. If the skill relies on supporting files, ensure the Developer extension is enabled.

## Questions to ask the user

When targeting goose specifically, ask:

1. **Scope:** Global (`~/.config/goose/skills/`) or project-local (`.goose/skills/`)?
2. **Developer extension:** Does this skill reference supporting files (scripts, templates)? If so, confirm the Developer extension is enabled.
3. **Cross-harness sharing:** goose scans `~/.claude/skills/` with the highest priority — if the user also uses Claude Code, placing the skill there makes it available in both.

## Notable constraints and quirks

- `~/.claude/skills/` has the **highest** priority in goose — skills placed there for Claude Code are automatically picked up by goose.
- The Developer extension is required to access files in `scripts/` or other subdirectories.
- No slash commands documented.
- Priority order is explicitly documented — useful when debugging why a skill isn't activating as expected.
