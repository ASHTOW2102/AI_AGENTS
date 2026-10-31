"""Review ML drift metrics for threshold and alert coverage."""
from typing import Any


def audit(model: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if model.get("drift_metric_enabled") and not model.get("drift_alert_configured"):
        findings.append({"severity": "high", "issue": "Drift is measured but no alert is configured."})
    if model.get("drift_alert_configured") and model.get("drift_threshold") is None:
        findings.append({"severity": "medium", "issue": "Drift alert has no threshold."})
    if model.get("production") and not model.get("feature_drift_monitored"):
        findings.append({"severity": "high", "issue": "Production model has no feature-drift monitoring."})
    if model.get("alert_owner") is None:
        findings.append({"severity": "low", "issue": "Drift alerts have no response owner."})
    return findings
