# Claude Code — Harness Reference

**Docs:** https://code.claude.com/docs/en/skills
**Spec repo:** https://github.com/agentskills/agentskills
**Example skills:** https://github.com/anthropics/skills

## Skill placement (Linux)

| Scope | Path |
|---|---|
| Project | `.claude/skills/<name>/SKILL.md` |
| Personal (global) | `~/.claude/skills/<name>/SKILL.md` |
| Legacy (still works) | `.claude/commands/<name>.md` |

Place in CWD unless user specifies otherwise.

## Frontmatter fields

All fields beyond the base spec are optional.

| Field | Notes |
|---|---|
| `name` | Base spec rules apply. Becomes the `/name` slash command. |
| `description` | Recommended even though optional. Falls back to first paragraph. |
| `argument-hint` | Shown during `/` autocomplete, e.g. `[issue-number]` or `<branch>`. |
| `disable-model-invocation` | `true` = slash-command only; Claude will not auto-load. |
| `user-invocable` | `false` = hidden from `/` menu; agent-invoked only. |
| `allowed-tools` | Space-delimited pre-approved tools, e.g. `Bash(git:*) Read Write`. |
| `model` | Override the model for this skill, e.g. `claude-opus-4-5`. |
| `context` | `fork` runs the skill in an isolated subagent with no conversation history. |
| `agent` | Subagent type when `context: fork`: `Explore`, `Plan`, `general-purpose`, or custom. |
| `hooks` | Lifecycle hooks scoped to this skill only. |

## Slash command setup

The `name` field **automatically becomes** the `/name` slash command — no extra config needed.

Invocation control matrix:

| `disable-model-invocation` | `user-invocable` | Result |
|---|---|---|
| `false` (default) | `true` (default) | Auto-loaded by Claude + available as `/name` |
| `true` | `true` | Slash command only; Claude never auto-loads |
| `false` | `false` | Claude auto-loads; hidden from `/` menu |
| `true` | `false` | Unusable by users; only callable by other skills |

## Dynamic shell injection

Use `` !`command` `` anywhere in the skill body to run a shell command at load time. The output is inlined before the content reaches Claude:

```markdown
Current branch: !`git branch --show-current`
```

This is preprocessing — Claude only sees the rendered result.

## Subagent forking

```yaml
context: fork
agent: Explore   # or: Plan, general-purpose, or a custom agent name
```

Runs the skill in a completely isolated subagent. Use for tasks that should not have access to conversation history.

## Extended thinking

Including the word **ultrathink** anywhere in the skill body activates extended thinking mode for that skill's execution.

## String substitutions

| Variable | Value |
|---|---|
| `$ARGUMENTS` | All arguments passed at invocation |
| `$ARGUMENTS[0]`, `$0` | First argument |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `${CLAUDE_SKILL_DIR}` | Absolute path to the skill's directory |

## Questions to ask the user

When targeting Claude Code specifically, ask:

1. **Invocation mode:** Should this skill be user-invocable as a slash command, agent-invocable only, or both? (Default: both)
2. **Argument hint:** Does this skill accept arguments? If so, what's the hint text (e.g. `[issue-number]`)?
3. **Tool permissions:** Should any tools be pre-approved so users aren't prompted per-use? (e.g. `Bash Read Write`)
4. **Model override:** Should this skill use a specific model? (e.g. for a reasoning-heavy skill)
5. **Subagent fork:** Should this skill run in isolation, without access to the current conversation?

## Notable constraints and quirks

- Context budget: skill descriptions share ~2% of the context window (~16k chars). Skills beyond this budget are excluded from context. Keep descriptions concise.
- The skill's directory name must exactly match the `name` field.
- `allowed-tools` is experimental but well-supported in Claude Code.
- `"ultrathink"` in the body is a Claude Code-specific feature; it will be ignored by other harnesses.
- Shell injection (`` !`cmd` ``) is Claude Code-specific and not portable.
