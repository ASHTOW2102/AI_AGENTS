"""Checks live ConfigMap values against declared manifest source to detect undocumented drift."""
from typing import Any


def audit(configmap: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    drifted = sorted(k for k in configmap.get("live_values", {}) if configmap.get("live_values", {}).get(k) != configmap.get("declared_values", {}).get(k))
    if drifted:
        findings.append({"severity": "high", "issue": "ConfigMap keys drifted from declared source: " + ", ".join(drifted)})
    if configmap.get("mounted_as_env") and configmap.get("requires_restart_on_change") and not configmap.get("restart_triggered_on_change"):
        findings.append({"severity": "medium", "issue": "Config change requires a restart that is not automatically triggered."})
    if configmap.get("contains_secret_like_values"):
        findings.append({"severity": "high", "issue": "ConfigMap holds secret-like values that belong in a Secret object."})
    return findings
