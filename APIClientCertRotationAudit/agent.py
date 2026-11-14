"""Flags mutual-TLS API clients whose certificates are approaching expiry without an automated renewal process."""
from typing import Any


def audit(client: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if client.get("days_until_cert_expiry", 999) < client.get("renewal_warning_days", 14) and not client.get("auto_renewal_enabled"):
        findings.append({"severity": "high", "issue": "Client certificate is nearing expiry with no automated renewal."})
    if not client.get("cert_expiry_monitored"):
        findings.append({"severity": "medium", "issue": "Client certificate expiry is not monitored."})
    return findings
