"""Checks that mobile apps handling sensitive operations detect rooted or jailbroken devices."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if app.get("handles_sensitive_operations") and not app.get("root_detection_enabled"):
        findings.append({"severity": "high", "issue": "App handling sensitive operations has no root/jailbreak detection."})
    if app.get("root_detection_enabled") and not app.get("response_on_detection"):
        findings.append({"severity": "medium", "issue": "Root detection exists but has no defined response action."})
    return findings
