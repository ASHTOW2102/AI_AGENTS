import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("experiment")
  if not n:raise ValueError(f"item {i}.experiment required")
  if not x.get("primary_metric"):f.append({"code":"missing_primary_metric","severity":"high","item":i,"message":f"{n} has no primary success metric."})
  if not x.get("guardrail_metrics"):f.append({"code":"missing_guardrails","severity":"high","item":i,"message":f"{n} has no safety guardrail metrics."})
  if not x.get("exposure_logging"):f.append({"code":"missing_exposure_log","severity":"medium","item":i,"message":f"{n} cannot audit who saw the variant."})
  if not x.get("end_date"):f.append({"code":"no_end_date","severity":"medium","item":i,"message":f"{n} has no planned end date."})
  if x.get("mutually_exclusive") is False:f.append({"code":"overlapping_assignment","severity":"high","item":i,"message":f"{n} may assign users to conflicting variants."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
