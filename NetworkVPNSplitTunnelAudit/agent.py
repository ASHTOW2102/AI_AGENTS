"""Flags VPN configurations using split tunneling that route sensitive corporate traffic outside the tunnel."""
from typing import Any


def audit(vpn: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if vpn.get("split_tunnel_enabled") and vpn.get("corporate_traffic_excluded_from_tunnel"):
        findings.append({"severity": "high", "issue": "Split tunnel excludes corporate traffic from the encrypted tunnel."})
    if vpn.get("split_tunnel_enabled") and not vpn.get("dns_leak_protection_enabled"):
        findings.append({"severity": "medium", "issue": "Split tunnel is enabled without DNS leak protection."})
    return findings
