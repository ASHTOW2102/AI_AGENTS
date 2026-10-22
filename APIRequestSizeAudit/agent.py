"""Review API request size and upload limits against operational policies."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("max_body_bytes", 0) <= 0:
        findings.append({"severity": "high", "issue": "Endpoint has no positive request-body size limit."})
    if endpoint.get("max_body_bytes", 0) > endpoint.get("approved_max_body_bytes", 0):
        findings.append({"severity": "medium", "issue": "Request-body limit exceeds the approved maximum."})
    if endpoint.get("streaming_upload") and not endpoint.get("total_size_enforced"):
        findings.append({"severity": "high", "issue": "Streaming uploads do not enforce a total size bound."})
    if endpoint.get("decompression_enabled") and not endpoint.get("decompressed_size_limit"):
        findings.append({"severity": "high", "issue": "Decompressed payloads have no size limit."})
    return findings
