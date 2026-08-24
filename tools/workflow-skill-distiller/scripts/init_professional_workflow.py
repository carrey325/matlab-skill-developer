from __future__ import annotations

import argparse
import sys
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.common import ensure_workspace_structure, load_yaml, schema_errors, write_yaml_atomic


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize one professional workflow workspace without generating semantic content.")
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--contract", required=True, type=Path)
    args = parser.parse_args()
    contract = load_yaml(args.contract) or {}
    issues = schema_errors(contract, "task-contract.schema.json")
    if issues:
        print("\n".join(f"- {issue}" for issue in issues), file=sys.stderr)
        return 1
    if (args.workspace / "task-contract.yaml").exists():
        print("workspace already contains task-contract.yaml", file=sys.stderr)
        return 2
    ensure_workspace_structure(args.workspace)
    write_yaml_atomic(args.workspace / "task-contract.yaml", contract)
    print(f"initialized {args.workspace}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
