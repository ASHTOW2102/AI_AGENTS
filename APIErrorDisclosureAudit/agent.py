"""Check API error response metadata for sensitive detail disclosure."""
from typing import Any


def audit(response: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if response.get("production") and response.get("stack_trace_in_body"):
        findings.append({"severity": "high", "issue": "Production error response includes a stack trace."})
    if response.get("database_error_details_exposed"):
        findings.append({"severity": "high", "issue": "Database or internal query details are exposed to clients."})
    if response.get("request_id_enabled") and not response.get("request_id_in_error"):
        findings.append({"severity": "low", "issue": "Error response omits the request ID needed for support correlation."})
    if response.get("error_contains_personal_data"):
        findings.append({"severity": "critical", "issue": "Error response may expose personal data."})
    return findings
