import argparse,json
from datetime import date
from pathlib import Path
def analyze(items,today=None):
 today=today or date.today();f=[]
 for i,x in enumerate(items,1):
  n=x.get("request_id")
  if not n:raise ValueError(f"item {i}.request_id required")
  if not x.get("verified_request"):f.append({"code":"unverified_request","severity":"critical","item":i,"message":f"{n} request was not verified."})
  if not x.get("completed_at"):f.append({"code":"not_completed","severity":"high","item":i,"message":f"{n} has no completion evidence."})
  if not x.get("systems_checked"):f.append({"code":"downstream_unchecked","severity":"high","item":i,"message":f"{n} has no downstream-system coverage."})
  if not x.get("evidence_reference"):f.append({"code":"missing_evidence","severity":"medium","item":i,"message":f"{n} has no evidence reference."})
  due=x.get("due_date")
  if due:
   try:overdue=date.fromisoformat(due)<today and not x.get("completed_at")
   except ValueError:raise ValueError(f"item {i}.due_date must be YYYY-MM-DD")
   if overdue:f.append({"code":"overdue","severity":"critical","item":i,"message":f"{n} is past its due date."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
