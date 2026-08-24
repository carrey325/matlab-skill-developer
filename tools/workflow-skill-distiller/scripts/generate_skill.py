from __future__ import annotations

import argparse
import sys
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.generation import render_skill
from workflow_skill_distiller.validators import validate_workflow_ir


def main() -> int:
    parser = argparse.ArgumentParser(description="Render an agent-neutral Skill from validated Workflow IR.")
    parser.add_argument("--workspace", required=True, type=Path)
    args = parser.parse_args()
    issues = validate_workflow_ir(args.workspace)
    if issues:
        print("Workflow IR invalid:", file=sys.stderr)
        print("\n".join(f"- {issue}" for issue in issues), file=sys.stderr)
        return 1
    print(render_skill(args.workspace))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
