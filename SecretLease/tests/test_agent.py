import pytest
from agent import SecretLeaseAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"name":"api","owner":"team","age_days":10,"rotation_days":90,"expires_in_days":80,"scope":"service"}]).healthy

def test_risky_input_is_detected():
    assert {"rotation_overdue","missing_owner","no_expiry","global_scope"} <= codes(audit([{"name":"legacy","owner":"","age_days":400,"rotation_days":90,"expires_in_days":None,"scope":"global"}]))

def test_agent_delegates_to_audit():
    assert SecretLeaseAgent().inspect([{"name":"api","owner":"team","age_days":10,"rotation_days":90,"expires_in_days":80,"scope":"service"}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
