"""Checks request-ID propagation across service hops for end-to-end trace correlation."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not service.get("accepts_incoming_request_id"):
        findings.append({"severity": "medium", "issue": "Service does not accept an incoming request-ID header."})
    if service.get("calls_downstream") and not service.get("propagates_request_id_downstream"):
        findings.append({"severity": "high", "issue": "Service does not propagate the request ID to downstream calls."})
    if not service.get("request_id_in_logs"):
        findings.append({"severity": "medium", "issue": "Request ID is not included in service logs."})
    return findings
