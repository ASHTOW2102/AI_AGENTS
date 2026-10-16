import argparse,json
from datetime import date
from pathlib import Path
def analyze(items,today=None):
 today=today or date.today(); f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("endpoint","")).strip()
  if not name: raise ValueError(f"item {i}.endpoint is required")
  if x.get("deprecated"):
   if not x.get("replacement"): f.append({"code":"missing_replacement","severity":"high","item":i,"message":f"{name} has no replacement."})
   sunset=x.get("sunset_date")
   if not sunset: f.append({"code":"missing_sunset","severity":"medium","item":i,"message":f"{name} has no sunset date."})
   else:
    try: days=(date.fromisoformat(sunset)-today).days
    except ValueError: raise ValueError(f"item {i}.sunset_date must be YYYY-MM-DD")
    if days<0: f.append({"code":"past_sunset","severity":"critical","item":i,"message":f"{name} is past sunset."})
    elif days<90 and not x.get("migration_notice"): f.append({"code":"notice_missing","severity":"high","item":i,"message":f"{name} sunsets soon without notice."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
