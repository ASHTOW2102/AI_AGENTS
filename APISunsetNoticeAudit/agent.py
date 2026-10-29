"""Review API deprecation and sunset communication coverage."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("deprecated") and not endpoint.get("deprecation_date"):
        findings.append({"severity": "medium", "issue": "Deprecated endpoint has no deprecation date."})
    if endpoint.get("deprecated") and not endpoint.get("successor_documented"):
        findings.append({"severity": "medium", "issue": "Deprecated endpoint has no documented successor."})
    if endpoint.get("sunset_date") and not endpoint.get("consumer_notice_sent"):
        findings.append({"severity": "high", "issue": "Sunset date is set but consumers have not been notified."})
    if endpoint.get("sunset_date") and endpoint.get("days_until_sunset", 99999) < endpoint.get("minimum_notice_days", 90):
        findings.append({"severity": "low", "issue": "Sunset notice window is shorter than policy."})
    return findings
