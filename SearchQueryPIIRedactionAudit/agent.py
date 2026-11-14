"""Flags search query logging pipelines that store raw user queries without redacting PII before persistence."""
from typing import Any


def audit(search: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if search.get("logs_raw_queries") and not search.get("pii_redaction_applied"):
        findings.append({"severity": "high", "issue": "Raw search queries are logged without PII redaction."})
    if search.get("pii_redaction_applied") and not search.get("redaction_coverage_tested"):
        findings.append({"severity": "medium", "issue": "PII redaction is applied but its coverage has not been tested."})
    return findings
