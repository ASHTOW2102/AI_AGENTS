"""Flags service mesh routing that ignores availability-zone locality, causing unnecessary cross-zone traffic cost and latency."""
from typing import Any


def audit(mesh: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not mesh.get("zone_aware_routing_enabled"):
        findings.append({"severity": "medium", "issue": "Zone-aware routing is not enabled, causing unnecessary cross-zone traffic."})
    if mesh.get("cross_zone_traffic_percent", 0) > mesh.get("max_acceptable_cross_zone_percent", 30):
        findings.append({"severity": "low", "issue": "Cross-zone traffic percentage exceeds the acceptable threshold."})
    return findings
