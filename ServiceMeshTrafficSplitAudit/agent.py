"""Checks service-mesh weighted traffic splits sum correctly and honor rollback triggers."""
from typing import Any


def audit(route: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    total_weight = sum(route.get("weights", {}).values())
    if route.get("weights") and total_weight != 100:
        findings.append({"severity": "high", "issue": "Traffic-split weights sum to " + str(total_weight) + " instead of 100."})
    if route.get("canary_weight", 0) > 0 and not route.get("automatic_rollback_configured"):
        findings.append({"severity": "medium", "issue": "Canary traffic split has no automatic rollback trigger."})
    if route.get("stale_split_age_hours", 0) > route.get("max_split_age_hours", 24):
        findings.append({"severity": "low", "issue": "Traffic split has remained unpromoted longer than expected."})
    return findings
