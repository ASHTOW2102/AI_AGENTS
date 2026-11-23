"""Flags IAM roles that combine the ability to create/attach policies with the ability to pass roles to services, a well-known privilege-escalation pair."""
from typing import Any


def audit(iam_role: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if iam_role.get("has_pass_role_permission") and iam_role.get("has_create_policy_permission"):
        findings.append({"severity": "high", "issue": "Role can both pass roles to services and create/attach policies, enabling privilege escalation."})
    return findings
