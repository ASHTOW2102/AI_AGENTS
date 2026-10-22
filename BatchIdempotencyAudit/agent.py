"""Review batch-job retry behavior and idempotency safeguards."""
from typing import Any


def audit(job: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if job.get("retry_enabled") and not job.get("idempotency_key"):
        findings.append({"severity": "high", "issue": "Retryable batch job has no idempotency key."})
    if job.get("retry_enabled") and job.get("max_attempts", 0) < 1:
        findings.append({"severity": "medium", "issue": "Retry is enabled without a positive attempt limit."})
    if job.get("writes_external_state") and not job.get("deduplication_store"):
        findings.append({"severity": "high", "issue": "External writes lack a deduplication record."})
    if job.get("idempotency_ttl_hours", 0) < job.get("max_retry_window_hours", 0):
        findings.append({"severity": "medium", "issue": "Idempotency record expires before the retry window."})
    return findings
