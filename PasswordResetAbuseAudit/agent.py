"""Review password-reset flow rate limits and account-enumeration controls."""
from typing import Any


def audit(flow: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if flow.get("same_response_for_known_and_unknown_users") is False:
        findings.append({"severity": "medium", "issue": "Password reset responses can reveal whether an account exists."})
    if not flow.get("request_rate_limited"):
        findings.append({"severity": "high", "issue": "Password reset requests are not rate limited."})
    if not flow.get("token_single_use"):
        findings.append({"severity": "high", "issue": "Reset tokens can be reused."})
    if flow.get("token_ttl_minutes", 0) > flow.get("max_token_ttl_minutes", 60):
        findings.append({"severity": "medium", "issue": "Password reset token lifetime exceeds policy."})
    return findings
