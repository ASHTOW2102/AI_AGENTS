"""Flags authoritative DNS servers that allow full zone transfers (AXFR) from arbitrary hosts, leaking the entire internal DNS zone."""
from typing import Any


def audit(dns_server: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if dns_server.get("allows_axfr_from_any"):
        findings.append({"severity": "high", "issue": "DNS server permits zone transfer (AXFR) from any host, leaking the full zone."})
    return findings
