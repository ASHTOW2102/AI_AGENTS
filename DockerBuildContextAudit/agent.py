"""Review container build context for secret and unnecessary file exposure."""
from typing import Any


def audit(build: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if build.get("secrets_in_context", 0) > 0:
        findings.append({"severity": "critical", "issue": "Build context includes secret files."})
    if build.get("excluded_patterns_missing"):
        findings.append({"severity": "medium", "issue": "Build context excludes no local or generated files."})
    if build.get("context_size_bytes", 0) > build.get("max_context_size_bytes", 0):
        findings.append({"severity": "low", "issue": "Build context exceeds the configured size budget."})
    if build.get("dockerfile_outside_context"):
        findings.append({"severity": "medium", "issue": "Dockerfile and build context paths are inconsistently scoped."})
    return findings
