import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("issuer")
  if not n:raise ValueError(f"item {i}.issuer required")
  if not x.get("audience"):f.append({"code":"missing_audience","severity":"high","item":i,"message":f"{n} tokens omit audience."})
  if not x.get("expiry_required"):f.append({"code":"expiry_optional","severity":"critical","item":i,"message":f"{n} tokens may not expire."})
  if not x.get("nonce_required") and x.get("browser_flow"):f.append({"code":"nonce_optional","severity":"high","item":i,"message":f"{n} browser flow omits nonce."})
  if x.get("max_lifetime_seconds",0)>86400:f.append({"code":"long_lifetime","severity":"medium","item":i,"message":f"{n} tokens live over 24 hours."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
