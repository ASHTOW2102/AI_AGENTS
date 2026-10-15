"""Compare baseline and current numerical feature summaries."""
import argparse,json,math
from pathlib import Path
def analyze(items,z_limit=3.0):
    findings=[]
    for i,x in enumerate(items,1):
        name=str(x.get("feature","")).strip()
        if not name: raise ValueError(f"item {i}.feature is required")
        mean=x.get("baseline_mean"); current=x.get("current_mean"); std=x.get("baseline_std")
        if not all(isinstance(v,(int,float)) and math.isfinite(v) for v in (mean,current,std)) or std<0: raise ValueError(f"item {i} statistics are invalid")
        if std==0:
            if current!=mean: findings.append({"code":"constant_feature_changed","severity":"high","item":i,"message":f"{name} changed from a constant baseline."})
        elif abs(current-mean)/std>z_limit: findings.append({"code":"mean_drift","severity":"high","item":i,"message":f"{name} mean shifted by {abs(current-mean)/std:.2f} standard deviations."})
        missing=x.get("current_missing_rate",0)
        if not 0<=missing<=1: raise ValueError(f"item {i}.current_missing_rate is invalid")
        if missing>x.get("max_missing_rate",.05): findings.append({"code":"missingness_drift","severity":"medium","item":i,"message":f"{name} missing rate is {missing:.2%}."})
    return {"healthy":not findings,"items_checked":len(items),"findings":findings}
if __name__=="__main__":
 p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text())); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)
