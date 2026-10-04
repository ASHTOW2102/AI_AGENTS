from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class FileRisk:
    path: str
    coverage_percent: float
    missing_lines: int
    missing_branches: int
    risk_score: float
    reasons: list[str]


@dataclass(frozen=True)
class CoverageReport:
    valid: bool
    total_percent: float
    threshold: float
    files_analyzed: int
    priorities: list[FileRisk]
    recommendations: list[str]
    explanation: str = ""
    mode: str = "local"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _number(value: Any, label: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be numeric")
    return float(value)


def prioritize_coverage(
    payload: dict[str, Any],
    *,
    threshold: float = 80.0,
    top: int = 10,
) -> CoverageReport:
    if not isinstance(payload, dict):
        raise ValueError("coverage report must be a JSON object")
    if not 0 <= threshold <= 100:
        raise ValueError("threshold must be between 0 and 100")
    if top < 1:
        raise ValueError("top must be at least 1")

    files = payload.get("files")
    totals = payload.get("totals")
    if not isinstance(files, dict) or not isinstance(totals, dict):
        raise ValueError("coverage.py JSON must contain files and totals objects")

    total_percent = _number(
        totals.get("percent_covered", totals.get("percent_covered_display")),
        "totals.percent_covered",
    )
    priorities: list[FileRisk] = []

    for path, item in files.items():
        if not isinstance(path, str) or not isinstance(item, dict):
            raise ValueError("each files entry must map a path to an object")
        summary = item.get("summary")
        if not isinstance(summary, dict):
            raise ValueError(f"{path}: summary is required")

        covered = int(_number(summary.get("covered_lines", 0), f"{path}.covered_lines"))
        missing = int(_number(summary.get("missing_lines", 0), f"{path}.missing_lines"))
        excluded = int(_number(summary.get("excluded_lines", 0), f"{path}.excluded_lines"))
        missing_branches = int(
            _number(summary.get("missing_branches", 0), f"{path}.missing_branches")
        )
        num_statements = covered + missing
        percent = (
            _number(summary["percent_covered"], f"{path}.percent_covered")
            if "percent_covered" in summary
            else (100.0 * covered / num_statements if num_statements else 100.0)
        )

        reasons: list[str] = []
        if num_statements and covered == 0:
            reasons.append("zero line coverage")
        if percent < threshold:
            reasons.append(f"below {threshold:g}% target")
        if missing_branches:
            reasons.append(f"{missing_branches} missing branches")
        if excluded > max(5, num_statements // 4):
            reasons.append("large excluded-line count")

        if not reasons:
            continue

        deficit = max(0.0, threshold - percent)
        size_weight = min(num_statements, 500) / 50.0
        score = round(
            deficit
            + min(missing, 200) * 0.35
            + min(missing_branches, 100) * 0.75
            + size_weight
            + (25.0 if num_statements and covered == 0 else 0.0),
            2,
        )
        priorities.append(
            FileRisk(path, round(percent, 2), missing, missing_branches, score, reasons)
        )

    priorities.sort(key=lambda item: (-item.risk_score, item.path))
    priorities = priorities[:top]

    recommendations: list[str] = []
    if total_percent < threshold:
        recommendations.append(
            f"Raise total coverage from {total_percent:.2f}% to at least {threshold:.2f}%."
        )
    if any("zero line coverage" in item.reasons for item in priorities):
        recommendations.append("Start with executable files that currently have zero coverage.")
    if any(item.missing_branches for item in priorities):
        recommendations.append("Add boundary and failure-path tests for missing branches.")
    if priorities:
        recommendations.append("Work through the ranked file list, highest risk score first.")

    return CoverageReport(
        valid=total_percent >= threshold and not priorities,
        total_percent=round(total_percent, 2),
        threshold=threshold,
        files_analyzed=len(files),
        priorities=priorities,
        recommendations=recommendations,
    )


class CoverageCompassAgent:
    def __init__(self, use_model: bool = True) -> None:
        self.use_model = use_model

    def inspect(
        self,
        payload: dict[str, Any],
        *,
        threshold: float = 80.0,
        top: int = 10,
    ) -> CoverageReport:
        report = prioritize_coverage(payload, threshold=threshold, top=top)
        if not self.use_model or not os.getenv("OPENAI_API_KEY"):
            return report

        try:
            from openai import OpenAI

            safe_payload = {
                "total_percent": report.total_percent,
                "threshold": report.threshold,
                "priorities": [asdict(item) for item in report.priorities],
                "recommendations": report.recommendations,
            }
            response = OpenAI().responses.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                input=(
                    "Turn this sanitized coverage risk report into a concise test plan. "
                    "Do not invent code behavior.\n" + json.dumps(safe_payload)
                ),
            )
            return CoverageReport(
                report.valid,
                report.total_percent,
                report.threshold,
                report.files_analyzed,
                report.priorities,
                report.recommendations,
                response.output_text.strip(),
                "openai",
            )
        except Exception:
            return report
