"""Flags read replicas with no replication-lag monitoring or alert threshold, allowing stale reads to silently serve outdated data after a lag spike."""
from typing import Any


def audit(replica: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    monitors_lag = replica.get("monitors_replication_lag", False)
    alert_threshold_s = replica.get("alert_threshold_seconds")

    if not monitors_lag:
        findings.append({"severity": "high", "issue": "Read replica has no replication-lag monitoring, so a lag spike causing stale reads would go undetected."})
    elif not alert_threshold_s:
        findings.append({"severity": "medium", "issue": "Replication lag is monitored but has no alert threshold configured, so a spike would be visible only on manual inspection."})
    return findings
