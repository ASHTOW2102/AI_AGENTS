"""Checks service-mesh mutual TLS enforcement and certificate rotation coverage."""
from typing import Any


def audit(service: dict[str, Any]):
    findings = []
    if service.get("mesh_enabled") and not service.get("mtls_strict_mode"):
        findings.append({"severity": "high", "issue": "Mesh traffic allows non-mTLS connections."})
    if service.get("mtls_strict_mode") and service.get("cert_age_days", 0) > service.get("max_cert_age_days", 90):
        findings.append({"severity": "medium", "issue": "mTLS certificate exceeds its rotation window."})
    if service.get("external_callers") and service.get("mtls_strict_mode"):
        findings.append({"severity": "low", "issue": "External callers may be unable to present mesh certificates."})
    if not service.get("cert_rotation_automated"):
        findings.append({"severity": "medium", "issue": "Certificate rotation is not automated."})
    return findings
