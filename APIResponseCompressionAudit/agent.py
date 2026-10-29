"""Review API response compression policy for compatibility and resource bounds."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("compression_enabled") and not endpoint.get("minimum_size_threshold_bytes"):
        findings.append({"severity": "low", "issue": "Compression has no minimum-size threshold."})
    if endpoint.get("compression_enabled") and not endpoint.get("content_type_allowlist"):
        findings.append({"severity": "medium", "issue": "Compression has no content-type allowlist."})
    if endpoint.get("compress_secrets_with_reflected_input"):
        findings.append({"severity": "high", "issue": "Compression combines secrets with reflected attacker-controlled input."})
    if endpoint.get("max_uncompressed_response_bytes", 0) > endpoint.get("approved_max_response_bytes", 0):
        findings.append({"severity": "medium", "issue": "Response size limit exceeds the approved maximum."})
    return findings
