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

1. **Create a Virtual Environment**
    
    ```bash 
    virtualenv ~/Chatbot_Langchain
    source ~/Chatbot_Langchain/bin/activate

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt

3. **Download and Install Ollama**

In order to use open source llms locally, this app uses [Ollama](https://ollama.com/), a tool for running large language models locally.

    ```bash
    curl -fsSL https://ollama.com/install.sh | sh

4. **Download LLMs** 

    ```bash
    ollama pull llama3
    ollama pull gemma
    ollama pull deepseek-v2

## ▶️ Start application 

5. **Run**
    ```bash
    streamlit run app.py
