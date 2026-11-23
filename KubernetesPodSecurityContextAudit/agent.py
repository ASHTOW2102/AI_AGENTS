"""Flags Kubernetes pods whose security context allows privilege escalation or does not require running as a non-root user."""
from typing import Any


def audit(pod: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pod.get("allow_privilege_escalation"):
        findings.append({"severity": "high", "issue": "Pod security context allows privilege escalation."})
    if not pod.get("run_as_non_root"):
        findings.append({"severity": "medium", "issue": "Pod security context does not require running as a non-root user."})
    return findings
