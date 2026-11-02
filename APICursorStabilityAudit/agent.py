"""Checks cursor-based pagination for stability under concurrent inserts and deletes."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("cursor_based") and endpoint.get("cursor_field") in (None, "offset"):
        findings.append({"severity": "high", "issue": "Cursor pagination is based on a mutable offset rather than a stable key."})
    if endpoint.get("cursor_based") and not endpoint.get("cursor_tie_breaker"):
        findings.append({"severity": "medium", "issue": "Cursor has no tie-breaker for duplicate sort values."})
    if endpoint.get("deletions_during_pagination_possible") and not endpoint.get("stable_under_deletion"):
        findings.append({"severity": "medium", "issue": "Pagination is not verified stable when rows are deleted mid-traversal."})
    return findings
