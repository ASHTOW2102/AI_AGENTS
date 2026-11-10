"""Flags API write endpoints that reuse idempotency keys across semantically different request bodies."""
from typing import Any


def audit(request: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if request.get("idempotency_key_reused") and request.get("body_hash") != request.get("original_body_hash"):
        findings.append({"severity": "high", "issue": "Idempotency key reused with a different request body."})
    if request.get("mutating_method") and not request.get("idempotency_key_present"):
        findings.append({"severity": "medium", "issue": "Mutating request has no idempotency key."})
    return findings
