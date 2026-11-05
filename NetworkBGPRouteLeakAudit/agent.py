"""Checks BGP route advertisements for unintended leaks of internal prefixes to external peers."""
from typing import Any


def audit(route: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if route.get("internal_prefix") and route.get("advertised_to_external_peer"):
        findings.append({"severity": "critical", "issue": "Internal prefix is advertised to an external peer."})
    if not route.get("prefix_filter_configured"):
        findings.append({"severity": "high", "issue": "No prefix filter is configured on the peering session."})
    if route.get("max_prefix_limit_configured") is False:
        findings.append({"severity": "medium", "issue": "Peering session has no maximum prefix limit."})
    return findings
