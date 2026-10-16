import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("event","")).strip()
  if not name:raise ValueError(f"item {i}.event is required")
  if not x.get("version"):f.append({"code":"missing_version","severity":"high","item":i,"message":f"{name} is unversioned."})
  if not x.get("schema"):f.append({"code":"missing_schema","severity":"high","item":i,"message":f"{name} has no schema."})
  if not x.get("owner"):f.append({"code":"missing_owner","severity":"medium","item":i,"message":f"{name} has no owner."})
  if x.get("breaking_change") and not x.get("migration_period_days"):f.append({"code":"unmanaged_breaking_change","severity":"critical","item":i,"message":f"{name} has an unmanaged breaking change."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
