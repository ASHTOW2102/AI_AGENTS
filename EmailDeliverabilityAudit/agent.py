"""Review domain email authentication and delivery-health metadata."""
from typing import Any


def audit(domain: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    for record in ("spf_valid", "dkim_valid", "dmarc_valid"):
        if not domain.get(record):
            findings.append({"severity": "high", "issue": f"Email authentication check {record.removesuffix('_valid')} is not passing."})
    if domain.get("dmarc_policy", "none").lower() == "none":
        findings.append({"severity": "medium", "issue": "DMARC policy is monitor-only."})
    if domain.get("bounce_rate_percent", 0) > domain.get("max_bounce_rate_percent", 5):
        findings.append({"severity": "medium", "issue": "Bounce rate exceeds the configured maximum."})
    return findings
