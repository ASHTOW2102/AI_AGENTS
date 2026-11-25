"""Flags cloud functions storing credential-shaped values directly in plaintext environment variables instead of a secret manager."""
from typing import Any


_SECRET_HINTS = ("key", "secret", "password", "token", "credential")


def audit(function: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    env_vars = function.get("env_vars", {})
    if function.get("uses_secret_manager"):
        return findings
    suspicious = [name for name in env_vars if any(hint in name.lower() for hint in _SECRET_HINTS)]
    if suspicious:
        findings.append({"severity": "high", "issue": f"Credential-shaped env vars stored in plaintext, not a secret manager: {suspicious}"})
    return findings
