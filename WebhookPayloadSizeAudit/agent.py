"""Checks outbound webhook payload sizes against receiver limits and truncation safety."""
from typing import Any


def audit(webhook: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if webhook.get("max_payload_bytes", 0) > webhook.get("known_receiver_limit_bytes", 0) and webhook.get("known_receiver_limit_bytes"):
        findings.append({"severity": "high", "issue": "Webhook payloads can exceed the receiver's documented size limit."})
    if webhook.get("payload_grows_with_data_volume") and not webhook.get("pagination_or_reference_pattern"):
        findings.append({"severity": "medium", "issue": "Payload size scales with data volume with no pagination or reference pattern."})
    if webhook.get("oversized_payload_behavior") == "silent_drop":
        findings.append({"severity": "high", "issue": "Oversized payloads are silently dropped rather than erroring."})
    return findings
