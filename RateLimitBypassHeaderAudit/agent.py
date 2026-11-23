"""Flags API gateways that trust client-supplied headers to determine rate-limit identity, letting an attacker bypass limits by spoofing the header."""
from typing import Any


def audit(api_gateway: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if api_gateway.get("trusts_client_supplied_rate_limit_headers"):
        findings.append({"severity": "high", "issue": "Gateway trusts client-supplied headers for rate-limit identity, allowing limit bypass via header spoofing."})
    return findings
