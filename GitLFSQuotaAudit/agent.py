"""Flags Git LFS storage usage approaching its quota, before pushes start failing outright."""
from typing import Any


def audit(repo: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    usage = repo.get("lfs_usage_bytes", 0)
    quota = repo.get("lfs_quota_bytes", 0)
    if quota and usage > quota * 0.9:
        findings.append({"severity": "medium", "issue": f"Git LFS usage ({usage} bytes) is over 90% of the {quota}-byte quota."})
    return findings
