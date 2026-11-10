"""Checks that database replication lag has an alerting threshold and is within acceptable bounds."""
from typing import Any


def audit(replica: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not replica.get("lag_alert_configured"):
        findings.append({"severity": "medium", "issue": "No alert is configured for replication lag."})
    if replica.get("current_lag_seconds", 0) > replica.get("max_acceptable_lag_seconds", 30):
        findings.append({"severity": "high", "issue": "Current replication lag exceeds the acceptable threshold."})
    return findings
