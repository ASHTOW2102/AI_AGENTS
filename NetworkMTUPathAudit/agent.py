"""Review network path MTU assumptions and fragmentation evidence."""
from typing import Any


def audit(path: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if path.get("interface_mtu", 0) > path.get("path_mtu", 0):
        findings.append({"severity": "high", "issue": "Interface MTU exceeds the measured path MTU."})
    if path.get("large_payloads_expected") and not path.get("path_mtu_discovery_working"):
        findings.append({"severity": "medium", "issue": "Path MTU discovery is not confirmed for large payloads."})
    if path.get("fragmentation_observed") and not path.get("fragmentation_acceptable"):
        findings.append({"severity": "medium", "issue": "Unexpected packet fragmentation was observed."})
    if not path.get("mtu_monitoring_configured"):
        findings.append({"severity": "low", "issue": "No monitoring is configured for path MTU failures."})
    return findings
