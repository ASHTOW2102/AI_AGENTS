import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("job");duration=x.get("duration_minutes")
  if not n or not isinstance(duration,(int,float)) or duration<0:raise ValueError(f"item {i} job/duration invalid")
  if duration>x.get("max_duration_minutes",60):f.append({"code":"duration_exceeded","severity":"high","item":i,"message":f"{n} exceeded its duration budget."})
  if not x.get("checkpointing") and duration>30:f.append({"code":"missing_checkpoint","severity":"medium","item":i,"message":f"{n} long job lacks checkpoints."})
  if not x.get("idempotent"):f.append({"code":"not_idempotent","severity":"high","item":i,"message":f"{n} cannot be retried safely."})
  if not x.get("owner"):f.append({"code":"missing_owner","severity":"medium","item":i,"message":f"{n} has no owner."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
