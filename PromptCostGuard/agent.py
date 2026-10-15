"""Estimate prompt-run cost from supplied token prices and enforce budgets."""
import argparse,json
from pathlib import Path
def analyze(items):
    findings=[]; total=0.0
    for i,x in enumerate(items,1):
        name=str(x.get("name","")).strip()
        if not name: raise ValueError(f"item {i}.name is required")
        values=[x.get(k) for k in ("input_tokens","output_tokens","input_cost_per_million","output_cost_per_million","runs_per_day","daily_budget")]
        if not all(isinstance(v,(int,float)) and v>=0 for v in values): raise ValueError(f"item {i} contains invalid numeric values")
        cost=((values[0]*values[2]+values[1]*values[3])/1_000_000)*values[4]; total+=cost
        if cost>values[5]: findings.append({"code":"daily_budget_exceeded","severity":"high","item":i,"message":f"{name} estimates {cost:.4f} per day."})
        if values[1]>values[0]*2 and values[1]>1000: findings.append({"code":"large_output_ratio","severity":"medium","item":i,"message":f"{name} output tokens dominate input."})
    return {"healthy":not findings,"items_checked":len(items),"estimated_daily_cost":round(total,6),"findings":findings}
if __name__=="__main__":
 p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text())); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)
