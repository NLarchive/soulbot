import logging
import google.generativeai as palm

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GoogleLLM:
    def __init__(self, api_key, model_name="gemini-pro"):
        palm.configure(api_key=api_key)
        self.model_name = model_name
        self.model = palm.GenerativeModel(self.model_name)

    def _call(self, prompt, stop=None, **kwargs):
        logger.info(f"Prompt: {prompt}")
        try:
            completion = self.model.generate_content(prompt, stop_sequences=stop, **kwargs)
            return completion.result
        except Exception as e:
            logger.error(f"Error generating content: {e}")
            return f"Error: {e}"

    @property
    def _llm_type(self):
        return "google_generative_ai_llm"
    
    @property
    def _identifying_params(self):
        return {"api_key": "REDACTED"} # Replace with a real redaction mechanism if needed