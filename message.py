from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai.chat_models import _parse_chat_history
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

chat_history=[
    SystemMessage(content="Provide responses in plain text only. Do not use Markdown or LaTeX formatting.")
]

while True:
    user_input = input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
        
    try:
        result = model.invoke(chat_history)
        chat_history.append(AIMessage(content=result.content))
        
        # Extract content if it's a list of blocks
        if isinstance(result.content, list):
            content = "".join([block.get("text", "") if isinstance(block, dict) else str(block) for block in result.content])
        else:
            content = result.content
            
        print("NTS:", content)
    except Exception as e:
        print(f"Error: {e}")

print("\n--- Conversation Summary ---")
for msg in chat_history:
    if isinstance(msg, HumanMessage):
        print(f"Human: {msg.content}")
    elif isinstance(msg, AIMessage):
        print(f"AI: {msg.content}")
print("---------------------------")