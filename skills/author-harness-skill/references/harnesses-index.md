# Supported Harnesses Index

When a user asks to tailor a skill for a specific harness, present this list and ask them to choose. Always include an "other / not listed" option.

## Supported harnesses

| # | Harness | Slash cmd? | Primary skill dir |
|---|---|---|---|
| 1 | **Claude Code** | Yes (`/<name>`) | `.claude/skills/<name>/` |
| 2 | **OpenAI Codex** | Yes (`$<name>`) | `.agents/skills/<name>/` |
| 3 | **OpenCode** | No (tool call) | `.agents/skills/<name>/` |
| 4 | **KiloCode** | No (LLM only) | `.kilocode/skills/<name>/` |
| 5 | **Gemini CLI** | Management only | `.agents/skills/<name>/` |
| 6 | **pi** | Yes (`/skill:<name>`) | `.pi/skills/<name>/` |
| 7 | **amp** | No (palette) | `.agents/skills/<name>/` |
| 8 | **Cursor** | Yes (`/<name>`) | `.cursor/skills/<name>/` |
| 9 | **cline** | No | `.cline/skills/<name>/` |
| 10 | **goose** | No | `.goose/skills/<name>/` |
| 11 | **OpenClaw** | Yes (`/<name>`) | `<workspace>/skills/<name>/` |
| 12 | **Warp** | Yes (`/<name>`) | `.agents/skills/<name>/` |
| 13 | **GitHub Copilot** | Yes (`/<name>`) | `.github/skills/<name>/` |
| 14 | **Crush** | Yes (`/<name>`) | (config-defined) |
| 15 | **Qwen** | Yes (`/skills <name>`) | `.qwen/skills/<name>/` |
| — | **Other / not listed** | — | — |

## Most portable location

`.agents/skills/<name>/` is scanned by: Codex, OpenCode, Gemini CLI, pi, amp, Warp, goose, Cursor (compat), and Copilot (compat). Use this as the default when the user hasn't specified a harness.

## Per-harness detail files

Load the relevant file from this `references/` directory when adapting for a specific harness:

- Claude Code → `harness-claude-code.md`
- OpenAI Codex → `harness-openai-codex.md`
- OpenCode → `harness-opencode.md`
- KiloCode → `harness-kilocode.md`
- Gemini CLI → `harness-gemini-cli.md`
- pi → `harness-pi.md`
- amp → `harness-amp.md`
- Cursor → `harness-cursor.md`
- cline → `harness-cline.md`
- goose → `harness-goose.md`
- OpenClaw → `harness-openclaw.md`
- Warp → `harness-warp.md`
- GitHub Copilot → `harness-github-copilot.md`
- Crush → `harness-crush.md`
- Qwen → `harness-qwen.md`
