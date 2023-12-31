from main import config, agent
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)

config.init()

if st.session_state["OPENAI_API_KEY"]:
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"])
else:
    chat = None

# st.set_page_config(page_title="Lakehouse-ai", layout="wide")
st.title("TalkWithLakehouse")

if not chat: st.warning("plz set your key in the config page") 

with st.container():
    question = st.chat_input("Type Something...")
    # question = st.text_input("Question", value="", max_chars=None, key=None, type="default")
    # ask = st.button("Ask")
    if question:
        st.session_state["MESSAGE"].append(HumanMessage(content=question))
        response = agent.get_result_from_query(question)
        st.session_state["MESSAGE"].append(AIMessage(content=response))

    for message in st.session_state["MESSAGE"]:
        if isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(message.content)
        else:
            with st.chat_message("user"):
                st.markdown(message.content)