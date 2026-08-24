from __future__ import annotations

import argparse
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.common import print_issues
from workflow_skill_distiller.validators import validate_provider_signatures


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a provider skill-signature inventory.")
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--inventory", required=True, type=Path)
    args = parser.parse_args()
    return print_issues(validate_provider_signatures(args.inventory))


if __name__ == "__main__":
    raise SystemExit(main())
