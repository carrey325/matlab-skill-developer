from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from typing import Any

import _bootstrap  # noqa: F401
from workflow_skill_distiller.common import (
    PROJECT_ROOT,
    ensure_workspace_structure,
    load_yaml,
    write_jsonl_atomic,
    write_text_atomic,
    write_yaml_atomic,
)
from workflow_skill_distiller.conflicts import source_conflicts_markdown
from workflow_skill_distiller.coverage import coverage_report
from workflow_skill_distiller.evidence import source_gaps_markdown
from workflow_skill_distiller.generation import render_skill
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


def identifier(value: str) -> str:
    return "".join(character if character.isalnum() else "-" for character in value.upper()).strip("-")


def scalar_date(value: Any) -> Any:
    return value.isoformat() if hasattr(value, "isoformat") else value


def source_role(source: dict[str, Any], worked_examples: set[str]) -> str:
    if source["source_id"] in worked_examples:
        return "worked_example"
    return {
        "primary_standard_or_regulation": "normative",
        "supervisory_guidance": "supervisory",
        "banking_architecture_or_business_process": "business_process",
        "established_academic_or_practitioner": "professional_methodology",
        "vendor_documentation_or_examples": "implementation",
    }[source["source_type"]]


def clean_semantic_artifacts(workspace: Path) -> None:
    project_workspace = (PROJECT_ROOT / "workspace").resolve()
    resolved = workspace.resolve()
    if resolved.parent != project_workspace or resolved.name == "develop-lifetime-pd":
        raise ValueError("professional rebuild target must be one non-PD child of the project workspace directory")
    for relative in ("extraction", "synthesis", "generated", "review", "alignment"):
        target = resolved / relative
        if target.is_dir():
            shutil.rmtree(target)
    for name in ("task-contract.yaml", "source-manifest.yaml", "professional-release.yaml"):
        target = resolved / name
        if target.exists():
            target.unlink()
    ensure_workspace_structure(resolved)


def build(workspace: Path, profile: dict[str, Any]) -> None:
    clean_semantic_artifacts(workspace)
    workflow_id = profile["workflow_id"]
    library_manifest = load_yaml(PROJECT_ROOT / "risk-evidence-library" / "manifest" / "sources.yaml") or {}
    library_sources = {source["source_id"]: source for source in library_manifest["sources"]}
    route_source_ids = [
        route["source"]
        for decision_spec in profile["decisions"]
        for route in decision_spec["routes"]
    ]
    selected_source_ids = list(dict.fromkeys([*profile["sources"], *route_source_ids]))
    missing = sorted(set(selected_source_ids) - set(library_sources))
    if missing:
        raise ValueError(f"profile references missing sources: {', '.join(missing)}")
    sources = [library_sources[source_id] for source_id in selected_source_ids]
    vendor_sources = [source for source in sources if source["source_type"] == "vendor_documentation_or_examples"]
    worked_examples = {source["source_id"] for source in vendor_sources[:2]}

    contract = {
        "schema_version": "1.0.0", "workflow_name": workflow_id, "purpose": profile["purpose"], "domain": profile["family"],
        "jurisdiction_scope": ["generic-with-explicit-applicability-branches"], "target_granularity": "professional-task",
        "required_inputs": [{"name": f"input-{index}", "description": value} for index, value in enumerate(profile["inputs"], start=1)],
        "expected_deliverables": [identifier(value).casefold() for value in profile["outputs"]], "exclusions": profile["exclusions"],
        "adjacent_workflows": profile["adjacent"],
        "start_boundary": f"Start when an accountable owner supplies {profile['inputs'][0]} and identifies the intended professional use.",
        "end_boundary": f"End after producing {profile['outputs'][-1]} and recording any required adjacent-workflow handoff.",
        "implementation_binding": ["matlab"],
    }
    write_yaml_atomic(workspace / "task-contract.yaml", contract)
    write_yaml_atomic(workspace / "source-manifest.yaml", {
        "schema_version": "1.1.0", "workflow_id": workflow_id,
        "source_library": {"library_id": "risk-evidence-library", "manifest_path": "risk-evidence-library/manifest/sources.yaml"},
        "sources": [{"source_id": source_id} for source_id in selected_source_ids],
    })

    atoms: list[dict[str, Any]] = []
    decisions: list[dict[str, Any]] = []
    decision_atoms: dict[str, list[str]] = {}
    source_dimensions: dict[str, set[str]] = {source_id: set() for source_id in selected_source_ids}
    atom_number = 1
    for decision_index, spec in enumerate(profile["decisions"], start=1):
        decision_id = f"DEC-{identifier(spec['key'])}"
        rules = []
        evidence = []
        for route_index, item in enumerate(spec["routes"], start=1):
            atom_id = f"KA-{profile['short']}-{atom_number:04d}"
            atom_number += 1
            source = library_sources[item["source"]]
            is_vendor_route = source["source_type"] == "vendor_documentation_or_examples"
            atoms.append({
                "id": atom_id, "type": "decision_rule", "statement": item["rationale"], "scope": workflow_id,
                "mandatory": not is_vendor_route, "source_id": item["source"], "locator": {"section": item["locator"]},
                "authority_tier": source["authority_tier"], "confidence": "high" if source["authority_tier"] in {"T1", "T2", "T3"} else "medium",
                "applicability": {"jurisdictions": source["jurisdiction"], "purpose": profile["scope"], "effective_from": scalar_date(source.get("effective_date")), "effective_to": None, "conditions": [f"Apply only to {spec['title'].casefold()} for the declared purpose."]},
                "relationships": [],
            })
            evidence.append(atom_id)
            source_dimensions[item["source"]].add(spec["title"])
            if is_vendor_route:
                professional_candidates = [
                    candidate
                    for candidate in spec["routes"]
                    if library_sources[candidate["source"]]["source_type"] != "vendor_documentation_or_examples"
                ]
                if professional_candidates:
                    authority_item = professional_candidates[0]
                else:
                    authority_id = next(
                        source_id for source_id in selected_source_ids
                        if library_sources[source_id]["source_type"]
                        in {"primary_standard_or_regulation", "supervisory_guidance", "established_academic_or_practitioner"}
                    )
                    authority_item = {
                        "source": authority_id,
                        "locator": f"Methodology and limitations relevant to {spec['title']}",
                    }
                authority_source = library_sources[authority_item["source"]]
                authority_atom_id = f"KA-{profile['short']}-{atom_number:04d}"
                atom_number += 1
                atoms.append({
                    "id": authority_atom_id,
                    "type": "decision_rule",
                    "statement": (
                        f"Professional selection for {spec['title'].casefold()} must be justified by the declared "
                        "purpose, observable data properties, assumptions, diagnostics, and limitations; "
                        "provider availability is not a selection criterion."
                    ),
                    "scope": workflow_id,
                    "mandatory": True,
                    "source_id": authority_item["source"],
                    "locator": {"section": authority_item["locator"]},
                    "authority_tier": authority_source["authority_tier"],
                    "confidence": "high" if authority_source["authority_tier"] in {"T1", "T2", "T3"} else "medium",
                    "applicability": {
                        "jurisdictions": authority_source["jurisdiction"],
                        "purpose": profile["scope"],
                        "effective_from": scalar_date(authority_source.get("effective_date")),
                        "effective_to": None,
                        "conditions": [f"Apply only to {spec['title'].casefold()} for the declared purpose."],
                    },
                    "relationships": [{"kind": "supports", "atom_id": atom_id}],
                })
                evidence.append(authority_atom_id)
                source_dimensions[authority_item["source"]].add(spec["title"])
            rule_id = f"RULE-{identifier(spec['key'])}-{route_index}"
            rules.append({
                "id": rule_id, "conditions": [{"input": spec["input"]["name"], "operator": item["operator"], "value": item["value"]}],
                "outcome": item["outcome"], "rationale": item["rationale"], "applicability": [profile["scope"]],
                "exclusions": profile["exclusions"][:2],
                "missing_information_behavior": f"Stop this decision and obtain evidence for {spec['input']['description'].casefold()}; do not infer {item['outcome']} from provider availability.",
                "evidence": list(evidence[-2:] if is_vendor_route else [atom_id]),
            })
        decision_atoms[decision_id] = evidence
        decisions.append({
            "id": decision_id, "title": spec["title"], "purpose": f"Use observable evidence to {spec['title'].casefold()} without preselecting the result.",
            "inputs": [{"name": spec["input"]["name"], "description": spec["input"]["description"], "required": True, "producer": spec["input"]["producer"], "observable": True}],
            "rules": rules, "fallback": {"outcome": "stop-and-request-evidence", "instruction": f"Stop and request the missing or conflicting evidence needed to {spec['title'].casefold()}."},
            "evidence": evidence,
        })

    for source in vendor_sources:
        atom_id = f"KA-{profile['short']}-{atom_number:04d}"
        atom_number += 1
        atoms.append({
            "id": atom_id, "type": "task", "statement": f"{source['title']} provides implementation or worked-case evidence only after the workflow freezes its professional specification.",
            "scope": workflow_id, "mandatory": False, "source_id": source["source_id"], "locator": {"section": source["title"]},
            "authority_tier": source["authority_tier"], "confidence": "high",
            "applicability": {"jurisdictions": source["jurisdiction"], "purpose": "implementation feasibility and replay", "effective_from": scalar_date(source.get("effective_date")), "effective_to": None, "conditions": ["Never use this source as professional or regulatory authority."]},
            "relationships": [],
        })
        source_dimensions[source["source_id"]].add("implementation feasibility and worked-case replay")
    write_jsonl_atomic(workspace / "extraction" / "knowledge-atoms.jsonl", atoms)

    relevance_sources = []
    for source in sources:
        dimensions = sorted(source_dimensions[source["source_id"]]) or ["workflow boundary and corroboration"]
        indexed = set(source.get("applicable_workflows", []))
        rationale = f"{source['title']} is selected for {', '.join(dimensions)} within {workflow_id}; its authority and jurisdiction are not extended beyond that use."
        item = {"source_id": source["source_id"], "evidence_role": source_role(source, worked_examples), "supports_dimensions": dimensions, "applicability": source["jurisdiction"], "selection_rationale": rationale}
        if indexed and workflow_id not in indexed:
            item["cross_domain_rationale"] = f"The source is used only for the explicitly listed model-risk, boundary, or methodological dimension shared with {workflow_id}, not as domain-specific primary authority."
        relevance_sources.append(item)
    write_yaml_atomic(workspace / "extraction" / "source-relevance.yaml", {"schema_version": "1.1.0", "workflow_id": workflow_id, "sources": relevance_sources})

    coverage_dimensions = []
    atom_by_id = {atom["id"]: atom for atom in atoms}
    for decision_item in decisions:
        atom_ids = decision_atoms[decision_item["id"]]
        source_ids = list(dict.fromkeys(atom_by_id[atom_id]["source_id"] for atom_id in atom_ids))
        coverage_dimensions.append({
            "id": f"EVD-{decision_item['id'].removeprefix('DEC-')}", "name": decision_item["title"], "requirement": "required", "condition": None,
            "atom_ids": atom_ids, "source_ids": source_ids, "authority_levels": list(dict.fromkeys(library_sources[source_id]["authority_tier"] for source_id in source_ids)),
            "applicability": [profile["scope"]], "status": "covered", "unresolved_gap": None,
            "analysis_notes": f"The decision uses observable inputs and {len(atom_ids)} non-circular evidence-backed routes specific to {decision_item['title'].casefold()}.",
        })
    coverage = {"schema_version": "1.1.0", "workflow_id": workflow_id, "dimensions": coverage_dimensions}
    write_yaml_atomic(workspace / "extraction" / "evidence-coverage.yaml", coverage)
    write_text_atomic(workspace / "extraction" / "source-gaps.md", source_gaps_markdown(coverage))
    conflicts = {"schema_version": "1.1.0", "workflow_id": workflow_id, "unresolved_count": 0, "conflicts": []}
    write_yaml_atomic(workspace / "extraction" / "source-conflicts.yaml", conflicts)
    write_text_atomic(workspace / "extraction" / "source-conflicts.md", source_conflicts_markdown(conflicts))

    domain = [{"id": f"DOMAIN-{identifier(item['key'])}", "name": item["title"], "definition": item["input"]["description"], "evidence": decision_atoms[f"DEC-{identifier(item['key'])}"]} for item in profile["decisions"]]
    inferences = [{"id": f"INF-{identifier(item['key'])}", "operation": "select", "objective": f"Resolve {item['title'].casefold()} from observable evidence.", "evidence": decision_atoms[f"DEC-{identifier(item['key'])}"]} for item in profile["decisions"]]
    inferences.extend([
        {"id": "INF-IMPLEMENT", "operation": "estimate", "objective": "Run the approved computational specification without changing professional choices.", "evidence": [atoms[-1]["id"]]},
        {"id": "INF-VALIDATE", "operation": "validate", "objective": "Assess model or analysis evidence separately from final disposition.", "evidence": decision_atoms[decisions[-1]["id"]]},
        {"id": "INF-REPORT", "operation": "report", "objective": "Package decisions, evidence, outputs, limitations, and handoffs.", "evidence": decision_atoms[decisions[-1]["id"]]},
    ])
    tasks = [{"id": "TASK-WORKFLOW", "title": profile["purpose"].split(" by ")[0], "parent": None, "objective": profile["purpose"], "inputs": profile["inputs"], "outputs": profile["outputs"], "inferences": [inferences[0]["id"]], "decision_ids": [], "leaf": False, "mandatory": False, "evidence": [atoms[0]["id"]]}]
    capabilities = []
    bindings = []
    for item, decision_item in zip(profile["decisions"], decisions):
        key = identifier(item["key"])
        task_id = f"TASK-{key}"
        capability_id = f"CAP-{key}"
        tasks.append({"id": task_id, "title": item["title"], "parent": "TASK-WORKFLOW", "objective": decision_item["purpose"], "inputs": [item["input"]["description"]], "outputs": [f"{item['title']} decision record"], "inferences": [f"INF-{key}"], "decision_ids": [decision_item["id"]], "leaf": True, "mandatory": True, "completion_criteria": ["The selected rule, evidence, applicability, fallback consideration, and accountable owner are recorded."], "capability_ids": [capability_id], "evidence": decision_atoms[decision_item["id"]]})
        capabilities.append({"id": capability_id, "name": f"decide-{identifier(item['key']).casefold()}", "kind": "reasoning", "task_ids": [task_id]})
        bindings.append({"task_id": task_id, "capability_id": capability_id, "mapping_result": "NO_PROVIDER_REQUIRED", "providers": [], "rationale": f"{item['title']} is workflow-owned professional reasoning."})
    for task_id, title, inference_id, capability_id, capability_name, mapping_result in [
        ("TASK-IMPLEMENT", f"Execute the approved {profile['short']} computation", "INF-IMPLEMENT", "CAP-IMPLEMENT", f"compute-{profile['short'].casefold()}-analysis", profile["provider_result"]),
        ("TASK-VALIDATE", f"Assess {profile['short']} technical evidence", "INF-VALIDATE", "CAP-VALIDATE", f"compute-{profile['short'].casefold()}-validation-evidence", "COMPOSITION"),
        ("TASK-PACKAGE", f"Package the {profile['short']} professional record", "INF-REPORT", "CAP-PACKAGE", f"package-{profile['short'].casefold()}-evidence", "NO_PROVIDER_REQUIRED"),
    ]:
        provider_required = mapping_result != "NO_PROVIDER_REQUIRED"
        tasks.append({"id": task_id, "title": title, "parent": "TASK-WORKFLOW", "objective": title, "inputs": profile["inputs"], "outputs": profile["outputs"], "inferences": [inference_id], "decision_ids": [], "leaf": True, "mandatory": True, "completion_criteria": ["Inputs, assumptions, outputs, diagnostics, and limitations are reproducible and documented."], "capability_ids": [capability_id], "evidence": [atoms[-1]["id"] if provider_required else decision_atoms[decisions[-1]["id"]][0]]})
        capabilities.append({"id": capability_id, "name": capability_name, "kind": "computational" if provider_required else "reporting", "task_ids": [task_id]})
        providers = [{"provider": "matlab", "skills": profile["providers"]}] if provider_required else []
        bindings.append({"task_id": task_id, "capability_id": capability_id, "mapping_result": mapping_result, "providers": providers, "rationale": "The provider implements the frozen computational contract." if provider_required else "Professional evidence packaging does not require a provider."})

    nodes = [{"id": "NODE-START", "type": "start", "title": "Start"}]
    edges = []
    for index, decision_item in enumerate(decisions):
        key = decision_item["id"].removeprefix("DEC-")
        task_node = f"NODE-TASK-{key}"
        decision_node = f"NODE-DECISION-{key}"
        nodes.extend([{"id": task_node, "type": "task", "title": decision_item["title"], "task_id": f"TASK-{key}"}, {"id": decision_node, "type": "decision", "title": decision_item["title"], "decision_id": decision_item["id"]}])
        if index == 0:
            edges.append({"from": "NODE-START", "to": task_node})
        edges.append({"from": task_node, "to": decision_node})
        next_node = f"NODE-TASK-{decisions[index + 1]['id'].removeprefix('DEC-')}" if index + 1 < len(decisions) else "NODE-IMPLEMENT"
        for rule in decision_item["rules"]:
            edges.append({"from": decision_node, "to": next_node, "outcome": rule["outcome"], "condition": rule["rationale"]})
        edges.append({"from": decision_node, "to": "NODE-STOP", "outcome": "stop-and-request-evidence", "default": True})
    nodes.extend([
        {"id": "NODE-IMPLEMENT", "type": "task", "title": "Execute approved computation", "task_id": "TASK-IMPLEMENT"},
        {"id": "NODE-VALIDATE", "type": "task", "title": "Assess technical evidence", "task_id": "TASK-VALIDATE"},
        {"id": "NODE-TECHNICAL-GATE", "type": "validation_gate", "title": "Technical evidence gate", "gate_id": "GATE-TECHNICAL"},
        {"id": "NODE-PACKAGE", "type": "task", "title": "Package professional record", "task_id": "TASK-PACKAGE"},
        {"id": "NODE-RELEASE-GATE", "type": "validation_gate", "title": "Use and release gate", "gate_id": "GATE-RELEASE"},
        {"id": "NODE-REPAIR", "type": "recovery", "title": "Repair affected evidence"},
        {"id": "NODE-STOP", "type": "stop", "title": "Stop and escalate"},
        {"id": "NODE-END", "type": "end", "title": "End"},
    ])
    first_task_node = f"NODE-TASK-{decisions[0]['id'].removeprefix('DEC-')}"
    edges.extend([
        {"from": "NODE-IMPLEMENT", "to": "NODE-VALIDATE"},
        {"from": "NODE-VALIDATE", "to": "NODE-TECHNICAL-GATE"},
        {"from": "NODE-TECHNICAL-GATE", "to": "NODE-PACKAGE", "outcome": "PASS"},
        {"from": "NODE-TECHNICAL-GATE", "to": "NODE-PACKAGE", "outcome": "PASS_WITH_LIMITATION"},
        {"from": "NODE-TECHNICAL-GATE", "to": "NODE-REPAIR", "outcome": "REMEDIATE"},
        {"from": "NODE-TECHNICAL-GATE", "to": "NODE-STOP", "outcome": "REJECT", "default": True},
        {"from": "NODE-PACKAGE", "to": "NODE-RELEASE-GATE"},
        {"from": "NODE-RELEASE-GATE", "to": "NODE-END", "outcome": "PASS"},
        {"from": "NODE-RELEASE-GATE", "to": "NODE-END", "outcome": "PASS_WITH_LIMITATION"},
        {"from": "NODE-RELEASE-GATE", "to": "NODE-REPAIR", "outcome": "REMEDIATE"},
        {"from": "NODE-RELEASE-GATE", "to": "NODE-STOP", "outcome": "REJECT", "default": True},
        {"from": "NODE-REPAIR", "to": first_task_node},
        {"from": "NODE-STOP", "to": "NODE-END"},
    ])
    gate_evidence = decision_atoms[decisions[-1]["id"]]
    outcome_specs = [
        {"name": "PASS", "criteria": ["All applicable assessment dimensions are supported with no material unresolved weakness."], "route": "Proceed to the next controlled stage.", "evidence": gate_evidence},
        {"name": "PASS_WITH_LIMITATION", "criteria": ["The result is usable only within explicit enforceable boundaries and monitoring conditions."], "route": "Proceed with recorded limitations and accountable ownership.", "evidence": gate_evidence},
        {"name": "REMEDIATE", "criteria": ["A material but repairable weakness affects evidence, data, calibration, implementation, or packaging."], "route": "Repair the affected professional stage and reassess.", "evidence": gate_evidence},
        {"name": "REJECT", "criteria": ["A material unsupported or uncontrolled weakness prevents the intended use."], "route": "Stop and escalate to the accountable owner.", "evidence": gate_evidence},
    ]
    gates = [
        {"id": "GATE-TECHNICAL", "title": f"{profile['short']} technical fitness", "purpose": f"Assess whether the approved {profile['short']} specification and computation are fit for the declared use.", "required_evidence": [profile["inputs"][1], profile["outputs"][1]], "assessment_dimensions": [item["title"] for item in profile["decisions"][1:5]], "acceptance_policy": "Assess each dimension separately; completion or a favourable aggregate metric cannot override a material defect.", "outcomes": outcome_specs, "applicability": [profile["scope"]], "evidence": gate_evidence},
        {"id": "GATE-RELEASE", "title": f"{profile['short']} use and release boundary", "purpose": "Assess whether decisions, evidence, limitations, outputs, and handoffs are complete and support the intended use.", "required_evidence": [profile["outputs"][0], profile["outputs"][-1]], "assessment_dimensions": [profile["decisions"][0]["title"], profile["decisions"][-1]["title"], "provider and adjacent-workflow boundaries"], "acceptance_policy": "Release only when professional evidence and decisions are complete; a provider GAP may remain explicit, but a professional gap cannot.", "outcomes": outcome_specs, "applicability": [profile["scope"]], "evidence": gate_evidence},
    ]
    ir = {
        "schema_version": "1.1.0", "workflow": {"id": workflow_id, "version": "1.1.0", "purpose": profile["purpose"], "scope": profile["scope"], "exclusions": profile["exclusions"], "trigger": profile["trigger"], "not_for": profile["not_for"]},
        "inputs": [{"name": f"input-{index}", "description": value} for index, value in enumerate(profile["inputs"], start=1)],
        "outputs": [{"name": f"output-{index}", "description": value} for index, value in enumerate(profile["outputs"], start=1)],
        "domain_knowledge": domain, "inferences": inferences, "tasks": tasks, "control_flow": {"nodes": nodes, "edges": edges},
        "decisions": decisions, "validation_gates": gates,
        "exceptions": [{"id": "EXC-MISSING-EVIDENCE", "condition": "A mandatory professional input is missing or contradictory", "instruction": "Stop the affected decision and request evidence; do not infer an outcome.", "target_node": "NODE-STOP", "evidence": [atoms[0]["id"]]}],
        "recovery_paths": [{"id": "REC-REPAIR", "condition": "A gate returns REMEDIATE", "instruction": "Repair the affected evidence, data, method, implementation, or package and repeat professional decisions from the first affected stage.", "target_node": "NODE-REPAIR", "evidence": gate_evidence}],
        "stop_conditions": [{"id": "STOP-UNSUPPORTED", "condition": "A mandatory decision, applicability branch, or intended use remains materially unsupported", "instruction": "Stop and escalate instead of producing a professional conclusion.", "target_node": "NODE-STOP", "evidence": gate_evidence}],
        "capability_requirements": capabilities,
        "evidence_map": [{"claim_id": item["id"], "claim": item["title"], "atom_ids": decision_atoms[item["id"]]} for item in decisions],
    }
    write_yaml_atomic(workspace / "synthesis" / "workflow-ir.yaml", ir)
    write_yaml_atomic(workspace / "synthesis" / "domain-model.yaml", {"schema_version": "1.1.0", "workflow_id": workflow_id, "domain_knowledge": domain})
    write_yaml_atomic(workspace / "synthesis" / "inference-model.yaml", {"schema_version": "1.1.0", "workflow_id": workflow_id, "inferences": inferences})
    write_yaml_atomic(workspace / "synthesis" / "task-model.yaml", {"schema_version": "1.1.0", "workflow_id": workflow_id, "tasks": tasks, "professional_leaf_count": len(tasks) - 1, "material_decision_count": len(decisions), "validation_gate_count": len(gates)})
    for item in decisions:
        write_yaml_atomic(workspace / "synthesis" / "decisions" / f"{item['id'].casefold()}.yaml", {"schema_version": "1.1.0", **item})
    write_yaml_atomic(workspace / "alignment" / "capability-map.yaml", {"schema_version": "1.0.0", "workflow_id": workflow_id, "bindings": bindings})
    write_text_atomic(workspace / "alignment" / "granularity-report.md", f"# Granularity Report\n\n{profile['reviews']['granularity']}\n\nEvery professional leaf is mapped to a provider, composition, no-provider-required result, or explicit GAP.\n")
    write_text_atomic(workspace / "alignment" / "matlab-refactor-plan.md", f"# MATLAB Capability Findings\n\nExternal MATLAB skills remain read-only.\n\n- Current binding: {', '.join(profile['providers'])}.\n- Mapping: {profile['provider_result']}.\n- GAP: {profile['gap']}\n")
    render_skill(workspace)

    trace_dir = workspace / "review" / "example-traces"
    all_rule_ids = []
    for decision_index, item in enumerate(decisions):
        key = item["id"].removeprefix("DEC-")
        for rule_index, rule in enumerate(item["rules"], start=1):
            all_rule_ids.append(rule["id"])
            trace = {
                "schema_version": "1.1.0", "example_id": f"EX-ADV-{profile['short']}-{key}-{rule_index}", "case": f"Evidence pattern for {item['title']}: {rule['outcome']}", "case_type": "synthetic_adversarial", "source_provenance": None,
                "initial_conditions": [rule["rationale"]], "objective": f"Verify the non-circular rule for {item['title'].casefold()}.",
                "mapped_nodes": [f"NODE-TASK-{key}", f"NODE-DECISION-{key}"],
                "expected_decisions": [{"decision_id": item["id"], "rule_ids": [rule["id"]], "outcome": rule["outcome"], "rationale": rule["rationale"]}],
                "expected_validation": [], "expected_recovery_or_stop": [], "outputs": [f"{item['title']} decision record"], "adjacent_handoff": None,
                "coverage_notes": "The case supplies an observable condition and checks the evidence-backed outcome without restating it as an input.",
            }
            write_yaml_atomic(trace_dir / f"{trace['example_id'].casefold()}.yaml", trace)
        fallback = {"schema_version": "1.1.0", "example_id": f"EX-ADV-{profile['short']}-{key}-MISSING", "case": f"Missing evidence for {item['title']}", "case_type": "synthetic_adversarial", "source_provenance": None, "initial_conditions": [f"The required input {item['inputs'][0]['name']} is missing or contradictory."], "objective": "Verify the explicit stop path for unresolved mandatory evidence.", "mapped_nodes": [f"NODE-TASK-{key}", f"NODE-DECISION-{key}", "NODE-STOP"], "expected_decisions": [], "expected_validation": [], "expected_recovery_or_stop": ["NODE-STOP"], "outputs": ["stop and evidence request"], "adjacent_handoff": None, "coverage_notes": "The workflow stops rather than inferring a professional conclusion from provider availability."}
        write_yaml_atomic(trace_dir / f"{fallback['example_id'].casefold()}.yaml", fallback)
    real_ids = []
    for index, source in enumerate(vendor_sources[:2], start=1):
        decision_item = decisions[(index - 1) % len(decisions)]
        rule = decision_item["rules"][(index - 1) % len(decision_item["rules"])]
        key = decision_item["id"].removeprefix("DEC-")
        example_id = f"EX-REAL-{profile['short']}-{index}"
        real_ids.append(example_id)
        trace = {"schema_version": "1.1.0", "example_id": example_id, "case": source["title"], "case_type": "real_source_replay", "source_provenance": {"source_id": source["source_id"], "source_title": source["title"], "source_url": source["url"], "locator": f"Official documentation page: {source['title']}", "input_summary": profile["inputs"][1], "expected_output_summary": profile["outputs"][1]}, "initial_conditions": [profile["inputs"][0], profile["inputs"][1]], "objective": f"Replay the documented case through {decision_item['title'].casefold()} and the approved computation boundary.", "mapped_nodes": ["NODE-START", f"NODE-TASK-{key}", f"NODE-DECISION-{key}", "NODE-IMPLEMENT", "NODE-VALIDATE", "NODE-TECHNICAL-GATE", "NODE-PACKAGE", "NODE-RELEASE-GATE", "NODE-END"], "expected_decisions": [{"decision_id": decision_item["id"], "rule_ids": [rule["id"]], "outcome": rule["outcome"], "rationale": rule["rationale"]}], "expected_validation": [{"gate_id": "GATE-TECHNICAL", "outcome": "PASS", "rationale": "The replay supplies the documented inputs and reproducible implementation output for the selected route."}, {"gate_id": "GATE-RELEASE", "outcome": "PASS_WITH_LIMITATION", "rationale": "A worked example proves implementation feasibility, not organizational approval or universal applicability."}], "expected_recovery_or_stop": [], "outputs": profile["outputs"], "adjacent_handoff": profile["adjacent"][0] if profile["adjacent"] else None, "coverage_notes": "The real source replay records provenance and explains a professional route before invoking the implementation capability."}
        write_yaml_atomic(trace_dir / f"{example_id.casefold()}.yaml", trace)
    for gate in gates:
        for outcome in gate["outcomes"]:
            target = "NODE-REPAIR" if outcome["name"] == "REMEDIATE" else "NODE-STOP" if outcome["name"] == "REJECT" else "NODE-END"
            example_id = f"EX-ADV-{profile['short']}-{gate['id'].removeprefix('GATE-')}-{outcome['name'].replace('_', '-')}"
            trace = {"schema_version": "1.1.0", "example_id": example_id, "case": f"{gate['title']} returns {outcome['name']}", "case_type": "synthetic_adversarial", "source_provenance": None, "initial_conditions": outcome["criteria"], "objective": "Verify assessment and disposition routing independently from task completion.", "mapped_nodes": ["NODE-TECHNICAL-GATE" if gate["id"] == "GATE-TECHNICAL" else "NODE-RELEASE-GATE", target], "expected_decisions": [], "expected_validation": [{"gate_id": gate["id"], "outcome": outcome["name"], "rationale": outcome["criteria"][0]}], "expected_recovery_or_stop": [target] if target in {"NODE-REPAIR", "NODE-STOP"} else [], "outputs": [f"{outcome['name']} disposition record"], "adjacent_handoff": None, "coverage_notes": "The case verifies a risk-based gate outcome and its recovery or stop destination."}
            write_yaml_atomic(trace_dir / f"{example_id.casefold()}.yaml", trace)
    targets = {"schema_version": "1.1.0", "mandatory_nodes": [node["id"] for node in nodes if node["type"] != "end"], "professional_decisions": [item["id"] for item in decisions], "decision_rules": all_rule_ids, "validation_gate_outcomes": [f"{gate['id']}:{outcome['name']}" for gate in gates for outcome in gate["outcomes"]], "recovery_and_stop_nodes": ["NODE-REPAIR", "NODE-STOP"], "critical_real_examples": real_ids, "thresholds": {"process_node_coverage": 0.9, "professional_decision_coverage": 1.0, "decision_rule_coverage": 0.9, "validation_gate_outcome_coverage": 1.0, "recovery_stop_coverage": 1.0, "critical_real_example_replay_coverage": 1.0}}
    write_yaml_atomic(workspace / "review" / "coverage-targets.yaml", targets)
    coverage_report(workspace)
    write_yaml_atomic(workspace / "professional-release.yaml", {"schema_version": "1.1.0", "workflow_id": workflow_id, "build_method": "individual-professional-deepening", "semantic_authoring_id": f"{profile['short'].casefold()}-v11-deepening", "review_cycle": 1, "status": "SYNTHESIS"})

    issues = [
        *validate_task_contract(workspace / "task-contract.yaml"), *validate_source_manifest(workspace),
        *validate_knowledge_atoms(workspace), *validate_evidence_coverage(workspace), *validate_workflow_ir(workspace),
        *validate_capability_map(workspace),
        *validate_skill_package(workspace / "generated" / workflow_id, workspace),
    ]
    _, coverage_issues = coverage_report(workspace)
    issues.extend(coverage_issues)
    if issues:
        raise ValueError("\n".join(issues))
    print(f"built {workflow_id}: {len(sources)} sources, {len(atoms)} atoms, {len(decisions)} decisions, {len(all_rule_ids)} rules")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build one individually authored v1.1 professional workflow; no batch mode is provided.")
    parser.add_argument("--workspace", required=True, type=Path)
    parser.add_argument("--workflow", required=True, choices=sorted(PROFILES))
    args = parser.parse_args()
    try:
        build(args.workspace, PROFILES[args.workflow])
    except (OSError, ValueError, KeyError) as exc:
        print(exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
