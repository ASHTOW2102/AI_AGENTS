import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("dependency","")).strip()
  if not name:raise ValueError(f"item {i}.dependency is required")
  threshold=x.get("failure_threshold");reset=x.get("reset_seconds")
  if not isinstance(threshold,int) or threshold<=0:f.append({"code":"invalid_threshold","severity":"high","item":i,"message":f"{name} lacks a valid failure threshold."})
  if not isinstance(reset,(int,float)) or not 1<=reset<=3600:f.append({"code":"invalid_reset","severity":"high","item":i,"message":f"{name} reset window is unsafe."})
  if not x.get("fallback"):f.append({"code":"missing_fallback","severity":"medium","item":i,"message":f"{name} has no fallback."})
  if not x.get("metrics"):f.append({"code":"missing_metrics","severity":"medium","item":i,"message":f"{name} has no breaker telemetry."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
