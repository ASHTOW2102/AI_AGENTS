"""Flags search engines with fuzzy/typo-tolerant matching enabled that can be abused to enumerate near-matches of sensitive restricted terms."""
from typing import Any


def audit(search: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if search.get("fuzzy_matching_enabled") and search.get("indexes_restricted_terms") and not search.get("fuzzy_matching_excludes_restricted_terms"):
        findings.append({"severity": "medium", "issue": "Fuzzy matching can surface near-matches of restricted terms that should be excluded."})
    if search.get("fuzzy_matching_enabled") and not search.get("query_rate_limited"):
        findings.append({"severity": "low", "issue": "Fuzzy search has no rate limiting, enabling enumeration via repeated near-miss queries."})
    return findings
