import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  r=x.get("route");methods={str(v).upper() for v in x.get("methods",[])}
  if not r or not methods:raise ValueError(f"item {i} route/methods required")
  if "TRACE" in methods:f.append({"code":"trace_enabled","severity":"high","item":i,"message":f"{r} enables TRACE."})
  if "CONNECT" in methods:f.append({"code":"connect_enabled","severity":"critical","item":i,"message":f"{r} enables CONNECT."})
  if methods&{"PUT","PATCH","DELETE"} and not x.get("authentication"):f.append({"code":"unauthenticated_mutation","severity":"critical","item":i,"message":f"{r} exposes mutation methods anonymously."})
  if "*" in methods:f.append({"code":"wildcard_methods","severity":"high","item":i,"message":f"{r} allows all methods."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
