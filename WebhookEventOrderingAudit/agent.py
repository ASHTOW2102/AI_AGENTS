"""Checks webhook event delivery for ordering guarantees and out-of-order handling by consumers."""
from typing import Any


def audit(webhook: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if webhook.get("ordering_matters") and not webhook.get("sequence_number_included"):
        findings.append({"severity": "high", "issue": "Order-sensitive events carry no sequence number."})
    if webhook.get("sequence_number_included") and not webhook.get("consumer_reorders_on_receipt"):
        findings.append({"severity": "medium", "issue": "Consumer does not reorder events using the sequence number."})
    if webhook.get("retries_can_reorder_delivery") and webhook.get("ordering_matters"):
        findings.append({"severity": "high", "issue": "Retry delivery can reorder order-sensitive events."})
    return findings
