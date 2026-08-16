#!/usr/bin/env python3
"""Validate the portable fact-checker skill package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REQUIRED = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/status-and-verdicts.md",
    "references/source-evaluation.md",
    "references/publication-modules.md",
    "references/evidence-ledger-schema.json",
    "references/report-output-schema.md",
    "references/role-boundaries.md",
    "references/high-stakes-escalation.md",
    "references/quality-gates.md",
    "references/research-corpus.md",
    "references/qa-test-cases.md",
    "scripts/validate_skill.py",
    "scripts/validate_ledger.py",
)


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    skill_path = root / "SKILL.md"
    if skill_path.is_file():
        text = skill_path.read_text(encoding="utf-8")
        lines = text.splitlines()
        if len(lines) < 4 or lines[0] != "---" or lines[3] != "---":
            errors.append("SKILL.md frontmatter must be a four-line block with name and description")
        else:
            if not re.fullmatch(r"name:\s*fact-checker", lines[1]):
                errors.append("SKILL.md name must be fact-checker")
            description = lines[2].removeprefix("description:").strip()
            if not description or len(description) > 1024:
                errors.append("SKILL.md description must be non-empty and <= 1024 characters")
        if "TODO" in text or "FIXME" in text:
            errors.append("SKILL.md contains TODO/FIXME placeholder")
        if "example.invalid" in text:
            errors.append("SKILL.md contains a placeholder domain")
        for link in re.findall(r"\]\((references/[^)]+)\)", text):
            if not (root / link).is_file():
                errors.append(f"SKILL.md references missing file: {link}")

    metadata = root / "agents/openai.yaml"
    if metadata.is_file():
        yaml_text = metadata.read_text(encoding="utf-8")
        for key in ("display_name", "short_description", "default_prompt"):
            if not re.search(rf"^\s+{key}:\s+\".+\"\s*$", yaml_text, re.MULTILINE):
                errors.append(f"agents/openai.yaml missing quoted interface.{key}")
        if "$fact-checker" not in yaml_text:
            errors.append("agents/openai.yaml default_prompt must mention $fact-checker")

    schema_path = root / "references/evidence-ledger-schema.json"
    if schema_path.is_file():
        try:
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid evidence-ledger-schema.json: {exc}")
        else:
            claim = schema.get("$defs", {}).get("claim", {})
            statuses = claim.get("properties", {}).get("status", {}).get("enum", [])
            if set(statuses) != {"Strongly confirming", "Confirming", "Unable to confirm", "Inaccurate"}:
                errors.append("schema status enum does not match required statuses")
            required = set(claim.get("required", []))
            if "status" in required or "confidence" in required:
                errors.append("schema must allow scope-only claims without status/confidence")
            if "example.invalid" in schema_path.read_text(encoding="utf-8"):
                errors.append("schema contains a placeholder domain")

    for long_reference in ("references/status-and-verdicts.md", "references/source-evaluation.md", "references/research-corpus.md"):
        path = root / long_reference
        if path.is_file() and len(path.read_text(encoding="utf-8").splitlines()) > 100:
            if "## Contents" not in path.read_text(encoding="utf-8"):
                errors.append(f"long reference lacks Contents section: {long_reference}")

    return errors


def main(argv: list[str]) -> int:
    root = Path(argv[1]).resolve() if len(argv) > 1 else Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: validated fact-checker skill at {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
