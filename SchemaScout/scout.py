"""CSV profiling and contract-validation agent."""

from __future__ import annotations

import csv
import io
import json
import os
from dataclasses import asdict, dataclass
from datetime import date
from typing import Any

_NULLS = {"", "null", "none", "na", "n/a"}


@dataclass(frozen=True)
class ColumnProfile:
    name: str
    inferred_type: str
    nullable: bool
    null_count: int
    unique_ratio: float
    examples: list[str]


@dataclass(frozen=True)
class ProfileReport:
    row_count: int
    columns: list[ColumnProfile]
    warnings: list[str]
    explanation: str | None = None
    mode: str = "local"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def contract(self) -> dict[str, Any]:
        return {
            "version": 1,
            "columns": {
                column.name: {
                    "type": column.inferred_type,
                    "nullable": column.nullable,
                }
                for column in self.columns
            },
        }


def _is_null(value: str) -> bool:
    return value.strip().lower() in _NULLS


def _value_type(value: str) -> str:
    value = value.strip()
    lowered = value.lower()
    if lowered in {"true", "false", "yes", "no"}:
        return "boolean"
    try:
        int(value)
        return "integer"
    except ValueError:
        pass
    try:
        float(value)
        return "number"
    except ValueError:
        pass
    try:
        date.fromisoformat(value)
        return "date"
    except ValueError:
        return "string"


def _merge_types(types: set[str]) -> str:
    if not types:
        return "string"
    if types <= {"integer"}:
        return "integer"
    if types <= {"integer", "number"}:
        return "number"
    if len(types) == 1:
        return next(iter(types))
    return "string"


def profile_csv(text: str, max_rows: int = 10_000) -> ProfileReport:
    if max_rows < 1:
        raise ValueError("max_rows must be positive")
    reader = csv.DictReader(io.StringIO(text))
    if not reader.fieldnames:
        raise ValueError("CSV must include a header")
    names = [name.strip() for name in reader.fieldnames]
    if any(not name for name in names) or len(set(names)) != len(names):
        raise ValueError("CSV headers must be non-empty and unique")

    values = {name: [] for name in names}
    for index, raw_row in enumerate(reader):
        if index >= max_rows:
            break
        row = {key.strip(): value for key, value in raw_row.items() if key is not None}
        for name in names:
            values[name].append(row.get(name, ""))

    row_count = max((len(items) for items in values.values()), default=0)
    columns: list[ColumnProfile] = []
    warnings: list[str] = []
    for name, items in values.items():
        non_null = [item.strip() for item in items if not _is_null(item)]
        null_count = len(items) - len(non_null)
        inferred = _merge_types({_value_type(item) for item in non_null})
        ratio = round(len(set(non_null)) / len(non_null), 3) if non_null else 0.0
        examples = list(dict.fromkeys(non_null))[:3]
        columns.append(ColumnProfile(name, inferred, null_count > 0, null_count, ratio, examples))
        if row_count and null_count / row_count > 0.25:
            warnings.append(f"{name}: {null_count}/{row_count} values are null")
        if inferred == "string" and len({_value_type(item) for item in non_null}) > 1:
            warnings.append(f"{name}: mixed value types were normalized to string")
    return ProfileReport(row_count, columns, warnings)


def validate_csv(text: str, contract: dict[str, Any]) -> list[str]:
    reader = csv.DictReader(io.StringIO(text))
    if not reader.fieldnames:
        return ["CSV must include a header"]
    expected = contract.get("columns", {})
    actual = set(reader.fieldnames)
    violations = [f"Missing column: {name}" for name in expected if name not in actual]
    violations += [f"Unexpected column: {name}" for name in actual if name not in expected]
    for line_number, row in enumerate(reader, start=2):
        for name, rule in expected.items():
            if name not in row:
                continue
            value = row[name]
            if _is_null(value):
                if not rule.get("nullable", False):
                    violations.append(f"Line {line_number}, {name}: null is not allowed")
                continue
            inferred = _value_type(value)
            wanted = rule.get("type", "string")
            compatible = inferred == wanted or (wanted == "number" and inferred == "integer")
            if not compatible:
                violations.append(
                    f"Line {line_number}, {name}: expected {wanted}, got {inferred}"
                )
    return violations


class SchemaScoutAgent:
    def __init__(self, use_model: bool = True) -> None:
        self.use_model = use_model

    def profile(self, text: str) -> ProfileReport:
        report = profile_csv(text)
        if not self.use_model or not os.getenv("OPENAI_API_KEY"):
            return report
        try:
            from openai import OpenAI

            response = OpenAI().responses.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                input=(
                    "You are a data-quality reviewer. Explain the three most important "
                    "risks in this CSV profile. Do not invent facts.\n"
                    + json.dumps(report.to_dict())
                ),
            )
            return ProfileReport(
                report.row_count,
                report.columns,
                report.warnings,
                response.output_text.strip(),
                "openai",
            )
        except Exception:
            return report
