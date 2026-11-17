"""Flags services reading from replicas immediately after a write without a mechanism to guarantee read-after-write consistency."""
from typing import Any


def audit(service: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if service.get("reads_from_replica_after_write") and not service.get("read_after_write_guarantee_mechanism"):
        findings.append({"severity": "high", "issue": "Service reads from a replica after writing with no read-after-write consistency guarantee."})
    if service.get("read_after_write_guarantee_mechanism") == "sleep":
        findings.append({"severity": "medium", "issue": "Read-after-write consistency relies on a fixed sleep rather than a replication-aware mechanism."})
    return findings
