"""Flags search autocomplete endpoints that reflect unsanitized user input into suggestion responses."""
from typing import Any


def audit(endpoint: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if endpoint.get("reflects_raw_input") and not endpoint.get("output_encoding_applied"):
        findings.append({"severity": "high", "issue": "Autocomplete reflects raw input without output encoding."})
    if not endpoint.get("input_length_capped"):
        findings.append({"severity": "low", "issue": "Autocomplete query input has no length cap."})
    return findings
