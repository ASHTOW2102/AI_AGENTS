"""Checks cookie/tracking consent banner behavior for default state and category granularity."""
from typing import Any


def audit(banner: dict[str, Any]):
    findings = []
    if banner.get("non_essential_cookies_set_before_consent"):
        findings.append({"severity": "high", "issue": "Non-essential cookies are set before consent is given."})
    if banner.get("default_state") == "all_accepted":
        findings.append({"severity": "high", "issue": "Consent banner defaults to all categories accepted."})
    if not banner.get("reject_all_option"):
        findings.append({"severity": "medium", "issue": "Banner has no reject-all option."})
    if not banner.get("category_level_choice"):
        findings.append({"severity": "medium", "issue": "Banner does not offer category-level consent choices."})
    return findings
