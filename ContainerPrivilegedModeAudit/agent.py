"""Checks container runtime configuration for privileged mode and host-namespace sharing."""
from typing import Any


def audit(container: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if container.get("privileged"):
        findings.append({"severity": "critical", "issue": "Container runs in privileged mode."})
    if container.get("host_network"):
        findings.append({"severity": "high", "issue": "Container shares the host network namespace."})
    if container.get("host_pid"):
        findings.append({"severity": "high", "issue": "Container shares the host PID namespace."})
    if container.get("added_capabilities"):
        findings.append({"severity": "medium", "issue": "Container adds Linux capabilities beyond the default set."})
    return findings
