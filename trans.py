import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
import google.generativeai as genai

# 🔐 Set Gemini API key directly in the code (Not recommended for production)
GEMINI_API_KEY = "AIzaSyBOvPpqgx3FifXFlFzuPKzQEZJ_gNH14L8"  # Replace with your real API key
genai.configure(api_key=GEMINI_API_KEY)

# 🌍 Create Gemini LLM via LangChain
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3,google_api_key=GEMINI_API_KEY)

# 🧠 Define a prompt template with system & user messages
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a translation assistant. Translate the following English sentence to French."),
    ("user", "{text}")
])

# 🔗 Chain the prompt and the model
chain: Runnable = prompt | llm

# 🚀 Streamlit UI
st.set_page_config(page_title="English to French Translator", page_icon="🌍")
st.title("🌍 English to French Translator")
st.markdown("Translate your English sentence into French using Google Gemini.")

# ✏️ User input
english_text = st.text_input("Enter an English sentence:")

# 🔘 Button to trigger translation
if st.button("Translate"):
    if english_text.strip() == "":
        st.warning("Please enter a sentence to translate.")
    else:
        try:
            # Run the chain with input
            result = chain.invoke({"text": english_text})
            # Show result
            st.success("✅ Translation complete!")
            st.markdown(f"**French Translation:**\n\n> {result.content}")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")