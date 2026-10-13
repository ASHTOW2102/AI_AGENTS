"""Summarise high-risk actions in Terraform plan JSON."""
from __future__ import annotations
import argparse, json
from pathlib import Path
def analyze(plan: dict) -> dict:
    changes=plan.get("resource_changes")
    if not isinstance(changes,list): raise ValueError("resource_changes must be an array")
    findings=[]; sensitive=("database","db_instance","bucket","kms","iam","firewall","security_group")
    for i,r in enumerate(changes,1):
        address=str(r.get("address","")).strip(); actions=r.get("change",{}).get("actions",[])
        if not address: raise ValueError(f"resource {i}.address is required")
        if "delete" in actions and "create" not in actions: findings.append({"code":"destructive_delete","severity":"critical","item":i,"message":f"{address} will be deleted."})
        if actions==["delete","create"]: findings.append({"code":"replacement","severity":"high","item":i,"message":f"{address} requires replacement."})
        if any(x in address.lower() for x in sensitive) and any(x in actions for x in ("delete","update")): findings.append({"code":"sensitive_change","severity":"high","item":i,"message":f"Sensitive resource {address} will change."})
    return {"healthy":not findings,"items_checked":len(changes),"findings":findings}
if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text()))
    print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)
