"""Flags high-risk feature flag changes that can be toggled in production without a second-person approval step."""
from typing import Any


def audit(flag: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if flag.get("risk_level") == "high" and not flag.get("requires_approval_to_toggle"):
        findings.append({"severity": "high", "issue": "High-risk flag can be toggled in production without requiring approval."})
    if flag.get("requires_approval_to_toggle") and flag.get("approver_can_be_same_as_requester"):
        findings.append({"severity": "medium", "issue": "Approval workflow allows the requester to approve their own change."})
    return findings
