"""Checks workload taint tolerations for overly broad scheduling onto restricted nodes."""
from typing import Any


def audit(workload: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if workload.get("tolerates_all_taints"):
        findings.append({"severity": "high", "issue": "Workload tolerates all node taints without restriction."})
    for toleration in workload.get("tolerations", []):
        if toleration.get("operator") == "Exists" and not toleration.get("key"):
            findings.append({"severity": "medium", "issue": "Toleration matches on Exists with no specific key."})
    if workload.get("scheduled_on_restricted_node") and not workload.get("restricted_node_approved"):
        findings.append({"severity": "high", "issue": "Workload is scheduled on a restricted node without approval."})
    return findings
