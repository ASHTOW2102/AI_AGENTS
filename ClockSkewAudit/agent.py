import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("node","")).strip();skew=x.get("skew_ms")
  if not name:raise ValueError(f"item {i}.node is required")
  if not isinstance(skew,(int,float)):raise ValueError(f"item {i}.skew_ms is invalid")
  limit=x.get("max_skew_ms",1000)
  if abs(skew)>limit:f.append({"code":"clock_skew_exceeded","severity":"high","item":i,"message":f"{name} clock skew is {skew}ms."})
  if not x.get("time_source"):f.append({"code":"missing_time_source","severity":"medium","item":i,"message":f"{name} has no declared time source."})
  if not x.get("monitoring"):f.append({"code":"missing_monitoring","severity":"medium","item":i,"message":f"{name} clock is not monitored."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
