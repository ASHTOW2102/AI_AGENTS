"""Flags load balancer backend pools with health checks too shallow (e.g. a bare TCP connect) to detect an application that is listening but unable to serve requests correctly."""
from typing import Any


def audit(lb: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    check_type = lb.get("health_check_type", "tcp")
    checks_dependencies = lb.get("health_check_verifies_dependencies", False)

    if check_type == "tcp":
        findings.append({"severity": "medium", "issue": "Health check is a bare TCP connect, which passes even when the application is listening but unable to serve requests correctly (e.g. deadlocked or out of DB connections)."})
    if not checks_dependencies:
        findings.append({"severity": "low", "issue": "Health check does not verify critical downstream dependencies (database, cache), so backend-dependency outages aren't reflected in routing decisions."})
    return findings
