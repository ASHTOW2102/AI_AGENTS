"""
Speech-to-text via Hugging Face's Inference Providers (Whisper). Used for
both local dev and the deployed Space - HF gives a free monthly inference
credit allowance, and unlike an LLM chat model, ASR isn't something Ollama
does, so there's no local-first option here the way there is for the score.
"""

import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

_ASR_MODEL = "openai/whisper-large-v3"


def transcribe_audio(audio_path: str) -> str:
    token = os.getenv("HF_TOKEN")
    if not token:
        raise RuntimeError(
            "HF_TOKEN is required for speech-to-text (Hugging Face Inference "
            "Providers), even if MODEL_PROVIDER for scoring is set to something else."
        )
    client = InferenceClient(token=token)
    result = client.automatic_speech_recognition(audio_path, model=_ASR_MODEL)
    return result.text.strip()
