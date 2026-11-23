"""Flags list endpoints that do not enforce a maximum page size, or whose enforced maximum is large enough to still enable resource-exhaustion scraping."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not endpoint.get("enforces_max_page_size"):
        findings.append({"severity": "high", "issue": "Endpoint does not enforce a maximum page size on list results."})
    else:
        max_size = endpoint.get("max_page_size", 0)
        if max_size and max_size > 1000:
            findings.append({"severity": "low", "issue": f"Enforced max page size ({max_size}) is large enough to enable resource-exhaustion scraping."})
    return findings
