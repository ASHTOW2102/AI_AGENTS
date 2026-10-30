"""Review data-retention exceptions for ownership, scope, and expiry."""
from typing import Any


def audit(exception: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not exception.get("exception_reference"):
        findings.append({"severity": "medium", "issue": "Retention exception has no approval reference."})
    if not exception.get("owner"):
        findings.append({"severity": "medium", "issue": "Retention exception has no accountable owner."})
    if not exception.get("expires_on"):
        findings.append({"severity": "high", "issue": "Retention exception has no expiry date."})
    if exception.get("data_classes") and not exception.get("scope_minimized"):
        findings.append({"severity": "low", "issue": "Exception data scope has not been minimized."})
    return findings
