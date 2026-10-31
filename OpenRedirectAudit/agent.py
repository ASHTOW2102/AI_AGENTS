"""Review redirect handling for allowlist and scheme validation controls."""
from typing import Any


def audit(policy: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if policy.get("user_controlled_redirect") and not policy.get("destination_allowlist"):
        findings.append({"severity": "high", "issue": "User-controlled redirect has no destination allowlist."})
    if not policy.get("https_only"):
        findings.append({"severity": "medium", "issue": "Redirect policy does not require HTTPS destinations."})
    if policy.get("relative_redirects_only") is False and not policy.get("absolute_destination_validated"):
        findings.append({"severity": "high", "issue": "Absolute redirect destinations are not validated."})
    if policy.get("redirect_chain_max", 0) > policy.get("approved_redirect_chain_max", 5):
        findings.append({"severity": "low", "issue": "Redirect chain limit exceeds policy."})
    return findings
