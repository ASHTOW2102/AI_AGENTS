"""Flags CDN-fronted origins that remain publicly reachable directly, letting attackers bypass the CDN's WAF and caching entirely."""
from typing import Any


def audit(cdn: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if cdn.get("origin_publicly_accessible") and not cdn.get("origin_restricted_to_cdn_ips"):
        findings.append({"severity": "high", "issue": "Origin server is directly reachable, bypassing the CDN's WAF and caching."})
    return findings
