"""Flags search indexes that include PII fields among their indexed and therefore searchable/returnable fields."""
from typing import Any


def audit(index: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    indexed = index.get("indexed_fields", [])
    leaked = [f for f in index.get("pii_fields", []) if f in indexed]
    if leaked:
        findings.append({"severity": "high", "issue": f"PII fields are indexed and searchable: {leaked}"})
    return findings
