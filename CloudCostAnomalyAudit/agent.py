"""Detects anomalous cloud spend spikes relative to historical baselines."""
from typing import Any


def audit(billing: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    baseline = billing.get("baseline_daily_cost", 0)
    current = billing.get("current_daily_cost", 0)
    if baseline > 0 and current > baseline * billing.get("anomaly_multiplier", 2):
        findings.append({"severity": "high", "issue": "Current daily cost exceeds the anomaly threshold over baseline."})
    if not billing.get("budget_alert_configured"):
        findings.append({"severity": "medium", "issue": "No budget alert is configured for this cost center."})
    return findings
