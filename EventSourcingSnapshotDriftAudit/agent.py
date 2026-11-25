"""Flags event-sourced aggregates whose stored snapshot predates the current schema version, risking a crash or silent misread when the snapshot is rehydrated."""
from typing import Any


def audit(aggregate: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    snapshot_version = aggregate.get("snapshot_version", 0)
    current_version = aggregate.get("current_schema_version", 0)
    if current_version and snapshot_version < current_version:
        findings.append({"severity": "medium", "issue": f"Snapshot version {snapshot_version} predates current schema version {current_version}."})
    return findings
