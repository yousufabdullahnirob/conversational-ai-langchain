import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# The client gets the API key from the environment variable
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("Error: API Key not found. Please add GEMINI_API_KEY or GOOGLE_API_KEY to your .env file.")
    exit(1)

# Initialize the Google GenAI client
client = genai.Client(api_key=api_key)

print("Connecting to Gemini via new SDK...")

try:
    response = client.models.generate_content(
        model="gemini-3-flash-preview", 
        contents="Explain how AI works in a few words"
    )
    print("\nGemini Response:")
    print(response.text)
except Exception as e:
    print(f"\nAn error occurred: {e}")
