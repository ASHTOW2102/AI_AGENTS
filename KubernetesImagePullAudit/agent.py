"""Check Kubernetes image references for reproducible pull policy."""
from typing import Any


def audit(workload: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    for image in workload.get("images", []):
        ref = image.get("reference", "")
        if ref.endswith(":latest") or ":" not in ref.rsplit("/", 1)[-1]:
            findings.append({"severity": "medium", "issue": f"Image {ref or '<unknown>'} does not use an explicit version tag."})
        if image.get("digest_pinned") is False:
            findings.append({"severity": "low", "issue": f"Image {ref or '<unknown>'} is not pinned by digest."})
    if workload.get("pull_policy") == "Never" and not workload.get("image_preloaded_guaranteed"):
        findings.append({"severity": "high", "issue": "Never pull policy is used without guaranteed image preloading."})
    if workload.get("private_registry") and not workload.get("pull_secret_configured"):
        findings.append({"severity": "high", "issue": "Private registry has no pull secret configured."})
    return findings
