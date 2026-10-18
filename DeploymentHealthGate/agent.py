import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("deployment","")).strip()
  if not name:raise ValueError(f"item {i}.deployment is required")
  if x.get("error_rate",0)>x.get("max_error_rate",.01):f.append({"code":"error_gate_failed","severity":"critical","item":i,"message":f"{name} error rate exceeds gate."})
  if x.get("latency_ms",0)>x.get("max_latency_ms",1000):f.append({"code":"latency_gate_failed","severity":"high","item":i,"message":f"{name} latency exceeds gate."})
  if x.get("healthy_instances",0)<x.get("min_healthy_instances",1):f.append({"code":"capacity_gate_failed","severity":"critical","item":i,"message":f"{name} lacks healthy capacity."})
  if not x.get("rollback_automated"):f.append({"code":"manual_rollback","severity":"medium","item":i,"message":f"{name} rollback is not automated."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
