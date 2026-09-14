import gradio as gr
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# AI generation functio
def generate_plan(user_info, plan_type):
    if not user_info.strip():
        return "Please provide your health details."

    prompt = ""
    if plan_type == "Daily Diet Plan":
        prompt = f"Create a healthy daily meal plan for a person with the following details:\n{user_info}\nMake it realistic, balanced, and easy to follow."
    elif plan_type == "Weekly Workout Plan":
        prompt = f"Create a 7-day workout plan for a person with the following details:\n{user_info}\nMake it practical and beginner-friendly."

    try:
        response = client.responses.create(
            model="gpt-4o",
            input=[{"role": "user", "content": prompt}],
            max_output_tokens=500
        )
        return response.output_text.strip()
    except Exception as e:
        return f"Error generating {plan_type}: {e}"

# Process function
def process(user_info, plan_type, uploaded_file):
    # If a file is uploaded, read it
    if uploaded_file:
        try:
            with open(uploaded_file, "r", encoding="utf-8", errors="ignore") as f:
                user_info = f.read()
        except Exception as e:
            return f"Error reading uploaded file: {e}"

    return generate_plan(user_info, plan_type)

# Build UI
with gr.Blocks(theme=gr.themes.Soft(), css="""
    body {background: linear-gradient(135deg, #56ab2f, #a8e063);}
    .gradio-container {max-width: 700px; margin: auto;}
    .output-card {
        background: rgba(255, 255, 255, 0.15);
        padding: 15px;
        border-radius: 15px;
        color: white;
        font-size: 16px;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 30px rgba(0,0,0,0.1);
        white-space: pre-wrap;
    }
""") as demo:

    gr.Markdown(
        "<h1 style='text-align:center;color:white;'>🥗 AI Health & Diet Planner</h1>"
        "<p style='text-align:center;color:white;'>Enter your health details or upload a file to get a custom diet or workout plan.</p>"
    )

    with gr.Row():
        user_info = gr.Textbox(label="Enter Health Details", placeholder="Example: 28 years old, 70kg, 175cm, goal: lose 5kg in 2 months")
        plan_type = gr.Radio(["Daily Diet Plan", "Weekly Workout Plan"], label="Select Plan", value="Daily Diet Plan")

    uploaded_file = gr.File(label="Upload Health Notes (TXT)", type="filepath")

    generate_btn = gr.Button("Generate Plan")
    output_box = gr.Markdown(elem_classes="output-card")

    generate_btn.click(fn=process, inputs=[user_info, plan_type, uploaded_file], outputs=output_box)

# Run app
if __name__ == "__main__":
    demo.launch(share=True)
