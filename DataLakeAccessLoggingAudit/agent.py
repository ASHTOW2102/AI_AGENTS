"""Flags data lake storage layers with object-level access logging disabled."""
from typing import Any


def audit(lake: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not lake.get("access_logging_enabled"):
        findings.append({"severity": "high", "issue": "Data lake has no object-level access logging enabled."})
    if lake.get("access_logging_enabled") and lake.get("log_retention_days", 0) < lake.get("min_required_retention_days", 90):
        findings.append({"severity": "medium", "issue": "Access log retention is shorter than the required minimum."})
    return findings
