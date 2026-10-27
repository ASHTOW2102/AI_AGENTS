"""Compare cloud IAM grants with approved role baselines."""
from typing import Any


def audit(identity: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    extra = sorted(set(identity.get("granted_actions", [])) - set(identity.get("approved_actions", [])))
    if extra:
        findings.append({"severity": "high", "issue": "Actions exceed role baseline: " + ", ".join(extra)})
    if identity.get("wildcard_resource"):
        findings.append({"severity": "high", "issue": "Role grants access to wildcard resources."})
    if identity.get("unused_days", 0) > identity.get("max_unused_days", 90) and not identity.get("exception_approved"):
        findings.append({"severity": "medium", "issue": "Identity exceeds inactivity limit without an approved exception."})
    if identity.get("human_user") and not identity.get("federated_login"):
        findings.append({"severity": "medium", "issue": "Human cloud access does not use federated login."})
    return findings
