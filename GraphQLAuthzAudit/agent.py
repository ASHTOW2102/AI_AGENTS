"""Check GraphQL operation and field authorization coverage metadata."""
from typing import Any


def audit(schema: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    for field in schema.get("fields", []):
        name = field.get("name", "<unnamed>")
        if field.get("sensitive") and not field.get("authorization_rule"):
            findings.append({"severity": "high", "issue": f"Sensitive field {name} has no authorization rule."})
        if field.get("mutation") and not field.get("csrf_protection"):
            findings.append({"severity": "medium", "issue": f"Mutation {name} lacks CSRF protection metadata."})
    if schema.get("introspection_enabled_in_production"):
        findings.append({"severity": "low", "issue": "Schema introspection is enabled in production."})
    return findings
