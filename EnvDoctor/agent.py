"""Secret-safe environment configuration auditor."""
from __future__ import annotations
import json,math,os,re
from collections import Counter
from dataclasses import asdict,dataclass
from typing import Any

_PLACEHOLDERS={"","changeme","change-me","todo","replace_me","your_key_here","example"}
_SENSITIVE=re.compile(r"(?i)(secret|password|passwd|token|api.?key|private.?key|credential)")

@dataclass(frozen=True)
class Finding:
 severity:str
 code:str
 key:str
 message:str

@dataclass(frozen=True)
class AuditReport:
 valid:bool
 findings:list[Finding]
 checked_keys:int
 explanation:str|None=None
 mode:str="local"
 def to_dict(self)->dict[str,Any]: return asdict(self)

def parse_env(text:str)->dict[str,str]:
 values={}
 for number,line in enumerate(text.splitlines(),1):
  line=line.strip()
  if not line or line.startswith("#"): continue
  if line.startswith("export "): line=line[7:].strip()
  if "=" not in line: raise ValueError(f"Line {number}: expected KEY=VALUE")
  key,value=line.split("=",1); key=key.strip()
  if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*",key): raise ValueError(f"Line {number}: invalid key")
  if key in values: raise ValueError(f"Line {number}: duplicate key {key}")
  value=value.strip()
  if len(value)>=2 and value[0]==value[-1] and value[0] in "'\"": value=value[1:-1]
  values[key]=value
 return values

def _entropy(value:str)->float:
 if not value:return 0.0
 counts=Counter(value)
 return -sum((n/len(value))*math.log2(n/len(value)) for n in counts.values())

def audit_env(template_text:str,actual_text:str)->AuditReport:
 template=parse_env(template_text); actual=parse_env(actual_text); findings=[]
 for key in template:
  if key not in actual: findings.append(Finding("error","missing",key,"Required key is missing"))
 for key in actual:
  if key not in template: findings.append(Finding("warning","unexpected",key,"Key is not declared in the template"))
 for key,value in actual.items():
  if value.strip().lower() in _PLACEHOLDERS:
   findings.append(Finding("error","placeholder",key,"Value is empty or still a placeholder"))
  if _SENSITIVE.search(key) and len(value)>=16 and _entropy(value)>=3.2:
   findings.append(Finding("warning","possible_secret",key,"Value resembles a real secret; keep it out of version control"))
 return AuditReport(not any(f.severity=="error" for f in findings),findings,len(actual))

class EnvDoctorAgent:
 def __init__(self,use_model:bool=True)->None:self.use_model=use_model
 def inspect(self,template_text:str,actual_text:str)->AuditReport:
  report=audit_env(template_text,actual_text)
  if not self.use_model or not os.getenv("OPENAI_API_KEY"):return report
  try:
   from openai import OpenAI
   sanitized={"valid":report.valid,"checked_keys":report.checked_keys,"findings":[asdict(x) for x in report.findings]}
   response=OpenAI().responses.create(model=os.getenv("OPENAI_MODEL","gpt-4.1-mini"),input="Explain how to fix these sanitized environment configuration findings. Never request or invent secret values.\n"+json.dumps(sanitized))
   return AuditReport(report.valid,report.findings,report.checked_keys,response.output_text.strip(),"openai")
  except Exception:return report
