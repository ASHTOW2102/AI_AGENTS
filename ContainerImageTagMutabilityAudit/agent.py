"""Flags container registries that use a mutable 'latest' tag in production, or that have not enabled tag immutability at all."""
from typing import Any


def audit(registry: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if registry.get("uses_latest_tag_in_production"):
        findings.append({"severity": "high", "issue": "Production deployment uses the mutable 'latest' tag."})
    elif not registry.get("tag_immutability_enabled"):
        findings.append({"severity": "medium", "issue": "Tag immutability is not enabled on the registry."})
    return findings
