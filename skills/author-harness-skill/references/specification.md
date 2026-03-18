# Agent Skills Specification Reference

Source: https://agentskills.io/specification

## Directory structure

```text
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

## SKILL.md frontmatter fields

| Field | Required | Constraints |
|---|---|---|
| `name` | Yes | Max 64 characters. Lowercase letters, numbers, and hyphens only. Must not start or end with a hyphen. Must not contain consecutive hyphens. Must match parent directory name. |
| `description` | Yes | Max 1024 characters. Non-empty. Describes what the skill does and when to use it. |
| `license` | No | License name or reference to a bundled license file. |
| `compatibility` | No | Max 500 characters. Environment requirements (intended product, system packages, network access, etc.). |
| `metadata` | No | Arbitrary key-value mapping (string keys to string values) for additional metadata. |
| `allowed-tools` | No | Space-delimited list of pre-approved tools the skill may use. (Experimental) |

## Name field rules

- 1-64 characters
- Unicode lowercase alphanumeric (`a-z`, `0-9`) and hyphens (`-`) only
- Must not start or end with a hyphen
- Must not contain consecutive hyphens (`--`)
- Must match the parent directory name

## Description best practices

- 1-1024 characters
- Should describe both what the skill does AND when to use it
- Should include specific keywords that help agents identify relevant tasks

## Body content

The markdown body after the frontmatter contains the skill instructions. No format restrictions. Recommended sections:
- Step-by-step instructions
- Examples of inputs and outputs
- Common edge cases

Keep the body under 500 lines. Move detailed reference material to separate files.

## Token budget tiers

| Tier | What loads | When | Recommended budget |
|---|---|---|---|
| Catalog | `name` + `description` | Session start | ~50-100 tokens per skill |
| Instructions | Full `SKILL.md` body | Skill activation | <5000 tokens |
| Resources | Scripts, references, assets | On demand | Varies |

## File references

Use relative paths from the skill root:

```markdown
See [the reference guide](references/REFERENCE.md) for details.
Run: scripts/extract.py
```

Keep references one level deep from `SKILL.md`. Avoid deeply nested reference chains.

## Validation

Use the skills-ref reference library:

```bash
skills-ref validate ./my-skill
```

Repository: https://github.com/agentskills/agentskills/tree/main/skills-ref
