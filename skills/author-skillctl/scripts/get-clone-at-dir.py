#!/usr/bin/env python3

from __future__ import annotations

import os
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    print("error: Python 3.11+ with tomllib is required", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    config_path = Path(
        os.environ.get("SKILLCTL_CONFIG_PATH", "~/.config/skillctl/config.toml")
    ).expanduser()

    try:
        with config_path.open("rb") as f:
            config = tomllib.load(f)
    except FileNotFoundError:
        print(f"error: skillctl config not found at {config_path}", file=sys.stderr)
        return 1
    except tomllib.TOMLDecodeError as exc:
        print(f"error: could not parse {config_path}: {exc}", file=sys.stderr)
        return 1

    clone_at = config.get("clone-at")
    if not isinstance(clone_at, str) or not clone_at.strip():
        print(
            f"error: {config_path} does not contain a non-empty 'clone-at' setting",
            file=sys.stderr,
        )
        return 1

    print(Path(clone_at).expanduser())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
