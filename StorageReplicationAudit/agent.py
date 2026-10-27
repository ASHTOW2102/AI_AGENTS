"""Review object storage replication coverage and replication health evidence."""
from typing import Any


def audit(bucket: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if bucket.get("replication_required") and not bucket.get("replication_enabled"):
        findings.append({"severity": "high", "issue": "Required cross-region replication is disabled."})
    if bucket.get("replication_enabled") and not bucket.get("replication_status_monitored"):
        findings.append({"severity": "medium", "issue": "Replication status is not monitored."})
    if bucket.get("replication_lag_minutes", 0) > bucket.get("max_replication_lag_minutes", 0):
        findings.append({"severity": "high", "issue": "Storage replication lag exceeds its objective."})
    if bucket.get("delete_marker_replication_required") and not bucket.get("delete_marker_replication_enabled"):
        findings.append({"severity": "medium", "issue": "Delete-marker replication does not match the required policy."})
    return findings
