"""Review container filesystem write permissions and temporary storage controls."""
from typing import Any


def audit(container: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not container.get("root_filesystem_read_only"):
        findings.append({"severity": "high", "issue": "Container root filesystem is writable."})
    if container.get("read_only_root_filesystem") and container.get("write_paths_required") and not container.get("writable_tmp_mount"):
        findings.append({"severity": "medium", "issue": "Required temporary writes have no dedicated writable mount."})
    if container.get("host_path_mounts", 0) > 0 and not container.get("host_mounts_reviewed"):
        findings.append({"severity": "high", "issue": "Host path mounts have not been reviewed."})
    if container.get("writable_mount_count", 0) > container.get("approved_writable_mount_count", 0):
        findings.append({"severity": "medium", "issue": "Writable mounts exceed the approved count."})
    return findings
