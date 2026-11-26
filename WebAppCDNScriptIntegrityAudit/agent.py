"""Flags pages that load third-party scripts without a Subresource Integrity hash, letting a compromised CDN inject arbitrary code."""
from typing import Any


def audit(page: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if page.get("loads_third_party_scripts") and not page.get("uses_subresource_integrity"):
        findings.append({"severity": "high", "issue": "Third-party scripts are loaded with no Subresource Integrity hash."})
    return findings
