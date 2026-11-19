"""Flags mobile apps with certificate pinning that can be bypassed because it only checks the leaf certificate, not the full chain."""
from typing import Any


def audit(app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if app.get("certificate_pinning_enabled") and app.get("pinning_scope") == "leaf_only":
        findings.append({"severity": "medium", "issue": "Certificate pinning only checks the leaf certificate, not the full chain or public key."})
    if not app.get("certificate_pinning_enabled") and app.get("handles_sensitive_data"):
        findings.append({"severity": "high", "issue": "App handling sensitive data has no certificate pinning at all."})
    return findings
