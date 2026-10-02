import pytest

from agent import IncidentTriageAgent, local_triage, redact_secrets


def test_redacts_common_credentials():
    text, count = redact_secrets("password=hunter2 api_key:abc123 token=qwerty")
    assert count == 3
    assert "hunter2" not in text
    assert "abc123" not in text
    assert "qwerty" not in text


def test_critical_incident_has_actionable_plan():
    report = local_triage("Production down for all users; possible data loss")
    assert report.severity == "critical"
    assert report.confidence >= 0.79
    assert len(report.immediate_actions) >= 4
    assert report.mode == "local"


def test_agent_runs_without_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    report = IncidentTriageAgent().run("Login requests return 500")
    assert report.severity == "high"
    assert report.mode == "local"


def test_empty_incident_is_rejected():
    with pytest.raises(ValueError, match="cannot be empty"):
        IncidentTriageAgent(use_model=False).run("   ")
