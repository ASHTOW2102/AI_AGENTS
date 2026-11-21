"""Flags containers running with a writable root filesystem when their workload never needs to write outside a declared volume."""
from typing import Any


def audit(container: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not container.get("root_filesystem_readonly") and not container.get("requires_root_writes"):
        findings.append({"severity": "medium", "issue": "Container has a writable root filesystem despite not needing to write outside a volume."})
    if not container.get("root_filesystem_readonly") and not container.get("tmp_mounted_as_tmpfs"):
        findings.append({"severity": "low", "issue": "Writable root filesystem has no tmpfs mount for /tmp, encouraging writes to the image layer."})
    return findings
