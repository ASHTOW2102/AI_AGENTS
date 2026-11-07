"""Checks that risky feature flags have a verified kill switch path for rapid rollback."""
from typing import Any


def audit(flag: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if flag.get("risk_level") == "high" and not flag.get("kill_switch_tested"):
        findings.append({"severity": "high", "issue": "High-risk flag has no tested kill switch."})
    if flag.get("kill_switch_tested") and flag.get("rollback_time_seconds", 0) > flag.get("max_acceptable_rollback_seconds", 60):
        findings.append({"severity": "medium", "issue": "Kill switch rollback time exceeds the acceptable threshold."})
    return findings
