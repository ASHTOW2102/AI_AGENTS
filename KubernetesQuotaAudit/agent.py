import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("namespace");used=x.get("used");limit=x.get("limit")
  if not n or not isinstance(used,dict) or not isinstance(limit,dict) or not limit:raise ValueError(f"item {i} namespace/used/limit invalid")
  for resource,cap in limit.items():
   value=used.get(resource,0)
   if not isinstance(value,(int,float)) or not isinstance(cap,(int,float)) or cap<=0 or value<0:raise ValueError(f"item {i} quota values invalid")
   ratio=value/cap
   if ratio>=1:f.append({"code":"quota_exceeded","severity":"critical","item":i,"message":f"{n} {resource} quota is exhausted."})
   elif ratio>=x.get("warning_ratio",.85):f.append({"code":"quota_near_limit","severity":"high","item":i,"message":f"{n} {resource} quota is {ratio:.0%} used."})
  if not x.get("owner"):f.append({"code":"missing_owner","severity":"medium","item":i,"message":f"{n} has no quota owner."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
