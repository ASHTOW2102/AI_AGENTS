"""
Single place that decides which LLM backend the agent talks to.

Everything else in this project (summarizer_agent.py, app.py) just calls
get_model() and never imports a provider SDK directly. To switch providers -
e.g. from a local Ollama model today to OpenAI or Anthropic later - change
MODEL_PROVIDER (and the matching *_MODEL / *_API_KEY vars) in your .env file.
No other code needs to change.
"""

import os

from dotenv import load_dotenv

load_dotenv()


def get_model():
    provider = os.getenv("MODEL_PROVIDER", "ollama").lower()

    if provider == "ollama":
        from strands.models.ollama import OllamaModel

        return OllamaModel(
            host=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
            model_id=os.getenv("OLLAMA_MODEL", "llama3.1"),
            temperature=float(os.getenv("MODEL_TEMPERATURE", "0.3")),
        )

    if provider == "openai":
        from strands.models.openai import OpenAIModel

        return OpenAIModel(
            client_args={"api_key": os.getenv("OPENAI_API_KEY")},
            model_id=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            params={"temperature": float(os.getenv("MODEL_TEMPERATURE", "0.3"))},
        )

    if provider == "anthropic":
        from strands.models.anthropic import AnthropicModel

        return AnthropicModel(
            client_args={"api_key": os.getenv("ANTHROPIC_API_KEY")},
            model_id=os.getenv("ANTHROPIC_MODEL", "claude-sonnet-5"),
            max_tokens=int(os.getenv("MODEL_MAX_TOKENS", "2048")),
            params={"temperature": float(os.getenv("MODEL_TEMPERATURE", "0.3"))},
        )

    if provider == "huggingface":
        # Uses HF's free Inference Providers router (OpenAI-compatible), so
        # the deployed Space doesn't need Ollama or any GPU of its own.
        from strands.models.openai import OpenAIModel

        return OpenAIModel(
            client_args={
                "api_key": os.getenv("HF_TOKEN"),
                "base_url": "https://router.huggingface.co/v1",
            },
            model_id=os.getenv("HF_MODEL", "meta-llama/Llama-3.1-8B-Instruct"),
            params={"temperature": float(os.getenv("MODEL_TEMPERATURE", "0.3"))},
        )

    raise ValueError(
        f"Unknown MODEL_PROVIDER '{provider}'. Use one of: ollama, openai, anthropic, huggingface."
    )


def current_provider_label() -> str:
    """Human-readable description of the active provider, for the UI."""
    provider = os.getenv("MODEL_PROVIDER", "ollama").lower()
    if provider == "ollama":
        return f"Ollama · {os.getenv('OLLAMA_MODEL', 'llama3.1')} (local)"
    if provider == "openai":
        return f"OpenAI · {os.getenv('OPENAI_MODEL', 'gpt-4o-mini')}"
    if provider == "anthropic":
        return f"Anthropic · {os.getenv('ANTHROPIC_MODEL', 'claude-sonnet-5')}"
    if provider == "huggingface":
        return f"Hugging Face Inference · {os.getenv('HF_MODEL', 'meta-llama/Llama-3.1-8B-Instruct')}"
    return provider
