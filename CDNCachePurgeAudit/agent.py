"""Checks CDN purge coverage, propagation timing, and cache-key scope after deploys."""
from typing import Any


def audit(deploy: dict[str, Any]):
    findings = []
    if deploy.get("cache_affecting_change") and not deploy.get("purge_triggered"):
        findings.append({"severity": "high", "issue": "Cache-affecting deploy did not trigger a CDN purge."})
    if deploy.get("purge_triggered") and deploy.get("purge_propagation_seconds", 0) > deploy.get("max_propagation_seconds", 60):
        findings.append({"severity": "medium", "issue": "Purge propagation exceeded the expected window."})
    if deploy.get("purge_scope") == "all" and not deploy.get("purge_scope_approved"):
        findings.append({"severity": "medium", "issue": "Full-cache purge was not approved."})
    if deploy.get("stale_object_count", 0) > 0 and deploy.get("purge_verified") is False:
        findings.append({"severity": "low", "issue": "Purge completion was not verified against stale objects."})
    return findings
