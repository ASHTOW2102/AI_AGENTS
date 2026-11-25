"""Flags load balancers that terminate TLS at the edge but forward backend traffic unencrypted, exposing requests to anyone on the internal network segment."""
from typing import Any


def audit(lb: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if lb.get("terminates_ssl_at_lb") and not lb.get("backend_traffic_encrypted"):
        findings.append({"severity": "medium", "issue": "TLS is terminated at the load balancer but backend traffic is unencrypted."})
    return findings
