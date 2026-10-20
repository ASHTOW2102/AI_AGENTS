import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("model")
  if not n:raise ValueError(f"item {i}.model required")
  latency=x.get("p99_latency_ms");target=x.get("latency_target_ms");avail=x.get("availability_percent");goal=x.get("availability_goal_percent")
  if not all(isinstance(v,(int,float)) and v>=0 for v in (latency,target,avail,goal)):raise ValueError(f"item {i} SLO metrics invalid")
  if latency>target:f.append({"code":"latency_slo_breach","severity":"high","item":i,"message":f"{n} p99 latency exceeds target."})
  if avail<goal:f.append({"code":"availability_slo_breach","severity":"critical","item":i,"message":f"{n} availability is below goal."})
  if x.get("queue_depth",0)>x.get("queue_limit",100):f.append({"code":"queue_saturation","severity":"high","item":i,"message":f"{n} inference queue is saturated."})
  if not x.get("capacity_alert"):f.append({"code":"missing_capacity_alert","severity":"medium","item":i,"message":f"{n} lacks a capacity alert."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
