"""Flags repositories that do not require signed commits, making it impossible to verify a commit's actual author after the fact."""
from typing import Any


def audit(repo: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not repo.get("requires_signed_commits"):
        findings.append({"severity": "medium", "issue": "Repository does not require signed commits."})
    return findings
