"""Checks load-test coverage and recency against peak-traffic planning targets."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if service.get("days_since_last_load_test", 0) > service.get("max_days_between_tests", 180):
        findings.append({"severity": "medium", "issue": "Load test has not been run within the required interval."})
    if service.get("last_test_peak_rps", 0) < service.get("projected_peak_rps", 0):
        findings.append({"severity": "high", "issue": "Last load test did not reach the projected peak traffic."})
    if service.get("test_included_dependencies") is False:
        findings.append({"severity": "medium", "issue": "Load test did not include downstream dependencies."})
    return findings
