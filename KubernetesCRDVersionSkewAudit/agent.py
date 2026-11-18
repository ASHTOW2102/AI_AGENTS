"""Flags Kubernetes custom resources still on a deprecated CRD schema version with no migration path defined."""
from typing import Any


def audit(crd: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if crd.get("served_version_deprecated") and not crd.get("conversion_webhook_configured"):
        findings.append({"severity": "high", "issue": "Deprecated CRD version is served with no conversion webhook to migrate resources."})
    if crd.get("served_version_deprecated") and not crd.get("removal_date_announced"):
        findings.append({"severity": "medium", "issue": "Deprecated CRD version has no announced removal date."})
    return findings
