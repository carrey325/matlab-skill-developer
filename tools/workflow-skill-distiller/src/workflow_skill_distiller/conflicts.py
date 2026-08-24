from __future__ import annotations

from pathlib import Path
from typing import Any

from .common import load_yaml, write_text_atomic


def source_conflicts_markdown(conflicts: dict[str, Any]) -> str:
    lines = ["# Source Conflicts", ""]
    lines.extend([conflicts.get("analysis_scope", "Applicability conflicts across the active evidence corpus."), ""])
    resolved = conflicts.get("resolved_conflicts", [])
    unresolved = conflicts.get("unresolved_conflicts", [])
    lines.extend([f"Resolved conflicts: {len(resolved)}", f"Unresolved conflicts: {conflicts.get('unresolved_count', len(unresolved))}", ""])
    for heading, records in (("Resolved", resolved), ("Unresolved", unresolved)):
        lines.extend([f"## {heading}", ""])
        if not records:
            lines.extend(["None.", ""])
            continue
        for index, record in enumerate(records, start=1):
            identifier = record.get("id", f"CONFLICT-{index}")
            lines.extend([
                f"### {identifier}", "",
                record.get("description", ""), "",
                f"Resolution: {record.get('resolution', 'Open')}", "",
                f"Applicability: {', '.join(record.get('applicability', []))}", "",
            ])
    return "\n".join(lines).rstrip() + "\n"


def render_source_conflicts(workspace: Path) -> Path:
    conflicts = load_yaml(workspace / "extraction" / "source-conflicts.yaml") or {}
    output = workspace / "extraction" / "source-conflicts.md"
    write_text_atomic(output, source_conflicts_markdown(conflicts))
    return output
