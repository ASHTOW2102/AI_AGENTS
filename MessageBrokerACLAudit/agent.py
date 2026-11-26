"""Flags message brokers whose default ACL allows any client to publish or subscribe to any topic."""
from typing import Any


def audit(broker: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if broker.get("default_acl_allow_all"):
        findings.append({"severity": "high", "issue": "Broker default ACL allows any client to publish/subscribe to any topic."})
    return findings
