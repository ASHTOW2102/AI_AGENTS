import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("database")
  if not n:raise ValueError(f"item {i}.database required")
  if not x.get("tls_required"):f.append({"code":"tls_not_required","severity":"critical","item":i,"message":f"{n} connections do not require TLS."})
  if x.get("tls_required") and not x.get("certificate_verification"):f.append({"code":"certificate_unverified","severity":"high","item":i,"message":f"{n} TLS certificates are not verified."})
  if not x.get("least_privilege_role"):f.append({"code":"broad_role","severity":"high","item":i,"message":f"{n} has no least-privilege application role."})
  if not x.get("network_allowlist"):f.append({"code":"unrestricted_network","severity":"high","item":i,"message":f"{n} has no client network allowlist."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
