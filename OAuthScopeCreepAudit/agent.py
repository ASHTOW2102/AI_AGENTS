"""Flags OAuth clients requesting scopes they never actually use, violating least privilege and widening the blast radius of a stolen token."""
from typing import Any


def audit(client: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    requested = set(client.get("requested_scopes", []))
    used = set(client.get("actually_used_scopes", []))
    unused = requested - used
    if unused:
        findings.append({"severity": "medium", "issue": f"Client requests scopes it never uses: {sorted(unused)}"})
    return findings
