"""Flags service mesh canary deployments with no automated rollback trigger tied to error-rate or latency regression."""
from typing import Any


def audit(deployment: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if deployment.get("uses_canary_traffic_split") and not deployment.get("automated_rollback_on_metric_regression"):
        findings.append({"severity": "high", "issue": "Canary deployment has no automated rollback on metric regression."})
    if deployment.get("automated_rollback_on_metric_regression") and not deployment.get("rollback_tested"):
        findings.append({"severity": "medium", "issue": "Automated rollback trigger exists but has never been tested."})
    return findings
