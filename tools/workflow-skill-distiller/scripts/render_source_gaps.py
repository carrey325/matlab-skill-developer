from __future__ import annotations

import argparse
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.evidence import render_source_gaps


def main() -> int:
    parser = argparse.ArgumentParser(description="Render source-gaps.md from evidence-coverage.yaml.")
    parser.add_argument("--workspace", required=True, type=Path)
    output = render_source_gaps(parser.parse_args().workspace)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
