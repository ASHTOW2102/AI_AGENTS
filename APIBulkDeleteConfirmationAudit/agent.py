"""Flags bulk-delete endpoints with no confirmation token requirement, so a single mistaken or spoofed request can destroy many records at once."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("supports_bulk_delete") and not endpoint.get("requires_confirmation_token"):
        findings.append({"severity": "high", "issue": "Bulk-delete endpoint requires no confirmation token before destroying records."})
    return findings
