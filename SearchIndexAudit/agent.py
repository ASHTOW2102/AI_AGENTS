import argparse,json
from pathlib import Path
def analyze(items):
 f=[]
 for i,x in enumerate(items,1):
  name=str(x.get("index","")).strip();docs=x.get("documents");source=x.get("source_documents")
  if not name:raise ValueError(f"item {i}.index is required")
  if not all(isinstance(v,int) and v>=0 for v in (docs,source)):raise ValueError(f"item {i} document counts are invalid")
  drift=abs(docs-source)/max(source,1)
  if drift>x.get("max_count_drift",.05):f.append({"code":"count_drift","severity":"high","item":i,"message":f"{name} count drift is {drift:.2%}."})
  if not x.get("last_indexed_at"):f.append({"code":"missing_freshness","severity":"medium","item":i,"message":f"{name} has no freshness timestamp."})
  if not x.get("owner"):f.append({"code":"missing_owner","severity":"medium","item":i,"message":f"{name} has no owner."})
 return {"healthy":not f,"items_checked":len(items),"findings":f}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("input");n=p.parse_args();r=analyze(json.loads(Path(n.input).read_text()));print(json.dumps(r,indent=2));raise SystemExit(0 if r["healthy"] else 2)
