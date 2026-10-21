import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("consumer_group");lag=x.get("lag");age=x.get("oldest_unprocessed_seconds")
  if not n or not all(isinstance(v,(int,float)) and v>=0 for v in (lag,age)):raise ValueError(f"item {i} consumer group/metrics invalid")
  if lag>x.get("max_lag",1000):f.append({"code":"lag_exceeded","severity":"high","item":i,"message":f"{n} lag is {lag}."})
  if age>x.get("max_age_seconds",300):f.append({"code":"old_event","severity":"high","item":i,"message":f"{n} oldest event age is {age}s."})
  if x.get("partitions",0)>0 and x.get("active_consumers",0)<x["partitions"]:f.append({"code":"under_consumed_partitions","severity":"medium","item":i,"message":f"{n} has fewer active consumers than partitions."})
  if not x.get("lag_alert"):f.append({"code":"missing_lag_alert","severity":"medium","item":i,"message":f"{n} has no lag alert."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
