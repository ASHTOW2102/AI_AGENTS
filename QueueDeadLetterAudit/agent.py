"""Audit dead-letter queue handling and poison-message recovery controls."""
from typing import Any


def audit(queue: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if queue.get("dead_letter_enabled") is False:
        findings.append({"severity": "high", "issue": "Dead-letter handling is disabled."})
    if queue.get("max_delivery_attempts", 0) <= 0:
        findings.append({"severity": "high", "issue": "No positive delivery-attempt limit is configured."})
    if queue.get("dead_letter_retention_days", 0) < queue.get("replay_window_days", 0):
        findings.append({"severity": "medium", "issue": "Dead-letter retention is shorter than the replay window."})
    if queue.get("oldest_message_age_hours", 0) > queue.get("max_message_age_hours", 0):
        findings.append({"severity": "high", "issue": "Oldest dead-letter message exceeds the handling objective."})
    if queue.get("redrive_without_review"):
        findings.append({"severity": "medium", "issue": "Redrive can occur without operator review."})
    return findings
