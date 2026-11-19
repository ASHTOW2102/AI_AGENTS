"""Flags database triggers that can recursively fire other triggers with no depth limit, risking runaway cascades on bulk writes."""
from typing import Any


def audit(trigger: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if trigger.get("can_trigger_other_triggers") and not trigger.get("cascade_depth_limited"):
        findings.append({"severity": "high", "issue": "Trigger can cascade into other triggers with no depth limit."})
    if trigger.get("fires_on_bulk_operations") and not trigger.get("bulk_operation_performance_tested"):
        findings.append({"severity": "medium", "issue": "Trigger fires on bulk operations but has not been performance-tested at scale."})
    return findings
