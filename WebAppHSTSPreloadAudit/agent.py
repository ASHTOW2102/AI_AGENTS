"""Flags sites with no HSTS header, or whose HSTS max-age is shorter than a year, weakening protection against TLS-stripping downgrade attacks."""
from typing import Any


def audit(site: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not site.get("hsts_enabled"):
        findings.append({"severity": "high", "issue": "Site has no HSTS header."})
    elif site.get("hsts_max_age_seconds", 0) < 31536000:
        findings.append({"severity": "medium", "issue": "HSTS max-age is shorter than one year."})
    return findings
