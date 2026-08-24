from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

from .common import load_source_manifest, load_yaml, read_jsonl, schema_errors


REQUIRED_REVIEWS = {
    "evidence-review.yaml",
    "structure-review.yaml",
    "domain-review.yaml",
    "example-replay-review.yaml",
    "adversarial-review.yaml",
    "granularity-review.yaml",
}
PROHIBITED_CONCLUSION_INPUTS = {"method-context", "assessment-result", "selected-method", "final-disposition"}
PROFESSIONAL_ATOM_TYPES = {"requirement", "decision_rule", "validation_gate", "constraint", "stop_condition"}
PROFESSIONAL_ROLES = {"normative", "supervisory", "professional_methodology", "business_process"}
VENDOR_ROLES = {"implementation", "worked_example"}


def _norm(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(value).casefold())


def _workspace_id(workspace: Path) -> str:
    return str(load_yaml(workspace / "synthesis" / "workflow-ir.yaml")["workflow"]["id"])


def validate_source_relevance(workspace: Path) -> list[str]:
    path = workspace / "extraction" / "source-relevance.yaml"
    if not path.is_file():
        return ["missing extraction/source-relevance.yaml"]
    value = load_yaml(path) or {}
    issues = schema_errors(value, "source-relevance.schema.json")
    if issues:
        return issues
    workflow_id = _workspace_id(workspace)
    if value["workflow_id"] != workflow_id:
        issues.append("source relevance workflow_id differs from Workflow IR")
    manifest = load_source_manifest(workspace)
    sources = {source["source_id"]: source for source in manifest["sources"]}
    relevance = {item["source_id"]: item for item in value["sources"]}
    if len(relevance) != len(value["sources"]):
        issues.append("source relevance source IDs must be unique")
    if set(relevance) != set(sources):
        missing = sorted(set(sources) - set(relevance))
        extra = sorted(set(relevance) - set(sources))
        if missing:
            issues.append(f"source relevance omits selected sources: {', '.join(missing)}")
        if extra:
            issues.append(f"source relevance references unselected sources: {', '.join(extra)}")
    for source_id, item in relevance.items():
        source = sources.get(source_id)
        if not source:
            continue
        role = item["evidence_role"]
        source_type = source["source_type"]
        if source_type == "vendor_documentation_or_examples" and role not in VENDOR_ROLES:
            issues.append(f"{source_id}: vendor evidence cannot serve as {role}")
        if role in {"normative", "supervisory"} and source_type not in {"primary_standard_or_regulation", "supervisory_guidance"}:
            issues.append(f"{source_id}: {role} role requires official standard or supervisory guidance")
        applicable = set(source.get("applicable_workflows", []))
        if applicable and workflow_id not in applicable and not item.get("cross_domain_rationale"):
            issues.append(f"{source_id}: source is not indexed for {workflow_id} and lacks a cross-domain rationale")
    atoms = read_jsonl(workspace / "extraction" / "knowledge-atoms.jsonl")
    for atom in atoms:
        item = relevance.get(atom["source_id"])
        if atom.get("mandatory") and atom.get("type") in PROFESSIONAL_ATOM_TYPES:
            if not item or item["evidence_role"] not in PROFESSIONAL_ROLES:
                issues.append(f"{atom['id']}: mandatory professional claim relies on implementation/example evidence")
    return issues


def validate_decision_semantics(workspace: Path) -> list[str]:
    ir = load_yaml(workspace / "synthesis" / "workflow-ir.yaml") or {}
    issues: list[str] = []
    for decision in ir.get("decisions", []):
        if len(decision.get("rules", [])) < 2:
            issues.append(f"{decision.get('id')}: material decision requires at least two evidence-backed routes")
        input_names = set()
        for item in decision.get("inputs", []):
            name = str(item.get("name", ""))
            input_names.add(name)
            if name in PROHIBITED_CONCLUSION_INPUTS:
                issues.append(f"{decision.get('id')}: prohibited conclusion-bearing input {name}")
            if item.get("producer") is None or item.get("observable") is not True:
                issues.append(f"{decision.get('id')}:{name}: input requires an observable producer")
        outcomes = Counter(str(rule.get("outcome")) for rule in decision.get("rules", []))
        if any(count > 1 for count in outcomes.values()):
            issues.append(f"{decision.get('id')}: duplicate outcomes require consolidation or explicit priority")
        for rule in decision.get("rules", []):
            outcome = _norm(rule.get("outcome"))
            for condition in rule.get("conditions", []):
                values = condition.get("value") if isinstance(condition.get("value"), list) else [condition.get("value")]
                if any(_norm(value) == outcome and outcome for value in values):
                    issues.append(f"{rule.get('id')}: condition value merely restates outcome {rule.get('outcome')}")
            if not rule.get("missing_information_behavior"):
                issues.append(f"{rule.get('id')}: missing-information behavior is absent")
        fallback = decision.get("fallback", {})
        if not fallback.get("outcome") or not fallback.get("instruction"):
            issues.append(f"{decision.get('id')}: explicit fallback is absent")
    return issues


def validate_professional_reviews(workspace: Path) -> list[str]:
    review_dir = workspace / "review"
    existing = {path.name for path in review_dir.glob("*-review.yaml")}
    issues: list[str] = []
    missing = sorted(REQUIRED_REVIEWS - existing)
    if missing:
        issues.append(f"missing professional reviews: {', '.join(missing)}")
    reviewers: set[str] = set()
    for name in sorted(REQUIRED_REVIEWS & existing):
        review = load_yaml(review_dir / name) or {}
        reviewer = str(review.get("reviewer", ""))
        if reviewer in reviewers:
            issues.append(f"{name}: reviewer identity duplicates another review")
        reviewers.add(reviewer)
        checks = review.get("checks", [])
        if len(checks) < 2:
            issues.append(f"{name}: professional review requires at least two substantive checks")
        if review.get("status") == "PASS":
            combined = " ".join(str(check.get("notes", "")) for check in checks)
            if _norm(combined) in {"pass", "allcheckspass", "noproblemsfound"}:
                issues.append(f"{name}: PASS lacks workflow-specific findings")
    metadata_path = workspace / "professional-release.yaml"
    if not metadata_path.is_file():
        issues.append("missing professional-release.yaml")
    else:
        metadata = load_yaml(metadata_path) or {}
        issues.extend(schema_errors(metadata, "professional-release.schema.json"))
        if metadata.get("workflow_id") != _workspace_id(workspace):
            issues.append("professional-release workflow_id differs from Workflow IR")
    return issues


def validate_replay_relevance(workspace: Path) -> list[str]:
    relevance_path = workspace / "extraction" / "source-relevance.yaml"
    if not relevance_path.is_file():
        return ["cannot validate replay relevance without source-relevance.yaml"]
    relevance = {item["source_id"]: item for item in (load_yaml(relevance_path) or {}).get("sources", [])}
    issues: list[str] = []
    for path in sorted((workspace / "review" / "example-traces").glob("*.yaml")):
        trace = load_yaml(path) or {}
        if trace.get("case_type") != "real_source_replay":
            continue
        provenance = trace.get("source_provenance") or {}
        source_id = provenance.get("source_id")
        item = relevance.get(source_id)
        if not item:
            issues.append(f"{path.name}: real replay source lacks relevance assessment")
        elif item["evidence_role"] not in {"worked_example", "implementation", "professional_methodology"}:
            issues.append(f"{path.name}: {source_id} is not designated for credible replay or methodology use")
        if not str(provenance.get("locator", "")).strip():
            issues.append(f"{path.name}: real replay lacks a precise locator")
    return issues


def decision_signature(workspace: Path) -> str:
    ir = load_yaml(workspace / "synthesis" / "workflow-ir.yaml") or {}
    payload = []
    for decision in ir.get("decisions", []):
        payload.append({
            "title": _norm(decision.get("title")),
            "inputs": sorted(_norm(item.get("name")) for item in decision.get("inputs", [])),
            "rules": sorted((tuple(sorted((_norm(condition.get("input")), str(condition.get("operator")), _norm(condition.get("value"))) for condition in rule.get("conditions", []))), _norm(rule.get("outcome"))) for rule in decision.get("rules", [])),
        })
    return json.dumps(payload, sort_keys=True, ensure_ascii=True)


def _mandatory_atom_statements(workspace: Path) -> set[str]:
    return {_norm(atom["statement"]) for atom in read_jsonl(workspace / "extraction" / "knowledge-atoms.jsonl") if atom.get("mandatory")}


def validate_cross_workflow_originality(workspaces: Iterable[Path]) -> list[str]:
    paths = list(workspaces)
    issues: list[str] = []
    signatures: dict[str, Path] = {}
    atom_sets: dict[Path, set[str]] = {}
    review_hashes: dict[tuple[str, str], Path] = {}
    for workspace in paths:
        signature = decision_signature(workspace)
        if signature in signatures:
            issues.append(f"{workspace.name}: decision graph duplicates {signatures[signature].name}")
        signatures[signature] = workspace
        atoms = _mandatory_atom_statements(workspace)
        atom_sets[workspace] = atoms
        for other, other_atoms in atom_sets.items():
            if other == workspace or not atoms or not other_atoms:
                continue
            overlap = len(atoms & other_atoms) / min(len(atoms), len(other_atoms))
            if overlap >= 0.5:
                issues.append(f"{workspace.name}: mandatory atom text overlaps {other.name} by {overlap:.0%}")
        for name in REQUIRED_REVIEWS:
            path = workspace / "review" / name
            if not path.is_file():
                continue
            review = load_yaml(path) or {}
            normalized = json.dumps({"checks": review.get("checks"), "defects": review.get("defects"), "required_changes": review.get("required_changes")}, sort_keys=True, ensure_ascii=True)
            key = (name, _norm(normalized))
            if key in review_hashes:
                issues.append(f"{workspace.name}:{name}: review content duplicates {review_hashes[key].name}")
            review_hashes[key] = workspace
    return issues


def validate_professional_workspace(workspace: Path) -> list[str]:
    return [
        *validate_source_relevance(workspace),
        *validate_decision_semantics(workspace),
        *validate_professional_reviews(workspace),
        *validate_replay_relevance(workspace),
    ]
