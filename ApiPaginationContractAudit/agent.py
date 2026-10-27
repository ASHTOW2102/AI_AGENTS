"""Check API pagination contracts for stable, bounded traversal."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not endpoint.get("pagination_supported"):
        findings.append({"severity": "medium", "issue": "Collection endpoint has no pagination contract."})
    if endpoint.get("pagination_supported") and not endpoint.get("max_page_size"):
        findings.append({"severity": "high", "issue": "Pagination has no maximum page-size bound."})
    if endpoint.get("mutable_collection") and not endpoint.get("cursor_pagination"):
        findings.append({"severity": "medium", "issue": "Mutable collection uses offset-only pagination."})
    if endpoint.get("has_next") and not endpoint.get("next_cursor") and endpoint.get("cursor_pagination"):
        findings.append({"severity": "low", "issue": "Response reports another page but no next cursor."})
    return findings
