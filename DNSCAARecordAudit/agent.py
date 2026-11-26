"""Flags domains that issue certificates but have no CAA record restricting which certificate authorities may issue for them."""
from typing import Any


def audit(domain: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if domain.get("issues_certificates") and not domain.get("has_caa_record"):
        findings.append({"severity": "medium", "issue": "Domain has no CAA record restricting authorized certificate authorities."})
    return findings
