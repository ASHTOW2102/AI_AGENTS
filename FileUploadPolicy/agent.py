import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("route","")).strip()
  if not name:raise ValueError(f"item {i}.route is required")
  if not x.get("max_bytes") or x["max_bytes"]>100_000_000:f.append({"code":"unsafe_size_limit","severity":"high","item":i,"message":f"{name} has no safe size limit."})
  if not x.get("allowed_types"):f.append({"code":"missing_allowlist","severity":"high","item":i,"message":f"{name} lacks a type allowlist."})
  if not x.get("content_sniffing"):f.append({"code":"no_content_validation","severity":"high","item":i,"message":f"{name} trusts declared file types."})
  if not x.get("malware_scan"):f.append({"code":"no_malware_scan","severity":"critical","item":i,"message":f"{name} does not scan uploads."})
  if x.get("public_by_default"):f.append({"code":"public_default","severity":"critical","item":i,"message":f"{name} publishes uploads by default."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
