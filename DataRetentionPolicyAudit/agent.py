"""Flags datasets containing PII with no defined retention policy, risking indefinite storage of personal data past its lawful purpose."""
from typing import Any


def audit(dataset: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if dataset.get("contains_pii") and not dataset.get("retention_policy_defined"):
        findings.append({"severity": "high", "issue": "Dataset contains PII but has no defined retention policy."})
    return findings
