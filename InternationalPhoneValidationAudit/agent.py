"""Check international phone-number validation and normalization policies."""
from typing import Any


def audit(form: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not form.get("country_code_supported"):
        findings.append({"severity": "medium", "issue": "Phone input has no supported-country validation."})
    if not form.get("e164_normalization"):
        findings.append({"severity": "low", "issue": "Phone numbers are not normalized to a consistent international format."})
    if form.get("verification_required") and not form.get("verification_before_sensitive_action"):
        findings.append({"severity": "high", "issue": "Required phone verification is not enforced before sensitive actions."})
    if form.get("phone_as_account_identifier") and not form.get("number_change_recovery"):
        findings.append({"severity": "medium", "issue": "Phone-based accounts have no verified number-change recovery path."})
    return findings
