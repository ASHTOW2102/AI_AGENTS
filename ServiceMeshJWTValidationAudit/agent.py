"""Flags service mesh sidecars configured to validate JWTs without pinning the expected issuer, accepting tokens from any trusted-looking issuer."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if service.get("jwt_validation_enabled") and not service.get("issuer_pinned"):
        findings.append({"severity": "high", "issue": "JWT validation does not pin an expected issuer."})
    if service.get("jwt_validation_enabled") and not service.get("audience_validated"):
        findings.append({"severity": "medium", "issue": "JWT validation does not check the audience claim."})
    return findings
