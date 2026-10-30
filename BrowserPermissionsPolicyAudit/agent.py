"""Review browser Permissions-Policy grants for unnecessary capabilities."""
from typing import Any


def audit(policy: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    enabled = set(policy.get("enabled_features", []))
    approved = set(policy.get("approved_features", []))
    extra = sorted(enabled - approved)
    if extra:
        findings.append({"severity": "medium", "issue": "Unapproved browser features enabled: " + ", ".join(extra)})
    if "*" in policy.get("feature_allowlists", {}):
        findings.append({"severity": "high", "issue": "A Permissions-Policy feature allows all origins."})
    if policy.get("cross_origin_iframes") and not policy.get("iframe_feature_allowlist"):
        findings.append({"severity": "low", "issue": "Cross-origin iframe capabilities are not explicitly scoped."})
    return findings
