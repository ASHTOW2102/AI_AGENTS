"""Flags public OAuth clients (mobile/SPA, which cannot hold a secret) that do not enforce PKCE, leaving the authorization code flow open to interception."""
from typing import Any


def audit(client: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if client.get("client_type") == "public" and not client.get("enforces_pkce"):
        findings.append({"severity": "high", "issue": "Public OAuth client does not enforce PKCE."})
    return findings
