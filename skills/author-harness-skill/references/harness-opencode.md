# OpenCode — Harness Reference

**Docs:** https://opencode.ai/docs/skills/
**Repo:** https://github.com/sst/opencode

## Skill placement (Linux)

OpenCode searches from CWD up through the git worktree root. Multiple directory conventions are scanned simultaneously.

| Scope | Paths scanned |
|---|---|
| Project | `.opencode/skills/<name>/SKILL.md` |
| Project (compat) | `.claude/skills/<name>/SKILL.md` |
| Project (compat) | `.agents/skills/<name>/SKILL.md` |
| Global | `~/.config/opencode/skills/<name>/SKILL.md` |
| Global (compat) | `~/.claude/skills/<name>/SKILL.md` |
| Global (compat) | `~/.agents/skills/<name>/SKILL.md` |

**Recommended:** use `.agents/skills/<name>/` for portability across harnesses.

## Frontmatter fields

OpenCode recognizes only these fields; all others are silently ignored.

| Field | Required | Constraints |
|---|---|---|
| `name` | Yes | Pattern: `^[a-z0-9]+(-[a-z0-9]+)*$`; 1–64 chars; must match directory name |
| `description` | Yes | 1–1024 chars |
| `license` | No | License name or bundled file reference |
| `compatibility` | No | Environment requirements |
| `metadata` | No | Arbitrary key-value pairs |

**Fields not supported:** `model`, `allowed-tools`, `disable-model-invocation`, `user-invocable`, `context`, `agent`, `hooks`.

## Name validation

The `name` field pattern is stricter than the base spec:
- Only lowercase alphanumeric and single hyphens
- No leading or trailing hyphens
- No consecutive hyphens
- Must exactly match the containing directory name
- For symlinks: must match the **symlink name**, not the target directory name

## Slash command / invocation

OpenCode does **not** expose skills as user-facing slash commands. Skills are invoked internally via the `skill({ name: "skill-name" })` tool call. There is no `/` prefix syntax.

If the user wants a slash command in OpenCode, it must be created as a **separate commands file**:

```text
.opencode/
├── skills/
│   └── my-skill/
│       └── SKILL.md
└── commands/
    └── my-skill.md    ← slash command definition
```

The commands file follows a simpler format (plain markdown prompt, no frontmatter required). The slash command name matches the filename.

## Questions to ask the user

When targeting OpenCode specifically, ask:

1. **Slash command:** Do you want this skill to also be available as a slash command (e.g. `/my-skill`)? If yes, a separate file needs to be created in `.opencode/commands/`.
2. **Directory convention:** Should this go in `.opencode/skills/` (OpenCode-native) or `.agents/skills/` (portable across harnesses)?

## Notable constraints and quirks

- OpenCode silently ignores unknown frontmatter fields — Claude Code-specific fields (`model`, `allowed-tools`, `hooks`, etc.) won't cause errors but won't do anything.
- The search walks up from CWD to git worktree root, so skills in parent directories are automatically discovered.
- OpenCode's cross-harness directory compatibility (scanning `.opencode/`, `.claude/`, `.agents/`) makes it easy to share a single skill file with other tools.
