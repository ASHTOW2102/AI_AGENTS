"""Check certificate inventory for expiry and renewal readiness."""
from datetime import date
from typing import Any


def audit(cert: dict[str, Any], today: date | None = None) -> list[dict[str, str]]:
    today = today or date.today()
    findings = []
    if cert.get("expires_on"):
        days = (date.fromisoformat(cert["expires_on"]) - today).days
        if days < 0:
            findings.append({"severity": "critical", "issue": "Certificate has expired."})
        elif days <= cert.get("renewal_window_days", 30) and not cert.get("renewal_started"):
            findings.append({"severity": "high", "issue": "Certificate is within renewal window but renewal has not started."})
    if not cert.get("automated_renewal") and not cert.get("renewal_owner"):
        findings.append({"severity": "medium", "issue": "Certificate has neither automated renewal nor an assigned owner."})
    if cert.get("hostname_match") is False:
        findings.append({"severity": "high", "issue": "Certificate does not match its intended hostname."})
    return findings
