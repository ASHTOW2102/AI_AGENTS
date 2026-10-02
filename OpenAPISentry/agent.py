"""Offline OpenAPI quality and security review agent."""
from __future__ import annotations
import json,os
from dataclasses import asdict,dataclass
from typing import Any

_METHODS={"get","post","put","patch","delete","options","head","trace"}

@dataclass(frozen=True)
class Finding:
 severity:str
 code:str
 location:str
 message:str

@dataclass(frozen=True)
class AuditReport:
 valid:bool
 operations:int
 findings:list[Finding]
 explanation:str|None=None
 mode:str="local"
 def to_dict(self)->dict[str,Any]:return asdict(self)

def audit_openapi(spec:dict[str,Any],public_prefixes:tuple[str,...]=("/health","/status"))->AuditReport:
 if not isinstance(spec,dict):raise ValueError("Specification must be an object")
 version=str(spec.get("openapi",""))
 if not version.startswith("3."):raise ValueError("Only OpenAPI 3.x specifications are supported")
 paths=spec.get("paths")
 if not isinstance(paths,dict) or not paths:raise ValueError("Specification must contain paths")
 findings=[];operation_ids={};count=0
 global_security=spec.get("security")
 for path,item in paths.items():
  if not isinstance(item,dict):continue
  for method,operation in item.items():
   if method.lower() not in _METHODS or not isinstance(operation,dict):continue
   count+=1;location=f"{method.upper()} {path}"
   operation_id=operation.get("operationId")
   if not operation_id:findings.append(Finding("error","missing_operation_id",location,"Operation has no operationId"))
   else:operation_ids.setdefault(str(operation_id),[]).append(location)
   if not operation.get("summary") and not operation.get("description"):
    findings.append(Finding("warning","missing_description",location,"Operation has no summary or description"))
   responses=operation.get("responses",{})
   if not isinstance(responses,dict) or not any(str(code).startswith("2") for code in responses):
    findings.append(Finding("error","missing_success_response",location,"Operation declares no 2xx response"))
   is_public=any(str(path).startswith(prefix) for prefix in public_prefixes)
   security=operation.get("security",global_security)
   if not is_public and not security:
    findings.append(Finding("warning","missing_security",location,"Non-public operation declares no security requirement"))
 for operation_id,locations in operation_ids.items():
  if len(locations)>1:
   findings.append(Finding("error","duplicate_operation_id",", ".join(locations),f"operationId {operation_id} is reused"))
 return AuditReport(not any(x.severity=="error" for x in findings),count,findings)

class OpenAPISentryAgent:
 def __init__(self,use_model:bool=True)->None:self.use_model=use_model
 def inspect(self,spec:dict[str,Any])->AuditReport:
  report=audit_openapi(spec)
  if not self.use_model or not os.getenv("OPENAI_API_KEY"):return report
  try:
   from openai import OpenAI
   payload={"valid":report.valid,"operations":report.operations,"findings":[asdict(x) for x in report.findings]}
   response=OpenAI().responses.create(model=os.getenv("OPENAI_MODEL","gpt-4.1-mini"),input="Prioritize fixes for these sanitized OpenAPI audit findings. Do not invent endpoints.\n"+json.dumps(payload))
   return AuditReport(report.valid,report.operations,report.findings,response.output_text.strip(),"openai")
  except Exception:return report
