import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("flow")
  if not n:raise ValueError(f"item {i}.flow required")
  if not x.get("rate_limit"):f.append({"code":"no_rate_limit","severity":"critical","item":i,"message":f"{n} has no login rate limit."})
  if not x.get("progressive_delay"):f.append({"code":"no_progressive_delay","severity":"medium","item":i,"message":f"{n} has no progressive delay."})
  if not x.get("credential_stuffing_detection"):f.append({"code":"no_stuffing_detection","severity":"high","item":i,"message":f"{n} has no credential-stuffing signal."})
  if not x.get("account_recovery_rate_limit"):f.append({"code":"recovery_unlimited","severity":"high","item":i,"message":f"{n} recovery flow is not rate limited."})
  if x.get("permanent_lockout"):f.append({"code":"permanent_lockout","severity":"medium","item":i,"message":f"{n} can permanently lock out users."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
