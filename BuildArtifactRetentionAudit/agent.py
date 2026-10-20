import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("artifact")
  if not n:raise ValueError(f"item {i}.artifact required")
  days=x.get("retention_days")
  if not isinstance(days,int) or days<0:raise ValueError(f"item {i}.retention_days invalid")
  if x.get("production") and days==0:f.append({"code":"production_without_retention","severity":"high","item":i,"message":f"{n} production artifact is not retained."})
  if days>x.get("max_retention_days",365):f.append({"code":"retention_excessive","severity":"medium","item":i,"message":f"{n} exceeds its retention limit."})
  if not x.get("access_policy"):f.append({"code":"uncontrolled_access","severity":"high","item":i,"message":f"{n} has no access policy."})
  if not x.get("cleanup_owner"):f.append({"code":"missing_cleanup_owner","severity":"low","item":i,"message":f"{n} has no cleanup owner."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
