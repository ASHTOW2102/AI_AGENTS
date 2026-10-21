import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("route");produces={str(v).lower() for v in x.get("produces",[])};consumes={str(v).lower() for v in x.get("consumes",[])}
  if not n:raise ValueError(f"item {i}.route required")
  if not produces:f.append({"code":"missing_response_types","severity":"high","item":i,"message":f"{n} declares no response media types."})
  if x.get("accepts_body") and not consumes:f.append({"code":"missing_request_types","severity":"high","item":i,"message":f"{n} accepts a body without declaring media types."})
  if "application/json" not in produces and x.get("json_contract"):f.append({"code":"json_not_declared","severity":"medium","item":i,"message":f"{n} has a JSON contract but does not advertise JSON."})
  if "*" in produces or "*/*" in produces:f.append({"code":"wildcard_response_type","severity":"medium","item":i,"message":f"{n} advertises an unrestricted response type."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
