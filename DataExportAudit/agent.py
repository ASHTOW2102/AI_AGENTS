import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("export","")).strip()
  if not name:raise ValueError(f"item {i}.export is required")
  if not x.get("requester_verified"):f.append({"code":"unverified_requester","severity":"critical","item":i,"message":f"{name} requester is not verified."})
  if not x.get("scope_reviewed"):f.append({"code":"unreviewed_scope","severity":"high","item":i,"message":f"{name} scope is not reviewed."})
  if not x.get("encrypted"):f.append({"code":"unencrypted_export","severity":"critical","item":i,"message":f"{name} is not encrypted."})
  if not x.get("expires_at"):f.append({"code":"missing_expiry","severity":"high","item":i,"message":f"{name} has no expiry."})
  if not x.get("audit_event"):f.append({"code":"missing_audit_event","severity":"medium","item":i,"message":f"{name} is not audit logged."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
