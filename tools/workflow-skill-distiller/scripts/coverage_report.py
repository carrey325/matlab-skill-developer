from __future__ import annotations

import argparse
import sys
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.coverage import coverage_report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", required=True, type=Path)
    args = parser.parse_args()
    report, issues = coverage_report(args.workspace)
    if issues:
        print("\n".join(f"- {issue}" for issue in issues), file=sys.stderr)
        return 1
    print(report)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
