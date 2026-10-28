"""Review model deployment rollback readiness and artifact availability."""
from typing import Any


def audit(deployment: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not deployment.get("previous_model_artifact_retained"):
        findings.append({"severity": "high", "issue": "Previous model artifact is not retained for rollback."})
    if not deployment.get("rollback_route_tested"):
        findings.append({"severity": "medium", "issue": "Model rollback route has not been tested."})
    if deployment.get("feature_schema_changed") and not deployment.get("backward_compatible_schema"):
        findings.append({"severity": "high", "issue": "Feature schema change is not backward-compatible with rollback model."})
    if deployment.get("rollback_slo_minutes", 0) > deployment.get("max_rollback_slo_minutes", 0):
        findings.append({"severity": "medium", "issue": "Rollback duration exceeds the recovery objective."})
    return findings
