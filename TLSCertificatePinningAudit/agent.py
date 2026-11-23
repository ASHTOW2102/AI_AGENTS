"""Flags mobile apps that handle sensitive data over TLS without certificate pinning, leaving them exposed to MITM via a trusted-but-rogue CA."""
from typing import Any


def audit(mobile_app: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if mobile_app.get("handles_sensitive_data") and not mobile_app.get("certificate_pinning_enabled"):
        findings.append({"severity": "high", "issue": "App handles sensitive data but does not pin TLS certificates, exposing it to MITM via a rogue trusted CA."})
    return findings
