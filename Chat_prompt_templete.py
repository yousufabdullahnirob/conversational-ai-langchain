from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {user_input} expert. Provide responses in plain text only. Do not use Markdown, bold text (**), or LaTeX formatting."),
    ("human", "Explain in simple words in {language} {explanation_for} topic")
])

    

user_expert_type = input("Expert Type (e.g. programming, science): ")
target_language = input("Language (e.g. bangla, english): ")
topic_name = input("Explain what topic?: ")

prompt = prompt_template.invoke(
    {
        "user_input": user_expert_type,
        "language": target_language,
        "explanation_for": topic_name
    }
)

print("--- Generated Prompt ---")
print(prompt)

print("\n--- AI Response ---")

response = model.invoke(prompt)

if isinstance(response.content, list):
   
    content = "".join([block.get("text", "") if isinstance(block, dict) else str(block) for block in response.content])
else:
    content = response.content

print(content)