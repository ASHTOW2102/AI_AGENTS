import argparse,json
from datetime import date
from pathlib import Path
def analyze(items,today=None):
 today=today or date.today();f=[]
 for i,x in enumerate(items,1):
  n=x.get("key_id")
  if not n:raise ValueError(f"item {i}.key_id required")
  if not x.get("owner"):f.append({"code":"missing_owner","severity":"high","item":i,"message":f"{n} has no owner."})
  if not x.get("scope"):f.append({"code":"missing_scope","severity":"high","item":i,"message":f"{n} has no declared scope."})
  raw=x.get("last_rotated")
  if not raw:f.append({"code":"never_rotated","severity":"high","item":i,"message":f"{n} has no rotation date."})
  else:
   try:age=(today-date.fromisoformat(raw)).days
   except ValueError:raise ValueError(f"item {i}.last_rotated must be YYYY-MM-DD")
   if age>x.get("max_age_days",90):f.append({"code":"rotation_overdue","severity":"critical","item":i,"message":f"{n} was last rotated {age} days ago."})
  if x.get("shared_users",0)>1 and not x.get("shared_key_justification"):f.append({"code":"shared_key","severity":"medium","item":i,"message":f"{n} is shared without justification."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
