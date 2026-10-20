import argparse,json
from datetime import date
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("incident_id");updates=x.get("updates",[])
  if not n or not isinstance(updates,list):raise ValueError(f"item {i} incident/updates invalid")
  if not updates:f.append({"code":"no_updates","severity":"high","item":i,"message":f"{n} has no stakeholder updates."})
  for j,u in enumerate(updates,1):
   for field in ("timestamp","audience","channel","summary"):
    if not u.get(field):f.append({"code":f"missing_{field}","severity":"medium","item":i,"message":f"{n} update {j} lacks {field}."})
   if not u.get("next_update_at") and not u.get("resolved"):f.append({"code":"no_next_update","severity":"medium","item":i,"message":f"{n} update {j} gives no next update time."})
  if not x.get("communications_owner"):f.append({"code":"missing_owner","severity":"high","item":i,"message":f"{n} has no communications owner."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
