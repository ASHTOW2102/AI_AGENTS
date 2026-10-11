import pytest
from agent import DataFreshnessAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"dataset":"orders","age_minutes":10,"sla_minutes":60,"owner":"analytics","monitoring":True}]).healthy
def test_risky():assert set(['missed_sla','stale_dataset','missing_owner','monitoring_off']) <= codes(audit([{"dataset":"inventory","age_minutes":500,"sla_minutes":30,"owner":"","monitoring":False}]))
def test_agent():assert DataFreshnessAgent().inspect([{"dataset":"orders","age_minutes":10,"sla_minutes":60,"owner":"analytics","monitoring":True}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
def test_bad_item():
    with pytest.raises(ValueError,match="object"):audit(["bad"])
