"""Flags VPC peering connections that allow transitive routing to a third network the peer was never authorized to reach."""
from typing import Any


def audit(peering: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if peering.get("route_propagation_enabled") and not peering.get("transit_routes_reviewed"):
        findings.append({"severity": "high", "issue": "Route propagation is enabled without reviewing which transit routes it exposes."})
    if peering.get("allows_transitive_peering"):
        findings.append({"severity": "medium", "issue": "Peering connection allows transitive access to networks beyond the direct peer."})
    return findings
