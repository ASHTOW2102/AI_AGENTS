import pytest
from agent import RunbookReadyAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"service":"checkout","owner":"payments","reviewed_days_ago":20,"rollback_steps":True,"tested_days_ago":30,"contacts":True}]).healthy

def test_risky_input_is_detected():
    assert {"missing_owner","stale_runbook","missing_rollback","never_tested","missing_contacts"} <= codes(audit([{"service":"legacy","owner":"","reviewed_days_ago":500,"rollback_steps":False,"tested_days_ago":None,"contacts":False}]))

def test_agent_delegates():
    assert RunbookReadyAgent().inspect([{"service":"checkout","owner":"payments","reviewed_days_ago":20,"rollback_steps":True,"tested_days_ago":30,"contacts":True}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"):
        audit(["bad"])
