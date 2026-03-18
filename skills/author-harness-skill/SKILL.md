---
name: author-harness-skill
description: >-
  Create, validate, and refine Agent Skills (Open Skills Standard). Use when
  writing a new SKILL.md, structuring a skill directory, reviewing skill
  quality, or converting instructions into a portable skill package.
compatibility: Requires filesystem access to create directories and files
metadata:
  author: personal
  version: "2.0"
---

# Skill Authoring

Write skills that conform to the [Agent Skills](https://agentskills.io/) open standard.

## Workflow

Always follow this process. Ask questions one at a time. Do not write files until Phase 4.

---

### Phase 1: Gather requirements

Ask the following if not already clear from context:

1. **What should this skill do?** — the specific capability it provides
2. **What triggers it?** — conditions under which an agent should activate it (keywords, task types, user phrases)
3. **What's the skill name?** — suggest a lowercase kebab-case name; confirm with the user
4. **Are there supporting files?** — scripts to run, reference docs, templates? (These go in `scripts/`, `references/`, `assets/`)

---

### Phase 2: Harness selection

Always ask the user which harness this skill is for, even if context seems obvious. Present the full list:

> Which coding harness is this skill for? (You can pick one or say "agnostic" for a portable skill that works across tools.)
>
> 1. Claude Code
> 2. OpenAI Codex
> 3. OpenCode
> 4. KiloCode
> 5. Gemini CLI
> 6. pi
> 7. amp
> 8. Cursor
> 9. cline
> 10. goose
> 11. OpenClaw
> 12. Warp
> 13. GitHub Copilot
> 14. Crush
> 15. Qwen
> 16. Other / not listed (describe your harness)
> 0. None — create a harness-agnostic skill (default)

**If the user picks 0 or "agnostic":** proceed to Phase 3 without loading a harness reference. The skill will target `.agents/skills/` (the most portable location).

**If the user picks a specific harness:** load the relevant reference file from `references/harness-<name>.md` before asking Phase 3 questions. See [Harnesses Index](references/harnesses-index.md) for the file list.

**If the user picks "other":** ask them to describe the harness and proceed with base spec only.

---

### Phase 3: Harness-specific questions

**For agnostic skills:** no additional questions — proceed to Phase 4.

**For harness-specific skills:** read the loaded reference file and ask the questions listed in its "Questions to ask the user" section. At minimum, always ask:

- **Slash command:** Does the user want this invocable as a slash command?
  - If the harness does not support slash commands (KiloCode, cline, goose, amp), say so and skip.
  - If yes, note the harness-specific syntax and any required setup (see [Slash Command Handling](#slash-command-handling) below).
- **Skill scope:** Global (user-wide) or project-local? Default to project-local.

---

### Phase 4: Create the skill

1. Create the skill directory in the **current working directory** unless the user specifies otherwise:
   ```
   <cwd>/<skill-name>/
   └── SKILL.md
   ```
2. Write `SKILL.md` with correct frontmatter and body (see [SKILL.md Format](#skillmd-format) below).
3. Create any supporting files the user requested (`scripts/`, `references/`, `assets/`).
4. If the skill is harness-agnostic, use `.agents/skills/<name>/` as the placement recommendation when giving the user install instructions.

---

### Phase 5: Harness adaptation (if applicable)

If a specific harness was selected:

1. **Adjust frontmatter** — add, remove, or rename fields per the harness reference. This is the primary adaptation step. Be conservative with the body.
2. **Slash command setup** — apply any harness-specific slash command config (see below).
3. **Additional files** — create any harness-required files (e.g. OpenCode `commands/` file, OpenAI Codex `agents/openai.yaml` sidecar, amp `mcp.json`).
4. **Validate** — run through the [Validation Checklist](#validation-checklist).

Only edit the skill body if the harness has a concrete, documented convention that requires it. Do not rewrite prose for stylistic preference.

---

## Slash command handling

Slash command support and syntax vary significantly by harness. Consult the relevant reference file for full details.

| Harness | Slash cmd? | Syntax | Extra setup |
|---|---|---|---|
| Claude Code | Yes | `/<name>` | None — `name` field is the command |
| OpenAI Codex | Yes | `$<name>` | None; `allow_implicit_invocation: false` in sidecar to disable auto |
| OpenCode | No built-in | N/A | Create `.opencode/commands/<name>.md` separately |
| KiloCode | No | — | Not supported |
| Gemini CLI | Management only | `/skills enable/disable` | Skills are not directly invocable by name |
| pi | Yes | `/skill:<name>` | `"enableSkillCommands": true` in `settings.json` |
| amp | No | — | Not supported |
| Cursor | Yes | `/<name>` | None — `name` field is the command |
| cline | No | — | Not supported |
| goose | No | — | Not supported |
| OpenClaw | Yes | `/<name>` | Optionally set `command-dispatch: tool` for LLM-bypass |
| Warp | Yes | `/<name>` | None — all discovered skills are auto-commandable |
| GitHub Copilot | Yes | `/<name>` | None (CLI); coding agent uses autonomous activation |
| Crush | Yes | `/<name>` | None — `name` field is the command |
| Qwen | Yes | `/skills <name>` | Note: "skills" prefix, not `/<name>` directly |

**OpenCode slash command:** if the user wants `/my-skill` in OpenCode, create a separate file:
```text
.opencode/commands/my-skill.md
```
Content is a plain markdown prompt (no frontmatter required). The filename becomes the command name.

---

## SKILL.md format

Every skill is a directory whose name matches the `name` field in its `SKILL.md`:

```text
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: supplementary documentation
└── assets/           # Optional: templates, static resources
```

### Frontmatter fields (base spec)

| Field | Required | Constraints |
|---|---|---|
| `name` | Yes | Lowercase `a-z`, digits, hyphens only. Max 64 chars. No leading/trailing/consecutive hyphens. Must match parent directory name. |
| `description` | Yes | 1–1024 chars. Describe what it does AND when to use it. Include trigger keywords. |
| `license` | No | Short license name or reference to bundled file |
| `compatibility` | No | 1–500 chars. Environment requirements only — omit if none |
| `metadata` | No | Arbitrary string key-value map |
| `allowed-tools` | No | Space-delimited pre-approved tools (experimental) |

Harness-specific fields (e.g. `model`, `context`, `disable-model-invocation`) are documented in the individual reference files.

### Body content

No structural restrictions. Recommended sections:
- **When to use** — trigger conditions
- **Step-by-step instructions** — the core procedure
- **Examples** — inputs and expected outputs
- **Edge cases** — common pitfalls

---

## Authoring rules

### Name correctly

Valid: `pdf-processing`, `data-analysis`, `code-review`
Invalid: `PDF-Processing` (uppercase), `-pdf` (leading hyphen), `pdf--processing` (consecutive hyphens), `my skill` (spaces)

The directory name must exactly match the `name` field.

### Write effective descriptions

The description determines whether agents activate the skill. It must answer: **what does it do?** and **when should it be used?**

Good:
```yaml
description: >-
  Extracts text and tables from PDF files, fills PDF forms, and merges
  multiple PDFs. Use when working with PDF documents or when the user
  mentions PDFs, forms, or document extraction.
```

Bad: `description: Helps with PDFs.`

### Keep SKILL.md under 500 lines

Move detailed reference material, long examples, and lookup tables into `references/` files — they load on demand.

### Design for progressive disclosure

| Tier | What loads | Recommended budget |
|---|---|---|
| Catalog | `name` + `description` | ~50–100 tokens |
| Activation | Full `SKILL.md` body | <5000 tokens |
| Resources | `scripts/`, `references/`, `assets/` | On demand |

### Use relative paths

```markdown
See [the API reference](references/api-guide.md) for details.
Run `scripts/setup.sh` to initialize.
```

Keep references one level deep. Avoid deeply nested chains.

### Make scripts self-contained

Scripts in `scripts/` should document their dependencies at the top, include helpful error messages, handle edge cases, and be executable (`chmod +x`).

---

## Validation checklist

Before finalizing any skill:

- [ ] `name` matches directory name exactly
- [ ] `name` is lowercase kebab-case, no leading/trailing/consecutive hyphens, max 64 chars
- [ ] `description` is 1–1024 chars and includes both purpose and trigger keywords
- [ ] `SKILL.md` body is under 500 lines
- [ ] All file references use relative paths from skill root
- [ ] No deeply nested reference chains
- [ ] Scripts are self-contained with documented dependencies
- [ ] `compatibility` is present only if there are real environment requirements
- [ ] Harness-specific frontmatter fields are correct for the target (check reference file)
- [ ] Slash command setup is complete if requested (see Slash Command Handling above)

---

## Anti-patterns to avoid

- **Overly broad descriptions** — "Helps with code" matches everything and nothing
- **Monolithic SKILL.md** — 1000-line files waste context on every activation
- **Hardcoded absolute paths** — breaks portability
- **Missing trigger keywords** — agents can't match tasks to the skill
- **Deeply nested references** — `references/sub/sub/detail.md` is hard to discover
- **Unnecessary frontmatter** — omit `compatibility` and `metadata` if you have nothing to say
- **Harness-specific fields in agnostic skills** — `model`, `context: fork`, `command-dispatch` etc. are not portable
