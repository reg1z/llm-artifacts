# Gemini CLI — Harness Reference

**Docs:** https://geminicli.com/docs/cli/skills/
**Repo:** https://github.com/google-gemini/gemini-cli

## Skill placement (Linux)

Gemini scans two directory conventions per scope; `.agents/skills/` takes priority over `.gemini/skills/` within each tier.

| Scope | Paths scanned (priority order) |
|---|---|
| Workspace | `.agents/skills/<name>/SKILL.md` (higher) |
| Workspace | `.gemini/skills/<name>/SKILL.md` (lower) |
| User/global | `~/.agents/skills/<name>/SKILL.md` (higher) |
| User/global | `~/.gemini/skills/<name>/SKILL.md` (lower) |
| Extension-bundled | `skills/` within installed extensions |

**Recommended:** `.agents/skills/<name>/` for portability. `.gemini/skills/<name>/` for Gemini-specific skills.

## Frontmatter fields

Only `name` and `description` are documented by Gemini CLI. Additional base spec fields (`license`, `compatibility`, `metadata`) should be safe to include but are not explicitly documented.

| Field | Required |
|---|---|
| `name` | Yes |
| `description` | Yes |

## Slash command / invocation

Gemini CLI exposes `/skills` as a **management command**, not a direct skill invocation:

| Command | Effect |
|---|---|
| `/skills list` | Display all discovered skills |
| `/skills link <path>` | Symlink a local skills directory |
| `/skills disable <name>` | Deactivate (default: user scope) |
| `/skills disable <name> --scope workspace` | Deactivate for project only |
| `/skills enable <name>` | Reactivate |
| `/skills reload` | Refresh discovery without restart |

CLI equivalents: `gemini skills list/link/install/uninstall/enable/disable`.

**Skills are not individually invocable via `/skill-name`** — they activate when Gemini matches a request to the skill's description, after a consent prompt.

## Consent prompt

When Gemini decides a skill is relevant, it shows a UI prompt to the user displaying the skill's purpose and directory access. The user must **approve** before the skill body loads. This is unique to Gemini CLI — other harnesses activate silently.

Write descriptions with the consent prompt in mind: the description is what the user sees when asked to approve. Make it clear and trust-building.

## `/skills link` for live editing

```bash
/skills link /path/to/my-skills-repo
# or
gemini skills link /path/to/my-skills-repo
```

This creates a symlink rather than copying, enabling live edits to the source directory without reinstalling.

## Questions to ask the user

When targeting Gemini CLI specifically, ask:

1. **Scope:** Should this skill be workspace-scoped (project) or user-scoped (global)?
2. **Directory preference:** `.agents/skills/` (portable) or `.gemini/skills/` (Gemini-native)?
3. **Consent prompt copy:** The skill description doubles as the consent prompt text shown to users before activation — should it be written with that in mind (clear, trust-building language)?

## Notable constraints and quirks

- The consent prompt at activation is unique to Gemini — users must explicitly approve each skill activation. This affects UX; descriptions should be written to reassure, not just match.
- Extension-bundled skills are a distribution tier not present in most other harnesses.
- `/skills reload` allows refreshing without restarting the CLI session.
