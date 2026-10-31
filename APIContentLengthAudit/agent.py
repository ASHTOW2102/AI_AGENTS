"""Review API request and response content-length bounds."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("max_request_bytes", 0) <= 0:
        findings.append({"severity": "high", "issue": "Endpoint has no positive request-size limit."})
    if endpoint.get("max_request_bytes", 0) > endpoint.get("approved_request_bytes", 0):
        findings.append({"severity": "medium", "issue": "Request-size limit exceeds the approved maximum."})
    if endpoint.get("streaming_request") and not endpoint.get("stream_total_limit"):
        findings.append({"severity": "high", "issue": "Streaming request has no total content-length bound."})
    if endpoint.get("max_response_bytes", 0) > endpoint.get("approved_response_bytes", 0):
        findings.append({"severity": "low", "issue": "Response-size limit exceeds the approved maximum."})
    return findings
