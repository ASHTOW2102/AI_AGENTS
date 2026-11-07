"""Detects schema version skew between API producers and consumers."""
from typing import Any


def audit(api: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if api.get("producer_schema_version") != api.get("consumer_schema_version"):
        findings.append({"severity": "high", "issue": "Producer and consumer schema versions differ."})
    if not api.get("schema_registry_checked"):
        findings.append({"severity": "medium", "issue": "Schema compatibility was not checked against a registry."})
    if api.get("breaking_change_detected"):
        findings.append({"severity": "high", "issue": "A breaking schema change was detected without a migration plan."})
    return findings
