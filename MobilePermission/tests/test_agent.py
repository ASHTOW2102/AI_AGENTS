import pytest
from agent import MobilePermissionAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"permission":"camera","sensitive":True,"required":True,"purpose":"Scan QR codes","background":False,"owner":"mobile"}]).healthy
def test_risky():assert set(['unnecessary_permission','missing_purpose','background_access','missing_owner']) <= codes(audit([{"permission":"location","sensitive":True,"required":False,"purpose":"","background":True,"owner":""}]))
def test_agent():assert MobilePermissionAgent().inspect([{"permission":"camera","sensitive":True,"required":True,"purpose":"Scan QR codes","background":False,"owner":"mobile"}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
def test_bad_item():
    with pytest.raises(ValueError,match="object"):audit(["bad"])
