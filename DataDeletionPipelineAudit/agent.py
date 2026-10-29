"""Review data deletion jobs for request coverage and completion evidence."""
from typing import Any


def audit(pipeline: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pipeline.get("deletion_requests_pending", 0) > 0 and not pipeline.get("scheduled_worker_enabled"):
        findings.append({"severity": "high", "issue": "Pending deletion requests have no active processing worker."})
    if pipeline.get("worker_enabled") and not pipeline.get("retry_dead_letter_handling"):
        findings.append({"severity": "medium", "issue": "Deletion worker failures have no retry or dead-letter handling."})
    if pipeline.get("completion_requires_evidence") and not pipeline.get("evidence_store_configured"):
        findings.append({"severity": "high", "issue": "Deletion completion has no configured evidence store."})
    if pipeline.get("oldest_pending_age_hours", 0) > pipeline.get("max_pending_age_hours", 24):
        findings.append({"severity": "high", "issue": "Oldest deletion request exceeds its completion objective."})
    return findings
