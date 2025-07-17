import streamlit as st
from langchain_community.llms import Cohere
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

# Load .env if needed
load_dotenv()

# ✅ Set your Cohere API key securely
COHERE_API_KEY=your_api_key_here

# 🔧 Streamlit app title
st.title("Chatbot with LangChain and Cohere")

# 🔧 Input field
question = st.text_input("Ask a question:")

# 🔧 Define prompt template
Prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful assistant."),
     ("user", "Question: {question}")]
)

# 🔧 Initialize Cohere LLM via LangChain
llm = Cohere(model="command-r")  # or another Cohere model if desired

# 🔧 Output parser for clean string outputs
output_parser = StrOutputParser()

# 🔧 Create the chain
chain = Prompt | llm | output_parser

# 🔧 Run the chain if user inputs a question
if question:
    response = chain.invoke({"question": question})
    st.write(response)
