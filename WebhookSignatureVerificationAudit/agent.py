"""Flags webhook receivers that process inbound payloads without verifying an HMAC signature header, allowing forged webhook events to be accepted as genuine."""
from typing import Any


def audit(webhook: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    verifies_signature = webhook.get("verifies_hmac_signature", False)
    uses_constant_time = webhook.get("uses_constant_time_compare", False)

    if not verifies_signature:
        findings.append({"severity": "high", "issue": "Webhook receiver does not verify an HMAC signature header, allowing forged events from any source that knows the endpoint URL."})
    elif not uses_constant_time:
        findings.append({"severity": "medium", "issue": "Signature comparison is not constant-time, creating a timing side channel that could help an attacker forge a valid signature."})

    if webhook.get("accepts_replay_without_timestamp_check"):
        findings.append({"severity": "medium", "issue": "Webhook accepts payloads without checking a timestamp or nonce, making it vulnerable to replay of previously captured valid requests."})
    return findings
