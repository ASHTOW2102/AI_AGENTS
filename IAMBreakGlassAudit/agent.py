"""Checks emergency break-glass access accounts for monitoring, expiry, and usage review."""
from typing import Any


def audit(account: dict[str, Any]):
    findings = []
    if not account.get("usage_alerting_enabled"):
        findings.append({"severity": "high", "issue": "Break-glass account has no usage alerting."})
    if not account.get("credential_expiry_enforced"):
        findings.append({"severity": "medium", "issue": "Break-glass credentials do not expire."})
    if account.get("used_in_last_90_days") and not account.get("usage_reviewed"):
        findings.append({"severity": "high", "issue": "Recent break-glass usage has not been reviewed."})
    return findings
