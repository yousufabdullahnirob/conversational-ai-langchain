import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = "AIzaSyAxcfimTQlqiD9hAyvOKcbvKkt0pTYxEWo"
client = genai.Client(api_key=api_key)

print("Models supporting 'generateContent':")

try:
    for model in client.models.list():
        # Check if generateContent is in supported_actions
        # In the new SDK, supported_actions might be a list of strings
        actions = getattr(model, 'supported_actions', [])
        if 'generateContent' in actions:
            print(f"- {model.name}")
except Exception as e:
    print(f"Error: {e}")
