"""Evaluate whether sensitive fields are covered by log redaction rules."""
from typing import Any


def audit(policy: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    sensitive = set(policy.get("sensitive_fields", []))
    redacted = set(policy.get("redacted_fields", []))
    missing = sorted(sensitive - redacted)
    if missing:
        findings.append({"severity": "high", "issue": "Sensitive fields missing redaction: " + ", ".join(missing)})
    if policy.get("sampled_unredacted_events", 0) > 0:
        findings.append({"severity": "critical", "issue": "Unredacted sensitive events were observed in samples."})
    if not policy.get("redaction_tested"):
        findings.append({"severity": "medium", "issue": "Redaction rules have no recorded test evidence."})
    if policy.get("raw_payload_retention_days", 0) > policy.get("max_raw_payload_retention_days", 0):
        findings.append({"severity": "medium", "issue": "Raw payload retention exceeds the configured maximum."})
    return findings
