import streamlit as st
from langchain.llms import HuggingFaceHub
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = ""

#App UI starts here
st.set_page_config(page_title="LangChain Intro", page_icon=":robot:")
st.header("LangChain Demo")

def get_input():
    input_text = st.text_input("You: ", key="input")
    return input_text

def get_response(query):    
    llm = HuggingFaceHub(repo_id="google/flan-t5-large")
    response = llm(query)
    return response

user_input = get_input()
Submit = st.button("Generate")

#if user click on submit button
if Submit:
    st.subheader("Answer:")
    st.write(get_response(user_input))


