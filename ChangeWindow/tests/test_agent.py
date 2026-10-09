import pytest
from agent import ChangeWindowAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"id":"CHG-1","owner":"platform","start_hour":2,"duration_minutes":30,"rollback":True,"service":"api"}]).healthy

def test_risky_input_is_detected():
    assert {"missing_owner","peak_hours","long_change","missing_rollback"} <= codes(audit([{"id":"CHG-2","owner":"","start_hour":12,"duration_minutes":240,"rollback":False,"service":"database"}]))

def test_agent_delegates():
    assert ChangeWindowAgent().inspect([{"id":"CHG-1","owner":"platform","start_hour":2,"duration_minutes":30,"rollback":True,"service":"api"}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
