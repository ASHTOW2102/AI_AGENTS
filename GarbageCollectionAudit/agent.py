import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("runtime");pause=x.get("p99_pause_ms");heap=x.get("heap_usage_percent")
  if not n:raise ValueError(f"item {i}.runtime required")
  if not all(isinstance(v,(int,float)) and v>=0 for v in (pause,heap)):raise ValueError(f"item {i} metrics invalid")
  if pause>x.get("max_pause_ms",200):f.append({"code":"pause_exceeded","severity":"high","item":i,"message":f"{n} GC pause exceeds target."})
  if heap>90:f.append({"code":"heap_pressure","severity":"high","item":i,"message":f"{n} heap usage is {heap}%."})
  if not x.get("metrics_enabled"):f.append({"code":"missing_metrics","severity":"medium","item":i,"message":f"{n} GC metrics disabled."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
