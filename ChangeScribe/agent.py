"""Conventional Commit release-note agent."""
from __future__ import annotations
import json,os,re
from dataclasses import asdict,dataclass
from typing import Any

_PATTERN=re.compile(r"^(?P<type>[a-z]+)(?:\((?P<scope>[^)]+)\))?(?P<breaking>!)?:\s+(?P<subject>.+)$")
_HEADINGS={"feat":"Features","fix":"Fixes","perf":"Performance","docs":"Documentation","refactor":"Refactoring","test":"Tests","build":"Build","ci":"CI","chore":"Chores"}

@dataclass(frozen=True)
class Change:
 type:str
 scope:str|None
 subject:str
 breaking:bool
 raw:str

@dataclass(frozen=True)
class ReleaseReport:
 version_bump:str
 changes:list[Change]
 ignored:list[str]
 markdown:str
 polished_markdown:str|None=None
 mode:str="local"
 def to_dict(self)->dict[str,Any]:return asdict(self)

def parse_commit(message:str)->Change|None:
 first=message.strip().splitlines()[0] if message.strip() else ""
 match=_PATTERN.match(first)
 if not match:return None
 breaking=bool(match.group("breaking")) or "BREAKING CHANGE:" in message or "BREAKING-CHANGE:" in message
 return Change(match.group("type"),match.group("scope"),match.group("subject").strip(),breaking,message)

def build_release(messages:list[str])->ReleaseReport:
 changes=[];ignored=[]
 for message in messages:
  change=parse_commit(message)
  (changes if change else ignored).append(change if change else message)
 if any(x.breaking for x in changes):bump="major"
 elif any(x.type=="feat" for x in changes):bump="minor"
 elif any(x.type in {"fix","perf"} for x in changes):bump="patch"
 else:bump="none"
 lines=["# Release notes","",f"Recommended version bump: **{bump}**"]
 breaking=[x for x in changes if x.breaking]
 if breaking:
  lines+=["","## Breaking changes"]+[f"- {x.subject}"+(f" ({x.scope})" if x.scope else "") for x in breaking]
 for commit_type,heading in _HEADINGS.items():
  group=[x for x in changes if x.type==commit_type and not x.breaking]
  if group:
   lines+=["",f"## {heading}"]+[f"- {x.subject}"+(f" ({x.scope})" if x.scope else "") for x in group]
 other=[x for x in changes if x.type not in _HEADINGS and not x.breaking]
 if other:lines+=["","## Other"]+[f"- {x.subject}"+(f" ({x.scope})" if x.scope else "") for x in other]
 return ReleaseReport(bump,changes,ignored,"\n".join(lines)+"\n")

class ChangeScribeAgent:
 def __init__(self,use_model:bool=True)->None:self.use_model=use_model
 def write(self,messages:list[str])->ReleaseReport:
  report=build_release(messages)
  if not self.use_model or not os.getenv("OPENAI_API_KEY"):return report
  try:
   from openai import OpenAI
   payload={"version_bump":report.version_bump,"changes":[asdict(x) for x in report.changes]}
   response=OpenAI().responses.create(model=os.getenv("OPENAI_MODEL","gpt-4.1-mini"),input="Polish these parsed changes into concise Markdown release notes. Preserve every breaking-change warning and invent nothing.\n"+json.dumps(payload))
   return ReleaseReport(report.version_bump,report.changes,report.ignored,report.markdown,response.output_text.strip(),"openai")
  except Exception:return report
