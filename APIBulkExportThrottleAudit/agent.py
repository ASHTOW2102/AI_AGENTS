"""Checks bulk data export endpoints for throttling that prevents full-dataset exfiltration in a single request."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not endpoint.get("max_rows_per_export"):
        findings.append({"severity": "high", "issue": "Bulk export endpoint has no maximum row cap."})
    if endpoint.get("max_rows_per_export") and endpoint.get("max_rows_per_export", 0) > endpoint.get("recommended_row_cap", 10000):
        findings.append({"severity": "medium", "issue": "Export row cap exceeds the recommended limit."})
    return findings
