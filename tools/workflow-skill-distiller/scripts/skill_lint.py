from __future__ import annotations

import argparse
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.common import print_issues
from workflow_skill_distiller.validators import validate_skill_package


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--skill", required=True, type=Path)
    parser.add_argument("--release", action="store_true", help="lint a published package outside its source workspace")
    args = parser.parse_args()
    try:
        args.skill.resolve().relative_to(args.workspace.resolve())
        inside_workspace = True
    except ValueError:
        inside_workspace = False
    if not inside_workspace and not args.release:
        parser.error("--skill must be located inside --workspace unless --release is used")
    return print_issues(validate_skill_package(args.skill, args.workspace if inside_workspace else None))


if __name__ == "__main__":
    raise SystemExit(main())
