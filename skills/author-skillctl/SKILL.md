---
name: author-skillctl
description: Create/Edit/Read a skillctl skill in an installed git repository
---
Create new skill in repos managed by skillctl's `clone-at` directory. Resolve it with THIS skill's `get-clone-at-dir.py`, which reads `~/.config/skillctl/config.toml`.

Use author-harness-skill to author/edit this skill.
- DO NOT edit project-local skills when doing so. Solely edit skills under the directory returned by THIS skill's `get-clone-at-dir.py` script.

Context:
- skillctl is a CLI tool for centrally managing agent skills by cloning git repos and symlinking/importing their contents.
- You can use `skillctl list` to see the current state of skills on a system.

