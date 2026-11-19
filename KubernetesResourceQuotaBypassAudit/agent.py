"""Flags Kubernetes namespaces with a ResourceQuota that pods can bypass by omitting resource requests entirely."""
from typing import Any


def audit(namespace: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if namespace.get("has_resource_quota") and not namespace.get("limit_range_defaults_configured"):
        findings.append({"severity": "high", "issue": "ResourceQuota exists but no LimitRange default means pods without requests can bypass it."})
    if namespace.get("has_resource_quota") and namespace.get("pods_without_requests_count", 0) > 0:
        findings.append({"severity": "medium", "issue": "Pods without resource requests are already running in this namespace."})
    return findings
