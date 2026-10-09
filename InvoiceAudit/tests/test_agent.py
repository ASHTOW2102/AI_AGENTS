import pytest
from agent import InvoiceAuditAgent, audit

def codes(report):
    return {finding.code for finding in report.findings}

def test_healthy_input_passes():
    assert audit([{"number":"INV-1","subtotal":100,"tax":20,"total":120,"paid":120}]).healthy

def test_risky_input_is_detected():
    assert {"total_mismatch","negative_payment","outstanding_balance"} <= codes(audit([{"number":"INV-2","subtotal":100,"tax":20,"total":150,"paid":-5}]))

def test_agent_delegates():
    assert InvoiceAuditAgent().inspect([{"number":"INV-1","subtotal":100,"tax":20,"total":120,"paid":120}]).items_checked == 1

def test_empty_input_rejected():
    with pytest.raises(ValueError, match="non-empty"):
        audit([])

def test_non_object_rejected():
    with pytest.raises(ValueError, match="object"):
        audit(["bad"])
