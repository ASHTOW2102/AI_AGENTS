"""Checks network segmentation boundaries between trust zones for unexpected open paths."""
from typing import Any


def audit(path: dict[str, Any]):
    findings = []
    if path.get("source_zone") == "public" and path.get("destination_zone") == "data" and not path.get("approved"):
        findings.append({"severity": "critical", "issue": "Unapproved path from public zone directly to data zone."})
    if path.get("source_zone") != path.get("destination_zone") and not path.get("firewall_rule_documented"):
        findings.append({"severity": "medium", "issue": "Cross-zone path has no documented firewall rule."})
    if path.get("port_range_open", False) and not path.get("port_range_justified"):
        findings.append({"severity": "medium", "issue": "Open port range lacks a documented justification."})
    return findings
