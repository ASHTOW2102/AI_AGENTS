"""Review database client TLS configuration and certificate verification."""
from typing import Any


def audit(connection: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not connection.get("tls_enabled"):
        findings.append({"severity": "critical", "issue": "Database connection does not use TLS."})
    if connection.get("tls_enabled") and not connection.get("certificate_validation"):
        findings.append({"severity": "high", "issue": "Database TLS certificate validation is disabled."})
    if connection.get("min_tls_version", "TLS1.2") < "TLS1.2":
        findings.append({"severity": "high", "issue": "Database client allows TLS versions older than 1.2."})
    if connection.get("client_certificate_required") and not connection.get("client_certificate_configured"):
        findings.append({"severity": "medium", "issue": "Mutual TLS is required but no client certificate is configured."})
    return findings
