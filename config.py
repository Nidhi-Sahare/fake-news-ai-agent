from google import genai
import time
GEMINI_API_KEY = ""
client = genai.Client(api_key=GEMINI_API_KEY)
MODEL_PRIORITY = ["gemini-2.0-flash","gemini-flash-latest"]
def get_model_response(prompt: str):
    last_error = None
    for model in MODEL_PRIORITY:
        try:
            response = client.models.generate_content(model=model,contents=prompt)
            return response.text

        except Exception as e:
            last_error = e
            time.sleep(1)
    raise last_error