"""Flags secrets retaining far more old versions than their own configured maximum, needlessly widening the window in which a leaked old version stays valid-looking."""
from typing import Any


def audit(secret: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    old_versions = secret.get("old_version_count", 0)
    max_retained = secret.get("max_retained_versions", 0)
    if max_retained and old_versions > max_retained:
        findings.append({"severity": "low", "issue": f"Secret retains {old_versions} old versions, above the configured maximum of {max_retained}."})
    return findings
