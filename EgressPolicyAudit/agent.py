import argparse,json,ipaddress
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("workload");dest=x.get("destination")
  if not n or not dest:raise ValueError(f"item {i} workload/destination required")
  if dest in {"0.0.0.0/0","::/0","*"}:f.append({"code":"unrestricted_egress","severity":"critical","item":i,"message":f"{n} permits unrestricted egress."})
  if x.get("port") in {0,"*","any"}:f.append({"code":"all_ports","severity":"high","item":i,"message":f"{n} permits all destination ports."})
  if not x.get("owner"):f.append({"code":"missing_owner","severity":"medium","item":i,"message":f"{n} rule has no owner."})
  if not x.get("purpose"):f.append({"code":"missing_purpose","severity":"medium","item":i,"message":f"{n} rule has no purpose."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
