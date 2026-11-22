"""Flags authoritative DNS servers that allow unrestricted zone transfer (AXFR) requests from arbitrary IP addresses, leaking the full internal DNS record set to anyone who asks."""
from typing import Any


def audit(dns_server: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    axfr_restricted = dns_server.get("axfr_restricted_to_secondaries", False)

    if not axfr_restricted:
        findings.append({"severity": "high", "issue": "Zone transfer (AXFR) is not restricted to known secondary name servers, allowing any client to pull the full DNS zone and enumerate internal hostnames."})
    if dns_server.get("exposes_internal_subdomains_in_zone") and not axfr_restricted:
        findings.append({"severity": "high", "issue": "Zone includes internal-only subdomains and is reachable via unrestricted zone transfer, directly leaking internal network topology."})
    return findings
