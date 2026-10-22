"""Check localization delivery coverage and fallback risks by locale."""
from typing import Any


def audit(locale: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    total = locale.get("required_strings", 0)
    translated = locale.get("translated_strings", 0)
    if translated < total:
        findings.append({"severity": "medium", "issue": f"{total - translated} required strings are untranslated."})
    if locale.get("fallback_rate_percent", 0) > locale.get("max_fallback_rate_percent", 5):
        findings.append({"severity": "low", "issue": "Runtime locale fallback rate exceeds the configured maximum."})
    if locale.get("missing_critical_strings", 0) > 0:
        findings.append({"severity": "high", "issue": "One or more critical strings are missing."})
    if locale.get("stale_translation_days", 0) > locale.get("max_translation_age_days", 365):
        findings.append({"severity": "low", "issue": "Locale translation review is stale."})
    return findings
