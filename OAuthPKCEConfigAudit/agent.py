"""Review OAuth public-client configuration for PKCE and redirect safety."""
from typing import Any


def audit(client: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if client.get("public_client") and not client.get("pkce_required"):
        findings.append({"severity": "high", "issue": "Public OAuth client does not require PKCE."})
    if client.get("pkce_required") and client.get("pkce_method") != "S256":
        findings.append({"severity": "high", "issue": "PKCE does not use the S256 challenge method."})
    if not client.get("redirect_uri_exact_match"):
        findings.append({"severity": "high", "issue": "Redirect URI matching is not exact."})
    if client.get("implicit_flow_enabled"):
        findings.append({"severity": "medium", "issue": "Legacy implicit flow remains enabled."})
    return findings
