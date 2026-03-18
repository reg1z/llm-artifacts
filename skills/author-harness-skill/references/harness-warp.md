# Warp — Harness Reference

**Docs:** https://docs.warp.dev/agent-platform/capabilities/skills
**Skills collection:** https://github.com/warpdotdev/oz-skills

## Skill placement (Linux)

Warp scans more directories than any other harness. It scans up to the git repo root, picking up skills from any parent directory.

**Project-level** (any of these will be found):

| Path | Tool origin |
|---|---|
| `.agents/skills/<name>/SKILL.md` | Recommended / portable |
| `.warp/skills/<name>/SKILL.md` | Warp-native |
| `.claude/skills/<name>/SKILL.md` | Claude Code compat |
| `.codex/skills/<name>/SKILL.md` | Codex compat |
| `.cursor/skills/<name>/SKILL.md` | Cursor compat |
| `.gemini/skills/<name>/SKILL.md` | Gemini compat |
| `.copilot/skills/<name>/SKILL.md` | Copilot compat |
| `.factory/skills/<name>/SKILL.md` | Factory compat |
| `.github/skills/<name>/SKILL.md` | GitHub compat |
| `.opencode/skills/<name>/SKILL.md` | OpenCode compat |

**Global** (home-directory equivalents of all the above, e.g. `~/.agents/skills/`, `~/.warp/skills/`, etc.)

## Frontmatter fields

Only `name` and `description` are documented. Base spec fields are safe to include.

| Field | Required |
|---|---|
| `name` | Yes |
| `description` | Yes |

**Fields not supported:** `model`, `allowed-tools`, `disable-model-invocation`, `user-invocable`, `context`, `agent`, `hooks`.

## Slash command setup

`/<name>` invokes a skill directly. Additional context can be appended:

```
/deploy push the latest changes to staging
```

**Multi-match disambiguation:** If multiple skills share the same name (from different tool directories), Warp displays all matches with their descriptions and lets the user select. Give skills distinctive names to avoid this.

## Cross-tool sharing advantage

Warp's broad directory scanning means a single skill file in `.agents/skills/` is automatically available in Warp without any Warp-specific setup. This makes it ideal for teams that use multiple AI coding tools in the same repo.

## Questions to ask the user

When targeting Warp specifically, ask:

1. **Slash command:** Do you want this invocable as `/<name>` in Warp? (All discovered skills are automatically available as slash commands — no extra config needed.)
2. **Directory:** Should this go in `.warp/skills/` (Warp-specific) or `.agents/skills/` (cross-tool portable)?
3. **Name uniqueness:** Are there other harness skill directories in this repo? Ensure the skill name is unique to avoid disambiguation prompts.

## Notable constraints and quirks

- Warp is a **terminal application** — skill interactions happen in the terminal context, not a chat UI.
- Skills from any of the 10 supported tool directories are automatically slash-commandable — no per-harness config needed.
- Git repo traversal means skills in parent directories are discovered automatically — useful for monorepos.
- The disambiguation UI when names collide is unique to Warp.
