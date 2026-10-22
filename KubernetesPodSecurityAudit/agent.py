"""Review workload pod-security settings for privilege and host access."""
from typing import Any


def audit(pod: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pod.get("privileged"):
        findings.append({"severity": "critical", "issue": "Container is configured as privileged."})
    if pod.get("run_as_root"):
        findings.append({"severity": "high", "issue": "Workload runs as root."})
    if pod.get("host_network") or pod.get("host_pid"):
        findings.append({"severity": "high", "issue": "Workload shares host network or process namespace."})
    if not pod.get("read_only_root_filesystem"):
        findings.append({"severity": "medium", "issue": "Root filesystem is writable."})
    if pod.get("capabilities_added"):
        findings.append({"severity": "medium", "issue": "Additional Linux capabilities are configured."})
    return findings
