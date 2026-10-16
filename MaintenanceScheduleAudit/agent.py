import argparse,json
from datetime import datetime
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("service","")).strip()
  if not name:raise ValueError(f"item {i}.service is required")
  try:start=datetime.fromisoformat(x["start"].replace("Z","+00:00"));end=datetime.fromisoformat(x["end"].replace("Z","+00:00"))
  except (KeyError,ValueError):raise ValueError(f"item {i} start/end must be ISO-8601")
  if end<=start:f.append({"code":"invalid_window","severity":"high","item":i,"message":f"{name} window does not end after start."})
  if not x.get("owner"):f.append({"code":"missing_owner","severity":"high","item":i,"message":f"{name} has no owner."})
  if not x.get("customer_notice") and x.get("customer_impact"):f.append({"code":"missing_notice","severity":"high","item":i,"message":f"{name} impact lacks customer notice."})
  if not x.get("rollback_plan"):f.append({"code":"missing_rollback","severity":"high","item":i,"message":f"{name} has no rollback plan."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
