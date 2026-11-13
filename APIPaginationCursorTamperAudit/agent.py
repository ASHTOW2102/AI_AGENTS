"""Flags paginated API endpoints whose cursor tokens are not signed, allowing clients to tamper with pagination state."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("cursor_format") == "plain" and not endpoint.get("cursor_signed"):
        findings.append({"severity": "medium", "issue": "Pagination cursor is plain and unsigned, allowing tampering."})
    if endpoint.get("cursor_encodes_internal_ids") and not endpoint.get("cursor_signed"):
        findings.append({"severity": "high", "issue": "Cursor encodes internal identifiers without a signature to prevent tampering."})
    return findings
