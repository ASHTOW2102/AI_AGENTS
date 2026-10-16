import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  route=str(x.get("route","")).strip();method=str(x.get("method","")).upper()
  if not route or not method:raise ValueError(f"item {i} requires route and method")
  mutation=method in {"POST","PUT","PATCH","DELETE"}
  if mutation and not x.get("idempotency_key"):f.append({"code":"missing_key","severity":"high","item":i,"message":f"{method} {route} lacks idempotency protection."})
  if x.get("idempotency_key") and not x.get("ttl_seconds"):f.append({"code":"missing_ttl","severity":"medium","item":i,"message":f"{route} key has no expiry."})
  if x.get("idempotency_key") and not x.get("request_fingerprint"):f.append({"code":"missing_fingerprint","severity":"high","item":i,"message":f"{route} does not bind keys to request content."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
