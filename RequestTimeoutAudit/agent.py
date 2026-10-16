import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("dependency","")).strip();connect=x.get("connect_ms");read=x.get("read_ms")
  if not name:raise ValueError(f"item {i}.dependency is required")
  if not isinstance(connect,(int,float)) or connect<=0:f.append({"code":"missing_connect_timeout","severity":"high","item":i,"message":f"{name} lacks a connect timeout."})
  if not isinstance(read,(int,float)) or read<=0:f.append({"code":"missing_read_timeout","severity":"high","item":i,"message":f"{name} lacks a read timeout."})
  if isinstance(read,(int,float)) and read>60000:f.append({"code":"excessive_read_timeout","severity":"medium","item":i,"message":f"{name} read timeout exceeds 60 seconds."})
  if x.get("retries",0)>0 and not x.get("overall_deadline_ms"):f.append({"code":"missing_deadline","severity":"high","item":i,"message":f"{name} retries lack an overall deadline."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
