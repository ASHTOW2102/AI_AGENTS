import argparse,json,re
from pathlib import Path
SHA=re.compile(r"^sha256:[0-9a-f]{64}$")
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  n=x.get("image")
  if not n:raise ValueError(f"item {i}.image required")
  if not SHA.fullmatch(str(x.get("digest",""))):f.append({"code":"missing_immutable_digest","severity":"high","item":i,"message":f"{n} is not pinned by digest."})
  if x.get("tag") in {"latest","edge","dev"}:f.append({"code":"mutable_tag","severity":"medium","item":i,"message":f"{n} uses mutable tag {x['tag']}."})
  if not x.get("source_repository"):f.append({"code":"missing_source","severity":"medium","item":i,"message":f"{n} has no source repository metadata."})
  if not x.get("rebuild_policy_days"):f.append({"code":"no_rebuild_policy","severity":"medium","item":i,"message":f"{n} has no rebuild cadence."})
  if x.get("runs_as_root"):f.append({"code":"root_user","severity":"high","item":i,"message":f"{n} runs as root."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
