import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("database","")).strip();minimum=x.get("min_connections");maximum=x.get("max_connections")
  if not name:raise ValueError(f"item {i}.database is required")
  if not isinstance(minimum,int) or not isinstance(maximum,int) or minimum<0 or maximum<=0 or minimum>maximum:raise ValueError(f"item {i} pool bounds are invalid")
  if maximum>x.get("database_limit",maximum):f.append({"code":"pool_exceeds_limit","severity":"critical","item":i,"message":f"{name} pool exceeds database capacity."})
  if not x.get("acquire_timeout_ms"):f.append({"code":"missing_acquire_timeout","severity":"high","item":i,"message":f"{name} has no acquisition timeout."})
  if not x.get("idle_timeout_ms"):f.append({"code":"missing_idle_timeout","severity":"medium","item":i,"message":f"{name} has no idle timeout."})
  if not x.get("metrics"):f.append({"code":"missing_metrics","severity":"medium","item":i,"message":f"{name} pool is not monitored."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
