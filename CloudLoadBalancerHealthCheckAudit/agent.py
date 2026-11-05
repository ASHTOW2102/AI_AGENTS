"""Checks load-balancer health-check configuration for backend-draining and false-positive risk."""
from typing import Any


def audit(lb: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if lb.get("health_check_path") in (None, "/"):
        findings.append({"severity": "medium", "issue": "Health check uses a generic path rather than a dedicated endpoint."})
    if lb.get("health_check_checks_downstream_dependency"):
        findings.append({"severity": "high", "issue": "Health check fails the backend when an unrelated downstream dependency is unhealthy."})
    if lb.get("unhealthy_threshold", 0) <= 1:
        findings.append({"severity": "medium", "issue": "A single failed check can mark a healthy backend as unhealthy."})
    if not lb.get("connection_draining_enabled"):
        findings.append({"severity": "medium", "issue": "Backends are removed without draining in-flight connections."})
    return findings
