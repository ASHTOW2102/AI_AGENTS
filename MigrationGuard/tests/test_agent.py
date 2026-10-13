import pytest
from agent import MigrationGuardAgent, audit_migrations

def migration(**updates):
    value = {"id":"20261013_add_status","operation":"add_column","owner":"orders","estimated_lock_seconds":1,"rollback_available":True,"tested_on_copy":True,"online":True}
    value.update(updates)
    return value

def codes(report):
    return {item.code for item in report.findings}

def test_safe_migration_passes():
    assert audit_migrations([migration()]).safe

def test_destructive_change_is_flagged():
    assert "destructive_operation" in codes(audit_migrations([migration(operation="drop_column")]))

def test_locking_offline_change_is_flagged():
    report = audit_migrations([migration(operation="add_index", estimated_lock_seconds=20, online=False)])
    assert {"lock_risk", "offline_change"} <= codes(report)

def test_missing_controls_are_flagged():
    report = audit_migrations([migration(owner="", rollback_available=False, tested_on_copy=False)])
    assert {"missing_owner", "missing_rollback", "untested_migration"} <= codes(report)

def test_duplicate_ids_are_flagged():
    assert "duplicate_id" in codes(audit_migrations([migration(), migration()]))

def test_invalid_lock_time_rejected():
    with pytest.raises(ValueError, match="non-negative"):
        audit_migrations([migration(estimated_lock_seconds=-1)])

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit_migrations([])

def test_no_key_stays_local(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert MigrationGuardAgent().inspect([migration()]).mode == "local"
