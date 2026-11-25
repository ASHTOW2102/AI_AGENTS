"""Flags DNS zones with a wildcard record whose target has not been verified, letting an attacker claim an unclaimed subdomain target and hijack arbitrary subdomains."""
from typing import Any


def audit(dns_zone: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if dns_zone.get("has_wildcard_record") and not dns_zone.get("wildcard_target_verified"):
        findings.append({"severity": "high", "issue": "Wildcard DNS record points to an unverified target, risking subdomain hijack."})
    return findings
