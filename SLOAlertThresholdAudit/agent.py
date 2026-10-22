"""Check service alert thresholds against documented SLO objectives."""
from typing import Any


def audit(slo: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if slo.get("alert_error_rate_percent", 0) >= slo.get("objective_error_rate_percent", 0):
        findings.append({"severity": "high", "issue": "Error-rate alert triggers at or beyond the SLO limit."})
    if slo.get("alert_latency_ms", 0) >= slo.get("objective_latency_ms", 0):
        findings.append({"severity": "high", "issue": "Latency alert triggers at or beyond the SLO limit."})
    if not slo.get("burn_rate_alert_configured"):
        findings.append({"severity": "medium", "issue": "No error-budget burn-rate alert is configured."})
    if not slo.get("alert_owner"):
        findings.append({"severity": "low", "issue": "SLO alert has no assigned response owner."})
    return findings
