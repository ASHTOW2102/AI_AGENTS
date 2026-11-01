"""Checks container image vulnerability scan results against severity and age policy."""
from typing import Any


def audit(image: dict[str, Any]):
    findings = []
    if image.get("critical_cve_count", 0) > 0 and not image.get("critical_cve_waiver"):
        findings.append({"severity": "critical", "issue": "Image has unwaived critical CVEs."})
    if image.get("high_cve_count", 0) > image.get("max_high_cve_count", 0):
        findings.append({"severity": "high", "issue": "High-severity CVE count exceeds policy."})
    if image.get("scan_age_days", 0) > image.get("max_scan_age_days", 7):
        findings.append({"severity": "medium", "issue": "Image vulnerability scan is stale."})
    return findings
