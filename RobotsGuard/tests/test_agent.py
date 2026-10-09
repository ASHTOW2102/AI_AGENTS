import pytest
from agent import RobotsGuardAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"host":"example.com","disallow":["/admin"],"allow":["/"],"sitemap":"https://example.com/sitemap.xml","crawl_delay":0}]).healthy

def test_risky_input_is_detected():
    assert {"blanket_block","sensitive_allow","missing_sitemap","high_crawl_delay"} <= codes(audit([{"host":"staging.example.com","disallow":["/"],"allow":["/private"],"sitemap":"","crawl_delay":120}]))

def test_agent_delegates():
    assert RobotsGuardAgent().inspect([{"host":"example.com","disallow":["/admin"],"allow":["/"],"sitemap":"https://example.com/sitemap.xml","crawl_delay":0}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
