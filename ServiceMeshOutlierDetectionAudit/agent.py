"""Checks service-mesh outlier detection ejects unhealthy endpoints without overreacting to blips."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not service.get("outlier_detection_enabled"):
        findings.append({"severity": "medium", "issue": "Service has no outlier detection to eject failing endpoints."})
    if service.get("outlier_detection_enabled") and service.get("consecutive_errors_threshold", 0) <= 1:
        findings.append({"severity": "medium", "issue": "Outlier ejection triggers on a single error, risking flapping."})
    if service.get("ejected_endpoint_count", 0) >= service.get("total_endpoint_count", 1):
        findings.append({"severity": "high", "issue": "All endpoints have been ejected, causing a full outage."})
    return findings
