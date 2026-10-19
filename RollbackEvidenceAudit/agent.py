import argparse,json
from datetime import date
from pathlib import Path
def analyze(xs,today=None):
 today=today or date.today();f=[]
 for i,x in enumerate(xs,1):
  n=x.get("service")
  if not n:raise ValueError(f"item {i}.service required")
  if not x.get("procedure"):f.append({"code":"missing_procedure","severity":"critical","item":i,"message":f"{n} has no rollback procedure."})
  tested=x.get("last_tested")
  if not tested:f.append({"code":"untested","severity":"high","item":i,"message":f"{n} has no rollback test evidence."})
  else:
   try:age=(today-date.fromisoformat(tested)).days
   except ValueError:raise ValueError(f"item {i}.last_tested invalid")
   if age>180:f.append({"code":"stale_test","severity":"high","item":i,"message":f"{n} rollback test is stale."})
  if not x.get("evidence_link"):f.append({"code":"missing_evidence","severity":"medium","item":i,"message":f"{n} lacks evidence."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
