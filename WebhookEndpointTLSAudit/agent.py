"""Checks outbound webhook destinations for TLS enforcement and certificate validation."""
from typing import Any


def audit(webhook: dict[str, Any]):
    findings = []
    if not webhook.get("https_only"):
        findings.append({"severity": "high", "issue": "Webhook endpoint accepts plain HTTP."})
    if webhook.get("https_only") and webhook.get("certificate_validation_disabled"):
        findings.append({"severity": "critical", "issue": "Webhook delivery disables certificate validation."})
    if webhook.get("redirect_followed") and not webhook.get("redirect_target_validated"):
        findings.append({"severity": "medium", "issue": "Webhook follows redirects without validating the target."})
    return findings
