from turtle import st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.outputs import StrOutputParser
from langhchain_community.llms import Ollama


from streamlit as st
import os   
from dotenv import load_dotenv

load_dotenv()


#os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY","your_openai_api_key_here")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

Prompt= ChatPromptTemplate.from_messages(
    [("system", "You are a helpful assistant."),
     ("user", "Question: {question}")] 
) 

st.title("Chatbot with LangChain and OpenAI")
question = st.text_input("Ask a question:")

llm=Ollama(model="llama2")
output_parser = StrOutputParser()
chain = Prompt | llm | output_parser
