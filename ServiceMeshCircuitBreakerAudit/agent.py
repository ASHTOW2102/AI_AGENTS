"""Flags service mesh routes with no circuit breaker configured, letting a single failing dependency cascade into widespread resource exhaustion."""
from typing import Any


def audit(mesh: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not mesh.get("circuit_breaker_configured"):
        findings.append({"severity": "medium", "issue": "No circuit breaker configured; a failing dependency can cascade into resource exhaustion."})
    return findings
