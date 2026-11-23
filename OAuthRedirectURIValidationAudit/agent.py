"""Flags OAuth clients whose redirect URI validation is wildcard or absent, enabling authorization-code theft via an attacker-controlled redirect."""
from typing import Any


def audit(oauth_client: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if oauth_client.get("redirect_uri_validation") in ("wildcard", "none"):
        findings.append({"severity": "high", "issue": f"OAuth client redirect URI validation is '{oauth_client.get('redirect_uri_validation')}', not an exact match."})
    return findings
