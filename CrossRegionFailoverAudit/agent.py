"""Flags multi-region services with no tested, automated failover procedure, relying instead on manual intervention during a regional outage."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    has_automated_failover = service.get("has_automated_failover", False)
    last_failover_test_days_ago = service.get("last_failover_test_days_ago")

    if not has_automated_failover:
        findings.append({"severity": "high", "issue": "Multi-region service has no automated failover, relying on manual intervention during a regional outage, which extends downtime."})
    if last_failover_test_days_ago is None or last_failover_test_days_ago > 180:
        findings.append({"severity": "medium", "issue": "Failover procedure has not been tested in over 180 days (or ever), so it may not work as expected when actually needed."})
    return findings
