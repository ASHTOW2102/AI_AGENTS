from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    path: str
    message: str


@dataclass(frozen=True)
class CacheReport:
    valid: bool
    responses: int
    findings: list[Finding]
    recommendations: list[str]
    explanation: str = ""
    mode: str = "local"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _directives(value: str) -> dict[str, str | None]:
    result: dict[str, str | None] = {}
    for part in value.lower().split(","):
        item = part.strip()
        if not item:
            continue
        name, separator, raw = item.partition("=")
        result[name.strip()] = raw.strip().strip('"') if separator else None
    return result


def audit_cache(responses: list[dict[str, Any]]) -> CacheReport:
    if not isinstance(responses, list) or not responses:
        raise ValueError("responses must be a non-empty JSON array")

    findings: list[Finding] = []
    for index, response in enumerate(responses, start=1):
        if not isinstance(response, dict):
            raise ValueError(f"response {index} must be an object")
        path = str(response.get("path", "")).strip()
        method = str(response.get("method", "GET")).upper().strip()
        status = response.get("status")
        cache_control = response.get("cache_control", "")
        vary = response.get("vary", "")
        if not path.startswith("/"):
            raise ValueError(f"response {index}.path must start with /")
        if method not in {"GET", "HEAD"}:
            raise ValueError(f"response {index}.method must be GET or HEAD")
        if isinstance(status, bool) or not isinstance(status, int) or not 100 <= status <= 599:
            raise ValueError(f"response {index}.status must be an HTTP status")
        if not isinstance(cache_control, str) or not isinstance(vary, str):
            raise ValueError(f"response {index} cache_control and vary must be strings")
        for flag in ("sensitive", "request_authenticated", "response_sets_cookie", "static_asset"):
            if flag in response and not isinstance(response[flag], bool):
                raise ValueError(f"response {index}.{flag} must be a boolean")

        directives = _directives(cache_control)
        public = "public" in directives or "s-maxage" in directives
        private = "private" in directives
        no_store = "no-store" in directives
        has_ttl = "max-age" in directives or "s-maxage" in directives
        cacheable = has_ttl and not no_store
        vary_names = {item.strip().lower() for item in vary.split(",") if item.strip()}

        if status < 400 and not cache_control.strip():
            findings.append(
                Finding(
                    "missing_cache_control",
                    "medium",
                    path,
                    "Successful response has no explicit Cache-Control policy.",
                )
            )

        conflicts: list[str] = []
        if public and private:
            conflicts.append("public with private")
        if no_store and has_ttl:
            conflicts.append("no-store with a cache lifetime")
        if conflicts:
            findings.append(
                Finding(
                    "conflicting_directives",
                    "high",
                    path,
                    "Cache-Control combines " + " and ".join(conflicts) + ".",
                )
            )

        if response.get("sensitive") and not no_store:
            findings.append(
                Finding(
                    "sensitive_response_storable",
                    "critical",
                    path,
                    "Sensitive response is not protected by no-store.",
                )
            )

        if response.get("request_authenticated") and public:
            findings.append(
                Finding(
                    "authenticated_shared_cache",
                    "critical",
                    path,
                    "Authenticated response permits shared caching.",
                )
            )

        if response.get("request_authenticated") and cacheable and "authorization" not in vary_names and not private:
            findings.append(
                Finding(
                    "missing_vary_authorization",
                    "high",
                    path,
                    "Cacheable authenticated response does not vary on Authorization.",
                )
            )

        if response.get("response_sets_cookie") and public:
            findings.append(
                Finding(
                    "cookie_response_public",
                    "critical",
                    path,
                    "A response that sets a cookie permits shared caching.",
                )
            )

        if "immutable" in directives and not response.get("static_asset"):
            findings.append(
                Finding(
                    "immutable_dynamic_response",
                    "medium",
                    path,
                    "A non-static response is marked immutable.",
                )
            )

        if response.get("static_asset") and not has_ttl:
            findings.append(
                Finding(
                    "static_asset_without_ttl",
                    "low",
                    path,
                    "Static asset has no max-age or s-maxage directive.",
                )
            )

    codes = {item.code for item in findings}
    recommendations: list[str] = []
    if {"sensitive_response_storable", "authenticated_shared_cache", "cookie_response_public"} & codes:
        recommendations.append("Use private, no-store policies for sensitive or user-specific responses.")
    if {"conflicting_directives", "missing_cache_control"} & codes:
        recommendations.append("Set one explicit, internally consistent Cache-Control policy per response.")
    if "missing_vary_authorization" in codes:
        recommendations.append("Keep authenticated content private or vary shared cache keys on Authorization.")
    if "immutable_dynamic_response" in codes:
        recommendations.append("Reserve immutable for content-addressed static assets.")
    if "static_asset_without_ttl" in codes:
        recommendations.append("Give versioned static assets a deliberate cache lifetime.")
    if not findings:
        recommendations.append("The supplied response metadata passes the configured cache-safety checks.")

    return CacheReport(not findings, len(responses), findings, recommendations)


class CacheGuardAgent:
    def __init__(self, use_model: bool = True) -> None:
        self.use_model = use_model

    def inspect(self, responses: list[dict[str, Any]]) -> CacheReport:
        report = audit_cache(responses)
        if not self.use_model or not os.getenv("OPENAI_API_KEY"):
            return report
        try:
            from openai import OpenAI

            safe = report.to_dict()
            safe.pop("explanation", None)
            response = OpenAI().responses.create(
                model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
                input=(
                    "Explain this sanitized HTTP caching audit and propose safe header "
                    "changes. Do not invent application data.\n" + json.dumps(safe)
                ),
            )
            return CacheReport(
                report.valid,
                report.responses,
                report.findings,
                report.recommendations,
                response.output_text.strip(),
                "openai",
            )
        except Exception:
            return report
