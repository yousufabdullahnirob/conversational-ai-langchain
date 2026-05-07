# Conversational AI with LangChain & Google Gemini

This repository contains a series of Python scripts demonstrating how to build intelligent, context-aware chatbots using the **LangChain** framework and **Google Gemini** models.

## 🚀 Features
- **Interactive Chatbots:** Simple and advanced chatbot implementations.
- **Context Management:** Utilizing `MessagesPlaceholder` and chat history from local files.
- **Dynamic Prompting:** Using `ChatPromptTemplate` for reusable and flexible prompts.
- **Clean Output:** Configured to provide plain text responses, avoiding Markdown/LaTeX formatting for terminal use.

## 📂 Project Structure
- `chatbot.py`: A basic interactive chatbot.
- `message.py`: Demonstrates message handling using `HumanMessage` and `AIMessage`.
- `Chat_prompt_templete.py`: Dynamic prompt generation based on user inputs.
- `Message_placeholder.py`: A sophisticated chatbot that maintains conversation context.

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yousufabdullahnirob/conversational-ai-langchain.git
cd conversational-ai-langchain
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# Activate on Windows:
.\venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install langchain-google-genai langchain-core python-dotenv
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your Google API Key:
```env
GOOGLE_API_KEY=your_api_key_here
```

### 5. Run the scripts
```bash
python Message_placeholder.py
```

## 🛡️ License
MIT License
