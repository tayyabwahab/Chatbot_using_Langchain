

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os 

################# For Langsmith Tracking ############
# from dotenv import load_dotenv
# load_dotenv()
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"] = 'true'

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a assistant. Provide response to the user queries."),
        ("user", "Question:{question}")
    ]
)

st.title("Chatbot for Q&A")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Dropdown for model selection
model_name = st.selectbox("Choose a model", ["llama3", "gemma3", "deepseek-v2"])

# Set up the LLM based on the selected model
llm = Ollama(model=model_name)
output = StrOutputParser()
chain = prompt | llm | output

# Input form at the bottom
with st.form(key="input_form"):
    input_text = st.text_input("Search the topic you want", key="input")
    submitted = st.form_submit_button("Submit")

# Immediately show the latest response if just submitted
latest_response = None
if submitted and input_text:
    latest_response = chain.invoke({'question': input_text})
    st.session_state.chat_history.append({"question": input_text, "answer": latest_response})

# Display chat history at the top, including the most recent response if any
for idx, message in enumerate(st.session_state.chat_history):
    st.markdown(f"---\n<span style='font-size: 28px; font-weight: bold;'>Q{idx+1}: {message['question']}</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='font-size: 16px;'>A{idx+1}: {message['answer']}</span>\n--", unsafe_allow_html=True)

# If latest response wasn't rendered yet (due to Streamlit rerun timing), show it here
if latest_response and not st.session_state.chat_history[-1].get("displayed"):
    st.session_state.chat_history[-1]["displayed"] = True
    print("Answered")

