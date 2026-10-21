"""Review service-account permissions for excessive privilege and stale use."""
from typing import Any


def audit(account: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    broad = sorted(set(account.get("granted_permissions", [])) - set(account.get("required_permissions", [])))
    if broad:
        findings.append({"severity": "high", "issue": "Unneeded permissions: " + ", ".join(broad)})
    if account.get("wildcard_permission"):
        findings.append({"severity": "critical", "issue": "Wildcard permission grants broad service-account access."})
    if not account.get("workload_identity") and account.get("long_lived_secret"):
        findings.append({"severity": "high", "issue": "Long-lived account secret is used instead of workload identity."})
    if account.get("days_since_last_use", 0) > account.get("max_idle_days", 90):
        findings.append({"severity": "medium", "issue": "Service account has exceeded its allowed idle period."})
    return findings
