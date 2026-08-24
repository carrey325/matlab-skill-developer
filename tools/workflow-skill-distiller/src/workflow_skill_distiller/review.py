from __future__ import annotations

from pathlib import Path
from typing import Any

from .common import load_yaml, schema_errors, write_yaml_atomic


PRECEDENCE = ["RESEARCH_MORE", "RESYNTHESIZE", "REGRANULARIZE", "REGENERATE", "PASS"]
RETURN_STAGE = {"RESEARCH_MORE": 1, "RESYNTHESIZE": 2, "REGENERATE": 3, "REGRANULARIZE": 5}


def aggregate_reviews(workspace: Path, cycle: int) -> tuple[dict[str, Any], list[str]]:
    review_dir = workspace / "review"
    paths = sorted(path for path in review_dir.glob("*-review.yaml") if path.name != "final-verdict.yaml")
    issues: list[str] = []
    reviews: list[dict[str, Any]] = []
    if not paths:
        return {}, ["no reviewer verdicts found"]
    for path in paths:
        review = load_yaml(path)
        for error in schema_errors(review, "review-verdict.schema.json"):
            issues.append(f"{path.name}: {error}")
        if review.get("status") == "PASS" and any(check.get("status") == "FAIL" for check in review.get("checks", [])):
            issues.append(f"{path.name}: PASS verdict contains a failed check")
        reviews.append(review)
    if issues:
        return {}, issues
    selected = next(status for status in PRECEDENCE if any(review["status"] == status for review in reviews))
    defects = [defect for review in reviews for defect in review["defects"]]
    changes = [change for review in reviews for change in review["required_changes"]]
    verdict: dict[str, Any] = {
        "schema_version": "1.1.0",
        "reviewer": "review-aggregator",
        "status": selected,
        "cycle": cycle,
        "checks": [{"dimension": "review aggregation", "status": "PASS" if selected == "PASS" else "FAIL", "notes": f"Applied precedence and selected {selected} across {len(reviews)} independent review records.", "evidence": [path.name for path in paths]}],
        "defects": defects,
        "required_changes": changes,
        "human_review_required": selected != "PASS" and cycle >= 3,
    }
    if selected != "PASS":
        verdict["return_to_stage"] = RETURN_STAGE[selected]
        if selected == "REGRANULARIZE":
            verdict["post_alignment_return_stage"] = 2
    write_yaml_atomic(review_dir / "final-verdict.yaml", verdict)
    return verdict, []
