"""Checks release pipelines for automated backward-compatibility testing against prior API contracts."""
from typing import Any


def audit(release: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if release.get("public_api_changed") and not release.get("backward_compat_test_run"):
        findings.append({"severity": "high", "issue": "Public API changed without a backward-compatibility test run."})
    if release.get("backward_compat_test_run") and release.get("breaking_changes_detected", 0) > 0 and not release.get("breaking_change_approved"):
        findings.append({"severity": "critical", "issue": "Breaking changes were detected but not approved before release."})
    if not release.get("contract_test_baseline_pinned"):
        findings.append({"severity": "medium", "issue": "Compatibility tests have no pinned baseline contract version."})
    return findings
