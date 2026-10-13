"""Audit CORS policy exports without contacting live services."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def analyze(policies: list[dict]) -> dict:
    findings = []
    for i, p in enumerate(policies, 1):
        origin = str(p.get("origin", "")).strip()
        if not origin: raise ValueError(f"item {i}.origin is required")
        credentials = bool(p.get("allow_credentials", False))
        methods = {str(x).upper() for x in p.get("methods", [])}
        headers = {str(x).lower() for x in p.get("headers", [])}
        if origin == "*" and credentials: findings.append({"code":"wildcard_credentials","severity":"critical","item":i,"message":"Wildcard origin is combined with credentials."})
        if origin == "*": findings.append({"code":"wildcard_origin","severity":"high","item":i,"message":"Any website may call this resource."})
        if "*" in headers: findings.append({"code":"wildcard_headers","severity":"medium","item":i,"message":"All request headers are accepted."})
        if methods & {"PUT", "PATCH", "DELETE"} and not credentials: findings.append({"code":"anonymous_mutation","severity":"high","item":i,"message":"Mutation methods are exposed without credential protection."})
    return {"healthy":not findings,"items_checked":len(policies),"findings":findings}

if __name__ == "__main__":
    a=argparse.ArgumentParser(); a.add_argument("input"); ns=a.parse_args()
    report=analyze(json.loads(Path(ns.input).read_text(encoding="utf-8")))
    print(json.dumps(report, indent=2)); raise SystemExit(0 if report["healthy"] else 2)
