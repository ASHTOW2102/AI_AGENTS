"""Flags feature flags evaluated globally instead of per-tenant, risking one tenant's rollout state leaking into another's."""
from typing import Any


def audit(flag: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if flag.get("evaluation_scope") == "global" and flag.get("intended_scope") == "per_tenant":
        findings.append({"severity": "high", "issue": "Flag intended to be per-tenant is evaluated globally."})
    if flag.get("evaluation_scope") == "per_tenant" and not flag.get("tenant_id_validated_at_evaluation"):
        findings.append({"severity": "medium", "issue": "Per-tenant flag evaluation does not validate the tenant identifier."})
    return findings
