import os

from dotenv import load_dotenv

from agents import (
    Agent,
    Runner,
    AsyncOpenAI,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)

from tools.govuk import search_govuk, fetch_govuk_page
from tools.calculator import calculate


# Load .env
load_dotenv()


# --------------------------------------------------
# Configuration
# --------------------------------------------------

MODEL_PROVIDER = os.getenv("MODEL_PROVIDER", "ollama").lower()

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434/v1",
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "gpt-oss:20b",
)

OLLAMA_API_KEY = os.getenv(
    "OLLAMA_API_KEY",
    "ollama",
)


# --------------------------------------------------
# Agent instructions
# --------------------------------------------------

INSTRUCTIONS = """
You are the UK Housing & Renting Assistant.

Your job is to help people with everyday housing and
private-renting problems in the United Kingdom.

LANGUAGE
- Understand English, Hindi and Hinglish.
- If the user writes in Hinglish, answer naturally in Hinglish.
- If the user writes in Hindi, answer in Hindi.
- If the user writes in English, answer in English.
- Keep explanations simple and practical.

UK JURISDICTION
- Housing law differs between England, Scotland, Wales and
  Northern Ireland.
- Do not assume that an England rule applies everywhere in the UK.
- If the nation matters and the user has not specified it,
  ask which UK nation they are in.
- If the user clearly says England, use England-specific information.

CURRENT INFORMATION
- For legal, procedural, deadline, rent, deposit, eviction,
  notice, eligibility or government-service questions,
  use the GOV.UK tools whenever possible.
- Prefer official government information.
- Never invent a legal rule, deadline, fee or entitlement.
- If information is uncertain, say so clearly.

SAFETY
- You provide general information, not legal representation.
- For urgent homelessness, domestic abuse, immediate danger,
  serious hazards or court matters, recommend appropriate
  professional or official help.
- Never tell someone to ignore a legal notice, court document
  or official deadline.

ANSWER STYLE
- Start with the direct answer.
- Then give a numbered action plan when useful.
- Explain complicated housing terms in simple language.
- Mention what additional information would change the answer.
- If GOV.UK sources were used, provide a Sources section.
"""


# --------------------------------------------------
# Build Ollama model
# --------------------------------------------------

def build_model():

    if MODEL_PROVIDER != "ollama":
        raise RuntimeError(
            "This project is configured to use Ollama. "
            "Set MODEL_PROVIDER=ollama in your .env file."
        )

    # We don't need OpenAI tracing for a local Ollama setup.
    set_tracing_disabled(disabled=True)

    client = AsyncOpenAI(
        base_url=OLLAMA_BASE_URL,
        api_key=OLLAMA_API_KEY,
    )

    model = OpenAIChatCompletionsModel(
        model=OLLAMA_MODEL,
        openai_client=client,
    )

    return model


# --------------------------------------------------
# Create model
# --------------------------------------------------

model = build_model()


# --------------------------------------------------
# Create housing agent
# --------------------------------------------------

housing_agent = Agent(
    name="UK Housing & Renting Assistant",

    instructions=INSTRUCTIONS,

    model=model,

    tools=[
        search_govuk,
        fetch_govuk_page,
        calculate,
    ],
)


# --------------------------------------------------
# Run agent
# --------------------------------------------------

def run_agent(user_message: str) -> str:

    try:

        result = Runner.run_sync(
            housing_agent,
            user_message,
            max_turns=8,
        )

        return str(result.final_output)

    except Exception as exc:

        return (
            "Sorry, agent run mein problem aa gayi.\n\n"
            f"Technical error:\n"
            f"`{type(exc).__name__}: {exc}`\n\n"
            "Please check:\n"
            "1. Ollama is running\n"
            "2. The Ollama model exists\n"
            "3. Your .env configuration is correct"
        )
