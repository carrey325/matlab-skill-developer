from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.common import ensure_workspace_structure, load_yaml, write_yaml_atomic
from workflow_skill_distiller.validators import validate_task_contract


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a standard Distiller workspace from a valid task contract.")
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--force", action="store_true", help="replace an existing task-contract.yaml only")
    args = parser.parse_args()
    issues = validate_task_contract(args.contract)
    if issues:
        print("Task contract invalid:", file=sys.stderr)
        print("\n".join(f"- {issue}" for issue in issues), file=sys.stderr)
        return 1
    target = args.workspace / "task-contract.yaml"
    if target.exists() and not args.force:
        print(f"refusing to overwrite {target}; use --force", file=sys.stderr)
        return 2
    ensure_workspace_structure(args.workspace)
    write_yaml_atomic(target, load_yaml(args.contract))
    print(args.workspace)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
