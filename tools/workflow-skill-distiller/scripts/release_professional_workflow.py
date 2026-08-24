from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
from pathlib import Path
from typing import Any

import _bootstrap  # noqa: F401
from workflow_skill_distiller.common import PROJECT_ROOT, load_yaml, write_yaml_atomic
from workflow_skill_distiller.coverage import coverage_report
from workflow_skill_distiller.generation import render_skill
from workflow_skill_distiller.professional import (
    validate_cross_workflow_originality,
    validate_professional_workspace,
)
from workflow_skill_distiller.professional_profiles import PROFILES
from workflow_skill_distiller.validators import (
    validate_capability_map,
    validate_knowledge_atoms,
    validate_skill_package,
    validate_source_manifest,
    validate_task_contract,
    validate_workflow_ir,
)
from workflow_skill_distiller.evidence import validate_evidence_coverage


def tree_hash(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def update_registry(profile: dict[str, Any], capability_map: dict[str, Any]) -> None:
    path = PROJECT_ROOT / "workflow-skills" / "workflow-registry.yaml"
    registry = load_yaml(path) or {"schema_version": "1.1.0", "workflows": []}
    bindings = capability_map["bindings"]
    coverage = []
    for binding in bindings:
        if not binding.get("providers"):
            continue
        for provider in binding["providers"]:
            for skill in provider.get("skills", []):
                item = {"provider": provider["provider"], "skill": skill, "coverage": binding["mapping_result"]}
                if item not in coverage:
                    coverage.append(item)
    entry = {
        "name": profile["workflow_id"],
        "family": profile["family"],
        "professional_purpose": profile["purpose"],
        "trigger_use_cases": [profile["trigger"]],
        "upstream_dependencies": profile["adjacent"],
        "downstream_dependencies": [],
        "required_capabilities": [binding["capability_id"] for binding in bindings],
        "matlab_provider_coverage": coverage,
        "known_capability_gaps": [profile["gap"]] if profile["gap"] else [],
        "evidence_version": "1.1.0",
        "workflow_version": "1.1.0",
        "release_status": "released",
    }
    by_name = {item["name"]: item for item in registry.get("workflows", [])}
    by_name[entry["name"]] = entry
    pd = by_name.pop("develop-lifetime-pd-workflow")
    ordered = [pd]
    for candidate in PROFILES.values():
        if candidate["workflow_id"] in by_name:
            ordered.append(by_name[candidate["workflow_id"]])
    registry["release_policy"] = "Only packages that pass workflow-specific professional and structural release gates appear here."
    registry["workflows"] = ordered
    write_yaml_atomic(path, registry)


def release(workspace: Path, profile: dict[str, Any]) -> None:
    workflow_id = profile["workflow_id"]
    workspace = workspace.resolve()
    expected = (PROJECT_ROOT / "workspace" / workflow_id.removesuffix("-workflow")).resolve()
    if workspace != expected:
        raise ValueError(f"workspace must be the exact individual target: {expected}")
    tracker_path = PROJECT_ROOT / "planning" / "professional-deepening-status.yaml"
    tracker = load_yaml(tracker_path)
    record = next((item for item in tracker["workflows"] if item["package"] == workflow_id), None)
    if record is None:
        raise ValueError(f"{workflow_id}: not present in the professional deepening tracker")
    unfinished = [item["package"] for item in tracker["workflows"] if item["order"] < record["order"] and item["state"] != "RELEASED"]
    if unfinished:
        raise ValueError(f"release order violation; earlier workflows are unfinished: {', '.join(unfinished)}")

    generated = workspace / "generated" / workflow_id
    verdict = load_yaml(workspace / "review" / "final-verdict.yaml") or {}
    issues = [
        *validate_task_contract(workspace / "task-contract.yaml"),
        *validate_source_manifest(workspace),
        *validate_knowledge_atoms(workspace),
        *validate_evidence_coverage(workspace),
        *validate_workflow_ir(workspace),
        *validate_capability_map(workspace),
        *validate_professional_workspace(workspace),
        *validate_skill_package(generated, workspace),
    ]
    _, coverage_issues = coverage_report(workspace)
    issues.extend(coverage_issues)
    if verdict.get("status") != "PASS" or verdict.get("human_review_required"):
        issues.append(f"final review verdict is {verdict.get('status', 'missing')}, not releasable PASS")
    previous = [PROJECT_ROOT / "workspace" / item["workspace"] for item in tracker["workflows"] if item["state"] == "RELEASED" and item["package"] != workflow_id]
    issues.extend(validate_cross_workflow_originality([*previous, workspace]))
    before = tree_hash(generated)
    rerendered = render_skill(workspace)
    after = tree_hash(rerendered)
    if before != after:
        issues.append("deterministic generation failed: identical IR changed the generated package hash")
    if issues:
        raise ValueError("\n".join(issues))

    destination = PROJECT_ROOT / "workflow-skills" / profile["family"] / workflow_id
    if destination.exists():
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(generated, destination)
    published_issues = validate_skill_package(destination)
    if published_issues:
        shutil.rmtree(destination)
        raise ValueError("published package lint failed:\n" + "\n".join(published_issues))

    release_record = load_yaml(workspace / "professional-release.yaml")
    release_record.update({"status": "RELEASED", "generated_package_sha256": after})
    write_yaml_atomic(workspace / "professional-release.yaml", release_record)
    record["state"] = "RELEASED"
    record["released_package_sha256"] = after
    write_yaml_atomic(tracker_path, tracker)
    update_registry(profile, load_yaml(workspace / "alignment" / "capability-map.yaml"))
    print(f"released {workflow_id}: {after}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Release one independently reviewed professional workflow in dependency order.")
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--workflow", required=True, choices=sorted(PROFILES))
    args = parser.parse_args()
    try:
        release(args.workspace, PROFILES[args.workflow])
    except (OSError, ValueError, KeyError) as exc:
        print(exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
