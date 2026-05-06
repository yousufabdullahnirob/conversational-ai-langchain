import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error" # Suppress harmless transformers warnings
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Gemini model using LangChain
# It will automatically find GOOGLE_API_KEY from .env
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.7,
)

print("Connecting to Gemini via LangChain...")

try:
    response = llm.invoke("Explain how AI works in a few words")
    
    print("\nGemini Response:")
    if isinstance(response.content, list):
        for item in response.content:
            if isinstance(item, dict) and 'text' in item:
                print(item['text'])
            else:
                print(item)
    else:
        print(response.content)
except Exception as e:
    print(f"\nAn error occurred: {e}")