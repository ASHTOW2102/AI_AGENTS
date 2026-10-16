import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("service","")).strip()
  if not name:raise ValueError(f"item {i}.service is required")
  for field,severity in (("logs","high"),("metrics","high"),("traces","medium"),("dashboard","medium"),("alerts","high")):
   if not x.get(field):f.append({"code":f"missing_{field}","severity":severity,"item":i,"message":f"{name} lacks {field} coverage."})
  if x.get("alerts") and not x.get("runbook"):f.append({"code":"alert_without_runbook","severity":"medium","item":i,"message":f"{name} alerts lack a runbook."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
