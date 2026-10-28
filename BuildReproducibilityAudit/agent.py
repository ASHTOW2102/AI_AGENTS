"""Review build metadata for reproducibility and artifact traceability."""
from typing import Any


def audit(build: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if not build.get("dependency_lockfile_used"):
        findings.append({"severity": "medium", "issue": "Build did not use a dependency lockfile."})
    if not build.get("build_environment_pinned"):
        findings.append({"severity": "medium", "issue": "Build environment is not pinned."})
    if build.get("reproducible_check_required") and not build.get("artifact_digest_matches"):
        findings.append({"severity": "high", "issue": "Independent build artifact digests do not match."})
    if not build.get("source_revision_recorded"):
        findings.append({"severity": "high", "issue": "Artifact is not linked to an immutable source revision."})
    return findings
