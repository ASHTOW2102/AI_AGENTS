"""Review host time-synchronization configuration and observed drift."""
from typing import Any


def audit(host: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not host.get("time_sync_enabled"):
        findings.append({"severity": "high", "issue": "Time synchronization is disabled."})
    if host.get("configured_sources", 0) < 2:
        findings.append({"severity": "medium", "issue": "Fewer than two time sources are configured."})
    if abs(host.get("observed_drift_ms", 0)) > host.get("max_drift_ms", 1000):
        findings.append({"severity": "high", "issue": "Observed clock drift exceeds the allowed maximum."})
    if host.get("last_sync_age_hours", 0) > host.get("max_sync_age_hours", 24):
        findings.append({"severity": "medium", "issue": "Last successful synchronization is too old."})
    return findings
