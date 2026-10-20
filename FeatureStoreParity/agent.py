import argparse,json,math
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("feature")
  if not n:raise ValueError(f"item {i}.feature required")
  off=x.get("offline_mean");online=x.get("online_mean");tol=x.get("tolerance",0)
  if not all(isinstance(v,(int,float)) and math.isfinite(v) for v in (off,online,tol)) or tol<0:raise ValueError(f"item {i} parity values invalid")
  if abs(off-online)>tol:f.append({"code":"mean_parity_gap","severity":"high","item":i,"message":f"{n} offline/online mean gap exceeds tolerance."})
  if x.get("offline_version")!=x.get("online_version"):f.append({"code":"version_mismatch","severity":"critical","item":i,"message":f"{n} offline and online definitions differ."})
  if not x.get("owner"):f.append({"code":"missing_owner","severity":"medium","item":i,"message":f"{n} has no owner."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
