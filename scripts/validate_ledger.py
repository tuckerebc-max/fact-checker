#!/usr/bin/env python3
"""Validate a fact-check evidence ledger using only the Python standard library."""

from __future__ import annotations

import json
import sys
from pathlib import Path


STATUSES = {"Strongly confirming", "Confirming", "Unable to confirm", "Inaccurate"}
POSITIVE = {"Strongly confirming", "Confirming"}
BLOCKED_STRONG_COVERAGE = {"abstract_or_summary_only", "metadata_only", "snippet_only", "no_inspectable_evidence", "not_applicable"}
REQUIRED_COMMON = {"claim_id", "location", "original_text", "atomic_claim", "claim_type", "claim_scope", "materiality", "risk_level", "evidence_coverage", "source_access_level", "reason", "verified_at"}


def validate_ledger(payload: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return ["ledger root must be an object"]
    if not isinstance(payload.get("document"), dict):
        errors.append("missing document object")
    claims = payload.get("claims")
    if not isinstance(claims, list) or not claims:
        return errors + ["claims must be a non-empty array"]

    seen: set[str] = set()
    statuses: list[str] = []
    material_unresolved = False
    material_inaccurate = False

    for index, claim in enumerate(claims):
        prefix = f"claims[{index}]"
        if not isinstance(claim, dict):
            errors.append(f"{prefix} must be an object")
            continue
        for field in sorted(REQUIRED_COMMON - set(claim)):
            errors.append(f"{prefix} missing {field}")

        claim_id = claim.get("claim_id")
        if isinstance(claim_id, str):
            if claim_id in seen:
                errors.append(f"duplicate claim_id: {claim_id}")
            seen.add(claim_id)

        scope = claim.get("claim_scope")
        if scope == "not_fact_checkable":
            if "status" in claim or "confidence" in claim:
                errors.append(f"{prefix} scope-only claim must not contain status or confidence")
            if not claim.get("scope_reason"):
                errors.append(f"{prefix} scope-only claim needs scope_reason")
            if claim.get("source_access_level") != "not_applicable":
                errors.append(f"{prefix} scope-only claim needs source_access_level=not_applicable")
            if claim.get("evidence_coverage") != "not_applicable":
                errors.append(f"{prefix} scope-only claim needs evidence_coverage=not_applicable")
            continue

        if scope not in {"fact_checkable", "mixed_factual_and_nonfactual"}:
            errors.append(f"{prefix} has invalid claim_scope: {scope!r}")
        for field in ("status", "confidence"):
            if field not in claim:
                errors.append(f"{prefix} missing {field}")

        status = claim.get("status")
        if status not in STATUSES:
            errors.append(f"{prefix} has invalid status: {status!r}")
            continue
        statuses.append(status)
        material = claim.get("materiality") in {"critical", "high"} or claim.get("risk_level") in {"critical", "high"}
        if material and status == "Unable to confirm":
            material_unresolved = True
        if material and status == "Inaccurate":
            material_inaccurate = True

        if status == "Unable to confirm" and not claim.get("unable_subtype"):
            errors.append(f"{prefix} Unable to confirm needs unable_subtype")
        if status == "Inaccurate" and not claim.get("inaccuracy_type"):
            errors.append(f"{prefix} Inaccurate needs inaccuracy_type")
        if status == "Strongly confirming":
            if claim.get("evidence_coverage") in BLOCKED_STRONG_COVERAGE:
                errors.append(f"{prefix} Strongly confirming cannot use {claim.get('evidence_coverage')}")
            if claim.get("source_access_level") not in {"direct_full_access", "partial_access"}:
                errors.append(f"{prefix} Strongly confirming requires direct or partial source access")
        if status in POSITIVE:
            support = claim.get("supporting_evidence")
            if not isinstance(support, list) or not support:
                errors.append(f"{prefix} positive status needs supporting_evidence")
        if status == "Inaccurate":
            counter = claim.get("counterevidence")
            citation_support = str(claim.get("citation_support", ""))
            if not isinstance(counter, list) or not counter:
                if "does not support" not in citation_support.lower():
                    errors.append(f"{prefix} Inaccurate needs counterevidence or citation-support failure")
        if not isinstance(claim.get("reason"), str) or not claim.get("reason", "").strip():
            errors.append(f"{prefix} needs a non-empty reason")

    overall = payload.get("overall")
    if isinstance(overall, dict) and overall.get("status") in STATUSES:
        overall_status = overall["status"]
        if material_inaccurate and overall_status != "Inaccurate":
            errors.append("overall status must be Inaccurate when a material claim is Inaccurate")
        if material_unresolved and overall_status in {"Confirming", "Strongly confirming"}:
            errors.append("overall status cannot be Confirming or Strongly confirming with a material unresolved claim")
        if overall_status == "Strongly confirming" and any(status != "Strongly confirming" for status in statuses):
            errors.append("overall Strongly confirming requires every fact-checkable claim to be Strongly confirming")
        if len(set(statuses)) > 1 and overall.get("mixed_findings") is not True:
            errors.append("mixed fact-checkable statuses require mixed_findings=true")

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python validate_ledger.py path/to/ledger.json")
        return 2
    path = Path(argv[1])
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"FAIL: file not found: {path}")
        return 1
    except json.JSONDecodeError as exc:
        print(f"FAIL: invalid JSON: {exc}")
        return 1
    errors = validate_ledger(payload)
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: ledger validated: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
