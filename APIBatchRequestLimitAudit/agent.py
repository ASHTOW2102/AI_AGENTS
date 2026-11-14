"""Flags batch API endpoints with no cap on the number of operations per batch request."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not endpoint.get("max_batch_size"):
        findings.append({"severity": "high", "issue": "Batch endpoint has no maximum batch size limit."})
    if endpoint.get("max_batch_size") and endpoint.get("max_batch_size", 0) > endpoint.get("recommended_max_batch_size", 100):
        findings.append({"severity": "medium", "issue": "Batch size limit exceeds the recommended maximum."})
    return findings
