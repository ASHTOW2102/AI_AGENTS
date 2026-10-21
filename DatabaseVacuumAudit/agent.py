import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("table");dead=x.get("dead_tuple_percent");age=x.get("seconds_since_vacuum")
  if not n or not all(isinstance(v,(int,float)) and v>=0 for v in (dead,age)):raise ValueError(f"item {i} table/vacuum metrics invalid")
  if dead>=x.get("max_dead_tuple_percent",20):f.append({"code":"dead_tuples_high","severity":"high","item":i,"message":f"{n} dead tuples are {dead}%."})
  if age>x.get("max_vacuum_age_seconds",604800):f.append({"code":"vacuum_overdue","severity":"medium","item":i,"message":f"{n} has not been vacuumed recently."})
  if x.get("transaction_id_age_percent",0)>80:f.append({"code":"transaction_id_wraparound_risk","severity":"critical","item":i,"message":f"{n} transaction ID age is high."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
