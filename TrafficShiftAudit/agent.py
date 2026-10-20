import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("service");steps=x.get("weights",[])
  if not n or not isinstance(steps,list) or not steps:raise ValueError(f"item {i} service/weights required")
  if any(not isinstance(w,(int,float)) or not 0<=w<=100 for w in steps):raise ValueError(f"item {i} has invalid traffic weight")
  if any(b<a for a,b in zip(steps,steps[1:])):f.append({"code":"non_monotonic_shift","severity":"high","item":i,"message":f"{n} rollout weights decrease."})
  if sum(steps)>100:f.append({"code":"weight_overflow","severity":"critical","item":i,"message":f"{n} traffic weights exceed 100%."})
  if any(b-a>x.get("max_step_percent",25) for a,b in zip(steps,steps[1:])):f.append({"code":"large_step","severity":"medium","item":i,"message":f"{n} rollout has a step larger than allowed."})
  if not x.get("health_gate"):f.append({"code":"missing_gate","severity":"high","item":i,"message":f"{n} traffic shift lacks a health gate."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
