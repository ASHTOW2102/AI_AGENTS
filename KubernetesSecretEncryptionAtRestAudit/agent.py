"""Flags Kubernetes clusters storing Secret objects in etcd without encryption at rest, exposing them to anyone with etcd backup access."""
from typing import Any


def audit(cluster: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not cluster.get("etcd_encryption_at_rest_enabled"):
        findings.append({"severity": "high", "issue": "etcd encryption at rest is disabled; Secret objects are stored in plaintext."})
    return findings
