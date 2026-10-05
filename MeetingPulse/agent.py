from __future__ import annotations

import json
import os
import re
from dataclasses import asdict, dataclass
from datetime import date
from typing import Any

WORD = re.compile(r"\b[\w'-]+\b", re.UNICODE)


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    subject: str
    message: str


@dataclass(frozen=True)
class MeetingReport:
    valid: bool
    participants: int
    total_words: int
    speaking_share: dict[str, float]
    findings: list[Finding]
    recommendations: list[str]
    explanation: str = ""
    mode: str = "local"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def audit_meeting(
    payload: dict[str, Any],
    *,
    dominance_threshold: float = 0.65,
    monologue_words: int = 150,
) -> MeetingReport:
    if not isinstance(payload, dict):
        raise ValueError("meeting must be a JSON object")
    if not 0.5 <= dominance_threshold <= 1:
        raise ValueError("dominance_threshold must be between 0.5 and 1")
    if monologue_words < 20:
        raise ValueError("monologue_words must be at least 20")

    declared = payload.get("participants", [])
    turns = payload.get("turns")
    actions = payload.get("actions", [])
    decisions = payload.get("decisions", [])

    if not isinstance(declared, list) or not all(
        isinstance(item, str) and item.strip() for item in declared
    ):
        raise ValueError("participants must be a list of non-empty names")
    if not isinstance(turns, list) or not turns:
        raise ValueError("turns must be a non-empty list")
    if not isinstance(actions, list) or not isinstance(decisions, list):
        raise ValueError("actions and decisions must be lists")

    names = {name.strip() for name in declared}
    words: dict[str, int] = {name: 0 for name in names}
    findings: list[Finding] = []

    for index, turn in enumerate(turns, start=1):
        if not isinstance(turn, dict):
            raise ValueError(f"turn {index} must be an object")
        speaker = str(turn.get("speaker", "")).strip()
        text = turn.get("text")
        if not speaker or not isinstance(text, str) or not text.strip():
            raise ValueError(f"turn {index} requires speaker and text")
        names.add(speaker)
        count = len(WORD.findall(text))
        words[speaker] = words.get(speaker, 0) + count

        duration = turn.get("duration_seconds")
        if duration is not None and (
            isinstance(duration, bool)
            or not isinstance(duration, (int, float))
            or duration < 0
        ):
            raise ValueError(f"turn {index}: duration_seconds must be non-negative")

        if count >= monologue_words or (
            isinstance(duration, (int, float)) and duration >= 180
        ):
            findings.append(
                Finding(
                    "long_monologue",
                    "medium",
                    speaker,
                    f"Turn {index} contains {count} words"
                    + (f" over {duration:g} seconds." if duration is not None else "."),
                )
            )

    total_words = sum(words.values())
    if total_words == 0:
        raise ValueError("turns must contain spoken words")

    shares = {
        name: round(count / total_words, 4)
        for name, count in sorted(words.items())
    }
    if len(names) >= 2:
        leader, leader_words = max(words.items(), key=lambda item: item[1])
        share = leader_words / total_words
        if share >= dominance_threshold:
            findings.append(
                Finding(
                    "dominant_speaker",
                    "medium",
                    leader,
                    f"{leader} contributed {share:.1%} of spoken words.",
                )
            )

    for name in sorted(set(declared)):
        if words.get(name, 0) == 0:
            findings.append(
                Finding(
                    "silent_participant",
                    "low",
                    name,
                    f"{name} was listed but had no recorded speaking turn.",
                )
            )

    for index, action in enumerate(actions, start=1):
        if not isinstance(action, dict):
            raise ValueError(f"action {index} must be an object")
        task = str(action.get("task", "")).strip()
        if not task:
            raise ValueError(f"action {index}: task is required")
        owner = str(action.get("owner", "")).strip()
        due = str(action.get("due_date", "")).strip()
        if not owner:
            findings.append(
                Finding(
                    "missing_action_owner",
                    "high",
                    task,
                    f"Action {index} has no owner.",
                )
            )
        if not due:
            findings.append(
                Finding(
                    "missing_action_deadline",
                    "medium",
                    task,
                    f"Action {index} has no due date.",
                )
            )
        else:
            try:
                date.fromisoformat(due)
            except ValueError:
                raise ValueError(f"action {index}: due_date must be an ISO date") from None

    if not decisions:
        findings.append(
            Finding(
                "no_recorded_decision",
                "medium",
                "meeting",
                "No decisions were recorded.",
            )
        )
    elif not all(isinstance(item, str) and item.strip() for item in decisions):
        raise ValueError("decisions must contain non-empty strings")

    codes = {item.code for item in findings}
    recommendations: list[str] = []
    if {"dominant_speaker", "silent_participant", "long_monologue"} & codes:
        recommendations.append("Use timed rounds or direct invitations to balance participation.")
    if {"missing_action_owner", "missing_action_deadline"} & codes:
        recommendations.append("Give every action one accountable owner and an ISO due date.")
    if "no_recorded_decision" in codes:
        recommendations.append("Close by recording explicit decisions or stating that none were made.")
    if not findings:
        recommendations.append("Participation, decisions, and action ownership meet the configured checks.")

    return MeetingReport(
        valid=not findings,
        participants=len(names),
        total_words=total_words,
        speaking_share=shares,
        findings=findings,
        recommendations=recommendations,
    )


class MeetingPulseAgent:
    def __init__(self, use_model: bool = True) -> None:
        self.use_model = use_model

    def inspect(
        self,
        payload: dict[str, Any],
        *,
        dominance_threshold: float = 0.65,
        monologue_words: int = 150,
    ) -> MeetingReport:
        report = audit_meeting(
            payload,
            dominance_threshold=dominance_threshold,
            monologue_words=monologue_words,
        )
        if not self.use_model or not os.getenv("OPENAI_API_KEY"):
            return report

        try:
            from openai import OpenAI

            safe_payload = report.to_dict()
            safe_payload.pop("explanation", None)
            response = OpenAI().responses.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                input=(
                    "Suggest inclusive meeting improvements from these aggregate, "
                    "sanitized metrics. Do not infer personalities or sensitive traits.\n"
                    + json.dumps(safe_payload)
                ),
            )
            return MeetingReport(
                report.valid,
                report.participants,
                report.total_words,
                report.speaking_share,
                report.findings,
                report.recommendations,
                response.output_text.strip(),
                "openai",
            )
        except Exception:
            return report
