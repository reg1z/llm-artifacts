# amp — Harness Reference

**Docs:** https://ampcode.com/manual#agent-skills
**Community skills:** https://github.com/ampcode/amp-contrib

## Skill placement (Linux)

| Scope | Path (priority order, highest first) |
|---|---|
| Global | `~/.config/agents/skills/<name>/SKILL.md` |
| Global (amp-specific) | `~/.config/amp/skills/<name>/SKILL.md` |
| Project | `.agents/skills/<name>/SKILL.md` |
| Project (compat) | `.claude/skills/<name>/SKILL.md` |
| Global (compat) | `~/.claude/skills/<name>/SKILL.md` |

**Recommended:** `.agents/skills/<name>/` for portability; `~/.config/amp/skills/<name>/` for amp-specific global skills.

## Frontmatter fields

Only `name` and `description` are documented. Base spec fields (`license`, `compatibility`, `metadata`) are safe to include.

| Field | Required |
|---|---|
| `name` | Yes |
| `description` | Yes |

**Fields not supported:** `model`, `allowed-tools`, `disable-model-invocation`, `user-invocable`, `context`, `agent`, `hooks`.

## Slash command / invocation

Amp does **not** expose skills as `/` slash commands. Skills are managed via the command palette or CLI:

| Command | Effect |
|---|---|
| `skill: add` | Install from GitHub, git URL, or local path |
| `skill: list` | View installed skills |
| `skill: remove` | Remove a skill |

Install example:
```bash
amp skill add ampcode/amp-contrib/tmux
amp skill add github.com/myorg/myrepo/my-skill
amp skill add /local/path/to/skill
```

## MCP server bundling

Amp uniquely supports bundling MCP servers within a skill directory via an `mcp.json` file. This is documented as "the recommended way to use MCP servers" in Amp.

```json
{
  "servers": {
    "my-server": {
      "command": "node",
      "args": ["server.js"],
      "env": { "API_KEY": "..." }
    }
  }
}
```

For remote servers:
```json
{
  "servers": {
    "my-remote": {
      "url": "https://example.com/mcp",
      "headers": { "Authorization": "Bearer ..." },
      "includeTools": ["tool-one", "tool-two*"]
    }
  }
}
```

Behavior: MCP servers start when Amp launches, but their tools remain hidden from the model until the skill is loaded.

## Built-in skill generation

Amp ships a built-in `building-skills` skill. Prompting Amp with "Create a skill for X" triggers it to generate a tailored skill automatically. This is useful to mention to users who want to iterate within Amp itself.

## Questions to ask the user

When targeting amp specifically, ask:

1. **MCP tools:** Does this skill require any external MCP servers? If yes, create an `mcp.json` in the skill directory.
2. **Distribution:** Personal use (global `~/.config/amp/skills/`) or project-specific (`.agents/skills/`)?
3. **Install method:** Will this be installed via `amp skill add` from a GitHub repo, or placed manually?

## Notable constraints and quirks

- No slash commands at all — skills only activate via model matching.
- `mcp.json` bundling is unique to amp and not portable to other harnesses (other harnesses will ignore the file).
- `~/.config/agents/skills/` (note: `agents`, not `amp`) has the highest priority and is shared with other harnesses that scan that path.
