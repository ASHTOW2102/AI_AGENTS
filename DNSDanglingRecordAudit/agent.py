"""Flags DNS records still pointing at a deprovisioned resource, a classic subdomain-takeover precondition."""
from typing import Any


def audit(dns_record: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if dns_record.get("points_to_deprovisioned_resource"):
        findings.append({"severity": "high", "issue": "DNS record points to a deprovisioned resource, enabling subdomain takeover."})
    return findings
