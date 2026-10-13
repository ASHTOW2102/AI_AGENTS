from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from typing import Any

DESTRUCTIVE = {"drop_table", "drop_column", "truncate", "rename_column"}
LOCKING = {"alter_column", "add_index", "drop_index", "add_foreign_key"}

@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    migration: str
    message: str

@dataclass(frozen=True)
class MigrationReport:
    safe: bool
    migrations_checked: int
    findings: list[Finding]
    recommendations: list[str]
    explanation: str = ""
    mode: str = "local"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

def audit_migrations(migrations: list[dict[str, Any]]) -> MigrationReport:
    if not isinstance(migrations, list) or not migrations:
        raise ValueError("migrations must be a non-empty JSON array")
    findings: list[Finding] = []
    seen: set[str] = set()
    for index, migration in enumerate(migrations, 1):
        if not isinstance(migration, dict):
            raise ValueError(f"migration {index} must be an object")
        migration_id = str(migration.get("id", "")).strip()
        operation = str(migration.get("operation", "")).strip().lower()
        owner = str(migration.get("owner", "")).strip()
        if not migration_id or not operation:
            raise ValueError(f"migration {index} requires id and operation")
        if migration_id in seen:
            findings.append(Finding("duplicate_id", "critical", migration_id, "Migration ID appears more than once."))
        seen.add(migration_id)
        estimated_lock = migration.get("estimated_lock_seconds", 0)
        if not isinstance(estimated_lock, (int, float)) or isinstance(estimated_lock, bool) or estimated_lock < 0:
            raise ValueError(f"{migration_id}.estimated_lock_seconds must be non-negative")
        if operation in DESTRUCTIVE:
            findings.append(Finding("destructive_operation", "critical", migration_id, f"{operation} can remove or invalidate data."))
        if operation in LOCKING and estimated_lock > 5:
            findings.append(Finding("lock_risk", "high", migration_id, f"Estimated lock time {estimated_lock:g}s exceeds 5s."))
        if migration.get("rollback_available") is not True:
            findings.append(Finding("missing_rollback", "high", migration_id, "No tested rollback is declared."))
        if migration.get("tested_on_copy") is not True:
            findings.append(Finding("untested_migration", "high", migration_id, "Migration was not tested on a production-like copy."))
        if not owner:
            findings.append(Finding("missing_owner", "medium", migration_id, "Migration has no accountable owner."))
        if migration.get("online") is not True and operation in LOCKING:
            findings.append(Finding("offline_change", "medium", migration_id, "Potentially locking change is not marked online."))

    codes = sorted({finding.code for finding in findings})
    recommendations = (
        ["Resolve before rollout: " + ", ".join(codes) + ".", "Back up affected data and rehearse rollback before production."]
        if findings else ["Migration metadata passes the configured safety checks."]
    )
    return MigrationReport(not findings, len(migrations), findings, recommendations)

class MigrationGuardAgent:
    def __init__(self, use_model: bool = True) -> None:
        self.use_model = use_model

    def inspect(self, migrations: list[dict[str, Any]]) -> MigrationReport:
        report = audit_migrations(migrations)
        if not self.use_model or not os.getenv("OPENAI_API_KEY"):
            return report
        try:
            from openai import OpenAI
            safe = {"findings": [asdict(item) for item in report.findings], "recommendations": report.recommendations}
            response = OpenAI().responses.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                input="Explain this sanitized database migration audit. Do not invent schema details.\n" + json.dumps(safe),
            )
            return MigrationReport(report.safe, report.migrations_checked, report.findings, report.recommendations, response.output_text.strip(), "openai")
        except Exception:
            return report
