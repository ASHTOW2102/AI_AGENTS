import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  route=str(x.get("route","")).strip()
  if not route:raise ValueError(f"item {i}.route is required")
  if not x.get("origin_allowlist"):f.append({"code":"missing_origin_allowlist","severity":"high","item":i,"message":f"{route} accepts any origin."})
  if not x.get("authentication"):f.append({"code":"missing_authentication","severity":"critical","item":i,"message":f"{route} lacks authentication."})
  if not x.get("max_message_bytes"):f.append({"code":"missing_size_limit","severity":"high","item":i,"message":f"{route} has no message-size limit."})
  if not x.get("idle_timeout_seconds"):f.append({"code":"missing_idle_timeout","severity":"medium","item":i,"message":f"{route} has no idle timeout."})
  if not x.get("rate_limit"):f.append({"code":"missing_rate_limit","severity":"high","item":i,"message":f"{route} has no message rate limit."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
