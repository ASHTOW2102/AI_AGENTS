import pytest
from agent import CostPulseAgent, audit

def codes(report):
    return {item.code for item in report.findings}

def test_healthy_input_passes():
    assert audit([{"name":"compute","cost_today":80,"cost_yesterday":75,"daily_budget":100,"untagged_cost":0}]).healthy

def test_risky_input_is_detected():
    assert {"budget_exceeded", "daily_spike", "untagged_cost", "high_untagged_ratio"} <= codes(audit([{"name":"database","cost_today":240,"cost_yesterday":100,"daily_budget":150,"untagged_cost":60}]))

def test_agent_delegates_to_audit():
    assert CostPulseAgent().inspect([{"name":"compute","cost_today":80,"cost_yesterday":75,"daily_budget":100,"untagged_cost":0}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
