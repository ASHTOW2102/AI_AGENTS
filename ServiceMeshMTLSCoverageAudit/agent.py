"""Audits service mesh traffic for gaps in mutual TLS coverage between services."""
from typing import Any


def audit(mesh: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    total = mesh.get("total_services", 0)
    covered = mesh.get("mtls_covered_services", 0)
    if total > 0 and covered < total:
        findings.append({"severity": "high", "issue": f"{total - covered} of {total} services lack mTLS coverage."})
    if mesh.get("permissive_mode_enabled"):
        findings.append({"severity": "medium", "issue": "Mesh is running in permissive mTLS mode, allowing plaintext fallback."})
    return findings
