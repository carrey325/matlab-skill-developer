from __future__ import annotations

import argparse
import mimetypes
import sys
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import urlparse

import requests

import _bootstrap  # noqa: F401
from workflow_skill_distiller.common import sha256_file, write_bytes_atomic, write_yaml_atomic, load_yaml


def extension_for(url: str, content_type: str) -> str:
    suffix = Path(urlparse(url).path).suffix.lower()
    if suffix and len(suffix) <= 8:
        return suffix
    guessed = mimetypes.guess_extension(content_type.split(";", 1)[0].strip())
    return guessed or ".bin"


def main() -> int:
    parser = argparse.ArgumentParser(description="Download source candidates and create a source manifest.")
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--candidates", required=True, type=Path, help="YAML with a top-level sources list")
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    candidates = load_yaml(args.candidates) or {}
    sources = candidates.get("sources")
    if not isinstance(sources, list) or not sources:
        print("candidates must have a nonempty sources list", file=sys.stderr)
        return 2
    raw_dir = args.workspace / "sources" / "raw"
    normalized_dir = args.workspace / "sources" / "normalized"
    raw_dir.mkdir(parents=True, exist_ok=True)
    normalized_dir.mkdir(parents=True, exist_ok=True)
    manifest_sources = []
    for candidate in sources:
        url = candidate.get("url", "")
        if urlparse(url).scheme not in {"http", "https"}:
            print(f"{candidate.get('source_id')}: URL must be HTTP(S)", file=sys.stderr)
            return 2
        response = requests.get(url, timeout=args.timeout, headers={"User-Agent": "workflow-skill-distiller/0.2"})
        response.raise_for_status()
        suffix = extension_for(url, response.headers.get("content-type", ""))
        raw_relative = f"sources/raw/{candidate['source_id'].lower()}{suffix}"
        raw_path = args.workspace / raw_relative
        if raw_path.exists() and not args.overwrite:
            print(f"refusing to overwrite {raw_path}; use --overwrite", file=sys.stderr)
            return 2
        write_bytes_atomic(raw_path, response.content)
        entry = {
            "source_id": candidate["source_id"],
            "organization": candidate["organization"],
            "title": candidate["title"],
            "version": str(candidate.get("version") or candidate["publication_date"]),
            "url": url,
            "source_type": candidate["source_type"],
            "publication_date": candidate["publication_date"],
            "effective_date": candidate.get("effective_date"),
            "jurisdiction": candidate["jurisdiction"],
            "authority_tier": candidate["authority_tier"],
            "official_primary": candidate["official_primary"],
            "status": candidate.get("status", "current"),
            "retrieved_at": datetime.now(UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            "sha256": sha256_file(raw_path),
            "raw_path": raw_relative,
            "normalized_path": f"sources/normalized/{candidate['source_id'].lower()}.md",
            "normalization": {"status": "pending", "text_characters": 0, "heading_count": 0, "duplicate_of": None, "quality_flags": []},
        }
        manifest_sources.append(entry)
    workflow_id = (load_yaml(args.workspace / "task-contract.yaml") or {}).get("workflow_name", "unknown-workflow")
    write_yaml_atomic(args.workspace / "source-manifest.yaml", {"schema_version": "1.1.0", "workflow_id": workflow_id, "sources": manifest_sources})
    print(f"downloaded {len(manifest_sources)} sources")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except requests.RequestException as exc:
        print(f"source download failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
