#!/usr/bin/env python3
"""Audit a workflow skill and its MATLAB implementation boundary."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
HEADER_KEY = re.compile(r"^([A-Za-z0-9_-]+):", re.MULTILINE)
MAX_DESCRIPTION_CHARS = 1024
MAX_SKILL_LINES = 500


def read_skill(folder: Path) -> tuple[str, str, str, list[str]]:
    errors: list[str] = []
    skill = folder / "SKILL.md"
    if not skill.is_file():
        return "", "", "", [f"{folder}: missing SKILL.md"]
    try:
        text = skill.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return "", "", "", [f"{skill}: cannot read UTF-8 content ({exc})"]
    match = FRONTMATTER.match(text)
    if not match:
        return "", "", "", [f"{skill}: invalid frontmatter"]
    header = match.group(1)
    keys = HEADER_KEY.findall(header)
    if sorted(keys) != ["description", "name"]:
        errors.append(f"{skill}: frontmatter must contain exactly name and description")
    name_match = re.search(r"^name:\s*(.+)$", header, re.MULTILINE)
    description_match = re.search(r"^description:\s*(.+)$", header, re.MULTILINE)
    name = name_match.group(1).strip() if name_match else ""
    description = description_match.group(1).strip() if description_match else ""
    body = text[match.end():]
    if not NAME.fullmatch(name) or len(name) > 64:
        errors.append(f"{skill}: name must be lowercase hyphen-case and at most 64 characters")
    if not 40 <= len(description) <= MAX_DESCRIPTION_CHARS:
        errors.append(f"{skill}: description must be 40-{MAX_DESCRIPTION_CHARS} characters")
    if len(body.splitlines()) > MAX_SKILL_LINES:
        errors.append(f"{skill}: body exceeds {MAX_SKILL_LINES} lines")
    if not (folder / "agents" / "openai.yaml").is_file():
        errors.append(f"{folder}: missing agents/openai.yaml")
    return name, description, body, errors


def has_heading(body: str, heading: str) -> bool:
    return bool(re.search(rf"^#{{2,6}}\s+{re.escape(heading)}\s*$", body, re.IGNORECASE | re.MULTILINE))


def inspect_family(workflow_folder: Path, matlab_folder: Path) -> list[str]:
    workflow_name, _, workflow_body, errors = read_skill(workflow_folder)
    matlab_name, matlab_description, matlab_body, matlab_errors = read_skill(matlab_folder)
    errors.extend(matlab_errors)

    if not workflow_name.endswith("-workflow"):
        errors.append(f"{workflow_folder}: workflow name must end with -workflow")
        capability = ""
    else:
        capability = workflow_name.removesuffix("-workflow")

    if not matlab_name.startswith("matlab-") or matlab_name.endswith("-api"):
        errors.append(f"{matlab_folder}: MATLAB name must be matlab-<capability> without -api")
    elif capability and matlab_name != f"matlab-{capability}":
        errors.append(f"{matlab_folder}: expected matlab-{capability} for {workflow_name}")

    for heading in ("When to Use", "When Not to Use", "Implementation Selection", "Workflow"):
        if not has_heading(workflow_body, heading):
            errors.append(f"{workflow_folder / 'SKILL.md'}: missing {heading} heading")

    for heading in ("Scope", "Prerequisites", "Capability Contract", "Critical Rules", "Failure Handling", "Gotchas"):
        if not has_heading(matlab_body, heading):
            errors.append(f"{matlab_folder / 'SKILL.md'}: missing {heading} heading")

    forbidden_matlab_headings = ("When to Use", "When Not to Use", "Implementation Selection", "Workflow")
    for heading in forbidden_matlab_headings:
        if has_heading(matlab_body, heading):
            errors.append(f"{matlab_folder / 'SKILL.md'}: {heading} belongs in workflow skill")

    if re.search(r"\bmethod-to-object\b|\btask-to-function\b", matlab_body, re.IGNORECASE):
        errors.append(f"{matlab_folder / 'SKILL.md'}: method/task routing belongs in workflow skill")
    if capability and workflow_name.lower() not in matlab_description.lower():
        errors.append(f"{matlab_folder / 'SKILL.md'}: description must mention {workflow_name} planning handoff")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("workflow", type=Path)
    parser.add_argument("matlab", type=Path)
    args = parser.parse_args()
    errors = inspect_family(args.workflow.resolve(), args.matlab.resolve())
    if errors:
        print("Capability family audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Capability family audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
