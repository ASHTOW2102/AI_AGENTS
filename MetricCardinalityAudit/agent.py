import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("metric");series=x.get("series")
  if not n or not isinstance(series,int) or series<0:raise ValueError(f"item {i} metric/series invalid")
  if series>x.get("max_series",10000):f.append({"code":"cardinality_exceeded","severity":"high","item":i,"message":f"{n} has {series} series."})
  labels={str(v).lower() for v in x.get("labels",[])}
  risky=labels&{"user_id","request_id","email","timestamp","uuid"}
  if risky:f.append({"code":"unbounded_label","severity":"high","item":i,"message":f"{n} uses unbounded labels: {sorted(risky)}."})
  if not x.get("owner"):f.append({"code":"missing_owner","severity":"medium","item":i,"message":f"{n} has no owner."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
