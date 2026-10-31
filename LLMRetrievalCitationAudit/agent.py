"""Review retrieval-grounded answer citation coverage and source metadata."""
from typing import Any


def audit(answer: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    if answer.get("retrieved_chunks", 0) > 0 and answer.get("cited_chunks", 0) == 0:
        findings.append({"severity": "high", "issue": "Answer used retrieved context but cites no sources."})
    if answer.get("cited_chunks", 0) > answer.get("retrieved_chunks", 0):
        findings.append({"severity": "medium", "issue": "Citation count exceeds the retrieved-source count."})
    if answer.get("source_ids_present") and not answer.get("source_ids_validated"):
        findings.append({"severity": "medium", "issue": "Source identifiers are not validated against retrieval results."})
    if answer.get("citation_required") and not answer.get("citation_rendered"):
        findings.append({"severity": "high", "issue": "Required citation was not rendered in the answer."})
    return findings
