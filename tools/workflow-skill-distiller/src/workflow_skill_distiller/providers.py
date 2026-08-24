from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .common import sha256_file, write_yaml_atomic


def _frontmatter_description(text: str) -> str:
    match = re.search(r"^description:\s*(.+)$", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def _find_methods(text: str) -> list[str]:
    candidates = ["Logistic", "Probit", "Cox", "custom", "Tobit", "Beta", "two-stage", "mean", "regression"]
    return [candidate for candidate in candidates if re.search(rf"\b{re.escape(candidate)}\b", text, flags=re.IGNORECASE)]


def extract_matlab_signatures(skills_root: Path, output_path: Path) -> dict[str, Any]:
    signatures: list[dict[str, Any]] = []
    for folder in sorted(path for path in skills_root.iterdir() if path.is_dir() and path.name.startswith("matlab-")):
        skill_path = folder / "SKILL.md"
        if not skill_path.is_file():
            continue
        text = skill_path.read_text(encoding="utf-8")
        signatures.append({
            "skill": folder.name,
            "skill_sha256": sha256_file(skill_path),
            "evidence_state": "inspected",
            "description": _frontmatter_description(text),
            "methods": _find_methods(text),
            "capabilities": [match.lower().replace(" ", "-") for match in re.findall(r"Implement(?: selected)? ([A-Za-z ,/-]+?)(?: in MATLAB| work| calculations| code| analyses)", text, flags=re.IGNORECASE)][:5],
        })
    inventory = {"schema_version": "1.0.0", "provider": "matlab", "signatures": signatures}
    write_yaml_atomic(output_path, inventory)
    return inventory
