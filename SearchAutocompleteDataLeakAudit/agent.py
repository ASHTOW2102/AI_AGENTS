"""Checks search autocomplete suggestions for leaking other users' private or sensitive data."""
from typing import Any


def audit(autocomplete: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if autocomplete.get("suggestions_derived_from_all_users_history") and not autocomplete.get("per_user_isolation"):
        findings.append({"severity": "critical", "issue": "Autocomplete suggests terms from other users' private history."})
    if autocomplete.get("suggestions_include_pii_patterns"):
        findings.append({"severity": "high", "issue": "Autocomplete surfaces suggestions matching PII patterns."})
    if autocomplete.get("admin_only_terms_suggested_to_regular_users"):
        findings.append({"severity": "high", "issue": "Privileged terms are suggested to users without the matching access."})
    return findings
