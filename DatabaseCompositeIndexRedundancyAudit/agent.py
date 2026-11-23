"""Flags database tables where one composite index is a strict column prefix of another, making the shorter index redundant dead weight on every write."""
from typing import Any


def audit(table: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    indexes = table.get("indexes", [])
    redundant = []
    for i, shorter in enumerate(indexes):
        for j, longer in enumerate(indexes):
            if i != j and len(shorter) < len(longer) and longer[: len(shorter)] == shorter:
                redundant.append(shorter)
                break
    if redundant:
        findings.append({"severity": "low", "issue": f"Indexes {redundant} are redundant prefixes of longer indexes on the same table."})
    return findings
