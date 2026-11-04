"""Checks cloud NAT gateway port allocation and failure-alert coverage for outbound capacity limits."""
from typing import Any


def audit(nat: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if nat.get("port_allocation_errors", 0) > 0:
        findings.append({"severity": "high", "issue": "NAT gateway is dropping connections due to port allocation errors."})
    if nat.get("concurrent_connections", 0) > nat.get("estimated_port_capacity", 0) * 0.8:
        findings.append({"severity": "medium", "issue": "Connection volume approaches the NAT gateway's port capacity."})
    if not nat.get("single_gateway_redundancy") and nat.get("critical_path"):
        findings.append({"severity": "high", "issue": "Critical path depends on a single NAT gateway with no redundancy."})
    return findings
