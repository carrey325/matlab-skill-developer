from __future__ import annotations

import argparse
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.conflicts import render_source_conflicts


def main() -> int:
    parser = argparse.ArgumentParser(description="Render the required Markdown source-conflict view from canonical YAML.")
    parser.add_argument("--workspace", required=True, type=Path)
    args = parser.parse_args()
    print(render_source_conflicts(args.workspace))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
