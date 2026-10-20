import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("client");retries=x.get("max_retries");delay=x.get("max_delay_ms")
  if not n or not isinstance(retries,int) or retries<0 or not isinstance(delay,(int,float)) or delay<0:raise ValueError(f"item {i} retry settings invalid")
  if retries>5:f.append({"code":"retry_storm_risk","severity":"high","item":i,"message":f"{n} permits over five retries."})
  if retries and not x.get("backoff"):f.append({"code":"no_backoff","severity":"high","item":i,"message":f"{n} retries without backoff."})
  if retries and not x.get("jitter"):f.append({"code":"no_jitter","severity":"medium","item":i,"message":f"{n} retries synchronously without jitter."})
  if retries and not x.get("overall_deadline_ms"):f.append({"code":"unbounded_retry_time","severity":"high","item":i,"message":f"{n} has no overall retry deadline."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
