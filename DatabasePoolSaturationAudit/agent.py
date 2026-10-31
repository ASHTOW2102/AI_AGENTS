"""Review database connection-pool saturation and queueing signals."""
from typing import Any


def audit(pool: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pool.get("utilization_percent", 0) >= pool.get("max_utilization_percent", 85):
        findings.append({"severity": "high", "issue": "Connection pool utilization is at or above its threshold."})
    if pool.get("waiting_requests", 0) > 0 and not pool.get("wait_alert_configured"):
        findings.append({"severity": "medium", "issue": "Requests are waiting for connections without an alert."})
    if pool.get("pool_max", 0) > pool.get("database_connection_budget", 0):
        findings.append({"severity": "high", "issue": "Pool maximum exceeds the database connection budget."})
    if pool.get("connection_leak_detection") is False:
        findings.append({"severity": "low", "issue": "Connection leak detection is disabled."})
    return findings
