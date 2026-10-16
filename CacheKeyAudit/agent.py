import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  route=str(x.get("route","")).strip();parts={str(v).lower() for v in x.get("key_parts",[])}
  if not route:raise ValueError(f"item {i}.route is required")
  if x.get("personalized") and not {"user_id","session_id"}&parts:f.append({"code":"missing_identity","severity":"critical","item":i,"message":f"{route} personalized cache key lacks identity."})
  if x.get("varies_by_language") and "language" not in parts:f.append({"code":"missing_language","severity":"high","item":i,"message":f"{route} key omits language."})
  if x.get("varies_by_query") and "query" not in parts:f.append({"code":"missing_query","severity":"high","item":i,"message":f"{route} key omits query parameters."})
  if not x.get("ttl_seconds"):f.append({"code":"missing_ttl","severity":"medium","item":i,"message":f"{route} has no cache expiry."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
