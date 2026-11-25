"""Flags feature flag configurations where flags depend on each other in a cycle, making it impossible to enable any of them cleanly."""
from typing import Any


def audit(flags: dict[str, Any]) -> list[dict[str, str]]:
    findings = []
    dependencies = flags.get("dependencies", {})

    def has_cycle(node, visiting, visited):
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for dep in dependencies.get(node, []):
            if has_cycle(dep, visiting, visited):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    visited: set = set()
    for flag in dependencies:
        if flag not in visited and has_cycle(flag, set(), visited):
            findings.append({"severity": "high", "issue": f"Feature flag dependency graph contains a cycle involving '{flag}'."})
            break
    return findings
