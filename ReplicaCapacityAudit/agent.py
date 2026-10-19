import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("service");desired=x.get("desired");ready=x.get("ready")
  if not n or not all(isinstance(v,int) and v>=0 for v in (desired,ready)):raise ValueError(f"item {i} service/counts invalid")
  if ready<desired:f.append({"code":"replicas_unready","severity":"high","item":i,"message":f"{n} has {ready}/{desired} ready replicas."})
  if desired<2 and x.get("critical"):f.append({"code":"insufficient_redundancy","severity":"critical","item":i,"message":f"{n} critical service has fewer than two replicas."})
  if not x.get("autoscaling") and x.get("variable_load"):f.append({"code":"no_autoscaling","severity":"medium","item":i,"message":f"{n} variable load lacks autoscaling."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
