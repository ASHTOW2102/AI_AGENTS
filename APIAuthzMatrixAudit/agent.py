"""Compare API route authorization requirements with implemented policies."""
from typing import Any


def audit(routes: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    for route in routes.get("routes", []):
        name = route.get("name", "<unnamed>")
        if route.get("authenticated_required") and not route.get("auth_middleware"):
            findings.append({"severity": "high", "issue": f"{name} requires authentication but has no auth middleware."})
        if route.get("sensitive_operation") and not route.get("authorization_policy"):
            findings.append({"severity": "high", "issue": f"{name} has no operation-level authorization policy."})
        if route.get("public_exception") and not route.get("exception_approved"):
            findings.append({"severity": "medium", "issue": f"{name} is public without an approved exception."})
    return findings
