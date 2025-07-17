import streamlit as st
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Streamlit app title
st.title("Chatbot with LangChain and Ollama (LLaMA2)")

# Input field
question = st.text_input("Ask a question:")

# Define prompt template
Prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful assistant."),
     ("user", "Question: {question}")]
)

# Initialize Ollama LLM
llm = Ollama(model="llama2")

# Output parser
output_parser = StrOutputParser()

# Create the chain
chain = Prompt | llm | output_parser

# Process input
if question:
    response = chain.invoke({"question": question})
    st.write(response)
