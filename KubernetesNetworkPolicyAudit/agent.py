"""Review Kubernetes namespace network-policy coverage metadata."""
from typing import Any


def audit(namespace: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not namespace.get("default_deny_ingress"):
        findings.append({"severity": "high", "issue": "Namespace has no default-deny ingress policy."})
    if not namespace.get("default_deny_egress"):
        findings.append({"severity": "medium", "issue": "Namespace has no default-deny egress policy."})
    if namespace.get("public_workloads", 0) > 0 and not namespace.get("public_ingress_reviewed"):
        findings.append({"severity": "high", "issue": "Publicly reachable workloads lack recorded ingress review."})
    if namespace.get("unrestricted_egress_rules", 0) > 0:
        findings.append({"severity": "medium", "issue": "Network policies contain unrestricted egress rules."})
    return findings
