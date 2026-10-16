import argparse,json
from pathlib import Path
def analyze(items):
 f=[];seen=set()
 for i,x in enumerate(items,1):
  eid=str(x.get("event_id","")).strip()
  if not eid: raise ValueError(f"item {i}.event_id is required")
  if eid in seen:f.append({"code":"duplicate_event","severity":"high","item":i,"message":f"{eid} is duplicated."})
  seen.add(eid)
  for field in ("timestamp","actor","action","target"):
   if not x.get(field):f.append({"code":f"missing_{field}","severity":"high","item":i,"message":f"{eid} lacks {field}."})
  if x.get("mutable"):f.append({"code":"mutable_audit_record","severity":"critical","item":i,"message":f"{eid} may be altered."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
