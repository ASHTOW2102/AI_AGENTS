"""Review TLS certificate chain inventory for expiry and trust completeness."""
from typing import Any


def audit(cert: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if cert.get("days_until_expiry", 99999) < 0:
        findings.append({"severity": "critical", "issue": "TLS certificate is expired."})
    elif cert.get("days_until_expiry", 99999) <= cert.get("renewal_window_days", 30) and not cert.get("renewal_started"):
        findings.append({"severity": "high", "issue": "Certificate is near expiry without renewal in progress."})
    if not cert.get("full_chain_served"):
        findings.append({"severity": "high", "issue": "Server does not provide the complete certificate chain."})
    if cert.get("chain_validation_errors", 0) > 0:
        findings.append({"severity": "high", "issue": "Certificate chain validation errors were reported."})
    return findings
