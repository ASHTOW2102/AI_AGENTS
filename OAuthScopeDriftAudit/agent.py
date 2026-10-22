"""Compare OAuth grants to approved scopes and consent requirements."""
from typing import Any


def audit(client: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    extra = sorted(set(client.get("granted_scopes", [])) - set(client.get("approved_scopes", [])))
    if extra:
        findings.append({"severity": "high", "issue": "Unapproved granted scopes: " + ", ".join(extra)})
    if client.get("sensitive_scopes") and not client.get("explicit_consent_required"):
        findings.append({"severity": "high", "issue": "Sensitive scopes do not require explicit consent."})
    if client.get("offline_access") and not client.get("refresh_token_rotation"):
        findings.append({"severity": "medium", "issue": "Offline access is enabled without refresh-token rotation."})
    if not client.get("redirect_uri_exact_match"):
        findings.append({"severity": "high", "issue": "Redirect URI validation does not require an exact match."})
    return findings
