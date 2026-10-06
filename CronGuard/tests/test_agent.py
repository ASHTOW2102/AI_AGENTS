import pytest
from agent import CronGuardAgent, audit_schedule

def job(**updates):
    value = {"name": "nightly-report", "enabled": True, "interval_minutes": 1440, "offset_minutes": 60, "timezone": "Europe/London", "expected_duration_minutes": 15, "timeout_minutes": 30, "max_retries": 2, "retry_delay_minutes": 10, "singleton": True}
    value.update(updates)
    return value

def test_healthy_schedule_passes():
    assert audit_schedule([job()]).valid

def test_runtime_and_timeout_overlap():
    report = audit_schedule([job(interval_minutes=30, offset_minutes=0, expected_duration_minutes=35, timeout_minutes=40, singleton=False, max_retries=0)])
    codes = {x.code for x in report.findings}
    assert {"runtime_overlap", "timeout_overlap"} <= codes

def test_retry_spillover():
    report = audit_schedule([job(interval_minutes=60, offset_minutes=0, expected_duration_minutes=30, max_retries=3, retry_delay_minutes=15)])
    assert "retry_spillover" in {x.code for x in report.findings}

def test_same_slot_collision():
    report = audit_schedule([job(), job(name="nightly-cleanup")])
    assert "same_slot_collision" in {x.code for x in report.findings}

def test_duplicate_name():
    report = audit_schedule([job(), job()])
    assert "duplicate_name" in {x.code for x in report.findings}

def test_disabled_job_does_not_collide():
    report = audit_schedule([job(), job(name="disabled-copy", enabled=False)])
    assert "same_slot_collision" not in {x.code for x in report.findings}

def test_invalid_timezone():
    with pytest.raises(ValueError, match="IANA"):
        audit_schedule([job(timezone="Mars/Olympus")])

def test_no_key_local(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    assert CronGuardAgent().inspect([job()]).mode == "local"
