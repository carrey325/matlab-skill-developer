from __future__ import annotations

import argparse
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.common import print_issues
from workflow_skill_distiller.validators import validate_task_contract


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Workflow Distiller task contract.")
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--contract", type=Path)
    args = parser.parse_args()
    contract = args.contract or args.workspace / "task-contract.yaml"
    return print_issues(validate_task_contract(contract))


if __name__ == "__main__":
    raise SystemExit(main())
