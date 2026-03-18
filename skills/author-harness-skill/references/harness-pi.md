# pi — Harness Reference

**Docs:** https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md
**Repo:** https://github.com/badlogic/pi-mono
**Skills collection:** https://github.com/badlogic/pi-skills

## Skill placement (Linux)

| Scope | Path |
|---|---|
| Project | `.pi/skills/<name>/SKILL.md` |
| Project (portable) | `.agents/skills/<name>/SKILL.md` |
| Global | `~/.pi/agent/skills/<name>/SKILL.md` |
| Global (portable) | `~/.agents/skills/<name>/SKILL.md` |

Additional sources:
- `pi.skills` entries in `package.json` (npm distribution)
- `settings.json` `"skills"` array (explicit paths)
- `--skill <path>` CLI flag (one-off injection)

Pi searches from CWD upward to the repo root, discovering skills in any parent directory's `.pi/skills/` or `.agents/skills/`.

## Frontmatter fields

| Field | Required | Constraints |
|---|---|---|
| `name` | Yes | Max 64 chars; lowercase, hyphens; must match parent directory name |
| `description` | Yes | Max 1024 chars |
| `license` | No | — |
| `compatibility` | No | Max 500 chars |
| `metadata` | No | Key-value mapping |
| `allowed-tools` | No | Space-delimited (experimental) |
| `disable-model-invocation` | No | `true` = hides skill from system prompt entirely |

**No `model` field** — pi does not support per-skill model overrides.

## Slash command setup

Pi uses a **colon-separated** syntax: `/skill:<name>` (not `/<name>` like most harnesses).

Requirements:
1. Add to `settings.json`:
   ```json
   { "enableSkillCommands": true }
   ```
2. Invoke: `/skill:my-skill` or with arguments: `/skill:my-skill some args here`

The `/reload` command hot-reloads all skills without restarting pi.

Auto-invocation also works: if the model recognizes a task matches the skill, it loads automatically. The docs note: "use prompting or `/skill:name` to force it" if auto-invocation doesn't trigger.

## npm / package.json distribution

Pi uniquely supports skill distribution via npm packages. To declare skills in a package:

```json
{
  "pi": {
    "skills": ["./skills/my-skill"]
  }
}
```

When this package is installed in a project, pi discovers the skill automatically.

## One-off skill injection

```bash
pi --skill /path/to/my-skill --skill /path/to/another
# Combine with --no-skills to disable defaults:
pi --no-skills --skill /path/to/my-skill
```

## Questions to ask the user

When targeting pi specifically, ask:

1. **Slash command:** Do you want this skill accessible as `/skill:<name>`? (Requires `enableSkillCommands: true` in settings.json)
2. **Distribution method:** Is this for personal/project use, or will it be distributed as an npm package?
3. **Model invocation:** Should pi auto-load this skill when relevant, or only when explicitly invoked? (`disable-model-invocation`)

## Notable constraints and quirks

- The `/skill:<name>` colon syntax is unique to pi — different from all other harnesses.
- `disable-model-invocation: true` completely hides the skill from the system prompt, preventing auto-invocation.
- Hot reload via `/reload` is unique to pi (no restart needed).
- No `model` field — per-skill model selection is not supported.
- `package.json` distribution via `pi.skills` is unique to pi.
