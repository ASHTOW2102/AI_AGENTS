"""Flags domains with no Certificate Transparency log monitoring configured, delaying detection of mis-issued or rogue TLS certificates issued for the organization's domains."""
from typing import Any


def audit(domain: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    monitors_ct_logs = domain.get("monitors_ct_logs", False)
    has_caa_record = domain.get("has_caa_record", False)

    if not monitors_ct_logs:
        findings.append({"severity": "medium", "issue": "Domain has no Certificate Transparency log monitoring, delaying detection of mis-issued or rogue certificates for this domain."})
    if not has_caa_record:
        findings.append({"severity": "medium", "issue": "Domain has no CAA DNS record restricting which certificate authorities may issue for it, widening the pool of CAs that could mis-issue."})
    return findings
