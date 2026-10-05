import pytest

from agent import MeetingPulseAgent, audit_meeting


def healthy():
    return {
        "participants": ["Asha", "Ben"],
        "turns": [
            {"speaker": "Asha", "text": "We should ship the tested change next week."},
            {"speaker": "Ben", "text": "Agreed. I will prepare the release checklist."},
        ],
        "decisions": ["Ship the tested change next week."],
        "actions": [
            {
                "task": "Prepare release checklist",
                "owner": "Ben",
                "due_date": "2026-10-09",
            }
        ],
    }


def test_healthy_meeting_passes():
    assert audit_meeting(healthy()).valid


def test_dominant_speaker_is_reported():
    payload = healthy()
    payload["turns"] = [
        {"speaker": "Asha", "text": "word " * 90},
        {"speaker": "Ben", "text": "word " * 10},
    ]
    assert "dominant_speaker" in {
        item.code for item in audit_meeting(payload).findings
    }


def test_silent_declared_participant_is_reported():
    payload = healthy()
    payload["participants"].append("Cara")
    assert "silent_participant" in {
        item.code for item in audit_meeting(payload).findings
    }


def test_long_monologue_is_reported():
    payload = healthy()
    payload["turns"][0] = {
        "speaker": "Asha",
        "text": "word " * 25,
        "duration_seconds": 180,
    }
    assert "long_monologue" in {
        item.code for item in audit_meeting(payload).findings
    }


def test_incomplete_action_and_no_decision_are_reported():
    payload = healthy()
    payload["actions"] = [{"task": "Write notes"}]
    payload["decisions"] = []
    codes = {item.code for item in audit_meeting(payload).findings}
    assert {
        "missing_action_owner",
        "missing_action_deadline",
        "no_recorded_decision",
    } <= codes


def test_invalid_action_date_is_rejected():
    payload = healthy()
    payload["actions"][0]["due_date"] = "next Friday"
    with pytest.raises(ValueError, match="ISO date"):
        audit_meeting(payload)


def test_no_key_uses_local_mode(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert MeetingPulseAgent().inspect(healthy()).mode == "local"
