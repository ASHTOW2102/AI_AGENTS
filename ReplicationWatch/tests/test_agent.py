import pytest
from agent import ReplicationWatchAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"replica":"orders-eu","lag_seconds":2,"healthy":True,"failover_test_days":20,"cross_region":True}]).healthy
def test_risky():assert set(['high_lag','unhealthy_replica','stale_failover_test','single_region'])<=codes(audit([{"replica":"orders-old","lag_seconds":600,"healthy":False,"failover_test_days":500,"cross_region":False}]))
def test_agent():assert ReplicationWatchAgent().inspect([{"replica":"orders-eu","lag_seconds":2,"healthy":True,"failover_test_days":20,"cross_region":True}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
