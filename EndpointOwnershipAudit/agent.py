import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("endpoint")
  if not n:raise ValueError(f"item {i}.endpoint required")
  if not x.get("team"):f.append({"code":"missing_team","severity":"high","item":i,"message":f"{n} has no owning team."})
  if not x.get("repository"):f.append({"code":"missing_repository","severity":"medium","item":i,"message":f"{n} has no source repository."})
  if not x.get("on_call"):f.append({"code":"missing_on_call","severity":"high","item":i,"message":f"{n} has no on-call route."})
  if not x.get("runbook"):f.append({"code":"missing_runbook","severity":"medium","item":i,"message":f"{n} has no runbook."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
