from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.common import load_yaml
from workflow_skill_distiller.coverage import coverage_report
from workflow_skill_distiller.evidence import validate_evidence_coverage
from workflow_skill_distiller.review import aggregate_reviews
from workflow_skill_distiller.professional import validate_cross_workflow_originality, validate_professional_workspace
from workflow_skill_distiller.validators import (
    validate_capability_map,
    validate_knowledge_atoms,
    validate_skill_package,
    validate_source_manifest,
    validate_task_contract,
    validate_workflow_ir,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run release gates for registry-listed professional workflow packages.")
    parser.add_argument("--workspace", required=True, type=Path, help="Parent directory containing workflow workspaces")
    parser.add_argument("--release-root", required=True, type=Path)
    parser.add_argument("--candidate", action="append", default=[], help="Also validate this workspace name before registry publication")
    args = parser.parse_args()
    registry = load_yaml(args.release_root / "workflow-registry.yaml") or {}
    workflow_ids = [item["name"] for item in registry.get("workflows", [])]
    workflow_ids.extend(args.candidate)
    workflow_ids = list(dict.fromkeys(workflow_ids))
    workspaces = []
    for workflow_id in workflow_ids:
        workspace_name = workflow_id.removesuffix("-workflow")
        path = args.workspace / workspace_name
        if (path / "synthesis" / "workflow-ir.yaml").is_file():
            workspaces.append(path)
    if not workspaces:
        print("no registry-listed or candidate workflow workspaces found", file=sys.stderr)
        return 2
    failures: list[str] = []
    for workspace in workspaces:
        checks = [
            validate_task_contract(workspace / "task-contract.yaml"), validate_source_manifest(workspace),
            validate_knowledge_atoms(workspace), validate_evidence_coverage(workspace), validate_workflow_ir(workspace),
            validate_capability_map(workspace),
        ]
        if workspace.name != "develop-lifetime-pd":
            checks.append(validate_professional_workspace(workspace))
        _, coverage_issues = coverage_report(workspace)
        checks.append(coverage_issues)
        _, review_issues = aggregate_reviews(workspace, cycle=1)
        checks.append(review_issues)
        workflow_id = load_yaml(workspace / "synthesis" / "workflow-ir.yaml")["workflow"]["id"]
        generated = workspace / "generated" / workflow_id
        checks.append(validate_skill_package(generated, workspace))
        release = next(args.release_root.rglob(workflow_id), None)
        if release is None:
            if workflow_id not in args.candidate:
                checks.append(["missing published workflow package"])
        else:
            checks.append(validate_skill_package(release))
        for issues in checks:
            failures.extend(f"{workspace.name}: {issue}" for issue in issues)
    professional_workspaces = [workspace for workspace in workspaces if workspace.name != "develop-lifetime-pd"]
    failures.extend(validate_cross_workflow_originality(professional_workspaces))
    baseline = load_yaml(args.workspace.parent / "snapshots" / "generic-family-v11-rejected-2026-08-24" / "REJECTION.yaml")
    pd = args.workspace / "develop-lifetime-pd"
    lines = []
    for path in sorted(item for item in pd.rglob("*") if item.is_file()):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {path.relative_to(args.workspace.parent)}")
    aggregate = hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()
    if aggregate != baseline["pd_baseline"]["workspace_aggregate_sha256"]:
        failures.append("develop-lifetime-pd: immutable v1.1 workspace hash changed")
    if failures:
        print("\n".join(f"- {failure}" for failure in failures), file=sys.stderr)
        return 1
    print(f"PASS: {len(workspaces)} registry-listed or candidate professional workflows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
