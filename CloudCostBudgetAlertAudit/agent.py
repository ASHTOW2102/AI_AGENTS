"""Checks cloud cost budgets for alert thresholds, recipients, and anomaly coverage."""
from typing import Any


def audit(budget: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not budget.get("alert_thresholds"):
        findings.append({"severity": "medium", "issue": "Budget has no alert thresholds configured."})
    if budget.get("alert_thresholds") and not budget.get("alert_recipients"):
        findings.append({"severity": "high", "issue": "Budget alerts have no configured recipients."})
    if budget.get("forecasted_overspend") and not budget.get("forecast_alert_enabled"):
        findings.append({"severity": "medium", "issue": "Forecasted overspend has no proactive alert enabled."})
    return findings
