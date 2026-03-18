# cline — Harness Reference

**Docs:** https://docs.cline.bot/customization/skills

## Skill placement (Linux)

| Scope | Path |
|---|---|
| Project | `.cline/skills/<name>/SKILL.md` |
| Project (compat) | `.clinerules/skills/<name>/SKILL.md` |
| Project (compat) | `.claude/skills/<name>/SKILL.md` |
| Global | `~/.cline/skills/<name>/SKILL.md` |

**Critical note — inverted precedence:** When a global skill and project skill share the same name, the **global skill takes precedence**. This is the opposite of every other harness. If overriding a global skill with a project-specific version, the `name` must differ, or the global skill must be removed.

## Frontmatter fields

| Field | Required | Constraints |
|---|---|---|
| `name` | Yes | Must match directory name in kebab-case |
| `description` | Yes | Max 1024 chars; determines when skill activates |

**Fields not supported:** `model`, `allowed-tools`, `disable-model-invocation`, `user-invocable`, `context`, `agent`, `hooks`, `license`, `compatibility`, `metadata`.

## Slash command / invocation

Cline does **not** support slash command invocation. Skills activate via Cline's internal `use_skill` tool when a request matches the description.

There is no user-facing mechanism to force a specific skill to activate.

## Optional subdirectory conventions

Cline documents these optional subdirectories within a skill:

```text
my-skill/
├── SKILL.md
├── docs/         ← detailed documentation
├── templates/    ← reusable templates
└── scripts/      ← helper scripts
```

Note: cline uses `docs/` where the base spec uses `references/`. Both can coexist.

## Three-tier progressive loading

| Tier | Content | Approximate cost |
|---|---|---|
| Catalog | `name` + `description` | ~100 tokens |
| Instructions | Full `SKILL.md` body | <5k tokens recommended |
| Resources | Files in subdirectories | On demand |

## Questions to ask the user

When targeting cline specifically, ask:

1. **Global vs project:** Should this be a global skill (`~/.cline/skills/`) or project-specific (`.cline/skills/`)? Remind them that global takes precedence if names conflict.
2. **Supporting files:** Will this skill include documentation templates or scripts? Use `docs/`, `templates/`, or `scripts/` subdirectories.

## Notable constraints and quirks

- **Inverted precedence** is the most important cline quirk: global wins over project. This is easily the biggest footgun when users are used to other harnesses.
- Only `name` and `description` are recognized in frontmatter — keep it minimal.
- No slash commands whatsoever.
- Cline is a VSCode extension; skills are only active within the VSCode environment.
