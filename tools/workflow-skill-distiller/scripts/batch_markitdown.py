from __future__ import annotations

import argparse
import sys
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.common import load_yaml, resolve_workspace_file, write_text_atomic, write_yaml_atomic
from workflow_skill_distiller.normalization import quality_flags


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize a source manifest using local MarkItDown conversion.")
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--retry", action="store_true", help="also convert failed/manual-review sources")
    args = parser.parse_args()
    try:
        from markitdown import MarkItDown
    except ImportError:
        print("MarkItDown is unavailable; install the project dependencies", file=sys.stderr)
        return 2
    manifest_path = args.workspace / "source-manifest.yaml"
    manifest = load_yaml(manifest_path)
    if manifest.get("source_library"):
        print("shared source manifests are already normalized in risk-evidence-library; do not reconvert them locally", file=sys.stderr)
        return 2
    converter = MarkItDown(enable_plugins=False)
    known_hashes: dict[str, str] = {}
    failures = 0
    for source in manifest["sources"]:
        state = source["normalization"]["status"]
        if state != "pending" and not (args.retry and state in {"failed", "manual_review"}):
            continue
        raw_path = resolve_workspace_file(args.workspace, source["raw_path"])
        output_path = resolve_workspace_file(args.workspace, source["normalized_path"])
        try:
            if hasattr(converter, "convert_local"):
                result = converter.convert_local(raw_path)
            else:
                result = converter.convert(str(raw_path))
            text = getattr(result, "text_content", None) or getattr(result, "markdown", "")
            flags = quality_flags(raw_path, text)
            duplicate_of = known_hashes.get(source["sha256"])
            known_hashes[source["sha256"]] = source["source_id"]
            write_text_atomic(output_path, text)
            source["normalization"] = {
                "status": "passed" if not flags and not duplicate_of else "manual_review",
                "text_characters": len(text),
                "heading_count": sum(line.startswith("#") for line in text.splitlines()),
                "duplicate_of": duplicate_of,
                "quality_flags": flags,
            }
            if source["normalization"]["status"] != "passed":
                failures += 1
        except Exception as exc:  # converter errors are retained as a quality flag
            source["normalization"] = {"status": "failed", "text_characters": 0, "heading_count": 0, "duplicate_of": None, "quality_flags": [f"conversion_failed:{type(exc).__name__}"]}
            failures += 1
    write_yaml_atomic(manifest_path, manifest)
    print(f"normalization complete; {failures} source(s) need attention")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
