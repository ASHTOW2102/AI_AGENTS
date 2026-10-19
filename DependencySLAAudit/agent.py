import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("dependency");target=x.get("availability_target");actual=x.get("availability_actual")
  if not n:raise ValueError(f"item {i}.dependency required")
  if not all(isinstance(v,(int,float)) and 0<=v<=100 for v in (target,actual)):raise ValueError(f"item {i} availability invalid")
  if actual<target:f.append({"code":"availability_breach","severity":"high","item":i,"message":f"{n} availability is below target."})
  if not x.get("support_contact"):f.append({"code":"missing_support","severity":"medium","item":i,"message":f"{n} has no support contact."})
  if not x.get("escalation_minutes"):f.append({"code":"missing_escalation","severity":"medium","item":i,"message":f"{n} has no escalation window."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
