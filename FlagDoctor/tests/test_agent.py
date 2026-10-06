import pytest
from agent import FlagDoctorAgent, audit_flags

def healthy():
    return {"evaluated_at": "2026-10-06", "flags": [{
        "key": "search-v2", "type": "release", "state": "enabled",
        "owner": "search-team", "created_at": "2026-10-01",
        "expires_at": "2026-10-20", "rollout_percentage": 25,
        "environments": ["production"],
    }]}

def test_healthy_inventory_passes():
    assert audit_flags(healthy()).valid

def test_expired_active_flag_is_critical():
    data = healthy(); data["flags"][0]["expires_at"] = "2026-10-05"
    finding = next(x for x in audit_flags(data).findings if x.code == "expired_enabled_flag")
    assert finding.severity == "critical"

def test_missing_owner_and_expiry():
    data = healthy(); data["flags"][0]["owner"] = ""; data["flags"][0]["expires_at"] = None
    codes = {x.code for x in audit_flags(data).findings}
    assert {"missing_owner", "temporary_flag_without_expiry"} <= codes

def test_stale_disabled_flag():
    data = healthy(); data["flags"][0].update(state="disabled", created_at="2026-08-01", rollout_percentage=0)
    assert "stale_disabled_flag" in {x.code for x in audit_flags(data).findings}

def test_disabled_rollout_is_reported():
    data = healthy(); data["flags"][0]["state"] = "disabled"
    assert "disabled_with_rollout" in {x.code for x in audit_flags(data).findings}

def test_duplicate_keys_are_reported():
    data = healthy(); data["flags"].append(dict(data["flags"][0]))
    assert "duplicate_key" in {x.code for x in audit_flags(data).findings}

def test_invalid_rollout_is_rejected():
    data = healthy(); data["flags"][0]["rollout_percentage"] = 101
    with pytest.raises(ValueError, match="rollout_percentage"):
        audit_flags(data)

def test_no_key_uses_local_mode(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert FlagDoctorAgent().inspect(healthy()).mode == "local"
