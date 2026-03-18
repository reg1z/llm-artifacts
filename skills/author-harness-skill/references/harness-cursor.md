# Cursor — Harness Reference

**Docs:** https://cursor.com/docs/skills
**Open standard:** https://github.com/agentskills/agentskills

## Skill placement (Linux)

| Scope | Path (priority order) |
|---|---|
| Project (recommended) | `.agents/skills/<name>/SKILL.md` |
| Project (Cursor-native) | `.cursor/skills/<name>/SKILL.md` |
| Global | `~/.cursor/skills/<name>/SKILL.md` |
| Project (compat) | `.claude/skills/<name>/SKILL.md` |
| Project (compat) | `.codex/skills/<name>/SKILL.md` |
| Global (compat) | `~/.claude/skills/<name>/SKILL.md` |
| Global (compat) | `~/.codex/skills/<name>/SKILL.md` |

## Frontmatter fields

| Field | Required | Notes |
|---|---|---|
| `name` | Yes | Standard base spec rules |
| `description` | Yes | Standard base spec rules |
| `license` | No | — |
| `compatibility` | No | — |
| `metadata` | No | Key-value pairs |
| `disable-model-invocation` | No | `true` = slash-command only |

**Fields not supported:** `model`, `allowed-tools`, `user-invocable`, `context`, `agent`, `hooks`.

## Slash command setup

Type `/` in Cursor's Agent chat and search by skill name. The `name` field becomes the command.

`disable-model-invocation: true` makes the skill function as a traditional slash command — Cursor will not auto-activate it, only respond to explicit `/name` invocation.

### Migrating existing rules to skills

Cursor ships a built-in `/migrate-to-skills` command that converts existing `.cursorrules` and Cursor rule files to the skills format. Mention this to users who are transitioning.

## Questions to ask the user

When targeting Cursor specifically, ask:

1. **Slash command:** Should this be user-invocable as `/name` in Agent chat, or only auto-activated by the model?
2. **Directory preference:** `.cursor/skills/` (Cursor-native) or `.agents/skills/` (portable)?
3. **Migrating rules:** Are you converting an existing Cursor rule? If so, `/migrate-to-skills` may handle this automatically.

## Notable constraints and quirks

- Progressive loading is documented: metadata always visible to the model, full body loads on demand.
- Backward compatibility scanning of `.claude/skills/` and `.codex/skills/` means skills from other tools are automatically picked up.
- Cursor is a GUI editor; skills appear in the Agent chat panel, not a terminal.
- `disable-model-invocation: true` is supported — use it for skills that should only be triggered manually.
