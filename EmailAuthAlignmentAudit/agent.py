"""Checks SPF, DKIM, and DMARC alignment and enforcement for a sending domain."""
from typing import Any


def audit(domain: dict[str, Any]):
    findings = []
    if not domain.get("spf_present"):
        findings.append({"severity": "high", "issue": "Domain has no SPF record."})
    if not domain.get("dkim_present"):
        findings.append({"severity": "high", "issue": "Domain has no DKIM signing configured."})
    if domain.get("dmarc_policy") in (None, "none"):
        findings.append({"severity": "medium", "issue": "DMARC policy is missing or set to none."})
    if domain.get("dmarc_policy") == "reject" and not domain.get("alignment_verified"):
        findings.append({"severity": "low", "issue": "DMARC reject policy has not been verified against alignment reports."})
    return findings
