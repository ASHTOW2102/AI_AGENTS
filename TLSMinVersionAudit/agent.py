"""Checks minimum negotiated TLS version and disallows deprecated protocol/cipher combinations."""
from typing import Any


def audit(endpoint: dict[str, Any]):
    findings = []
    if endpoint.get("min_tls_version", "1.2") in ("1.0", "1.1"):
        findings.append({"severity": "high", "issue": "Endpoint allows a deprecated TLS version."})
    if endpoint.get("allows_sslv3"):
        findings.append({"severity": "critical", "issue": "Endpoint allows SSLv3."})
    if endpoint.get("weak_cipher_enabled"):
        findings.append({"severity": "high", "issue": "Endpoint enables a weak cipher suite."})
    return findings
