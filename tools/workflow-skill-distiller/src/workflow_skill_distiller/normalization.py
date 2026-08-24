from __future__ import annotations

import re
from pathlib import Path


def quality_flags(raw_path: Path, text: str) -> list[str]:
    """Apply conservative, format-aware local conversion quality checks."""
    flags: list[str] = []
    stripped = text.strip()
    if not stripped:
        flags.append("empty_output")
    if len(stripped) < 200:
        flags.append("implausibly_short")
    conventional_heading = any(re.match(r"^\s*(?:\d+\.?\s+)?[A-Z][A-Z\s,&/-]{8,}$", line) for line in text.splitlines())
    conventional_heading = conventional_heading or sum(
        bool(re.match(r"^\s*[A-Z][A-Za-z]*(?:[ :,-]+[A-Z][A-Za-z]*){0,8}\s*$", line))
        for line in text.splitlines()
    ) >= 3
    if not any(line.startswith("#") for line in text.splitlines()) and not conventional_heading:
        flags.append("flattened_headings")
    suffix = raw_path.suffix.lower()
    if suffix == ".pdf" and len(stripped) < 500:
        flags.append("scanned_pdf_suspected")
    if re.search(r"#(?:REF!|VALUE!|NAME\?|DIV/0!)", text, flags=re.IGNORECASE):
        flags.append("formula_damaged")
    if suffix in {".xlsx", ".xls", ".csv", ".tsv"} and stripped and "|" not in text:
        flags.append("flattened_table_suspected")
    return flags
