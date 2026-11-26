"""Flags search layers that build their query DSL via raw string concatenation of user input instead of a parameterized query builder."""
from typing import Any


def audit(search: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if search.get("builds_query_from_raw_string_concat"):
        findings.append({"severity": "high", "issue": "Search query is built via raw string concatenation of user input."})
    return findings
