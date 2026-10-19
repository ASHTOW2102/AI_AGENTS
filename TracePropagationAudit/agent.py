import argparse,json,re
from pathlib import Path
TRACE=re.compile(r"^[0-9a-f]{32}$")
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("service");tid=str(x.get("trace_id",""))
  if not n:raise ValueError(f"item {i}.service required")
  if not TRACE.fullmatch(tid):f.append({"code":"invalid_trace_id","severity":"high","item":i,"message":f"{n} has invalid trace identity."})
  if not x.get("parent_propagated"):f.append({"code":"broken_parent","severity":"high","item":i,"message":f"{n} did not propagate its parent."})
  if not x.get("baggage_filtered"):f.append({"code":"unfiltered_baggage","severity":"medium","item":i,"message":f"{n} does not filter trace baggage."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
