"""Check software package inventory for provenance and integrity evidence."""
from typing import Any


def audit(package: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not package.get("source_registry"):
        findings.append({"severity": "medium", "issue": "Package source registry is not recorded."})
    if not package.get("version_pinned"):
        findings.append({"severity": "high", "issue": "Dependency version is not pinned."})
    if not package.get("checksum_verified"):
        findings.append({"severity": "high", "issue": "Package checksum or signature was not verified."})
    if package.get("unapproved_source"):
        findings.append({"severity": "critical", "issue": "Package was retrieved from an unapproved source."})
    return findings
