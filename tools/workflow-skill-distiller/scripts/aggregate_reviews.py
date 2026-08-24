from __future__ import annotations

import argparse
import sys
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.review import aggregate_reviews


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--cycle", required=True, type=int)
    args = parser.parse_args()
    verdict, issues = aggregate_reviews(args.workspace, args.cycle)
    if issues:
        print("\n".join(f"- {issue}" for issue in issues), file=sys.stderr)
        return 1
    print(verdict["status"])
    return 0 if verdict["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
