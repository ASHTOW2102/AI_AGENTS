import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("workload");lo=x.get("min_replicas");hi=x.get("max_replicas")
  if not n or not isinstance(lo,int) or not isinstance(hi,int) or lo<1 or hi<lo:raise ValueError(f"item {i} HPA bounds invalid")
  metrics=x.get("metrics",[])
  if not metrics:f.append({"code":"missing_metrics","severity":"critical","item":i,"message":f"{n} autoscaler has no scaling metrics."})
  if x.get("cpu_request_defined") is False:f.append({"code":"missing_cpu_request","severity":"high","item":i,"message":f"{n} CPU target cannot be calculated without requests."})
  if hi>x.get("cluster_capacity",hi):f.append({"code":"capacity_exceeded","severity":"high","item":i,"message":f"{n} maximum replicas exceed cluster capacity."})
  if not x.get("scale_down_stabilization_seconds"):f.append({"code":"no_scale_down_stabilization","severity":"medium","item":i,"message":f"{n} has no scale-down stabilization window."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
