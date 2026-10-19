import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("name")
  if not n:raise ValueError(f"item {i}.name required")
  if not x.get("health_check"):f.append({"code":"missing_health_check","severity":"critical","item":i,"message":f"{n} has no health check."})
  if not x.get("connection_draining"):f.append({"code":"no_draining","severity":"high","item":i,"message":f"{n} lacks connection draining."})
  if x.get("cross_zone") is False and x.get("zones",1)>1:f.append({"code":"cross_zone_disabled","severity":"medium","item":i,"message":f"{n} may imbalance zones."})
  if not x.get("tls_policy"):f.append({"code":"missing_tls_policy","severity":"high","item":i,"message":f"{n} has no TLS policy."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
