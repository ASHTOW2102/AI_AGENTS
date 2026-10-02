"""Offline HTML accessibility review agent."""
from __future__ import annotations
import json,os
from dataclasses import asdict,dataclass
from html.parser import HTMLParser
from typing import Any

@dataclass(frozen=True)
class Finding:
 severity:str
 code:str
 location:str
 message:str

@dataclass(frozen=True)
class AuditReport:
 valid:bool
 findings:list[Finding]
 elements_checked:int
 explanation:str|None=None
 mode:str="local"
 def to_dict(self)->dict[str,Any]:return asdict(self)

class _Scanner(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True);self.findings=[];self.labels=set();self.inputs=[];self.buttons=[];self.current_button=None;self.heading=0;self.elements=0;self.has_lang=False
 def handle_starttag(self,tag,attrs):
  self.elements+=1;a=dict(attrs);tag=tag.lower()
  if tag=="html":self.has_lang=bool(a.get("lang","").strip())
  if tag=="img" and "alt" not in a:self.findings.append(Finding("error","missing_alt","img","Image has no alt attribute"))
  if tag=="label" and a.get("for"):self.labels.add(a["for"])
  if tag in {"input","select","textarea"}:
   if tag=="input" and a.get("type","text").lower() in {"hidden","submit","button","reset"}:return
   self.inputs.append((tag,a.get("id"),a.get("aria-label") or a.get("aria-labelledby")))
  if tag=="button":
   self.current_button={"name":a.get("aria-label") or a.get("aria-labelledby"),"text":[]}
  if len(tag)==2 and tag[0]=="h" and tag[1].isdigit():
   level=int(tag[1])
   if self.heading and level>self.heading+1:self.findings.append(Finding("warning","heading_jump",tag,f"Heading jumps from h{self.heading} to h{level}"))
   self.heading=level
 def handle_data(self,data):
  if self.current_button is not None:self.current_button["text"].append(data)
 def handle_endtag(self,tag):
  if tag.lower()=="button" and self.current_button is not None:
   self.buttons.append(self.current_button);self.current_button=None

def audit_html(html:str)->AuditReport:
 if not html.strip():raise ValueError("HTML cannot be empty")
 scanner=_Scanner();scanner.feed(html);findings=list(scanner.findings)
 if not scanner.has_lang:findings.append(Finding("error","missing_lang","html","Document language is not declared"))
 for tag,element_id,aria in scanner.inputs:
  if not aria and (not element_id or element_id not in scanner.labels):
   findings.append(Finding("error","missing_label",tag,"Form control has no associated label or ARIA name"))
 for button in scanner.buttons:
  if not button["name"] and not "".join(button["text"]).strip():
   findings.append(Finding("error","empty_button","button","Button has no accessible name"))
 return AuditReport(not any(x.severity=="error" for x in findings),findings,scanner.elements)

class A11yScoutAgent:
 def __init__(self,use_model:bool=True)->None:self.use_model=use_model
 def inspect(self,html:str)->AuditReport:
  report=audit_html(html)
  if not self.use_model or not os.getenv("OPENAI_API_KEY"):return report
  try:
   from openai import OpenAI
   payload={"valid":report.valid,"findings":[asdict(x) for x in report.findings]}
   response=OpenAI().responses.create(model=os.getenv("OPENAI_MODEL","gpt-4.1-mini"),input="Explain fixes for these HTML accessibility findings. Use only the findings and do not claim WCAG conformance.\n"+json.dumps(payload))
   return AuditReport(report.valid,report.findings,report.elements_checked,response.output_text.strip(),"openai")
  except Exception:return report
