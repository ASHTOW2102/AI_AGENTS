"""Flags container images whose entrypoint runs as root instead of a dedicated unprivileged user, widening the blast radius of a container-breakout bug."""
from typing import Any


def audit(container: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if container.get("runs_as_root") or container.get("entrypoint_user") == "root":
        findings.append({"severity": "medium", "issue": "Container entrypoint runs as root instead of an unprivileged user."})
    return findings
