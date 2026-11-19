"""Flags cloud accounts with no billing anomaly alert covering one or more active cost centers."""
from typing import Any


def audit(account: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    uncovered = [c for c in account.get("active_cost_centers", []) if c not in account.get("cost_centers_with_alerts", [])]
    if uncovered:
        findings.append({"severity": "medium", "issue": f"Cost centers with no billing alert coverage: {uncovered}"})
    if not account.get("org_level_anomaly_detection_enabled"):
        findings.append({"severity": "low", "issue": "No organization-level billing anomaly detection is enabled as a backstop."})
    return findings
