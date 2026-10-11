import pytest
from agent import EncryptionAuditAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"dataset":"customers","encrypted":True,"algorithm":"AES-256-GCM","dedicated_key":True,"key_age_days":30}]).healthy
def test_risky():assert {"not_encrypted","weak_algorithm","shared_key","stale_key"} <= codes(audit([{"dataset":"archive","encrypted":False,"algorithm":"DES","dedicated_key":False,"key_age_days":900}]))
def test_agent():assert EncryptionAuditAgent().inspect([{"dataset":"customers","encrypted":True,"algorithm":"AES-256-GCM","dedicated_key":True,"key_age_days":30}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
def test_bad_item():
    with pytest.raises(ValueError,match="object"):audit(["bad"])
