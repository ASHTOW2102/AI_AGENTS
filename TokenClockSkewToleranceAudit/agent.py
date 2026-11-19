"""Flags token validators with clock skew tolerance set so loosely that it meaningfully extends a token's effective lifetime past expiry."""
from typing import Any


def audit(validator: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if validator.get("clock_skew_tolerance_seconds", 0) > validator.get("max_acceptable_tolerance_seconds", 60):
        findings.append({"severity": "medium", "issue": "Clock skew tolerance is set far looser than needed, extending effective token lifetime."})
    if not validator.get("clock_skew_tolerance_configured"):
        findings.append({"severity": "low", "issue": "No explicit clock skew tolerance is configured; relying on library defaults."})
    return findings
