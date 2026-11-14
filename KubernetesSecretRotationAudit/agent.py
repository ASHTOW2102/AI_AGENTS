"""Flags Kubernetes secrets that have not been rotated within policy and lack automated rotation."""
from typing import Any


def audit(secret: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if secret.get("age_days", 0) > secret.get("max_acceptable_age_days", 90):
        findings.append({"severity": "high", "issue": "Secret exceeds the maximum acceptable age without rotation."})
    if not secret.get("automated_rotation_enabled"):
        findings.append({"severity": "medium", "issue": "Secret has no automated rotation configured."})
    return findings
