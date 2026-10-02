"""Translation-catalog consistency agent."""
from __future__ import annotations
import json,os,re
from dataclasses import asdict,dataclass
from typing import Any
_PLACEHOLDER=re.compile(r"\{\{?\s*([A-Za-z_][A-Za-z0-9_.-]*)\s*\}?\}|%(?:\([^)]+\))?[sdif]")
@dataclass(frozen=True)
class Finding:
 severity:str
 code:str
 key:str
 message:str
@dataclass(frozen=True)
class AuditReport:
 valid:bool
 base_keys:int
 locale_keys:int
 findings:list[Finding]
 explanation:str|None=None
 mode:str="local"
 def to_dict(self)->dict[str,Any]:return asdict(self)
def flatten(data:dict[str,Any],prefix:str="")->dict[str,Any]:
 result={}
 for key,value in data.items():
  path=f"{prefix}.{key}" if prefix else str(key)
  if isinstance(value,dict):result.update(flatten(value,path))
  else:result[path]=value
 return result
def _placeholders(value:str)->set[str]:
 return {match.group(0) for match in _PLACEHOLDER.finditer(value)}
def audit_locale(base:dict[str,Any],locale:dict[str,Any])->AuditReport:
 if not isinstance(base,dict) or not isinstance(locale,dict):raise ValueError("Catalogs must be JSON objects")
 source=flatten(base);target=flatten(locale);findings=[]
 for key in sorted(source.keys()-target.keys()):findings.append(Finding("error","missing_key",key,"Translation key is missing"))
 for key in sorted(target.keys()-source.keys()):findings.append(Finding("warning","extra_key",key,"Key does not exist in the base catalog"))
 for key in sorted(source.keys()&target.keys()):
  left,right=source[key],target[key]
  if type(left) is not type(right):findings.append(Finding("error","type_mismatch",key,f"Expected {type(left).__name__}, got {type(right).__name__}"));continue
  if isinstance(right,str):
   if not right.strip():findings.append(Finding("error","empty_translation",key,"Translation is empty"))
   if _placeholders(left)!=_placeholders(right):findings.append(Finding("error","placeholder_mismatch",key,"Placeholders differ from the base message"))
 return AuditReport(not any(x.severity=="error" for x in findings),len(source),len(target),findings)
class LocaleLensAgent:
 def __init__(self,use_model:bool=True)->None:self.use_model=use_model
 def inspect(self,base:dict[str,Any],locale:dict[str,Any])->AuditReport:
  report=audit_locale(base,locale)
  if not self.use_model or not os.getenv("OPENAI_API_KEY"):return report
  try:
   from openai import OpenAI
   payload={"valid":report.valid,"findings":[asdict(x) for x in report.findings]}
   response=OpenAI().responses.create(model=os.getenv("OPENAI_MODEL","gpt-4.1-mini"),input="Explain how to repair these sanitized localization findings. Do not invent translations.\n"+json.dumps(payload))
   return AuditReport(report.valid,report.base_keys,report.locale_keys,report.findings,response.output_text.strip(),"openai")
  except Exception:return report
