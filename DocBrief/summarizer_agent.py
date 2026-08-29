"""
The actual Strands agent. Model-agnostic: it asks model_provider.get_model()
for whichever backend is configured and knows nothing about Ollama/OpenAI/etc.
"""

from strands import Agent

from model_provider import get_model

SYSTEM_PROMPT = (
    "You are a precise, neutral document summarizer. Summarize only what is "
    "in the provided text - never invent facts, names, or numbers that are "
    "not present. Preserve key figures, decisions, and action items."
)

STYLE_INSTRUCTIONS = {
    "concise": "Write a concise summary in 3-5 sentences.",
    "detailed": (
        "Write a thorough, well-organized summary covering all major points, "
        "in a few short paragraphs."
    ),
    "bullets": "Summarize as a clean bulleted list of the key points.",
}

# Keeps each request comfortably inside small local-model context windows.
_CHUNK_CHARS = 6000


def _fresh_agent() -> Agent:
    # A new Agent per call keeps each request stateless (no growing chat
    # history), which matters for local models with small context windows.
    return Agent(model=get_model(), system_prompt=SYSTEM_PROMPT)


def _chunk(text: str, size: int = _CHUNK_CHARS) -> list[str]:
    return [text[i : i + size] for i in range(0, len(text), size)]


def summarize(text: str, style: str = "concise") -> str:
    text = text.strip()
    if not text:
        raise ValueError("No text to summarize.")

    instructions = STYLE_INSTRUCTIONS.get(style, STYLE_INSTRUCTIONS["concise"])
    chunks = _chunk(text)

    if len(chunks) == 1:
        result = _fresh_agent()(f"{instructions}\n\nDocument:\n\n{chunks[0]}")
        return str(result)

    # Long document: map (summarize each chunk) then reduce (merge summaries).
    partial_summaries = []
    for i, chunk in enumerate(chunks, start=1):
        result = _fresh_agent()(
            f"This is part {i} of {len(chunks)} of a longer document. "
            f"Summarize the key points of this part only.\n\nPart:\n\n{chunk}"
        )
        partial_summaries.append(str(result))

    combined = "\n\n".join(partial_summaries)
    final = _fresh_agent()(
        f"{instructions}\n\nBelow are summaries of consecutive parts of one "
        f"document, in order. Combine them into a single coherent summary of "
        f"the whole document.\n\n{combined}"
    )
    return str(final)
