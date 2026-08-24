from __future__ import annotations

import re
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any

from .common import PROJECT_ROOT, ValidationFailure, load_source_manifest, load_yaml, read_jsonl, resolve_source_artifact, resolve_workspace_file, schema_errors, sha256_file
from .conflicts import source_conflicts_markdown
from .evidence import source_gaps_markdown


def validate_task_contract(path: Path) -> list[str]:
    return schema_errors(load_yaml(path), "task-contract.schema.json")


def validate_source_manifest(workspace: Path, check_files: bool = True) -> list[str]:
    manifest_path = workspace / "source-manifest.yaml"
    if not manifest_path.exists():
        return ["missing source-manifest.yaml"]
    raw_manifest = load_yaml(manifest_path)
    issues = schema_errors(raw_manifest, "source-manifest.schema.json")
    if issues:
        return issues
    try:
        manifest = load_source_manifest(workspace)
    except (ValidationFailure, OSError, KeyError) as exc:
        return [str(exc)]
    policy = load_yaml(Path(__file__).resolve().parents[2] / "config" / "source-policy.yaml")
    sources = manifest["sources"]
    identifiers = [source["source_id"] for source in sources]
    if len(identifiers) != len(set(identifiers)):
        issues.append("source IDs must be unique")
    if len(sources) < policy["min_total_sources"]:
        issues.append(f"requires at least {policy['min_total_sources']} sources")
    organizations = {source["organization"].strip().casefold() for source in sources}
    if len(organizations) < policy["min_independent_organizations"]:
        issues.append(f"requires at least {policy['min_independent_organizations']} independent organizations")
    official_count = sum(source["official_primary"] for source in sources)
    if official_count < policy["min_primary_official_sources"]:
        issues.append(f"requires at least {policy['min_primary_official_sources']} originating official sources")
    counts = Counter(source["source_type"] for source in sources)
    for source_type, minimum in policy["required_source_types"].items():
        if counts[source_type] < minimum:
            issues.append(f"requires {minimum} {source_type}; found {counts[source_type]}")
    hashes: dict[str, str] = {}
    for source in sources:
        sid = source["source_id"]
        normalization = source["normalization"]
        if source["official_primary"] and source["authority_tier"] not in {"T1", "T2", "T3"}:
            issues.append(f"{sid}: official_primary requires T1, T2, or T3")
        if normalization["status"] != "passed":
            issues.append(f"{sid}: normalization status is {normalization['status']}")
        duplicate = normalization["duplicate_of"]
        if duplicate:
            issues.append(f"{sid}: duplicate of {duplicate}")
        if source["sha256"] in hashes:
            issues.append(f"{sid}: raw content duplicates {hashes[source['sha256']]}")
        hashes[source["sha256"]] = sid
        if normalization["quality_flags"]:
            issues.append(f"{sid}: normalization has unresolved quality flags")
        if check_files:
            for artifact in (source["raw_path"], source["normalized_path"]):
                try:
                    resolved = resolve_source_artifact(workspace, manifest, artifact)
                except Exception as exc:
                    issues.append(f"{sid}: {exc}")
                    continue
                if not resolved.is_file():
                    issues.append(f"{sid}: missing {artifact}")
            try:
                raw_file = resolve_source_artifact(workspace, manifest, source["raw_path"])
                if raw_file.is_file() and sha256_file(raw_file) != source["sha256"]:
                    issues.append(f"{sid}: raw source hash drift")
            except Exception:
                pass
    conflicts_path = workspace / "extraction" / "source-conflicts.yaml"
    if not conflicts_path.exists():
        issues.append("missing extraction/source-conflicts.yaml")
    else:
        conflicts = load_yaml(conflicts_path) or {}
        if conflicts.get("unresolved_count", 0) != 0:
            issues.append("unresolved applicability conflicts are not zero")
        view_path = workspace / "extraction" / "source-conflicts.md"
        if not view_path.is_file():
            issues.append("missing extraction/source-conflicts.md")
        elif view_path.read_text(encoding="utf-8") != source_conflicts_markdown(conflicts):
            issues.append("source-conflicts.md is not the canonical YAML rendering")
    coverage_path = workspace / "extraction" / "evidence-coverage.yaml"
    gaps_path = workspace / "extraction" / "source-gaps.md"
    if coverage_path.is_file():
        coverage = load_yaml(coverage_path) or {}
        if not gaps_path.is_file():
            issues.append("missing extraction/source-gaps.md")
        elif gaps_path.read_text(encoding="utf-8") != source_gaps_markdown(coverage):
            issues.append("source-gaps.md is not the canonical evidence-coverage rendering")
    return issues


def validate_knowledge_atoms(workspace: Path) -> list[str]:
    atom_path = workspace / "extraction" / "knowledge-atoms.jsonl"
    try:
        atoms = read_jsonl(atom_path)
    except Exception as exc:
        return [str(exc)]
    if not atoms:
        return ["knowledge-atoms.jsonl is empty"]
    issues: list[str] = []
    manifest = load_source_manifest(workspace)
    source_tiers = {source["source_id"]: source["authority_tier"] for source in manifest["sources"]}
    identifiers: set[str] = set()
    for index, atom in enumerate(atoms, start=1):
        for error in schema_errors(atom, "knowledge-atom.schema.json"):
            issues.append(f"line {index}: {error}")
        atom_id = atom.get("id")
        if atom_id in identifiers:
            issues.append(f"duplicate atom ID: {atom_id}")
        identifiers.add(atom_id)
        source_id = atom.get("source_id")
        if source_id not in source_tiers:
            issues.append(f"{atom_id}: unknown source {source_id}")
        elif atom.get("authority_tier") != source_tiers[source_id]:
            issues.append(f"{atom_id}: authority tier differs from source manifest")
    for atom in atoms:
        for relationship in atom.get("relationships", []):
            if relationship["atom_id"] not in identifiers:
                issues.append(f"{atom['id']}: relationship references unknown atom {relationship['atom_id']}")
    return issues


def _tarjan(nodes: set[str], edges: dict[str, set[str]]) -> list[set[str]]:
    index = 0
    stack: list[str] = []
    on_stack: set[str] = set()
    indices: dict[str, int] = {}
    lowlinks: dict[str, int] = {}
    components: list[set[str]] = []

    def visit(node: str) -> None:
        nonlocal index
        indices[node] = index
        lowlinks[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)
        for target in edges[node]:
            if target not in indices:
                visit(target)
                lowlinks[node] = min(lowlinks[node], lowlinks[target])
            elif target in on_stack:
                lowlinks[node] = min(lowlinks[node], indices[target])
        if lowlinks[node] == indices[node]:
            component: set[str] = set()
            while True:
                popped = stack.pop()
                on_stack.remove(popped)
                component.add(popped)
                if popped == node:
                    break
            components.append(component)

    for node in nodes:
        if node not in indices:
            visit(node)
    return components


def validate_workflow_ir(workspace: Path) -> list[str]:
    path = workspace / "synthesis" / "workflow-ir.yaml"
    if not path.exists():
        return ["missing synthesis/workflow-ir.yaml"]
    ir = load_yaml(path)
    issues = schema_errors(ir, "workflow-ir.schema.json")
    if issues:
        return issues
    atom_by_id = {atom["id"]: atom for atom in read_jsonl(workspace / "extraction" / "knowledge-atoms.jsonl")}
    atom_ids = set(atom_by_id)
    task_by_id = {task["id"]: task for task in ir["tasks"]}
    inference_ids = {item["id"] for item in ir["inferences"]}
    capability_ids = {item["id"] for item in ir["capability_requirements"]}
    decision_by_id = {item["id"]: item for item in ir["decisions"]}
    gate_ids = {item["id"] for item in ir["validation_gates"]}
    if len(task_by_id) != len(ir["tasks"]):
        issues.append("task IDs must be unique")
    for task in ir["tasks"]:
        parent = task["parent"]
        if parent and parent not in task_by_id:
            issues.append(f"{task['id']}: unknown parent {parent}")
        for inference_id in task["inferences"]:
            if inference_id not in inference_ids:
                issues.append(f"{task['id']}: unknown inference {inference_id}")
        for decision_id in task["decision_ids"]:
            if decision_id not in decision_by_id:
                issues.append(f"{task['id']}: unknown decision {decision_id}")
        if task["leaf"]:
            if not task.get("completion_criteria"):
                issues.append(f"{task['id']}: leaf lacks completion criteria")
            if not task.get("capability_ids"):
                issues.append(f"{task['id']}: leaf lacks capability IDs")
            if any(inference_id in {item["id"] for item in ir["inferences"] if item["operation"] == "select"} for inference_id in task["inferences"]) and not task["decision_ids"]:
                issues.append(f"{task['id']}: professional selection leaf lacks a material decision")
        for capability_id in task.get("capability_ids", []):
            if capability_id not in capability_ids:
                issues.append(f"{task['id']}: unknown capability {capability_id}")
        for atom_id in task["evidence"]:
            if atom_id not in atom_ids:
                issues.append(f"{task['id']}: unknown atom {atom_id}")
    for task in ir["tasks"]:
        seen: set[str] = set()
        cursor = task["parent"]
        while cursor:
            if cursor == task["id"] or cursor in seen:
                issues.append(f"{task['id']}: task hierarchy cycle")
                break
            seen.add(cursor)
            cursor = task_by_id.get(cursor, {}).get("parent")
    nodes = {node["id"]: node for node in ir["control_flow"]["nodes"]}
    if len(nodes) != len(ir["control_flow"]["nodes"]):
        issues.append("control-flow node IDs must be unique")
    starts = [node for node in nodes.values() if node["type"] == "start"]
    if len(starts) != 1:
        issues.append("control flow requires exactly one start node")
    adjacency: dict[str, set[str]] = {node_id: set() for node_id in nodes}
    outgoing: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for edge in ir["control_flow"]["edges"]:
        if edge["from"] not in nodes or edge["to"] not in nodes:
            issues.append(f"edge {edge['from']} -> {edge['to']} references an unknown node")
            continue
        adjacency[edge["from"]].add(edge["to"])
        outgoing[edge["from"]].append(edge)
    for node in nodes.values():
        if node["type"] not in {"end", "stop"} and not outgoing[node["id"]]:
            issues.append(f"{node['id']}: dangling non-terminal node")
        if node["type"] == "task":
            task_id = node.get("task_id")
            if task_id not in task_by_id:
                issues.append(f"{node['id']}: unknown task {task_id}")
        if node["type"] == "decision":
            decision = decision_by_id.get(node.get("decision_id"))
            if not decision:
                issues.append(f"{node['id']}: unknown decision {node.get('decision_id')}")
            else:
                outcomes = {rule["outcome"] for rule in decision["rules"]}
                edge_outcomes = {edge.get("outcome") for edge in outgoing[node["id"]]}
                if not outcomes.issubset(edge_outcomes):
                    issues.append(f"{node['id']}: missing decision outcome edge")
                if not any(edge.get("default") for edge in outgoing[node["id"]]):
                    issues.append(f"{node['id']}: missing fallback edge")
        if node["type"] == "validation_gate" and node.get("gate_id") not in gate_ids:
            issues.append(f"{node['id']}: unknown validation gate {node.get('gate_id')}")
        if node["type"] == "validation_gate" and node.get("gate_id") in gate_ids:
            gate = next(item for item in ir["validation_gates"] if item["id"] == node["gate_id"])
            outcomes = {item["name"] for item in gate["outcomes"]}
            edge_outcomes = {edge.get("outcome") for edge in outgoing[node["id"]]}
            if not outcomes.issubset(edge_outcomes):
                issues.append(f"{node['id']}: missing validation-gate outcome edge")
    if starts:
        reached: set[str] = set()
        queue: deque[str] = deque([starts[0]["id"]])
        while queue:
            node = queue.popleft()
            if node in reached:
                continue
            reached.add(node)
            queue.extend(adjacency[node] - reached)
        for node_id, node in nodes.items():
            if node_id not in reached:
                issues.append(f"{node_id}: unreachable control-flow node")
        mandatory_task_nodes = {node.get("task_id") for node in nodes.values() if node["type"] == "task" and node.get("task_id")}
        for task in ir["tasks"]:
            if task["mandatory"] and task["id"] not in mandatory_task_nodes:
                issues.append(f"{task['id']}: mandatory task has no control-flow node")
    for component in _tarjan(set(nodes), adjacency):
        cyclic = len(component) > 1 or any(node in adjacency[node] for node in component)
        if cyclic and not any(target not in component for node in component for target in adjacency[node]):
            issues.append(f"dead loop: {', '.join(sorted(component))}")
    for route_group in ("exceptions", "recovery_paths", "stop_conditions"):
        for route in ir[route_group]:
            if route["target_node"] not in nodes:
                issues.append(f"{route_group} {route['id']}: target node is unknown")
            for atom_id in route.get("evidence", []):
                if atom_id not in atom_ids:
                    issues.append(f"{route_group} {route['id']}: unknown atom {atom_id}")
    for decision in ir["decisions"]:
        input_names = {item["name"] for item in decision["inputs"]}
        rule_ids = [rule["id"] for rule in decision["rules"]]
        if len(rule_ids) != len(set(rule_ids)):
            issues.append(f"{decision['id']}: rule IDs must be unique")
        for rule in decision["rules"]:
            for condition in rule["conditions"]:
                if condition["input"] not in input_names:
                    issues.append(f"{rule['id']}: condition references undeclared input {condition['input']}")
            if not any(atom_by_id.get(atom_id, {}).get("mandatory") for atom_id in rule["evidence"]):
                issues.append(f"{rule['id']}: mandatory decision rule lacks mandatory professional evidence")
        for atom_id in decision["evidence"] + [item for rule in decision["rules"] for item in rule["evidence"]]:
            if atom_id not in atom_ids:
                issues.append(f"{decision['id']}: unknown atom {atom_id}")
    for gate in ir["validation_gates"]:
        outcome_names = {item["name"] for item in gate["outcomes"]}
        if "PASS" not in outcome_names or not outcome_names.intersection({"REMEDIATE", "REJECT"}):
            issues.append(f"{gate['id']}: gate requires PASS and a remediation or rejection outcome")
        completion_only = gate["assessment_dimensions"] + gate["required_evidence"]
        if completion_only and all(re.search(r"\b(?:completion|completed|finished)\b", item, re.IGNORECASE) for item in completion_only):
            issues.append(f"{gate['id']}: completion-only validation gate lacks professional assessment dimensions")
        for atom_id in gate["evidence"]:
            if atom_id not in atom_ids:
                issues.append(f"{gate['id']}: unknown atom {atom_id}")
        for outcome in gate["outcomes"]:
            for atom_id in outcome["evidence"]:
                if atom_id not in atom_ids:
                    issues.append(f"{gate['id']}:{outcome['name']}: unknown atom {atom_id}")
    for capability in ir["capability_requirements"]:
        for task_id in capability["task_ids"]:
            if task_id not in task_by_id:
                issues.append(f"{capability['id']}: unknown task {task_id}")
    for mapping in ir["evidence_map"]:
        for atom_id in mapping["atom_ids"]:
            if atom_id not in atom_ids:
                issues.append(f"evidence map {mapping['claim_id']}: unknown atom {atom_id}")
    return issues


_FRONTMATTER = re.compile(r"\A---\n(?P<header>.*?)\n---\n", re.DOTALL)
_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_LEAKAGE = re.compile(r"\b(?:MATLAB|MathWorks|Codex|OpenAI|Claude|Anthropic|MCP|fitLifetimePDModel|predictLifetime)\b", re.IGNORECASE)
_INTERNAL_ID = re.compile(r"\b(?:NODE|TASK|DEC|GATE|KA)-[A-Z0-9-]+\b")
_REQUIRED_HEADINGS = ["Purpose", "Scope and Applicability", "Required Inputs", "Professional Workflow", "Decision Policy", "Validation and Acceptance Criteria", "Failure and Recovery", "Stop / Escalation Conditions", "Deliverables", "Workflow-Owned Professional Reasoning", "Delegated / Implementation Capabilities", "Reference Loading", "Final Quality Checks"]


def validate_skill_package(skill_dir: Path, workspace: Path | None = None) -> list[str]:
    skill_path = skill_dir / "SKILL.md"
    if not skill_path.exists():
        return ["missing SKILL.md"]
    text = skill_path.read_text(encoding="utf-8")
    issues: list[str] = []
    match = _FRONTMATTER.match(text)
    if not match:
        return ["invalid frontmatter"]
    header = load_yaml_from_text(match.group("header"))
    if not isinstance(header, dict) or set(header) != {"name", "description"}:
        issues.append("frontmatter must contain exactly name and description")
        return issues
    name = header["name"]
    description = header["description"]
    if not isinstance(name, str) or not _NAME.fullmatch(name) or len(name) > 64:
        issues.append("invalid skill name")
    if name != skill_dir.name:
        issues.append("skill name must match folder")
    if not isinstance(description, str) or not 40 <= len(description) <= 1024:
        issues.append("description must contain 40-1024 characters")
    body = text[match.end():]
    if len(body.splitlines()) > 500:
        issues.append("SKILL.md body exceeds 500 lines")
    for heading in _REQUIRED_HEADINGS:
        if not re.search(rf"^#{{1,3}}\s+{re.escape(heading)}\s*$", body, re.MULTILINE):
            issues.append(f"missing heading: {heading}")
    found = _LEAKAGE.search(body)
    if found:
        issues.append(f"provider-specific leakage: {found.group(0)}")
    for markdown in sorted(skill_dir.rglob("*.md")):
        internal = _INTERNAL_ID.search(markdown.read_text(encoding="utf-8"))
        if internal:
            issues.append(f"internal ID leaked in {markdown.relative_to(skill_dir)}: {internal.group(0)}")
    evidence_path = skill_dir / "references" / "regulatory-evidence.md"
    if evidence_path.is_file():
        evidence_text = evidence_path.read_text(encoding="utf-8")
        for label in ("Source:", "Source ID:", "Locator:", "Authority:", "Applicability:", "Interpretation:"):
            if label not in evidence_text:
                issues.append(f"regulatory evidence lacks {label.rstrip(':').lower()} fields")
    for relative in re.findall(r"\]\((references/[^)]+)\)", body):
        if not (skill_dir / relative).is_file():
            issues.append(f"missing referenced file: {relative}")
    if workspace is not None:
        ir = load_yaml(workspace / "synthesis" / "workflow-ir.yaml")
        mapping = load_yaml(workspace / "alignment" / "capability-map.yaml")
        binding_by_task = {item["task_id"]: item["mapping_result"] for item in mapping["bindings"]}
        reasoning_match = re.search(r"^# Workflow-Owned Professional Reasoning\s*$\n(?P<text>.*?)(?=^# )", body, re.MULTILINE | re.DOTALL)
        delegated_match = re.search(r"^# Delegated / Implementation Capabilities\s*$\n(?P<text>.*?)(?=^# )", body, re.MULTILINE | re.DOTALL)
        reasoning_text = reasoning_match.group("text").casefold() if reasoning_match else ""
        delegated_text = delegated_match.group("text").casefold() if delegated_match else ""
        for capability in ir["capability_requirements"]:
            label = capability["name"].replace("-", " ").casefold()
            results = {binding_by_task.get(task_id) for task_id in capability["task_ids"]}
            is_reasoning = capability["kind"] == "reasoning" or results == {"NO_PROVIDER_REQUIRED"}
            expected, unexpected = (reasoning_text, delegated_text) if is_reasoning else (delegated_text, reasoning_text)
            if label not in expected:
                issues.append(f"capability is missing from its derived section: {capability['name']}")
            if label in unexpected:
                issues.append(f"capability is merged into the wrong section: {capability['name']}")
    return issues


def load_yaml_from_text(text: str) -> Any:
    import yaml

    return yaml.safe_load(text)


def validate_capability_map(workspace: Path) -> list[str]:
    mapping_path = workspace / "alignment" / "capability-map.yaml"
    if not mapping_path.exists():
        return ["missing alignment/capability-map.yaml"]
    mapping = load_yaml(mapping_path)
    issues = schema_errors(mapping, "capability-map.schema.json")
    if issues:
        return issues
    ir = load_yaml(workspace / "synthesis" / "workflow-ir.yaml")
    leaves = {task["id"] for task in ir["tasks"] if task["leaf"]}
    bound = {item["task_id"] for item in mapping["bindings"]}
    missing = leaves - bound
    if missing:
        issues.append(f"unmapped professional leaves: {', '.join(sorted(missing))}")
    for binding in mapping["bindings"]:
        if binding["task_id"] not in leaves:
            issues.append(f"binding references non-leaf task {binding['task_id']}")
        if binding["mapping_result"] in {"GAP", "NO_PROVIDER_REQUIRED"} and binding["providers"]:
            issues.append(f"{binding['task_id']}: {binding['mapping_result']} must not bind a provider")
        if binding["mapping_result"] not in {"GAP", "NO_PROVIDER_REQUIRED"} and not binding["providers"]:
            issues.append(f"{binding['task_id']}: implementation mapping requires provider skills")
        for provider in binding["providers"]:
            inventory_path = PROJECT_ROOT / "provider-inventory" / provider["provider"] / "skill-signatures.yaml"
            if not inventory_path.is_file():
                issues.append(f"{binding['task_id']}: missing provider inventory for {provider['provider']}")
                continue
            inventory = load_yaml(inventory_path)
            known_skills = {signature["skill"] for signature in inventory.get("signatures", [])}
            for skill in provider["skills"]:
                if skill not in known_skills:
                    issues.append(f"{binding['task_id']}: unknown {provider['provider']} skill {skill}")
    return issues


def validate_provider_signatures(path: Path) -> list[str]:
    if not path.is_file():
        return [f"missing provider signature inventory: {path}"]
    inventory = load_yaml(path)
    issues = schema_errors(inventory, "provider-signatures.schema.json")
    if issues:
        return issues
    seen: set[str] = set()
    for signature in inventory["signatures"]:
        skill = signature["skill"]
        if skill in seen:
            issues.append(f"duplicate provider skill signature: {skill}")
        seen.add(skill)
    return issues
