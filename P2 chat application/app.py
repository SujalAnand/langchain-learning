import os
import streamlit as st
from langchain_openai import ChatOpenAI

#Add an API key below to successfuly run the project
os.environ["OPENAI_API_KEY"] = ""

#App UI starts here
st.set_page_config(page_title="Chatbot demo", page_icon=":robot:")
st.header("You:")

def get_input():
    text_input = st.text_input("You:", key=input)
    return text_input

if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages = [
        ("system", "You are a helpful assistant")
    ]

def get_answer(user_input):
    llm = ChatOpenAI(
        model="gpt-3.5-turbo-0125",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    st.session_state.sessionMessages.append(("human", user_input))
    ai_msg = llm.invoke(st.session_state.sessionMessages)
    st.session_state.sessionMessages.append(("ai", ai_msg.content))
    return ai_msg.content

user_input = get_input()
Submit = st.button("Generate")

if Submit:
    st.subheader("Answer:")
    st.write(get_answer(user_input))