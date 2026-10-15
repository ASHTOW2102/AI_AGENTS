"""Evaluate dataset quality metrics against explicit gates."""
import argparse,json
from pathlib import Path
def analyze(items):
    findings=[]
    for i,x in enumerate(items,1):
        name=str(x.get("dataset","")).strip()
        if not name: raise ValueError(f"item {i}.dataset is required")
        rows=x.get("rows"); nulls=x.get("null_rows",0); duplicates=x.get("duplicate_rows",0)
        if not isinstance(rows,int) or rows<=0: raise ValueError(f"item {i}.rows must be positive")
        if not all(isinstance(v,int) and 0<=v<=rows for v in (nulls,duplicates)): raise ValueError(f"item {i} quality counts are invalid")
        null_rate=nulls/rows; duplicate_rate=duplicates/rows
        if null_rate>x.get("max_null_rate",0): findings.append({"code":"null_rate_exceeded","severity":"high","item":i,"message":f"{name} null rate is {null_rate:.2%}."})
        if duplicate_rate>x.get("max_duplicate_rate",0): findings.append({"code":"duplicate_rate_exceeded","severity":"high","item":i,"message":f"{name} duplicate rate is {duplicate_rate:.2%}."})
        if rows<x.get("min_rows",1): findings.append({"code":"volume_below_minimum","severity":"medium","item":i,"message":f"{name} has only {rows} rows."})
    return {"healthy":not findings,"items_checked":len(items),"findings":findings}
if __name__=="__main__":
 p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text())); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)
