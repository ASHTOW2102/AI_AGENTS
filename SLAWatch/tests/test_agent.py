import pytest
from agent import SLAWatchAgent, audit

def codes(report):
    return {item.code for item in report.findings}

def test_healthy_input_passes():
    assert audit([{"id":"T-1","status":"open","priority":"normal","owner":"sam","age_minutes":10,"last_update_minutes":5,"response_sla_minutes":60}]).healthy

def test_risky_input_is_detected():
    assert {"response_overdue", "unowned_ticket", "stale_update"} <= codes(audit([{"id":"T-2","status":"open","priority":"urgent","owner":"","age_minutes":180,"last_update_minutes":180,"response_sla_minutes":30}]))

def test_agent_delegates_to_audit():
    assert SLAWatchAgent().inspect([{"id":"T-1","status":"open","priority":"normal","owner":"sam","age_minutes":10,"last_update_minutes":5,"response_sla_minutes":60}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
