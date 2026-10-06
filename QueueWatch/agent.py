from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    item: int
    message: str

@dataclass(frozen=True)
class AuditReport:
    healthy: bool
    items_checked: int
    findings: list[Finding]
    recommendations: list[str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def audit(items: list[dict[str, Any]]) -> AuditReport:
    if not isinstance(items, list) or not items:
        raise ValueError("queues must be a non-empty JSON array")
    findings: list[Finding] = []
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict):
            raise ValueError(f"item {index} must be an object")
        name = str(item.get("name", "")).strip()
        if not name:
            raise ValueError(f"item {index}.name is required")
        numbers = {}
        for field in ("backlog", "consumers", "oldest_message_seconds", "dead_letters", "sla_seconds"):
            value = item.get(field)
            if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
                raise ValueError(f"item {index}.{field} must be a non-negative number")
            numbers[field] = value
        if numbers["backlog"] and not numbers["consumers"]:
            findings.append(Finding("no_consumers", "critical", index, f"{name} has backlog but no consumers."))
        if numbers["oldest_message_seconds"] > numbers["sla_seconds"]:
            findings.append(Finding("stale_messages", "high", index, f"{name} has messages older than its SLA."))
        if numbers["dead_letters"] > 0:
            findings.append(Finding("dead_letters", "high", index, f"{name} has dead-lettered messages."))
        if numbers["consumers"] and numbers["backlog"] / numbers["consumers"] > 100:
            findings.append(Finding("high_backlog", "medium", index, f"{name} exceeds 100 queued messages per consumer."))
    codes = {finding.code for finding in findings}
    recommendations = (
        [f"Review and resolve: {', '.join(sorted(codes))}.", "Confirm findings against the live system before making changes."]
        if findings else ["No configured risks were detected."]
    )
    return AuditReport(not findings, len(items), findings, recommendations)

class QueueWatchAgent:
    def inspect(self, items: list[dict[str, Any]]) -> AuditReport:
        return audit(items)
