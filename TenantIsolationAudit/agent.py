import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("resource")
  if not n:raise ValueError(f"item {i}.resource required")
  if not x.get("tenant_key"):f.append({"code":"missing_tenant_key","severity":"critical","item":i,"message":f"{n} lacks a tenant partition key."})
  if not x.get("authorization_filter"):f.append({"code":"missing_auth_filter","severity":"critical","item":i,"message":f"{n} lacks tenant authorization filtering."})
  if x.get("shared_cache") and not x.get("tenant_cache_key"):f.append({"code":"shared_cache_leak","severity":"critical","item":i,"message":f"{n} cache keys omit tenant identity."})
  if not x.get("isolation_tests"):f.append({"code":"missing_tests","severity":"high","item":i,"message":f"{n} has no isolation tests."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
