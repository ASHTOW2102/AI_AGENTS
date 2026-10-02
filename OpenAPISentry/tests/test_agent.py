import pytest
from agent import OpenAPISentryAgent,audit_openapi

GOOD={"openapi":"3.1.0","security":[{"bearerAuth":[]}],"paths":{"/users":{"get":{"operationId":"listUsers","summary":"List users","responses":{"200":{"description":"OK"}}}}}}

def test_valid_spec_passes():
 report=audit_openapi(GOOD)
 assert report.valid and report.operations==1 and report.findings==[]

def test_finds_missing_operation_metadata():
 spec={"openapi":"3.0.3","paths":{"/items":{"post":{"responses":{"400":{"description":"Bad"}}}}}}
 report=audit_openapi(spec)
 codes={x.code for x in report.findings}
 assert {"missing_operation_id","missing_description","missing_success_response","missing_security"}<=codes
 assert not report.valid

def test_health_endpoint_can_be_public():
 spec={"openapi":"3.0.0","paths":{"/health":{"get":{"operationId":"health","summary":"Health","responses":{"204":{"description":"OK"}}}}}}
 assert audit_openapi(spec).valid

def test_duplicate_operation_ids_fail():
 spec={"openapi":"3.0.0","security":[{"key":[]}],"paths":{"/a":{"get":{"operationId":"same","summary":"A","responses":{"200":{}}}},"/b":{"get":{"operationId":"same","summary":"B","responses":{"200":{}}}}}}
 assert any(x.code=="duplicate_operation_id" for x in audit_openapi(spec).findings)

def test_agent_works_without_key(monkeypatch):
 monkeypatch.delenv("OPENAI_API_KEY",raising=False)
 assert OpenAPISentryAgent().inspect(GOOD).mode=="local"
