"""Review production source-map publication and exposure controls."""
from typing import Any


def audit(build: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if build.get("production") and build.get("public_source_maps") and not build.get("source_map_policy_approved"):
        findings.append({"severity": "high", "issue": "Production source maps are publicly published without approval."})
    if build.get("source_maps_required_for_monitoring") and not build.get("upload_to_private_monitoring"):
        findings.append({"severity": "medium", "issue": "Required source maps are not uploaded to a private monitoring service."})
    if build.get("source_maps_contain_sources_content") and build.get("proprietary_source"):
        findings.append({"severity": "medium", "issue": "Published source maps embed proprietary source content."})
    return findings
