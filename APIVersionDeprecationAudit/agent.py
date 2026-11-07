"""Audits deprecated API versions still receiving traffic without a sunset notice to clients."""
from typing import Any


def audit(api: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if api.get("deprecated") and api.get("active_traffic", 0) > 0 and not api.get("sunset_header_present"):
        findings.append({"severity": "medium", "issue": "Deprecated API version receives traffic without a Sunset header."})
    if api.get("deprecated") and not api.get("sunset_date"):
        findings.append({"severity": "medium", "issue": "Deprecated API version has no announced sunset date."})
    return findings
