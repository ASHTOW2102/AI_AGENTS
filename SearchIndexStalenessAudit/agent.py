"""Flags search indexes with no freshness SLA or staleness monitoring, allowing the index to silently drift out of sync with the source of truth after an indexing pipeline failure."""
from typing import Any


def audit(index: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    monitors_staleness = index.get("monitors_index_staleness", False)
    freshness_sla_s = index.get("freshness_sla_seconds")

    if not monitors_staleness:
        findings.append({"severity": "medium", "issue": "Search index has no staleness monitoring, so a silent indexing pipeline failure could leave the index out of sync with the source of truth indefinitely."})
    if not freshness_sla_s:
        findings.append({"severity": "low", "issue": "No freshness SLA is defined for this index, so there's no agreed threshold at which staleness becomes an incident."})
    return findings
