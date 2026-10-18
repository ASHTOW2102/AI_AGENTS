import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  route=str(x.get("route","")).strip(); size=x.get("bytes")
  if not route: raise ValueError(f"item {i}.route is required")
  if not isinstance(size,(int,float)) or size<0: raise ValueError(f"item {i}.bytes is invalid")
  budget=x.get("max_bytes",1_000_000)
  if size>budget:f.append({"code":"response_budget_exceeded","severity":"high","item":i,"message":f"{route} response is {size} bytes."})
  if size>100_000 and not x.get("compression"):f.append({"code":"large_uncompressed","severity":"medium","item":i,"message":f"{route} is large and uncompressed."})
  if x.get("collection") and not x.get("pagination"):f.append({"code":"unpaginated_collection","severity":"high","item":i,"message":f"{route} collection is not paginated."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
