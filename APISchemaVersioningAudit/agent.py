"""Flags API changes marked as breaking that ship without a corresponding version bump, silently breaking existing clients."""
from typing import Any


def audit(api: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if api.get("has_breaking_change") and not api.get("version_bumped"):
        findings.append({"severity": "high", "issue": "A breaking API change shipped without a version bump."})
    return findings
