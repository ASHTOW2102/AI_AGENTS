import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("operation","")).strip()
  if not name:raise ValueError(f"item {i}.operation is required")
  depth=x.get("depth");cost=x.get("cost")
  if not isinstance(depth,int) or depth<0 or not isinstance(cost,(int,float)) or cost<0:raise ValueError(f"item {i} has invalid metrics")
  if depth>x.get("max_depth",10):f.append({"code":"depth_exceeded","severity":"high","item":i,"message":f"{name} depth is {depth}."})
  if cost>x.get("max_cost",1000):f.append({"code":"cost_exceeded","severity":"high","item":i,"message":f"{name} cost is {cost}."})
  if x.get("anonymous") and x.get("introspection"):f.append({"code":"anonymous_introspection","severity":"medium","item":i,"message":f"{name} exposes introspection anonymously."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
