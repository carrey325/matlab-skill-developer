from __future__ import annotations

import argparse
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.common import print_issues
from workflow_skill_distiller.evidence import validate_evidence_coverage


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the professional evidence-coverage matrix.")
    parser.add_argument("--workspace", required=True, type=Path)
    return print_issues(validate_evidence_coverage(parser.parse_args().workspace))


if __name__ == "__main__":
    raise SystemExit(main())
