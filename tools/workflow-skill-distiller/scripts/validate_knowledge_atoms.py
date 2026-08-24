from __future__ import annotations

import argparse
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.common import print_issues
from workflow_skill_distiller.validators import validate_knowledge_atoms


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", required=True, type=Path)
    args = parser.parse_args()
    return print_issues(validate_knowledge_atoms(args.workspace))


if __name__ == "__main__":
    raise SystemExit(main())
