import gradio as gr
from typing import List, Dict
# Assuming these are defined elsewhere in your project
from google_llm import GoogleLLM  # Replace with your actual import
from personality_data import big_five_traits, mbti_types, disc_types, enneagram_types, sei_traits # Replace with your actual import
from api_key_utils import get_google_api_key # Replace with your actual import

# Placeholder for API key retrieval
api_key = get_google_api_key()
llm = GoogleLLM(api_key=api_key)


def generate_response(personality_traits: Dict[str, float], scenario: str) -> str:
    """Generates a response based on personality traits and a scenario."""
    trait_string = ", ".join([f"{trait}:{value}" for trait, value in personality_traits.items()])
    prompt = f"A person with the following personality traits: {trait_string} is in the following scenario: {scenario}. How would this person respond?"
    response = llm.generate_text(prompt)
    return response

def update_description(trait):
  # Replace with actual descriptions
  descriptions = {
      "Openness": "Openness to experience.",
      "Conscientiousness": "Conscientiousness description.",
      "Extraversion": "Extraversion description.",
      "Agreeableness": "Agreeableness description.",
      "Neuroticism": "Neuroticism description.",
      # Add other trait descriptions...
  }
  return descriptions.get(trait, "No description available.")


with gr.Blocks(css=".gradio-container {background-color: #f0f0f0;}") as demo:
    gr.Markdown("<h1>AI Personality Chatbot</h1>")

    with gr.Tab("Big Five"):
        big_five_sliders = {}
        for trait in big_five_traits:
            big_five_sliders[trait] = gr.Slider(minimum=0, maximum=100, step=1, label=trait, value=50)
        big_five_description = gr.Textbox(label="Trait Description")
        for trait, slider in big_five_sliders.items():
            slider.change(fn=update_description, inputs=trait, outputs=big_five_description)

    # ... (Add similar tabs for MBTI, DISC, Enneagram, SEI using dropdowns)

    scenario_input = gr.Textbox(label="Scenario", placeholder="Enter a scenario")
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")


    def respond(message, chat_history):
        bot_message = generate_response(big_five_sliders, message)
        chat_history.append((message, bot_message))
        return "", chat_history


    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)


demo.launch()