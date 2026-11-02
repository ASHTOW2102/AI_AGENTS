"""Checks container workloads for root-user execution and privilege-escalation settings."""
from typing import Any


def audit(container: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if container.get("run_as_user", 0) == 0:
        findings.append({"severity": "high", "issue": "Container runs as the root user."})
    if container.get("allow_privilege_escalation", True):
        findings.append({"severity": "high", "issue": "Container allows privilege escalation."})
    if not container.get("read_only_root_filesystem") and container.get("writable_root_required") is False:
        findings.append({"severity": "low", "issue": "Root filesystem is writable though the workload does not need it."})
    return findings
