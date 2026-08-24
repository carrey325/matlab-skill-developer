from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any, Iterable

import yaml
from jsonschema import Draft202012Validator, FormatChecker


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_DIR = PROJECT_ROOT / "config"
TEMPLATE_DIR = PROJECT_ROOT / "templates"


class ValidationFailure(Exception):
    """Raised when an artifact does not meet a required contract."""


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_source_manifest(workspace: Path) -> dict[str, Any]:
    """Load local source entries or resolve source-id references from the shared library.

    v1.1 local manifests remain valid.  A shared manifest stores only selected
    source IDs in the workflow workspace; raw and normalized bytes remain in
    the project-level risk-evidence-library.
    """
    manifest = load_yaml(workspace / "source-manifest.yaml") or {}
    library = manifest.get("source_library")
    if not library:
        return manifest
    relative = Path(str(library["manifest_path"]))
    if relative.is_absolute():
        raise ValidationFailure("source library manifest path must be project-relative")
    library_manifest_path = (PROJECT_ROOT / relative).resolve()
    if PROJECT_ROOT.resolve() not in library_manifest_path.parents:
        raise ValidationFailure("source library manifest path escapes project root")
    library_manifest = load_yaml(library_manifest_path) or {}
    available = {item["source_id"]: item for item in library_manifest.get("sources", [])}
    resolved: list[dict[str, Any]] = []
    for reference in manifest.get("sources", []):
        if set(reference) == {"source_id"}:
            source_id = reference["source_id"]
            if source_id not in available:
                raise ValidationFailure(f"shared source not found: {source_id}")
            resolved.append(dict(available[source_id]))
        else:
            resolved.append(reference)
    result = dict(manifest)
    result["sources"] = resolved
    result["_source_library_root"] = library_manifest_path.parent.parent
    return result


def resolve_source_artifact(workspace: Path, manifest: dict[str, Any], relative_path: str) -> Path:
    """Resolve a source artifact without allowing a workspace path escape."""
    root = Path(manifest.get("_source_library_root", workspace)).resolve()
    candidate = (root / relative_path).resolve()
    if candidate != root and root not in candidate.parents:
        raise ValidationFailure(f"source artifact escapes its root: {relative_path}")
    return candidate


def dump_yaml(value: Any) -> str:
    return yaml.safe_dump(value, allow_unicode=True, sort_keys=False, width=100)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent, text=True)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        Path(temp_name).replace(path)
    finally:
        if Path(temp_name).exists():
            Path(temp_name).unlink()


def write_bytes_atomic(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
        Path(temp_name).replace(path)
    finally:
        if Path(temp_name).exists():
            Path(temp_name).unlink()


def write_yaml_atomic(path: Path, value: Any) -> None:
    write_text_atomic(path, dump_yaml(value))


def write_json_atomic(path: Path, value: Any) -> None:
    write_text_atomic(path, json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def resolve_workspace_file(workspace: Path, relative_path: str) -> Path:
    candidate = (workspace / relative_path).resolve()
    workspace_root = workspace.resolve()
    if candidate != workspace_root and workspace_root not in candidate.parents:
        raise ValidationFailure(f"path escapes workspace: {relative_path}")
    return candidate


def schema_path(name: str) -> Path:
    locations = [CONFIG_DIR / name, TEMPLATE_DIR / name]
    for location in locations:
        if location.is_file():
            return location
    raise FileNotFoundError(f"schema not found: {name}")


def schema_errors(value: Any, schema_name: str) -> list[str]:
    schema = load_json(schema_path(schema_name))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(value), key=lambda item: list(item.absolute_path))
    rendered: list[str] = []
    for error in errors:
        path = ".".join(str(part) for part in error.absolute_path) or "$"
        rendered.append(f"{path}: {error.message}")
    return rendered


def ensure_schema(value: Any, schema_name: str) -> None:
    errors = schema_errors(value, schema_name)
    if errors:
        raise ValidationFailure("\n".join(errors))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    if not path.exists():
        return records
    with path.open("r", encoding="utf-8") as handle:
        for number, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            try:
                record = json.loads(text)
            except json.JSONDecodeError as exc:
                raise ValidationFailure(f"{path}:{number}: invalid JSON: {exc.msg}") from exc
            if not isinstance(record, dict):
                raise ValidationFailure(f"{path}:{number}: atom must be an object")
            records.append(record)
    return records


def write_jsonl_atomic(path: Path, records: Iterable[dict[str, Any]]) -> None:
    write_text_atomic(path, "".join(json.dumps(record, ensure_ascii=False) + "\n" for record in records))


def standard_workspace_directories(workspace: Path) -> list[Path]:
    return [
        workspace / "sources" / "raw",
        workspace / "sources" / "normalized",
        workspace / "extraction",
        workspace / "synthesis" / "decisions",
        workspace / "generated",
        workspace / "review" / "example-traces",
        workspace / "alignment",
    ]


def ensure_workspace_structure(workspace: Path) -> None:
    for directory in standard_workspace_directories(workspace):
        directory.mkdir(parents=True, exist_ok=True)


def print_issues(issues: list[str]) -> int:
    if issues:
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("PASS")
    return 0
