"""Flags networks with no detection in place for sequential port-scanning activity against internal hosts."""
from typing import Any


def audit(network: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not network.get("port_scan_detection_enabled"):
        findings.append({"severity": "high", "issue": "No port-scan detection is enabled on this network."})
    if network.get("port_scan_detection_enabled") and network.get("detection_to_alert_latency_seconds", 0) > network.get("max_acceptable_latency_seconds", 300):
        findings.append({"severity": "medium", "issue": "Port-scan detection-to-alert latency exceeds the acceptable threshold."})
    return findings
