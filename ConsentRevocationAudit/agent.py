import argparse,json
from datetime import date
from pathlib import Path
def analyze(items,today=None):
 today=today or date.today();f=[]
 for i,x in enumerate(items,1):
  n=x.get("subject_id");rev=x.get("revoked_at")
  if not n:raise ValueError(f"item {i}.subject_id required")
  if not rev:f.append({"code":"not_revoked","severity":"high","item":i,"message":f"{n} has no consent revocation record."});continue
  try:date.fromisoformat(rev)
  except ValueError:raise ValueError(f"item {i}.revoked_at must be YYYY-MM-DD")
  systems=x.get("systems",[])
  for s in systems:
   if s not in x.get("confirmed_removed_from",[]):f.append({"code":"removal_unconfirmed","severity":"critical","item":i,"message":f"{n} removal is unconfirmed in {s}."})
  if not systems:f.append({"code":"no_system_inventory","severity":"high","item":i,"message":f"{n} has no downstream-system inventory."})
  if not x.get("evidence_reference"):f.append({"code":"missing_evidence","severity":"medium","item":i,"message":f"{n} revocation has no evidence reference."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
