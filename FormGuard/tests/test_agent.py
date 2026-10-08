import pytest
from agent import FormGuardAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"name":"signup","method":"POST","action":"https://example.com","csrf":True,"fields":[{"name":"email","type":"email","autocomplete":"email"}]}]).healthy

def test_risky_input_is_detected():
    assert {"insecure_action","sensitive_get","missing_csrf","unsafe_password_autocomplete"} <= codes(audit([{"name":"login","method":"GET","action":"http://example.com","csrf":False,"fields":[{"name":"password","type":"password","autocomplete":"on"}]}]))

def test_post_without_csrf_is_detected():
    item = {"name":"contact","method":"POST","action":"https://example.com","csrf":False,"fields":[]}
    assert "missing_csrf" in codes(audit([item]))

def test_agent_delegates_to_audit():
    assert FormGuardAgent().inspect([{"name":"signup","method":"POST","action":"https://example.com","csrf":True,"fields":[{"name":"email","type":"email","autocomplete":"email"}]}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
