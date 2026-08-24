from __future__ import annotations

from pathlib import Path
from typing import Any

from .common import load_source_manifest, load_yaml, read_jsonl, schema_errors, write_text_atomic


def validate_evidence_coverage(workspace: Path) -> list[str]:
    path = workspace / "extraction" / "evidence-coverage.yaml"
    if not path.is_file():
        return ["missing extraction/evidence-coverage.yaml"]
    coverage = load_yaml(path) or {}
    issues = schema_errors(coverage, "evidence-coverage.schema.json")
    if issues:
        return issues
    atoms = {atom["id"]: atom for atom in read_jsonl(workspace / "extraction" / "knowledge-atoms.jsonl")}
    manifest = load_source_manifest(workspace)
    sources = {source["source_id"]: source for source in manifest["sources"]}
    seen: set[str] = set()
    for dimension in coverage["dimensions"]:
        identifier = dimension["id"]
        if identifier in seen:
            issues.append(f"duplicate evidence dimension {identifier}")
        seen.add(identifier)
        for atom_id in dimension["atom_ids"]:
            if atom_id not in atoms:
                issues.append(f"{identifier}: unknown atom {atom_id}")
        for source_id in dimension["source_ids"]:
            if source_id not in sources:
                issues.append(f"{identifier}: unknown source {source_id}")
        derived_sources = {atoms[atom_id]["source_id"] for atom_id in dimension["atom_ids"] if atom_id in atoms}
        if derived_sources != set(dimension["source_ids"]):
            issues.append(f"{identifier}: source_ids do not exactly match the referenced atoms")
        derived_tiers = {sources[source_id]["authority_tier"] for source_id in dimension["source_ids"] if source_id in sources}
        if derived_tiers != set(dimension["authority_levels"]):
            issues.append(f"{identifier}: authority_levels do not exactly match source manifest")
        if dimension["status"] == "covered" and not dimension["atom_ids"]:
            issues.append(f"{identifier}: covered dimension has no evidence atoms")
        if dimension["status"] in {"weak", "gap"} and not dimension["unresolved_gap"]:
            issues.append(f"{identifier}: weak/gap dimension must explain the unresolved gap")
        if dimension["requirement"] == "required" and dimension["status"] != "covered":
            issues.append(f"{identifier}: required dimension is {dimension['status']}")
        if dimension["requirement"] == "required" and dimension["status"] == "covered":
            current = [sources[sid] for sid in dimension["source_ids"] if sid in sources and sources[sid]["status"] == "current"]
            if not current:
                issues.append(f"{identifier}: required claim is supported only by historical or superseded sources")
    return issues


def source_gaps_markdown(coverage: dict[str, Any]) -> str:
    lines = ["# Source Gaps", "", "This register is generated from the evidence-coverage matrix. It records conditional or unresolved evidence weaknesses without treating them as established workflow rules.", ""]
    gaps = [item for item in coverage.get("dimensions", []) if item.get("status") in {"weak", "gap"}]
    if not gaps:
        lines.append("The coverage audit found no open evidence gaps for the currently declared scope and applicability conditions.")
    for item in gaps:
        lines.extend([
            f"## {item['name']}", "",
            f"- Status: {item['status']}",
            f"- Requirement: {item['requirement']}",
            f"- Applies when: {item.get('condition') or 'always'}",
            f"- Gap: {item['unresolved_gap']}",
            f"- Current evidence: {', '.join(item['source_ids']) or 'none'}",
            f"- Analysis: {item['analysis_notes']}", "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def render_source_gaps(workspace: Path) -> Path:
    coverage = load_yaml(workspace / "extraction" / "evidence-coverage.yaml") or {}
    output = workspace / "extraction" / "source-gaps.md"
    write_text_atomic(output, source_gaps_markdown(coverage))
    return output
