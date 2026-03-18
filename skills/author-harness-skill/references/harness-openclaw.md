# OpenClaw — Harness Reference

**Docs:** https://docs.openclaw.ai/tools/skills#skills
**Public skills registry:** https://clawhub.com

## Skill placement (Linux)

| Scope | Path (priority order, highest first) |
|---|---|
| Workspace | `<workspace>/skills/<name>/SKILL.md` |
| Global | `~/.openclaw/skills/<name>/SKILL.md` |
| Bundled (read-only) | Skills shipped with OpenClaw install |
| Extra dirs | Paths in `skills.load.extraDirs` in `~/.openclaw/openclaw.json` (lowest) |

## Frontmatter fields

OpenClaw extends the base spec with several additional fields. Note: **the YAML parser used by the embedded agent only supports single-line frontmatter values** — no multi-line strings.

| Field | Required | Notes |
|---|---|---|
| `name` | Yes | Standard base spec rules |
| `description` | Yes | Single-line only |
| `homepage` | No | URL shown as "Website" in the macOS Skills UI |
| `user-invocable` | No | Boolean, default `true`; `false` hides from `/` menu |
| `disable-model-invocation` | No | Boolean, default `false`; `true` = slash-command only |
| `command-dispatch` | No | `tool` = bypass model entirely (see below) |
| `command-tool` | No | Name of the tool to dispatch to when `command-dispatch: tool` |
| `command-arg-mode` | No | `raw` (default) |
| `metadata` | No | **Single-line JSON object** (parser limitation) |

### `metadata` for environment gating

Use the `metadata` field with an `openclaw` subkey to conditionally load or skip a skill based on environment:

```yaml
metadata: '{"openclaw": {"requires": {"bins": ["ffmpeg"], "env": ["API_KEY"]}, "os": "linux", "install": ["brew", "download"]}}'
```

Subfields under `openclaw`:
- `requires.bins` — list of required executables
- `requires.env` — list of required environment variables
- `requires.config` — required config keys
- `os` — OS restriction (`linux`, `mac`, `windows`)
- `install` — installer types: `brew`, `node`, `go`, `uv`, `download`

## Slash command setup

`/<name>` slash commands work by default when `user-invocable: true` (the default).

### Direct tool dispatch (bypass model)

`command-dispatch: tool` routes the slash command directly to a named tool without invoking the LLM at all. This is unique to OpenClaw.

```yaml
---
name: my-tool-proxy
description: Proxy for my-tool operations
command-dispatch: tool
command-tool: my_tool_name
command-arg-mode: raw
---
```

When invoked as `/my-tool-proxy some args`, OpenClaw calls `my_tool_name` with:
```json
{
  "command": "some args",
  "commandName": "my-tool-proxy",
  "skillName": "my-tool-proxy"
}
```

Use this pattern for skills that wrap a specific tool and don't need LLM reasoning.

## Questions to ask the user

When targeting OpenClaw specifically, ask:

1. **Slash command:** Should this be user-invocable as `/<name>`? (Default: yes)
2. **Model bypass:** Should this skill bypass the LLM and dispatch directly to a tool? If yes, what tool name?
3. **Environment requirements:** Are there required binaries, env vars, or OS restrictions? (Use `metadata.openclaw` for conditional loading)
4. **macOS UI:** Should a homepage URL appear in the Skills UI?

## Notable constraints and quirks

- **Single-line YAML only**: multi-line frontmatter values will break the parser. Write `description` on one line; use the `>-` fold syntax carefully or avoid it.
- `command-dispatch: tool` is unique to OpenClaw — not portable. Don't add it to skills intended for other harnesses.
- Environment gating via `metadata.openclaw` is powerful but also OpenClaw-specific.
- `metadata` must be a single-line JSON string, not a YAML mapping, due to the parser limitation.
