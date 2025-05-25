# Q&A Chatbot using LangChain and Streamlit

This project is a simple web-based chatbot application built using [Streamlit](https://streamlit.io/) and [LangChain](https://www.langchain.com/) for Q&A. It allows users to ask any kind of questions and receive answers using one of the selected large language models. The application runs 100% locally and involved only open source llms. 

## 🔍 Features

- Choose between three LLMs: `llama3`, `gemma3`, and `deepseek-v2`.
- Submit a Query.
- Answer questions from any field.
- Keep record of all answers in the sesssion. 

## 🚀 Technologies

- **LangChain** for chaining prompts and model calls.
- **Ollama** as the backend LLM wrapper.
- **Streamlit** for the web app interface.
- **Python-dotenv** for environment variable management (Optional for Langsmith Tracking).

## 📦 Setup Instructions

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt

2. **Download LLMs** 

    ```bash
    ollama pull llama3
    ollama pull gemma:2b
    ollama pull deepseek-v2

