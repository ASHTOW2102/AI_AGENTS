import argparse,json
from pathlib import Path
def analyze(xs):
 f=[]
 for i,x in enumerate(xs,1):
  n=x.get("path");p95=x.get("p95_ms");loss=x.get("packet_loss_percent")
  if not n or not all(isinstance(v,(int,float)) and v>=0 for v in (p95,loss)):raise ValueError(f"item {i} path/metrics invalid")
  if p95>x.get("max_p95_ms",200):f.append({"code":"latency_exceeded","severity":"high","item":i,"message":f"{n} p95 latency is {p95}ms."})
  if loss>x.get("max_packet_loss_percent",1):f.append({"code":"packet_loss","severity":"high","item":i,"message":f"{n} packet loss is {loss}%."})
  if not x.get("owner"):f.append({"code":"missing_owner","severity":"medium","item":i,"message":f"{n} has no owner."})
 return {"healthy":not f,"items_checked":len(xs),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
