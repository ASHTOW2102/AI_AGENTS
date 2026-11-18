"""Flags data shared with external parties that lacks a signed data processing agreement or an expiry date."""
from typing import Any


def audit(share: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if share.get("shared_externally") and not share.get("dpa_signed"):
        findings.append({"severity": "high", "issue": "Data is shared externally with no signed data processing agreement."})
    if share.get("shared_externally") and not share.get("access_expiry_date"):
        findings.append({"severity": "medium", "issue": "External data share has no access expiry date."})
    return findings
