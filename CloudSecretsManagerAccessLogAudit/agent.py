"""Flags secrets manager entries with access logging disabled, making it impossible to detect unauthorized reads."""
from typing import Any


def audit(secret: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not secret.get("access_logging_enabled"):
        findings.append({"severity": "high", "issue": "Secret has no access logging enabled."})
    if secret.get("access_logging_enabled") and not secret.get("unusual_access_alerting_enabled"):
        findings.append({"severity": "medium", "issue": "Access is logged but no alerting exists for unusual access patterns."})
    return findings
