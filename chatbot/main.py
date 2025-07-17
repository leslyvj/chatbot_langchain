import streamlit as st
from langchain_community.llms import Cohere
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
import os

load_dotenv()
os.environ["COHERE_API_KEY"] = os.getenv("COHERE_API_KEY")


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
