import pytest
from agent import IndexAdvisorAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"name":"orders_customer_idx","usage_per_day":120,"size_mb":80,"duplicate":False,"owner":"database"}]).healthy
def test_risky():assert set(['unused_index','oversized_index','duplicate_index','missing_owner'])<=codes(audit([{"name":"legacy_idx","usage_per_day":0,"size_mb":9000,"duplicate":True,"owner":""}]))
def test_agent():assert IndexAdvisorAgent().inspect([{"name":"orders_customer_idx","usage_per_day":120,"size_mb":80,"duplicate":False,"owner":"database"}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
