from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import re

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")


chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful expert. Provide responses in plain text only. Do not use Markdown or bold text (**)."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{user_input}")
])


def load_chat_history(file_path):
    history = []
    try:
        with open(file_path, "r") as f:
            for line in f:
                human_match = re.search(r'HumanMessage\(content="(.+?)"\)', line)
                ai_match = re.search(r'AIMessage\(content="(.+?)"\)', line)
                if human_match:
                    history.append(HumanMessage(content=human_match.group(1)))
                elif ai_match:
                    history.append(AIMessage(content=ai_match.group(1)))
    except FileNotFoundError:
        pass
    return history


chat_history = load_chat_history("chathistorytwxt.txt")

print("Chatbot is ready! (Type 'exit' to stop)")

while True:
    user_query = input("\nYou: ")
    if user_query.lower() == "exit":
        break

   
    prompt = chat_template.invoke(
        {
            "chat_history": chat_history,
            "user_input": user_query
        }
    )

    response = model.invoke(prompt)


    if isinstance(response.content, list):
        content = "".join([block.get("text", "") if isinstance(block, dict) else str(block) for block in response.content])
    else:
        content = response.content

    print(f"AI: {content}")

  
    chat_history.append(HumanMessage(content=user_query))
    chat_history.append(AIMessage(content=content))
