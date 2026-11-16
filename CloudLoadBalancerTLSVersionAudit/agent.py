"""Flags cloud load balancers that still permit deprecated TLS protocol versions."""
from typing import Any


def audit(lb: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if any(v in lb.get("allowed_tls_versions", []) for v in ("TLSv1.0", "TLSv1.1", "SSLv3")):
        findings.append({"severity": "high", "issue": "Load balancer permits deprecated TLS/SSL protocol versions."})
    if not lb.get("hsts_enabled"):
        findings.append({"severity": "medium", "issue": "Load balancer does not enforce HSTS."})
    return findings
