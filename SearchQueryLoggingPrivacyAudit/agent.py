"""Checks search query logs for personal-data redaction and retention limits."""
from typing import Any


def audit(search: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if search.get("logs_raw_query_text") and not search.get("pii_redaction_applied"):
        findings.append({"severity": "high", "issue": "Raw search queries are logged without PII redaction."})
    if search.get("query_linked_to_user_id") and not search.get("retention_limit_days"):
        findings.append({"severity": "medium", "issue": "User-linked search logs have no retention limit."})
    if search.get("logs_shared_with_analytics_vendor") and not search.get("vendor_dpa_signed"):
        findings.append({"severity": "high", "issue": "Search logs are shared with a vendor lacking a signed data processing agreement."})
    return findings
