import pytest
from agent import TokenScopeAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"name":"ci-read","scopes":["repo:read"],"expires_in_days":30,"last_used_days_ago":1,"owner":"platform"}]).healthy

def test_risky_input_is_detected():
    assert {"privileged_scope","no_expiry","stale_token","missing_owner"} <= codes(audit([{"name":"legacy-admin","scopes":["admin","write:*"],"expires_in_days":None,"last_used_days_ago":200,"owner":""}]))

def test_agent_delegates():
    assert TokenScopeAgent().inspect([{"name":"ci-read","scopes":["repo:read"],"expires_in_days":30,"last_used_days_ago":1,"owner":"platform"}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
