# OpenAI Codex — Harness Reference

**Docs:** https://developers.openai.com/codex/skills
**Repo:** https://github.com/openai/codex
**Skills catalog:** https://github.com/openai/skills

## Skill placement (Linux)

| Scope | Path |
|---|---|
| Project (recommended) | `.agents/skills/<name>/SKILL.md` |
| Repo root | `$REPO_ROOT/.agents/skills/<name>/SKILL.md` |
| Personal (global) | `$HOME/.agents/skills/<name>/SKILL.md` |
| System-wide | `/etc/codex/skills/<name>/SKILL.md` |

Codex also follows symlinked skill folders.

## Frontmatter fields

### In SKILL.md

| Field | Required | Notes |
|---|---|---|
| `name` | Yes | Standard base spec rules |
| `description` | Yes | Codex uses this for both matching and the "exactly when to trigger" decision |

### Optional OpenAI sidecar: `agents/openai.yaml`

Codex supports an additional sidecar file at `agents/openai.yaml` (relative to the skill directory) for display metadata and MCP tool declarations. This file is **Codex-specific** and ignored by all other harnesses.

```yaml
interface:
  display_name: "My Skill"
  short_description: "One-liner for the UI"
  icon_small: assets/icon-16.png
  icon_large: assets/icon-64.png
  brand_color: "#3B82F6"
  default_prompt: "Run the skill"

policy:
  allow_implicit_invocation: true   # false = explicit invocation only

dependencies:
  tools:
    - name: my-mcp-server
      type: mcp
```

## Slash command setup

Skills are invoked via:
- `$skill-name` mention syntax in prompts
- The `/skills` command for browsing
- `$skill-installer <name>` to install from the catalog

**No slash-command-specific config is needed** — implicit invocation is on by default. To disable auto-invocation, set `policy.allow_implicit_invocation: false` in the sidecar.

## Per-path disable

Users can disable a specific skill for a path in `~/.codex/config.toml`:

```toml
[[skills.config]]
path = "/path/to/skill/SKILL.md"
enabled = false
```

## Questions to ask the user

When targeting OpenAI Codex specifically, ask:

1. **Display metadata:** Should this skill have a custom display name, icon, or brand color in the Codex UI? (Requires `agents/openai.yaml`)
2. **MCP tools:** Does this skill depend on any MCP servers? If so, provide names/types for the sidecar.
3. **Implicit invocation:** Should Codex auto-activate this skill when relevant, or should users invoke it explicitly? (Default: auto)

## Notable constraints and quirks

- The `agents/openai.yaml` sidecar is the only harness-specific extra file format among all researched harnesses. Create it only if the user needs display customization or MCP tool declarations.
- Codex skill categories: `.system` (auto-installed), `.curated` (installable via `$skill-installer`), `.experimental`. If distributing publicly, plan which tier applies.
- `$skill-creator` (a bundled Codex skill) can be used to auto-generate skills interactively within Codex itself — worth mentioning to users.
