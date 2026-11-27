"""Flags load balancers whose targets span multiple availability zones but cross-zone load balancing is disabled, leaving traffic distribution uneven and single-zone-fragile."""
from typing import Any


def audit(lb: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if lb.get("targets_span_multiple_zones") and not lb.get("cross_zone_load_balancing_enabled"):
        findings.append({"severity": "medium", "issue": "Targets span multiple zones but cross-zone load balancing is disabled."})
    return findings
