"""Flags serverless functions with no dead-letter queue configured for failed asynchronous invocations."""
from typing import Any


def audit(function: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if function.get("invocation_type") == "async" and not function.get("dead_letter_queue_configured"):
        findings.append({"severity": "high", "issue": "Async function has no dead-letter queue for failed invocations."})
    if function.get("dead_letter_queue_configured") and not function.get("dlq_alerting_enabled"):
        findings.append({"severity": "medium", "issue": "Dead-letter queue exists but has no alerting on new messages."})
    return findings
