"""Compare outcome rates across supplied demographic groups."""
import argparse,json
from pathlib import Path
def analyze(groups, threshold=.8):
    if len(groups)<2: raise ValueError("at least two groups are required")
    rates=[]; out=[]
    for i,g in enumerate(groups,1):
        total=g.get("total"); positive=g.get("positive")
        if not isinstance(total,int) or total<=0 or not isinstance(positive,int) or not 0<=positive<=total: raise ValueError(f"group {i} counts are invalid")
        rates.append((i,str(g.get("name",i)),positive/total))
    best=max(r[2] for r in rates)
    for i,name,rate in rates:
        ratio=rate/best if best else 1
        if ratio<threshold: out.append({"code":"selection_rate_gap","severity":"high","item":i,"message":f"{name} has impact ratio {ratio:.3f}."})
    return {"healthy":not out,"items_checked":len(groups),"findings":out,"rates":{n:round(r,4) for _,n,r in rates}}
if __name__=="__main__":
 p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text())); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)
