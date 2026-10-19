import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("query");timeout=x.get("timeout_ms")
  if not n:raise ValueError(f"item {i}.query required")
  if not isinstance(timeout,(int,float)) or timeout<=0:f.append({"code":"missing_timeout","severity":"high","item":i,"message":f"{n} has no valid timeout."})
  elif timeout>x.get("max_timeout_ms",30000):f.append({"code":"timeout_too_long","severity":"medium","item":i,"message":f"{n} timeout is excessive."})
  if not x.get("cancellation"):f.append({"code":"no_cancellation","severity":"high","item":i,"message":f"{n} cannot be cancelled."})
  if x.get("writes") and not x.get("transaction_boundary"):f.append({"code":"unsafe_write_timeout","severity":"critical","item":i,"message":f"{n} writes lack a transaction boundary."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
