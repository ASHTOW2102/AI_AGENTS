"""Review queue retry policy for bounded attempts and backoff behavior."""
from typing import Any


def audit(queue: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if queue.get("max_attempts", 0) > queue.get("approved_max_attempts", 0):
        findings.append({"severity": "medium", "issue": "Retry attempts exceed the approved maximum."})
    if queue.get("max_attempts", 0) > 1 and queue.get("backoff_seconds", 0) <= 0:
        findings.append({"severity": "high", "issue": "Repeated retries have no backoff delay."})
    if queue.get("max_attempts", 0) > 1 and not queue.get("jitter_enabled"):
        findings.append({"severity": "low", "issue": "Retry backoff has no jitter."})
    if queue.get("retry_forever"):
        findings.append({"severity": "high", "issue": "Messages can retry indefinitely without a terminal path."})
    return findings
