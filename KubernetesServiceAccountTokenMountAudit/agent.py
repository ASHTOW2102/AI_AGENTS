"""Flags Kubernetes pods that auto-mount a service account token despite not calling the Kubernetes API."""
from typing import Any


def audit(pod: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pod.get("automount_service_account_token") and not pod.get("calls_kubernetes_api"):
        findings.append({"severity": "medium", "issue": "Service account token is mounted but the pod never calls the Kubernetes API."})
    if pod.get("calls_kubernetes_api") and pod.get("service_account") == "default":
        findings.append({"severity": "high", "issue": "Pod calling the Kubernetes API uses the default service account rather than a scoped one."})
    return findings
