"""Flags critical services that have never had fault injection testing performed against their mesh dependencies."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if service.get("criticality") == "high" and not service.get("fault_injection_tested"):
        findings.append({"severity": "high", "issue": "Critical service has never undergone fault injection testing."})
    if service.get("fault_injection_tested") and service.get("days_since_last_test", 0) > service.get("max_acceptable_test_interval_days", 180):
        findings.append({"severity": "medium", "issue": "Fault injection test is overdue for this service."})
    return findings
