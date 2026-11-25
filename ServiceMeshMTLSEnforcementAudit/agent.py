"""Flags service mesh mTLS policies set to permissive or disabled, allowing plaintext traffic between mesh workloads."""
from typing import Any


def audit(mesh: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if mesh.get("mtls_mode") in ("PERMISSIVE", "DISABLE"):
        findings.append({"severity": "high", "issue": f"Mesh mTLS mode is '{mesh.get('mtls_mode')}', permitting plaintext traffic between workloads."})
    return findings
