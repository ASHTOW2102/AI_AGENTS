"""Check incident records for timeline, impact, actions, and closure evidence."""
from typing import Any


def audit(incident: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    required = {"start_time": "incident start time", "impact_summary": "impact summary",
                "root_cause": "root-cause summary", "resolution_time": "resolution time"}
    for field, label in required.items():
        if not incident.get(field):
            findings.append({"severity": "medium", "issue": f"Incident record is missing {label}."})
    if incident.get("follow_up_actions", 0) > 0 and not incident.get("action_owners_assigned"):
        findings.append({"severity": "low", "issue": "Follow-up actions have no assigned owners."})
    if incident.get("customer_impact") and not incident.get("customer_communication_reference"):
        findings.append({"severity": "medium", "issue": "Customer impact has no communication evidence reference."})
    return findings
