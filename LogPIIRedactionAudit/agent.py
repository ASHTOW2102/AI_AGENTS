"""Flags logging pipelines that write request/response payloads without redacting personally identifiable information, leaking PII into log storage and any downstream log consumers."""
from typing import Any


def audit(logger: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    redacts_pii = logger.get("redacts_pii_fields", False)
    logs_full_payloads = logger.get("logs_full_request_response_bodies", False)

    if logs_full_payloads and not redacts_pii:
        findings.append({"severity": "high", "issue": "Logger writes full request/response bodies without PII redaction, leaking personal data into log storage and any downstream log consumers."})
    if not logger.get("has_log_retention_policy"):
        findings.append({"severity": "low", "issue": "No log retention policy is configured, so any leaked PII in logs persists indefinitely rather than being purged."})
    return findings
