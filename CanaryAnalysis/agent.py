import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("deployment");c=x.get("canary_error_rate");b=x.get("baseline_error_rate")
  if not n:raise ValueError(f"item {i}.deployment required")
  if not all(isinstance(v,(int,float)) and v>=0 for v in (c,b)):raise ValueError(f"item {i} rates invalid")
  if c>b+x.get("max_error_delta",.01):f.append({"code":"error_regression","severity":"critical","item":i,"message":f"{n} canary error rate regressed."})
  if x.get("canary_latency_ms",0)>x.get("baseline_latency_ms",0)*(1+x.get("max_latency_ratio",.2)):f.append({"code":"latency_regression","severity":"high","item":i,"message":f"{n} canary latency regressed."})
  if x.get("sample_size",0)<x.get("min_sample_size",100):f.append({"code":"insufficient_sample","severity":"medium","item":i,"message":f"{n} sample is too small."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
