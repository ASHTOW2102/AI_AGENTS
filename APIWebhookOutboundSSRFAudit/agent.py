"""Flags outbound webhook configurations that allow delivering to internal/private IP destinations without validating the URL against an allowlist, a classic SSRF vector."""
from typing import Any


def audit(webhook_config: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if webhook_config.get("allows_internal_ip_destinations") and not webhook_config.get("validates_destination_url_against_allowlist"):
        findings.append({"severity": "high", "issue": "Outbound webhooks can target internal IPs with no destination allowlist validation."})
    return findings
