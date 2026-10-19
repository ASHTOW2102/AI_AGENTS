import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("bucket")
  if not n:raise ValueError(f"item {i}.bucket required")
  if not x.get("expiration_days"):f.append({"code":"missing_expiration","severity":"high","item":i,"message":f"{n} objects never expire."})
  if x.get("versioning") and not x.get("noncurrent_expiration_days"):f.append({"code":"stale_versions","severity":"medium","item":i,"message":f"{n} old versions never expire."})
  if not x.get("abort_incomplete_upload_days"):f.append({"code":"incomplete_uploads","severity":"medium","item":i,"message":f"{n} incomplete uploads never expire."})
  if not x.get("owner"):f.append({"code":"missing_owner","severity":"medium","item":i,"message":f"{n} has no owner."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
