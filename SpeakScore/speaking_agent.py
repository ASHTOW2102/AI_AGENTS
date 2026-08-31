"""
Strands agent that scores spoken-language performance from a transcript.

Important honesty constraint: we only have text (from Whisper) plus timing,
never the actual audio, so this can score fluency/pacing, grammar,
vocabulary, and coherence - but it cannot judge pronunciation or accent.
The system prompt is written to make the model say so rather than bluff it.
"""

import json

from strands import Agent

from model_provider import get_model

SYSTEM_PROMPT = """You are an encouraging but honest language-speaking coach.

You are given the language the speaker intended to practice, a transcript of
what they said (from speech-to-text - it may contain minor transcription
errors, don't penalize obvious STT artifacts), and their speaking pace in
words per minute.

You have no access to the actual audio, so you CANNOT judge accent,
pronunciation, or intonation - never claim to. Score only what the
transcript and pace can tell you: fluency/pacing, grammar, vocabulary, and
coherence.

Return ONLY valid JSON, no markdown fences, no extra commentary, matching
exactly this shape:
{
  "overall_score": <integer 0-100>,
  "estimated_level": "<CEFR-style estimate, e.g. 'B1 (Intermediate)'>",
  "fluency_pacing": {"score": <0-100>, "comment": "<one sentence>"},
  "grammar": {"score": <0-100>, "comment": "<one sentence>"},
  "vocabulary": {"score": <0-100>, "comment": "<one sentence>"},
  "coherence": {"score": <0-100>, "comment": "<one sentence>"},
  "corrections": ["<original phrase> -> <corrected phrase>", "..."],
  "tips": ["<short actionable tip>", "..."]
}
Include at most 3 corrections and 3 tips. If there's nothing to correct, use an empty list.
"""


def _fresh_agent() -> Agent:
    return Agent(model=get_model(), system_prompt=SYSTEM_PROMPT)


def score_speaking(language: str, transcript: str, words_per_minute: float | None) -> dict:
    transcript = transcript.strip()
    if not transcript:
        raise ValueError("No speech was detected in the recording.")

    pace_line = (
        f"Speaking pace: {words_per_minute:.0f} words per minute"
        if words_per_minute
        else "Speaking pace: unavailable"
    )
    prompt = f"Target language: {language}\n{pace_line}\nTranscript:\n{transcript}"

    raw = str(_fresh_agent()(prompt)).strip()
    if raw.startswith("```"):
        raw = raw.strip("`")
        if raw.lower().startswith("json"):
            raw = raw[4:]
        raw = raw.strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {"raw": raw}
