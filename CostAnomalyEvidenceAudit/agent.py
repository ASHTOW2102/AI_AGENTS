"""Assess cloud cost anomalies for ownership and investigation evidence."""
from typing import Any


def audit(anomaly: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if anomaly.get("variance_percent", 0) >= anomaly.get("alert_threshold_percent", 100) and not anomaly.get("alert_emitted"):
        findings.append({"severity": "high", "issue": "Cost variance exceeded threshold without an alert."})
    if anomaly.get("monthly_estimate", 0) >= anomaly.get("materiality_amount", 0) and not anomaly.get("owner"):
        findings.append({"severity": "medium", "issue": "Material cost anomaly has no assigned owner."})
    if anomaly.get("resolved") and not anomaly.get("resolution_note"):
        findings.append({"severity": "low", "issue": "Resolved anomaly has no investigation or resolution note."})
    if anomaly.get("service") is None:
        findings.append({"severity": "low", "issue": "Anomaly is not attributed to a service."})
    return findings
