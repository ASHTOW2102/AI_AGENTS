import gradio as gr

from agent import run_agent


def chat(message, history):
    history = history or []

    transcript = []

    for item in history:

        if isinstance(item, dict):

            role = item.get("role", "")
            content = item.get("content", "")

            if isinstance(content, str) and content.strip():
                transcript.append(
                    f"{role.title()}: {content}"
                )

        elif isinstance(item, (list, tuple)):

            if len(item) >= 2:

                if item[0]:
                    transcript.append(
                        f"User: {item[0]}"
                    )

                if item[1]:
                    transcript.append(
                        f"Assistant: {item[1]}"
                    )

    if transcript:

        prompt = (
            "Previous conversation:\n\n"
            + "\n".join(transcript)
            + "\n\nCurrent user message:\n\n"
            + message
        )

    else:

        prompt = message

    return run_agent(prompt)


demo = gr.ChatInterface(
    fn=chat,
    title="🇬🇧 UK Housing & Renting Assistant",
    description=(
        "Ask about renting, landlords, deposits, repairs, "
        "eviction, tenancy agreements and housing problems. "
        "English or Hinglish is welcome."
    ),
    examples=[
        "Mera landlord rent increase kar raha hai, kya wo kar sakta hai?",
        "My landlord hasn't returned my deposit. What can I do?",
        "Flat mein mould hai aur landlord repair nahi kar raha.",
        "Landlord ne bola hai 2 months mein ghar khaali karo. Kya mere rights hain?",
        "How do I check whether my deposit is protected?",
    ],
)


if __name__ == "__main__":
    demo.launch()