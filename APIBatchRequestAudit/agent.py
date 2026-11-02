"""Checks batch API endpoints for item-count limits and partial-failure reporting."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not endpoint.get("max_batch_size"):
        findings.append({"severity": "high", "issue": "Batch endpoint has no maximum item-count limit."})
    if endpoint.get("partial_failure_possible") and not endpoint.get("per_item_status_reported"):
        findings.append({"severity": "high", "issue": "Partial batch failures are not reported per item."})
    if endpoint.get("atomic_required") and not endpoint.get("transactional_execution"):
        findings.append({"severity": "medium", "issue": "Batch requiring atomicity does not execute transactionally."})
    return findings
