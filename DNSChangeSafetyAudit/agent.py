"""Review DNS change plans for propagation, rollback, and TTL readiness."""
from typing import Any


def audit(change: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if change.get("high_impact") and not change.get("rollback_recorded"):
        findings.append({"severity": "high", "issue": "High-impact DNS change has no rollback record."})
    if change.get("ttl_reduced_for_migration") and not change.get("ttl_reduction_lead_hours"):
        findings.append({"severity": "medium", "issue": "TTL reduction has no lead time before migration."})
    if change.get("nameserver_change") and not change.get("registrar_consistency_checked"):
        findings.append({"severity": "high", "issue": "Nameserver change lacks registrar consistency verification."})
    if change.get("dnssec_enabled") and change.get("key_change") and not change.get("ds_coordination_confirmed"):
        findings.append({"severity": "high", "issue": "DNSSEC key change lacks parent DS coordination evidence."})
    return findings
