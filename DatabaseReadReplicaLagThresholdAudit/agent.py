"""Flags read replicas whose current replication lag exceeds the application's own configured maximum acceptable staleness."""
from typing import Any


def audit(replica: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    current_lag = replica.get("current_lag_seconds", 0)
    max_acceptable = replica.get("max_acceptable_lag_seconds", 0)
    if max_acceptable and current_lag > max_acceptable:
        findings.append({"severity": "high", "issue": f"Replica lag ({current_lag}s) exceeds the max acceptable staleness ({max_acceptable}s)."})
    return findings
