from __future__ import annotations

import argparse
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.providers import extract_matlab_signatures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--skills-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if not args.workspace.is_dir():
        parser.error("--workspace must be an existing workflow workspace")
    inventory = extract_matlab_signatures(args.skills_root, args.output)
    print(f"wrote {len(inventory['signatures'])} MATLAB provider signatures")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
