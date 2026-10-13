"""Audit CI workflow inventory for least privilege and reproducibility."""
import argparse,json,re
from pathlib import Path
SHA=re.compile(r"^[0-9a-f]{40}$")
def analyze(jobs):
    out=[]
    for i,j in enumerate(jobs,1):
        name=str(j.get("name","")).strip()
        if not name: raise ValueError(f"job {i}.name is required")
        if str(j.get("permissions","")).lower() in {"write-all","admin"}: out.append({"code":"broad_permissions","severity":"high","item":i,"message":f"{name} has broad permissions."})
        if j.get("pull_request_target") and j.get("runs_untrusted_code"): out.append({"code":"untrusted_privileged_code","severity":"critical","item":i,"message":f"{name} runs untrusted code with target privileges."})
        for action in j.get("actions",[]):
            ref=str(action).rsplit("@",1)[-1]
            if not SHA.fullmatch(ref): out.append({"code":"unpinned_action","severity":"medium","item":i,"message":f"{action} is not pinned to a commit SHA."})
    return {"healthy":not out,"items_checked":len(jobs),"findings":out}
if __name__=="__main__":
 p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text())); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)
