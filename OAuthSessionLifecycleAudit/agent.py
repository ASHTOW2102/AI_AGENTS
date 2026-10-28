"""Review OAuth session and token lifecycle configuration."""
from typing import Any


def audit(client: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if client.get("refresh_token_enabled") and not client.get("refresh_token_rotation"):
        findings.append({"severity": "high", "issue": "Refresh tokens are long-lived without rotation."})
    if client.get("refresh_token_rotation") and not client.get("reuse_detection"):
        findings.append({"severity": "high", "issue": "Rotated refresh-token reuse is not detected."})
    if client.get("logout_supported") and not client.get("server_side_revocation"):
        findings.append({"severity": "medium", "issue": "Logout does not revoke server-side session credentials."})
    if client.get("access_token_ttl_minutes", 0) > client.get("max_access_token_ttl_minutes", 60):
        findings.append({"severity": "medium", "issue": "Access-token lifetime exceeds policy."})
    return findings
