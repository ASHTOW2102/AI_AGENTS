"""Flags outbound webhook deliveries that are not signed, letting receivers be spoofed by forged payloads."""
from typing import Any


def audit(webhook: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not webhook.get("payload_signed"):
        findings.append({"severity": "high", "issue": "Webhook payload is not signed, allowing receiver spoofing."})
    if webhook.get("payload_signed") and webhook.get("signature_algorithm") in ("md5", "sha1"):
        findings.append({"severity": "medium", "issue": "Webhook signature uses a weak hashing algorithm."})
    return findings
