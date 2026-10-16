import argparse,json
from urllib.parse import urlparse
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("name","")).strip();url=str(x.get("url","")).strip();parsed=urlparse(url)
  if not name or not parsed.hostname:raise ValueError(f"item {i} requires name and absolute URL")
  if parsed.scheme!="https":f.append({"code":"insecure_transport","severity":"critical","item":i,"message":f"{name} does not use HTTPS."})
  if not x.get("owner"):f.append({"code":"missing_owner","severity":"medium","item":i,"message":f"{name} has no owner."})
  if not x.get("data_classification"):f.append({"code":"unknown_data","severity":"high","item":i,"message":f"{name} has no data classification."})
  if not x.get("timeout_ms"):f.append({"code":"missing_timeout","severity":"high","item":i,"message":f"{name} has no timeout."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
