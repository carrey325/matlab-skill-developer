from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.common import PROJECT_ROOT, load_yaml, write_yaml_atomic
from workflow_skill_distiller.generation import render_skill
from workflow_skill_distiller.professional_profiles import PROFILES
from workflow_skill_distiller.validators import validate_skill_package


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tree_hash(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        digest.update(path.relative_to(root).as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def contract_hashes(workspace: Path) -> dict[str, str]:
    roots = [
        workspace / "task-contract.yaml",
        workspace / "source-manifest.yaml",
        workspace / "extraction",
        workspace / "synthesis",
        workspace / "alignment",
        workspace / "review",
    ]
    paths: list[Path] = []
    for root in roots:
        paths.extend([root] if root.is_file() else [item for item in root.rglob("*") if item.is_file()])
    return {path.relative_to(workspace).as_posix(): file_hash(path) for path in sorted(paths)}


def polish(workspace: Path, profile: dict) -> None:
    workflow_id = profile["workflow_id"]
    workspace = workspace.resolve()
    expected = (PROJECT_ROOT / "workspace" / workflow_id.removesuffix("-workflow")).resolve()
    if workspace != expected or workflow_id == "develop-lifetime-pd-workflow":
        raise ValueError("polish target must be one exact non-PD professional workspace")
    generated = workspace / "generated" / workflow_id
    released = PROJECT_ROOT / "workflow-skills" / profile["family"] / workflow_id
    before_contracts = contract_hashes(workspace)
    before_references = {
        path.relative_to(generated).as_posix(): file_hash(path)
        for path in sorted((generated / "references").rglob("*")) if path.is_file()
    }
    old_skill_hash = file_hash(released / "SKILL.md")

    render_skill(workspace)

    after_contracts = contract_hashes(workspace)
    after_references = {
        path.relative_to(generated).as_posix(): file_hash(path)
        for path in sorted((generated / "references").rglob("*")) if path.is_file()
    }
    if before_contracts != after_contracts:
        changed = sorted(set(before_contracts) | set(after_contracts) - {key for key in before_contracts if before_contracts.get(key) == after_contracts.get(key)})
        raise ValueError(f"editorial boundary violated; contract artifacts changed: {', '.join(changed)}")
    if before_references != after_references:
        raise ValueError("editorial boundary violated; decision/evidence reference files changed")
    issues = validate_skill_package(generated, workspace)
    if issues:
        raise ValueError("polished generated Skill failed lint:\n" + "\n".join(issues))

    shutil.copy2(generated / "SKILL.md", released / "SKILL.md")
    issues = validate_skill_package(released)
    if issues:
        raise ValueError("polished released Skill failed lint:\n" + "\n".join(issues))
    new_skill_hash = file_hash(released / "SKILL.md")
    package_hash = tree_hash(released)

    release_record = load_yaml(workspace / "professional-release.yaml")
    release_record["generated_package_sha256"] = package_hash
    write_yaml_atomic(workspace / "professional-release.yaml", release_record)
    tracker_path = PROJECT_ROOT / "planning" / "professional-deepening-status.yaml"
    tracker = load_yaml(tracker_path)
    record = next(item for item in tracker["workflows"] if item["package"] == workflow_id)
    record["released_package_sha256"] = package_hash
    write_yaml_atomic(tracker_path, tracker)
    print(f"polished {workflow_id}: SKILL {old_skill_hash} -> {new_skill_hash}; contracts/references unchanged")


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply entrypoint-only editorial polish to one released non-PD Skill.")
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--workflow", required=True, choices=sorted(PROFILES))
    args = parser.parse_args()
    try:
        polish(args.workspace, PROFILES[args.workflow])
    except (OSError, ValueError, KeyError) as exc:
        print(exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
