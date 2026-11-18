"""Flags retrieval-augmented pipelines that index unvetted user-submitted content into the same embedding store queried for trusted context."""
from typing import Any


def audit(pipeline: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if pipeline.get("indexes_user_submitted_content") and not pipeline.get("content_moderation_before_indexing"):
        findings.append({"severity": "high", "issue": "User-submitted content is indexed into the retrieval store without moderation, enabling embedding poisoning."})
    if pipeline.get("indexes_user_submitted_content") and not pipeline.get("retrieval_source_segregated_by_trust_level"):
        findings.append({"severity": "medium", "issue": "Retrieval store does not segregate content by trust level."})
    return findings
