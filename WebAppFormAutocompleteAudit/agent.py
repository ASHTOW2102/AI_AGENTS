"""Flags web forms that allow browser autocomplete on fields holding sensitive data like payment or SSN."""
from typing import Any


def audit(form: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    sensitive_without_off = [f for f in form.get("sensitive_fields", []) if f not in form.get("autocomplete_off_fields", [])]
    if sensitive_without_off:
        findings.append({"severity": "medium", "issue": f"Sensitive fields allow autocomplete: {sensitive_without_off}"})
    if form.get("is_shared_device_context") and sensitive_without_off:
        findings.append({"severity": "high", "issue": "Shared-device form allows autocomplete on sensitive fields."})
    return findings
