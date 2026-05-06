import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error" 
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

print("Connecting to Llama-3 via Hugging Face... (Type 'exit' to stop)")

try:
    # Initialize the Hugging Face Endpoint
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
    )

    # Wrap it in ChatHuggingFace
    chat_model = ChatHuggingFace(llm=llm)

    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break
            
        if not user_input.strip():
            continue

        response = chat_model.invoke(user_input)
        
        print("\nLlama:")
        print(response.content)

except Exception as e:
    print(f"\nAn error occurred: {e}")
