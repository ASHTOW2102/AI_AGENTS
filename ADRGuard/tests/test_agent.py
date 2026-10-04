import os

from agent import ADRGuardAgent, audit_adr


GOOD = """# Use PostgreSQL for transactional data

Status: accepted

## Context
The service needs durable relational storage with transactional consistency.

## Decision
Use PostgreSQL as the primary transactional database for the service.

## Alternatives
We evaluated SQLite and a document database against scaling requirements.

## Consequences
The team must operate backups, migrations, monitoring, and failover.
"""


def test_complete_adr_passes():
    assert audit_adr(GOOD).valid


def test_missing_sections_and_status_are_reported():
    codes = {item.code for item in audit_adr("# Cache choice\n\n## Context\nShort").findings}
    assert {"missing_status", "missing_section", "thin_section"} <= codes


def test_accepted_placeholder_and_open_question_are_reported():
    text = GOOD.replace(
        "transactional consistency.",
        "transactional consistency. TODO confirm peak throughput.",
    ) + "\n## Open Questions\n\n- Who owns backups?\n"
    codes = {item.code for item in audit_adr(text).findings}
    assert {"unresolved_placeholder", "accepted_with_open_questions"} <= codes


def test_superseded_record_requires_replacement_link():
    text = GOOD.replace("Status: accepted", "Status: superseded")
    assert "missing_supersession_link" in {
        item.code for item in audit_adr(text).findings
    }


def test_superseded_record_with_link_passes():
    text = (
        GOOD.replace("Status: accepted", "Status: superseded")
        + "\n## Superseded By\n\n[ADR 002](002-new-database.md)\n"
    )
    report = audit_adr(text)
    assert "missing_supersession_link" not in {
        item.code for item in report.findings
    }


def test_broken_local_link_is_reported(tmp_path):
    text = GOOD + "\n## References\n\n[Missing](missing.md)\n"
    codes = {
        item.code
        for item in audit_adr(text, source_path=str(tmp_path / "001.md")).findings
    }
    assert "broken_local_link" in codes


def test_no_key_uses_local_mode(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert ADRGuardAgent().inspect(GOOD).mode == "local"
