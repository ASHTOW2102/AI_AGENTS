"""Review OIDC authorization-flow state and nonce validation settings."""
from typing import Any


def audit(client: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if client.get("authorization_code_flow") and not client.get("state_generated_and_validated"):
        findings.append({"severity": "high", "issue": "OAuth state is not generated and validated."})
    if client.get("openid_connect") and not client.get("nonce_validated"):
        findings.append({"severity": "high", "issue": "OIDC nonce is not validated against the authorization response."})
    if not client.get("state_bound_to_user_agent_session"):
        findings.append({"severity": "medium", "issue": "State value is not bound to the initiating user session."})
    if client.get("pkce_used") and client.get("pkce_verifier_reused"):
        findings.append({"severity": "high", "issue": "PKCE verifier may be reused across authorization attempts."})
    return findings
