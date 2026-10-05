import pytest
from agent import BackupBeaconAgent, audit_backups

def healthy():
    return {
        "evaluated_at": "2026-10-05T12:00:00Z",
        "policy": {"rpo_hours": 24, "restore_test_max_age_days": 30, "require_encryption": True, "require_offsite": True, "require_immutable": True},
        "backups": [{"completed_at": "2026-10-05T06:00:00Z", "status": "success", "bytes": 2048, "encrypted": True, "offsite": True, "immutable": True}],
        "restore_tests": [{"completed_at": "2026-09-20T12:00:00Z", "status": "success"}],
    }

def test_healthy_passes():
    assert audit_backups(healthy()).valid

def test_rpo_breach():
    data = healthy(); data["backups"][0]["completed_at"] = "2026-10-03T06:00:00Z"
    assert "rpo_breached" in {x.code for x in audit_backups(data).findings}

def test_missing_protections():
    data = healthy(); data["backups"][0].update(encrypted=False, offsite=False, immutable=False)
    assert {"missing_encrypted", "missing_offsite", "missing_immutable"} <= {x.code for x in audit_backups(data).findings}

def test_zero_byte_success():
    data = healthy(); data["backups"][0]["bytes"] = 0
    assert any(x.code == "empty_success" and x.severity == "critical" for x in audit_backups(data).findings)

def test_repeated_failures():
    data = healthy(); data["backups"] += [{"completed_at": "2026-10-05T10:00:00Z", "status": "failed"}, {"completed_at": "2026-10-05T11:00:00Z", "status": "failed"}]
    assert "repeated_failures" in {x.code for x in audit_backups(data).findings}

def test_missing_restore():
    data = healthy(); data["restore_tests"] = []
    assert "no_successful_restore_test" in {x.code for x in audit_backups(data).findings}

def test_naive_timestamp_rejected():
    data = healthy(); data["evaluated_at"] = "2026-10-05T12:00:00"
    with pytest.raises(ValueError, match="timezone"):
        audit_backups(data)

def test_no_key_local(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert BackupBeaconAgent().inspect(healthy()).mode == "local"
