import pytest
from agent import QueueWatchAgent, audit

def codes(report):
    return {item.code for item in report.findings}

def test_healthy_input_passes():
    assert audit([{"name":"orders","backlog":10,"consumers":2,"oldest_message_seconds":5,"dead_letters":0,"sla_seconds":60}]).healthy

def test_risky_input_is_detected():
    assert {"no_consumers", "stale_messages", "dead_letters"} <= codes(audit([{"name":"orders","backlog":500,"consumers":0,"oldest_message_seconds":120,"dead_letters":2,"sla_seconds":60}]))

def test_agent_delegates_to_audit():
    assert QueueWatchAgent().inspect([{"name":"orders","backlog":10,"consumers":2,"oldest_message_seconds":5,"dead_letters":0,"sla_seconds":60}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
