from __future__ import annotations

from pathlib import Path
from typing import Any

from .common import load_yaml, schema_errors, write_yaml_atomic


def _ratio(covered: set[str], targets: set[str]) -> float:
    return 1.0 if not targets else len(covered & targets) / len(targets)


def coverage_report(workspace: Path) -> tuple[dict[str, Any], list[str]]:
    ir = load_yaml(workspace / "synthesis" / "workflow-ir.yaml")
    targets_path = workspace / "review" / "coverage-targets.yaml"
    if not targets_path.is_file():
        return {}, ["missing review/coverage-targets.yaml"]
    targets = load_yaml(targets_path) or {}
    required = ["mandatory_nodes", "professional_decisions", "decision_rules", "validation_gate_outcomes", "recovery_and_stop_nodes", "critical_real_examples", "thresholds"]
    if any(key not in targets for key in required):
        return {}, ["coverage-targets.yaml is missing one or more v1.1 target dimensions"]
    node_by_id = {node["id"]: node for node in ir["control_flow"]["nodes"]}
    decision_by_id = {decision["id"]: decision for decision in ir["decisions"]}
    gate_by_id = {gate["id"]: gate for gate in ir["validation_gates"]}
    known_rules = {rule["id"]: (decision["id"], rule["outcome"]) for decision in ir["decisions"] for rule in decision["rules"]}
    known_gate_outcomes = {(gate["id"], outcome["name"]) for gate in ir["validation_gates"] for outcome in gate["outcomes"]}
    issues: list[str] = []
    covered_nodes: set[str] = set()
    covered_decisions: set[str] = set()
    covered_rules: set[str] = set()
    covered_gate_outcomes: set[str] = set()
    covered_recovery: set[str] = set()
    replayed_real: set[str] = set()
    trace_count = 0
    for path in sorted((workspace / "review" / "example-traces").glob("*.yaml")):
        trace = load_yaml(path)
        errors = schema_errors(trace, "example-trace.schema.json")
        issues.extend(f"{path.name}: {error}" for error in errors)
        if errors:
            continue
        trace_count += 1
        if trace["case_type"] == "real_source_replay":
            replayed_real.add(trace["example_id"])
            if not trace["expected_decisions"]:
                issues.append(f"{path.name}: real replay has no professional decision expectation")
        for node_id in trace["mapped_nodes"]:
            if node_id not in node_by_id:
                issues.append(f"{path.name}: unknown node {node_id}")
            else:
                covered_nodes.add(node_id)
        for expectation in trace["expected_decisions"]:
            decision_id = expectation["decision_id"]
            if decision_id not in decision_by_id:
                issues.append(f"{path.name}: unknown decision {decision_id}")
                continue
            covered_decisions.add(decision_id)
            for rule_id in expectation["rule_ids"]:
                known = known_rules.get(rule_id)
                if not known:
                    issues.append(f"{path.name}: unknown rule {rule_id}")
                elif known != (decision_id, expectation["outcome"]):
                    issues.append(f"{path.name}: {rule_id} does not support {decision_id}:{expectation['outcome']}")
                else:
                    covered_rules.add(rule_id)
        for expectation in trace["expected_validation"]:
            pair = (expectation["gate_id"], expectation["outcome"])
            if pair not in known_gate_outcomes:
                issues.append(f"{path.name}: unknown gate outcome {pair[0]}:{pair[1]}")
            else:
                covered_gate_outcomes.add(f"{pair[0]}:{pair[1]}")
        for node_id in trace["expected_recovery_or_stop"]:
            if node_id not in node_by_id or node_by_id[node_id]["type"] not in {"recovery", "stop"}:
                issues.append(f"{path.name}: invalid recovery/stop node {node_id}")
            else:
                covered_recovery.add(node_id)
    dimensions = {
        "process_node_coverage": _ratio(covered_nodes, set(targets["mandatory_nodes"])),
        "professional_decision_coverage": _ratio(covered_decisions, set(targets["professional_decisions"])),
        "decision_rule_coverage": _ratio(covered_rules, set(targets["decision_rules"])),
        "validation_gate_outcome_coverage": _ratio(covered_gate_outcomes, set(targets["validation_gate_outcomes"])),
        "recovery_stop_coverage": _ratio(covered_recovery, set(targets["recovery_and_stop_nodes"])),
        "critical_real_example_replay_coverage": _ratio(replayed_real, set(targets["critical_real_examples"])),
    }
    thresholds = targets["thresholds"]
    passed = not issues and all(dimensions[name] >= float(thresholds[name]) for name in dimensions)
    report = {"schema_version": "1.1.0", "trace_count": trace_count, "dimensions": {name: round(value, 4) for name, value in dimensions.items()}, "thresholds": thresholds, "pass": passed}
    write_yaml_atomic(workspace / "review" / "coverage-report.yaml", report)
    return report, issues
