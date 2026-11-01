"""Checks SOC 2 control evidence entries for freshness, ownership, and testing completeness."""
from typing import Any


def audit(control: dict[str, Any]):
    findings = []
    if not control.get("owner"):
        findings.append({"severity": "high", "issue": "Control has no assigned owner."})
    if control.get("evidence_age_days", 0) > control.get("max_evidence_age_days", 90):
        findings.append({"severity": "medium", "issue": "Control evidence is stale."})
    if not control.get("tested_this_period"):
        findings.append({"severity": "high", "issue": "Control has not been tested this audit period."})
    if control.get("exceptions_found", 0) > 0 and not control.get("remediation_plan"):
        findings.append({"severity": "high", "issue": "Control exceptions found with no remediation plan."})
    return findings
