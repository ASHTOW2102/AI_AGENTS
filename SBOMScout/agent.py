"""Find actionable supply-chain gaps in CycloneDX-like component exports."""
from __future__ import annotations
import argparse, json
from pathlib import Path
def analyze(data: dict) -> dict:
    components=data.get("components")
    if not isinstance(components, list): raise ValueError("components must be an array")
    findings=[]
    for i,c in enumerate(components,1):
        name=str(c.get("name","")).strip(); version=str(c.get("version","")).strip()
        if not name: raise ValueError(f"component {i}.name is required")
        if not version: findings.append({"code":"missing_version","severity":"high","item":i,"message":f"{name} has no pinned version."})
        if not c.get("purl"): findings.append({"code":"missing_purl","severity":"medium","item":i,"message":f"{name} has no package URL."})
        if not c.get("licenses",[]): findings.append({"code":"missing_license","severity":"medium","item":i,"message":f"{name} has no license evidence."})
        if str(c.get("scope","")).lower()=="required" and not c.get("hashes"): findings.append({"code":"missing_hash","severity":"high","item":i,"message":f"Required component {name} has no integrity hash."})
    return {"healthy":not findings,"items_checked":len(components),"findings":findings}
if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text()))
    print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)
