"""Flags containers that inject secrets as environment variables instead of mounted files, since env vars leak more easily via process listings, crash dumps, and child-process inheritance."""
from typing import Any


def audit(container: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if container.get("mounts_secrets_as_env_vars"):
        findings.append({"severity": "medium", "issue": "Secrets are injected as environment variables rather than mounted files."})
    return findings
