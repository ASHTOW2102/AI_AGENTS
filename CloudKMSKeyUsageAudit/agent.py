"""Flags cloud KMS keys whose decrypt permission is granted to any principal rather than a scoped allowlist."""
from typing import Any


def audit(kms_key: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if kms_key.get("allows_decrypt_from_any_principal"):
        findings.append({"severity": "high", "issue": "KMS key grants decrypt permission to any principal."})
    return findings
