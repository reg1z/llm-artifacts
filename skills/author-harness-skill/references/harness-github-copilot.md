# GitHub Copilot — Harness Reference

**Docs (concepts):** https://docs.github.com/en/copilot/concepts/agents/about-agent-skills
**Docs (CLI):** https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-skills
**Docs (coding agent):** https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-skills
**Open standard:** https://github.com/agentskills/agentskills

## Skill placement (Linux)

| Scope | Path |
|---|---|
| Project | `.github/skills/<name>/SKILL.md` |
| Project (compat) | `.claude/skills/<name>/SKILL.md` |
| Personal (global) | `~/.copilot/skills/<name>/SKILL.md` |
| Personal (compat) | `~/.claude/skills/<name>/SKILL.md` |

**Note:** Copilot works across three surfaces — Copilot coding agent (GitHub.com), Copilot CLI, and VS Code agent mode. Skills placed in `.github/skills/` are available across all three.

## Frontmatter fields

| Field | Required | Notes |
|---|---|---|
| `name` | Yes | Lowercase, hyphens for spaces |
| `description` | Yes | Describes what and when |
| `license` | No | — |

**Fields not supported:** `model`, `allowed-tools`, `disable-model-invocation`, `user-invocable`, `context`, `agent`, `hooks`, `compatibility`, `metadata`.

## Slash command setup (CLI surface)

In the Copilot CLI, `/<name>` invokes the skill directly. Copilot CLI also provides extensive skill management commands:

| Command | Effect |
|---|---|
| `/skills list` | Display available skills |
| `/skills` | Enable/disable interactively |
| `/skills info` | View details and file locations |
| `/skills add` | Register alternative storage locations |
| `/skills reload` | Refresh without restarting CLI |
| `/skills remove SKILL-DIRECTORY` | Delete a skill |

The coding agent (GitHub.com) uses autonomous model-driven activation — no slash commands.

## MCP tool references in skill body

Copilot skills can reference MCP Server tool names directly in the Markdown body. When activated, Copilot calls those MCP tools as part of execution:

```markdown
## Checking CI status

Use `list_workflow_runs` to get recent runs, then `summarize_job_log_failures` to identify failures.
```

This is unique to Copilot CLI and works because Copilot has an MCP tool integration layer.

## Questions to ask the user

When targeting GitHub Copilot specifically, ask:

1. **Surface:** Is this for the coding agent (GitHub.com), Copilot CLI, or VS Code agent mode? (Or all three — `.github/skills/` covers all)
2. **Slash command:** Should this be user-invocable as `/<name>` in the CLI?
3. **MCP tools:** Does this skill orchestrate any MCP server tools? If so, reference them by name in the body.
4. **Distribution:** Should this be committed to the repo (`.github/skills/`) or personal global (`~/.copilot/skills/`)?

## Notable constraints and quirks

- `.github/skills/` is the canonical location for Copilot — aligns with existing GitHub conventions and is visible to collaborators.
- Only three frontmatter fields recognized (`name`, `description`, `license`) — keep it minimal.
- MCP tool references in the body are Copilot-specific and ignored by other harnesses.
- `/skills add`, `/skills reload`, and `/skills remove` are the most comprehensive skill management commands of any harness.
- The coding agent on GitHub.com activates skills autonomously; the CLI supports explicit `/name` invocation.
