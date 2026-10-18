import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("workload","")).strip();request=x.get("request_mb");limit=x.get("limit_mb");peak=x.get("peak_mb")
  if not name:raise ValueError(f"item {i}.workload is required")
  if not all(isinstance(v,(int,float)) and v>0 for v in (request,limit,peak)) or request>limit:raise ValueError(f"item {i} memory values are invalid")
  if peak>limit:f.append({"code":"limit_exceeded","severity":"critical","item":i,"message":f"{name} peak exceeds its limit."})
  elif peak/limit>.9:f.append({"code":"low_headroom","severity":"high","item":i,"message":f"{name} has under 10% memory headroom."})
  if limit/request>4:f.append({"code":"request_limit_gap","severity":"medium","item":i,"message":f"{name} limit is over four times its request."})
  if not x.get("oom_alert"):f.append({"code":"missing_oom_alert","severity":"medium","item":i,"message":f"{name} has no OOM alert."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
