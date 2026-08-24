from __future__ import annotations

from pathlib import Path
import re
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from .common import TEMPLATE_DIR, load_source_manifest, load_yaml, read_jsonl, write_text_atomic


def _reference(title: str, path: str, when: str) -> dict[str, str]:
    return {"title": title, "path": path, "when": when}


def _condition_text(condition: dict[str, Any]) -> str:
    value = condition.get("value")
    if condition["operator"] in {"present", "missing"}:
        rendered = ""
    elif isinstance(value, bool):
        rendered = f" {str(value).lower()}"
    else:
        rendered = "" if value is None else f" {value}" if not isinstance(value, list) else f" one of {', '.join(map(str, value))}"
    return f"{condition['input'].replace('-', ' ')} {condition['operator'].replace('_', ' ')}{rendered}".strip()


ACRONYMS = {
    "pd": "PD", "lgd": "LGD", "ead": "EAD", "ecl": "ECL", "cds": "CDS",
    "var": "VaR", "es": "ES", "ifrs": "IFRS", "ccf": "CCF", "sicr": "SICR",
    "ttc": "TTC", "pit": "PIT", "asrf": "ASRF", "ngfs": "NGFS", "vares": "VaR/ES",
}


def _restore_acronyms(value: str) -> str:
    for source, target in ACRONYMS.items():
        value = re.sub(rf"\b{source}\b", target, value, flags=re.IGNORECASE)
    value = re.sub(r"\bp\s*&\s*l\b", "P&L", value, flags=re.IGNORECASE)
    value = re.sub(r"\bmonte carlo\b", "Monte Carlo", value, flags=re.IGNORECASE)
    value = re.sub(r"\bPD\s+LGD\s+EAD\s+and\b", "PD, LGD, EAD, and", value, flags=re.IGNORECASE)
    value = re.sub(r"\bPD\s+LGD\s+EAD\b", "PD, LGD, and EAD", value, flags=re.IGNORECASE)
    value = re.sub(r"\bPD\s+LGD\s+(and|or)\s+EAD\b", lambda match: f"PD, LGD, {match.group(1).lower()} EAD", value, flags=re.IGNORECASE)
    display_tokens = {
        "SCORECARD": "scorecard", "DEFAULT": "default-model", "VALIDATE": "validation",
        "MONITOR": "monitoring", "PORTFOLIO": "portfolio-risk", "STRESS": "stress-test",
        "TRANSITION": "rating-transition", "CURVE": "credit-curve", "STRUCTURAL": "structural-default",
        "BACKTEST": "VaR/ES backtesting", "CLIMATE": "climate-scenario",
    }
    for source, target in display_tokens.items():
        value = re.sub(rf"\b{source}\b", target, value)
    return value


def _without_terminal_punctuation(value: str) -> str:
    return _restore_acronyms(value.strip().rstrip(".\u3002;\uff1b"))


def _sentence(value: str) -> str:
    value = _without_terminal_punctuation(value)
    return value[:1].upper() + value[1:] + "." if value else value


def _lower_initial(value: str) -> str:
    value = value.strip().rstrip(".\u3002;\uff1b")
    value = value[:1].lower() + value[1:] if value else value
    return _restore_acronyms(value)


def _polish_action(value: str) -> str:
    value = _without_terminal_punctuation(value)
    value = re.sub(r"^Resolve\s+", "", value, flags=re.IGNORECASE)
    return value[:1].upper() + value[1:] if value else value


def _humanize_capability(value: str) -> str:
    value = value.replace("-", " ").strip()
    value = _restore_acronyms(value)
    return value[:1].upper() + value[1:] if value else value


def _capability_label(value: str) -> str:
    label = _humanize_capability(value)
    if "vares" in value.casefold():
        return f"{label} (capability: {value.replace('-', ' ')})"
    normalized_label = re.sub(r"[^a-z0-9]+", "", label.casefold())
    normalized_value = re.sub(r"[^a-z0-9]+", "", value.casefold())
    return label if normalized_label == normalized_value else f"{label} (capability: {value})"


def _joined_fragments(values: list[str]) -> str:
    value = ", ".join(_without_terminal_punctuation(item) for item in values)
    return value[:1].upper() + value[1:] if value else value


def _series(values: list[str], conjunction: str = "or") -> str:
    values = [_without_terminal_punctuation(value) for value in values]
    if len(values) < 2:
        return "".join(values)
    if len(values) == 2:
        return f"{values[0]} {conjunction} {values[1]}"
    return f"{', '.join(values[:-1])}, {conjunction} {values[-1]}"


def _task_outputs(task: dict[str, Any]) -> list[str]:
    if task["decision_ids"] and len(task["outputs"]) == 1 and task["outputs"][0].casefold().endswith(" decision record"):
        return [f"Decision record for {_lower_initial(task['title'])}"]
    return task["outputs"]


def render_skill(workspace: Path) -> Path:
    ir = load_yaml(workspace / "synthesis" / "workflow-ir.yaml")
    manifest = load_source_manifest(workspace)
    sources = {item["source_id"]: item for item in manifest["sources"]}
    atoms = {item["id"]: item for item in read_jsonl(workspace / "extraction" / "knowledge-atoms.jsonl")}
    workflow = ir["workflow"]
    legacy_pd = workflow["id"] == "develop-lifetime-pd-workflow"
    inference_by_id = {item["id"]: item["objective"] for item in ir["inferences"]}
    decision_titles = {item["id"]: item["title"] for item in ir["decisions"]}
    task_by_id = {task["id"]: task for task in ir["tasks"]}

    def legacy_task_title(task: dict[str, Any]) -> str:
        lineage = [task["title"]]
        parent = task["parent"]
        while parent:
            parent_task = task_by_id[parent]
            lineage.append(parent_task["title"])
            parent = parent_task["parent"]
        return " — ".join(reversed(lineage))

    if legacy_pd:
        tasks = [{
            "title": legacy_task_title(task), "objective": task["objective"], "inputs": task["inputs"], "outputs": task["outputs"],
            "actions": [inference_by_id[item].rstrip(".") for item in task["inferences"]], "completion": task.get("completion_criteria", []),
            "decisions": [decision_titles[item] for item in task["decision_ids"]],
        } for task in ir["tasks"] if task["leaf"]]
    else:
        tasks = [{
            "title": _restore_acronyms(task["title"]), "inputs_text": _joined_fragments(task["inputs"]),
            "outputs_text": _joined_fragments(_task_outputs(task)),
            "actions": [] if task["decision_ids"] else [_polish_action(inference_by_id[item]) for item in task["inferences"]],
            "completion": [_without_terminal_punctuation(item) for item in task.get("completion_criteria", [])],
            "decisions": [decision_titles[item] for item in task["decision_ids"]],
        } for task in ir["tasks"] if task["leaf"]]
    support_context = None
    if not legacy_pd:
        support_tasks = [task for task in tasks if task["actions"]]
        if support_tasks and len({(task["inputs_text"], task["outputs_text"]) for task in support_tasks}) == 1:
            support_context = {"inputs_text": support_tasks[0]["inputs_text"], "outputs_text": support_tasks[0]["outputs_text"]}
            for task in support_tasks:
                task["shared_context"] = True

    decision_summaries = [{
        "title": _restore_acronyms(item["title"]),
        "inputs": "; ".join(_lower_initial(value["description"]) for value in item["inputs"]),
        "fallback": _sentence(item["fallback"]["instruction"]),
    } for item in ir["decisions"]]
    validation_gate_summaries = [{
        **gate,
        "title": _restore_acronyms(gate["title"]),
        "assessment_text": ", ".join(_lower_initial(value) for value in gate["assessment_dimensions"]),
    } for gate in ir["validation_gates"]]

    mapping_path = workspace / "alignment" / "capability-map.yaml"
    binding_by_task = {}
    if mapping_path.is_file():
        binding_by_task = {item["task_id"]: item["mapping_result"] for item in load_yaml(mapping_path)["bindings"]}
    reasoning: list[str] = []
    delegated: list[str] = []
    for capability in ir["capability_requirements"]:
        results = {binding_by_task.get(task_id) for task_id in capability["task_ids"]}
        if capability["kind"] == "reasoning" or results == {"NO_PROVIDER_REQUIRED"}:
            if legacy_pd:
                reasoning.append(capability["name"].replace("-", " "))
            else:
                label = _capability_label(capability["name"])
                reasoning.extend(f"{label} — {_restore_acronyms(task_by_id[task_id]['title'])}" for task_id in capability["task_ids"])
        else:
            suffix = " (implementation coverage gap must be resolved)" if "GAP" in results else ""
            delegated.append((capability["name"].replace("-", " ") if legacy_pd else _capability_label(capability["name"])) + suffix)

    environment = Environment(loader=FileSystemLoader(TEMPLATE_DIR), undefined=StrictUndefined, keep_trailing_newline=True, trim_blocks=True, lstrip_blocks=True)
    output_dir = workspace / "generated" / workflow["id"]
    template_name = "workflow-skill-template-v11-pd.md" if legacy_pd else "workflow-skill-template.md"
    display_workflow = workflow if legacy_pd else {
        **workflow,
        "purpose": _restore_acronyms(workflow["purpose"]),
        "scope": _restore_acronyms(workflow["scope"]),
        "trigger": _restore_acronyms(workflow["trigger"]),
        "not_for": _restore_acronyms(workflow["not_for"]),
        "exclusions": [_restore_acronyms(value) for value in workflow["exclusions"]],
    }
    description = (
        f"{workflow['purpose']} Use for the stated professional task with explicit applicability, decision, validation, recovery, and escalation handling; not for excluded adjacent work."
        if legacy_pd else
        f"{_sentence(display_workflow['purpose'])} Use when {_lower_initial(display_workflow['trigger'])}. Not for {_series(display_workflow['exclusions'][:3])}."
    )
    references = (
        [_reference("regulatory evidence", "references/regulatory-evidence.md", "checking the authority, locator, applicability, or interpretation of a material claim"), _reference("decision rules", "references/decision-rules.md", "choosing purpose, data route, model family, rating philosophy, calibration target, or acceptance route"), _reference("validation guidance", "references/validation-guidance.md", "planning or evaluating developer validation and recovery")]
        if legacy_pd else
        [_reference("regulatory evidence", "references/regulatory-evidence.md", "checking the authority, locator, applicability, or interpretation of a material claim"), _reference("decision rules", "references/decision-rules.md", "making a professional decision or applying its fallback"), _reference("validation guidance", "references/validation-guidance.md", "planning or evaluating validation, acceptance, and recovery")]
    )
    rendered = environment.get_template(template_name).render(
        skill_name=workflow["id"],
        description=description,
        workflow=display_workflow,
        inputs=ir["inputs"] if legacy_pd else [{"description": _sentence(item["description"])} for item in ir["inputs"]],
        outputs=ir["outputs"] if legacy_pd else [{"description": _sentence(item["description"])} for item in ir["outputs"]],
        tasks=tasks, support_context=support_context,
        decisions=ir["decisions"], decision_summaries=decision_summaries,
        validation_gates=validation_gate_summaries,
        recoveries=[_restore_acronyms(item["instruction"]) for item in ir["recovery_paths"]], stop_conditions=[_restore_acronyms(item["instruction"]) for item in ir["stop_conditions"]],
        reasoning_capabilities=reasoning, delegated_capabilities=delegated,
        references=references,
    )
    write_text_atomic(output_dir / "SKILL.md", rendered)

    evidence_lines = ["# Regulatory Evidence", "", "This human-readable map supports professional claims. Vendor examples are intentionally excluded because implementation feasibility is not professional authority.", ""]
    for mapping in ir["evidence_map"]:
        evidence_lines.extend([f"## {mapping['claim']}", ""])
        for atom_id in mapping["atom_ids"]:
            atom = atoms[atom_id]
            source = sources[atom["source_id"]]
            locator = "; ".join(f"{key}: {value}" for key, value in atom["locator"].items())
            applicability = atom["applicability"]
            evidence_lines.extend([
                f"- Source: {source['organization']}, *{source['title']}*", f"- Locator: {locator}",
                f"- Source ID: {source['source_id']}",
                f"- Authority: {source['authority_tier']} ({source['status']})", f"- Applicability: {', '.join(applicability['jurisdictions'])}; {applicability['purpose']}",
                f"- Interpretation: {atom['statement']}", "",
            ])
    write_text_atomic(output_dir / "references" / "regulatory-evidence.md", "\n".join(evidence_lines).rstrip() + "\n")

    lines = ["# Decision Rules", "", "Apply only the rule whose conditions and applicability are established. Tool support does not select a rule.", ""]
    for decision in ir["decisions"]:
        lines.extend([f"## {decision['title']}", "", decision["purpose"], "", "### Inputs", ""])
        for item in decision["inputs"]:
            lines.append(f"- {item['name'].replace('-', ' ')} ({'required' if item['required'] else 'optional'}): {item['description']}")
        lines.extend(["", "### Rules", ""])
        for rule in decision["rules"]:
            lines.extend([
                f"#### {rule['outcome'].replace('-', ' ').title()}", "",
                f"- Conditions: {'; and '.join(_condition_text(item) for item in rule['conditions'])}.",
                f"- Rationale: {rule['rationale']}", f"- Applies to: {', '.join(rule['applicability'])}.",
                f"- Excludes: {', '.join(rule['exclusions']) or 'no additional cases'}.", f"- If information is missing: {rule['missing_information_behavior']}", "",
            ])
        lines.extend(["### Fallback", "", f"Outcome: {decision['fallback']['outcome'].replace('-', ' ')}. {decision['fallback']['instruction']}", ""])
    write_text_atomic(output_dir / "references" / "decision-rules.md", "\n".join(lines).rstrip() + "\n")

    lines = ["# Validation Guidance", "", "Developer testing supports selection and packaging but does not replace organizationally independent validation where that is required.", ""]
    for gate in ir["validation_gates"]:
        lines.extend([f"## {gate['title']}", "", gate["purpose"], "", f"Required evidence: {', '.join(gate['required_evidence'])}.", f"Assess: {', '.join(gate['assessment_dimensions'])}.", f"Policy: {gate['acceptance_policy']}", ""])
        for outcome in gate["outcomes"]:
            lines.extend([f"- {outcome['name'].replace('_', ' ').title()}: {'; '.join(outcome['criteria'])}. Route: {outcome['route']}"])
        lines.append("")
    write_text_atomic(output_dir / "references" / "validation-guidance.md", "\n".join(lines).rstrip() + "\n")
    return output_dir
