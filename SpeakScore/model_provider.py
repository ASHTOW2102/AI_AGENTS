"""
Single place that decides which LLM backend the scoring agent talks to.
Same pattern as the DocBrief project: everything else calls get_model() and
never imports a provider SDK directly. Switch providers via MODEL_PROVIDER
in .env - no other code changes needed.
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
