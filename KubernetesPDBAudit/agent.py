import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("workload");rep=x.get("replicas")
  if not n or not isinstance(rep,int) or rep<0:raise ValueError(f"item {i} workload/replicas invalid")
  if rep>1 and x.get("min_available") is None and x.get("max_unavailable") is None:f.append({"code":"missing_pdb","severity":"high","item":i,"message":f"{n} has no disruption budget."})
  if x.get("min_available",0)>=rep and rep>0:f.append({"code":"blocks_eviction","severity":"high","item":i,"message":f"{n} budget can block all voluntary evictions."})
  if rep<2 and x.get("critical"):f.append({"code":"single_replica_critical","severity":"critical","item":i,"message":f"{n} critical workload lacks redundancy."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
