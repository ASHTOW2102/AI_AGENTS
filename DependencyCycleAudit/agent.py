"""Detect service dependency cycles and missing references."""
import argparse,json
from pathlib import Path
def analyze(graph):
    if not isinstance(graph,dict) or not graph: raise ValueError("graph must be a non-empty object")
    findings=[]; state={}; stack=[]
    for node,deps in graph.items():
        if not isinstance(deps,list): raise ValueError(f"{node} dependencies must be an array")
        for dep in deps:
            if dep not in graph: findings.append({"code":"missing_service","severity":"high","item":node,"message":f"{node} references unknown service {dep}."})
    def visit(node):
        state[node]=1; stack.append(node)
        for dep in graph[node]:
            if dep not in graph: continue
            if state.get(dep)==1:
                cycle=stack[stack.index(dep):]+[dep]; findings.append({"code":"dependency_cycle","severity":"high","item":node,"message":" -> ".join(cycle)})
            elif not state.get(dep): visit(dep)
        stack.pop(); state[node]=2
    for node in graph:
        if not state.get(node): visit(node)
    return {"healthy":not findings,"items_checked":len(graph),"findings":findings}
if __name__=="__main__":
 p=argparse.ArgumentParser(); p.add_argument("input"); n=p.parse_args(); r=analyze(json.loads(Path(n.input).read_text())); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["healthy"] else 2)
