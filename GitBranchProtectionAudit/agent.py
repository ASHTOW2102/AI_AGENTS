"""Flags default branches that allow force pushes or do not require pull request review before merge."""
from typing import Any


def audit(branch: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if branch.get("is_default_branch") and (branch.get("allows_force_push") or not branch.get("requires_pr_review")):
        findings.append({"severity": "high", "issue": "Default branch allows force pushes and/or does not require PR review."})
    return findings
