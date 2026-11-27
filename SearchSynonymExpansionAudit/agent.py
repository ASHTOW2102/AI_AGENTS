"""Flags search synonym lists that have gone stale past their own configured maximum review interval, letting query expansion drift from current product terminology."""
from typing import Any


def audit(search: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    last_updated = search.get("synonym_list_last_updated_days_ago", 0)
    max_staleness = search.get("max_staleness_days", 0)
    if max_staleness and last_updated > max_staleness:
        findings.append({"severity": "low", "issue": f"Synonym list was last updated {last_updated} days ago, past the {max_staleness}-day review interval."})
    return findings
