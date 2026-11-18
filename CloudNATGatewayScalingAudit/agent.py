"""Flags cloud NAT gateways nearing their port-allocation limit, risking connection failures under load."""
from typing import Any


def audit(nat: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    utilization = nat.get("allocated_ports", 0) / nat.get("max_ports", 1)
    if utilization > nat.get("max_acceptable_utilization", 0.8):
        findings.append({"severity": "high", "issue": "NAT gateway port allocation utilization exceeds the acceptable threshold."})
    if not nat.get("port_exhaustion_alerting_enabled"):
        findings.append({"severity": "medium", "issue": "No alerting is configured for NAT port exhaustion."})
    return findings
