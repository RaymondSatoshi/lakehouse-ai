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

with st.sidebar:
    question = st.text_input("Question", value="", max_chars=None, key=None, type="default")
    if question:
        st.session_state["MESSAGE"].append(HumanMessage(content=question))
        response = chat([HumanMessage(content=question)])
        st.session_state["MESSAGE"].append(response)
        st.markdown(response.content)
    # if response.content:
    #     st.markdown(response.content)

# with st.sidebar:
#     question = st.text_input("Question", value="", max_chars=None, key=None, type="default")
#     if question:
#         response = chat([HumanMessage(content=question)])
#         st.write(response.content)
    
