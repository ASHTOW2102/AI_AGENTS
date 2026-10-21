"""Assess webhook delivery reliability, retry safety, and observability."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("retry_max_attempts", 0) < 1:
        findings.append({"severity": "high", "issue": "Webhook has no delivery retry attempts."})
    if endpoint.get("retry_max_attempts", 0) > 0 and endpoint.get("retry_backoff_seconds", 0) <= 0:
        findings.append({"severity": "medium", "issue": "Retries have no positive backoff."})
    if not endpoint.get("signature_verification"):
        findings.append({"severity": "high", "issue": "Incoming webhook signatures are not verified."})
    if not endpoint.get("idempotency_handling"):
        findings.append({"severity": "medium", "issue": "Duplicate webhook deliveries are not handled idempotently."})
    if endpoint.get("failure_alert_threshold") is None:
        findings.append({"severity": "low", "issue": "No delivery-failure alert threshold is defined."})
    return findings
