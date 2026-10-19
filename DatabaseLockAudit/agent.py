import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("database");wait=x.get("max_wait_seconds");blocked=x.get("blocked_sessions")
  if not n:raise ValueError(f"item {i}.database required")
  if not all(isinstance(v,(int,float)) and v>=0 for v in (wait,blocked)):raise ValueError(f"item {i} metrics invalid")
  if wait>x.get("wait_limit_seconds",5):f.append({"code":"long_lock_wait","severity":"high","item":i,"message":f"{n} lock wait is {wait}s."})
  if blocked>x.get("blocked_limit",0):f.append({"code":"blocked_sessions","severity":"high","item":i,"message":f"{n} has {blocked} blocked sessions."})
  if (wait or blocked) and not x.get("owner"):f.append({"code":"missing_owner","severity":"medium","item":i,"message":f"{n} lock issue has no owner."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
