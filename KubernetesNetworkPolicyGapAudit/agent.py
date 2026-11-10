"""Flags Kubernetes namespaces with no default-deny NetworkPolicy, leaving pod-to-pod traffic unrestricted."""
from typing import Any


def audit(namespace: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not namespace.get("default_deny_policy_present"):
        findings.append({"severity": "high", "issue": "Namespace has no default-deny NetworkPolicy."})
    if namespace.get("default_deny_policy_present") and namespace.get("unrestricted_egress"):
        findings.append({"severity": "medium", "issue": "Default-deny policy exists but egress remains unrestricted."})
    return findings
