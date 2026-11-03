"""Checks webhook delivery failure handling for dead-letter storage and alerting coverage."""
from typing import Any


def audit(webhook: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if webhook.get("max_retries_exhausted_count", 0) > 0 and not webhook.get("dead_letter_storage_configured"):
        findings.append({"severity": "high", "issue": "Exhausted webhook deliveries are discarded with no dead-letter storage."})
    if webhook.get("dead_letter_storage_configured") and not webhook.get("dead_letter_alerting"):
        findings.append({"severity": "medium", "issue": "Dead-lettered webhook deliveries have no alerting."})
    if webhook.get("dead_letter_backlog_age_hours", 0) > webhook.get("max_backlog_age_hours", 24):
        findings.append({"severity": "medium", "issue": "Dead-letter backlog exceeds the review age limit."})
    return findings
