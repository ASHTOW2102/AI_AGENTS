"""Flags Kubernetes admission webhooks with timeout or failure policy settings that risk cluster-wide blocking."""
from typing import Any


def audit(webhook: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if webhook.get("timeout_seconds", 0) > webhook.get("max_acceptable_timeout_seconds", 10):
        findings.append({"severity": "medium", "issue": "Admission webhook timeout exceeds the acceptable threshold."})
    if webhook.get("failure_policy") == "Fail" and not webhook.get("high_availability_configured"):
        findings.append({"severity": "high", "issue": "Fail-closed webhook has no high-availability deployment."})
    return findings
