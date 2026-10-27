"""Review search indexing delay and backlog against freshness objectives."""
from typing import Any


def audit(index: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if index.get("observed_lag_seconds", 0) > index.get("max_lag_seconds", 0):
        findings.append({"severity": "high", "issue": "Search indexing lag exceeds the freshness objective."})
    if index.get("failed_documents", 0) > 0:
        findings.append({"severity": "medium", "issue": "One or more documents failed indexing."})
    if index.get("oldest_queued_age_seconds", 0) > index.get("max_queued_age_seconds", 0):
        findings.append({"severity": "medium", "issue": "Oldest queued document exceeds the processing limit."})
    if not index.get("lag_alert_configured"):
        findings.append({"severity": "low", "issue": "No alert is configured for index freshness lag."})
    return findings
