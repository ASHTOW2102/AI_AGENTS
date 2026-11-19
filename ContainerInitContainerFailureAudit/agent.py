"""Flags Kubernetes pods whose init containers can fail silently, letting the main container start in a misconfigured state."""
from typing import Any


def audit(pod: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pod.get("has_init_containers") and not pod.get("init_container_failure_blocks_main_container"):
        findings.append({"severity": "high", "issue": "Init container failure does not block the main container from starting."})
    if pod.get("has_init_containers") and not pod.get("init_container_failures_alerted"):
        findings.append({"severity": "medium", "issue": "Init container failures are not alerted on."})
    return findings
