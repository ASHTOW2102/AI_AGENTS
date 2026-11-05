"""Checks Kubernetes namespaces for default resource limits that prevent unbounded pod consumption."""
from typing import Any


def audit(namespace: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not namespace.get("limit_range_defined"):
        findings.append({"severity": "high", "issue": "Namespace has no LimitRange, so pods can omit resource limits entirely."})
    if not namespace.get("resource_quota_defined"):
        findings.append({"severity": "medium", "issue": "Namespace has no ResourceQuota capping aggregate consumption."})
    if namespace.get("pods_without_limits_count", 0) > 0:
        findings.append({"severity": "high", "issue": "Some pods in the namespace have no resource limits set."})
    return findings
