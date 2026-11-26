"""Flags feature flag systems that do not log who changed a flag and when, leaving incident response with no change history to investigate."""
from typing import Any


def audit(flag_system: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not flag_system.get("logs_flag_changes"):
        findings.append({"severity": "medium", "issue": "Feature flag changes are not logged, leaving no audit trail for incident response."})
    return findings
