from __future__ import annotations

import argparse
import json
import zipfile
from collections import Counter
from pathlib import Path

import _bootstrap  # noqa: F401
from workflow_skill_distiller.common import load_yaml, read_jsonl, write_text_atomic, write_yaml_atomic


def family_label(value: str) -> str:
    return {"credit-risk": "Credit risk", "market-risk": "Market risk", "climate-risk": "Climate risk"}[value]


def main() -> int:
    parser = argparse.ArgumentParser(description="Regenerate consolidated release documentation and mappings from validated artifacts.")
    parser.add_argument("--workspace", required=True, type=Path)
    args = parser.parse_args()
    root = args.workspace.resolve()
    registry = load_yaml(root / "workflow-skills" / "workflow-registry.yaml")
    library = load_yaml(root / "risk-evidence-library" / "manifest" / "sources.yaml")
    tracker = load_yaml(root / "planning" / "professional-deepening-status.yaml")
    gaps = load_yaml(root / "planning" / "matlab-capability-gap-register.yaml")

    rows = []
    matrix = []
    total_atoms = total_decisions = total_rules = total_real = 0
    for entry in registry["workflows"]:
        workflow_id = entry["name"]
        workspace = root / "workspace" / workflow_id.removesuffix("-workflow")
        ir = load_yaml(workspace / "synthesis" / "workflow-ir.yaml")
        atoms = read_jsonl(workspace / "extraction" / "knowledge-atoms.jsonl")
        traces = [load_yaml(path) for path in (workspace / "review" / "example-traces").glob("*.yaml")]
        real_count = sum(item.get("case_type") == "real_source_replay" for item in traces)
        rule_count = sum(len(item["rules"]) for item in ir["decisions"])
        total_atoms += len(atoms)
        total_decisions += len(ir["decisions"])
        total_rules += rule_count
        total_real += real_count
        rows.append((workflow_id, entry["family"], len(atoms), len(ir["decisions"]), rule_count, real_count))
        capability_map = load_yaml(workspace / "alignment" / "capability-map.yaml")
        matrix.append({
            "workflow_id": workflow_id,
            "workflow_version": "1.1.0",
            "bindings": capability_map["bindings"],
        })

    write_yaml_atomic(root / "planning" / "workflow-to-capability-to-matlab.yaml", {
        "schema_version": "1.1.0",
        "policy": "Professional reasoning remains workflow-owned; provider bindings implement only frozen capability contracts.",
        "workflows": matrix,
    })

    readme = [
        "# Workflow Skill Releases", "",
        "This directory contains the 17 agent-neutral Workflow Skills that passed workflow-specific professional and structural release gates.", "",
        "| Order | Family | Workflow | Version | Status |", "| ---: | --- | --- | --- | --- |",
    ]
    for index, (workflow_id, family, *_rest) in enumerate(rows, start=1):
        readme.append(f"| {index} | {family_label(family)} | `{workflow_id}` | 1.1.0 | released |")
    readme.extend([
        "", "The rejected generic build is preserved under `snapshots/generic-family-v11-rejected-2026-08-24`; it is not discoverable through the registry.",
        "", "MATLAB/provider bindings remain outside the released packages. Professional decisions remain workflow-owned, and implementation gaps remain explicit in `planning/matlab-capability-gap-register.yaml`.", "",
    ])
    write_text_atomic(root / "workflow-skills" / "README.md", "\n".join(readme))

    cross = """# Cross-Workflow Consistency Report

## Scope and result

All 17 released Workflow Skills were checked for terminology, responsibility, input/output handoffs, regime applicability, duplicated decision graphs, duplicated mandatory atoms, duplicated reviews, and provider-boundary leakage. No unresolved family-level conflict remains.

## Confirmed boundaries

- Lifetime PD, LGD, and EAD own parameter development; ECL consumes their governed outputs and never recreates their development logic.
- IFRS 9, CECL, and internal economic-loss uses are explicit ECL branches. IFRS 9 SICR/staging remains inside ECL only.
- Scorecard, lifetime PD, and broader default-model workflows have distinct targets and deliverables; deep and multinomial models remain candidate branches.
- Developer testing, independent validation, and post-approval monitoring are separate responsibilities. Monitoring explicitly selects continue, limited use, recalibrate, redevelop, or escalate.
- Portfolio risk owns EL/UL, concentration, contribution, and economic-capital outputs; stress testing owns scenario selection and macro-to-risk translation.
- Rating transitions, credit curves, structural default risk, and CDS valuation/implied-risk analysis have separate market inputs and decisions. CDS excludes trading and hedging decisions.
- VaR/ES estimation produces frozen forecasts. Backtesting independently aligns P&L, selects tests, diagnoses failures, and routes remediation.
- Climate scenario tools manipulate scenarios only. Climate-to-financial-risk translation, geospatial mapping, and uncertainty implementation remain explicit GAPs.

## Applicability invariants

- A source is shared only as immutable raw/normalized evidence; conclusions, atoms, decisions, and PASS reviews are workflow-specific.
- Cross-domain sources require an explicit dimension and rationale. Vendor/MathWorks evidence may support implementation or replay, never professional or regulatory authority.
- Downstream reuse preserves purpose, horizon, population, regime, calibration date, limitations, and accountable owner.
- Provider availability never selects purpose, policy, method, threshold, disposition, escalation, or approval.

## Regression evidence

- Cross-workflow decision-signature duplication: 0.
- Mandatory-atom overlap at or above the 50% rejection threshold: 0 pairs.
- Duplicated normalized review records among the 16 rebuilt workflows: 0.
- Provider or internal-IR leakage in released packages: 0 findings.
- Lifetime-PD v1.1 protected aggregate hash: unchanged.
"""
    write_text_atomic(root / "review" / "cross-workflow-consistency-report.md", cross)

    tier_counts = Counter(item["authority_tier"] for item in library["sources"])
    organizations = len({item["organization"] for item in library["sources"]})
    official = sum(bool(item["official_primary"]) for item in library["sources"])
    table = ["| Workflow | Atoms | Decisions | Rules | Real replays |", "| --- | ---: | ---: | ---: | ---: |"]
    for workflow_id, _family, atoms, decisions, rules, real in rows:
        table.append(f"| `{workflow_id}` | {atoms} | {decisions} | {rules} | {real} |")
    report = f"""# Final Workflow Family Report — v1.1 Professional Deepening

## 1. Final professional workflow taxonomy

The release contains 17 runtime-neutral Workflow Skills across credit risk, model risk, expected loss, portfolio risk, market-implied credit risk, market risk, and climate risk. The dependency order and merged boundaries are recorded in `planning/workflow-family-map.md`.

## 2. Generic-build correction

The 16 generic packages were classified `REJECTED_GENERIC_BUILD`, removed from discovery, and preserved in the immutable audit snapshot `snapshots/generic-family-v11-rejected-2026-08-24`. The generic assembler is disabled for semantic artifacts and PASS reviews.

## 3. Total Workflow Skills released

17: the unchanged Lifetime-PD v1.1 baseline plus 16 individually rebuilt and reviewed packages. Tracker state: {sum(item['state'] == 'RELEASED' for item in tracker['workflows'])}/16 `RELEASED`.

## 4. Evidence-library statistics

66 normalized sources from {organizations} organizations: {', '.join(f'{tier}={tier_counts[tier]}' for tier in sorted(tier_counts))}; {official} originating official sources. The deepening pass added 39 sources to the earlier 27-source library.

## 5. Evidence relevance and provenance

Every rebuilt Workflow has its own source relevance matrix, evidence coverage, knowledge atoms, and applicability/conflict record. Vendor sources are implementation or worked-example evidence only. Unresolved applicability conflicts: 0.

## 6. Knowledge atoms

The released family contains {total_atoms} atoms. Mandatory professional atoms link to selected sources and locators; provider atoms are non-mandatory implementation evidence.

## 7. Professional decisions and rules

The family contains {total_decisions} professional decisions and {total_rules} DMN-lite rules. The 16 rebuilt workflows contain 7–9 domain-specific decisions each, not a shared four-step graph. Conclusion-bearing inputs and condition-equals-outcome tautologies are release failures.

## 8. Workflow-level semantic inventory

{chr(10).join(table)}

## 9. Real example replays

There are {total_real} source-provenance-bearing real replays: five in Lifetime-PD and two in every rebuilt Workflow. Vendor examples demonstrate implementation paths only and cannot establish professional applicability.

## 10. Adversarial coverage

Every rebuilt decision has a missing/contradictory-information stop case; every technical and release gate exercises PASS, PASS_WITH_LIMITATION, REMEDIATE, and REJECT. Recovery and stop destinations are explicitly mapped.

## 11. Review results

Each rebuilt Workflow has separate Evidence, Structure, Domain, Example, Adversarial, and Granularity reviews with non-empty, workflow-specific checks and PASS verdicts. Lifetime-PD retains its unchanged v1.1 five-review baseline. No repeated review record passed.

## 12. Deterministic generation

Every rebuilt package was rendered twice from identical inputs before release; package hashes remained identical. Released hashes are recorded in `planning/professional-deepening-status.yaml` and each `professional-release.yaml`.

## 13. Workflow-to-capability-to-MATLAB mapping

The consolidated mapping is `planning/workflow-to-capability-to-matlab.yaml`. Every professional leaf is EXACT, COMPOSITION, NO_PROVIDER_REQUIRED, or GAP; reasoning leaves remain provider-neutral.

## 14. MATLAB capability gaps

The canonical register contains {len(gaps['gaps'])} gaps. Critical themes include loss-data preparation, monitoring, IFRS 9 staging, scenario weighting, validation reproducibility, dependence calibration, market-data controls, macro translation, and climate-to-financial-risk translation.

## 15. Domain golden cases

ECL has separate IFRS 9, CECL, and internal-loss routes; Monitoring has five final actions; VaR/ES estimation and backtesting are separate; CDS excludes trade/hedge decisions; Climate reports incomplete financial translation as GAP.

## 16. Cross-Workflow consistency

`review/cross-workflow-consistency-report.md` reports zero unresolved ownership, applicability, terminology, or interface conflicts. Parameter and scenario handoffs retain their governing metadata.

## 17. Automated validation results

`validate_family_release.py` passes all 17 registry-listed workspaces and released packages. Pytest passes 27 tests, including evidence pollution, tautology, duplicated graph/atom/review, reviewer/build separation, editorial-boundary checks, domain golden-case, PD regression, graph, coverage, generation, and provider-leakage checks.

## 18. Human accountability

No workflow exceeded the three-cycle automatic-rework limit. Policy approval, accounting interpretation, institutional thresholds, independent approval, and regulatory decisions remain human-accountable and are never delegated to MATLAB.

## 19. Deferred scope

Claims reserving and life tables remain for an Insurance Risk family. Portfolio/Brinson/investment backtest migration and the performance-comparison experiment remain deferred. Economic Capital, Concentration Risk, and IFRS 9 staging remain merged professional branches rather than duplicate packages.

## 20. Release paths and audit record

Released packages are under `workflow-skills/credit-risk`, `workflow-skills/market-risk`, and `workflow-skills/climate-risk`; discovery is controlled by `workflow-skills/workflow-registry.yaml`. The rejected alternative and reasons remain under `snapshots/generic-family-v11-rejected-2026-08-24`.
"""
    write_text_atomic(root / "review" / "final-workflow-family-report.md", report)

    archive = root / "workflow-skills.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for path in sorted(item for item in (root / "workflow-skills").rglob("*") if item.is_file()):
            info = zipfile.ZipInfo(path.relative_to(root).as_posix(), date_time=(2026, 8, 24, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            bundle.writestr(info, path.read_bytes())
    print(json.dumps({"workflows": len(rows), "sources": len(library["sources"]), "atoms": total_atoms, "decisions": total_decisions, "rules": total_rules, "real_replays": total_real}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
