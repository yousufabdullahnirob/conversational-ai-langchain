from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

# Initialize the LLM
# Ensure you have GOOGLE_API_KEY in your .env file
llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

st.header('Research tools')
user_input = st.text_input('Ask a question')

if st.button('Get Answer'):
    if user_input:
        try:
            response = llm.invoke(user_input)
            
            # Handle cases where response.content is a list of content blocks
            if isinstance(response.content, list):
                final_text = ""
                for block in response.content:
                    if isinstance(block, dict) and 'text' in block:
                        final_text += block['text']
                    elif isinstance(block, str):
                        final_text += block
                st.markdown(final_text)
            else:
                st.markdown(response.content)
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question.")