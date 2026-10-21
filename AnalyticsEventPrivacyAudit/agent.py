"""Check analytics event schemas for privacy and retention risks."""
from __future__ import annotations

from typing import Any


def audit(event: dict[str, Any], approved_properties: set[str]) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    unexpected = sorted(set(event.get("properties", {})) - approved_properties)
    if unexpected:
        findings.append({"severity": "medium", "issue": "Unapproved event properties: " + ", ".join(unexpected)})
    if event.get("contains_direct_identifiers"):
        findings.append({"severity": "high", "issue": "Event includes direct personal identifiers."})
    if event.get("requires_consent") and not event.get("consent_gated"):
        findings.append({"severity": "high", "issue": "Consent-required event is not gated by consent."})
    if event.get("retention_days", 0) > event.get("approved_retention_days", 0):
        findings.append({"severity": "medium", "issue": "Event retention exceeds its approved period."})
    return findings
