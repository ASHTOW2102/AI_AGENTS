"""Checks authoritative DNS servers for unrestricted zone transfer exposure."""
from typing import Any


def audit(dns: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if dns.get("zone_transfer_allowed_from_any"):
        findings.append({"severity": "high", "issue": "Zone transfer is allowed from any host."})
    if not dns.get("tsig_signing_enabled"):
        findings.append({"severity": "medium", "issue": "Zone transfers are not authenticated with TSIG signing."})
    return findings
