import pytest
from agent import ReleaseReadyAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"version":"1.0","tests_passed":True,"rollback_plan":True,"monitoring":True,"owner":"team","initial_rollout_percent":10}]).healthy

def test_risky_input_is_detected():
    assert {"tests_failed","missing_rollback","missing_monitoring","missing_owner","full_rollout"} <= codes(audit([{"version":"2.0","tests_passed":False,"rollback_plan":False,"monitoring":False,"owner":"","initial_rollout_percent":100}]))

def test_agent_delegates_to_audit():
    assert ReleaseReadyAgent().inspect([{"version":"1.0","tests_passed":True,"rollback_plan":True,"monitoring":True,"owner":"team","initial_rollout_percent":10}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
