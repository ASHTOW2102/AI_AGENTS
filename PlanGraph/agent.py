"""Dependency-aware project planning agent."""
from __future__ import annotations
import json,os
from dataclasses import asdict,dataclass
from typing import Any

@dataclass(frozen=True)
class Task:
 id:str
 duration:float
 depends_on:tuple[str,...]=()

@dataclass(frozen=True)
class ScheduledTask:
 id:str
 start:float
 finish:float
 duration:float
 depends_on:tuple[str,...]

@dataclass(frozen=True)
class PlanReport:
 project_duration:float
 critical_path:list[str]
 schedule:list[ScheduledTask]
 warnings:list[str]
 briefing:str|None=None
 mode:str="local"
 def to_dict(self)->dict[str,Any]: return asdict(self)

def parse_tasks(data:list[dict[str,Any]])->dict[str,Task]:
 tasks={}
 for item in data:
  task_id=str(item.get("id","")).strip()
  if not task_id: raise ValueError("Every task needs a non-empty id")
  if task_id in tasks: raise ValueError(f"Duplicate task id: {task_id}")
  duration=float(item.get("duration",0))
  if duration<=0: raise ValueError(f"{task_id}: duration must be positive")
  deps=tuple(str(x).strip() for x in item.get("depends_on",[]))
  tasks[task_id]=Task(task_id,duration,deps)
 missing=sorted({dep for task in tasks.values() for dep in task.depends_on if dep not in tasks})
 if missing: raise ValueError("Missing dependencies: "+", ".join(missing))
 return tasks

def _topological(tasks:dict[str,Task])->list[str]:
 state={}; order=[]; trail=[]
 def visit(task_id:str)->None:
  if state.get(task_id)==2: return
  if state.get(task_id)==1:
   start=trail.index(task_id)
   raise ValueError("Dependency cycle: "+" -> ".join(trail[start:]+[task_id]))
  state[task_id]=1; trail.append(task_id)
  for dep in tasks[task_id].depends_on: visit(dep)
  trail.pop(); state[task_id]=2; order.append(task_id)
 for task_id in tasks: visit(task_id)
 return order

def build_plan(data:list[dict[str,Any]])->PlanReport:
 tasks=parse_tasks(data)
 if not tasks: raise ValueError("Plan must contain at least one task")
 order=_topological(tasks); finish={}; predecessor={}; scheduled=[]
 for task_id in order:
  task=tasks[task_id]
  if task.depends_on:
   lead=max(task.depends_on,key=lambda dep:finish[dep])
   start=finish[lead]; predecessor[task_id]=lead
  else: start=0.0
  finish[task_id]=start+task.duration
  scheduled.append(ScheduledTask(task_id,start,finish[task_id],task.duration,task.depends_on))
 end=max(finish,key=finish.get); path=[]
 while end in tasks:
  path.append(end)
  if end not in predecessor: break
  end=predecessor[end]
 path.reverse()
 warnings=[]
 fan_out={task_id:0 for task_id in tasks}
 for task in tasks.values():
  for dep in task.depends_on: fan_out[dep]+=1
 for task_id,count in fan_out.items():
  if count>=3: warnings.append(f"{task_id}: dependency bottleneck for {count} tasks")
 return PlanReport(max(finish.values()),path,scheduled,warnings)

class PlanGraphAgent:
 def __init__(self,use_model:bool=True)->None: self.use_model=use_model
 def analyze(self,data:list[dict[str,Any]])->PlanReport:
  report=build_plan(data)
  if not self.use_model or not os.getenv("OPENAI_API_KEY"): return report
  try:
   from openai import OpenAI
   response=OpenAI().responses.create(model=os.getenv("OPENAI_MODEL","gpt-4.1-mini"),input="Explain the top project delivery risks using only this computed plan. Do not invent facts.\n"+json.dumps(report.to_dict()))
   return PlanReport(report.project_duration,report.critical_path,report.schedule,report.warnings,response.output_text.strip(),"openai")
  except Exception: return report
