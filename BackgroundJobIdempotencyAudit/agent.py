"""Flags background job handlers that perform side effects (payments, emails, writes) without an idempotency key, causing duplicate side effects when the job framework retries after a crash."""
from typing import Any


def audit(job: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    has_side_effects = job.get("performs_external_side_effects", False)
    uses_idempotency_key = job.get("uses_idempotency_key", False)

    if has_side_effects and not uses_idempotency_key:
        findings.append({"severity": "high", "issue": "Job performs external side effects (payments, emails, writes) with no idempotency key, so a retry after a crash can duplicate the side effect."})
    if job.get("at_least_once_delivery") and not job.get("is_handler_idempotent"):
        findings.append({"severity": "high", "issue": "Job queue guarantees only at-least-once delivery but the handler is not idempotent, making duplicate execution a certainty over time rather than a rare edge case."})
    return findings
