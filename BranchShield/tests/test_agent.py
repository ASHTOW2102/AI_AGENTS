import pytest
from agent import BranchShieldAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"repository":"api","branch":"main","required_reviews":2,"status_checks":True,"force_push":False,"admin_bypass":False}]).healthy

def test_risky_input_is_detected():
    assert {"no_reviews","missing_checks","force_push_allowed","admin_bypass"} <= codes(audit([{"repository":"legacy","branch":"master","required_reviews":0,"status_checks":False,"force_push":True,"admin_bypass":True}]))

def test_agent_delegates():
    assert BranchShieldAgent().inspect([{"repository":"api","branch":"main","required_reviews":2,"status_checks":True,"force_push":False,"admin_bypass":False}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError,match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError,match="object"):
        audit(["bad"])
