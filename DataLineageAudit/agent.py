"""Audit dataset lineage records for traceability gaps."""
import argparse, json
from pathlib import Path
def analyze(items):
    if not isinstance(items,list): raise ValueError("input must be an array")
    out=[]
    for i,x in enumerate(items,1):
        name=str(x.get("dataset","")).strip()
        if not name: raise ValueError(f"item {i}.dataset is required")
        for field,severity in (("owner","high"),("source","high"),("updated_at","medium")):
            if not x.get(field): out.append({"code":f"missing_{field}","severity":severity,"item":i,"message":f"{name} has no {field}."})
        if x.get("contains_personal_data") and not x.get("retention_days"):
            out.append({"code":"missing_retention","severity":"high","item":i,"message":f"{name} has personal data without retention metadata."})
    return {"healthy":not out,"items_checked":len(items),"findings":out}
if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text())); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)
