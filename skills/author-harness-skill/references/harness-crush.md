# Crush — Harness Reference

**Docs / Repo:** https://github.com/charmbracelet/crush

Note: Crush has no separate documentation site. All documentation is in the GitHub README.

## Skill placement (Linux)

| Scope | Path |
|---|---|
| Default global | `~/.config/crush/skills/<name>/SKILL.md` |
| Custom (env var) | `$CRUSH_SKILLS_DIR/<name>/SKILL.md` |
| Custom (config) | Any path listed in `options.skills_paths` in `crush.json` |

Config file location: `~/.config/crush/crush.json`

### Multiple skill directories via config

```json
{
  "options": {
    "skills_paths": [
      "~/.config/crush/skills",
      "./project-skills",
      "/shared/team-skills"
    ]
  }
}
```

### Full directory override via environment variable

```bash
export CRUSH_SKILLS_DIR=/path/to/skills
crush
```

This overrides the default directory entirely. Useful for testing or environment-specific skill sets.

## Frontmatter fields

Crush follows the base Agent Skills spec. No Crush-specific extensions are documented.

| Field | Required |
|---|---|
| `name` | Yes |
| `description` | Yes |
| `license` | No |
| `compatibility` | No |
| `metadata` | No |

## Slash command setup

`/<name>` slash commands work automatically. Skills can also be auto-invoked when the agent detects a relevant task.

No additional configuration is required for slash commands beyond the `name` field.

## Questions to ask the user

When targeting Crush specifically, ask:

1. **Directory:** Default (`~/.config/crush/skills/`) or a custom path via `CRUSH_SKILLS_DIR` or `crush.json`?
2. **Slash command:** Do you want explicit `/<name>` invocation, or rely on auto-invocation? (Both work by default; no config needed.)

## Notable constraints and quirks

- `CRUSH_SKILLS_DIR` env var provides a full directory override — unique among researched harnesses.
- `options.skills_paths` array in `crush.json` allows multiple skill directories without env var management.
- Crush is a terminal application (built by Charmbracelet); skill interactions happen in the terminal.
- Documentation is entirely in the GitHub README — when in doubt, check the repo directly.
- Follows the base spec closely with no proprietary extensions, making Crush the most straightforward harness to target.
