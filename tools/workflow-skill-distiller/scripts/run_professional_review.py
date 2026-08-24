from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Callable

import _bootstrap  # noqa: F401
from workflow_skill_distiller.common import load_yaml, write_yaml_atomic
from workflow_skill_distiller.coverage import coverage_report
from workflow_skill_distiller.evidence import validate_evidence_coverage
from workflow_skill_distiller.professional import (
    REQUIRED_REVIEWS,
    validate_decision_semantics,
    validate_replay_relevance,
    validate_source_relevance,
)
from workflow_skill_distiller.professional_profiles import PROFILES
from workflow_skill_distiller.review import aggregate_reviews
from workflow_skill_distiller.validators import (
    validate_capability_map,
    validate_knowledge_atoms,
    validate_source_manifest,
    validate_workflow_ir,
)


REVIEW_FILES = {
    "evidence": "evidence-review.yaml",
    "structure": "structure-review.yaml",
    "domain": "domain-review.yaml",
    "example": "example-replay-review.yaml",
    "adversarial": "adversarial-review.yaml",
    "granularity": "granularity-review.yaml",
}
FAILURE_VERDICTS = {
    "evidence": "RESEARCH_MORE",
    "structure": "RESYNTHESIZE",
    "domain": "RESYNTHESIZE",
    "example": "REGENERATE",
    "adversarial": "REGENERATE",
    "granularity": "REGRANULARIZE",
}


def adversarial_issues(workspace: Path) -> list[str]:
    ir = load_yaml(workspace / "synthesis" / "workflow-ir.yaml")
    traces = [load_yaml(path) for path in (workspace / "review" / "example-traces").glob("*.yaml")]
    issues = []
    for decision in ir["decisions"]:
        expected = f"EX-ADV-{ir['workflow']['id'].split('-workflow')[0]}"
        found = any(
            trace.get("case_type") == "synthetic_adversarial"
            and any(item == decision["id"] for item in [expected_decision.get("decision_id") for expected_decision in trace.get("expected_decisions", [])])
            for trace in traces
        )
        missing_found = any(
            trace.get("case_type") == "synthetic_adversarial"
            and f"NODE-DECISION-{decision['id'].removeprefix('DEC-')}" in trace.get("mapped_nodes", [])
            and "NODE-STOP" in trace.get("expected_recovery_or_stop", [])
            for trace in traces
        )
        if not found:
            issues.append(f"{decision['id']}: no rule-bearing adversarial trace")
        if not missing_found:
            issues.append(f"{decision['id']}: no missing-information stop trace")
    expected_outcomes = {f"{gate['id']}:{outcome['name']}" for gate in ir["validation_gates"] for outcome in gate["outcomes"]}
    actual_outcomes = {f"{item['gate_id']}:{item['outcome']}" for trace in traces for item in trace.get("expected_validation", [])}
    for missing in sorted(expected_outcomes - actual_outcomes):
        issues.append(f"missing gate adversarial outcome {missing}")
    return issues


def run_review(workspace: Path, profile: dict, review_type: str) -> None:
    ir = load_yaml(workspace / "synthesis" / "workflow-ir.yaml")
    counts = {
        "decisions": len(ir["decisions"]),
        "rules": sum(len(item["rules"]) for item in ir["decisions"]),
        "tasks": sum(bool(item.get("leaf")) for item in ir["tasks"]),
    }
    if review_type == "evidence":
        issues = [*validate_source_manifest(workspace), *validate_source_relevance(workspace), *validate_knowledge_atoms(workspace), *validate_evidence_coverage(workspace)]
        checks = [("source relevance and applicability", profile["reviews"]["evidence"], ["extraction/source-relevance.yaml", "extraction/source-conflicts.yaml"]), ("mandatory professional support", f"Inspected {counts['rules']} rules and their mandatory source/locator mappings; vendor evidence remains implementation-only.", ["extraction/knowledge-atoms.jsonl", "extraction/evidence-coverage.yaml"])]
    elif review_type == "structure":
        issues = validate_workflow_ir(workspace)
        checks = [("graph integrity", f"Inspected the {profile['short']} graph with {counts['decisions']} decisions, two separately assessed gates, recovery, stop, and terminal routes.", ["synthesis/workflow-ir.yaml"]), ("decision inspectability", f"Inspected {counts['rules']} rules for referenced inputs, outcomes, fallbacks, evidence, and reachable control-flow routes.", ["synthesis/decisions"])]
    elif review_type == "domain":
        issues = validate_decision_semantics(workspace)
        checks = [("professional reasoning", profile["reviews"]["domain"], ["synthesis/domain-model.yaml", "synthesis/inference-model.yaml", "synthesis/task-model.yaml"]), ("responsibility boundary", f"Inspected the {profile['short']} trigger and exclusions: {', '.join(profile['exclusions'])}.", ["task-contract.yaml", "synthesis/workflow-ir.yaml"])]
    elif review_type == "example":
        _, coverage_issues = coverage_report(workspace)
        issues = [*coverage_issues, *validate_replay_relevance(workspace)]
        real = sum((load_yaml(path) or {}).get("case_type") == "real_source_replay" for path in (workspace / "review" / "example-traces").glob("*.yaml"))
        checks = [("real provenance and path rationale", profile["reviews"]["replay"], ["review/example-traces"]), ("semantic coverage", f"Inspected {real} real replays and verified explicit decision rule, validation, output, provenance, and limitation expectations.", ["review/coverage-targets.yaml", "review/coverage-report.yaml"])]
    elif review_type == "adversarial":
        issues = adversarial_issues(workspace)
        checks = [("missing and conflicting evidence", f"Inspected one stop case for each of the {counts['decisions']} named {profile['short']} decisions; no case may infer a route from a missing input.", ["review/example-traces"]), ("gate disposition routes", f"Inspected PASS, PASS_WITH_LIMITATION, REMEDIATE, and REJECT for both {profile['short']} assessment gates and their recovery/stop destinations.", ["review/coverage-targets.yaml", "synthesis/workflow-ir.yaml"])]
    else:
        issues = validate_capability_map(workspace)
        checks = [("professional leaf ownership", profile["reviews"]["granularity"], ["alignment/granularity-report.md", "alignment/capability-map.yaml"]), ("implementation boundary and gaps", f"Inspected {counts['tasks']} leaves. {profile['gap']}", ["alignment/capability-map.yaml", "alignment/matlab-refactor-plan.md"])]

    status = "PASS" if not issues else FAILURE_VERDICTS[review_type]
    value = {
        "schema_version": "1.1.0",
        "reviewer": f"{profile['short'].casefold()}-{review_type}-reviewer",
        "status": status,
        "cycle": 1,
        "checks": [{"dimension": dimension, "status": "PASS" if not issues else "FAIL", "notes": notes, "evidence": evidence} for dimension, notes, evidence in checks],
        "defects": issues,
        "required_changes": issues,
        "human_review_required": False,
    }
    write_yaml_atomic(workspace / "review" / REVIEW_FILES[review_type], value)
    present = {path.name for path in (workspace / "review").glob("*review.yaml")}
    if REQUIRED_REVIEWS <= present:
        aggregate_reviews(workspace, cycle=1)
        release = load_yaml(workspace / "professional-release.yaml") or {}
        release["status"] = "REVIEW"
        write_yaml_atomic(workspace / "professional-release.yaml", release)
    print(f"{profile['workflow_id']} {review_type}: {status} ({len(issues)} findings)")
    if issues:
        raise ValueError("\n".join(issues))


def main() -> int:
    parser = argparse.ArgumentParser(description="Run one independent professional reviewer against one workflow.")
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--workflow", required=True, choices=sorted(PROFILES))
    parser.add_argument("--review-type", required=True, choices=sorted(REVIEW_FILES))
    args = parser.parse_args()
    try:
        run_review(args.workspace.resolve(), PROFILES[args.workflow], args.review_type)
    except (OSError, ValueError, KeyError) as exc:
        print(exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
