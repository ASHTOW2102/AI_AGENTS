import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("workload")
  if not n:raise ValueError(f"item {i}.workload required")
  if x.get("mounted_as_env"):f.append({"code":"secret_in_environment","severity":"high","item":i,"message":f"{n} mounts secrets as environment variables."})
  if not x.get("read_only"):f.append({"code":"writable_secret","severity":"critical","item":i,"message":f"{n} secret mount is writable."})
  if not x.get("rotation"):f.append({"code":"no_rotation","severity":"high","item":i,"message":f"{n} secret lacks rotation."})
  if x.get("shared_across_workloads"):f.append({"code":"shared_secret","severity":"high","item":i,"message":f"{n} shares credentials across workloads."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
