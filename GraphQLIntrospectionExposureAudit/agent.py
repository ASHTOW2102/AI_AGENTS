"""Flags GraphQL schemas with introspection enabled in production, letting attackers enumerate the full API surface including unreleased fields."""
from typing import Any


def audit(schema: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if schema.get("introspection_enabled") and schema.get("environment") == "production":
        findings.append({"severity": "high", "issue": "GraphQL introspection is enabled in production, exposing the full schema to any client."})
    return findings
