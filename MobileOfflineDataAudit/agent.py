"""Review mobile offline-storage controls for expiry and synchronization safety."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if app.get("sensitive_data_cached_offline") and not app.get("offline_cache_encrypted"):
        findings.append({"severity": "high", "issue": "Sensitive offline cache is not encrypted."})
    if app.get("offline_cache_max_age_hours", 0) > app.get("approved_offline_cache_max_age_hours", 0):
        findings.append({"severity": "medium", "issue": "Offline cache lifetime exceeds policy."})
    if app.get("offline_mutations_enabled") and not app.get("conflict_resolution_defined"):
        findings.append({"severity": "medium", "issue": "Offline writes have no conflict-resolution policy."})
    if app.get("logout_clears_local_data") is False and app.get("shared_device_risk"):
        findings.append({"severity": "high", "issue": "Logout leaves cached data on a shared-risk device."})
    return findings
