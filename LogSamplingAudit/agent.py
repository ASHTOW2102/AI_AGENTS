import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("stream","")).strip();rate=x.get("sample_rate")
  if not name:raise ValueError(f"item {i}.stream is required")
  if not isinstance(rate,(int,float)) or not 0<=rate<=1:raise ValueError(f"item {i}.sample_rate must be 0..1")
  if x.get("security_events") and rate<1:f.append({"code":"sampled_security_events","severity":"critical","item":i,"message":f"{name} samples security events."})
  if x.get("errors") and rate<1:f.append({"code":"sampled_errors","severity":"high","item":i,"message":f"{name} samples errors."})
  if rate<.01 and not x.get("volume_review"):f.append({"code":"extreme_sampling","severity":"medium","item":i,"message":f"{name} retains under one percent without review."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
