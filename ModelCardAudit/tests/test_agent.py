import pytest
from agent import ModelCardAuditAgent,audit
def codes(r):return {x.code for x in r.findings}
def test_healthy():assert audit([{"model":"classifier-v2","owner":"ml","limitations":True,"evaluation":True,"data_documented":True,"human_review":True}]).healthy
def test_risky():assert set(['missing_owner','missing_limitations','missing_evaluation','missing_data_docs','missing_human_review'])<=codes(audit([{"model":"auto-decider","owner":"","limitations":False,"evaluation":False,"data_documented":False,"human_review":False}]))
def test_agent():assert ModelCardAuditAgent().inspect([{"model":"classifier-v2","owner":"ml","limitations":True,"evaluation":True,"data_documented":True,"human_review":True}]).items_checked==1
def test_empty():
    with pytest.raises(ValueError,match="non-empty"):audit([])
