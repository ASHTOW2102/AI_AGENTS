"""Flags TLS server configurations that still enable deprecated or weak cipher suites (e.g. RC4, 3DES, null ciphers) or protocol versions below TLS 1.2."""
from typing import Any

WEAK_CIPHERS = {"RC4", "3DES", "NULL", "DES"}


def audit(server: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    enabled_ciphers = set(server.get("enabled_cipher_suites", []))
    min_protocol = server.get("min_protocol_version", "TLS1.2")

    weak = enabled_ciphers & WEAK_CIPHERS
    if weak:
        findings.append({"severity": "high", "issue": f"Server enables deprecated/weak cipher suites: {sorted(weak)}"})

    if min_protocol in ("TLS1.0", "TLS1.1", "SSL3.0"):
        findings.append({"severity": "high", "issue": f"Server allows protocol version {min_protocol}, below the TLS 1.2 minimum recommended today."})
    return findings
